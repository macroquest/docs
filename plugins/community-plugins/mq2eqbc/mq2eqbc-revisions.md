# MQ2EQBC:Revisions

\_\_NOTOC\_\_

## Guide to Revision Numbering

_Version numbering currently follows incrementing sequence theory._  
~~All future releases are numbered based on date of release.~~  
~~The letter in the revision number indicates who made the contribution.~~

* Author: Omnictrl \(o\)
* Contributor: ascii38 \(a\)
* Contributor: Vladus2000 \(v\)
* Contributor: pms \(p\)
* Contributor: ieatacid \(i\)
* Contributor: three-p-o
* Contributor: MacQ
* Contributor: Jimbob

== MQ2EQBC ==

### Version 12.1

_Update by Jimbob_

* I added support for my latest eqbci release, so it will provide more information to the client.

### Version 12.0

_Update by MacQ_

* I modified the LoadINI\(\) section to first load from the \[Settings\] section of the INI, then it loads from the

  \[SERVER.CHARACTER\] section.

  If there is no \[SERVER.CHARACTER\] section or one of the variables is not listed in the \[SERVER.CHARACTER\]

  section, then the value of that variable defaults to the \[Settings\] section or the defaults originally hard coded

  in EQBC.

* With this technique, we have greater flexibility to control variables on either a global or per characters basis.

  Now you can set certain variables you deem to be more global in the \[Settings\] section, or variables you deem to

  be more character specific set in a \[SERVER.CHARACTER\] section, which will override the \[Settings\] section.

### Version 11.0219

_Update by three-p-o_

* Update for GetTickCount64

### Version 11.0218

* Fix for null pointer crash when logging in

  \(final pms update\)

### Version 10.0513

* Death to Diversity. \(Constant to prevent win7 64bit crashes\)

### Version 9.0904

* Item links now function in the custom window \(thanks dkaa, ieatacid\)
* Added a new option 'echoall' - /bccmd set echoall on
  * This will echo outgoing '/bca' commands back to you in this format: \(to all\) message or command here
  * This defaults to off.

### Version 9.0822

New Features

* /bccmd iniconnect 

-- you can now save regularly used servers to your ini and connect to them by the key name in the event you have your own server, and a few others for your mates. Example, in your ini you could do

```text
[Mine]
Server=127.0.0.1
Port=9999

[MyServer]
Server=10.0.0.10
Port=1234

[Sklug]
Server=soe.sony.com
Port=1337

[Ngreth]
Server=soe.sony.com
Port=7331
```

and then /bccmd iniconnect mine or /bccmd iniconnect myserver

and so on...

* /bccmd forceconnect 

-- will disconnect you from your current server and attempt to connect to the new one rather than warn you that you are already connected and do nothing.

* New Settings \(see the functionality changes about the syntax\)
* silentinccmd

-- if you trust those you botchat with and do not want to see incoming command requests, enabling this option will squelch all command requests

* silentoutmsg

-- this happens with compatmode off, but if you turn compatmode on \( &gt;name\&lt; looks weird!\) and want to hide the outgoing messages, you may enable this and it will keep the names irc-leet and still squelch the message

* notifycontrol

