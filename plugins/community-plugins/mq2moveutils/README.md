# MQ2MoveUtils

## General Details

Version 9 of MQ2MoveUtils was a rewrite from the ground up by pms. The original goal behind this rewrite was to cleanup numerous logical errors and reduce the amount of code duplication that existed in previous releases. Once this rewrite was complete and functional, version 9 expanded including more enhancements and more extensive configuration. Numbered by release date, the current of this plugin is 16.0717.

This plugin is no longer under active development and no new contributions have been made since 2011 by pms, with only one follow-up contribution in 2014 by Cr4zyb4rd. Others have continued to keep the offsets updated in the discussion thread linked below.

### Links

* Link to the latest stable source: \[16-Nov-2016th patch fix by

  trevyn\]\([https://macroquest2.com/phpBB3/download/file.php?id=988](https://macroquest2.com/phpBB3/download/file.php?id=988)\)

* Link to older sources: [MQ2MoveUtils v11.x Source](http://mq2.whyarewehappening.com/MQ2MoveUtils/)
* Link to emulator version of the source that works with the December 19, 2008 client: \[MoveUtils v11 for EMU by

  pms\]\([https://macroquest2.com/phpBB3/viewtopic.php?p=155710\#p155710](https://macroquest2.com/phpBB3/viewtopic.php?p=155710#p155710)\)

* Link to current discussion thread: \[MQ2MoveUtils v16.x

  Thread\]\([https://macroquest2.com/phpBB3/viewtopic.php?t=15909](https://macroquest2.com/phpBB3/viewtopic.php?t=15909)\)

### Development Notes

For the development history of this plugin, see the article MQ2MoveUtils 16.x Revision History

For the chronicle of the entire MoveUtils plugin including the original development history, see the article [MQ2MoveUtils:History](mq2moveutils-history.md)

### Help

* [Frequently Asked Questions](mq2moveutils-v11-faq.md)
* Configuration Examples

## Command Information

### Main Plugin Commands

_These parameters can be used from any of the four main plugin commands \('/stick', '/moveto', '/circle', and '/makecamp'\). For example purposes the most popular '/stick' command will be used._

\* **/stick help** **\[settings\]**

* * Displays generic help information, and help for the command used
  * The _settings_ optional parameter displays help information for all plugin 'set' and 'toggle' commands

\* **/stick debug**

* * Dumps the current values of all plugin variables to a debug INI file

\* **/stick status** **\[all\]**

* * ChatWnd output for the status of the issuing command \(stick in this example\)
  * The _all_ optional parameter displays status output for all aspects of the plugin

\* **/stick pause** **\[lock\]**

* * Pauses all aspects of the plugin
  * The _lock_ optional parameter prevents plugin from automatically unpausing under any circumstance other than

    user issuing _unpause_

  * **Note: This does not toggle**

\* **/stick unpause**

* * Resumes all aspects of the plugin
  * **Note: This does not toggle**

\* **/stick save \| load**

* * Saves or load your current configuration settings using MQ2MoveUtils.ini

\* **/stick imsafe**

* * BreakOnSummon and BreakOnGM have built-in protection disabling the ability to re-issue commands when triggered.

    This prevents macros from continuing to issue commands in a possibly unsafe situation

  * The _imsafe_ parameter allows command usage to resume

\* **/stick min**

* * Minimizes custom user window similar to [/mqmin](../../../commands/slash-commands/mqmin.md)

\* **/stick clear**

* * Clears custom user window buffer similar to [/mqclear](../../../commands/slash-commands/mqclear.md)

\* **/stick verbflags**

* * Outputs current verbosity flags setting \(this one displays even if totalsilence is enabled. too bad.\)

=== Main Plugin Settings === _These setting parameters can be used from any of the four main plugin commands._  
_The following can be used with_ **toggle** _or_ **set** _**name**_ **on \| off.**

\* **/stick toggle** _**name**_

* _\*/stick set_ name\* on&lt;/span&gt; \|

  off\*\*

_**name**_ **can be one of the following:**  
\* **mpause \| mousepause**

* * Pause current command if \[ keyboard \| mouse \] movement
  * Resumes after a random amount of delay set with _pausemindelay_ and _pausemaxdelay_ below
  * _\*Note: You_ may not\* have a pause and corresponding break on at the same time \(e.g. no mpause and breakonkb at

    the same time\)\*\*

  * **You** _**may**_ **have opposing options different though \(e.g. mousepause on and breakonkb on\)**

\* **breakonkb \| breakonmouse**

* * Break current command if \[ keyboard \| mouse \] movement
  * _\*Note: You_ may not\* have a pause and corresponding break on at the same time \(e.g. no mpause and breakonkb at

    the same time\)\*\*

  * **You** _**may**_ **have opposing options different though \(e.g. mousepause on and breakonkb on\)**

\* **autosave**

* * Automatically save settings to INI file when a _toggle_ or _set_ command is issued

\* **savebychar**

* * Save \[server._Yourcharacter_\] section of INI file for individual character settings

\* **feign**

* * Enable Feign Death support, which waits for you to stand up manually before moving

\* **lockpause**

* * Plugin will never automatically resume from _pause_ until user issues an _unpause_

\* **autopause**

* * Pause movement if casting spells \(non-bard\), stunned, rooted, sitting, FD, or self targeted \(non-hold\)

\* **autopauseoutput**

* * If enabled, will display ChatWnd output when autopause is halting movement
  * **Note: This bypasses** _**totalsilence**_ **and must be configured individually**

\* **stucklogic**

* * If enabled, stucklogic automatically attempts to get unstuck if running into walls and large objects

\* **trytojump**

* * If enabled, stucklogic also tries to jump to help get unstuck

\* **turnhalf**

* * If enabled, stucklogic will reset heading and turn the other direction if it has rotated halfway without success

\* **verbosity**

* * ChatWnd output for basic command information messages

\* **fullverbosity**

* * ChatWnd output for more detailed information messages and output for more actions

\* **totalsilence**

* * Silences most ChatWnd output except for critical information or user-requested messages

\* **totalverbosity**

* * Enable display of every ChatWnd message in the plugin

\* **hidehelp**

* * If enabled, the help output will not be displayed upon command failure \(e.g. invalid parameters\)

\* **window**

* * If enabled, MoveUtils will output any messages to a user-placed custom UI window dedicated to the plugin

\* **wineq**

* * By default, MoveUtils uses actual keypresses to control movement \(regardless of heading settings\)
  * WinEQ2 has a bug where background sessions can have their alt keys and certain mouse buttons held down, causing

    movement to run in weird directions

  * For Lavishsoft users who have not switched over to Innerspace, enabling _wineq_ setting will use old-style

    emulated movement via ExecuteCmd\(\)

\* **breakontarget**

* * Break from stick if target changes \(default behavior is switch over to sticking to new target\)

\* **breakonsummon**

* * Halts current command and disables ability to use any commands if summoned beyond _summondist_
  * **Note: Once this fires, you must use the** _**imsafe**_ **parameter to unlock the plugin**

\* **breakongm**

* * Halts current command and disables ability to use any commands if **visible** GM enters the zone
  * **Note: Once this fires, you must use the** _**imsafe**_ **parameter to unlock the plugin**

\* **breakonwarp**

* * Breaks from stick if target warps out of _breakdist_ range \(user set, see below\)
  * **Note: This does not limit your initial stick range. You may /stick from across the zone**

\* **pauseonwarp**

* * Pauses stick if target warps out of _breakdist_ range until they are back in range \(user set, see below\)
  * **Note: This does not limit your initial stick range. You may /stick from across the zone**

\* **breakongate**

* * Breaks from stick if _**target**_ **Gates.** message occurs
  * **Note: if using stick id or stick hold, it will break based on the held target name**

\* **breakonaggro**

* * Breaks from moveto command if you are aggro to an NPC
  * **Note: This checks the player window for the crossed swords indicator**

\* **alwaysdrunk**

* * Use _drunken_ by default when circling

\* **alwaysbackwards**

* * Run backwards by default when circling

\* **alwaysccw**

* * Circle in a counter-clockwise direction by default

\* **nohottfront**

* * Allow for _stick front_ to spin to front of the mob without Health of Target's Target Leader AA
  * **Note: By default stick front will not stay stuck to the front unless you are on the HoTT window**

\* **returnnoaggro**

* * Makecamp will auto-return to camp only if not aggro \(checks crossed swords indicator\)

\* **returnnotlooting**

* * Makecamp will not auto-return to camp if character has an open loot corpse window

\* **returnhavetarget**

* * Makecamp will auto-return to camp even if you have a target
  * **Note: By default, makecamp does not auto-return if you have any target**

\* **realtimeplayer**

* * Makecamp player will get realtime updates on player location, allowing for dynamic returns to players
  * By default, makecamp player will return to a players last location when return begins and not get a new update

    until the return is complete

  * The default behavior is a sort of ghetto MQ2AdvPath whereas enabling realtimeplayer will work more like an

    autofollow

\* **leash**

* * If enabled, leash prevents moving beyond leashlength \(user set value\)

\* **usewalk**

* * If enabled, plugin will switch to walking when closing in on moveto destination or camp return

\* **strafewalk**

* * If enabled, plugin will switch to walking when within strafe range for all stick commands

\* **randomize**

* * If enabled, stick behind and !front will use random arc values to position

\* **delaystrafe**

* * If enabled, strafe-based movement \(stick front, !front, behind, pin\) will use a delay before moving
  * \*\*Note: This helps prevent endless circling when aggro is gained, or spinning when mobs quick-turn to cast

    spells\*\*

  * \*\*Circling is one of the biggest signs that a player is using MoveUtils so it is recommended you ALWAYS leave

    this enabled\*\*

\* **autoUW**

* * If enabled, stick and moveto will use the _uw_ parameter whenever underwater \(look up and down at target\)

\* **usefleeing**

* * If enabled, stick front will not attempt to position in the front of a target that is fleeing

\* **usescatter**

* * If enabled, camp returns will use scattered return locations instead of default behavior
  * **Note: Default behavior attempts to get back within camp radius**

_The following option is unique_

* **/stick set heading** _**true**_ _**\|**_ _**loose**_ _**\|**_ _**fast**_
  * Changes plugin heading adjustments to use the specified type
  * true: actual keypressing -- **does not work with wineq=on**
  * loose: simulated incremental turning -- fast: instantly set heading

_The following 'set' commands require a numeric value, and can be used from any of the four main plugin commands. \(stick used for example purposes only\)_  
\* **/stick set pulsecheck \#**

* * Number of pulses used to calculate average movement distance in stucklogic
  * Valid: 1 or higher

\* **/stick set pulseunstuck \#**

* * Number of pulses successfully moved forward before considered unstuck
  * Valid: 1 or higher

\* **/stick set diststuck \#.\#\#**

* * Minimum distance needed to move or else considered stuck \(compares against pulse average\)
  * Valid: 0.01 or higher

\* **/stick set campmindelay \#**

* * Minimum delay before auto-returning to camp \(in ms\)
  * Valid: 125 or higher

\* **/stick set campmaxdelay \#**

* * Maximum delay before auto-returning to camp \(in ms\)
  * Valid: 125 more than campmindelay

\* **/stick set pausemindelay \#**

* * Minimum delay before resuming from mpause/mousepause \(in ms\)
  * Valid: 125 or higher

\* **/stick set pausemaxdelay \#**

* * Maximum delay before resuming from mpause/mousepause \(in ms\)
  * Valid: 125 more than pausemindelay

\* **/stick set strafemindelay \#**

* * Minimum delay before stick will strafe to move when delaystrafe is enabled \(in ms\)
  * Valid: 125 or higher
  * **note: higher values are better. default of 1500 \(1.5s\) is recommended**

\* **/stick set strafemaxdelay \#**

* * Maximum delay before stick will strafe to move when delaystrafe is enabled \(in ms\)
  * Valid: 125 higher than strafemindelay
  * **note: higher values are better. default of 3000 \(3s\) is recommended**

\* **/stick set ydist \#.\#\#**

* * Acceptable distance to have "arrived" for precisey moveto
  * Valid: 1.0 or higher

\* **/stick set xdist \#.\#\#**

* * Acceptable distance to have "arrived" for precisex moveto
  * Valid: 1.0 or higher

\* **/stick set snapdist \#.\#\#**

* * Default distance to run past target before turning to snaproll
  * Valid: 1.0 or higher

\* **/stick set summondist \#.\#\#**

* * Distance character must be summoned in a single pulse for BreakOnSummon to fire
  * Valid: 2.0 or higher

\* **/stick set turnrate \#.\#**

* * Rate at which loose heading turns
  * Valid: 1.0 to 100.0

\* **/stick set !frontarc \#.\#**

* * Angular distance arc for stick !front
  * Valid: 1.1 to 260.0

\* **/stick set behindarc \#.\#**

* * Angular distance arc for stick behind
  * Valid: 1.1 to 260.0

\* **/stick set breakdist \#.\#\#**

* * Distance to check for breakonwarp
  * Valid: 1.0 or higher

\* **/stick set campradius \#.\#\#**

* * Default camp radius and radius for active camp
  * Valid: 5.0 or higher

\* **/stick set circleradius \#.\#\#**

* * Default circle radius
  * Valid: 5.0 or higher

\* **/stick set leashlength \#.\#**

* * Default leash length and length for active leash
  * Valid: greater or equal to camp radius

\* **/stick set bearing \#.\#**

* * Bearing \(direction from center\) used for scatter camp
  * Valid: any

\* **/stick set scatsize \#.\#\#**

* * Radius size for scattering
  * Valid: 1.0 or higher

\* **/stick set scatdist \#.\#\#**

* * Distance from center of camp to scatter at
  * Valid: 1.0 or higher

\* **/stick set allowmove \#.\#\#**

* * Loose or True heading allow forward movement when reach this angular distance
  * This is "anti-orbit" code to stop circling near close-range destinations
  * Valid: 10.1 or higher

\* **/stick set font \#**

* * Custom user window font size
  * Valid: 1 to 10

\* **/stick set verbflags \#**

* * Current plugin verbosity flags
  * Valid: see verbosity section near bottom of this wiki entry

_The following settings are command-specific, use the command in the example only_  
\* **/stick set backupdist \#.\#\#**

* * Range that stick will walk backwards instead of turning to face target, if useback enabled
  * Valid: 1.0 or higher

\* **/moveto set backupdist \#.\#\#**

* * Range that moveto will walk backwards instead of turning to face destination, if useback enabled
  * Valid: 1.0 or higher

\* **/moveto set dist \#.\#\#**

* * Acceptable distance to have "arrived" for standard moveto and camp returns
  * Valid: 1.0 or higher

\* **/stick** **\[** **toggle** **\|** **set** **\] alwaysUW \[** **on** **\|** **off** **\]**

* * If enabled, stick will always adjust looking angle as if _uw_ parameter was typed inline
  * **Note: this is not the same as** _**autoUW**_**, which only enables** _**uw**_ **when actually underwater**

\* **/moveto** **\[** **toggle** **\|** **set** **\] alwaysUW \[** **on** **\|** **off** **\]**

* * If enabled, moveto will always adjust looking angle as if _uw_ parameter was typed inline
  * **Note: this is not the same as** _**autoUW**_**, which only enables** _**uw**_ **when actually underwater**

\* **/stick** **\[** **toggle** **\|** **set** **\] breakonhit \[** **on** **\|** **off** **\]**

* * Breaks from stick command if you are attacked by an NPC
  * \*\*Note: This parses chat for hits and misses. If you use the number only hitsmode then it will only parse for

    misses\*\*

\* **/moveto** **\[** **toggle** **\|** **set** **\] breakonhit \[** **on** **\|** **off** **\]**

* * Breaks from moveto command if you are attacked by an NPC
  * \*\*Note: This parses chat for hits and misses. If you use the number only hitsmode then it will only parse for

    misses\*\*

\* **/stick** **\[** **toggle** **\|** **set** **\] useback \[** **on** **\|** **off** **\]**

* * If enabled, stick will walk backwards to position itself when close to a target instead of turning to face it
  * **Note: This requires** _**loose**_ **or** _**truehead**_ **style heading adjustments, and does not work with fast heading**

\* **/moveto** **\[** **toggle** **\|** **set** **\] useback \[** **on** **\|** **off** **\]**

* * If enabled, moveto will walk backwards to position itself when close to a destination instead of turning to face

    it

  * **Note: This requires** _**loose**_ **or** _**truehead**_ **style heading adjustments, and does not work with fast heading**
  * This **includes** automatic and user-forced camp returns

\* **/stick** **\[** **toggle** **\|** **set** **\] loose** **\|** **truehead \[** **on** **\|** **off** **\]**

* \*\*/moveto \[ toggle \| set \] loose \| truehead

  \[ on \| off \]\*\*

* \*\*/circle \[ toggle \| set \] loose \| truehead

  \[ on \| off \]\*\*

  * Change the heading type for currently active \(stick \| moveto \| circle\) to this type of heading. If _WinEQ_ is

    enabled, truehead will fail to switch.

  * Once current command ends, heading type will return to previous.

### /stick

_The stick command sticks you to your target, so that if your target moves you will move along with it. There are many different parameters that cause this command to behave in different ways. You can combine any number of these parameters together inline to enable multiple options for the stick._

\* '''/stick

* * stick with no parameters will stick you to your current target, using max melee range

\* **/stick on** **\|** **off**

* * turns stick on and off with default values
  * on is a nearly-useless parameter and only included to support older macros or stickcmd=on in

    [MQ2Melee](../mq2melee.md) to prevent MQ2Melee from doing anything undesired

  * if you use _/stick on_ in your macro, expect to be laughed at whole-heartedly

\* **/stick id** **\[\#\]**

* * sticks to the given spawn id
  * uses id of your current target if no spawn id is given
  * this allows you to continue sticking when your target changes, e.g. casting a heal on someone

\* **/stick \#** **\|** **\#%**

* * Stick at the specified distance or percentage

\* **/stick** **-\#**

* * Reduce current stick distance modifier by \#

\* **/stick moveback**

* * stick will back up to the value if the target gets closer, e.g. many targets in the rear pushing target

    too close to the tank

\* **/stick loose**

* * stick using turn increments instead of instant heading adjustment

\* **/stick truehead**

* * stick using actual keypress heading adjustments
  * **does not work if wineq option is enabled**

\* **/stick healer**

* * Healer sticking does not perform face adjustments to look at the target while in stick range
  * This is good for keeping a healer close & sticking to another group member without having it turn to face the

    other character constantly as it moves

  * Does not work with any strafe-style sticks \(pin front !front behind behindonce snaproll\)

\* **/stick uw** **\|** **underwater**

* * face angle will look up/down at the stick target

\* **/stick hold**

* * stick to the current target even if your target changes

\* **/stick behind**

* * stick to the rear of the target unless you are on HoTT. will spin in circles if you do not have HoTT and gain

    aggro \(to prevent: USE DelayStrafe OPTION !!!\)

\* **/stick behindonce**

* * stick behind the target when first moving into position, only using  enforcement after

\* **/stick !front**

* * stick to target anywhere but the frontal arc, same considerations as behind apply \(use DelayStrafe!\)

\* **/stick pin**

* * stick to the side of the target, same consideration as behind apply \(use DelayStrafe!\)

\* **/stick front**

* * stick to the front arc of the target
  * if you have HoTT and lose aggro you will not spin
  * this will not work by default without HoTT

\* **/stick \(ANY STICK VALUES\) always**

* * when current target is lost, will wait and then resume sticking using supplied values upon next NPC targeted
  * **does not work with stick hold or stick id**

\* **/stick snaproll** **\[** **left** **\|** **right** **\|** **face** **\|** **rear** **\]**

* * runs in a straight line behind your target then turns to face
  * left/right/front of target if optional parameter direction supplied
  * rear is default

''the following inline configuration options are supported for one-time use:

* \*\*/stick breakontarget \| breakongate \| breakonwarp \|

  pauseonwarp \| randomize \| delaystrafe \| useback \| usefleeing \| strafewalk \| mindelay \# \| maxdelay \# \|

  backupdist \# \| breakdist \# \| snapdist \# \| !frontarc \# \| behindarc \# &lt;/span&gt;\*\*

  * Read the \_set **name**\_section for explanation of what these parameters do

\* **/stick mod \#** **\|** **-\#**

* * modify stick distance by the supplied amount _\(does not turn stick on\)_

=== /moveto === _The moveto command will move you from your current location to a specific location or target. You can combine any number of these parameters together inline to enable multiple options for the moveto._

\* **/moveto loc Y X** **\[Z\]**

* * moves to the specified location
  * **z is optional**
  * **must be the first parameter**

\* **/moveto yloc Y** **\|** **xloc X**

* * beeline to the Y or X supplied
  * different from precisey/x in that this only considers a single axis
  * **must be the first parameter**

\* **/moveto id** **\[\#\]**

* * moves to the supplied spawn id, or your current target if no id is given

\* **/moveto off**

* * stop moving to the current target/location

\* **/moveto loose**

* * moveto using more human-like heading adjustments

\* **/moveto truehead**

* * moveto using actual keypress heading adjustments

\* **/moveto \(id** **\|** **loc Y X** **\[Z\]\) precisey** **\|** **precisex**

* * moves to loc stopping when within x or y arrival dist values instead of both
  * works with either id or loc

\* **/moveto uw** **\|** **underwater**

* * look angle up and down at destination

\* **/moveto dist \#**

* * sets value for how close to actual location is considered arrival
  * **does not turn moveto on**
  * **permanently changes the value**

\* **/moveto \[id** _**spawnid**_ **\|** **loc y x** **\[z\]\]** **mdist \#** **\[id\]**

* * sets value for how close to actual location is considered arrival
  * allowed inline **BEFORE** _id_ or **AFTER** _loc y x \[z\]_ or _id \[spawn id\]_ parameter
  * **permanently changes the value**

''the following inline configuration options are supported for one-time use:

* \*\*/moveto breakonaggro \| breakonhit \| usewalk \| useback

  \| backupdist \# \| ydist \# \| xdist \#&lt;/span&gt;\*\*

  * Read the \_set **name**\_section for explanation of what these parameters do

### /circle

_The circle command spins you in a circle. If you are like me, looking at this for the first time wondering what the point is, this is mainly for bards to use while circle kiting, but could equally be used for amusement. You can combine any number of these parameters together inline to enable multiple options for the circle._

\* **/circle on** **\[** **\#** **\]**

* * begin circling using your current location as the center with default radius
  * if optional \# parameter supplied, use \# as the radius size
  * **must be first parameter**

\* **/circle off**

* * stop circling

\* **/circle loc Y X**

* * begin circling using the specified location as the center
  * **must be first parameter**

\* **/circle drunken**

* * turn to complete the circle at random intervals

\* **/circle clockwise** **\|** **cw**

* * circle in a clockwise direction. \(default\)

\* **/circle cw** **\|** **counterclockwise** **\|** **reverse**

* * circle in a counter-clockwise direction

\* **/circle radius \#**

* * sets the default size of the circle radius
  * for use with loc y x since _on \#_ would have to be first param

\* **/circle backward**

* * run backwards instead of forwards

=== /makecamp === _The makecamp command will create a camp spot for you to return to after combat, or to establish boundries for your character to prevent them from moving beyond a certain radius._

\* **/makecamp**

* * using makecamp with no parameters will set up a camp at your current location, using default values

\* **/makecamp on** **\[** **\#** **\]**

* * set up a camp at current location with default values
  * if optional \# parameter supplied, use \# as camp radius size
  * **must be first parameter**

\* **/makecamp off**

* * disable current makecamp

\* **/makecamp loc Y X**

* * set up a camp at the specified location
  * **must be first parameter**

\* **/makecamp player** **\[** **name** **\]**

* * set up a dynamic camp based on a certain pc name if in zone, or targeted pc if optional name not supplied

\* **/makecamp leash**

* * toggles leashing to camp radius so character cannot leave boundary

\* **/makecamp leash \#**

* * sets how far beyond camp radius you can move before leashing \(LeashLength\)

\* **/makecamp radius \#**

* * sets the radius of the camp size
  * **does not turn camp on if supplied on its own**

\* **/makecamp mindelay \#** **\|** **maxdelay \#**

* * sets the delay time before auto-returning to camp

\* **/makecamp return**

* * forces a return to the camp radius immediately

\* **/makecamp altreturn**

* * forces a return to the camp spot you had before your current one, or a camp that is now turned off

''the following inline configuration options are supported for one-time use:

* \*\*/makecamp returnhavetarget \| returnnoaggro \|

  returnnotlooting \| realtimeplayer \| scatter \| bearing \# \| scatsize \# \| scatdist \#&lt;/span&gt;\*\*

  * Read the \_set **name**\_section for explanation of what these parameters do

=== Other Plugin Commands === _Less popular commands of MQ2MoveUtils_  
\* '''/calcangle

* * Displays lots of basic numerical information related to moving such as Dist values, angular distance, 3D

    distance, melee range, stick range, speed multipliers

  * This command is useful to help determine what to set plugin options such as arc values or AllowMove, backup

    dist, etc.

\* **/rootme \[** **off** **\]**

* * roots the player in place, unable to move. this is not any form of actual debuff, just a plugin implementation

    of locking a character in place

  * supplying the optional _off_ parameter disables the root
  * **other commands will not function when rootme is active**

== Top-Level Objects ==

### ${MoveUtils}

_Members of this datatype relate to plugin settings and generic information_

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| **Type** | **Member** | **Return Values** | **Description** |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Command** | NONE STICK MOVETO MAKECAMP CIRCLE | Displays the currently active command. MAKECAMP returns if a camp is setup but no other command is currently in use |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Stuck** | TRUE FALSE | Displays true if plugin stucklogic has determined you are currently stuck |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Summoned** | TRUE FALSE | Displays true if BreakOnSummon is enabled and has fired due to your character being summoned beyond breakonsummon distance |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **StuckLogic** | TRUE FALSE | Displays true if stucklogic is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Verbosity** | TRUE FALSE | Displays true if verbosity is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **FullVerbosity** | TRUE FALSE | Displays true if fullverbosity is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **TotalSilence** | TRUE FALSE | Displays true if totalsilence is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Aggro** | TRUE FALSE | Displays true if you are facing your target and your target is facing you |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **TryToJump** | TRUE FALSE | Displays true if stucklogic trytojump is enabled |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **PauseMinDelay** | 125 or greater | Displays the min delay for mousepause and mpause to resume command in ms |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **PauseMaxDelay** | 125 or more greater than PauseMinDelay | Displays the max delay for mousepause and mpause to resume command in ms |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **PulseCheck** | 1 or greater | Displays the number of pulses used to average movement rate for stucklogic |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **PulseUnstuck** | 1 or greater | Displays the number of pulses successfully moved forward after being stuck to be considered unstuck |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **DistStuck** | 0.01 or greater | Displays the amount of distance needed to have moved \(compared against pulse average\) or else considered stuck by stucklogic |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **Version** | \#.\#\#\#\# | Displays the version number of the plugin |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **MovePause** | TRUE FALSE | Displays true if mpause \(PauseKB\) is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **GM** | TRUE FALSE | Displays true if BreakOnGM fired |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **To String** | Same as **Command** | Same as **Command** |

=== ${Stick} === _Members of this datatype relate to the '/stick' command_

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| **Type** | **Member** | **Return Values** | **Description** |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Status** | OFF PAUSED ON | Displays ON if any form of stick is active |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Active** | TRUE FALSE | Displays true if any form of stick is active |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Broken** | TRUE FALSE | Returns true if BreakOnHit event has halted stick prematurely |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **Distance** | \#.\#\# | Current distance used by stick |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **MoveBehind** | TRUE FALSE | Displays true if stick behind is active |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **MoveBack** | TRUE FALSE | Displays true if moveback is active |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Loose** | TRUE FALSE | Displays true if loose sticking is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Paused** | TRUE FALSE | Displays true if plugin is paused |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Behind** | TRUE FALSE | Displays true if currently behind target \(regardless of _/stick behind_\), false if outside of stick dist or not behind |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Stopped** | TRUE FALSE | Displays true if stick is within stick distance |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Pin** | TRUE FALSE | Displays true if stick pin is active |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **StickTarget** | SpawnID | Returns spawnid of stick target if stick id/hold used, else spawnid of current target, 0 if no target and id/hold not used |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **StickTargetName** | NONE [DisplayedName](../../../data-types-and-top-level-objects/data-types/datatype-spawn.md) | Returns DisplayedName of stick target if stick id/hold used, else current target or NONE if no target and hold/id not used |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **DistMod** | \[-\]\#.\#\# | Current stickdist modifier |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **DistModPercent** | \#.\#\# | Current stickdist percent modifier |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Always** | TRUE FALSE | Returns true if _/stick always_ is active |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **To String** | Same as **Status** | Same as **Status** |

=== ${MoveTo} === _Members of this datatype relate to the '/moveto' command_

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| **Type** | **Member** | **Return Values** | **Description** |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Moving** | TRUE FALSE | Displays true if moveto or camp return is active |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Stopped** | TRUE FALSE | Displays true if the last moveto command completed successfully |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **CampStopped** | TRUE FALSE | Displays true if within moveto distance of makecamp Y X location |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **UseWalk** | TRUE FALSE | Returns true if UseWalk is enabled |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **ArrivalDist** | 1.00+ | Acceptable arrival distance |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **ArrivalDistY** | 1.00+ | Acceptable arrival distance for precisey |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **ArrivalDistX** | 1.00+ | Acceptable arrival distance for precisex |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Broken** | TRUE FALSE | Returns true if BreakOnAggro or BreakOnHit event have halted moveto prematurely |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **To String** | OFF PAUSED ON | Displays ON if a moveto command is active |

=== ${MakeCamp} === _Members of this datatype relate to the '/makecamp' command_

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| **Type** | **Member** | **Return Values** | **Description** |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Status** | OFF PAUSED ON | Displays status of MakeCamp command. AltCamp returns OFF |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Leash** | TRUE FALSE | Displays true if leash is enabled |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **AnchorX** | 0.00 | Location of current camp X anchor |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **AnchorY** | 0.00 | Location of current camp Y anchor |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **LeashLength** | Greater than or equal to CampRadius | Size of Leash Length |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **CampRadius** | 10.0+ | Size of camp radius |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **MinDelay** | 125 or greater | Displays the min delay for auto-returning to camp in ms |
| [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) | **MaxDelay** | 125 or more greater than MinDelay | Displays the max delay for auto-returning to camp in ms |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Returning** | TRUE FALSE | Displays true if _/makecamp return_ issued |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **AltAnchorX** | 0.00 | Location of current altcamp X anchor |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **AltAnchorY** | 0.00 | Location of current altcamp Y anchor |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **CampDist** | 0.00 | Distance to camp anchor from your current location. Returns 0.00 if camp is disabled |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **AltCampDist** | 0.00 | Distance to altcamp anchor from your current location. Returns 0.00 if altcamp not established |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **AltRadius** | 10.0+ | Size of altcamp radius |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Scatter** | TRUE FALSE | Displays true if camp scattering enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **ReturnNoAggro** | TRUE FALSE | Displays true if ReturnNoAggro is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **ReturnNotLooting** | TRUE FALSE | Displays true if ReturnNotLooting is enabled |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **ReturnHaveTarget** | TRUE FALSE | Displays true if ReturnHaveTarget is enabled |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **Bearing** | 0.00 | Bearing \(heading\) of camp scattering |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **ScatDist** | 1.0+ | Distance from anchor to perform scatter |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **ScatSize** | 1.0+ | Size of scattering radius |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **To String** | Same as **Status** | Same as **Status** |

=== ${Circle} === _Members of this datatype relate to the '/circle' command_

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| **Type** | **Member** | **Return Values** | **Description** |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Status** | OFF PAUSED ON | Returns ON if circling |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **CircleY** | 0.00 | Location of circle center Y |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **CircleX** | 0.00 | Location of circle center X |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Drunken** | TRUE FALSE | Displays true if drunken |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Rotation** | CW CCW | Displays CCW if reverse circling |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Direction** | FORWARDS BACKWARDS | Movement direction of current circle |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Clockwise** | TRUE FALSE | Displays false if reverse circling |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Backwards** | TRUE FALSE | Displays true if movement direction backwards |
| [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) | **Radius** | 5.00+ | Radius size of circle |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **To String** | Same as **Status** | Same as **Status** |

== Configuration == _MQ2MoveUtils saves a configuration file to your root MQ2 folder: MQ2MoveUtils.ini_

### Default INI File

```text
[Defaults]
AllowMove=32.0
AutoPause=on
AutoPauseMsg=on
AutoSave=on
AutoUW=off
BreakKeyboard=on
BreakMouse=off
BreakOnGM=on
BreakOnSummon=off
DistSummon=8.00
FeignSupport=off
Heading=true
HideHelp=off
KeyboardPause=off
MousePause=off
LockPause=off
PauseMinDelay=500
PauseMaxDelay=5000
SaveByChar=on
TurnRate=14.00
UseWindow=off
Verbosity=on
FullVerbosity=on
TotalSilence=off
VerbosityFlags=33554431
WinEQ=off

[Stick]
AlwaysUW=off
AwareNotAggro=off
ArcBehind=45.0
ArcNotFront=135.0
BreakOnGate=on
BreakOnHit=off
BreakOnTarget=off
BreakOnWarp=on
PauseOnWarp=off
DelayStrafe=on
DistBackup=10.0
DistBreak=250.0
DistMod=0.0
DistMod%=1.0
DistSnaproll=10.0
RandomArc=off
StrafeMinDelay=1500
StrafeMaxDelay=3000
UseBackward=on
UseFleeing=on
UseWalk=off

[MakeCamp]
CampRadius=40.00
MinDelay=500
MaxDelay=1500
RealtimePlayer=off
ReturnHaveTarget=off
ReturnNoAggro=off
ReturnNotLooting=off
UseLeash=off
LeashLength=50.00
UseScatter=off
Bearing=0.00
ScatDist=10.00
ScatSize=10.00

[MoveTo]
AlwaysUW=off
ArrivalDist=10.0
ArrivalDistX=10.0
ArrivalDistY=10.0
BreakOnAggro=off
BreakOnHit=off
DistBackup=30.0
MoveToMod=0.0
UseBackward=off
UseWalk=on

[Circle]
Backward=off
CCW=off
Drunken=off
RadiusSize=30.0

[StuckLogic]
StuckLogic=on
DistStuck=0.10
PulseCheck=6
PulseUnstuck=10
TryToJump=off
TurnHalf=on

[Window]
ChatTop=10
ChatBottom=210
ChatLeft=10
ChatRight=410
Fades=0
Alpha=255
FadeToAlpha=255
Duration=500
Locked=0
Delay=2000
BGType=1
BGTint.red=255
BGTint.green=255
BGTint.blue=255
FontSize=2
WindowTitle=MoveUtils

[yourserver.yourcharacter]
DisregardMe=false
AllowMove=32.0
ArcBehind=45.0
ArcNotFront=135.0
AutoSave=on
AutoUW=off
DistBreak=250.0
BreakOnGate=on
BreakOnWarp=on
PauseOnWarp=off
LockPause=off
DistSnaproll=10.0
FeignSupport=off
Heading=true
LeashLength=50.00
UseLeash=off
UseWindow=off
Verbosity=on
FullVerbosity=on
VerbosityFlags=33554431
CampRadius=40.00
RealtimePlayer=off
UseScatter=off
Bearing=0.00
ScatDist=10.00
ScatSize=10.00
```

### INI options

Information on what the actual values can be and represent.

#### \[Defaults\]

This section is for default plugin settings

* _AllowMove_ - 10.0+, anti-orbit setting for true/loose heading representing angular distance before moving forward
* _AutoPause=_ - on or off, pauses command if casting spells, stunned, rooted, sitting, or self targeted
* _AutoPauseMsg=_ - on or off, displays output when AutoPause halts movement
* _AutoSave=_ - on or off, automatically save ini file when using 'toggle' or 'set'
* _AutoUW=_ - on or off, automatically use 'uw' heading adjustments when character is under water
* _BreakKeyboard=_ - on or off, break command from keyboard press
* _BreakMouse=_ - on or off, break command from mouselook usage
* _BreakOnGM=_ - on or off, break current command and prevent command usage if GM enters zone
* _BreakOnSummon=_ - on or off, halt command and ability to use commands if summoned beyond certain distance
* _DistSummon=_ - 2.0+, distance moved in a single pulse to trigger breakonsummon \(if on\)
* _FeignSupport=_ - on or off, fd support waits for you to stand up manually before moving, if feigned
* _Heading=_ = true or loose or fast, type of heading adjustments plugin will use \(fast=instant, loose=gradual

  emulated shift, true=real kb presses\)

* _HideHelp=_ - on or off, never automatically display help output unless requested
* _KeyboardPause=_ - on or off, pause command for a delay if keyboard press
* _MousePause=_ - on or off, pause command for a delay if mouselook used
* _LockPause=_ - on or off, plugin will not automatically unpause under any circumstance unless user unpauses
* _PauseMinDelay=_ - 125+ \(in ms\), minimum delay before resuming from mpause/mousepause
* _PauseMaxDelay=_ - 125 above min \(in ms\), maximum delay before resuming from mpause/mousepause
* _SaveByChar=_ - on or off, save \[server.Charname\] section of ini file for individual character settings
* _TurnRate=_ - 10.0 to 100.0, rate at which loose heading emulates turns
* _UseWindow=_ - on or off, uses a custom user-placed window for all moveutils output if enabled
* _Verbosity=_ - on or off, ChatWnd output for basic command info
* _FullVerbosity=_ - on or off, ChatWnd output for enhanced plugin info
* _TotalSilence=_ - on or off **overrides verb/fullverb**, silence ChatWnd output except for critical or

  user-requested messages

* _VerbosityFlags=_ - see verbosity section of this wiki
* _WinEQ=_ - on or off, when enabled moveutils uses feigned movement simulation due to the bug of WinEQ2 holding down

  alt keys and mouse buttons in background sessions

**note: if WinEQ is enabled, true heading is NOT possible**  
==== \[Stick\] ==== This section is for settings related to _/stick_

* _AlwaysUW=_ - on or off, if enabled stick will always use the 'uw' parameter as if it were typed inline
* _AwareNotAggro=_ - on or off, detect aggro loss if using stick front
* _ArcBehind=_ - 5.1 to 259.9, user can configure angular distance arc that "stick behind" uses
* _ArcNotFront=_ - 5.1 to 259.9, user can configure angular distance arc that "stick !front" uses
* _BreakOnGate=_ - on or off, break from stick if "target Gates." message occurs
* _BreakOnHit=_ - on or off, when enabled stick will halt if user is being attacked
* _BreakOnWarp=_ - on or off, break from stick if target warps beyond certain distance
* _PauseOnWarp=_ - on or off, pause stick unless target gets back in range if warps beyond certain distance \(break or

  pause, can't have both\)

* _DelayStrafe=_ - on or off, delay strafing movement when position adjustment required \(good for stopping endless

  circling if aggro is gained\)

* _DistBackup=_ - 1.0+, if you are within this distance when stick turned on, stick will walk backwards rather than

  spin in a circle to move to target

* _DistBreak=_ - 1.0+, distance mob moved in a single pulse to trigger breakonwarp \(if on\)
* _DistMod=_ - 0.0+, adjust default/supplied stick distance by this amount
* _DistMod%=_ - 0.0+ \(represents a percentage\), adjust default/supplied stick distance by this percent
* _DistSnaproll=_ - 1.0+, distance behind target snaproll will move before stopping and turning to face target
* _RandomArc=_ - on or off, randomize min/max arc for any strafe-based stick \(so you do not always stick to the exact

  same spot of a mob\)

* _StrafeMinDelay=_ - 125+ \(in ms\), minimum delay before attempting to strafe if delaystrafe enabled
* _StrafeMaxDelay=_ - 125 above min \(in ms\), maximum delay before attempting to strafe if delaystrafe enabled
* _UseBackward=_ - on or off, when enabled stick will walk backward rather than turn to face if within DistBackup of

  target

* _UseFleeing=_ - on or off, when enabled "stick front" will not attempt to position in front of the mob when target

  begins to flee

* _UseWalk=_ - on or off, when enabled stick uses walking when close to the target for precise movements and

  preventing overshooting

==== \[MakeCamp\] ==== This section is for settings related to _/makecamp_

* _CampRadius=_ - 5.0+, default camp radius size
* _MinDelay=_ - 125+ \(in ms\), minimum delay before auto-returning to camp
* _MaxDelay=_ - 125 above min \(in ms\), maximum delay before auto-returning to camp
* _RealtimePlayer=_ - on or off, when enabled "makecamp player" gets realtime location updates of player and adjusts

  returning on the fly

* _ReturnHaveTarget=_ - on or off, if on Auto-Return to camp even if you have a target \(default behavior is return

  only if no target\)

* _ReturnNoAggro=_ - on or off, Auto-Return to camp only if not aggro
* _ReturnNotLooting=_ - on or off, do not Auto-Return to camp if looting a corpse
* _UseLeash=_ - on or off, do not allow character to move beyond LeashLength
* _LeashLength=_ - \#.\# &gt;= camp radius, length of leash
* _UseScatter=_ - on or off, use specific scatter values instead of random return location
* _Bearing=_ - \#, bearing of scatter
* _ScatDist=_ - 1.0+, distance from camp center to perform scatter
* _ScatSize=_ - 1.0+, radius size of scatter area

==== \[MoveTo\] ==== This section is for settings related to _/moveto_

* _AlwaysUW=_ - on or off, if enabled moveto will always use the 'uw' parameter as if it were typed inline
* _ArrivalDist=_ - 1.0+, distance considered acceptable to have arrived at destination
* _ArrivalDistX=_ - 1.0+, distance considered acceptable to have arrived at destination when using precisex
* _ArrivalDistY=_ - 1.0+, distance considered acceptable to have arrived at destination when using precisey
* _BreakOnAggro=_ - on or off, when enabled moveto will halt if aggro is gained \(crossed swords in player window\)
* _BreakOnHit=_ - on or off, when enabled moveto will halt if user is being attacked
* _DistBackup=_ - 1.0+, moveto will walk backwards to location if within this distance rather than spin to face

  destination first

* _MoveToMod=_ - 0.0+, modifier applied to moveto arrivaldist
* _UseBackward=_ - on or off, when enabled moveto will use backward movement if within DistBackup \(applies to makecamp

  returns\)

* _UseWalk=_ - on or off, turn on walk when close to moveto location and camp return spot for precise movement

==== \[Circle\] ==== This section is for settings related to _/circle_

* _Backward=_ - on or off, always run backwards instead of forwards when circling
* _CCW=_ - on or off, always run in a ccw circle instead of default clockwise
* _Drunken=_ - on or off, always use drunken circling
* _RadiusSize=_ - 5.0+, default radius size of circle

==== \[StuckLogic\] ==== This section is for settings related to stucklogic

* _StuckLogic=_ - on or off, if enabled stucklogic detects and attempts to auto-correct getting stuck while moving
* _DistStuck=_ - 0.01+, distance needed to have moved or else stuck \(compared against an average\)
* _PulseCheck=_ - 1+, amount of pulses used to calculate moving average
* _PulseUnstuck=_ - 1+, number of pulses successfully moved forward to be considered unstuck
* _TryToJump=_ - on or off, attempt to jump to help get unstuck
* _TurnHalf=_ - on or off, if have turned halfway and failed to get unstuck, reset heading and try other direction

  instead

==== \[Window\] ====

* _ChatTop=_ - See EQ XML UI file settings
* _ChatBottom=_ - See EQ XML UI file settings
* _ChatLeft=_ - See EQ XML UI file settings
* _ChatRight=_ - See EQ XML UI file settings
* _Fades=_ - See EQ XML UI file settings
* _Alpha=_ - See EQ XML UI file settings
* _FadeToAlpha=_ - See EQ XML UI file settings
* _Duration=_ - See EQ XML UI file settings
* _Locked=_ - See EQ XML UI file settings
* _Delay=_ - See EQ XML UI file settings
* _BGType=_ - See EQ XML UI file settings
* _BGTint.red=_ - See EQ XML UI file settings
* _BGTint.green=_ - See EQ XML UI file settings
* _BGTint.blue=_ - See EQ XML UI file settings
* _FontSize=_ - 1 to 10, default font size for window
* _WindowTitle=_ - custom user title for the window

==== \[yourserver.yourcharacter\] ==== if savebychar is on, this section will be created for every character The settings in this section are some of the above values that could be desired to vary on a char-by-char basis \(including WINDOW settings\) with the exception of one value:

* _DisregardMe=_ true or false, if you want custom character values to load for some characters but this specific

  character to use the default values instead, set this to true and though a lot of entries will be written to this

  section, they will be ignored for this specific character

=== Verbosity === The verbosity system has been revamped to use bit flags for superior control of what messages will be displayed by the plugin. The older system has not been removed - if this is difficult to understand you may still use _verbosity_, _fullverbosity_ and _totalsilence_ as before. For those familiar with bit flags the flags table is below. If you have never worked with bit flags before, here is a brief summary of how to use the information below. Each subset of messages is assigned a numerical value. By adding the numerical values of the messages you want on together, you are able to customize each message that is shown or not shown. Examples:

* If you only wanted the plugin to display 'settings' and 'errors', you would look at the value of settings in the

  table below \(8192\) and the value of errors \(4194304\) and add them together to get \(4202496\). By setting your

  verbosity flag to 4202496 \(using the _set verbflags_ parameter or by saving the value in the INI file\) the plugin

  would then filter out everything except messages related to changing settings or error messages.

* If you only wanted to display 'stick verbosity' messages and nothing else, you would look up the value in the table

  below \(32\) and set your flags to 32 without adding anything to it.

* If you want to display a large number of messages, you continue to add them all together and use the total. To

  display 'autopause', 'movepause', 'stick verbosity', 'stick fullverbosity', 'settings' and 'errors', you would add

  all their values from the below table \(1 + 2 + 32 + 64 + 8192 + 4194304 = 4202595\) and use that number for your

  flags setting \(/stick set verbflags 4202595\)

#### Flags Table

```text
0 - total plugin silence
1 - autopause
2 - movepause, mousepause, breakonkb
4 - breakonmouse
8 - feign support
16 - hidehelp
32 - stick verbosity
64 - stick full verbosity
128 - moveto verbosity
256 - moveto full verbosity
512 - makecamp verbosity
1024 - makecamp full verbosity
2048 - circle verbosity
4096 - circle full verbosity
8192 - settings
16384 - file input / output
32768 - breakonwarp
65536 - breakonaggro
131072 - breakonhit
262144 - breakonsummon
524288 - breakongm
1048576 - breakongate
2097152 - stick always
4194304 - error messages
8388608 - arc randomization
16777216 - pause / unpause
2720 - prior 'verbosity' setting
11736390 - prior 'fullverbosity' setting
33554431 - all messages enabled
```

#### Actual Messages

Here is a list of exactly what messages are tied to each flag:

* 1 - autopause

  _AutoPause halting movement..._ \(when autopaused if autopause is enabled\)

  _Movement pausing due to self target..._ \(if self targeted during a stick with autopause off\)

* 2 - movepause, mousepause, breakonkb

  _Current command ended from manual movement._

  _Resuming previous command from movement pause._

* 4 - breakonmouse

  _Current command ended from mouse movement._

* 8 - feign support

  _Not standing as you are currently Feign Death_

* 16 - hidehelp

  Hidehelp when turned on prevents the help output \(seen in /stick help\) from being automatically output if you input a command incorrectly

* 32 - stick verbosity

  _You are now sticking to TargetName._

  _You are no longer sticking to anything._

  _You will now stick to every valid NPC target supplied._

* 64 - stick full verbosity

  Dir\(ANY\) Dist\(10.0\) Head\(true\) ID\(31337\) UW MB HEALER

* 128 - moveto verbosity

  _Moveto off._

  _Arrived at moveto location_

* 256 - moveto full verbosity

  _Moving to loc \#, \# Dist\(10\) Head\(true\)_

* 512 - makecamp verbosity

  _MakeCamp actived. Y\(\#\) X\(\#\) Radius\(\#\) Leash\(\#\) LeashLen\(\#\) Min\(\#\) Max\(\#\)_

  _MakeCamp returning to within camp radius immediately_

  _MakeCamp returning to altcamp immediately._

  _MakeCamp returning to altcamp immediately. Current camp now OFF._

  _MakeCamp player ended due to player leaving/death_

  _Outside of leash length, breaking from current command_

* 1024 - makecamp full verbosity

  _Ended '/moveto' or '/makecamp return' because leash is on._

* 2048 - circle verbosity

  _Circling radius \(\#\), center \(\#, \#\) OFF_

* 4096 - circle full verbosity

  **none at this time**

* 8192 - settings

  _Stick modifier changed to Mod\(\#\) Mod%\(\# %\)_ \(from /stick mod \#\)

  _Stick mod changed Mod\(\#\) ModPercent\(\# %\)_ \(from stick inline -\# or \#%\)

  _Moveto distance mod changed to \#._ \(from /moveto dist \#\)

  _Option turned ON_ \(from /command set option on, or /command toggle option\)

  _Option turned OFF_ \(from /command set option off, or /command toggle option\)

  _Option set to \#_ \(from /command set option \#\)

* 16384 - file input / output

  _Debug file created._

  _Saved settings to C:\yourpath\MQ2MoveUtils.ini_ \(from /command save\)

  _Loaded settings from C:\yourpath\MQ2MoveUtils.ini_ \(from /command load\)

* 32768 - breakonwarp

  _Stick pausing until target back in BreakDist range..._

  _Stick ending from target warping out of BreakDist range._

* 65536 - breakonaggro

  BreakOnAggro's: _Aggro gained during /moveto, Halting command..._

* 131072 - breakonhit

  BreakOnHit's: _Aggro gained during /moveto, Halting command..._

* 262144 - breakonsummon

  _WARNING Command ended from character summoned \# distance in a pulse._

  _WARNING Verify you are not being monitored and type /stick imsafe to allow command usage._

* 524288 - breakongm

  _WARNING Plugin halted from \[GM\] Name in zone._

  _\[GM\] Name has left the zone or turned invisible. Use /stick imsafe to allow command usage._

* 1048576 - breakongate

  _Mob gating ended previous command._

* 2097152 - stick always

  _Stick awaiting next valid NPC target..._

* 4194304 - error messages

  _\(ERROR\) /moveto or /circle command used with no parameter._

  _\(ERROR\) Plugin was already paused._

  _\(ERROR\) Plugin was not paused._

  _\(ERROR\) /stick mod \[\#\] supplied incorrectly._

  _\(ERROR\) /moveto yloc \[Y\] was supplied incorrectly._

  _\(ERROR\) /moveto xloc \[X\] was supplied incorrectly._

  _\(ERROR\) SpawnID must be a positive numerical value._

  _\(ERROR\) You cannot use yourself or your mount._

  _\(ERROR\) You cannot stick hold to yourself._

  _\(ERROR\) Incorrectly used /moveto dist \[\#\]_

  _\(ERROR\) /makecamp \[radius \] was supplied incorrectly._

  _\(ERROR\) You do not have an active camp._

  _\(ERROR\) You cannot use this command with a player-camp active._

  _\(ERROR\) You cannot use this command until you've established an altcamp location._

  _\(ERROR\) Invalid player name and do not have a valid player target._

  _\(ERROR\) You cannot makecamp yourself._

  _\(ERROR\) Use /circle radius \[\#\] to set radius._

  _ERROR: Invalid 'option set' syntax \( option \) \[on\|off\|number\]_

  _ERROR: Not a valid command toggle \( option \)._

  _ERROR: Not a valid command set option \( option \)._

  _Error - Font must be between 1 and 10._

  _ERROR: Invalid 'command set' parameter \( option \)_

  _\(ERROR\) You cannot stick to yourself!_

  _You must specify something to stick to!_

  _\(ERROR\) /moveto loc \[ \[z\] \] was supplied incorrectly._

  _\(ERROR\) /makecamp loc \[ \] was supplied incorrectly._

  _\(ERROR\) Usage /circle loc \[ \] \[other options\]_

  _\(ERROR\) Invalid SpawnID and do not have a valid target._

  _\(ERROR\) /makecamp \[mindelay\|maxdelay\] \[\#\] was supplied incorrectly._

* 8388608 - arc randomization

  _Arcs Randomized! Max: \# Min: \#_

* 16777216 - pause / unpause

  _PAUSED_ \(from /command pause\)

  _RESUMED_ \(from /command unpause\)

## See Also

* [MQ2MoveUtils Revision History](mq2moveutils-v11-revisions.md)
* [MQ2MoveUtils Older Versions](./)
* [MQ2MoveUtils History](mq2moveutils-history.md)
* [MacroQuest2 Plugins](../../../documentation/macroquest2-plugins.md)
* [Top-Level Objects](../../../data-types-and-top-level-objects/top-level-objects/)
* [Data Types](../../../data-types-and-top-level-objects/data-types/)

