---
tags:
   - plugin
---
# MQ2AutoLogin

## Description

AutoLogin is a plugin that automatically logs in your characters. It can also switch characters, servers and login new accounts via commandline. It was originally made by [ieatacid](https://macroquest.org/phpBB3/viewtopic.php?f=50&t=16427).

## Setting up profiles via tray icon

Right click on your MacroQuest tray icon

Select Profiles-&gt;Create New.

You'll be asked to enter nine fields:

1. Profile Set: (This creates "groups" of profiles, enter any custom name) 
2. EQ Path: (Path to eqgame.exe)
3. Login: (EverQuest login)
4. Password:  (EverQuest password)
5. Server: (Server short name)
6. Character Name: 
7. Class: (Optional)
8. Level: (Optional)
9. Hotkey: (Assign a key or combination of keys to bring this character's window to the front)

Upon clicking "Save", your profile will be encrypted and saved in MQ2AutoLogin.ini

## Commands

`/switchserver <server short name> <character name>`

Will log out your current character and log in the specified server/character on the same account. 

`/switchchar <name>`

Will log out your current character and log in the specified character on the same account/server. 

`/loginchar [server:character|profile_server:character|server^login^character^password|server^login^password]`

Will open a new EverQuest instance and login the specified character. Example: `/loginchar vox:bobby`

`/relog [#s|#m]`

Will log character out, and then log back in after specified time. Default time is in seconds. Example: `/relog 5m`

`END` and `HOME`

Pressing the "END" key at the character select screen will pause autologin, "HOME" will unpause.

## INI 

MQ2AutoLogin.ini has the following global settings,
```ini⏎
[Settings]
;The following settings are global. Settings changed for specific characters will override them.
NotifyOnServerUp=1
;0 is off, 1 is beep, 2 is email via MQ2Gmail
KickActiveCharacter=1
;0 is off, 1 is on. Will attempt to boot an active player to log in.
EndAfterCharSelect=1
;0 is off, 1 is on.
CharSelectDelay=3
;seconds to wait at the character select screen. Default is 3
ConnectRetries=0
;How many attempts to connect after a failure
UseMQ2Login=1
;Uses the default, encrypted method of autologin
UseStationNamesInsteadOfSessions=0
;Stores your login and pass in plaintext in MQ2AutoLogin.ini, but is compatible with ISBoxer/WinEQ.
```
If you're using `UseMQ2Login=1` and have created profiles via the tray icon, there will be additional sections such as `[Profiles]` and profile names. These should be left alone, as their settings are best changed via the GUI.

## Alternate login methods
There are two alternate login methods: Sessions (compatible with the EverQuest launcher and "-patchme" login method) and Station Names (best for WinEQ and ISBoxer) 

If you'd like to use sessions, set `UseMQ2Login=0`, and add sessions to the MQ2AutoLogin.ini in this format, 

**Sessions example INI**
```ini⏎
[Settings]
UseMQ2Login=0

[Session1]
StationName=StationNameforSession
Password=PasswordforSession
Server=ServerforSession
Character=Name

[Session2]
StationName=StationNameforSession
Password=PasswordforSession
Server=ServerforSession
Character=Name
```

If you're using ISBoxer, set `UseMQ2Login=0` AND `UseStationNamesInsteadOfSessions=1`, and add station names to the MQ2AutoLogin.ini in this format, 

**Station names example INI**
```ini⏎
[Settings]
UseMQ2Login=0
UseStationNamesInsteadOfSessions=1

[StationName1]
Password=PasswordforThisLoginName
Server=ServerforThisLoginName
Character=CharacterforThisLoginName

[StationName2]
Password=PasswordforThisLoginName
Server=ServerforThisLoginName
Character=CharacterforThisLoginName
```

Additional settings from the global section, such as `KickActiveCharacter=1` can be added to session or station name sections to affect only that character.


## List of server short names

    antonius
    bertox
    bristle
    cazic
    drinal
    erollisi
    firiona
    luclin
    phinigel
    povar
    ragefire
    rathe
    rizlona
    tunare
    vox
    xegony
    zek
    test
    beta

## Custom server names
To add a new server with a custom short name, which is particularly important for emulators, edit your MQ2AutoLogin.ini with the following format: 
```ini⏎
[Servers]
customshortname=Exact long name (as it appears on login screen)
```
For example, here are the most popular macroquest-compatible emu servers as of 9/27/2017: 
```ini⏎
[Servers]
peqgrand=[] [PEQ] The Grand Creation - Omens of War
ezserver=[] EZ Server - Custom Zones, Vendors, Quests, Items, etc
stormhaven=[] Storm Haven - High-Quality Custom Content
alkabor=[] The Al'Kabor Project [www.takproject.net]
thf=[] The Hidden Forest [ www.thehiddenforest.org ]
chronicles=[] Chronicles of Norrath
dragonsoul=[] Dragon Soul - CEQ [zh-cn/legit/PvE]
leetsauce=[] Leetsauce Productions
kmra=[] Raid Addicts (Fully Custom) [Solo/Group/Raid]
scorpious=[] Scorpious2k: The Next Generation [custom]
sod=[] Shards of Dalaya
vegarlson=[] Vegarlson Asylum
zek=[] Zek [Teams/Guildwars]
```

## MQ2Login Profiles GUI

Right click on the MacroQuest tray icon -> Profiles

`Check marks:`

A checked character will be loaded when clicking "Profile->Load All". Right-clicking a character's name will toggle the checkmark on or off.

`Loading individual accounts:`

Left click on a character name and if checked, it will login and load MacroQuest. Left-clicking a loaded character will unload MacroQuest for that character.

`Batch Files and hotkeys:`

If you currently use batch files or hotkeys or whatever, those should still be usable if you don't want to click the menu. Example: \(this example assumes you HAVE profiles created with "Create New..." in mq2autologin.ini\) Batch file can launch your accounts by sending the server\_charname to the eqgame client like this:  patchme /login:drinal\_eqmule And that's really all there is to it... You would of course change the server and Charname to your server and your char \(drinal and eqmule\)

`Encryption:`

If you make profiles via the tray icon GUI, they are encrypted in your MQ2AutoLogin.ini. Moving your file to another computer or changing computer hardware will invalidate these logins, so please use import/export for backup and moving purposes.

`Import/Export`

This helps export and import login profiles, which are otherwise hard to decrypt. 

`Launch Clean`

Launch single sessions without logging in.
