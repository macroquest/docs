# MQ2MoveUtils:v11 Revisions

\_\_FORCETOC\_\_

### MQ2MoveUtils v16.0 Revision History

#### Patch Fix for 16-Nov-2016

* Applied changes necessary because of the Nov 16th 2016 patch. \(trevyn\)

#### Made in Notepad only - v16.0717

* brainiac loves the D
* Fixed this bad code, a bug in the source for years that has always been wrong

#### Stable - v14.0416

* Added Circle Strafe Ability \(Cr4zyb4rd\)
  * /stick \[strafe \[left\|right\|flip\|random\]\]
    * Continuously strafes in one direction regardless of distance to target with no target-of-target check.
    * left\|right - direction to strafe
    * flip - strafes in opposite direction of last strafe command
    * random - strafe direction chosen by luck
* * I've found using
    * /stick strafe flip 50 moveback loose
  * lets me bow-kite a snared mob in a pretty tight circle, and I can just hit the same key again if I get too close

    to a wall or something and need to change direction. The only issue I've had is that mq2melee turns off all

    stick commands when it flips from melee to ranged mode, but I figured that's a problem better solved there than

    lying to mq2melee about what we're doing.

#### Stable - v11.0410

* Added Flexible sticking
  * /stick set flex on
  * /stick set flexdist \#.\#
    * between 2.0 and 20.0
  * Saves to INI under \[Stick\] as UseFlex=on/off and DistFlex=\#.\#
  * inline as /stick whatever useflex flexdist \#.\#

#### Stable - v11.0323

* Fix for brainiac's bullshit.
* Added ascii's VC6 auto-detection

#### Stable - v11.0319

* VC6 people can uncomment this line: //\#define OLD\_COMPILER\_USER
* StickCommand\("unpause"\) called via export will have a potential "plugin was not paused" error message

  auto-squelched.

* Added BreakOnHit option to Stick \(thank dkaa\)
  * /stick set breakonhit on \&lt;---perm
  * /stick 12 breakonhit \&lt;---inline
  * saves to ini under \[Stick\] as BreakOnHit=on
  * new TLO for this ${Stick.Broken}, which resets upon zone / next stick command usage

#### Stable - v11.0101

* ${Stick.Behind} now works when no commands are active.
* _/moveto_ now has a new parameter **mdist**, allowing you to change moveto distance on the fly instead of having to

  issue a _set_ or _/moveto dist \#_ command prior to the actual moveto command.

  * I left the old _dist_ as-is to not cause macro conflict.
  * **Note: In the case of** _**id**_**, you must use mdist first if you are not supplying the spawn id, i.e.**

```text
/moveto mdist 100 id

NOT

/moveto id mdist 100 \<----fails
```

* Dist3D change for snaproll to help when levitated now permanent.

#### Stable - v9.1231 - TLO Cleanup

* ${MoveTo.Stopped} now reflects if the last _/moveto_ command completed successfully.
  * Previously it measured if you were within your ArrivalDist of the last moveto location used.
  * If you were using this data for that purpose be aware if you move away from your /moveto location it will show

    as TRUE now.

  * This will reset to false the next time you issue a _/moveto_ command and upon gamestate changes.
* Fixed the PAUSED status for the following TLO's with no member:
  * ${MoveTo}
  * ${Stick}
  * ${Circle}
  * ${MakeCamp}
* ${MoveTo.Broken} once again functions as intended.

#### Stable - 9.0907

* Bug fixes for 0817

#### Beta - 9.0817 - non-linear

Major Changes

* The old style of movement has been reintroduced for WinEQ users i.e. those of you with problems of mouselook or

  strafe keys being left on when you alt-tab to switch sessions. You may switch over by using: /stick set wineq on

This saves to the ini under \[Defaults\] as WinEQ=on/off

* The true movement ability no longer makes the plugin offset-dependent. In the event the offset pattern changes and

  true movement is not established, the plugin should revert to the old style of movement so there would be no

  downtime or need to downgrade while waiting for an update.

* Heading settings are no longer command/INI situational. It applies to the plugin across the board. You may still

  apply inline adjustments for single command use only.

* To change plugin default headings, use:

```text
/stick set heading true
/stick set heading loose
/stick set heading fast
```

saves to the ini under \[Defaults\] Heading and character-specific section

* All commands now reset to INI \(user, not plugin\) defaults after each use.
* The INI no longer reloads every time you zone. It will only unload and reload defaults if you use the 'load'

  parameter \(ie /stick load\) or if you camp to character select and re-enter world.

* Loading the INI file will end commands in progress.
* Command parameters applied inline will no longer overwrite INI defaults. To change INI defaults, use 'set' or

  'toggle' to make changes permanent.

* The ability to use most INI settings inline has been added. This allows you to issue a command with the setting

  inline to apply it to the current command, and once the command has ended the next command will revert back to the

  INI defaults. As an example, if your snaproll default distance was 10.0 and you wanted to make your snaproll

  distance larger for a single mob, you could:

```text
/stick snaproll rear snapdist 20.0
```

...and this would snaproll 20 distance behind the target. The next snaproll you issued would then revert to using 10.0

* Complete list of supported inline additions:

_/stick_ breakontarget breakongate breakonwarp pauseonwarp randomize delaystrafe useback usefleeing strafewalk mindelay

## \(when used with stick, this applies to delaystrafe\) maxdelay \# \(when used with stick, this applies to delaystrafe\)

backupdist \# breakdist \# snapdist \# !frontarc \# behindarc \#

_/moveto_ breakonaggro breakonhit usewalk useback backupdist \# ydist \# xdist \#

_/makecamp_ returnhavetarget returnnoaggro returnnotlooting realtimeplayer scatter bearing \# scatsize \# scatdist \#

_/circle_ -already had all options

* Changed INI & Settings Information

I cleaned up the INI naming scheme a bit along with some additions and removals so take note of the following

\[Defaults\]

* BreakSummonDist --&gt; DistSummon
* new WinEQ
* removed TrueHeading
* new Heading \(true, loose, fast\)

\[Stick\]

* new AlwaysUW
* BehindArc --&gt; ArcBehind
* NotFrontArc -&gt; ArcNotFront
* BreakDist --&gt; DistBreak
* BackupDist --&gt; DistBackup
* new BreakOnTarget
* removed LooseStick
* SnaprollDist --&gt; DistSnaproll
* StickDistMod --&gt; DistMod
* StickDistModPercent --&gt; DistMod%
* new UseWalk
* new UseFleeing

\[MakeCamp\]

* new RealtimePlayer

\[MoveTo\]

* new AlwaysUW
* new DistBackup
* removed LooseMoveTo
* new UseBackward

\[Circle\]

* AlwaysBackwards --&gt; Backward
* AlwaysCounterClockwise --&gt; CCW
* AlwaysDrunken --&gt; Drunken

\[Character specific\]

* same changes as above where applicable
* added Heading, same as defaults
* added RealtimePlayer

New Features

* Added a new command "/rootme". This command will effectively lock your character in place until you turn it off with

  "/rootme off", preventing you via the keyboard or the plugin or /keypress from moving you forward. I figured this

  was within the scope of the plugin and may have some uses such as macro-based GM detection, or eqbc command passing

  for a character that is about to do something problematic. With rootme active, other commands will not work until

  you turn it off - though a makecamp on may still fight with it so consider this experimental for now.

* Added BreakOnTarget option to '/stick', which will break from the current stick if your target changes. /stick set

  breakontarget on, saves to the INI under \[Stick\] BreakOnTarget=on/off

* Added AlwaysUW options to both stick and moveto \(individually\). the current AutoUW option turns on underwater

  adjustments automatically only when you are underwater \(as intended\). The new 'alwaysuw' setting will instead always

  perform the stick or moveto as if you had typed 'uw' inline somewhere. /stick set alwaysuw on, /moveto set alwaysuw

  on, saves to the INI under \[Stick\] AlwaysUW=on/off && \[MoveTo\] AlwaysUW=on/off

* Added 'strafewalk' option to stick. This turns on walking when you are close to the target and using a strafe-based

  stick parameter. For characters with ridiculously high run speed this will help you position more accurately and

  should assist background sessions with moving slower and not overshooting the destination. /stick set strafewalk on,

  ini \[Stick\] UseWalk=on/off

* Added 'usefleeing' option to stick for 'stick front'. If the target is fleeing \(same check as the TLO\) and under 25%

  health, stick front will not attempt to strafe and reposition in front of the target. This is still experimental.

* Added 'useback' to moveto. Just like with stick, if you are close to the moveto destination \(which also includes

  camp returns\), this will walk backwards to the destination rather than turning, facing the destination, walking

  there, and turning again. /moveto set useback on, ini: \[MoveTo\] UseBack=on/off

* Set the distance same way as stick \(though unlike stick, you probably want a larger value here\) /moveto set

  backupdist \# \(1.0 min\). moveto and stick save their own distances, not use the same.

* Added 'realtimeplayer' setting to camp returning. Previous '/makecamp player' behavior set the location of the

  player, and began moving there. if the player moved during that time, it would walk to the old location first and

  then begin moving again. realtimeplayer now makes the positions dynamic and will adjust a return on the fly. i made

  this optional in case anyone used that as some form of ghetto advpath. /makecamp set realtimeplayer on

* BreakOnGM now displays a timestamp for zone in & zone out times. if you see one blink in and out within a matter of

  seconds, they went invis and you should not consider yourself safe.

Bug Fixes & Cleanup

* HideHelp now functions as the output message describes instead of in reverse.
* '/stick front' will no longer take the 'long way' around the mob to get back into position.
* Rewrote the UI window class to fix several bugs.
* Stripped the command history & output box from the UI window.
* The UI window should remain up when you are hovering
* When triggered, BreakOnGM & BreakOnSummon will prevent future commands from being used and output a message, rather

  than allow the commands to be accepted but then the plugin does nothing.

* ReturnHaveTarget, ReturnNoAggro, and ReturnNotLooting will now all perform their checks so that if you have multiple

  options enabled, one will not prevent the other from taking place.

* Changed the randomize formula a bit, though it may not have helped any.
* Setting the behindarc setting will actually take effect.
* Stucklogic should be less aggressive if a character is walking
* AutoPause will no longer apply if only makecamp is active and not returning
* Fixed the stick healer / uw parameter bug
* '/calcangle' has more data added to the output
* stick commands should no longer cause the character to run in circles around the target \(noticeably taking a while

  to correct itself\) if you turned it on when close to the target and facing certain angles.

