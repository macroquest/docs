# MacroQuest Launcher

Also known as MacroQuest.exe

MacroQuest.exe is _**an open-source**_ project and is known as the MacroQuest _injector_.

Running MacroQuest.exe is the way to start MacroQuest.  Note, that once MacroQuest has been loaded in all of the EQ instances you'd like it to load -- MacroQuest.exe is no longer required to be running.  However, it does handle profile launching and hotkey switching, so closing it will lose these functions.

## Usage

**MacroQuest.exe [/injectonce] [/noappcompat] [/spawnedprocess]**

| Switch            | Function                               |
| ----------------- | -------------------------------------- |
| _/injectonce_     | Tells MacroQuest to only inject one time and then exit.  This is only useful for platforms that only allow running one instance of EQ. |
| _/noappcompat_    | Disabled application compatibility checks when starting up.  Normally these checks will tell you if something MQ related was added to your application compatibility list (which should be fixed by you) |
| _/spawnedprocess_ | Tells MacroQuest that this is a spawned process and you want it to keep the same name.  This isn't useful outside of debugging. |
