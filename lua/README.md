# Lua Scripting in MacroQuest

Lua is in general a robust language with a multitude of tutorials and resources widely available:

- [Main Lua Page](https://www.lua.org/home.html) with getting started and documentation
- [Programming in Lua](https://www.lua.org/pil/contents.html)
- [Tutorials Point](https://www.tutorialspoint.com/lua/index.htm)
- [mq-defs VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ZenithCodeForge.mq-defs) [source](https://github.com/macroquest/mq-definitions)

I won't cover language conventions or features, just mention that mq2lua is built on **LuaJIT 2.0.5** if you need to know the specific flavor.

### Command Reference

```plaintext
/lua [COMMAND] {OPTIONS}
MQ2Lua: A lua script binding plugin.

run -- run lua script from file location
parse -- parse a lua string with an available mq namespace
stop -- stop one or all running lua scripts
pause -- pause one or all running lua scripts
conf -- set or view configuration variable
reloadconf -- reload configuration
ps -- ps-like process listing
info -- info for a process
-h, -?, help -- displays this help text
```

- run
    - the first argument is a script name (.lua is optional)
    - additional arguments will be passed as arguments to the script parse
    - all arguments will be interpreted as a lua script (via `loadstring`)
    - the mq namespace is provided for you (as `mq`)
- stop
    - no argument will stop all running scripts
    - will accept script name or PID as an argument to stop individual scripts
- pause
    - no argument will attempt to pause or resume all running scripts
        - if all scripts are paused or resumed, will toggle state on all of them
        - otherwise, will just pause any running scripts
    - will accept script name or PID as an argument to pause or resume individual scripts
- conf
    - arguments are option and value
    - if only option is specified, will just echo the value
- reloadconf
    - just reloads the config after it has been edited
- ps
    - provides a table of processes with a quick status
    - takes a list of statuses to filter the list (`STARTING`, `RUNNING`, `PAUSED`, `EXITED`)
    - defaults to listing `RUNNING` and `PAUSED` scripts
- info
    - displays detailed information about the status of a script
    - takes a PID or a script name
    - defaults to an unfiltered ps list when no script is specified

### TLO & Datatypes

One new TLO is provided, `Lua`. This is a transparent accessor to the new `lua` datatype, and takes no index because it is a global state. The new datatypes (and their members) are as follows:

- lua
  - PIDs (string) - a comma-delimited list of integer PIDs that have info to access
  - Dir (string) - the base lua scripts directory
  - Turbo (int) - the turbo value
  - RequirePaths (string) - the semicolon-delimited value for lua require search paths
  - CRequirePaths (string) - the semicolon-delimited value for dll require search paths
  - Script (luainfo) - the accessor to get info on individual scripts. Accepts a PID as an index, or will default to the last executed script that has finished running.
- luainfo (accessed using the Script accessor above)
  - PID (int)- the PID of the running or most recently executed version of this script
  - Name (string) - the name of the script
  - Path (string) - the full path of the script
  - Arguments (string) - a comma delimited list of arguments passed to the script
  - StartTime (string) - The time the most recent execution of the script was started
  - EndTime (string) - The time the most recent execution of the script ended or NULL if the script has not ended
  - ReturnCount (int) - The number of returns from the script, will be 0 if the script has not ended
  - Return (string) - if not indexed, a comma-delimited list of return values. Accepts an integer index to get a single return value if there is more than one
  - Status (string) - The execution status of the script

### First Script Step

The first thing to do when writing a lua script for MQ2 is to `require('mq')`. The 'mq' package is built into the plugin and is what provides access to all of the lua-mq bridge bindings. Everything that binds lua to mq is going to be accessed like `mq.something`, with one exception. The single exception is that the built-in lua function `print()` has been redirected to write to the mq chat. Special functions provided at the base level are:

`print('string')`
:   as noted before

`mq.delay(val, --[[optional]]callback)`
:   where val can be an integer (which denotes milliseconds of delay) or a string that ends in 's' 'm' or 'ms' to have delays with human readable durations. The callback is optinal and is a function which evaluates to true or false to decide whether to end the delay early.

`mq.join(args...)`
:   where args must be convertible to string inside lua. This will join all the arguments into a single string

`mq.exit()`
:   force exits the script, ignoring the normal lua return flow

`mq.bind('/command', callback)`
:   where the callback is a lua function to execute when the user enters `/command`

`mq.unbind('/command')`
:   un-binds the command so that it will no longer function

`mq.event('name', 'matcher text', callback)`
:   where the callback is a lua function to execute when the text matching the matcher is detected

`mq.unevent('name')`
:   unregisters the event 'name' so that it won't react to the text anymore

`mq.doevents(optional 'event')`
:   will process queued events (binds don't queue, they execute automatically, this is only for events).  No arguments will process all events in the queue, and optionally you can pass in a single event that you wish to process and all other events will remain queued(but not flushed).

`mq.flushevents(optional 'event')`
:   clears all events in the queue without processing them.  No arguments will flush all events in the queue, and optionally you can pass in a single event that you wish to flush.


`mq.parse(string)`
:   runs the string through the macro parser and returns the result as a string (regardles of the data type returned).  This is not a replacement for mq.TLO or mq.TLO.MacroVariable and is only for complex operations where neither of those will work (generally converting from old ini/macro formats)

`mq.TLO`
:   noted in [TLO Bindings](#tlo-bindings) below

`mq.cmd` and `mq.cmdf`
:   noted in [Command Bindings](#command-bindings) below

`mq.imgui`
:   noted in [ImGui Bindings](#imgui-bindings) below


## Lua Bindings

### TLO Bindings

TLOs are the same as macro TLOs, just accessed via the lua API. The reason for exposing these is to allow a quick conversion from macros directly into lua. The quick rules to convert are as follows:

1. Remove the `${}`
2. prepend the expression with `mq.TLO.`
3. replace all `[]` with `()`
4. wrap all strings with quotes (double or single, it doesn't matter)
5. append `()` to the end to finally bring the result into lua

For example, let's take the macro data value of `${Me.Buff[Spirit of Wolf].ID}`. To convert this into lua following the steps, you get this:

1. `Me.Buff[Spirit of Wolf].ID`
2. `mq.TLO.Me.Buff[Spirit of Wolf].ID`
3. `mq.TLO.Me.Buff(Spirit of Wolf).ID`
4. `mq.TLO.Me.Buff('Spirit of Wolf').ID`
5. `mq.TLO.Me.Buff('Spirit of Wolf').ID()`

Something in particular to note. While things like `mq.TLO.Math` and `mq.TLO.SomeString.Equals` _will_ work, it would be much better if you just bring those types into lua and do lua operations on them. so do `mq.TLO.SomeString() == 'thatstring'` or instead of `mq.TLO.Math('1 + 1')` just do `1 + 1`. Take advantage of the medium!

### Command Bindings

This binding allows you to pass commands to EQ. It is very dumb in that it can take any value, and will just prepend a `/` in front of it and send it to the EQ parser. Any arguments passed to it are stringified (in lua), concatenated (with a space delimiter), and sent as part of the command. So for instance, `mq.cmd('/who all fred')` will end up getting passed to EQ as `/who all fred`. You can also use cmdf to provide a format string: `mq.cmdf('/who all %s', someStringValue)`

### ImGui Bindings

ImGui is a feature that lua supports that has no equivalent in the macro world. For full documentation of the source binding API, this page has the source: [sol2 ImGui Bindings](https://github.com/macroquest/macroquest/tree/master/src/plugins/lua/contrib/imgui). As mq may have different needs, we can expand this as time goes on, and if that happens, then we will add a page on this wiki to document all the available bindings.

To use imgui, you must register a callback using `mq.imgui.init('name', callback)`. The callback will be a function that will be called every imgui update, and will usually be the code to render your imgui windows. To remove the callback, you can use `mq.imgui.destroy('name')` and the callback will unregister and no longer render on imgui updates.

## Additional Bindings

In addition to the full set of binds in the MSeys repo, we have also added the following:

### Drag and drop support

```lua
-- ImGui.BeginDragDropSource(...)
-- Parameters: int (flags) [O]
-- Returns: bool (isDragged)
-- Overloads
isDragged = ImGui.BeginDragDropSource()
isDragged = ImGui.BeginDragDropSource(ImGuiDragDropFlags.SourceNoPreviewTooltip)

-- ImGui.EndDragDropSource()
ImGui.EndDragDropSource()

-- ImGui.BeginDragDropTarget()
-- Returns: bool (isDropped)
isDropped = ImGui.BeginDragDropTarget()

-- ImGui.EndDragDropTarget()
ImGui.EndDragDropTarget()

-- ImGui.SetDragDropPayload(...)
-- Parameters: text (type), object(data), int (cond) [O]
-- Returns: bool
-- Overloads
ImGui.SetDragDropPayload('ITEMN', i)
ImGui.SetDragDropPayload('ITEMN', i, ImGuiCond.Always)

-- ImGui.AcceptDragDropPayload(...)
-- Parameters: text (type), flags (cond) [O]
-- Returns: object
-- Overloads
payload = ImGui.AcceptDragDropPayload('ITEMN')
payload = ImGui.AcceptDragDropPayload('ITEMN', ImGuiDragDropFlags.AcceptNoDrawDefaultRect)

-- ImGui.GetDragDropPayload()
-- Returns: object
payload = ImGui.GetDragDropPayload()
```

### EQ Icon rendering

```lua
-- Get the table of icons, which live in an animation texture
anim = mq.FindTextureAnimation('A_SpellIcons')
...
-- once you know the index of the icon inside the texture, set the cell
anim:SetTextureCell(spell.SpellIcon())
-- render the texture at the cell
ImGui.DrawTextureAnimation(anim)
```

### Events and Binds

As alluded to earlier, lua supports events and binds similar to the macro language. The details of how to use them are documented [here](./events-and-binds.md).

## Including Modules

In general, if you have some lua code from somewhere, you can simply `require('thescript')` and it will be usable in your code. The `fishb` example does this with an external behavior tree module. There is something special to consider about loading modules like this -- they can sometimes be quite large, and in order to prevent some errors the implementation of mq2lua turns off the normal frame yielding operation to load requires. What this means is that your client can hang when you require a file, especially if it is large. The good news is that lua caches requires, so it will only hang on the first load, and won't hang again until the plugin restarts.

There is another type of module that lua can include: compiled dlls. This is slightly more complex because you have to build it against the version of lua that we use in mq2lua. Luckily, this version of lua is in our vcpkg repo, so everything you need to link against is available in the mq git. LuaRocks is a great resource for these kinds of packages, and I have made detailed instructions for building these [here](./luarocks-modules.md).


## Config Options

- turboNum
    - the number of instructions that will be processed before yielding the frame
    - default: 500
- luaDir
    - the path where lua scripts live, relative to the MQ2 root directory
    - default: 'lua'
- luaRequirePaths
    - list of additional require lookup paths, written in lua require lookup format
    - appends the global `package.path` in lua environments
    - default: empty list
- dllRequirePaths
    - list of additional require lookup paths for c modules, written in lua require lookup format
    - appends the global `package.cpath` in lua environments
    - default: empty list
- infoGC
    - the time to garbage collect `ps` and `info` output so they don't always persist in memory
    - accepts numbers (in milliseconds) or strings ending in 'h', 'm', 's', or 'ms' for hours, minutes, seconds, and milliseconds
    - default: 1 hour
- squelchStatus
    - a flag to set whether or not to print lua status messages when running, pausing, and stopping scripts
    - default: false (do not squelch)
