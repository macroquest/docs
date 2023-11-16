# How to use Actors

Actors are a subsystem added to the MQ ecosystem to allow for different clients and applications to communicate with one another simply. The underlying tech for local (same computer) communication is Windows Named Pipes, and is very fast -- essentially no different than just using shared memory. The tech for remote communication is still WIP and is currently planned to be ASIO-based TCP communication with a UDP discovery mechanism and the ability to specify peers.

The entire system hinges on the launcher (MacroQuest.exe) being present as the central routing mechanism. If the launcher goes down, then all routing will stop and the system will become inoperable.

While messaging can use any serialization for internal mailbox communication, protobuf has been utilized to wrap these messages in routing packages to allow for system-independent communication, implicit versioning, and efficient marshalling/unmarshalling. When selecting a serialization strategy, be aware that there are protobuf examples in code and you are probably already building the library.

The point of using this technology is to allow for consistent and simple communication between processes that couldn't communicate before. The framework is ideally highly extensible with a minimum amount of boilerplate needed to set up, feedback is welcome.

## Terminology

- **Actor**: An actor is self-contained computational entity that receives messages and performs actions based on the content of those messages such as side effects and composing replies.
- **Mailbox**: This is the receiver of messages. Each actor has exactly one, and this provides the unique address for said actor. A mailbox is set up by taking a callback function to process a message.
- **Dropbox**: This is the sender of messages. Each actor again has exactly one, and this provides automatic return address composition as well as an interface to the application's central Post Office.
- **Post Office**: The central authority for message routing in a single application. Each independent application will need to set one post office up for actors in that application to register mailboxes. This will maintain ownership of the mailboxes and dropboxes and route all messages received by the application.
- **Address**: A specifier for routing a message. On the sending side, this does not have to be unique -- one could address a message to all applications that have a certain mailbox, for instance. There are two levels of addressing: mailbox, and postoffice. On the receiving side, the post office must be fully qualified with one of three strategies:
    - By name: You can specify a unique name for an application, which is useful for external application naming. There is one name-specified application that should always be present: `launcher` -- the MQ launcher
    - By pid: You can use the PID of the application (not very useful to the sender as it is not deterministic)
    - By EQ information: The most available of the following three strings: account, server, character. All three of these strings present means that the address must be unique, and this type of addressing replaces name as a convenience mechanism.
- **Envelope**: This is a protobuf spec that all messages that need to be routed to actors will get wrapped in automatically (as a function of using the Dropbox) so the routing system can ensure it ends up at the correct post offices and mailboxes.

## In Plugins

Plugins are a special case for the actor API as the post office itself is maintained within mq2main.dll and is not exposed at all to any plugins. Instead, plugins will have access to an actor API by including:

```cpp
#include "mq/api/ActorAPI.h"
```

This include provides everything necessary for creating and registering an actor, as well as sending (and receiving) messages. There is one free function (with two overloads) provided as part of this API:

### AddActor

```cpp
using ReceiveCallbackAPI = std::function<void(Message&&)>;

DropboxAPI AddActor(const char* localAddress, ReceiveCallbackAPI&& receive);
DropboxAPI AddActor(ReceiveCallbackAPI&& receive);
```

Both of these functions return a `DropboxAPI` object, which serves as the interface to the dropbox functionality needed to operate the actor. If a `localAddress` is not specified, then the canonical name of the plugin is used as the mailbox name (convenient for when you only need one mailbox in a plugin, which should be pretty common).

An important implementation detail is that mailbox names are mutated when they are set to ensure that they are unique in the post office. The `localAddress` specified is the mailbox name *local to the plugin* and not the full mailbox name that is stored in the mailbox. This registration function will prepend the mailbox with the canonical plugin name followed by a colon like so: `myplugin:mymailbox`. This is only important to the plugin author if they need to send messages to mailboxes outside their plugin, otherwise the send functions will handle this implementation detail opaquely.

There are three more structures to explore in a plugin, `Address`, `Message`, and `DropboxAPI`.

### Address

An address is a shim to the protobuf-defined address, and follows the same rules as the [terminology section above](#terminology). The API provides this shim as a simple struct where you can set the address parameters directly like this (as an example):

```cpp
postoffice::Address addr;
addr.Server = "test";
addr.Character = "target";
```

The one difference to note is that there is a member of this address called `AbsoluteMailbox`. If this is set to true, then all values of the address are passed as-is without any modification, useful only for sending messages to actors that are created outside the plugin. Otherwise, the mailbox name follows these rules:

- If no mailbox is specified at all, then the plugin name becomes the target mailbox.
- If a mailbox is specified, then the target mailbox becomes `<pluginName>:<mailbox>` as was noted in [the implementation details specified in `AddActor`](#addactor)

### Message

A message consists of 2 parts useful to the plugin author, `Sender` and `Payload`. Both are optional (and are wrapped in `std::optional`), so the author will need to handle the absence of either.

- `Sender`: This is the address of the message sender. It's useful if message handling is dependent on the source of the message.
- `Payload`: This is the actual message payload. It is represented as a string, which is a convenient data storage mechanism that provides bytes and length, and is deserializable directly as a protobuf message. It could be any data that your plugin can handle though, since the handling of it is local to your plugin.

### DropboxAPI

This is the object that is returned when an actor is added to the postoffice via the API. The plugin author should store this somewhere where it can be accessed because they will need to use it to send messages and unregister the actor. The object provides the following functions:

- `Post(address, messageId, data, callback)`: Send a message to an address. The `messageId` is a message identifier the target will understand and can be used in message handling, and `data` is what you want to send. `callback` is a to be used to handle a response to the message sent; setting this parameter (to something other than `nullptr`) will send a message that expects a response, and will send back an error status if none is received. There is a convenience overload that allow you to specify a protobuf object as data, otherwise you will need to provide the data as a string. The id will need to be convertible to `uint16_t` -- using an `enum` is a good choice for that.
- `PostReply(message, messageId, data, status)`: This is a method mostly to be used in message handling. Note that the message needs to be **moved** into this response. `messageId` and `data` are as above, and `status` is a convenience 8-bit parameter that defaults to 0 that some actors expect as a response (mostly used as error codes).
- `Remove()`: Remove the actor from the post office. Will unregister the actor, clean up the internal dropbox, and will ensure that any further use of the `DropboxAPI` does nothing.
