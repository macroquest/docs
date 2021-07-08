# MQ2AutoLogin

## Credits

`Created by ieatacid, incorporated into MQ2Core by EQMule`  
[`http://www.macroquest2.com/phpBB3/viewtopic.php?f=50&t=16427`](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=16427) \`\`

## Description

There are 3 main ways people can use this.

`1. MQ2Login via tray icon gui right click`  
`2. MQ2AutoLogin via a windows shortcut with -patchme`  
`3. MQ2Autologin via ISBoxer or WinEQ using station name with -patchme`

Any of these methods would of course require you to have MQ2 loaded, with MQ2AutoLogin enabled. --Note MQ2AutoLogin is now part of the core download, enable/disable it through the MQ2 tray icon \(Mq2Login\) --

## MQ2Login via tray icon gui right click

Right clicking on your MQ2 tray icon will activate a pop up window.

Select profile-&gt;Create New.

You click it and a small window will pop up asking for 6 things.

`Profile Set:`  
`Login:`  
`Password:`  
`Server:`  
`Charname: (Character Name)`  
`EQ Path: and path to eqgame.exe EX c:\games\everquest (or click on the "Browse" button to find it)`

Once you have that filled in you click an SAVE button and your profile will be encrypted and saved in mq2autologin.ini

You can save as many profiles as you want and they will sort per profile set on the menu.

Each profile set has a Load/Unload All option so once you have added all your accounts for a group you just click the Load All and away it goes, it will login all of the characters in that profile set that are checked.

## MQ2AutoLogin via a windows shortcut with -patchme

First, you'll need to set up the ini file \(named: MQ2AutoLogin.ini\) with your account information:

**Sample INI**

`[Settings]`  
`KickActiveCharacter=1`  
`InstantCamp=0`  
`KickActiveTrader=1`  
`UseStationNamesInsteadOfSessions=0`

`[Session1]`  
`StationName=StationNameforSession`  
`Password=PasswordforSession`  
`Server=ServerforSession`  
`Character=`

`[Session2]`  
`StationName=StationNameforSession`  
`Password=PasswordforSession`  
`Server=ServerforSession`  
`Character=`

## MQ2Autologin via ISBoxer or WinEQ using station name with -patchme

Alternatively, you can use station names rather than sessions \(handy if you use ISBoxer or WinEQ2 profiles\). MQ2AutoLogin will use the defined station name and input the password and log in to the server and character indicated in the ini.

**Sample INI**

`[Settings]`  
`UseMQ2Login=0`  
`KickActiveCharacter=1`  
`InstantCamp=0`  
`KickActiveTrader=1`  
`UseStationNamesInsteadOfSessions=1`

`[StationName1]`  
`Password=PasswordforThisLoginName`  
`Server=ServerforThisLoginName`  
`Character=CharacterforThisLoginName`

`[StationName2]`  
`Password=PasswordforThisLoginName`  
`Server=ServerforThisLoginName`  
`Character=CharacterforThisLoginName`

## In Game Commands

`/switchserver`

when issued in game, logs you out and logs you back in on whatever server and character specified:

`/switchchar|-instant <on|off>`

`/loginchar server:charname`

Will now launch eq and log the char in.

NOTE: if you run this command and server:char is already running, you will kill his game and he will be logged in again, this command ALWAYS launches a new client. this is for advanced users only, I use it personally to launch and get back into a game when one of my clients has crashed. \(easily detected with the ${Group.Member\[soandso\].Offline} tlo member... or lets say I havent seen the guy for 15 minutes\) NOTE2: this command only works if you are using the mq2 login system and have a profile for the character. Example: /loginchar tunare:eqmule will search all mq2 profile sets for the tunare server and the char eqmule if it finds it, it will launch eq and log in that character

## INI configuration values

MQ2AutoLogin has 2 types of sections

`1 - The global settings under [Settings]`  
`2 - The per-character section. This can be either [Session#] or [LoginName]`

**Section = \[Settings\]**

**`KickActiveCharacter=1/0`**  
`Defaults to 1 (on) if it's not in your ini file. If enabled, this clicks the "Yes" button when the window pops up asking if you want to kick the character that you already have logged into a world server, else it just sits there at the server-select screen.`

**`KickActiveTrader=1/0`**  
`Defaults to 0 (off) if it's not in your ini file. If enabled, this clicks the "Yes" button when the window pops up asking if you want to kick the trader that you already have logged into a world server, else it just sits there at the server-select screen.`

**`InstantCamp=1/0`**  
`Defaults to 0 (off) if it's not in your ini file. If enabled, this uses instant-camp to camp you out rather than the 30 second countdown.`

**`UseStationNamesInsteadOfSessions=1/0`**````` Defaults to 0 \(off\).```0 = Off, it will login the session\#````` 1 = On, this uses account information based on the specified station name in brackets, which works well if you're using ISBoxer or WinEQ2 profiles.\`

**Section = either \[Session\#\] or \[LoginName\]**

**`StationName=YourStationName`**  
`If you are using sessions you need to specify the StationName, if you are not using sessions you dont need this value.`

**`Password=YourPassword`**  
`The password for your character`

**`Server=YourServer`**  
`The server you want to log in to. If set to none it will go to server select screen`

**`Character=YourCharacterName`**  
`The character you want to log in, if this is blank it will go to the character select screen for the specified server`

**List of server short names for \[Session\#\] or \[LoginName\] sections**

`; List of server short names`  
`;antonius`  
`;bertox`  
`;bristle`  
`;cazic`  
`;drinal`  
`;erollisi`  
`;fippy`  
`;firiona`  
`;luclin`  
`;mayong`  
`;povar`  
`;rathe`  
`;trakanon`  
`;tunare`  
`;vox`  
`;vulak`  
`;xegony`  
`;zek`

## MQ2Login Details - \[Profiles\]

\(Derived from right clicking on the MQ2 tray icon\)

`Check marks:`

Each character can be marked for loading by simply right clicking the character name to toggle it marked on or off. \(for the LOAD ALL option\)

`Loading individual accounts:`

You just left click on a character name and if it is check marked, it will load and the name will be changed to

\(Loaded\)

`Unloading individual accounts:`

If a char is loaded and has the text \(Loaded\) behind it you just left click it to unload. I kept this as simple as I possibly could so its a Toggle.

`Batch Files and hotkeys:`

If you currently use batch files or hotkeys or whatever, those should still be usable if you don't want to click the menu. Example: \(this example assumes you HAVE profiles created with "Create New..." in mq2autologin.ini\) Batch file can launch your accounts by sending the server\_charname to the eqgame client like this:  patchme /login:drinal\_eqmule And that's really all there is to it... You would of course change the server and Charname to your server and your char \(drinal and eqmule\)

`Encryption:`

I strongly recommend getting this setup though, because it encrypts your password in a way that in "theory" makes it only decryptable on YOUR computer, this means that even if you accidently post your mq2autologin.ini somewhere, or someone gets hold of it, the information inside it will be useless to them.

`Launch Clean`

The Launcher can now launch single sessions without logging u in, i basically just "launches clean" rightclick the "Launch Clean" menu item to toggle starting eqgame in suspended mode \(for power users\)

`Import/Export profiles`

The Launcher can now export and import login profiles.

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

