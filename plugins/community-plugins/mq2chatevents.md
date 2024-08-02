# MQ2ChatEvents

## Description

**MQ2ChatEvents** The purpose of this plugin is to handle chat events in various ways. When a string (and optionally a corresponding color) is matched, several possible actions can be taken. Events are defined in the .ini file and can be enabled per character\_server. I've used this as a general replacement for in-game macros, Audio Triggers, and even some tasks I wanted available outside of a running MQ macro. I realize there are other plugins that do these various pieces individually, but I liked the idea of having it all under one configuration. Parts of the code were pieced together from other plugins and I tried to give credit where appropriate.

You can find the latest version of MQ2ChatEvents [here](https://macroquest.org/phpBB3/viewtopic.php?f=50&t=18906&hilit=mq2chatevents).

## Features

Match strings and perform an event

`Play a sound`<br>
`Up to 100 different matchable strings per event`<br>
`Use in-game variables in matchable strings`<br>
`Handy for generating custom voice sound files:`[`https://ttsmaker.com/`](https://ttsmaker.com/)<br>
`Display a popup`<br>
`Define popup text, including the full text of the matched string`<br>
`Define popup color`<br>
`Define popup duration`<br>
`Execute Commands`<br>
`Up to 100 commands per event`<br>
`Use in-game variables in commands.`<br>
`One command executed per pulse`<br>
`Display chat that gets lost while zoning`<br>

This information used to be seen by OnIncomingChat() even though it was not displayed to the screen by the client. At that time, the messages could be captured and then printed after zoning was complete. Unfortunately, it looks like those messages are no longer seen by OnIncomingChat() --- It's amazing that SOE has never fixed this. I left the functionality in the plugin, but turned the default options off since it no longer works as it originally did.

## Commands

Usage: /ce

`Sound : Toggles playing of custom sounds`<br>
`Popup : Toggles displaying of custom popups`<br>
`MissedChat : Toggles popup notification after missing chat while zoning`<br>
`MissedChatEcho : Toggles echoing of missed chat to MQ window`<br>
`Commands : Toggles executing custom commands`<br>
`Verbose : Toggles verbosity on command execution. Echos the command before executing it (mostly to test variable substitution)`<br>
`On : Turns plugin On`<br>
`Off : Turns plugin Off`<br>
`Reload : Reload INI file`<br>
`Help : Displays the in game commands and shows the current settings`<br>

## INI

INI Event Options:

`MatchString#=Chat string to match`<br>
`MatchColor#=Color to match. This must be the string name of a color defined in EQData.h`<br>
`Soundfile=Location of a .wav file to play when a match is found`<br>
`PopupText=Text to display as a popup when a match is found`<br>
`PopupColor=The color of the displayed popup when a match is found (again from EQData.h)`<br>
`PopupDuration=Time in ms that the popup should remain on screen`<br>
`Command#=Command to execute when a match is found.`<br>

## Examples

`[JoinGroup]`<br>
`MatchString1=${PuppetMaster} invites you to join a group`<br>
`Command1=/nomodkey /notify GroupWindow GW_FollowButton leftmouseup`<br>

`[AttackThis]`<br>
`MatchString1=AttackThis`<br>
`Command1=/squelch /stick off`<br>
`Command2=/melee on`<br>
`Command3=/if (${Me.CleanName.Equal[${MA1}]}) /target ${Spawn[${MATarget}]}`<br>
`Command4=/if (${Me.CleanName.Equal[${MA1}]}) /face`<br>
`Command5=/if (${Me.CleanName.Equal[${MA1}]}) /stick`<br>
`Command7=/if (${Me.CleanName.Equal[${MA1}]}) /killthis`<br>
`Command8=/rdpause off`

`[TellIn]`<br>
`MatchString1=tells you`<br>
`MatchString2=told you`<br>
`MatchColor1=USERCOLOR_TELL`<br>
`Soundfile=g:\\mq2\\sounds\\message-inbound.wav`<br>
`PopupText=`<br>
`PopupColor=`<br>
`PopupDuration=`<br>
`Command1=/if (${Me.CleanName.NotEqual[${PuppetMaster}]}) /bct ${PuppetMaster} "Received a TELL on <${Me.CleanName}>: #FULLTEXT#"`<br>

`[TellOut]`<br>
`MatchString1=You tell`<br>
`MatchString2=You told`<br>
`MatchColor1=USERCOLOR_ECHO_TELL`<br>
`Soundfile=g:\\mq2\\sounds\\message-outbound.wav`<br>
`PopupText=`<br>
`PopupColor=`<br>
`PopupDuration=`<br>
`Command=`<br>

`[TellRelay]`<br>
`MatchString1=Received a TELL on <`<br>
`PopupText=---Received a tell on a bot!---`<br>
`Soundfile=g:\\mq2\\sounds\\message-inbound.wav`<br>
`PopupDuration=10000`<br>

`[OMMGaze]`<br>
`MatchString1=You feel a gaze of deadly power focusing on you.`<br>
`Soundfile=d:\\mq2\\sounds\\gaze.wav`<br>
`PopupText=---!!! GAZE !!! Click your mask now!---`<br>
`PopupColor=CONCOLOR_RED`<br>
`PopupDuration=7000`<br>
`Command1=/nomodkey /itemnotify ${FindItem[Mirrored Mask].InvSlot} rightmouseup`<br>

`[gate]`<br>
`MatchString1=begins to cast the gate spell.`<br>
`Soundfile=g:\\mq2\\sounds\\gate.wav`<br>
`PopupText=#FULLTEXT#`<br>
`PopupColor=`<br>
`PopupDuration=`<br>
`Command=`<br>

`[GoM]`<br>
`MatchString1=You have been granted a gift of mana!`<br>
`MatchString2=You have been granted a gift of radiant mana!`<br>
`MatchString3=You have been granted a gift of exquisite radiant mana!`<br>
`MatchString4=You have been granted a gift of amazing exquisite radiant mana!`<br>
`MatchString5=You've been granted a gift of dreamlike exquisite radiant mana!`<br>
`MatchString6=You've been granted a gift of ascendant exquisite radiant mana!`<br>
`MatchString7=You are granted a gift of phantasmal exquisite radiant mana`<br>
`MatchString8=You are granted a gift of gracious mana`<br>
`Soundfile=g:\\mq2\\sounds\\hoo-ah1.wav`<br>
`PopupText=~~ Gift of Mana! ~~`<br>
`PopupColor=`<br>
`PopupDuration=`<br>
`Command=`<br>

`[DT]`<br>
`MatchString1=A dire disease creeps through your veins`<br>
`MatchString2=You feel the cold grip of death looming over you.`<br>
`MatchString3=You sense your doom approaching`<br>
`Soundfile=g:\\mq2\\sounds\\deathtouch.wav`<br>
`PopupText=~~ DT ~~`<br>
`PopupColor=`<br>
`PopupDuration=`<br>
`Command1=/bca I'm Death Touched!`<br>

`[DA]`<br>
`MatchString1=You can't cast spells while invulnerable!`<br>
`Soundfile=g:\\mq2\\sounds\\DA.wav`<br>
`PopupText=`<br>
`PopupColor=`<br>
`PopupDuration=`<br>
`Command=`<br>

`[MercDefDisc]`<br>
`MatchString1=tells the group, 'Initiating Fortitude Discipline.'`<br>
`MatchString2=tells the group, 'Initiating Final Stand Discipline Rk. II.'`<br>
`Soundfile=g:\\mq2\\sounds\\MercDefensiveDisc.wav`<br>
`PopupText=Merc defensive disc`<br>
`PopupColor=`<br>
`PopupDuration=5000`<br>