* delaystrafe should now work exactly as intended / problem free, and i suggest using it always, especially for those

  who do not regularly have HOTT data

* mousepause & mpause will no longer try to resume when the plugin was paused by the user \(ie /stick pause\)
* if you ditch your stick target while mpause / mousepause is in effect, the plugin will take note instantly instead

  of waiting the normal delay time and then attempting to resume followed by breaking later

* pause/breakonkb \(with true movement\) should not interfere with your keypresses unless your ubermicro beats the speed

  of the threading.

* for mpause if you are using the oldstyle movement it will still behave as it did before \(if you hold down two keys

  and let one go, the timer starts from the first key even though you still have the second key held\).

* a bug with zoning while a pause was active causing keybinds movement to be broken while the plugin was loaded has

  been fixed \(rare case\)

#### Development - 9.0608 - verbosity rewrite, stick healer, breakongm

* Rewrote the verbosity system to be based off bit flags. This allows the user full control of every message that will

  or will not be displayed by the plugin. Read this wiki entry for the flags

  table and details on how it works, and what specific messages are tied to what bit flags. I have converted the old

  system, so if the new system is a bit confusing, _verbosity_, _fullverbosity_, _autopauseoutput_, and _totalsilence_

  still work very close to as before. I have not updated the wiki yet with the new commands, Usage:

```text
/stick verbflags - Lists your current verbosity bit flags (useful for knowing what to add/subtract from if you want to make a single change)
/stick set verbflags # - Sets your verbosity flags to # (where # is the total sum of whatever flags you added up, check the wiki link)
note: if you set # to 0 or a negative number, it is equivalent to totalsilence

Numerical flags value saves to the INI under [Defaults] as "VerbosityFlags" and to [server.char] section as well.
```

* The _totalsilence_ option now applies to everything, and not 'almost everything'.
* Added a new verbosity toggle so that you do not have to memorize 33554431, and may use \*/stick toggle

  totalverbosity\* to turn on every message possible.

* Added a new safety option, BreakOnGM. This works similar to BreakOnSummon. When active, it will scan OnAddSpawn for

  a GM type zoning in. If a visible GM/Guide does zone in, the plugin will halt any active MoveUtils commands and

  prevent future MoveUtils command usage until you unlock it \(same command as BreakOnSummon - _/stick imsafe_\). I

  highly recommend you turn on the verbosity bit flags for this if you are using this feature, as otherwise you may

  wonder why your commands are not working. Usage:

```text
/stick toggle breakongm
Saves to the INI under [Defaults] as "BreakOnGM"
```

* Added a new TLO member ${MoveUtils.GM}, which returns TRUE if the GM detection has fired and the plugin is currently

  locked.

* Added a new stick type, _/stick healer_. \*\*This does not work with any custom angles \(pin, front, !front, behind,

  behindonce, snaproll\).\*\* This is useful for those who may wish to stick their healer to another group member to keep

  them following without having them look like they are sticking. \*\*The main difference of this stick type is that

  until the character is out of stick range, it will not perform any heading adjustments\*\*. For example, currently if

  you stick your healer to your tank, every time the tank moves the healer would turn to be facing directly at the

  tank and it is very noticeable. With _/stick healer_, you can issue a command such as _/stick 100 hold healer_ and

  as long as your healer is within 100 range of the tank, it will sit still and not turn at all. Once the tank moves

  beyond 100 range, the healer would then turn to face it and move until it is within 100 range again.

* If you keep autopause off, targeting yourself while sticking will now halt your movement until you target something

  else \(unless you are using stick id/hold\). AutoPause on includes this functionality, but if you have it off and

  switched from an NPC to yourself with moveback enabled, previously you would try to move away from yourself, backing

  up forever. This displays a message as well, and is tied to the Autopause verbosity flag.

* Unducking will now also use /stand instead of hitting the duck key, which in very rare cases would also cause a

  server desync. WTB /stand as a native EQ mappable key.

* The fullverbosity message for stick will no longer display the mod output unless you actually have a mod active.
* The fullverbosity message for stick now will reflect HEALER if _/stick healer_ is used.
* Issuing _/makecamp on/player_ will no longer automatically stand the user up.
* Fixed a bug with BreakOnWarp / PauseOnWarp when using very large stick distances.

#### Stable - 9.0526 - UI window

* Added an optional dedicated UI window for the plugin.

  Usage \(may use any of the 4 commands\):

```text
/stick toggle window - toggles window display
/stick set font # - sets window font size (1 to 10)
/stick min - minimizes the window (like /mqmin)
/stick clear - clears the window (like /mqclear)
```

#### Development - 9.0524

* Added two more fixes to help prevent possible turn keys being left on
* Moveback will wait until snaproll and other drastic heading changes have completed before kicking in. \(thanks above

  posters\)

* Confirmed the 'moveto spinning' reported by Magoo was due to GetDistance3D not reaching its ArrivalDist. All moveto

  \(including 'id'\) and camp returns once again use GetDistance except the special case of /moveto y x z. If you supply

  a z parameter that your character cannot reach, you will rotate in place above or below the unreachable z point

  endlessly. Bottom line: use sanity checking on your z locations if you opt to use this. Don't guesstimate.

* BehindArc can now be set by the user. /stick set behindarc \#, saves to the INI under \[Stick\] "BehindArc" and the

  \[CharName\] sections.

* Snaproll distance can now be set by the user. This is the distance behind \(or in front/side if you are using custom

  position\) the target where the snap location is plotted. For reference, the default has been 10.0. If you frequently

  snaproll behind targets near walls and other tight objects with a large snapdist set you may run into problems.

  Usage:

/stick set snapdist \#, saves to the INI under \[Stick\] "SnaprollDist" and the \[CharName\] sections.

* New feature 'pauseonwarp'. Instead of breaking from stick like BreakOnWarp currently does, pauseonwarp will stop

  movement and pause until the target is once again within BreakDist range. Pause or Break, not both at the same time.

  saves to INI under \[Stick\] "PauseOnWarp" and command /stick toggle pauseonwarp.

* Tightened up breakonsummon formula to work more efficiently
* BreakSummonDist can now be set in game, not just via INI: /stick set summondist \#
* AutoUW defaults to false instead of true.
* TurnRate minimum lowered from 12.0 to 1.0. if you want to turn slow, more power to you.
* Useback has been cleaned up and should work more effectively.
* delaystrafe should work fully as intended and not fail to strafe in some cases - please report any more problems

  with this as it may need more testing \(thanks LrdDread\)

* /stick id \#, with self targeted, will work as intended \(thanks dkaa\)
* /stick hold, followed by /stick \[without hold\] will no longer reset incorrectly. if you were previously using

  /stick hold and then issuing a second /stick to make changes to active stick parameters while keeping the hold going

  this will no longer work.

* AutoPause with loose/true heading will no longer attempt to keep adjusting heading, and will halt turning when

  active \(thanks LrdDread\)

* Changed ${Stick.MovePause} TLO member to ${MoveUtils.MovePause} as it applies to more than stick.
* ${Stick.Behind} will now also be accurate from the target's right arc, not just the left.
* Camp returns use their own floats now, so that TLO members such as ${MoveTo.Stopped} and ${MoveTo.CampStopped} are

  reflected separately.

* Changed the fullverbosity output for stick from Head\(fast/true/loose\) Water\(yes/no\) Hold\(yes/no\) to only display

  what is active i.e.:

Head\(true\) ID\(31337\) Head\(true\) ID\(31337\) UW Head\(true\) UW MB \(the MB is new, and reflects if MoveBack is enabled\)

* /moveto loc y x z - will display the z loc in verbosity if used
* commands that shouldn't have a reason to stand up will not try to

#### Development - 9.0419 - bug fixes, uw enhancement

* Ending commands & pausing the plugin should no longer cause the turn keys to be left on. Please let me know if there

  are still cases where the "spinning" happens as I may not have got them all.

* Fixed an issue with stucklogic attempting to get unstuck when it was not.
* Stucklogic when underwater should no longer almost always think it is stuck. The current formula may not be tight

  enough so you may run into cases where stucklogic will not get unstuck while underwater. This will need more

  tweaking in the future. For now, this prevents the endless spinning when underwater.

* Stucklogic will no longer try to jump when underwater if TryToJump is enabled.
* Added a new option _AutoUW_ which will automatically turn on underwater face angle adjustments when fully

  underwater. This will affect _moveto_ and _stick_ commands when active and the plugin detects you are underwater and

  you have a target. **This is enabled by default.** If you frequently use _/moveto_ or _/makecamp_ while underwater

  and having a target unrelated to your destination, you may want to disable this option. Usage:

_/stick toggle autouw_ Saves to the INI as AutoUW under \[Defaults\] and \[server.char\] sections.

* The _/moveto loc_ command now accepts an optional Z axis. If you use _/moveto loc Y X_ as before, it will behave as

  it always did. If you use _/moveto loc Y X Z_, it will now use the Z axis in a GetDistance3D comparison. \(See Below\)

* Moveto now uses GetDistance3D instead of GetDistance to process being in range of ArrivalDist in some cases. If you

  currently use a small arrivaldist you may need to increase the size if when arriving at the moveto destination your

  character keeps attempting to reposition themselves. This only applies to _/moveto id_ or if the Z axis is supplied

  in the _/moveto loc Y X \[z\]_ format. This will not affect precisey, precisex, or camp returns.

* Moveto now accepts the _uw_ and _underwater_ parameters, which will adjust your face angle based on the height and

  location of your current target. Note you cannot _/moveto id uw_, but you can _/moveto uw id_ or \*/moveto id 12345

  uw\*

* Loose/True heading anti-orbit angle value is now able to be configured by the user. It still defaults to 32.0f, so

  if everything works fine for you there is no need to change it. You may adjust the value with:

_/stick set allowmove \#_ \(e.g. /stick set allowmove 64.0 \) Saves to the INI as AllowMove under \[Defaults\] and \[server.char\] sections.

* TurnRate cap has been increased from 24.0 to 100.0, though I wouldn't suggest going that high.
* the _pause_ parameter, and kb/mouse break/pause will now halt heading adjustments for loose/true heading \(previously

  seen example: typing /stick pause and seeing your heading still finish the rotation afterward\)

* gFaceAngle will now be reset by the plugin if moveto, circle, or stick is active \(meaning you cannot use /face

  during those cases\).

