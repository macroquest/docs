---
tags:
    - lua
---
# LuaRocks Modules

MacroQuest includes helpers for lua script writers to allow their users to install modules from LuaRocks.  MacroQuest also includes luarocks.exe with the compile for facilitating this install.

The repository of tested LuaRocks exists at https://luarocks.macroquest.org/ and these are all verified as working.  Packages can be added by submitting a pull request to the [MQ LuaRocks Repo config](https://github.com/macroquest/luarocks/blob/main/mq_luarocks.yaml)

## Script Writer's Guide to using PackageMan

PackageMan is the primary helper for installing LuaRocks modules.  The simplest method for package installation is PackageMan.Require.  However, there are also functions for InstallAndLoad and just Install.

### PackageMan.Require

The simplest method of installing a required package is PackageMan.Require.  This will check for the package, try to install it if it is not found, and try to load it after the install.  If it fails, Require returns a customizable message that tells the user what happened.  By default this message just states that there was a failure.

An example of how to require lsqlite3 for your script is:

```lua
local mq = require('mq')
local PackageMan = require('mq/PackageMan')
local sql = PackageMan.Require('lsqlite3')
```

This will contact the default MacroQuest rock server, install lsqlite3 and load it to be used under the sql variable.  If there is a failure, the simplest message ("Failed to load package lsqlite3") will be displayed to the user.

Require also supports overloads for packages that do not have the same name as their luarocks name would suggest.  In this case, you can use two parameters for Require.  An example of this is lfs.  The name of the package is "luafilesystem" but when you load it, you load it with "lfs" so you can pass that information to Require as below:

```lua
local mq = require('mq')
local PackageMan = require('mq/PackageMan')
local lfs = PackageMan.Require('luafilesystem', 'lfs')
```

This will perform the same steps as above, but once the package is installed it uses the lfs name instead of the luafilesystem name for loading.

Lastly, you can use Require to send your own custom message if you do not like the default message.  This is the third overload for Require.  For example, in the case that you want to return the message "[ScriptNameHere] LFS failed to install and is required for this script" you can do so as:

```lua
local mq = require('mq')
local PackageMan = require('mq/PackageMan')
local lfs = PackageMan.Require('luafilesystem', 'lfs', '[ScriptNameHere] LFS failed to install and is required for this sript')
```

The default message should suffice for most usages.

In all cases, when there is a failure to load the package using Require, your script will be exited.  If you'd like more control, you can use the other functions of PackageMan.

### PackageMan.InstallAndLoad

For most use cases, Require should be sufficient.  However, for more granular control over what happens when a package fails to load, you can start with InstallAndLoad.  This will attempt to install the package and load it.  It does not check to see if the package is installed first, as that is up to the script writer.  The mq/utils library has an example of an Include function which will try to load a library and gracefully fail.  An example of using this library to do your own error handling on a package install is below:

```lua
local mq = require('mq')
local PackageMan = require('mq/PackageMan')
local Utils = require('mq/Utils')

local sql = Utils.Library.Include('lsqlite3')
if not sql then
    sql = PackageMan.InstallAndLoad('lsqlite3')
end

if not sql then
    print('Could not load or install lsqlite3')
end
```

Because Utils.Library.Include is a graceful failure, the above code will try to load the library, install and try to load it if the initial load fails, and lastly print a message if it is still not loaded.  This is useful if your script does not have a strict dependency on the library and would only use the library if it was available.

InstallAndLoad also can be overloaded with an additional parameter for packages where the name is different.  Referencing luafilesystem, the appropriate usage for InstallAndLoad would be:

```lua
local mq = require('mq')
local PackageMan = require('mq/PackageMan')
local Utils = require('mq/Utils')

local lfs = Utils.Library.Include('lfs')
if not lfs then
    lfs = PackageMan.InstallAndLoad('luafilesystem', 'lfs')
end

if not lfs then
    print('Could not load or install luafilesystem/lfs')
end
```

Unlike Require, InstallAndLoad does not have a third overload for a message, since you are expected to handle your own failure messages.

### PackageMan.Install

If Require or InstallAndLoad does not meet your needs, then Install provides the most granular control over installing a package.  Again, for most people Require should be sufficient.  However, Install will allow you to determine the REASON for failures, which none of the other methods do.

Install is also only responsible for installing your package, it will not try to load your package at all and it does not check if the package is already installed.  The return on Install is a numerical error code, the most up to date details for which can be found in the source for PackageMan.lua.  The most relevant return code that a script writer would probably be handling is error code 2 -- the user declined the installation of the package.

