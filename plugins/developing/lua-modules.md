# Lua Modules From Plugins

MQ2Lua can load Lua modules provided by other plugins via `require()`. This allows a plugin to expose native Lua tables, functions, and usertypes without using the TLO system.

## Lua Usage

```lua
local myplugin = require("plugin.myplugin")

myplugin.hello()
local value = myplugin.add(2, 3)
```

## Plugin Authoring (C++)

### Build Setup

If your plugin uses the Lua interface, import the MQ2Lua props file:

```
src/plugins/lua/LuaPlugin.props
```

This adds the LuaJIT include path and links `lua51.lib`.

### Example

#### Plugin
```cpp
#include <mq/Plugin.h>
#include <sol/sol.hpp>

PreSetup("MQLuaModuleTest");
PLUGIN_VERSION(0.1);

void EchoPrimitive(const int value)
{
	WriteChatf("[LuaModuleTest] EchoPrimitive called with value=%d", value);
}

PLUGIN_API bool CreateLuaModule(const sol::this_state luaState, sol::object& outModule)
{
	sol::state_view lua(luaState);
	sol::table module = lua.create_table();

	module["version"] = 1;
	module["EchoPrimitive"] = &EchoPrimitive;

	outModule = module;
	return true;
}
```

#### Script
```lua
local module = require("plugin.MQLuaModuleTest")
printf("\ag[LuaModuleTest Script] Loaded Module version %d", module.version)
print("\ay[LuaModuleTest Script] Calling EchoPrimitive(42)")
module.EchoPrimitive(42)
print("\ag[LuaModuleTest Script] Exercise complete")
```

### Usage Notes

- Lua requires the `plugin.` (or `plugin/`) prefix, e.g. `require("plugin.myplugin")`.
- Plugin names are canonicalized (case-insensitive, `MQ`/`MQ2` prefix optional).
- Module creation runs per Lua thread; do not share Lua tables across states.
- If the owning plugin unloads, any Lua scripts that required its module will terminate.
