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

### Minimal Example

```cpp
#include <mq/Plugin.h>
#include <sol/sol.hpp>

PreSetup("MQ2MyPlugin");
PLUGIN_VERSION(1.0);

extern "C" __declspec(dllexport) sol::object CreateLuaModule(sol::this_state s)
{
    sol::state_view sv{ s };
    sol::table module = sv.create_table();

    module.set_function("hello", []() {
        WriteChatf("Hello from MyPlugin!");
    });

    module.set_function("add", [](int a, int b) { return a + b; });
    return sol::make_object(s, module);
}
```

### Usage Notes

- Lua requires the `plugin.` (or `plugin/`) prefix, e.g. `require("plugin.myplugin")`.
- Plugin names are canonicalized (case-insensitive, `MQ`/`MQ2` prefix optional).
- Module creation runs per Lua thread; do not share Lua tables across states.
- If the owning plugin unloads, any Lua scripts that required its module will terminate.
