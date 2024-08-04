# MQ2MoveUtils:History

## The tonio era

The first version of [MQ2MoveUtils](./) was developed by tonio and released May 5, 2004.
_See:_ [_Original MQ2MoveUtils Discussion History_](https://macroquest2.com/phpBB3/viewtopic.php?t=6973)

The conception of this plugin was inspired by the /circle command, developed by Easar to be included in the earliest versions of [MQ2Twist](../mq2twist/). For all intents and purposes Easar should be considered the inspiration for this entire project.
_See:_ [_Easar's contribution to MQ2Twist / MQ2Twister\(abandoned\)_](https://macroquest2.com/phpBB3/viewtopic.php?p=42768#42768)

tonio did an amazing job enhancing the early versions of this plugin with features including: _breaking from mob gate, breaking from mob warp with distance configuration, autopause to prevent casting interrupts, stick behind, stick id, mpause, stick loose, and stick hold_

Contributors to the enhancement of MQ2MoveUtils after tonio stopped supporting it include: Bombadil \(_Binds for mpause_\), onetimehero \(_noface option_\), Lax, Cr4zyb4rd \(_TLO's & /stick pin_\), and rswiders \(_/moveto_\)

Quagmire offered full support for the plugin for a brief period in 2005, adding many bug fixes, code cleanup, and features such as: _/stick behindonce, walk/run switching, mount checking, and snare checking._
_See:_ [_Quagmire's MoveUtils_](https://macroquest2.com/phpBB3/viewtopic.php?t=10941)

=== The Outlander era === Outlander took over supporting MQ2MoveUtils on July 9, 2005.
_See:_ [_Outlander's MoveUtils_](https://macroquest2.com/phpBB3/viewtopic.php?t=11732)

Outlander's first big contributions to MQ2MoveUtils were his stuck logic, which started off as an [include file](https://macroquest2.com/phpBB3/viewtopic.php?t=11609), and the /makecamp command, which created a radius that you could use to prevent your character from moving out of range to chase down mobs or potentially gain unwanted aggro. Over time other additions included: _stick !front, HoTT awareness, and more TLO's_

Contributors to the enhancement of MQ2MoveUtils during Outlander's support include: dont\_know\_at\_all \(_bug fixes_\), ieatacid \(_bug fixes_\), somelamedruid \(_bug fixes_\), s0rcier \(_walk mode_\), deadchicken \(_loose moveto_\), bertbert \(_/followpath_\), Ralindal \(_bug fixes_\), and rswiders \(_many enhancements to /circle_\).

== Development History ==

## tonio

Version 2004.05.06:

* /stick now breaks when mob gates

Version 2004.05.07:

* /stick pause\|unpause added
* automatic /stick pause on casting
* /stick will break on a large enough sudden distance increment \(defaults to 250 units\)
* INI file support:

  A default ini file is created if it doesn't exist. Section \[Defaults\] contains global defaults. New sections can be

  added with character names as titles to override those defaults, for example:

AutoPause on/off enables/disables the automatic pause on cast feature \(regardless of this setting, bards won't pause /stick for casting... it's unneeded, and besides, that'd mean we can't sing while /stick'ing :\)\).
BreakOnWarp on/off enables/disables the automatic break on large distance increment
BreakDist sets how large a sudden distance increment is required for a break
BreakOnGate on/off enables/disables the monitoring chat for "targetname Gates." feature.

Version 2004.05.14:

* /stick pause changed \(now normal movement is possible w/o breaking stick while paused\)
* /stick hold added \(stores your current target, so that you follow it even if you lose or change your target later\)
* text output added to /stick
* /circle changed: if no center is given, current loc is taken to be the outside of the circle, not the center \(so you

  start angling immediately, instead of going straight then suddenly turning\)

Version 2004.05.16:

* slight bug fix with /stick
* added /cirlce drunken: use "drunken" instead of "on" to have /circle update heading less often for a more

  human-controlled look

Version 2004.05.17:

* coupla bug fixes

Version 2004.05.20:

* /stick behind added, tries to move behind a mob while sticking

Version 2004.06.14:

* /stick moveback added, tries to stay at exactly the stick distance
* /stick mpause added, causes manual movement to pause stick instead of breaking
* /stick loose added, checks for distance/angle less often, to give a more human-controlled appearace
* Added "Verbosity" to ini file \(set to 0 for no messages, 1 for normal messages\)
* Added "Stick" TLO, of type "stick", with members:

  Status \(ON, OFF, PAUSED\), Active \(bool\), Distance \(float\), MoveBehind \(bool\), MoveBack \(bool\), MovePause \(bool\), Loose

  \(bool\), and Paused \(bool\)

Version 2004.06.21:

* /stick uw added, for underwater /stick'ing, looks up/down to follow target

  \* this option should eventually disappear and become automatic... but as of now, mq isn't correctly reporting

  underwater status

* /stick - and /stick % added, to modify stick distance \(useful when a wrong melee range is reported\)
* /stick loose fixed
* /circle drunken upgraded \(uses slow turning\)

New version 2004.06.23:

* bug fix \(pause/unpause were clearing settings\)

2004.11.08:

* \(Lax\) Replaced the code shown here with the correct version as supplied by Bombadil. Note that InitializePlugin is

  called at load time, REGARDLESS of the state of EverQuest. In other words, CEverQuest might not even EXIST at the time

  of loading. Consequently, this plugin tried to initialize things too early and the bug was exposed by WinEQ 2.0 as a

  crash. Enjoy.

=== Quagmire === New version 2005.03.22: by Quagmire

* Cleaned up initialization slightly
* /stick behindonce added, moves you behind once then switches to normal stick
* /stick hold breaks when the target changes "state" \(ie: npc to corpse\)
* reduced the rate of calls to MQ2Globals::ExecuteCmd
* automatically switches walk/run mode when close to the target
* automatic pausing when sitting, stunned or have yourself targeted
* when the target is close and directly behind you, will back up instead of spinning and moving forward \(helps when you

  overshoot the target\)

Updated 2005.03.24:

* Merged in Cr4zyb4rd's Pin code
* Switched run/walk state reading to a new memory location

Updated 2005.04.20:

* Attempt to fix an infrequent crash.

Updated 2005.05.25:

* Fixed a null pointer crash when on a mount.

Updated 2005.06.05:

* Added automatic detection of being snared, won't go into walk mode.
* Stick / Pin won't kick in until you're close to the target.
* Several cleanups.

Updated 2005.06.26:

* Merged in /MoveTo code

=== Outlander === \* Corrections and additions 2005.07.08
Added Version Number at top of help commands
Added /stick id functionality
Added break MoveTo functionality so that when you manually move MoveTo is turned off

\* Corrections and additions 2005.07.14
Added break Circle functionality so that when you manually move Circle is turned off
Added MoveStuck logic to MoveTo and Circle commands
Adjusted the stuck distance to take into account the SpeedMultiplier currently on the character.
Adjusted the the MoveStuck stuckDist to be 1/3 of what it normally is if your under water.

\* Corrections 2005.07.19
Modified /stick movestuck logic when you are close to mob and are switched to walk mode, this was causing movestuck logic to be executed incorrectly.

\* Corrections 2005.09.19
Changed IsBardClass function to use GetCharInfo2\(\) instead of the old GetCharInfo\(\) function.

\* Corrections 2005.09.21
Changed movestuck logic for underwater to not kick in till you are not moving at all; pulse average = 0.

\* Addition 2005.09.26
Added new option: /stick !front
This option will keep you not in front of the mob, so off to the side or behind.
This option should reduce the amount your toon moves around during a fight with a mob when you are not the target as your will only adjust your position if you you are in the front 180 degrees of the mob, as long as you are in the behind 180 degrees you will not move around just because the mob shifts.

\* Addition 2005.09.28
Added HoTT check to stick, if sticking to a MOB or PC and you are their target
then if you are doing stick !front, behind, or pin you just do a a normal stick until
you are not the HoTT target then you go back to what ever option you had before.

\* Corrections 2005.09.28
Corrected problem with IsBardClass function, thanks BardOMatic and DKAA

\* Addition 2005.10.22
Added /makecamp functionality
Added /stick help, /circle help, /moveto help, and of course /makecamp help
Added some commands to all the functions
Changed the way some commands are parsed and changed the help command look

\* Corrections 2005.10.23
/makecamp is now a toggle for on/off
with mpause enabled any movement keys would spew a "no longer sticking to anything" message this has been fixed.
mpause option is now a toggle so if it was on doing /makecamp mpause will turn it off
INI load and save were reversed, this is now corrected
maxdelay variable being loaded from mindelay INI value, this has been corrected

\* Corrections 2005.12.13 - based off VZMule's post
Structure changes in last patch corrected in this version

\* Corrections 2005.12.19 - based off somelamedruid's post
added stickOn=true; to /stick hold and /stick id command parsers

\* Additions 2005.12.22
Added OnRemoveSpawn sub to help with crashes as posted by DKAA
Added /moveto id  functionality as discussed on boards.

* Updated 2006.02.27
* updated 2006.02.28
* Updated 2006.03.01
* Updated 2006.03.13
* Updated 2006.03.16
* Updated 2006.04.04
* Updated 2006.04.23
* Updated 2006.04.24
* Updated 2007.05.10 by rswiders \(added clockwise/counterclockwise circling; added forward and kiting \(backwards\) facing

  circling\)

* Updated 2007.05.18 by deadchicken \(added loose to /moveto\)

  \* Additions 2007.5.18

  Added loose option to /moveto to be similar to /stick loose and use gFaceAngle instead of directly setting heading. This

  also just turns without moving if angle is to great to avoid circling moveto location.

  Fixed some 180deg turns which were += 265 instead of += 256.

* Updated 2007.08.11 by bertbert \(added /followpath and /fp commands\)

\* 2007.08.11 - Added fp command to go to a person or location in a zone
\* Missed a return in new TLO StickTarget member
\* Added TLO object StickTarget
\* MoveTo, and Stick will stand you up if sitting
\* Changed a message display routine so it would not give you an incorrect break stick message
\* Fixed the CTD bug for the third time.
\* Fixed the CTD bug \(again\)
\* Opened the StickCommand, CircleCommand, MoveToCommand, and MakeCampCommand functions for other plugins for Sorcier
\* Added StandUp on /stick for A\_Druid\_00 \(thanks Sorcier, I just copied your StandUp\(\) code!\)
\* Fixed a CTD bug in the command processor for Stick.
\*Added in Sorcier's run/walk logic
\* Corrected a bug with /stick if your target was further away than your BreakDist from the MQ2MoveUtils.ini file then /stick would think your target had warped and would not stick.
\* Added some code to the bottom of the /stick command to account for this issue.
\* Added save of mPause setting so you can save your preference for mPause.
\* Changes Reduced Sensitivity on MoveStuck Logic by default from 0.8 to 0.1
\* Added Delay to resume movement after manually moving with mpause enabled. While each command has mindelay and maxdelay they all set the same variables so this only needs to be done once.
\* Added checks to stick, moveto, and circle to not kick in the MoveStuck Logic if you are stunned
