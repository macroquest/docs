# Persisting Configuration in Lua Scripts

Lua comes with several options for reading and writing configuration files in a variety of formats.  


## Configuration File Formats

### Lua Tables
The most straightforward approach to persisting configuration in Lua is to use Lua itself. Tables in Lua can be persisted to files and loaded back in by Lua scripts. Tables look very similar to JSON in structure.  

Example Lua table as a configuration file:
```lua
return {
  setting1 = true,
  setting2 = 5,
  ['multiple word setting'] = 'some value',
  nestedSettings = {
    settingA = 1,
    settingB = false
  }
}
```

#### mq.pickle
This is a built-in function provided by MQ for serializing a Lua table to a file.  

```lua
local mq = require('mq')

-- initialize your config table
local myconfig = {}
-- name of config file in config folder
local path = 'pickletestcfg.lua'
-- attempt to read the config file
local configData, err = loadfile(mq.configDir..'/'..path)
if err then
    -- failed to read the config file, create it using pickle
    mq.pickle(path, myconfig)
elseif configData then
    -- file loaded, put content into your config table
    myconfig = configData()
end
-- print the contents
for k,v in pairs(myconfig) do print(k,v) end

myconfig.testkey = 'testvalue'

-- save the config
mq.pickle(path, myconfig)
```

#### Many table serialization options on lua-users
The [lua-users](http://lua-users.org/wiki/TableSerialization) wiki provides many example Lua table serialization implementations.

### YAML
YAML provides an easy to read format if you don't mind being dependent on proper indentation.

```yaml
settings:
- setting1: somevalue
- setting2:
  - nestedSetting: anothervalue
```

#### lyaml LuaRock
The MQ LuaRocks server has a version of lyaml available which can be installed using the Lua PackageMan script provided by MQ.  

```lua
local lyaml = PackageMan.Require('lyaml')
```

More info on lyaml [here](https://github.com/gvvaughan/lyaml).

### JSON
```json
{
  "setting1": "somevalue",
  "setting2": {
    "nestedSetting": "anothervalue"
  }
}
```

#### cjson LuaRock
The MQ LuaRocks server has a version of `cjson` available which can be installed using the Lua PackageMan script provided by MQ.  

```lua
local cjson = PackageMan.Require('lua-cjson', 'cjson')
```

More info on cjson [here](https://github.com/mpx/lua-cjson)

### SQLite3
If you would prefer to use a database over a text based configuration file, SQLite3 is supported as well.  

#### libsqlite3
The MQ LuaRocks server has a version of `lsqlite3` available which can be installed using the Lua PackageMan script provided by MQ.

```lua
local sql = PackageMan.Require('lsqlite3')
```

More info on lsqlite3 [here](http://lua.sqlite.org/index.cgi/doc/tip/doc/lsqlite3.wiki)

### INI

#### mq.TLO.Ini and /ini command
MQ has the `Ini` TLO and `/ini` commands which are used heavily by macros and work well for reading and writing INI files. Refer to the reference pages for more info on them.

#### LIP.lua Lua INI Parser
Lua INI Parser is a tiny Lua library allowing to handle .ini files.
https://github.com/Dynodzzo/Lua_INI_Parser

