# MQ2ChatEvents

## Description

**MQ2ChatEvents** The purpose of this plugin is to handle chat events in various ways. When a string \(and optionally a corresponding color\) is matched, several possible actions can be taken. Events are defined in the .ini file and can be enabled per character\_server. I've used this as a general replacement for in-game macros, Audio Triggers, and even some tasks I wanted available outside of a running MQ macro. I realize there are other plugins that do these various pieces individually, but I liked the idea of having it all under one configuration. Parts of the code were pieced together from other plugins and I tried to give credit where appropriate.

You can find the latest version of MQ2ChatEvents [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=18906&hilit=mq2chatevents).

## Features

Match strings and perform an event

`Play a sound`  
`Up to 100 different matchable strings per event`  
`Use in-game variables in matchable strings`  
`Handy for generating custom voice sound files:`[`http://www2.research.att.com/~ttsweb/tts/demo.php`](http://www2.research.att.com/~ttsweb/tts/demo.php)  
`Display a popup`  
`Define popup text, including the full text of the matched string`  
`Define popup color`  
`Define popup duration`  
`Execute Commands`  
`Up to 100 commands per event`  
`Use in-game variables in commands.`  
`One command executed per pulse`  
`Display chat that gets lost while zoning`

This information used to be seen by OnIncomingChat\(\) even though it was not displayed to the screen by the client. At that time, the messages could be captured and then printed after zoning was complete. Unfortunately, it looks like those messages are no longer seen by OnIncomingChat\(\) --- It's amazing that SOE has never fixed this. I left the functionality in the plugin, but turned the default options off since it no longer works as it originally did.

## Commands

Usage: /ce \

`Sound : Toggles playing of custom sounds`  
`Popup : Toggles displaying of custom popups`  
`MissedChat : Toggles popup notification after missing chat while zoning`  
`MissedChatEcho : Toggles echoing of missed chat to MQ window`  
`Commands : Toggles executing custom commands`  
`Verbose : Toggles verbosity on command execution. Echos the command before executing it (mostly to test variable substitution)`  
`On : Turns plugin On`  
`Off : Turns plugin Off`  
`Reload : Reload INI file`  
`Help : Displays the in game commands and shows the current settings`

## INI

INI Event Options:

`MatchString#=Chat string to match`  
`MatchColor#=Color to match. This must be the string name of a color defined in EQData.h`  
`Soundfile=Location of a .wav file to play when a match is found`  
`PopupText=Text to display as a popup when a match is found`  
`PopupColor=The color of the displayed popup when a match is found (again from EQData.h)`  
`PopupDuration=Time in ms that the popup should remain on screen`  
`Command#=Command to execute when a match is found.`

## Examples

`[JoinGroup]`  
`MatchString1=${PuppetMaster} invites you to join a group`  
`Command1=/nomodkey /notify GroupWindow GW_FollowButton leftmouseup`

`[AttackThis]`  
`MatchString1=AttackThis`  
`Command1=/squelch /stick off`  
`Command2=/melee on`  
`Command3=/if (${Me.CleanName.Equal[${MA1}]}) /target ${Spawn[${MATarget}]}`  
`Command4=/if (${Me.CleanName.Equal[${MA1}]}) /face`  
`Command5=/if (${Me.CleanName.Equal[${MA1}]}) /stick`  
`Command7=/if (${Me.CleanName.Equal[${MA1}]}) /killthis`  
`Command8=/rdpause off`

`[TellIn]`  
`MatchString1=tells you`  
`MatchString2=told you`  
`MatchColor1=USERCOLOR_TELL`  
`Soundfile=g:\\mq2\\sounds\\message-inbound.wav`  
`PopupText=`  
`PopupColor=`  
`PopupDuration=`  
`Command1=/if (${Me.CleanName.NotEqual[${PuppetMaster}]}) /bct ${PuppetMaster} "Received a TELL on <${Me.CleanName}>: #FULLTEXT#"`

`[TellOut]`  
`MatchString1=You tell`  
`MatchString2=You told`  
`MatchColor1=USERCOLOR_ECHO_TELL`  
`Soundfile=g:\\mq2\\sounds\\message-outbound.wav`  
`PopupText=`  
`PopupColor=`  
`PopupDuration=`  
`Command=`

`[TellRelay]`  
`MatchString1=Received a TELL on <`  
`PopupText=---Received a tell on a bot!---`  
`Soundfile=g:\\mq2\\sounds\\message-inbound.wav`  
`PopupDuration=10000`

`[OMMGaze]`  
`MatchString1=You feel a gaze of deadly power focusing on you.`  
`Soundfile=d:\\mq2\\sounds\\gaze.wav`  
`PopupText=---!!! GAZE !!! Click your mask now!---`  
`PopupColor=CONCOLOR_RED`  
`PopupDuration=7000`  
`Command1=/nomodkey /itemnotify ${FindItem[Mirrored Mask].InvSlot} rightmouseup`

`[gate]`  
`MatchString1=begins to cast the gate spell.`  
`Soundfile=g:\\mq2\\sounds\\gate.wav`  
`PopupText=#FULLTEXT#`  
`PopupColor=`  
`PopupDuration=`  
`Command=`

`[GoM]`  
`MatchString1=You have been granted a gift of mana!`  
`MatchString2=You have been granted a gift of radiant mana!`  
`MatchString3=You have been granted a gift of exquisite radiant mana!`  
`MatchString4=You have been granted a gift of amazing exquisite radiant mana!`  
`MatchString5=You've been granted a gift of dreamlike exquisite radiant mana!`  
`MatchString6=You've been granted a gift of ascendant exquisite radiant mana!`  
`MatchString7=You are granted a gift of phantasmal exquisite radiant mana`  
`MatchString8=You are granted a gift of gracious mana`  
`Soundfile=g:\\mq2\\sounds\\hoo-ah1.wav`  
`PopupText=~~ Gift of Mana! ~~`  
`PopupColor=`  
`PopupDuration=`  
`Command=`

`[DT]`  
`MatchString1=A dire disease creeps through your veins`  
`MatchString2=You feel the cold grip of death looming over you.`  
`MatchString3=You sense your doom approaching`  
`Soundfile=g:\\mq2\\sounds\\deathtouch.wav`  
`PopupText=~~ DT ~~`  
`PopupColor=`  
`PopupDuration=`  
`Command1=/bca I'm Death Touched!`

`[DA]`  
`MatchString1=You can't cast spells while invulnerable!`  
`Soundfile=g:\\mq2\\sounds\\DA.wav`  
`PopupText=`  
`PopupColor=`  
`PopupDuration=`  
`Command=`

`[MercDefDisc]`  
`MatchString1=tells the group, 'Initiating Fortitude Discipline.'`  
`MatchString2=tells the group, 'Initiating Final Stand Discipline Rk. II.'`  
`Soundfile=g:\\mq2\\sounds\\MercDefensiveDisc.wav`  
`PopupText=Merc defensive disc`  
`PopupColor=`  
`PopupDuration=5000`

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

