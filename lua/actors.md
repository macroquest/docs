# Actors in Lua

The lua plugin has been equipped with a method to utilize the actor subsystem of MQ. This system will allow script writers to communicate between scripts, clients, or even external applications using the same framework that is available [to plugins](../plugins/developing/actors.md). There are some few specializations unique to lua, and this document aims to provide a reference for them. Please refer to the [terminology section](../plugins/developing/actors.md#terminology) in the other actors document for a glossary of terms.

## Module

The module is loaded by requiring `actors`. This module has a method `register` for creating actors, and a method `send` for sending anonymous messages to actors. Both of these methods provide overloads for various use cases:

```lua
local actors = require('actors')

-- create an actor for the script -- the actor is addressed using script
local script_actor = actors.register(function (message) ... end)

-- create an actor with a mailbox name -- the actor is addressed using script and mailbox
local actor = actors.register('myactor', function (message) ... end)

local payload = {test='payload'}

-- send a simple message to script_actor across all clients
actors.send(payload)

-- send a simple message to a specific address
actors.send({mailbox='targetmailbox'}, payload)

-- send a response message to script_actor across all clients (this will fail if any other client is running the same script)
actors.send(payload, function (status, message) ... end)

-- send a response message to a specific address
actors.send({character='charname', mailbox='targetmailbox'}, payload, function (status, message) ... end)
```

There are some things to notice about these functions that are essential for understanding how actors function. These will be addressed in the following sections: [What Goes in a Message](#what-goes-in-a-message), [Addressing](#addressing), [Message Handler](#message-handler), and [Response Callbacks](#response-callbacks)

## What Goes in a Message

Before we get to the register functions and the message handler, let's look at what a message is. In general, a message can contain any native lua primitive or a lua table. Different types can be added to the serialization in the plugin if they are required, so please open feature requests if there are types that need to be added. **MacroQuest datatypes can not be serialized because they are localized to the eqgame client.** In the example above, the payload is the message content, and is simple a table with a single named string entry. This could be arbitrarily complex and nested tables will serialize as well, any type in the table that can't be serialized will simply be ignored.

## Addressing

Next, we want to see what goes into an address. An address in lua can also be referred to as a header, and is a table that can optionally contain the following entries:

```lua
{
    mailbox='', -- the target mailbox name for an actor
    absolute_mailbox=false, -- if you want to provide the fully-qualified mailbox name, set this to true
    script='', -- the target script for an actor, which is a qualifier to mailbox names to gurantee uniqueness
    pid=0, -- an unsigned integer value for Windows PID. This won't likely be available, but it could be used to direct a message to a specific client
    name='', -- a name of a standalone actor client, like 'launcher' -- used to direct messages to external applications
    account='', -- the name of the target client's account
    server='', -- the name of the target client's server shortname
    character='', -- the name of the target client's character
}
```

All of these entries are completely optional, and can be ambiguous if you want to send messages to multiple clients. If mailbox and script are not specified, then the target is assumed to be the current actor's mailbox (or just script if sent anonymously). Everything else can be used to disambiguate.

## Message Handler

Now we get to the meat of the actors, the message handler. The function that is specified when you register an actor is what is called a "message handler". The function takes a message and returns nothing, to be used to handle incoming messages as you receive them. **Delay will not work in the message handler and will throw a script error.** The typical message handler would look something like this:

```lua
local function handler(message)
    if message.content.id == 'something' then
        ...
    elseif message.content.id == 'somethingelse' then
        ...
    end
end
```

In this example, `id` is something that the script writer provided in the message table, but `content` is provided by the plugin.

### Message Structure

The plugin passes the message into the handler with some specific structure, as follows:

- `content`: the actual data that was serialized from the sending side, following the rules for [what goes in a message](#what-goes-in-a-message).
- `reply`: a method used to reply to messages that have specified a [response callback](#response-callbacks). This has two overloads: `function(content)` and `function(status, content)`, where `content` is any message as before, and `status` is an integer status (defaults to 0 in the first overload).
- `sender`: the [Address](#addressing) of the sender, fully qualified.
- `send`: a method similar to reply, but is used for cases where the message doesn't have a response callback and you just want to send a message back to the sender for it to go through their message handler.

## Response Callbacks

A response callback is similar to a message handler, but has an additional argument for `status`, which is just an integer value indicating response status. And important thing to consider is that these response messages will *not* be routed through your message handler, but will instead be routed directly through the response callback specified. The message is the same as [in the message handler](#message-structure), so the only additional information needed for the callback is status. Typically, negative values indicate some kind of failure and should be handled, while positive values indicate something meaningful with 0 being the nominal "acknowledge" status. The follow enums are provided as they are errors that can happen external to the lua plugin:

```lua
actors.ResponseStatus.ConnectionClosed = -1
actors.ResponseStatus.NoConnection = -2
actors.ResponseStatus.RoutingFailed = -3
actors.ResponseStatus.AmbiguousRecipient = -4
```

Of these, only the last two are something that you would have any control over in lua. `RoutingFailed` would happen if there is no recipient at the given [address](#addressing) specified (like if you tried to address a specific character that was no longer logged in). `AmbiguousRecipient` would happen if there was too much ambiguity in the address (like if you addressed an entire server). This is important because these are RPC-style messages, and the requirement is that exactly 1 recipient will receive the message, or we wouldn't be able to provide the guarantee that you will get a response. If you need to send a response to a multi-recipient message, then just use `message.send` to do so, and handle the responses in the message handler.
