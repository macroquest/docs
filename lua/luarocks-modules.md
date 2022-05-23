# LuaRocks Modules

## Step-by-Step Building a LuaRocks Module for MQ

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