One example of usage is below:

```lua
local mq = require('mq')
local PackageMan = require('mq/PackageMan')
local Utils = require('mq/Utils')

local sql = Utils.Library.Include('lsqlite3')
if not sql then
    if PackageMan.Install('lsqlite3') == 2 then
        print('User canceled the install, cannot proceed')
        mq.exit()
    else
        sql = require('lsqlite3')
    end
end
```

### Advanced Configuration

PackageMan includes parameters repoUrl and repoName for pointing users at your own repo should you want to beta test with users.  However, use this at your own risk as there is no setup of maintaining multiple versions of packages from different repos.

## Step-by-Step Building a LuaRocks Module for MQ

While the easiest method is to allow MQ's team to build the module you're looking for, if you're trying to build something locally for testing, one set of instructions are below.

This is one method of compiling using [LuaRocks](https://luarocks.org/) with the [Lua SQLite3](http://lua.sqlite.org/index.cgi/index) library. These instructions are available in generic form [in the official installation instructions](https://github.com/luarocks/luarocks/wiki/Installation-instructions-for-Windows); but this covers the specific details needed for MQ.

1.  Grab LuaRocks for Windows at the [LuaRocks download page](https://luarocks.github.io/luarocks/releases/) (you want the legacy windows package,
    because you will need to build it yourself)

2.  Extract the zip to someplace nice.

3.  Open up the developer command prompt for VS and navigate to the aforementioned nice place.

    ![image](../uploads/0021e9a535cd57b2db748b02fa2f7682.png)

    ```
    C:\Program Files (x86)\Microsoft Visual Studio\2019\Community>cd C:\Users\dannu\Downloads\luarocks-3.6.0-win32

    C:\Users\dannu\Downloads\luarocks-3.6.0-win32>
    ```

4.  If you have not built mq2lua (in VS), do so now. It will run the vcpkg install of `luajit` that we need to run `luarocks` with.
    You can alternately just install it through the MQ vcpkg environment, but this is the simplest way to get what you need.

5.  Run `install.bat` with `/SELFCONTAINED`, using `/P` to point to the install directory, and (most importantly) `/INC`, `/LIB`, and `/BIN`
    to point to the mq install of luajit that you just built, and `/NOADMIN` because this is a local install. Hit enter when prompted:

    ```
    C:\Users\dannu\Downloads\luarocks-3.6.0-win32>.\install.bat /P C:\Users\dannu\Downloads\luarocks_install /SELFCONTAINED /INC "C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\include\luajit" /LIB "C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\lib" /BIN "C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\tools" /NOADMIN

    C:\Users\dannu\Downloads\luarocks-3.6.0-win32>rem=rem --[[--lua
    LuaRocks 3.6.x installer.


    ========================
    == Checking system... ==
    ========================


    Attempting to install without admin privileges...
    Looking for Lua interpreter
        Found luajit.exe, testing it...
        checking for C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\lib\lua5.1.lib
        checking for C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\lib\lua51.lib
        Found lua51.lib
        checking for C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\include\luajit\lua.h
        Found lua.h
    *** WARNING ***: could not analyse the runtime used, defaulting to MSVCR80
    Runtime check completed.
    arch: 14c -> IMAGE_FILE_MACHINE_I386
    Looking for Microsoft toolchain matching runtime MSVCR80 and architecture x86
        checking: HKLM\Software\Microsoft\VisualStudio\8.0\Setup\VC
        checking: HKLM\Software\Microsoft\VCExpress\8.0\Setup\VS
        Cannot auto-detect Windows SDK version from MSVCR80

    ==========================
    == System check results ==
    ==========================

    Will configure LuaRocks with the following paths:
    LuaRocks        : C:\Users\dannu\Downloads\luarocks_install
    Config file     : C:\Users\dannu\Downloads\luarocks_install\config-5.1.lua
    Rocktree        : C:\Users\dannu\Downloads\luarocks_install\systree

    Lua interpreter : C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\tools\luajit.exe
        binaries    : C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\tools
        libraries   : C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\lib
        includes    : C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\include\luajit
        architecture: x86
        binary link : lua51.lib with runtime MSVCR80.dll

    Compiler        : Microsoft (make sure it is in your path before using LuaRocks)

    Press <ENTER> to start installing, or press <CTRL>+<C> to abort. Use install /? for installation options.


    ============================
    == Installing LuaRocks... ==
    ============================


    Installing LuaRocks in C:\Users\dannu\Downloads\luarocks_install...
    Created LuaRocks command: C:\Users\dannu\Downloads\luarocks_install\luarocks.bat
    Created LuaRocks command: C:\Users\dannu\Downloads\luarocks_install\luarocks-admin.bat

    Configuring LuaRocks...
    Created LuaRocks hardcoded settings file: C:\Users\dannu\Downloads\luarocks_install\lua\luarocks\core\hardcoded.lua
    Created LuaRocks config file: C:\Users\dannu\Downloads\luarocks_install\config-5.1.lua

    Creating rocktrees...
    Created system rocktree    : "C:\Users\dannu\Downloads\luarocks_install\systree"
    Local user rocktree exists : "C:\Users\dannu\AppData\Roaming\LuaRocks"

    ============================
    == LuaRocks is installed! ==
    ============================


    You may want to add the following elements to your paths;
    Lua interpreter;
    PATH     :   C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\tools
    PATHEXT  :   .LUA
    LuaRocks;
    PATH     :   C:\Users\dannu\Downloads\luarocks_install
    LUA_PATH :   C:\Users\dannu\Downloads\luarocks_install\lua\?.lua;C:\Users\dannu\Downloads\luarocks_install\lua\?\init.lua
    Local user rocktree (Note: %APPDATA% is user dependent);
    PATH     :   %APPDATA%\LuaRocks\bin
    LUA_PATH :   %APPDATA%\LuaRocks\share\lua\5.1\?.lua;%APPDATA%\LuaRocks\share\lua\5.1\?\init.lua
    LUA_CPATH:   %APPDATA%\LuaRocks\lib\lua\5.1\?.dll
    System rocktree
    PATH     :   C:\Users\dannu\Downloads\luarocks_install\systree\bin
    LUA_PATH :   C:\Users\dannu\Downloads\luarocks_install\systree\share\lua\5.1\?.lua;C:\Users\dannu\Downloads\luarocks_install\systree\share\lua\5.1\?\init.lua
    LUA_CPATH:   C:\Users\dannu\Downloads\luarocks_install\systree\lib\lua\5.1\?.dll

    Note that the %APPDATA% element in the paths above is user specific and it MUST be replaced by its actual value.
    For the current user that value is: C:\Users\dannu\AppData\Roaming.



    C:\Users\dannu\Downloads\luarocks-3.6.0-win32>
    ```

6.  Navigate to the path you specified with the `/P` switch

    ```
    C:\Users\dannu\Downloads\luarocks-3.6.0-win32>cd C:\Users\dannu\Downloads\luarocks_install

    C:\Users\dannu\Downloads\luarocks_install>
    ```

7.  Run `luarocks.bat` to `install` `lsqlite3complete`, which will build it with `cl` (this is why you needed to do this in the developer console)

    ```
    C:\Users\dannu\Downloads\luarocks_install>.\luarocks.bat install lsqlite3complete
    Installing https://luarocks.org/lsqlite3complete-0.9.5-1.src.rock

    lsqlite3complete 0.9.5-1 depends on lua >= 5.1, < 5.5 (5.1-1 provided by VM)
    cl /nologo /MD /O2 -c -Folsqlite3.obj -IC:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\include\luajit lsqlite3.c -DLSQLITE_VERSION="0.9.5" -Dluaopen_lsqlite3=luaopen_lsqlite3complete
    lsqlite3.c
    cl /nologo /MD /O2 -c -Fosqlite3.obj -IC:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\include\luajit sqlite3.c -DLSQLITE_VERSION="0.9.5" -Dluaopen_lsqlite3=luaopen_lsqlite3complete
    sqlite3.c
    link -dll -def:lsqlite3complete.def -out:lsqlite3complete.dll C:\Users\dannu\workspace\mqnext\contrib\vcpkg\installed\x86-windows-static\lib/lua51.lib lsqlite3.obj sqlite3.obj
    Microsoft (R) Incremental Linker Version 14.28.29913.0
    Copyright (C) Microsoft Corporation.  All rights reserved.

    Creating library lsqlite3complete.lib and object lsqlite3complete.exp
    LINK : warning LNK4098: defaultlib 'LIBCMT' conflicts with use of other libs; use /NODEFAULTLIB:library
    No existing manifest. Attempting to rebuild...
    lsqlite3complete 0.9.5-1 is now installed in C:\Users\dannu\Downloads\luarocks_install\systree (license: MIT)


    C:\Users\dannu\Downloads\luarocks_install>
    ```

8.  You now have a dll in `systree\lib\lua\5.1\lsqlite3complete.dll` that you can copy into your mq lua directory (wherever you lua script lives) and use it with `require('lsqlite3complete')`
