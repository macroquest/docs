# Improved Spawn Search

## Introduction to getFilteredSpawns and getAllSpawns
The functions `getFilteredSpawns` and `getAllSpawns`are available as part of the Macroquest Lua bindings. They provide a sensible manner in which to retrieve and filter `spawn` objects for your scripts and then return the results in a native Lua table, making it painless for you to iterate through, sort or even further filter in your Lua scripts.

## getFilteredSpawns
`getFilteredSpawns` is a Lua function that takes an optional predicate argument, which is a Lua function that can be used to filter the list of `spawn` objects. If the predicate argument is provided, the function iterates over all `spawn` objects and applies the predicate function to each one. If the predicate function returns true for a given `spawn` object, that object is added to a Lua table that is ultimately returned by the function.

### How to use getFilteredSpawns
Here's an example of how to use getFilteredSpawns:
```lua
local mq = require('mq')

-- Define a predicate function that checks if the spawn is an NPC
local function isNPC(spawn)
    return spawn.Type() == 'NPC'
end

-- Call getFilteredSpawns with the predicate function
local npcs = mq.getFilteredSpawns(isNPC)
```
In this example, we define an `isNPC` function that checks whether a given `spawn` object is of the type NPC (the type method return value equals the string "NPC").  This predicate is passed as the single argument to `getFilteredSpawns` function to retrieve a table of all `spawn` objects that meet this filtering criteria.

### Inline predicate function
It is also possible to write the predicate and call to `getFilteredSpawns` together by in-lining the predicate function as part of the call.  This is sometimes more convienant when the preciate check is simple and easily understood.  Here is the above example condensed into a single line.

```lua
local mq = require('mq')

-- Call getFilteredSpawns with an inline predicate function
local npcs = getFilteredSpawns(function(spanw) return spawn.Type() == 'NPC' end)
```

## getAllSpawns
`getAllSpawns` is another Lua function that retrieves all `spawn` objects and returns them as a Lua table. It does not take a predicate, and by default returns all spawns in the zone in a Lua table.

### How to use getAllSpawns
Here's an example of how to use getAllSpawns:
```lua
local mq = require('mq')

-- Call getAllSpawns to retrieve a table of all `spawn` objects in the zone
local allSpawns = getAllSpawns()
```
In this example, we call getAllSpawns to retrieve a table of all `spawn` objects in the zone.