* Hitting turn left/right with breakonkb/mpause will once again allow you to continue turning
* UseBack defaults to false instead of true
* Added output for GetDistance and GetDistance3D to the _/calcangle_ command. \(Able to see the differences in distance

  to help set arrivaldist values based on your usage\)

#### Development - 9.0412 - Major Release

* All movement is now tied directly to the variables used by eqgame. This plugin now uses self-finding offsets, though

  they are no different than the current \_\_RunWalkState type of offset provided in the main compile. This has

  allowed me to end the over-compensation needed to stop movement and prevent the shooting off into the distance that

  plagued the original version. In testing, movement is less choppy and more accurate than ever before. As an extra

  precaution, I also have made the applicable keyboard flags reflect being pressed \(like MQ2's keybinds do\) while any

  movement is active. **YOU MAY NEED TO READJUST YOUR STUCKLOGIC SETTINGS**

* Along with this comes a new feature, "true heading". This uses the actual turn left and turn right movement keys to

  perform heading adjustments. **This is enabled by default** as loose heading was before. If you do not wish to use

  this, you may _/stick toggle alwaystruehead_ to turn it off for good. By using actual turning, the turnspeed

  multiplier and heading change increments are now 100% legit. Loose heading logic is still provided for those who

  want to go quasi-legit with a custom turn increment, and fast heading is the same as before. Note if you disabled

  loose heading because you want fast heading, you will now also need to disable true heading. When enabled \(again, it

  is on by default\) it will apply to stick and moveto both, not separately like loose heading works.

Ways to use this:

_/stick \_\_\_\_ truehead _- usable inline with any other parameters_ /stick toggle truehead _- toggle truehead for current command in process_ /stick toggle alwaystruehead _- toggle using it always Saves to INI as TrueHeading under \[Defaults\]. This also saves to the character-specific setting if \_savebychar_ is turned on.

* Added an optional strafe delay timer to prevent instant strafing when mobs turn for a short period of time such as

  quick spells, or gaining aggro without HoTT. Consider this, properly configured, a replacement to the old _nohott_

  and a fix to an issue reported by LrdDread.

Ways to use this:

_/stick toggle delaystrafe_ - turns the delay for strafe-based movement \(pin, !front, front, behind\) on or off _/stick set strafemindelay \#_ - sets the minimum amount of time you wish to delay before strafing \(in miliseconds\). The default is 1500 \(1.5 seconds\). _/stick set strafemaxdelay \#_ - sets the maximum amount of time you wish to wait before strafing \(in miliseconds\). The default is 3000 \(3 seconds\). Saves to the INI under \[Stick\] as DelayStrafe, and StrafeMinDelay / StrafeMaxDelay.

* The size of the arc for _/stick !front_ is now configurable by the user. You may use:

_/stick set !frontarc \#_ - Valid ranges 260.0 to 1.0. The default is 135.0 and if you do not adjust it, it will continue to behave like normal. Saves to the INI as NotFrontArc under \[Stick\]. This also saves to the character-specific setting if _savebychar_ is turned on.

* Implemented optional arc randomization for pin/!front/behind. You may enable this with _/stick toggle randomize_. My

  formula is pretty basic so it will not be anything special yet, but its a foundation for improvement in the next

  release down the road. This saves to the INI as RandomArc under \[Stick\], and if you have _fullverbosity_ enabled

  then behind/!front will also output their arc values to the chatwnd.

* Added a command, _/calcangle_, which dumps the value moveutils uses to determine angular dist \(useful if you want to

  configure your !front arc\) or know what the randomization values represent.

* When rewriting loose heading I had inadvertently disabled a feature of the original MoveUtils. With loose heading

  enabled: when very close to your target it would walk backwards to stick instead of turning to face the target,

  moving into stick position, and turning to face the target again. **This is now enabled by default**. I noticed in

  some cases it can end up causing your character to move in crazy-eight style patterns, and adjusted the math to

  correct this. Using _moveback_ in your stick commands overcomes that problem with ease, but if you do not like to

  use _moveback_ and/or run into that problem often, please report a solid way of recreating it here and then consider

  turning it off based on your play style. Unlike the old moveutils, I have made this feature optional.

Ways to use this:

_/stick toggle useback_ - turns the backwards walking on and off _/stick set backupdist \#_ - how close to the target you can be to use backward walking. **The smaller the better**. This defaults to 10.0 like the old moveutils Saves to INI as UseBackward and BackupDist under \[Stick\]

* Snaproll now uses GetDistance3D to prevent certain bugs related to being unable to get in range of a target on large

  slopes. I have left the old line in place so if you have any issues with snaprolls, you may uncomment the old line

  and comment out the new one \(fGetSnapDist around line 4100\)

* Snaproll now sets the final heading adjustment before handling control back over to normal stick.
* AutoPause now has an optional message output, so you can have greater awareness of why your character is suddenly

  standing still doing nothing. You may enable/disable this with _/stick toggle autopauseoutput_. If this is enabled,

  it will not respect _totalsilence_ so you will need to configure this on its own. This saves to the INI as

  AutoPauseMsg under \[Defaults\].

* MoveTo now has two new BreakOn options \(my implementation of a suggestion from dkaa\). They are different forms of

  detecting aggro during a _/moveto_ that will halt the command. This mostly assists macro writers in being able to

  stop moving to a location and handle the event of getting aggro during the move.

Ways to use this:

_/moveto toggle breakonaggro_ - this will halt the moveto if you gain aggro \(crossed-swords indicator\) _/moveto toggle breakonhit_ - this will halt the moveto if you are swung at \(both contact or miss\), if you want to keep moving until something is actually trying to hit you. I have added support for all three types of hitmodes, though if you use the "number only", I am only parsing for misses not the numerics \[and you are annoying to support\]. If you wish to use this, you should consider switching to abbreviated or normal. Saves to the INI under BreakOnAggro and BreakOnHit under \[MoveTo\].

In the event either of these trigger:

* A new TLO member, ${MoveTo.Broken} will show as true, so that you may see if the event fired. This will not reset to false until the next time you issue a _/moveto_ command. - An output message will display to the chatwnd \(if you do not have _totalsilence_ enabled\)
* Fixed a problem with the _/stick pin_ formula on one side of the target not positioning correctly.
* Camp returns and moveto's now resume after pausing the plugin and unpausing with _/stick pause\|unpause_.
* Mousepause will no longer spam if the pause flips active with only a makecamp setup and attempting to auto-return.
* Makecamp will no longer try to return while mouselook movement is active. Once the return begins and you attempt to

  use the mouse though it still will not let you, so if you use mouselook movement often consider turning on

  mousepause or breakonmouse.

* BreakOnGate has been switched from OnIncomingChat to a Blech event. Please report if this does not work as intended.
* Bard detection has switched from string parsing to numeric comparison. It will now only check once every time you

  type a command \(to support switching to shrouds with the plugin loaded\) instead of OnPulse. If you switch to a

  shroud with stick active, \[please stab yourself and then\] you will need to end the command and restart it to

  detect the class change.

* ReturnNoTarget has been renamed to **ReturnHaveTarget**, as the naming incorrectly implied the opposite of what it

  actually does. The command is also updated: _/makecamp toggle returnhavetarget_.

* Loose\(yes/no\) output in _fullverbosity_ has been changed to Head\(true/loose/fast\)
* MakeCamp Leash and Delay value output has been slightly modified.
* Fixed some cases where BreakOnWarp and BreakOnSummon would incorrectly fire \(mainly due to mpause/mousepause\) and

  cleaned up the logic.

* Removed _nohott_ \(AwareAggro in the INI\) as it has been nothing but problematic.
* Removed the MQ2Melee _/mutils_ output
* Renamed the keybinds, so you may want to cleanup your MacroQuest.ini after loading this.
* Nerfed the ability to _/stick id \#_ to your mount.
* Nerfed the ability to _/makecamp player_ to your mount.
* Major plugin logic overhaul, code cleanup, "best practices" and general bug fixes.

#### Stable - 9.0314

* Fix for strafe not properly turning off in some cases, most commonly if you got on HoTT \(thanks rswiders\)
* _nohott_ option will no longer process when it is enabled and you actually do have the HoTT LAA active and showing

  you on HoTT \(thanks fearless\)

* _nohott_ should be less aggressive and less prone to spinning endlessly \(relates to both fixes above and LrdDread's

  post a while back\)

* Bug Fix for BreakOnSummon \(= != ==\)
* Bug Fix for Debug options
* All MQ2Melee exports are now in the release, there will no longer be 2 separate versions of MoveUtils 9.x to worry

  about if you are using my changes to MQ2Melee.

* Misc. code cleanup and dewindefification

#### Stable - 9.0225 - minor

* Fix for verbosity level output bug that has been present since the change to the way this works in November.

#### Stable - 9.0110 - minor

* _/makecamp Y X_ and _/circle y x_ are no longer valid inputs. this may break some macros.
* Added new syntax: _/makecamp loc Y X_ and _/circle loc Y X_ as replacements. Please report if any problems or odd

  behavior due to this change.

* TurnHalf is now functional again for stucklogic. Saves to ini or toggled via command line: _/stick toggle turnhalf_
* Snaproll left/right math corrected by deadchicken
* Added _${MoveUtils.Version}_ TLO member by request

#### Stable - 9.0101 - fixes/TLO

* Most problems reported should be fixed. Get this version and delete your ini file. Anyone that was using loose

  heading and had issues they should be corrected now as well, as long as you delete your INI file.

* Corrected a bug with camp return and moveto.
* Corrected a bug with makecamp return and altreturn if too close to camp.
* Camp return scattering should once again function as deadchicken intended.
* CampRadius now stores to the character section of the INI file.
* Adjusted the default values for stucklogic a bit \(not the only reason to delete the ini\)
* Returned keypress down, up and down, up, down as not having it causes characters to run off into the abyss in some

  cases.

* Added New TLO's:

${MakeCamp.ReturnNoAggro} - bool  
${MakeCamp.ReturnNotLooting} - bool  
${MakeCamp.ReturnNoTarget} - bool  
${MakeCamp.Scatter} - bool  
${MakeCamp.Bearing} - float  
${MakeCamp.ScatDist} - float  
${MakeCamp.ScatSize} - float  
${MoveTo.ArrivalDist} - float  
${MoveTo.ArrivalDistY} - float  
${MoveTo.ArrivalDistX} - float  
${MoveTo.UseWalk} - bool  
${MoveUtils.PulseCheck} - int  
${MoveUtils.PulseUnstuck} - int  
${MoveUtils.DistStuck} - float  
${MoveUtils.TryToJump} - bool  
=== Beta - 8.1227 - bug fixes === **note: this was a bad release, if you are still using it, delete it.**

* Cleaned up loose heading function to not set heading to illegal values
* Removed the excessive double/float conversions. Circle radius and gLookAngle should be the only double math used

  anymore.

* Fix for leash bug reported by Kroak

#### Beta - 8.1224 - tweaks

* _snaproll_ now has a distance check so if it is close enough to the destination it will not try to roll again a very

  small amount in place. snaproll moves 10 units away, and this new distance check is 5 units.

* _snaproll_ will now accept destination as a parameter. Usage:

  ```text
  /stick snaproll rear
  ```

  * \(normal behavior and not necessary, you can use _/stick snaproll_ as before\)

```text
    /stick snaproll face

-   front of target


    /stick snaproll left

-   snaproll to the target's right shoulder


    /stick snaproll right

-   snaproll to the target's left shoulder
```

* **If enabled...**
  * stucklogic will no longer try to jump when levitating
  * stucklogic will no longer try to jump if not moving
  * stucklogic will now work if using strafing
  * stucklogic will now be used whenever stick is active, instead of not if you are within stickdist \(except the

    normal skip conditions: summoned, stunned, snared, rooted\)

  * Autopause will now apply to rooted
* No commands will try to move if rooted
* Fixed pin/!front/rear errors when snared
* Changed DoMovement to not press up and down again

#### Beta - 8.1221 - deadchicken stucklogic rewrite

* Stucklogic has gotten a major overhaul - \*\*It is highly recommended that you delete your old INI and re-set / copy

  over any values you wish to keep not related to stucklogic\*\*.

* Stucklogic uses new values for a new formula written by deadchicken. This formula calculates your pulse averages based on a table, with greater accuracy than before. The new values are configured as such:

  ```text
  /stick set pulsecheck #
  ```

  * pulsecheck defaults to 4
  * this value is sort of what "stuckcheck" was before.
  * it serves as the size of your pulse history to be used to calculate your average movement distance. the largest

    you can set this value to is 32 \(defined by MAXRINGSIZE\). The higher you set this number, the less often

    stucklogic would misfire \(so if you are getting the "jittery" problem you will want to increase this value\).

    This also means it will take longer to know that it is stuck, so if you are getting stuck and not responding

    fast enough, you would do the opposite and lower this value.

```text
    /stick set pulseunstuck #

-   pulseunstuck defaults to 5
-   this value is new
-   this is the amount of pulses you have successfully moved forward before hard-forcing stucklogic to be considered
    unstuck. this serves the purpose in that if you were stuck for 20 pulses, your stuck counter would normally try
    to move forward for 20 more pulses before considering itself free. there was some handling for this that had
    some issues so now you can set a value such as this one to force a faster "im unstuck" process.
-   the higher your framerate, the higher you want this value. 5 may not be enough on better computers and you may
    end up getting restuck again, it will look like what we are calling "snaking". If you notice yourself "snaking"
    then this would be the first value to try increasing.


    /stick set diststuck #.##

-   diststuck defaults to 0.5
-   this is similar to before in that it is the amount of distance you need to have moved versus your average pulse
    rate in order to not be stuck
-   this value should properly scale for all speeds of computers. you may want to set it higher or lower, play with
    it and find what works best (and please let us know!!), but keep in mind setting this value to something tiny
    such as 0.001 as we did in the old logic should no longer be necessary. deadchicken has determined that mindset
    was only working because of some incorrect math in the formulas. try to stick with more logical values and then
    reporting back your results would be appreciated.
```

* '''The following needs more testing/information:
  * stucklogic behavior when snared
  * stucklogic behavior underwater
  * stucklogic behavior when mounted \(all different speeds of mounts\)'''
* Please note the old values and logic behind setting them no longer applies. I've changed their names in the INI so

  that no one can mistakenly use crappy settings because they did not read any of this.

* Added jumping support, which will try to jump to overcome obstacles. For as simple as this sounds, this will prevent

  you from getting stuck on small obstacles the majority of the time. It works awesome, to the point we had to disable

  it to test a lot of the other aspects of the new formulas. This defaults to true, so if undesired you may disable

  this with _/stick toggle trytojump_ \(or set on/off\)

* Stucklogic now uses GetDistance3D instead of GetDistance to compare movement between pulses, so changes in z axis

  should be factored into movement. This should correct the bug with stucklogic firing when walking up and down

  inclines, but please report if it is working as intended or not. It was working correctly in our testing.

* Rewrote a lot of the main function to reduce the number of evaluations processed per pulse by 30% \(made up figure,

  it was a large portion\)

* Bards can once again use AutoPause \(all aspects except casting spells\)
* _/stick snaproll_ should now be 100% accurate and no longer overshoot the target due to getting stuck along the way.

  Thanks deadchicken for his camp scatter math which worked perfectly for this formula too. Please report any cases

  where it is having problems, but I hope there should be none now.

* Switching targets mid-stick will no longer trigger stucklogic or breakonwarp. If you target a mob that is out of

  server-update radius, breakonwarp can still fire once you receive accurate location data for the target. Cross-map

  targeting stuff is bad, let alone with **stick still on**.

* _breakdist_ may now be set in game with _/stick set breakdist \#.\#\#_
* Added a new feature to MakeCamp courtesy of deadchicken: scattering.

This is a bit complex but when configured properly it is amazing. The idea behind this is that instead of returning to a random location within your camp radius, you can define a specific bearing, distance, and scatter radius from the center of your camp. This way you could configure your characters to return to specified areas all the time. The INI supports values on a character by character basis as well, so you could configure your tank to return to the center, your casters to return behind the tank, and your melee to return to the sides of the tank.

* To configure the values the commands are:

  ```text
  /makecamp toggle usescatter
  ```

  * Turn on/off scattering

```text
    /makecamp set bearing #.##

-   set scatter bearing


    /makecamp set scatsize #.##

-   set scatter radius


    /makecamp set scatdist #.##

-   set scatter distance
```

* Leash length can now be set to &gt;= camp radius, instead of just &gt;
* AltCamp now retains its own radius size.
* Added new MakeCamp TLO's relating to the distance from your camp.
  * _${MakeCamp.CampDist}_ - float - distance from your current camp \(0.00 if makecamp is off\)
  * _${MakeCamp.AltCampDist}_ - float - distance from your altcamp \(0.00 if altcamp has not been established\)
  * _${MakeCamp.AltRadius}_ - float - radius size of your altcamp  
* MoveTo now allows for ArrivalDist to be set as low as 1.0.
* MoveTo now has the option to turn on walk when closing in on the arrival destination to maximize precision. This

  defaults to true so if you do not want to use this, then _/moveto toggle usewalk_.

* Autosave \(save to INI when issuing a _set_ or _toggle_ parameter\) now defaults to true.
* Added _savebychar_ as optional for the INI. Defaults to true as that was the old behavior. Use \*/stick toggle

  savebychar\* to disable saving/loading character-specific settings.

* Added optional INI value \[YourCharName\] "DisregardMe=true". This allows you to use character-specific settings but

  ignore them on a specific character and use defaults instead. Manually add this line for the characters you wish to

  use defaults on, and leave it off \(or you could put =false, but no need\) for those you wish to continue using

  specifics.

* Fixed a crash bug related to using _/stick id 2mooks_. The "id" parameter now enforces all numerics. strtoul ftw.
* Fixed a bug with stick 'always' not processing mpause/mousepause/breakonkb/breakonmouse if you had a target when you

  issued the command, until you had no target and got a new target again.

* Fixed a small bug with min/max delays requiring 126 instead of 125 difference.
* Fixed a bug where if you unloaded the plugin mid-command walk would be left on.
* Fixed a bug with breakonsummon firing the first time you issued a command.
* Disabled _advancedautopause_ as I'm out of ideas.
* _checkbard_ has been removed \(forever\).
* Stripped _/followpath_ from this plugin. Use MQ2AdvPath instead.
* Other new set / toggles:
  * _/circle set circleradius \#.\#\#_ - set radius on the fly
  * _/makecamp set leashlength \#.\#\#_ - set leashlength on the fly
  * _/makecamp set campradius \#.\#\#_ - set camp radius on the fly
  * _/makecamp toggle leash_ - toggle leash on and off
* Cleaned up the debug command output.
* Cleaned up the help command output.
* Added new help command format to display detailed information on the plugins settings as it has grown large.

  \(_/stick help settings_\)

* All options that could previously be toggled or previously be set on/off now may be used both ways. So for example

  autopause, you have the option of doing:

```text
/stick toggle autopause
/stick set autopause off
/stick set autopause on
```

Use the "help settings" parameter for more information.  
=== Beta - 8.1205 - deadchicken polar math ===

* Corrected the bugs with BreakOnSummon that would cause occasional misfires in _/stick_, and consistent misfires with

  _/circle_. This feature now works as intended \(and its very useful in gm-detection detection\).

* deadchicken has generously offered up his polar-math code for camp returns, which is much smoother, more seamless,

  and far more accurate in generating a return to camp. This also makes _/makecamp player_ work much better. Many

  thanks to deadchicken for this simple yet elegant contribution to the plugin.

#### Beta - 8.1202 - makecamp cleanup

* makecamp return delay and mpause/mousepause resume delay are now on separate values. They are now able to be

  configured independently via commandline or within the INI.

  * Important: The old ini values no longer apply, so if you use non-default settings you need to adjust them again

    based on the following

    * \(you can use any command, its not restricted to _/makecamp_\)
    * To set the delays for camp return

```text
    /makecamp set campmindelay #.##

    /makecamp set campmaxdelay #.##

-   -   To set the delays for mpause/mousepause return:


    /makecamp set pausemindelay #.##

    /makecamp set pausemaxdelay #.##
```

* You will now need to use different INI values for these delays. \[Defaults\] "MinDelay" and "MaxDelay" no longer do

  anything.

* For mpause/mousepause:

```text
[Defaults]
PauseMinDelay=125
PauseMaxDelay=250
```

* For makecamp return times:

```text
[MakeCamp]
MinDelay=250
MaxDelay=500
```

* The ${MakeCamp.MinDelay} and ${MakeCamp.MaxDelay} members now refer to the campmindelay and campmaxdelay settings

  only

* There are new TLO members for the pausemindelay and pausemaxdelay settings: ${MoveUtils.PauseMinDelay} and

  ${MoveUtils.PauseMaxDelay}

* This change has allowed for the return of inline min/max delay for makecamp, you can use it as it was before.

  Examples:

```text
/makecamp mindelay 150 maxdelay 500
/makecamp on maxdelay 500
/makecamp on mindelay 150 maxdelay 500
```

* There is now the ability to retain an "altcamp" location stored. Right now this is only used for one purpose, being

  able to return to the altcamp location. This is very barebones at the moment, and works as follows

  * You go to a location and turn on a camp \(ie /makecamp on\)
  * You turn off your camp \(ie /makecamp off\)
  * The location that was your camp is now the altcamp location.
  * You now have two options to utilize the old camp:
    * At any time, as long as you remain in the same zone, you can _/makecamp altreturn_. This will return you to

      the altcamp location, aka the location of your camp that is now off. This works how makecamp return with no

      camp active tried to work, but without the bugs that existed with it.

    * You move to another location and setup a new camp \(ie _/makecamp on_\). With this new camp active, you can

      _/makecamp altreturn_. This will turn OFF your current camp \(so as not to get stuck trying to stay there\)

      and move to the altcamp location.
  * Note: You cannot altreturn until you've setup a camp at least once in the current zone.
  * Note: The Altcamp values reset if you die or zone.
  * Note: You cannot altreturn if currently using a player-camp.

* There are two new TLO members that keep track of the altcamp location. If they are both == 0.0 then you do not have

  an altcamp setup. They are ${MakeCamp.AltAnchorX} and ${MakeCamp.AltAnchorY}

* The "on" parameter for _/stick_ may now be used anywhere inline again, since removing that broke popular macros like

  RH. Please note the on parameter is useless in this version of MoveUtils. In the original version it was able to

  overcome a bug with breakonwarp \(which is fixed\), so now it does nothing that any other _/stick_ parameter does not

  do. This is only for retro-support, using it in your macros is bad practice.

* If you use _precisey_ or _precisex_ as a parameter in your _/moveto_ command, it will now display your YDist or

  XDist values in the output \(sorry for the long delay in this request\)

* Added an experimental features for those of you bards that are having the "jittery" problem when StuckLogic is

  enabled. Following the suggested quickfix earlier in the thread, if you enable a new option _checkbard_, your

  speedmultiplier is divided by two if you are a bard class. This only applies to bards, not everyone with selos. This

  feature is disabled by default, so if you wish to test it, use \(_/stick set checkbard on\|off_ then _/stick save_\).

  This saves to the ini under \[Defaults\] "CheckBard"

  * Turning this on as a non-bard will not do anything, so turning it on for your bard alt and loading up another

    character will not affect your non-bard.

  * If this solution works, I could work on detecting if selo's is present and open this to all classes, but I think

    it would be better to find out what the problem in the stucklogic formula is, and try to fix that instead. If

    you wish to help, please read a few posts back about the formula and issues.

* For those of you who wish to return to camp when you are outside of the camp radius, regardless of if you have a

  target or aggro, there is a new option ReturnNoTarget. The previous new feature ReturnNoAggro will ignore target as

  well, but only return if you do not have aggro. ReturnNoTarget works with ReturnNoAggro OFF, and will return when

  you exceed the camp radius, target or not. Thanks to Muley for the suggestion. Usage \(**/makecamp enforced**\):

```text
/makecamp set returnnotarget on|off
```

* This saves to the INI

```text
[MakeCamp]
ReturnNoTarget=on
```

* Identified a bug with _snaproll_ where it would not stop moving/readjust heading if stucklogic kicked in or if the

  player moved with mpause/mousepause in the middle of the roll.

  * I've taken steps to correct the issue. If you are close to the target, the problem should be gone unless your

    snaproll runs you into a wall. If you are far away from the target, there is a chance your roll will still

    continue on beyond the normal distance \(due to stucklogic or mousepause/mpause\) but it will now halt if it

    travels the same distance beyond the target that you were when you issued the command.

  * The problem would still exist if you snaprolled from 100 units away, got stuck along the way, you will run 100

    units beyond the mob before snaprolling. I'm working on a better formula to address this problem.

  * In the meantime, snaproll still works as it did before, just with more checking and correction of

    heading/movement. Shortrolls should have little to no problem.

  * This feature will be improved in the future.

* Cleaned up the help command output to reflect new settings that were missing, or settings that no longer applied. A

  few of the newer ones may still be missing.

#### Beta - 8.1123 - loose enhancement

* Rewrote loose heading to be calculated and adjusted within this plugin, using a fixed turn increment
  * **Note:** the maximum rate you turn when holding the right/left keys down is 16.0, and hence the default
  * This turn increment can be configured by the user for any number within 12.0 and 24.0
  * Lower than 12.0 will cause awkward stuttering
  * Higher than 24.0 is noticeable hax and you may as well use fast heading
  * To configure in game, you may use _/stick set turnrate 12.0_
    * If you use a value out of bounds, it will not change the rate
  * To configure in the ini, you may use \[Defaults\] "TurnRate" section
    * If you use a value out of bounds, it will use the plugin default of 16.0 and resave this value to your ini
* Adjusted _/stick snaproll_ to use this new math, and improved the calculations to determine when to roll so it

  should no longer roll early

#### Beta - 8.1119 - minor

* Removed ${Stick.Aggro} TLO
* Added ${MoveUtils.Aggro} TLO
  * this TLO now functions any time you have a target instead of only when _/stick_ is active
  * This check is still calculated the same way, it is not "true" aggro detection
  * This checks your target's heading relative to your heading via angular distance math. If you are facing your

    target and your target is facing you, you are aggro. If your target is facing you and you are facing AWAY from

    your target, the math will show your aggro as false

  * ideally this is still only worth using if you are facing your target \(which _/stick_ always did\) and not in any

    other case
* By request, added _/stick snaproll_ \(thanks Agripa for the name, which is based off flight terminology\)
  * This command is designed to be used like _/stick behind_
  * This runs in a straight line to the rear arc of the target based on your targets heading, spins in place, and

    then turn on _/stick behind_ automatically afterwards

  * This uses and enforces loose heading/stick, so it will not snap your heading instantly
  * I have not incorporated this into NoHoTT checking so either use this \(by detecting ${MoveUtils.Aggro} is true

    have your macro issue the command\) or nohott but dont try to use both together as they do opposite things
* By request, added an option to _/makecamp_, ReturnNotLooting, which will not return to camp automatically until you

  no longer have a loot window up \(or manually issued a _/makecamp return\)_

  * This defaults to false so everything behaves as you are familiar with
  * If you wish to use this, it can be set up as follows
    * \[MakeCamp\] "ReturnNotLooting" on/off in the ini
    * _/makecamp set returnnotlooting \[on\|off\]_

#### Beta - 8.1116 - minor

* Fix for _/makecamp_ no parameters
* Added _status_ parameter which dumps the status of the command used, or _status all_ which dumps complete status of

  the plugin

  * _/moveto status_ will only display info related to moveto, circle status only to circle, and makecamp status

    only to makecamp

  * _all_ for every command will dump status for every command as well as all other plugin settings
  * These will display regardless of if you have totalsilence set to on
  * Example:

```text
    /stick status

will output
```

```text
MQ2MoveUtils Current Status
Stick: Status(on) Dir(Behind) Dist(10.0) Mod(0.0) Mod%(0.0) Loose(yes) Water(no) MoveBack(yes) Hold(yes) Always(yes)
Stick: Holding to ID(1115) Name(Guide Peyote)   <---only displays if holding
Stick Options: AlwaysLoose(on) BreakOnWarp(on) BreakDist(300.00) BreakOnGate(on)
```

#### Beta - 8.1111 - moveto enhance / misc

* By request, added new parameters to _/moveto loc_, _precisey_ and _precisex_
  * When used these will move in the general direction of the loc specified and stop moving when it gets in the

    acceptable arrival distance for that location, disregarding the other

  * This is to be used as a trailing paramater to _/moveto loc_
  * Using it with _/moveto id_ or the new _/moveto yloc/xloc_ will likely cause problems so don't do it
  * Usage example:

```text
    /moveto loc -100 -200 precisey

-   will head towards -100 -200, but stop when it gets within acceptable Y arrival distance even if your loc is -100
    -500
-   This is not the same as new command */moveto yloc/xloc* in that it does head in the desired direction first
    until it reaches the "precise" desired
-   The other command below will beeline with no regard to the other coordinate
```

* Added two new settings to support the _precisey_ and _precisex_ trailing parameters
  * These also save to the ini under \[MoveTo\] as "ArrivalDistY" and "ArrivalDistX"
  * Usage:

```text
/moveto set xdist 10.00
/moveto set ydist 10.00 (default is 10, can use any .2 digit float)
```

* Changed INI setting for \[MoveTo\] "ArrivalDistance" to "ArrivalDist"
* Added _/moveto yloc \[\#\]_ and _/moveto xloc \[\#\]_ which will use your current x\(yloc\)/y\(xloc\) and beeline for the

  x\(xloc\) or y\(yloc\) you requested

* Included fix for _/moveto dist_ reset problem reported by KFH
* By request, added a new option for makecamp returning only if not aggro
  * currently if you have a camp setup makecamp will return to camp if you are outside of the camp radius and do not

    have a target. this is still the default, so if you like this, you don't have to do anything

  * if you wish to change this so that you will return only if you are not aggro, with or without a target, you can

    enable this using:

```text
    /makecamp toggle returnnoaggro

-   this will also save to the ini under \[MakeCamp\] "ReturnNoAggro" (on/off)
```

* Makecamp returning on its own \(meaning any case other than typing in _/makecamp return_\) will no longer display the

  "Arrived at /moveto location" message

* Makecamp returning on its own will no longer display halt/pause messages when using breakonkb/mouse or

  mpause/mousepause since it continually will retry until camp is turned off

  * using _/makecamp return_ still will display the messages

* Makecamp returning on its own now respects mpause/mousepause and will not try to fight you for returning to the camp
* Moved _toggle_ and _set_ parameters to their own function
* mindelay & maxdelay can no longer be used inline as a parameter since they apply to multiple things and this created

  some problems. instead they are now adjusted with the set parameter \(any command\)

  * the minimum for mindelay is still 125, so if you try to set this lower it will default to the plugin

    default \(500\)

  * the minimum value for maxdelay is still mindelay+125, so if you try to set this lower it will set to current

    mindelay+125

  * Usage:

```text
/stick set mindelay 125
/circle set maxdelay 250
```

* Updated AutoSave to only save if you adjust a setting with _toggle_ or _set_ instead of every time a command is

  typed since that makes more sense and is less resource intensive

* Added rswiders' change for bRunNextCommand = true for the 4 main commands \(followpath still getting overlooked\)
* Lowered default camp radius from 100 to 40
* LeashLength can now be set = CampRadius in the ini instead of CampRadius+10
* Made a new ResetCamp function to reset camp values similar to EndPreviousCmd for the other 3 commands
* Entering valid parameters followed by an invalid parameter for /stick, /moveto and /circle will no longer output

  help and continue trying the command, the command will now fail

* turning a command off or typing a new command that resets a previous command with loose heading will halt the loose

  heading from trying to finish turning. same applies when using loose moveto when you have arrived at your

  destination, it will no longer continue turning once it has arrived \(previously only noticeable in short moveto's\)

* _/stick toggle spinme_ for use with _/stick front_ has been removed. This is now set with \*/stick toggle

  nohottfront\* and saves to the ini under \[Stick\] "AwareNotAggro" \(on/off\) so you only have to type it once if you

  wish to use it

* To stay in line with this change, previous "AggroAwareness" \(on/off\) in the ini renamed to "AwareAggro" \(\*value for

  the nohott option on/off\*\)

* Adding on to the ability to _/stick set stucklogic on/off_, you can now set more values. "stuckcheck \#" and

  "stuckdist \#", i.e.:

```text
/stick set stuckdist 0.001
/moveto set stuckcheck 8
```

* StuckDist, StuckCheck, and TurnIncrement can no longer be set to zero in the ini or via command. If you want to

  disable stucklogic use _/stick set stucklogic off_ instead

* You are now able to disable stucklogic's check for if you are facing exactly halfway away from your destination to

  start turning back the same way it was turning from

  * This is currently only in the INI but will soon be added to the set parameter
  * \[StuckLogic\] "TurnHalfway" \(on/off\)

#### Beta - 8.1101a - CTD fix

* fix for ctd
* more checks added to prevent future ctd \(\*thanks ieatacid & dkaa for help finding the reason: dont call ExecuteCmd

  to press keys if not in game\*\)

#### Beta - 8.1030 - minor bugfix

* Keybinds will no longer interfere with normal gameplay if a command is not active \(\*or if stick always is on but you

  do not have a current npc target\*\)

#### Beta - 8.1029d - sit/stand bug finally gone

* Changed all references of GetCharInfo to check pCharSpawn \(which we determine is valid first\)
* Fixed circle 'alwaysccw'/drunk/etc & stick alwaysloose values to not reset after one usage
* ${Stick.Aggro} TLO now returns TRUE/FALSE regardless of if you use the nohott option \*\(true is determined if you are

  within the front arc of the target you are **facing**\)\*

* Changed the method of standing up from _ExecuteCmd\(sit\_stand\)_ key to _EzCommand\("/stand"\)_ to play nice with

  MQ2Melee and not offer an opportunity for this plugin to force you to sit down under any circumstance

* Determined that _/circle_ and breakonsummon math \(uses breakonwarp math\) do not play nice together
  * This only affects _/circle_ so don't use breakonsummon with circle for the time being
  * _If you are good with math / angles / etc. \(I'm not\) and want to help out look at the notes in the To-Do post_
* Fixed loose stick/moveto fighting you for the heading still if using mpause/mousepause/breakonkb/breakonmouse
* Fixed mpause resuming the command if you pressed down two keys at the same time, such as move forward and right, but

  only let go of one of them

* Mousepause now breaks movement since you have to press+hold the right button before the left button to move unless

  you've got uber micro...

* In finding the fix for mpause key releases I came up with a solution for mpause leaving you moving fowards even if

  the key you pressed was _strafe\_left_ for example

  * It should now stop all movement and repress whatever key you pressed so that your movement was not interrupted

#### Beta - 8.1029 - new features / misc

* Fixed the crash bug related to v2008-10-26
* Removed redundant check. thanks goes to ascii and dkaa for help in indentifying it.
* Fixed another potential crash bug. thanks goes to ieatacid for help in identifying it.
* Another fix attempt at sit/stand bug
* Added an option for always loose stick now that it uses deadchicken's improved logic. You can turn this option on

  with _/stick toggle alwaysloose_ just as moveto's has been set with _/moveto toggle alwaysloose_ in a previous

  update

* Updated _/moveto toggle loose_ and _/stick toggle loose_ to toggle loose on and off, since supplying it in the

  command will always turn it on

  * These are independent, meaning if you use _/moveto_ it will not toggle stick's loose, and if you use _/stick_ it

    will not toggle moveto's loose

* Identified that on some newer computers \(it also might relate to duo/quad core cpu\) that stucklogic even at 0.1 can

  cause absurd behavior such as random camera angle jerks. deadchicken has some ideas on rewriting this whole process,

  but for the time being I discovered that if we allow the value to be set to smaller numbers it will improve. On one

  of my duo core boxes it was always having problems to the point I had to turn it off. I found with setting the value

  to 0.05 those problems went away and stucklogic worked better

  * It still has problems with the way the math works, it does not properly attempt to work its way around all

    angles to break from stuck

  * If it reaches exactly the halfway point \(facing the exact angle away from your target\) it will start turning

    back towards the target. This is most noticeable if you are stuck in a corner or doorway

  * To fix the duo-core/faster cpu issues, the value for stucklogic now may be set up to the hundreths
  * The minimum value you can now use in the ini is: 0.001

* Added a new \(long overdue\) parameter to stick: _/stick front_
  * If you lose aggro \(or use this command on a non-tank to help control push and the mob aggros someone in the

    rear\), you will be spinning endlessly trying to get to the front of the mob

  * By default, if you have access to Health of Target's Target and you are not the target, you will not try to spin

    with the mob to stay in its front arc

  * For those who do not want that, or for those characters you desire to be in the front arc that will not be the

    one's on HoTT, you can bypass this with the following toggle: _/stick toggle spinme_

  * You will then always stick to the front, no matter what, if using _/stick front_ parameter
* Made major improvements to the NoHoTT aggro detection
  * The way this works is if you are using any arc enforcement other than _/stick front_ \(meaning _pin_, _!front_,

    _behind_\), and you do not have access to Health of Target's Target data, this feature will detect if you are

    aggro by checking if the mob's heading is pointed towards you

  * If so, it will slide you slightly to the side, and stop for around 7 seconds, then attempt to continue sliding

    back into position. If the mob is still facing you, it will assume you are aggro, and repeat the process. If the

    mob is no longer turning with you, you will resume sticking to your prior arc choice
* Using _/makecamp off_ will now halt a makecamp return if its currently happening when you issue the off command
* Using _/makecamp return_ will no longer work if you do not currently have a camp or camp-player active
* Rewrote all WriteChat output to use a new custom function WriteLine, to support the following request
* By request, there is a new option added to verbosity, TotalSilence
  * This can be turned on using _/stick set totalsilence on_ \(or _/moveto_, _/circle_, and _/makecamp_\)
  * This can be turned off using _/stick set totalsilence off_ \(or _/moveto_, _/circle_, and _/makecamp_\)
  * This option will reduce the output to only major events such as the actual toggle itself \(totalsilence on,

    totalsilence off\), the help output only if you type '/command help', breakonsummon firing \(since it requires you

    to type '/command imsafe' in order to resume anything\), and a few other drastic errors

  * All other output will be suppressed
  * This option saves to the INI and is disabled by default
  * Turning verbosity or fullverbosity back on will disable totalsilence
* You are no longer allowed to stick to yourself with certain parameters. Sorry for this nerf
* You can now set your leash length to &gt;= camp radius in the ini, instead of &gt;= campradius + 10
* Generic code cleanup and bug fixes

#### Beta - 8.1026 - minor

* More changes to 'always' stick parameter. Really trying to clean it up a bit more.
* Fix for my creating a new sit/stand bug by fixing the old one \(\*setting standstate while dead = bugged until zone

  out\*\)

* Related to above, death should now break all commands except makecamp \(\*will resume if you get res, but will break

  if you exit zone\*\)

* _/stick_ with invalid parameters will no longer stick
* Fix for mpause/breakonkb with 'always'
* Added 'TotalSilence' option to ini that will not display any output except critical errors, breakonsummon

  notification \(_since it halts command usage entirely until you turn it off_\), and help output if you manually type

  _/stick help_

* Generic code cleanup and bug fixes

#### Beta - 8.1025 - bugfixes

* Attempted a fix to the long-standing SIT/STAND bug. Major thanks to frostx for supplying me with a ton of

  information on how to recreate it.

* Fixed a bug with distance to target not being reset after a stick command was used and ended. this had behavior of

  sometimes causing breakonwarp messages to fire if the target was outside of breakdist range when you issued a

  following command. This only applied to certain parameters \(_i.e. /stick \#, /stick behind/pin/!front_\), and not with

  anything that set the distance \(_/stick, /stick on_\). Major thanks to frostx for supplying me with a ton of

  information on how to recreate this so I could find the cause. That's twice!

* Fixed a crash bug with "id" if used with invalid id. \(_/moveto_ and _/stick_\)
* Added Dist and Loose values to _/moveto_ verbosity output
* Added more checks to prevent stick "No Target" error msg instead of halting command attempt if the command requires

  a target. You will still see the "You must specify..." message as normal, but this fix relates to the "You are now

  sticking to NO TARGET ERROR" message

* Fixed a bug with strafe being held down sometimes, keeping you sliding sideways when you should have stopped
* Fixed a bug with _/stick \[parameters\] always_ checking events for breakonsummon,

  mpause/mousepause/breakonkb/breakonmouse when you did not have a target. This will now only make those checks if you

  have a valid npc target and are currently sticking to it

#### Beta - 8.1024 TLO adds / settings rewrite

* Removed the following TLO members \(\*${Circle.Summoned}, ${Stick.Summoned}, ${MoveTo.Summoned}, ${Stick.Stuck},

  ${MakeCamp.InUseBy}\*\)

* Added a new TLO **${MoveUtils}** with the following members:
  * **${MoveUtils.Stuck}** - _TRUE / FALSE - \(former stick.stuck\)_
  * **${MoveUtils.Summoned}** - _TRUE / FALSE \(former everything.summoned\)_
  * **${MoveUtils.Command}** - _NONE / STICK / CIRCLE / MOVETO / MAKECAMP_
    * this is the replacement for makecamp.inuseby
    * _MAKECAMP_ will only show up if nothing else active
    * if you have makecamp on and stick active, _STICK_ will be the result
    * **${MoveUtils}** returns this same information
  * **${MoveUtils.StuckLogic}** - _TRUE / FALSE \(if you have stuck logic on or not\)_
  * **${MoveUtils.Verbosity}** - _TRUE / FALSE \(if you have verbosity on or not\)_
  * **${MoveUtils.FullVerbosity}** - _TRUE / FALSE \(if you have fullverbosity on or not\)_
* Added new members to **${Circle}** TLO for those of you who prefer true / false:
  * **${Circle.Clockwise}** - _TRUE / FALSE \(circle.rotation still shows CW/CCW\)_
  * **${Circle.Backwards}** - _TRUE / FALSE \(circle.direction still shows FORWARDS/BACKWARDS\)_
* BreakOnSummon no longer fires if only makecamp is on. it will fire if makecamp is attempting to return to camp

  though since that turns moveto on, which is checked

* Added the same fix from the previous posts for turn-walk-off adjustment to mouse pause as well. breakonmouse did not

  have this problem, only pause

* In the process of changing the syntax of anything that toggles to be able to be toggled as well as set via on / off.

  I'll also be adding the ability to set just about anything that should be modifiable using this same foundation.

  This already is a major change to the syntax of most every toggle I've added so please take note:

  * The help output doesnt reflect any of this yet.
  * Where /command can be \(/stick, /moveto, /circle, /makecamp\)

```text
//The same as before

/command help
/command debug
/command pause
/command unpause
/command save
/command load
/command imsafe

//Different: "set" - this is just a basic foundation

/command set verbosity on|off
/command set fullverbosity on|off
/command set stucklogic on|off

//Different: "toggle" - this is used to toggle values

/command toggle mpause
/command toggle mousepause
/command toggle breakonkb
/command toggle breakonmouse
/command toggle autosave
/command toggle feign
/command toggle autopause
/command toggle advancedautopause <---still doesnt work any better dont bother using really
/command toggle stucklogic
/command toggle verbosity
/command toggle fullverbosity
/command toggle nohott
/command toggle hidehelp
/command toggle breakongate
/command toggle breakonwarp
/command toggle alwaysdrunk
/command toggle alwaysbackwards
/command toggle alwaysccw
/command toggle alwaysloose  <---this only applies to moveto atm
/command toggle breakonsummon
```

* _/command checkifstuck_ is forever removed. use _toggle stucklogic_ or _set stucklogic \[on\|off\]_
* Preserved the values for 'ArrivalDist' and 'MoveToMod' in the ini since they were defaulting back to plugin-default

  values instead of your own custom settings. Will apply this to most everything else in the near future.

* Fixed mpause resuming no command if makecamp was active by itself. it should still resume an interrupted return to

  camp.

#### Beta - 8.1023 - minor

* Added "Stuck" TLO
  * **${Stick.Stuck}** - _FALSE / TRUE - \(true if stucklogic detects you are stuck_
* Added a turn off walking adjustment to BreakOnKB to fix a bug with walk being left on

#### Beta - 8.1019 - cleanup

* StuckLogic fixed. I loaded a session running old source and one running beta source side by side on 2 screens and it

  behaves the same way on both. Its sloppy and could use work but it was not functioning at all before so now it

  functions like its used to. I used the preferred settings posted earlier in the thread so please report any

  differences on other settings. The TurnIncrement of 10 seems to take forever to unstick in tight areas \(hallways,

  small indoor rooms\), so I upped it for myself to much better results around 35.0, you may want to try a higher value

  here if you use this indoors. outdoors might only need small increments

* StuckLogic now turns on walk when its stuck also, to help reduce getting unstuck only to get restuck because of a

  burst of speed in hallways and tight corners

* _/stick loose_ - now uses deadchicken's _/moveto loose_ improvements
  * this will now spin before moving if the heading to the target is greater than 1/4 a turn
  * this should be much more functional and cut down quite a large amount of the orbiting and getting stuck due to

    loose sticking

  * after playing with it for a good hour in multiple situations, I can say it looks much more natural than before

    and could be used viably in situations where the fast facing would not be acceptable. test it out by adding

    'loose' anywhere in your normal command line for _/stick_

  * \*Drunken circle still needs to be looked at because circle and stucklogic are having issues when you turn on

    circle next to a wall, which I don't know why you'd ever do that, but the circle gets stuck running forward

    indefinately \(in both versions of the source it looks like\) so I need to track that down before bringing circle

    over to the new loose logic\*
* Added _/moveto toggle loose_ - to turn off loose without moving, since /moveto loose always forces it on

#### Beta - 8.1018 - cleanup

* Fixed a bug with _/stick uw \| underwater_ not working
* BreakOnSummon now applies to all commands, not just _/stick_
* Updated BreakOnSummon to be more assertive. If BreakOnSummon fires, it will prevent any future command usage in case

  your macro continually reissues a /stick, /circle or /moveto command

  * When this fires this will display a warning message and notify you
  * There is now a new parameter to reset this, _/stick imsafe_, which will allow command usage once again
  * For macros that may continually trigger BreakOnSummon, but you still want to use it, there are new TLOs:
    * ${Stick.Summoned} ${Circle.Summoned} ${MoveTo.Summoned} - _TRUE / FALSE_
    * These apply across the board, meaning they all will be true or they all will be false, so use whichever you

      like. So in theory if you know something is going to fire breakonsummoned but you still want to use it for

      other cases, you could issue the command, check the state of the TLO and then have your macro issue a

      _/stick imsafe_ to undo the command halting

* BreakOnSummon defaults to false now instead of true since its more assertive
* Fixed a bug with BreakOnWarp where if you have a camp setup and you issued a _/stick_ or _/moveto_ it would report

  that mob had warped out of range when the mob never really moved to begin with. If you are leashed you should still

  not be able to go to the mob, just for different reasons

* Renamed TurnDirection \(ini setting\) to TurnIncrement to be more appropriate for what it actually does.
* Thanks to deadchicken, _/moveto loose_ is improved. There is now an additional check comparing your current heading

  to the heading you want to go to, and if its larger than a 1/4 turn, you will spin before you begin moving instead

  of trying to spin while moving. This prevents the endless "orbiting" in circles without ever being able to reach

  your destination

* LooseMoveTo in the ini \(always use loose when using _/moveto_\) now defaults to true because this is really superior

  now, and you should use this to prevent the fast facing that goes on if its false. It is very noticeable and

  detectable. Should you still want the fast facing, then you can either set LooseMoveTo to 'off' in the ini, or type

  _/moveto toggle alwaysloose_ to toggle it off, then issue a _/moveto save_ to save it to your ini as well

* _/moveto toggle alwaysloose_ is restricted to the _/moveto_ command, and doesnt work if you use _/stick_ or

  _/circle_. I plan to keep them command-based in the future as well

* Starting to add more comments to the source for those of you trying to learn how it works

#### Beta - 8.1015a - breakonsummon

* Added a new feature, BreakOnSummon
  * This command works like BreakOnWarp except it checks the distance change of your own x / y locations from pulse

    to pulse, not related to the mob

  * If your own x / y changes too drastically, with this enabled it will halt all commands.
  * This is useful for COH, or mob summon \(though I guess not if to the mob you are sticking\), but more important if

    you are summoned by those invisible people in short distances where breakonwarp normally wouldn't fire due to

    what they do, small repeated summons, doesnt matter with the large distance check you want to use for mob-warp

    checking. this one you can safely set to a small amount and not worry about your stick breaking from mobs

    warping small distances

  * the default is set to 20 soas not to interfere with summon from mob you are stuck to, but it may need to be set

    smaller to be effective, or larger if the mobs you fight you get summoned more than 20 range. it seems the max

    you move onpulse is around 2.0 with runspeed5, but bard or mount may be higher than that

  * Added new INI settings for this
    * **\[Stick\] 'BreakOnSummon'** - _on / off_
    * **\[Stick\] 'BreakSummonDist'** - _distance to consider summoned \(default 20.0\)_
  * Added toggle: _/stick toggle breakonsummon_
* Related to this, I fixed a since-inception bug with breakonwarp that only worked on half of the angles from your

  mob. the math \(if sqrt\(yourdist\) - sqrt\(mob dist\) &gt; breakdist\) never worked when the differences were negative. now

  they do.

#### Beta - 8.1015 - pause logic

* mpause, if set to ON, will now apply to mouselook as well.
  * you can mouselook or mouselook+left click to move around and it will return based on min/max delay
  * if mpause is set OFF, unlike pressing a key, mouselook will not break your command
  * it will no longer fight with you for the heading. it will allow you to move with the mouse but once you let go

    of mouselook it will resume the previous command immediately.

  * _/stick toggle mousepause_
    * this works independently of mpause now. its optional and works identically to mpause for keyboard movement.
    * it saves to the ini as MousePause as well. if turned on, any movement of the mouse while mouselook \(turn

      head with right-click-hold only, or move by right-click-hold plus left-click\) will pause the command and

      return after the min/max delays. if its turned off it will behave like it always did and fight with you for

      the heading if you try to do anything. to overcome that there is now another option
  * _/stick toggle breakonmouse_
    * this works like mpause=off used to work for keyboard movement
    * if you move the mouse while a command is active, it will break from the command altogether
    * you can set this under \[Defaults\] 'BreakOnMouse' in the ini
  * _/stick toggle breakonkb_
    * this works like mpause=off used to
    * mpause=off will not break from your current commands any longer, it will resume immediately as opposed to

      with a delay, and fight you for the keyboard.

    * you need to set breakonkb or \(BreakOnKB in the ini\) the way you like it
    * breakonkb will default to true since this was the old default behavior
  * Pause and break turn each other off, but do not turn the others on.
  * You can have mpause and breakonkb both off, but breakonkb on = mpause off and mpause on = breakonkb off.
  * If you like and use mpause, but decided to try breakonkb, then turned breakonkb off, mpause needs to be turned

    back on

  * trying to turn both true in the ini will result in breaks being off and pauses being on.
* ManualPause changed to KeyboardPause in the ini. command still is mpause though.
* Fixed a bug with _/makecamp on \[\#\]_
* _/makecamp radius_ and _/makecamp on \[\#\]_ and _/makecamp player_ and _/makecamp \[y\] \[x\]_ commands now also

  enforce leash size update if leash is smaller than camp radius \(before only /makecamp with no params did this\)

* Put the stick dir\(normal\) dist\(\#\) mod\(\#\) hold\(no\) loose\(no\) msg on verbosity instead of fullverbosity
* Failing to input a command-specific parameter correctly will no longer issue help for the entire plugin, only the

  command it relates to.

* Typing '/command help' if HideHelp option is on now assumes you wanted the display and will output the help one time

  instead of blocking it in this case.

#### Beta - 8.1014 - TLO adds

* Added New TLOs:
  * **${Stick.DistMod}** - _value set with /stick mod \# or /stick -\#_
  * **${Stick.DistModPercent}** - _value set with /stick \#%_
  * **${Stick.Always}** - _PAUSED / TRUE / FALSE - \(true if '/stick \[parameters\] always' was activated\)_
  * **${Stick.Aggro}** - _PAUSED / TRUE / FALSE - \(true if NoHoTT detects aggro\)_
* Help output completed, hence the new hidehelp option since it is spamcity
* _INI Revamp_ - ini file now breaks down into logical sections
  * \[Defaults\] \[Stick\] \[Circle\] \[MoveTo\] \[MakeCamp\] \[StuckLogic\] \[your-char-name\]
* INI file supports many more features. I suggest you backup your current one and delete it, then log in game and

  /stick save to output a new one.

  Then edit in your old values from backup and save the file and then /stick load.

  That way you can see all the new features organized correctly.

  Loading all values from \[Defaults\] will no longer work in this version, but some still remain there.

* _New INI Options_
  * **\[Defaults\] 'HideHelp'** - _never display spam-filled help syntax_
  * **\[Stick\] 'AwareAggro'** - _NoHoTT checking on/off_
  * **\[Stick\] 'StickDistMod'** - _always use specific dist mod_
  * **\[Stick\] 'StickDistModPercent'** - _always use specific dist mod percent_
  * **\[MoveTo\] 'ArrivalDist'** - _max dist from moveto loc that is acceptable_
  * **\[MoveTo\] 'LooseMoveTo'** - _always use loose heading_
  * **\[MoveTo\] 'MoveToMod'** - _always use specific moveto dist mod_
  * **\[Circle\] 'AlwaysBackwards'** - _always run backwards_
  * **\[Circle\] 'AlwaysCounterClockwise'** - _always run in a counter-clockwise circle_
  * **\[Circle\] 'AlwaysDrunken'** - _always use drunken movement_
  * **\[Circle\] 'RadiusSize'** - _always use specific radius size_
* New primary command parameters \(_usable with /stick, /moveto, /makecamp, or /circle_\):
  * _/stick toggle hidehelp_ - toggle hidehelp on/off
  * _/stick toggle breakongate_ - toggle on/off
  * _/stick toggle breakonwarp_ - toggle on/off
  * _/circle toggle alwaysdrunk_ - toggle default to drunken
  * _/circle toggle alwaysbackwards_ - toggle default to backwards
  * _/circle toggle alwaysccw_ - toggle default to counterclockwise
  * **issue a '/stick save' afterwards to write these changes to ini if desired**
* **Experimental new command**: '/stick advancedautopause'
  * this will attempt to turn on walk, stop moving, turn to the right to force a position update to prevent casting

    while moving from getting interrupted. i dont know how well it will work or not, since the current

    implementation only is good for stopping you from moving if already stationary then casting.

```text
*this doesnt work, need a better way to check if casting before the bar pops up*
```

#### Beta - 8.1013 - minor

* My attempt to fix the negative stick/movedist halting movement broke the mod applied and forced a very close stick

  value. Fixed this.

* You can now set the modifier independently. This will not turn stick on or modify current stick, just change the

  base value.

  * Before you had to set the mod with: _/stick -5_

```text
This would subtract 5 from whatever value you used (or mob melee range, which i believe is the intention of this
whole thing) every time.

It defaulted to 0, but once you set it, you were stuck with negative forever.

-   Now using */stick mod \[#\]*, you can:
    -   reset it to zero (*/stick mod 0*)
    -   or use a positive number (*/stick mod 5* would make */stick 10* function as */stick 15*.


This will defeat the purpose of melee range checking but would be good for increasing the number for macros that use
too small of number or something along those lines. It is there if you can find a use for it.
```

* Added output for modchanges without any verbosity check \(will move it to Verbosity once its all correct\) so you can

  see these actions taking place. FullVerbosity also displays the mod on every use of /stick.

* Added toggle for Verbosity option
* Added toggle for FullVerbosity option

#### Beta - 8.1012a - minor

* Added Circle TLOs
  * \([string]()\) - **${Circle}** - _ON / OFF / PAUSED_
  * \([string]()\) - **${Circle.Status}** - _ON / OFF/ PAUSED_
  * \([float](../../../reference/data-types/datatype-float.md)\) - **${Circle.CircleX}** - _location of the center X_
  * \([float](../../../reference/data-types/datatype-float.md)\) - **${Circle.CircleY}** - _location of the center Y_
  * \([bool](../../../reference/data-types/datatype-bool.md)\) - **${Circle.Drunken}** - _TRUE / FALSE_
  * \([string]()\) - **${Circle.Rotation}** - _CW / CCW_
  * \([string]()\) - **${Circle.Direction}** - _FORWARDS / BACKWARDS_
* Added the ability to change circle radius
  * Before you had to re-issue /circle on \[\#\] to change the radius\(size\) of the circle.
  * This would plant the anchor where you were at, forcing you to reset any custom anchor or options.
  * Now you can do this:
    * _/circle radius \[\#\]_ - will keep circling but increase the radius on the fly
* Removed the ability to do /moveto \[dist/-dist\] because it was having conflicts. To set the moveto distance now you

  need to use:

  * _/moveto dist \[\#\]_ - to set distance
  * _/moveto dist \[-dist\]_ - to subtract from currently set distance
  * You can no longer set stick or moveto distance to a value below 0.

    Negative numbers halted all movement so any attempt to do so will force the distance value to 1.

#### Beta - 8.1012 - makecamp player

* Fixed two more crash bugs \(thanks ieatacid\)
* Added /makecamp player \[name\]
  * Makecamp player works if you supply a valid name of a PC in the zone
  * uses your current target \(fails if target is not SPAWN\_PLAYER\) if you do not supply the name.

    This will create a dynamic camp based on the location of this player as they move, using the current 'radius'

    and 'leash' values that you are used to.

  * This works like a ghetto autofollow and actually appears somewhat natural because it uses moveto logic instead

    of stick logic.

  * This means no fast/loose facing the person, just moving to their general area \(which is cool\).
  * If the camp is based around your puller, that is a bad idea, don't do it.
  * If the person you supply is really far away when you issue the command, it may have trouble getting to them.
  * If the person magically warps/gets summoned way far away, it will likely have problems.
  * Also note this still uses the mindelay and maxdelay values for deciding when to move, so it will look like you

    are really two/three/four/etc-boxing and moving them if you set the values correctly.

  * The downside to this is that if the character is on the very edge of the leash length and you are taking small

    steps forward it will take its own small steps forward as well, based on the min/max delays, so that can look

    weird

#### Beta - 8.1011 - minor

* attempt a fix at a crash bug related to verbosity output. Went through the whole source and that was the only time

  the writechat was used incorrectly in that way

* Please report any occurrences of new "NULL POINTER ERROR" message or new "NO TARGET" error message \(both relate to

  only the verbose output for /stick\) and how to reproduce it

* The old NULL POINTER message still exists as it always did in original moveutils

#### Beta - 8.1002 - _complete rewrite_ \(first beta\)

* _Command Syntax_ - Many base commands all can be used from every command

  i.e. /circle load, /stick load, /makecamp load, /moveto load - all will do the same thing

\*_INI File_ - many more settings supported

* _INI File Verbosity_ - Changed from 1/0 to on/off. It will auto-correct old files, so you dont need to mess with it.

  Just a FYI.

* _Output_ - drastically changed, may break macro events \(tried to keep the most common ones the same\)
* _Issuing one command completely ends the other_ - This does not apply to /makecamp, only /circle, /moveto, and

  /stick

* _Feign Support_ - added feign parameter or \[FeignSupport\] in the INI.

  When enabled this will not begin your command if you are FD until you manually stand up

\*_AutoSave_ - automatically save ini like old save cmd \(/stick save\) every time you change a setting

* _New TLOs_
  * \([string]()\) - **${MakeCamp.InUseBy}** - which command is active
  * \([string]()\) - **${Stick.StickTargetName}** - name of stick target if using /stick id,

    or /stick hold, otherwise will be target name/NONE

\*_Additional Verbosity_ - fullverbosity option \(ini file\) to output more detailed information.  
original verbosity still exists and fullverbosity does NOT turn on original stick verbosity messages. you have to set each independently  
\*_StuckLogic Toggle_ - added a toggle for stucklogic, no longer need to reload ini file  
\*_AutoPause Toggle_ - added a toggle for autopause, no longer need to reload ini file  
\*_New Stick Parameter 'always'_ - Usage:

```text
/stick [other parameters] always
```

* * Putting 'always' at the end will not require another /stick after you lose your target \(i.e. mob dies\).
  * This behaves the same way as if you /stick something, then change the target before it dies which uses the same

    settings as the last time you typed the command.

  * This does not work with stick hold or stick id.
  * This only works with NPC targets \(not their pets\), so changing to other target types like PC, chest, corpse,

    etc. will not make you run around constantly.

  * This works great if you pass targets with EQBC for example.
  * Using this on your puller or when cross-zone targeting will probably cause you problems.
  * This setting cannot be saved and will reset upon any new command typed by design because of its potential

    misuse. Don't ask for huge features on this. I can see it being used carelessly so be careful.

\*_Check for aggro if you dont have HoTT_ - this is experimental and still needs improvement

#### Original - 8.0913 - first moveutils change

* every 'break' function that used this method to stop moving seems to be failing:

```text
MQ2Globals::ExecuteCmd(FindMappableCommand("forward"),0,0);
```

* Changed the ExecuteCmds to supply a down then up to stop the issue:

```text
MQ2Globals::ExecuteCmd(FindMappableCommand("forward"),1,0);
MQ2Globals::ExecuteCmd(FindMappableCommand("forward"),0,0);
```
