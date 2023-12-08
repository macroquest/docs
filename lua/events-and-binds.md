---
tags:
    - lua
---
# Lua Events and Binds

Events and binds are very similar to their macro counterparts, but use the fact that Lua functions are first class
to allow you to simply specify callback functions that will process events and binds when they get processed.
The callbacks will require a specific signature to work, so this page is here to document how to use callbacks.

### Lua Events

When you set up an event, you call `mq.event('name', 'matcher text', callback)`. The name is just a string to
identify the event with so you can remove it later with `mq.unevent('name')` if the event is no longer necessary.
The matcher text is the same matcher text that everyone is used to from macro events, where `#*#` is an uncaptured
wildcard and `#1#` is a captured wildcard that will be the first argument. More arguments are similarly captured,
so you can specify the argument order in a callback. 

The callback is the important feature of Lua. It expects a function with a signature of `(line, arg1, arg2, etc)`
that will process the text of the event (the full matched line and the captured arguments, ordered by number).
A simple example would look like this:

```lua
local function callback(line, arg1, arg2)
    print(arg1)
    print(arg2)
end

mq.event('mysay', '#1# says, #2#', callback)
```

Finally, events will not automatically process (much like in the macro language) -- you will have to call `mq.doevents()` when it makes sense in your lua script to process the queue of captured events:

```lua
while not terminate
do
    mq.doevents()
    mq.delay(1) -- just yield the frame every loop
end
```


### Lua Binds

Binds are very similar to events (and even use the same backend code) with a couple of important differences.
Instead of capturing arbitrary text, it will pass arguments specified by the user, and it will execute at the
beginning of the next frame always (no need to call `mq.doevents()`). When you set up a bind, you call
`mq.bind('/command', callback)`. The command is simultaneously what the user will input to call the bind, and
what the bind is indexed by to unbind with `mq.unbind('/command')` when you no longer want the bind to
function while your script is running.

The callback now has a function signature of `(arg1, arg2, etc)`. A simple example would look like this:

```lua
local callback = function (...)
    local args = {...}
    local str = ''
    for i = 1, #args, 1 do
        if i > 1 then
            str = str .. ' '
        end
        str = str .. args[i]
    end
    print(str)
end

mq.bind('/myecho', callback)
```

That's all that is required to implement an echo command.