-- with the allow control option disabled, enabling notifycontrol will output a message to /bc notifying that the command request was not processed due to allow control being off. \(/bcaa //bc test ...\)

* The dedicated UI window now allows for a keybind. Pressing the keybind will set the cursor focus on the bc window

  \(which, for those who do not know, anything you type there defaults to /bc, so you do not need to prefix the msg if

  you do not want\).

-The keybind defaults to nothing -It saves to MacroQuest.ini as "EQBC\_Nrm=clear" when you first load the plugin. You may adjust it in \[Settings\] Keybind=key of your EQBC ini file \(i do it there\) before loading the plugin.

* New TLO members

string ${EQBC.Server} - OFFLINE if not connected, the name of the server \(hostname or ip depending on how you made the connection\) if connected -- /if \(${EQBC.Server.Equal\[127.0.0.1\]}\) { // do my private stuff } else { // do other stuff }

string ${EQBC.Port} - OFFLINE if not connected, the port number otherwise

string ${EQBC.ToonName} - the name of your character _AS SEEN BY EQBC_ aka /if \(${EQBC.ToonName.Equal\[YouPlayer\]}\) { // im bugged or have a ghost, so do my fix routine }

bool ${EQBC.Setting\[\[i\]settingname\[/i\]\]} - returns the TRUE or FALSE based on if a setting is enabled. the form is required, so if you do not supply a \[i\]settingname\[/i\] it will return FALSE. -- /if \(${EQBC.Setting\[tellwatch\]}\) { /echo I have tellwatch enabled }

Functionality Changes

* the syntax of all the settings has changed slightly. sorry for the annoyance but it had to be done...
* you now adjust the settings either with 'set \_\_ on/off' or 'toggle \_\_\_'

```text
so previously:  /bccmd toggletellwatch

now becomes

/bccmd toggle tellwatch
or
/bccmd set tellwatch on
or
/bccmd set tellwatch off

this applies to all setting options. 

/bccmd set reconnectsecs #  <---this is the only one that does not support on/off, and the only that accepts a number as a parameter
```

as seen in the source, valid settings are: autoconnect control compatmode reconnect window reconnectsecs localecho tellwatch guildwatch groupwatch fswatch silentcmd savebychar silentinccmd notifycontrol silentoutmsg

* Rather than pretend it will be fixed again one day, removed the 'relog' command parameter \(and all related

  functions\) as [MQ2SwitchChar](https://macroquest.org/phpBB3/viewtopic.php?t=16201) by ieatacid provides all the

  functionality needed.

* when offline, /bcaa will no longer announce the 'you are not connected' error message followed by processing the

  command locally regardless.

Cleanup & Bug Fixes

* The dedicated UI window will no longer clear previous buffer when zoning in some cases
* The dedicated UI window will now remain when hovering.
* The dedicated UI window will no longer set the cursor at the beginning of the line when scrolling through the

  command history.

* The dedicated UI window history will no longer scroll through the history out of order in some cases.
* The dedicated UI window should now properly update the window title when reconnecting to a different server \(unless

  you set UseMyTitle=1\)

* The dedicated UI window should save your title for you instead of requiring a manual entry to the INI
* Camping out should properly save your window settings \(probably not CTD or /exit\) without forcing you to toggle the

  window on & off to force a save

* The dedicated UI window will no longer display item links as long strings of item data. They will properly display

  with their pink clickable names. _FOR NOW THE LINKS DO NOT FUNCTION_, I have a feeling due to buffer size &

  MAX\_STRING not being big enough in other places, so it may be fixable in the future but no promises.

* \_\_\_watch features no longer output the weird characters in the name. \(thanks ieatacid for donating this logic\)
* fswatch no longer relays your own output \("You tell your fellowship"\)
* Using '/camp server' will now properly disconnect you instead of leaving a ghost toon connected \(previously stayed

  until exit eqgame, or reconnect to char select\) --- WTB '\#define GAMESTATE\_SERVERSELECT -1', pst with price

* Logging into eqbcs via EQBC Interface with a ridiculously large username will no longer cause the eqbc client to

  crash from buffer overflows.

* The welcome to EQBC message now properly displays upon first entry \(of the session\) into the world rather than only

  displaying if you loaded the plugin after you were in game, without a dedicated UI window.

Irrelevant

* Source revision history has been moved from the cpp to this wiki article
* Converted from tabs back to spaces &gt;\&lt;
* Seeing as it has been over a year since anyone else messed with this, switched the version numbering to be based on

  date of release.

* Some output messages are less polite
* Updated help msgs and help parameter to reflect new changes
* oop-d to hell.

### Version 1.3.p6 - 20090120

* * Added '/bcclear' based off the '/mqclear' command
* a command instead of only a select few commands working
  a command instead of only a select few commands working

### Version 1.3.p5 - 20081219

* additions to the toggletellwatch idea
  additions to the toggletellwatch idea

### Version 1.3.i4 - 20081215

* * Added support for EQBC Interface by ieatacid

### Version 1.3.p3 - 20081214

* * Fix for vc6 by dkaa

### Version 1.3.p2 - 20081208

* * '/bcfont' and '/bcmin' are now useable in the UI window &gt;\&lt;

### Version 1.3.p1 - 20081207

* more INI file settings relating to the UI window
  more INI file settings relating to the UI window

* * Moved UI data from \[Settings\] to \[Window\] as it is plentiful now
* to be optional, always using \[Window\] options instead
  to be optional, always using \[Window\] options instead

* * Added '/bccmd togglesavebychar' to allow toggle this setting.
* * Change UseMyTitle to 1 if you wish to use a custom window title instead of server IP

  You need to create "WindowTitle=Custom Title" in \[Window\] and/or \[CharName\] to use it

  You do not need to put the title in quotes, and fearless might flame you if you admit to doing it

* * Updated UI window to support '/bca', '/bcaa', and '/bct' command input

### Version 1.2.p7 - 20081026

* * Added Fades, Alpha, and FadeToAlpha to Window INI Settings
* * /bcaa will now perform the command even if togglecontrol is disabled
* * Code cleanup/better handling for toggletellwatch
* * Added 'togglesilentcmd', which silences the 'CMD: \[command\]' message
* * Added INI support for silentcmd and tellwatch

### Version 1.2.p6 - 20080909

* to prevent banker and trader spam
  to prevent banker and trader spam

* * Fixed indenting. All indenting uses tabs now.
* * Slightly changed bca and bcaa function names for identification

### Version 1.2.a5 - 20080805 \(Why did I start playing again release\)

* * Fix for changes to EQUIStructs::\_CSIDLWND structure

### Version 1.2.p4 - 20070712

* * Added /bccmd toggletellwatch to pass tells received along, credit for string logic to MQ2MasterMind
* * Updated HandleHelpRequest for /bca, /bcaa, and /bccmd toggletellwatch

### Version 1.2.a3 - 20070617 \(I'm still not playing release\)

* * EQBC window will not close when escape key is pressed.

### Version 1.2.v2 - 20070324

* * Added better connection timeout handling

### Version 1.2.v1 - 20070116

* block certain messages from appearing, and this was the only way I knew how.
  block certain messages from appearing, and this was the only way I knew how.

* is an example of where this is useful
  is an example of where this is useful

### Version 1.1.a1 - 20060728

* It's up to you to decide if the 'a' is "ascii" or "alpha" :\)
  It's up to you to decide if the 'a' is "ascii" or "alpha" :\)

* * Channel list saved in INI file and restored when you log in.
* * New command: /bccmd togglelocalecho. When Local Echo is on, commands sent
* to a channel you are in will be sent back to you \(as per toomanynames\)

### Version 1.0.a17 - 20060715

* the channel.
  the channel.

* * New command: /bccmd channels channel\_list
* * Added ability to escape characters  will be translated to just 

### Version 1.0.a16 - 20060701

* Added patch supplied by Sorcerer for updated Netbots support

### Version 1.0.a15 - 20060520

* In IRC compatibility mode /bct will display msg being sent

### Version 1.0.a14 - 20060423

* Added tell command /bct

### Version 1.0.o13 - 20050123

* Fixed crash bug reported by LrdDread.

### Version 1.0.o12 - 20051021

* In last fix, I forgot to change the char spawn pointer

  in DoCommand. Fixed now.

### Version 1.0.o11 - 20051021

* Fix for fun bug that set name as the name of the mount when

  /bccmd connect used after login.

### Version 1.0.o10 - 20051017

* Added code to fix problem with high input \(ie. 6 Netbots at 125ms\) causing

  TCP backups, eventual buffer overruns, and horrid lags on eqbcs.

* Warning: High amounts of traffic can lag you. ;-P

### Version 1.0.o9 - 20051014

* Added color support \[+c+\], where c can be one of "yogbrtbmpwx"
* These are the same as the "\ac" codes for WriteChatColor.
* If the color char is uppercase, then dark version is used.
* Example: /bc Slow \[+g+\]Successful\[+x+\].
* Example: /bc Slow \[+r+\]Failed\[+x+\], retrying.
* Added new command to display colors, /bccmd colordump
* Added \(untested\) password ability. Requires recompile of eqbcs with

  login info redefined, see source comments both here and there.

### Version 1.0.o8 - 20051009

* Chat window locations now save/load by character.
* Requires eqbcs v1.0.3 or greater

### Version 1.0.o7 - 20051006

* Added CMD Support \(Ping/Pong implemented\)
* Added Window support. With CommandHistory \(shift up/shift down\)
* Added TLO. ${EQBC.Connected}
* Added beta Netbot Support.
* Tested, but some things may have stability issues. Let me know.
* Requires eqbcs v1.0.3 or greater

### Version 1.0.o6 - 20050926

* Added relog command, somewhat experimental.

### Version 1.0.o5 - 20050926

* * Handles zoning better.

### Version 1.0.o4 - 20050926

* * Added commands: togglecompatmode togglereconnect setreconnectsecs stopreconnect

### Version 1.0.o3 - 20050926

* * Now attempts to close socket when plugin is unloaded.

### Version 1.0.o2 - 20050926

* * Now recognizes when server is shut down.

## EQBCS

### Version 2.0.0 - 20101218 \(ASCII\)

* * Runs natively as a service in Windows
* * To install it as a service under Windows, add -c to the command line \(e.g. EQBCS2 -l c:\eqbcs.log -c will

  install the Windows service and configure it to log to C:\eqbcs.log\). The service will be installed to point to the

  same executable. EQBCS2 -d will remove the service.

### Version 1.2.i2 - 20081215

* * Added support for EQBC Interface by ieatacid

### Version 1.2.v1 - 20070116 \(vladus2000 addition\)

* * Added a 50 second ping. The client does not need to be changed for this

  as it already accepts a ping message. This should prevent the connection

  from crapping out. It also should speed up detection of dead users.

### Version 1.1.a12 - 20060807 \(ASCII's on crack release\)

* * Fixed the local echo check

### Version 1.1.a11 - 20060727

* * Changed version numbering system. It's up to you to decide if the 'a' is "ascii" or "alpha" :\)
* * Channel list saved in INI file and restored when you log in.
* to a channel you are in will be sent back to you \(as per toomanynames\)
  to a channel you are in will be sent back to you \(as per toomanynames\)

### Version 1.0.a10 - 20060725

* oldest server connection left a channel.
  oldest server connection left a channel.

### Version 1.0.a9 - 20060715

* * Added support for pseudo-channels. A /bct to channel goes to everyone in the channel.
* * New command: /bccmd channels channel\_list
* * Added ability to escape characters  will be translated to just 

### Version 1.0.a8 - 20060701

* * Apply patch from Sorcerer for updated Netbots.
* on non-windows.
  on non-windows.

### Version 1.0.a7 - 20060520

* Flush input buffer after processing tell to invalid username

### Version 1.0.a6 - 20060416

* Added support for tells. \(/bct\)
* Added command line options -p, -i, -l, -u and -d.
* -p  sets port number to listen on
* -i  IP Address of interface to listen on. Unspecified = ALL
* -d \(Unix only\) Run as daemon
* -l  log to file rather than STDOUT
* -u  \(UNIX only\) setuid to named user

### Version 1.0.o5 - 20051117

* Fixed name problem bug reported by DKAA.

### Version 1.0.o4 - 20051013

* * Fixed unix version not handling unclean disconnects properly.

### Version 1.0.o3 - 20051005

* * Made more clear where to add login password \(LOGIN\_START\_TOKEN\).
* * Changed select timeout to non debugging value, doh.
* * Added support for msgall. \(/bca\)
* * Added support for mq2netbots.
* \(ie. crash, plugin unload\)
  \(ie. crash, plugin unload\)

* * More cpu friendly.

### Version 1.0.o2 - 20050926

* * Made compatible with VC6

### Version 1.0.o1 - 20050925

* * Fixed hang on reading when closing. Now uses select to see if data exists
