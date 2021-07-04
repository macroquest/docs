## General Details

Version 9 of MQ2MoveUtils was a rewrite from the ground up by pms. The original goal behind this
rewrite was to cleanup numerous logical errors and reduce the amount of code duplication that existed in previous
releases. Once this rewrite was complete and functional, version 9 expanded including more enhancements and more
extensive configuration. Numbered by release date, the current of this plugin is 16.0717.

This plugin is no longer under active development and no new contributions have been made since 2011 by pms, with only
one follow-up contribution in 2014 by Cr4zyb4rd. Others have continued to keep the offsets updated in the discussion
thread linked below.

### Links

-   Link to the latest stable source: [16-Nov-2016th patch fix by
    trevyn](https://macroquest2.com/phpBB3/download/file.php?id=988)
-   Link to older sources: [MQ2MoveUtils v11.x Source](http://mq2.whyarewehappening.com/MQ2MoveUtils/)

<!-- -->

-   Link to emulator version of the source that works with the December 19, 2008 client: [MoveUtils v11 for EMU by
    pms](https://macroquest2.com/phpBB3/viewtopic.php?p=155710#p155710)

<!-- -->

-   Link to current discussion thread: [MQ2MoveUtils v16.x
    Thread](https://macroquest2.com/phpBB3/viewtopic.php?t=15909)

### Development Notes

For the development history of this plugin, see the article MQ2MoveUtils 16.x Revision
History

For the chronicle of the entire MoveUtils plugin including the original development history, see the article
[MQ2MoveUtils:History](../history/mq2moveutils-history.md)

### Help

-   [Frequently Asked Questions](../example/mq2moveutils-v11-faq.md)
-   Configuration Examples

## Command Information

### Main Plugin Commands

*These parameters can be used from any of the four main plugin commands ('/stick', '/moveto', '/circle', and
'/makecamp'). For example purposes the most popular '/stick' command will be used.*  
  
\* **<span style="color:red">/stick</span> <span style="color:blue">help \[settings\]</span>**

-   -   Displays generic help information, and help for the command used
    -   The *settings* optional parameter displays help information for all plugin 'set' and 'toggle' commands

  
\* **<span style="color:red">/stick</span> <span style="color:blue">debug</span>**

-   -   Dumps the current values of all plugin variables to a debug INI file

  
\* **<span style="color:red">/stick</span> <span style="color:blue">status \[all\]</span>**

-   -   ChatWnd output for the status of the issuing command (stick in this example)
    -   The *all* optional parameter displays status output for all aspects of the plugin

  
\* **<span style="color:red">/stick</span> <span style="color:blue">pause \[lock\]</span>**

-   -   Pauses all aspects of the plugin
    -   The *lock* optional parameter prevents plugin from automatically unpausing under any circumstance other than
        user issuing *unpause*
    -   **Note: This does not toggle**

  
\* **<span style="color:red">/stick</span> <span style="color:blue">unpause</span>**

-   -   Resumes all aspects of the plugin
    -   **Note: This does not toggle**

  
\* **<span style="color:red">/stick</span> <span style="color:blue">save</span> \|
<span style="color:blue">load</span>**

-   -   Saves or load your current configuration settings using MQ2MoveUtils.ini

  
\* **<span style="color:red">/stick</span> <span style="color:blue">imsafe</span>**

-   -   BreakOnSummon and BreakOnGM have built-in protection disabling the ability to re-issue commands when triggered.
        This prevents macros from continuing to issue commands in a possibly unsafe situation
    -   The *imsafe* parameter allows command usage to resume

  
\* **<span style="color:red">/stick</span> <span style="color:blue">min</span>**

-   -   Minimizes custom user window similar to [/mqmin](../commands/mqmin.md)

  
\* **<span style="color:red">/stick</span> <span style="color:blue">clear</span>**

-   -   Clears custom user window buffer similar to [/mqclear](../commands/mqclear.md)

  
\* **<span style="color:red">/stick</span> <span style="color:blue">verbflags</span>**

-   -   Outputs current verbosity flags setting (this one displays even if totalsilence is enabled. too bad.)

  
=== Main Plugin Settings === *These setting parameters can be used from any of the four main plugin commands.*  
*The following can be used with* **toggle** *or* **set *name* on \| off.**  
  
\* **<span style="color:red">/stick</span> <span style="color:blue">toggle *name*</span>**

-   **<span style="color:red">/stick</span> <span style="color:blue">set *name* on</span> \|
    <span style="color:blue">off</span>**

  
***name* can be one of the following:**  
\* **<span style="color:blue">mpause</span> \| <span style="color:blue">mousepause</span>**

-   -   Pause current command if \[ keyboard \| mouse \] movement
    -   Resumes after a random amount of delay set with *pausemindelay* and *pausemaxdelay* below
    -   **Note: You *may not* have a pause and corresponding break on at the same time (e.g. no mpause and breakonkb at
        the same time)**
    -   **You *may* have opposing options different though (e.g. mousepause on and breakonkb on)**

  
\* **<span style="color:blue">breakonkb</span> \| <span style="color:blue">breakonmouse</span>**

-   -   Break current command if \[ keyboard \| mouse \] movement
    -   **Note: You *may not* have a pause and corresponding break on at the same time (e.g. no mpause and breakonkb at
        the same time)**
    -   **You *may* have opposing options different though (e.g. mousepause on and breakonkb on)**

  
\* **<span style="color:blue">autosave</span>**

-   -   Automatically save settings to INI file when a *toggle* or *set* command is issued

  
\* **<span style="color:blue">savebychar</span>**

-   -   Save \[server.*Yourcharacter*\] section of INI file for individual character settings

  
\* **<span style="color:blue">feign</span>**

-   -   Enable Feign Death support, which waits for you to stand up manually before moving

  
\* **<span style="color:blue">lockpause</span>**

-   -   Plugin will never automatically resume from *pause* until user issues an *unpause*

  
\* **<span style="color:blue">autopause</span>**

-   -   Pause movement if casting spells (non-bard), stunned, rooted, sitting, FD, or self targeted (non-hold)

  
\* **<span style="color:blue">autopauseoutput</span>**

-   -   If enabled, will display ChatWnd output when autopause is halting movement
    -   **Note: This bypasses *totalsilence* and must be configured individually**

  
\* **<span style="color:blue">stucklogic</span>**

-   -   If enabled, stucklogic automatically attempts to get unstuck if running into walls and large objects

  
\* **<span style="color:blue">trytojump</span>**

-   -   If enabled, stucklogic also tries to jump to help get unstuck

  
\* **<span style="color:blue">turnhalf</span>**

-   -   If enabled, stucklogic will reset heading and turn the other direction if it has rotated halfway without success

  
\* **<span style="color:blue">verbosity</span>**

-   -   ChatWnd output for basic command information messages

  
\* **<span style="color:blue">fullverbosity</span>**

-   -   ChatWnd output for more detailed information messages and output for more actions

  
\* **<span style="color:blue">totalsilence</span>**

-   -   Silences most ChatWnd output except for critical information or user-requested messages

  
\* **<span style="color:blue">totalverbosity</span>**

-   -   Enable display of every ChatWnd message in the plugin

  
\* **<span style="color:blue">hidehelp</span>**

-   -   If enabled, the help output will not be displayed upon command failure (e.g. invalid parameters)

  
\* **<span style="color:blue">window</span>**

-   -   If enabled, MoveUtils will output any messages to a user-placed custom UI window dedicated to the plugin

  
\* **<span style="color:blue">wineq</span>**

-   -   By default, MoveUtils uses actual keypresses to control movement (regardless of heading settings)
    -   WinEQ2 has a bug where background sessions can have their alt keys and certain mouse buttons held down, causing
        movement to run in weird directions
    -   For Lavishsoft users who have not switched over to Innerspace, enabling *wineq* setting will use old-style
        emulated movement via ExecuteCmd()

  
\* **<span style="color:blue">breakontarget</span>**

-   -   Break from stick if target changes (default behavior is switch over to sticking to new target)

  
\* **<span style="color:blue">breakonsummon</span>**

-   -   Halts current command and disables ability to use any commands if summoned beyond *summondist*
    -   **Note: Once this fires, you must use the *imsafe* parameter to unlock the plugin**

  
\* **<span style="color:blue">breakongm</span>**

-   -   Halts current command and disables ability to use any commands if **visible** GM enters the zone
    -   **Note: Once this fires, you must use the *imsafe* parameter to unlock the plugin**

  
\* **<span style="color:blue">breakonwarp</span>**

-   -   Breaks from stick if target warps out of *breakdist* range (user set, see below)
    -   **Note: This does not limit your initial stick range. You may /stick from across the zone**

  
\* **<span style="color:blue">pauseonwarp</span>**

-   -   Pauses stick if target warps out of *breakdist* range until they are back in range (user set, see below)
    -   **Note: This does not limit your initial stick range. You may /stick from across the zone**

  
\* **<span style="color:blue">breakongate</span>**

-   -   Breaks from stick if ***target* Gates.** message occurs
    -   **Note: if using stick id or stick hold, it will break based on the held target name**

  
\* **<span style="color:blue">breakonaggro</span>**

-   -   Breaks from moveto command if you are aggro to an NPC
    -   **Note: This checks the player window for the crossed swords indicator**

  
\* **<span style="color:blue">alwaysdrunk</span>**

-   -   Use *drunken* by default when circling

  
\* **<span style="color:blue">alwaysbackwards</span>**

-   -   Run backwards by default when circling

  
\* **<span style="color:blue">alwaysccw</span>**

-   -   Circle in a counter-clockwise direction by default

  
\* **<span style="color:blue">nohottfront</span>**

-   -   Allow for *stick front* to spin to front of the mob without Health of Target's Target Leader AA
    -   **Note: By default stick front will not stay stuck to the front unless you are on the HoTT window**

  
\* **<span style="color:blue">returnnoaggro</span>**

-   -   Makecamp will auto-return to camp only if not aggro (checks crossed swords indicator)

  
\* **<span style="color:blue">returnnotlooting</span>**

-   -   Makecamp will not auto-return to camp if character has an open loot corpse window

  
\* **<span style="color:blue">returnhavetarget</span>**

-   -   Makecamp will auto-return to camp even if you have a target
    -   **Note: By default, makecamp does not auto-return if you have any target**

  
\* **<span style="color:blue">realtimeplayer</span>**

-   -   Makecamp player will get realtime updates on player location, allowing for dynamic returns to players
    -   By default, makecamp player will return to a players last location when return begins and not get a new update
        until the return is complete
    -   The default behavior is a sort of ghetto MQ2AdvPath whereas enabling realtimeplayer will work more like an
        autofollow

  
\* **<span style="color:blue">leash</span>**

-   -   If enabled, leash prevents moving beyond leashlength (user set value)

  
\* **<span style="color:blue">usewalk</span>**

-   -   If enabled, plugin will switch to walking when closing in on moveto destination or camp return

  
\* **<span style="color:blue">strafewalk</span>**

-   -   If enabled, plugin will switch to walking when within strafe range for all stick commands

  
\* **<span style="color:blue">randomize</span>**

-   -   If enabled, stick behind and !front will use random arc values to position

  
\* **<span style="color:blue">delaystrafe</span>**

-   -   If enabled, strafe-based movement (stick front, !front, behind, pin) will use a delay before moving
    -   **Note: This helps prevent endless circling when aggro is gained, or spinning when mobs quick-turn to cast
        spells**
    -   **Circling is one of the biggest signs that a player is using MoveUtils so it is recommended you ALWAYS leave
        this enabled**

  
\* **<span style="color:blue">autoUW</span>**

-   -   If enabled, stick and moveto will use the *uw* parameter whenever underwater (look up and down at target)

  
\* **<span style="color:blue">usefleeing</span>**

-   -   If enabled, stick front will not attempt to position in the front of a target that is fleeing

  
\* **<span style="color:blue">usescatter</span>**

-   -   If enabled, camp returns will use scattered return locations instead of default behavior
    -   **Note: Default behavior attempts to get back within camp radius**

  
  
*The following option is unique*

-   **<span style="color:red">/stick set</span> <span style="color:blue">heading *true \| loose \| fast* </span>**
    -   Changes plugin heading adjustments to use the specified type
    -   true: actual keypressing -- **does not work with wineq=on**
    -   loose: simulated incremental turning -- fast: instantly set heading

  
  
  
*The following 'set' commands require a numeric value, and can be used from any of the four main plugin commands. (stick
used for example purposes only)*  
\* **<span style="color:red">/stick set</span> <span style="color:blue">pulsecheck #</span>**

-   -   Number of pulses used to calculate average movement distance in stucklogic
    -   Valid: 1 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">pulseunstuck #</span>**

-   -   Number of pulses successfully moved forward before considered unstuck
    -   Valid: 1 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">diststuck #.##</span>**

-   -   Minimum distance needed to move or else considered stuck (compares against pulse average)
    -   Valid: 0.01 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">campmindelay #</span>**

-   -   Minimum delay before auto-returning to camp (in ms)
    -   Valid: 125 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">campmaxdelay #</span>**

-   -   Maximum delay before auto-returning to camp (in ms)
    -   Valid: 125 more than campmindelay

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">pausemindelay #</span>**

-   -   Minimum delay before resuming from mpause/mousepause (in ms)
    -   Valid: 125 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">pausemaxdelay #</span>**

-   -   Maximum delay before resuming from mpause/mousepause (in ms)
    -   Valid: 125 more than pausemindelay

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">strafemindelay #</span>**

-   -   Minimum delay before stick will strafe to move when delaystrafe is enabled (in ms)
    -   Valid: 125 or higher
    -   **note: higher values are better. default of 1500 (1.5s) is recommended**

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">strafemaxdelay #</span>**

-   -   Maximum delay before stick will strafe to move when delaystrafe is enabled (in ms)
    -   Valid: 125 higher than strafemindelay
    -   **note: higher values are better. default of 3000 (3s) is recommended**

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">ydist #.##</span>**

-   -   Acceptable distance to have "arrived" for precisey moveto
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">xdist #.##</span>**

-   -   Acceptable distance to have "arrived" for precisex moveto
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">snapdist #.##</span>**

-   -   Default distance to run past target before turning to snaproll
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">summondist #.##</span>**

-   -   Distance character must be summoned in a single pulse for BreakOnSummon to fire
    -   Valid: 2.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">turnrate #.#</span>**

-   -   Rate at which loose heading turns
    -   Valid: 1.0 to 100.0

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">!frontarc #.#</span>**

-   -   Angular distance arc for stick !front
    -   Valid: 1.1 to 260.0

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">behindarc #.#</span>**

-   -   Angular distance arc for stick behind
    -   Valid: 1.1 to 260.0

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">breakdist #.##</span>**

-   -   Distance to check for breakonwarp
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">campradius #.##</span>**

-   -   Default camp radius and radius for active camp
    -   Valid: 5.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">circleradius #.##</span>**

-   -   Default circle radius
    -   Valid: 5.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">leashlength #.#</span>**

-   -   Default leash length and length for active leash
    -   Valid: greater or equal to camp radius

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">bearing #.#</span>**

-   -   Bearing (direction from center) used for scatter camp
    -   Valid: any

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">scatsize #.##</span>**

-   -   Radius size for scattering
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">scatdist #.##</span>**

-   -   Distance from center of camp to scatter at
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">allowmove #.##</span>**

-   -   Loose or True heading allow forward movement when reach this angular distance
    -   This is "anti-orbit" code to stop circling near close-range destinations
    -   Valid: 10.1 or higher

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">font #</span>**

-   -   Custom user window font size
    -   Valid: 1 to 10

  
\* **<span style="color:red">/stick set</span> <span style="color:blue">verbflags #</span>**

-   -   Current plugin verbosity flags
    -   Valid: see verbosity section near bottom of this wiki entry

  
  
*The following settings are command-specific, use the command in the example only*  
\* **<span style="color:red">/stick set</span> <span style="color:blue">backupdist #.##</span>**

-   -   Range that stick will walk backwards instead of turning to face target, if useback enabled
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/moveto set</span> <span style="color:blue">backupdist #.##</span>**

-   -   Range that moveto will walk backwards instead of turning to face destination, if useback enabled
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/moveto set</span> <span style="color:blue">dist #.##</span>**

-   -   Acceptable distance to have "arrived" for standard moveto and camp returns
    -   Valid: 1.0 or higher

  
\* **<span style="color:red">/stick \[ toggle \| set \]</span> <span style="color:blue">alwaysUW</span>
<span style="color:red">\[ on \| off \]</span>**

-   -   If enabled, stick will always adjust looking angle as if *uw* parameter was typed inline
    -   **Note: this is not the same as *autoUW*, which only enables *uw* when actually underwater**

  
\* **<span style="color:red">/moveto \[ toggle \| set \]</span> <span style="color:blue">alwaysUW</span>
<span style="color:red">\[ on \| off \]</span>**

-   -   If enabled, moveto will always adjust looking angle as if *uw* parameter was typed inline
    -   **Note: this is not the same as *autoUW*, which only enables *uw* when actually underwater**

  
\* **<span style="color:red">/stick \[ toggle \| set \]</span> <span style="color:blue">breakonhit</span>
<span style="color:red">\[ on \| off \]</span>**

-   -   Breaks from stick command if you are attacked by an NPC
    -   **Note: This parses chat for hits and misses. If you use the number only hitsmode then it will only parse for
        misses**

  
\* **<span style="color:red">/moveto \[ toggle \| set \]</span> <span style="color:blue">breakonhit</span>
<span style="color:red">\[ on \| off \]</span>**

-   -   Breaks from moveto command if you are attacked by an NPC
    -   **Note: This parses chat for hits and misses. If you use the number only hitsmode then it will only parse for
        misses**

  
\* **<span style="color:red">/stick \[ toggle \| set \]</span> <span style="color:blue">useback</span>
<span style="color:red">\[ on \| off \]</span>**

-   -   If enabled, stick will walk backwards to position itself when close to a target instead of turning to face it
    -   **Note: This requires *loose* or *truehead* style heading adjustments, and does not work with fast heading**

  
\* **<span style="color:red">/moveto \[ toggle \| set \]</span> <span style="color:blue">useback</span>
<span style="color:red">\[ on \| off \]</span>**

-   -   If enabled, moveto will walk backwards to position itself when close to a destination instead of turning to face
        it
    -   **Note: This requires *loose* or *truehead* style heading adjustments, and does not work with fast heading**
    -   This **includes** automatic and user-forced camp returns

  
\* **<span style="color:red">/stick \[ toggle \| set \]</span> <span style="color:blue">loose \| truehead</span>
<span style="color:red">\[ on \| off \]</span>**

-   **<span style="color:red">/moveto \[ toggle \| set \]</span> <span style="color:blue">loose \| truehead</span>
    <span style="color:red">\[ on \| off \]</span>**
-   **<span style="color:red">/circle \[ toggle \| set \]</span> <span style="color:blue">loose \| truehead</span>
    <span style="color:red">\[ on \| off \]</span>**
    -   Change the heading type for currently active (stick \| moveto \| circle) to this type of heading. If *WinEQ* is
        enabled, truehead will fail to switch.
    -   Once current command ends, heading type will return to previous.

  
  

### /stick

*The stick command sticks you to your target, so that if your target moves you will move along with it. There are many
different parameters that cause this command to behave in different ways. You can combine any number of these parameters
together inline to enable multiple options for the stick.*  
  
\* '''<span style="color:red">/stick</span>

-   -   stick with no parameters will stick you to your current target, using max melee range

  
\* **<span style="color:red">/stick</span> <span style="color:blue">on \| off</span>**

-   -   turns stick on and off with default values
    -   on is a nearly-useless parameter and only included to support older macros or stickcmd=on in
        [MQ2Melee](mq2melee.md) to prevent MQ2Melee from doing anything undesired
    -   if you use */stick on* in your macro, expect to be laughed at whole-heartedly

  
\* **<span style="color:red">/stick</span> <span style="color:blue">id \[#\]</span>**

-   -   sticks to the given spawn id
    -   uses id of your current target if no spawn id is given
    -   this allows you to continue sticking when your target changes, e.g. casting a heal on someone

  
\* **<span style="color:red">/stick</span> <span style="color:blue"># \| #%</span>**

-   -   Stick at the specified distance or percentage

  
\* **<span style="color:red">/stick</span> <span style="color:blue"> -#</span>**

-   -   Reduce current stick distance modifier by #

  
\* **<span style="color:red">/stick</span> <span style="color:blue">moveback</span>**

-   -   stick will back up to the <dist> value if the target gets closer, e.g. many targets in the rear pushing target
        too close to the tank

  
\* **<span style="color:red">/stick</span> <span style="color:blue">loose</span>**

-   -   stick using turn increments instead of instant heading adjustment

  
\* **<span style="color:red">/stick</span> <span style="color:blue">truehead</span>**

-   -   stick using actual keypress heading adjustments
    -   **does not work if wineq option is enabled**

  
\* **<span style="color:red">/stick</span> <span style="color:blue">healer</span>**

-   -   Healer sticking does not perform face adjustments to look at the target while in stick range
    -   This is good for keeping a healer close & sticking to another group member without having it turn to face the
        other character constantly as it moves
    -   Does not work with any strafe-style sticks (pin front !front behind behindonce snaproll)

  
\* **<span style="color:red">/stick</span> <span style="color:blue">uw \| underwater</span>**

-   -   face angle will look up/down at the stick target

  
\* **<span style="color:red">/stick</span> <span style="color:blue">hold</span>**

-   -   stick to the current target even if your target changes

  
\* **<span style="color:red">/stick</span> <span style="color:blue">behind</span>**

-   -   stick to the rear of the target unless you are on HoTT. will spin in circles if you do not have HoTT and gain
        aggro (to prevent: USE DelayStrafe OPTION !!!)

  
\* **<span style="color:red">/stick</span> <span style="color:blue">behindonce</span>**

-   -   stick behind the target when first moving into position, only using <dist> enforcement after

  
\* **<span style="color:red">/stick</span> <span style="color:blue">!front</span>**

-   -   stick to target anywhere but the frontal arc, same considerations as behind apply (use DelayStrafe!)

  
\* **<span style="color:red">/stick</span> <span style="color:blue">pin</span>**

-   -   stick to the side of the target, same consideration as behind apply (use DelayStrafe!)

  
\* **<span style="color:red">/stick</span> <span style="color:blue">front</span>**

-   -   stick to the front arc of the target
    -   if you have HoTT and lose aggro you will not spin
    -   this will not work by default without HoTT

  
\* **<span style="color:red">/stick</span> <span style="color:blue">(ANY STICK VALUES) always</span>**

-   -   when current target is lost, will wait and then resume sticking using supplied values upon next NPC targeted
    -   **does not work with stick hold or stick id**

  
\* **<span style="color:red">/stick</span> <span style="color:blue">snaproll \[ left \| right \| face \| rear
\]</span>**

-   -   runs in a straight line behind your target then turns to face
    -   left/right/front of target if optional parameter direction supplied
    -   rear is default

  
  
''the following inline configuration options are supported for one-time use:

-   **<span style="color:red">/stick</span> <span style="color:blue">breakontarget \| breakongate \| breakonwarp \|
    pauseonwarp \| randomize \| delaystrafe \| useback \| usefleeing \| strafewalk \| mindelay # \| maxdelay # \|
    backupdist # \| breakdist # \| snapdist # \| !frontarc # \| behindarc # </span>**
    -   Read the *set **name***section for explanation of what these parameters do

  
\* **<span style="color:red">/stick</span> <span style="color:blue">mod # \| -#</span>**

-   -   modify stick distance by the supplied amount *(does not turn stick on)*

  
  
=== /moveto === *The moveto command will move you from your current location to a specific location or target. You can
combine any number of these parameters together inline to enable multiple options for the moveto.*  
  
\* **<span style="color:red">/moveto</span> <span style="color:blue">loc Y X \[Z\]</span>**

-   -   moves to the specified location
    -   **z is optional**
    -   **must be the first parameter**

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">yloc Y \| xloc X</span>**

-   -   beeline to the Y or X supplied
    -   different from precisey/x in that this only considers a single axis
    -   **must be the first parameter**

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">id \[#\]</span>**

-   -   moves to the supplied spawn id, or your current target if no id is given

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">off</span>**

-   -   stop moving to the current target/location

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">loose</span>**

-   -   moveto using more human-like heading adjustments

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">truehead</span>**

-   -   moveto using actual keypress heading adjustments

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">(id \| loc Y X \[Z\]) precisey \| precisex</span>**

-   -   moves to loc stopping when within x or y arrival dist values instead of both
    -   works with either id or loc

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">uw \| underwater</span>**

-   -   look angle up and down at destination

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">dist #</span>**

-   -   sets value for how close to actual location is considered arrival
    -   **does not turn moveto on**
    -   **permanently changes the value**

  
\* **<span style="color:red">/moveto</span> <span style="color:blue">\[id *spawnid* \| loc y x \[z\]\] mdist #
\[id\]</span>**

-   -   sets value for how close to actual location is considered arrival
    -   allowed inline **BEFORE** *id* or **AFTER** *loc y x \[z\]* or *id \[spawn id\]* parameter
    -   **permanently changes the value**

  
''the following inline configuration options are supported for one-time use:

-   **<span style="color:red">/moveto</span> <span style="color:blue">breakonaggro \| breakonhit \| usewalk \| useback
    \| backupdist # \| ydist # \| xdist #</span>**
    -   Read the *set **name***section for explanation of what these parameters do

  
  

### /circle

*The circle command spins you in a circle. If you are like me, looking at this for the first time wondering what the
point is, this is mainly for bards to use while circle kiting, but could equally be used for amusement. You can combine
any number of these parameters together inline to enable multiple options for the circle.*  
  
\* **<span style="color:red">/circle</span> <span style="color:blue">on \[ # \]</span>**

-   -   begin circling using your current location as the center with default radius
    -   if optional # parameter supplied, use # as the radius size
    -   **must be first parameter**

  
\* **<span style="color:red">/circle</span> <span style="color:blue">off</span>**

-   -   stop circling

  
\* **<span style="color:red">/circle</span> <span style="color:blue">loc Y X</span>**

-   -   begin circling using the specified location as the center
    -   **must be first parameter**

  
\* **<span style="color:red">/circle</span> <span style="color:blue">drunken</span>**

-   -   turn to complete the circle at random intervals

  
\* **<span style="color:red">/circle</span> <span style="color:blue">clockwise \| cw</span>**

-   -   circle in a clockwise direction. (default)

  
\* **<span style="color:red">/circle</span> <span style="color:blue">cw \| counterclockwise \| reverse</span>**

-   -   circle in a counter-clockwise direction

  
\* **<span style="color:red">/circle</span> <span style="color:blue">radius #</span>**

-   -   sets the default size of the circle radius
    -   for use with loc y x since *on #* would have to be first param

  
\* **<span style="color:red">/circle</span> <span style="color:blue">backward</span>**

-   -   run backwards instead of forwards

  
  
=== /makecamp === *The makecamp command will create a camp spot for you to return to after combat, or to establish
boundries for your character to prevent them from moving beyond a certain radius.*  
  
\* **<span style="color:red">/makecamp</span>**

-   -   using makecamp with no parameters will set up a camp at your current location, using default values

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">on \[ # \]</span>**

-   -   set up a camp at current location with default values
    -   if optional # parameter supplied, use # as camp radius size
    -   **must be first parameter**

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">off</span>**

-   -   disable current makecamp

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">loc Y X</span>**

-   -   set up a camp at the specified location
    -   **must be first parameter**

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">player \[ name \]</span>**

-   -   set up a dynamic camp based on a certain pc name if in zone, or targeted pc if optional name not supplied

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">leash</span>**

-   -   toggles leashing to camp radius so character cannot leave boundary

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">leash #</span>**

-   -   sets how far beyond camp radius you can move before leashing (LeashLength)

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">radius #</span>**

-   -   sets the radius of the camp size
    -   **does not turn camp on if supplied on its own**

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">mindelay # \| maxdelay #</span>**

-   -   sets the delay time before auto-returning to camp

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">return</span>**

-   -   forces a return to the camp radius immediately

  
\* **<span style="color:red">/makecamp</span> <span style="color:blue">altreturn</span>**

-   -   forces a return to the camp spot you had before your current one, or a camp that is now turned off

  
''the following inline configuration options are supported for one-time use:

-   **<span style="color:red">/makecamp</span> <span style="color:blue">returnhavetarget \| returnnoaggro \|
    returnnotlooting \| realtimeplayer \| scatter \| bearing # \| scatsize # \| scatdist #</span>**
    -   Read the *set **name***section for explanation of what these parameters do

  
  
=== Other Plugin Commands === *Less popular commands of MQ2MoveUtils*  
\* '''<span style="color:red">/calcangle</span>

-   -   Displays lots of basic numerical information related to moving such as Dist values, angular distance, 3D
        distance, melee range, stick range, speed multipliers
    -   This command is useful to help determine what to set plugin options such as arc values or AllowMove, backup
        dist, etc.

  
\* **<span style="color:red">/rootme</span> <span style="color:blue">\[ off \]</span>**

-   -   roots the player in place, unable to move. this is not any form of actual debuff, just a plugin implementation
        of locking a character in place
    -   supplying the optional *off* parameter disables the root
    -   **other commands will not function when rootme is active**

  
  
== Top-Level Objects ==

### ${MoveUtils}

*Members of this datatype relate to plugin settings and generic information*

|                                        |                   |                                        |                                                                                                                              |
|----------------------------------------|-------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Type**                               | **Member**        | **Return Values**                      | **Description**                                                                                                              |
| *[string](../data-types/datatype-string.md)* | **Command**       | NONE STICK MOVETO MAKECAMP CIRCLE      | Displays the currently active command. MAKECAMP returns if a camp is setup but no other command is currently in use          |
| *[bool](../data-types/datatype-bool.md)*     | **Stuck**         | TRUE FALSE                             | Displays true if plugin stucklogic has determined you are currently stuck                                                    |
| *[bool](../data-types/datatype-bool.md)*     | **Summoned**      | TRUE FALSE                             | Displays true if BreakOnSummon is enabled and has fired due to your character being summoned beyond breakonsummon distance   |
| *[bool](../data-types/datatype-bool.md)*     | **StuckLogic**    | TRUE FALSE                             | Displays true if stucklogic is enabled                                                                                       |
| *[bool](../data-types/datatype-bool.md)*     | **Verbosity**     | TRUE FALSE                             | Displays true if verbosity is enabled                                                                                        |
| *[bool](../data-types/datatype-bool.md)*     | **FullVerbosity** | TRUE FALSE                             | Displays true if fullverbosity is enabled                                                                                    |
| *[bool](../data-types/datatype-bool.md)*     | **TotalSilence**  | TRUE FALSE                             | Displays true if totalsilence is enabled                                                                                     |
| *[bool](../data-types/datatype-bool.md)*     | **Aggro**         | TRUE FALSE                             | Displays true if you are facing your target and your target is facing you                                                    |
| *[bool](../data-types/datatype-bool.md)*     | **TryToJump**     | TRUE FALSE                             | Displays true if stucklogic trytojump is enabled                                                                             |
| *[int](../data-types/datatype-int.md)*       | **PauseMinDelay** | 125 or greater                         | Displays the min delay for mousepause and mpause to resume command in ms                                                     |
| *[int](../data-types/datatype-int.md)*       | **PauseMaxDelay** | 125 or more greater than PauseMinDelay | Displays the max delay for mousepause and mpause to resume command in ms                                                     |
| *[int](../data-types/datatype-int.md)*       | **PulseCheck**    | 1 or greater                           | Displays the number of pulses used to average movement rate for stucklogic                                                   |
| *[int](../data-types/datatype-int.md)*       | **PulseUnstuck**  | 1 or greater                           | Displays the number of pulses successfully moved forward after being stuck to be considered unstuck                          |
| *[float](../data-types/datatype-float.md)*   | **DistStuck**     | 0.01 or greater                        | Displays the amount of distance needed to have moved (compared against pulse average) or else considered stuck by stucklogic |
| *[float](../data-types/datatype-float.md)*   | **Version**       | #.####                                 | Displays the version number of the plugin                                                                                    |
| *[bool](../data-types/datatype-bool.md)*     | **MovePause**     | TRUE FALSE                             | Displays true if mpause (PauseKB) is enabled                                                                                 |
| *[bool](../data-types/datatype-bool.md)*     | **GM**            | TRUE FALSE                             | Displays true if BreakOnGM fired                                                                                             |
| *[string](../data-types/datatype-string.md)* | **To String**     | Same as **Command**                    | Same as **Command**                                                                                                          |

  
=== ${Stick} === *Members of this datatype relate to the '/stick' command*

|                                        |                     |                                                 |                                                                                                                            |
|----------------------------------------|---------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Type**                               | **Member**          | **Return Values**                               | **Description**                                                                                                            |
| *[string](../data-types/datatype-string.md)* | **Status**          | OFF PAUSED ON                                   | Displays ON if any form of stick is active                                                                                 |
| *[bool](../data-types/datatype-bool.md)*     | **Active**          | TRUE FALSE                                      | Displays true if any form of stick is active                                                                               |
| *[bool](../data-types/datatype-bool.md)*     | **Broken**          | TRUE FALSE                                      | Returns true if BreakOnHit event has halted stick prematurely                                                              |
| *[float](../data-types/datatype-float.md)*   | **Distance**        | #.##                                            | Current distance used by stick                                                                                             |
| *[bool](../data-types/datatype-bool.md)*     | **MoveBehind**      | TRUE FALSE                                      | Displays true if stick behind is active                                                                                    |
| *[bool](../data-types/datatype-bool.md)*     | **MoveBack**        | TRUE FALSE                                      | Displays true if moveback is active                                                                                        |
| *[bool](../data-types/datatype-bool.md)*     | **Loose**           | TRUE FALSE                                      | Displays true if loose sticking is enabled                                                                                 |
| *[bool](../data-types/datatype-bool.md)*     | **Paused**          | TRUE FALSE                                      | Displays true if plugin is paused                                                                                          |
| *[bool](../data-types/datatype-bool.md)*     | **Behind**          | TRUE FALSE                                      | Displays true if currently behind target (regardless of */stick behind*), false if outside of stick dist or not behind     |
| *[bool](../data-types/datatype-bool.md)*     | **Stopped**         | TRUE FALSE                                      | Displays true if stick is within stick distance                                                                            |
| *[bool](../data-types/datatype-bool.md)*     | **Pin**             | TRUE FALSE                                      | Displays true if stick pin is active                                                                                       |
| *[int](../data-types/datatype-int.md)*       | **StickTarget**     | SpawnID                                         | Returns spawnid of stick target if stick id/hold used, else spawnid of current target, 0 if no target and id/hold not used |
| *[string](../data-types/datatype-string.md)* | **StickTargetName** | NONE [DisplayedName](../data-types/datatype-spawn.md) | Returns DisplayedName of stick target if stick id/hold used, else current target or NONE if no target and hold/id not used |
| *[float](../data-types/datatype-float.md)*   | **DistMod**         | \[-\]#.##                                       | Current stickdist modifier                                                                                                 |
| *[float](../data-types/datatype-float.md)*   | **DistModPercent**  | #.##                                            | Current stickdist percent modifier                                                                                         |
| *[bool](../data-types/datatype-bool.md)*     | **Always**          | TRUE FALSE                                      | Returns true if */stick always* is active                                                                                  |
| *[string](../data-types/datatype-string.md)* | **To String**       | Same as **Status**                              | Same as **Status**                                                                                                         |

  
=== ${MoveTo} === *Members of this datatype relate to the '/moveto' command*

|                                        |                  |                   |                                                                                 |
|----------------------------------------|------------------|-------------------|---------------------------------------------------------------------------------|
| **Type**                               | **Member**       | **Return Values** | **Description**                                                                 |
| *[bool](../data-types/datatype-bool.md)*     | **Moving**       | TRUE FALSE        | Displays true if moveto or camp return is active                                |
| *[bool](../data-types/datatype-bool.md)*     | **Stopped**      | TRUE FALSE        | Displays true if the last moveto command completed successfully                 |
| *[bool](../data-types/datatype-bool.md)*     | **CampStopped**  | TRUE FALSE        | Displays true if within moveto distance of makecamp Y X location                |
| *[bool](../data-types/datatype-bool.md)*     | **UseWalk**      | TRUE FALSE        | Returns true if UseWalk is enabled                                              |
| *[float](../data-types/datatype-float.md)*   | **ArrivalDist**  | 1.00+             | Acceptable arrival distance                                                     |
| *[float](../data-types/datatype-float.md)*   | **ArrivalDistY** | 1.00+             | Acceptable arrival distance for precisey                                        |
| *[float](../data-types/datatype-float.md)*   | **ArrivalDistX** | 1.00+             | Acceptable arrival distance for precisex                                        |
| *[bool](../data-types/datatype-bool.md)*     | **Broken**       | TRUE FALSE        | Returns true if BreakOnAggro or BreakOnHit event have halted moveto prematurely |
| *[string](../data-types/datatype-string.md)* | **To String**    | OFF PAUSED ON     | Displays ON if a moveto command is active                                       |

  
=== ${MakeCamp} === *Members of this datatype relate to the '/makecamp' command*

|                                        |                      |                                     |                                                                                                |
|----------------------------------------|----------------------|-------------------------------------|------------------------------------------------------------------------------------------------|
| **Type**                               | **Member**           | **Return Values**                   | **Description**                                                                                |
| *[string](../data-types/datatype-string.md)* | **Status**           | OFF PAUSED ON                       | Displays status of MakeCamp command. AltCamp returns OFF                                       |
| *[bool](../data-types/datatype-bool.md)*     | **Leash**            | TRUE FALSE                          | Displays true if leash is enabled                                                              |
| *[float](../data-types/datatype-float.md)*   | **AnchorX**          | 0.00                                | Location of current camp X anchor                                                              |
| *[float](../data-types/datatype-float.md)*   | **AnchorY**          | 0.00                                | Location of current camp Y anchor                                                              |
| *[float](../data-types/datatype-float.md)*   | **LeashLength**      | Greater than or equal to CampRadius | Size of Leash Length                                                                           |
| *[float](../data-types/datatype-float.md)*   | **CampRadius**       | 10.0+                               | Size of camp radius                                                                            |
| *[int](../data-types/datatype-int.md)*       | **MinDelay**         | 125 or greater                      | Displays the min delay for auto-returning to camp in ms                                        |
| *[int](../data-types/datatype-int.md)*       | **MaxDelay**         | 125 or more greater than MinDelay   | Displays the max delay for auto-returning to camp in ms                                        |
| *[bool](../data-types/datatype-bool.md)*     | **Returning**        | TRUE FALSE                          | Displays true if */makecamp return* issued                                                     |
| *[float](../data-types/datatype-float.md)*   | **AltAnchorX**       | 0.00                                | Location of current altcamp X anchor                                                           |
| *[float](../data-types/datatype-float.md)*   | **AltAnchorY**       | 0.00                                | Location of current altcamp Y anchor                                                           |
| *[float](../data-types/datatype-float.md)*   | **CampDist**         | 0.00                                | Distance to camp anchor from your current location. Returns 0.00 if camp is disabled           |
| *[float](../data-types/datatype-float.md)*   | **AltCampDist**      | 0.00                                | Distance to altcamp anchor from your current location. Returns 0.00 if altcamp not established |
| *[float](../data-types/datatype-float.md)*   | **AltRadius**        | 10.0+                               | Size of altcamp radius                                                                         |
| *[bool](../data-types/datatype-bool.md)*     | **Scatter**          | TRUE FALSE                          | Displays true if camp scattering enabled                                                       |
| *[bool](../data-types/datatype-bool.md)*     | **ReturnNoAggro**    | TRUE FALSE                          | Displays true if ReturnNoAggro is enabled                                                      |
| *[bool](../data-types/datatype-bool.md)*     | **ReturnNotLooting** | TRUE FALSE                          | Displays true if ReturnNotLooting is enabled                                                   |
| *[bool](../data-types/datatype-bool.md)*     | **ReturnHaveTarget** | TRUE FALSE                          | Displays true if ReturnHaveTarget is enabled                                                   |
| *[float](../data-types/datatype-float.md)*   | **Bearing**          | 0.00                                | Bearing (heading) of camp scattering                                                           |
| *[float](../data-types/datatype-float.md)*   | **ScatDist**         | 1.0+                                | Distance from anchor to perform scatter                                                        |
| *[float](../data-types/datatype-float.md)*   | **ScatSize**         | 1.0+                                | Size of scattering radius                                                                      |
| *[string](../data-types/datatype-string.md)* | **To String**        | Same as **Status**                  | Same as **Status**                                                                             |

  
=== ${Circle} === *Members of this datatype relate to the '/circle' command*

|                                        |               |                    |                                               |
|----------------------------------------|---------------|--------------------|-----------------------------------------------|
| **Type**                               | **Member**    | **Return Values**  | **Description**                               |
| *[string](../data-types/datatype-string.md)* | **Status**    | OFF PAUSED ON      | Returns ON if circling                        |
| *[float](../data-types/datatype-float.md)*   | **CircleY**   | 0.00               | Location of circle center Y                   |
| *[float](../data-types/datatype-float.md)*   | **CircleX**   | 0.00               | Location of circle center X                   |
| *[bool](../data-types/datatype-bool.md)*     | **Drunken**   | TRUE FALSE         | Displays true if drunken                      |
| *[string](../data-types/datatype-string.md)* | **Rotation**  | CW CCW             | Displays CCW if reverse circling              |
| *[string](../data-types/datatype-string.md)* | **Direction** | FORWARDS BACKWARDS | Movement direction of current circle          |
| *[bool](../data-types/datatype-bool.md)*     | **Clockwise** | TRUE FALSE         | Displays false if reverse circling            |
| *[bool](../data-types/datatype-bool.md)*     | **Backwards** | TRUE FALSE         | Displays true if movement direction backwards |
| *[float](../data-types/datatype-float.md)*   | **Radius**    | 5.00+              | Radius size of circle                         |
| *[string](../data-types/datatype-string.md)* | **To String** | Same as **Status** | Same as **Status**                            |

  
  
== Configuration == *MQ2MoveUtils saves a configuration file to your root MQ2 folder: MQ2MoveUtils.ini*

### Default INI File

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

  
  

### INI options

Information on what the actual values can be and represent.

#### \[Defaults\]

This section is for default plugin settings

-   *AllowMove* - 10.0+, anti-orbit setting for true/loose heading representing angular distance before moving forward
-   *AutoPause=* - on or off, pauses command if casting spells, stunned, rooted, sitting, or self targeted
-   *AutoPauseMsg=* - on or off, displays output when AutoPause halts movement
-   *AutoSave=* - on or off, automatically save ini file when using 'toggle' or 'set'
-   *AutoUW=* - on or off, automatically use 'uw' heading adjustments when character is under water
-   *BreakKeyboard=* - on or off, break command from keyboard press
-   *BreakMouse=* - on or off, break command from mouselook usage
-   *BreakOnGM=* - on or off, break current command and prevent command usage if GM enters zone
-   *BreakOnSummon=* - on or off, halt command and ability to use commands if summoned beyond certain distance
-   *DistSummon=* - 2.0+, distance moved in a single pulse to trigger breakonsummon (if on)
-   *FeignSupport=* - on or off, fd support waits for you to stand up manually before moving, if feigned
-   *Heading=* = true or loose or fast, type of heading adjustments plugin will use (fast=instant, loose=gradual
    emulated shift, true=real kb presses)
-   *HideHelp=* - on or off, never automatically display help output unless requested
-   *KeyboardPause=* - on or off, pause command for a delay if keyboard press
-   *MousePause=* - on or off, pause command for a delay if mouselook used
-   *LockPause=* - on or off, plugin will not automatically unpause under any circumstance unless user unpauses
-   *PauseMinDelay=* - 125+ (in ms), minimum delay before resuming from mpause/mousepause
-   *PauseMaxDelay=* - 125 above min (in ms), maximum delay before resuming from mpause/mousepause
-   *SaveByChar=* - on or off, save \[server.Charname\] section of ini file for individual character settings
-   *TurnRate=* - 10.0 to 100.0, rate at which loose heading emulates turns
-   *UseWindow=* - on or off, uses a custom user-placed window for all moveutils output if enabled
-   *Verbosity=* - on or off, ChatWnd output for basic command info
-   *FullVerbosity=* - on or off, ChatWnd output for enhanced plugin info
-   *TotalSilence=* - on or off **overrides verb/fullverb**, silence ChatWnd output except for critical or
    user-requested messages
-   *VerbosityFlags=* - see verbosity section of this wiki
-   *WinEQ=* - on or off, when enabled moveutils uses feigned movement simulation due to the bug of WinEQ2 holding down
    alt keys and mouse buttons in background sessions

**note: if WinEQ is enabled, true heading is NOT possible**  
==== \[Stick\] ==== This section is for settings related to */stick*

-   *AlwaysUW=* - on or off, if enabled stick will always use the 'uw' parameter as if it were typed inline
-   *AwareNotAggro=* - on or off, detect aggro loss if using stick front
-   *ArcBehind=* - 5.1 to 259.9, user can configure angular distance arc that "stick behind" uses
-   *ArcNotFront=* - 5.1 to 259.9, user can configure angular distance arc that "stick !front" uses
-   *BreakOnGate=* - on or off, break from stick if "target Gates." message occurs
-   *BreakOnHit=* - on or off, when enabled stick will halt if user is being attacked
-   *BreakOnWarp=* - on or off, break from stick if target warps beyond certain distance
-   *PauseOnWarp=* - on or off, pause stick unless target gets back in range if warps beyond certain distance (break or
    pause, can't have both)
-   *DelayStrafe=* - on or off, delay strafing movement when position adjustment required (good for stopping endless
    circling if aggro is gained)
-   *DistBackup=* - 1.0+, if you are within this distance when stick turned on, stick will walk backwards rather than
    spin in a circle to move to target
-   *DistBreak=* - 1.0+, distance mob moved in a single pulse to trigger breakonwarp (if on)
-   *DistMod=* - 0.0+, adjust default/supplied stick distance by this amount
-   *DistMod%=* - 0.0+ (represents a percentage), adjust default/supplied stick distance by this percent
-   *DistSnaproll=* - 1.0+, distance behind target snaproll will move before stopping and turning to face target
-   *RandomArc=* - on or off, randomize min/max arc for any strafe-based stick (so you do not always stick to the exact
    same spot of a mob)
-   *StrafeMinDelay=* - 125+ (in ms), minimum delay before attempting to strafe if delaystrafe enabled
-   *StrafeMaxDelay=* - 125 above min (in ms), maximum delay before attempting to strafe if delaystrafe enabled
-   *UseBackward=* - on or off, when enabled stick will walk backward rather than turn to face if within DistBackup of
    target
-   *UseFleeing=* - on or off, when enabled "stick front" will not attempt to position in front of the mob when target
    begins to flee
-   *UseWalk=* - on or off, when enabled stick uses walking when close to the target for precise movements and
    preventing overshooting

  
==== \[MakeCamp\] ==== This section is for settings related to */makecamp*

-   *CampRadius=* - 5.0+, default camp radius size
-   *MinDelay=* - 125+ (in ms), minimum delay before auto-returning to camp
-   *MaxDelay=* - 125 above min (in ms), maximum delay before auto-returning to camp
-   *RealtimePlayer=* - on or off, when enabled "makecamp player" gets realtime location updates of player and adjusts
    returning on the fly
-   *ReturnHaveTarget=* - on or off, if on Auto-Return to camp even if you have a target (default behavior is return
    only if no target)
-   *ReturnNoAggro=* - on or off, Auto-Return to camp only if not aggro
-   *ReturnNotLooting=* - on or off, do not Auto-Return to camp if looting a corpse
-   *UseLeash=* - on or off, do not allow character to move beyond LeashLength
-   *LeashLength=* - #.# >= camp radius, length of leash
-   *UseScatter=* - on or off, use specific scatter values instead of random return location
-   *Bearing=* - #, bearing of scatter
-   *ScatDist=* - 1.0+, distance from camp center to perform scatter
-   *ScatSize=* - 1.0+, radius size of scatter area

  
==== \[MoveTo\] ==== This section is for settings related to */moveto*

-   *AlwaysUW=* - on or off, if enabled moveto will always use the 'uw' parameter as if it were typed inline
-   *ArrivalDist=* - 1.0+, distance considered acceptable to have arrived at destination
-   *ArrivalDistX=* - 1.0+, distance considered acceptable to have arrived at destination when using precisex
-   *ArrivalDistY=* - 1.0+, distance considered acceptable to have arrived at destination when using precisey
-   *BreakOnAggro=* - on or off, when enabled moveto will halt if aggro is gained (crossed swords in player window)
-   *BreakOnHit=* - on or off, when enabled moveto will halt if user is being attacked
-   *DistBackup=* - 1.0+, moveto will walk backwards to location if within this distance rather than spin to face
    destination first
-   *MoveToMod=* - 0.0+, modifier applied to moveto arrivaldist
-   *UseBackward=* - on or off, when enabled moveto will use backward movement if within DistBackup (applies to makecamp
    returns)
-   *UseWalk=* - on or off, turn on walk when close to moveto location and camp return spot for precise movement

  
==== \[Circle\] ==== This section is for settings related to */circle*

-   *Backward=* - on or off, always run backwards instead of forwards when circling
-   *CCW=* - on or off, always run in a ccw circle instead of default clockwise
-   *Drunken=* - on or off, always use drunken circling
-   *RadiusSize=* - 5.0+, default radius size of circle

  
==== \[StuckLogic\] ==== This section is for settings related to stucklogic

-   *StuckLogic=* - on or off, if enabled stucklogic detects and attempts to auto-correct getting stuck while moving
-   *DistStuck=* - 0.01+, distance needed to have moved or else stuck (compared against an average)
-   *PulseCheck=* - 1+, amount of pulses used to calculate moving average
-   *PulseUnstuck=* - 1+, number of pulses successfully moved forward to be considered unstuck
-   *TryToJump=* - on or off, attempt to jump to help get unstuck
-   *TurnHalf=* - on or off, if have turned halfway and failed to get unstuck, reset heading and try other direction
    instead

  
==== \[Window\] ====

-   *ChatTop=* - See EQ XML UI file settings
-   *ChatBottom=* - See EQ XML UI file settings
-   *ChatLeft=* - See EQ XML UI file settings
-   *ChatRight=* - See EQ XML UI file settings
-   *Fades=* - See EQ XML UI file settings
-   *Alpha=* - See EQ XML UI file settings
-   *FadeToAlpha=* - See EQ XML UI file settings
-   *Duration=* - See EQ XML UI file settings
-   *Locked=* - See EQ XML UI file settings
-   *Delay=* - See EQ XML UI file settings
-   *BGType=* - See EQ XML UI file settings
-   *BGTint.red=* - See EQ XML UI file settings
-   *BGTint.green=* - See EQ XML UI file settings
-   *BGTint.blue=* - See EQ XML UI file settings
-   *FontSize=* - 1 to 10, default font size for window
-   *WindowTitle=* - custom user title for the window

  
==== \[yourserver.yourcharacter\] ==== if savebychar is on, this section will be created for every character The
settings in this section are some of the above values that could be desired to vary on a char-by-char basis (including
WINDOW settings) with the exception of one value:

-   *DisregardMe=* true or false, if you want custom character values to load for some characters but this specific
    character to use the default values instead, set this to true and though a lot of entries will be written to this
    section, they will be ignored for this specific character

  
  
=== Verbosity === The verbosity system has been revamped to use bit flags for superior control of what messages will be
displayed by the plugin. The older system has not been removed - if this is difficult to understand you may still use
*verbosity*, *fullverbosity* and *totalsilence* as before. For those familiar with bit flags the flags table is below.
If you have never worked with bit flags before, here is a brief summary of how to use the information below. Each subset
of messages is assigned a numerical value. By adding the numerical values of the messages you want on together, you are
able to customize each message that is shown or not shown. Examples:

-   If you only wanted the plugin to display 'settings' and 'errors', you would look at the value of settings in the
    table below (8192) and the value of errors (4194304) and add them together to get (4202496). By setting your
    verbosity flag to 4202496 (using the *set verbflags* parameter or by saving the value in the INI file) the plugin
    would then filter out everything except messages related to changing settings or error messages.
-   If you only wanted to display 'stick verbosity' messages and nothing else, you would look up the value in the table
    below (32) and set your flags to 32 without adding anything to it.
-   If you want to display a large number of messages, you continue to add them all together and use the total. To
    display 'autopause', 'movepause', 'stick verbosity', 'stick fullverbosity', 'settings' and 'errors', you would add
    all their values from the below table (1 + 2 + 32 + 64 + 8192 + 4194304 = 4202595) and use that number for your
    flags setting (/stick set verbflags 4202595)

#### Flags Table

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

#### Actual Messages

Here is a list of exactly what messages are tied to each flag:

-   1 - autopause
      
    *AutoPause halting movement...* (when autopaused if autopause is enabled)

    *Movement pausing due to self target...* (if self targeted during a stick with autopause off)
-   2 - movepause, mousepause, breakonkb
      
    *Current command ended from manual movement.*

    *Resuming previous command from movement pause.*
-   4 - breakonmouse
      
    *Current command ended from mouse movement.*
-   8 - feign support
      
    *Not standing as you are currently Feign Death*
-   16 - hidehelp
      
    Hidehelp when turned on prevents the help output (seen in /stick help) from being automatically output if you input
    a command incorrectly
-   32 - stick verbosity
      
    *You are now sticking to TargetName.*

    *You are no longer sticking to anything.*

    *You will now stick to every valid NPC target supplied.*
-   64 - stick full verbosity
      
    Dir(ANY) Dist(10.0) Head(true) ID(31337) UW MB HEALER
-   128 - moveto verbosity
      
    *Moveto off.*

    *Arrived at moveto location*
-   256 - moveto full verbosity
      
    *Moving to loc #, # Dist(10) Head(true)*
-   512 - makecamp verbosity
      
    *MakeCamp actived. Y(#) X(#) Radius(#) Leash(#) LeashLen(#) Min(#) Max(#)*

    *MakeCamp returning to within camp radius immediately*

    *MakeCamp returning to altcamp immediately.*

    *MakeCamp returning to altcamp immediately. Current camp now OFF.*

    *MakeCamp player ended due to player leaving/death*

    *Outside of leash length, breaking from current command*
-   1024 - makecamp full verbosity
      
    *Ended '/moveto' or '/makecamp return' because leash is on.*
-   2048 - circle verbosity
      
    *Circling radius (#), center (#, #) OFF*
-   4096 - circle full verbosity
      
    **none at this time**
-   8192 - settings
      
    *Stick modifier changed to Mod(#) Mod%(# %)* (from /stick mod #)

    *Stick mod changed Mod(#) ModPercent(# %)* (from stick inline -# or #%)

    *Moveto distance mod changed to #.* (from /moveto dist #)

    *Option turned ON* (from /command set option on, or /command toggle option)

    *Option turned OFF* (from /command set option off, or /command toggle option)

    *Option set to #* (from /command set option #)
-   16384 - file input / output
      
    *Debug file created.*

    *Saved settings to C:\\yourpath\\MQ2MoveUtils.ini* (from /command save)

    *Loaded settings from C:\\yourpath\\MQ2MoveUtils.ini* (from /command load)
-   32768 - breakonwarp
      
    *Stick pausing until target back in BreakDist range...*

    *Stick ending from target warping out of BreakDist range.*
-   65536 - breakonaggro
      
    BreakOnAggro's: *Aggro gained during /moveto, Halting command...*
-   131072 - breakonhit
      
    BreakOnHit's: *Aggro gained during /moveto, Halting command...*
-   262144 - breakonsummon
      
    *WARNING Command ended from character summoned # distance in a pulse.*

    *WARNING Verify you are not being monitored and type /stick imsafe to allow command usage.*
-   524288 - breakongm
      
    *WARNING Plugin halted from \[GM\] Name in zone.*

    *\[GM\] Name has left the zone or turned invisible. Use /stick imsafe to allow command usage.*
-   1048576 - breakongate
      
    *Mob gating ended previous command.*
-   2097152 - stick always
      
    *Stick awaiting next valid NPC target...*
-   4194304 - error messages
      
    *(ERROR) /moveto or /circle command used with no parameter.*

    *(ERROR) Plugin was already paused.*

    *(ERROR) Plugin was not paused.*

    *(ERROR) /stick mod \[#\] supplied incorrectly.*

    *(ERROR) /moveto yloc \[Y\] was supplied incorrectly.*

    *(ERROR) /moveto xloc \[X\] was supplied incorrectly.*

    *(ERROR) SpawnID must be a positive numerical value.*

    *(ERROR) You cannot use yourself or your mount.*

    *(ERROR) You cannot stick hold to yourself.*

    *(ERROR) Incorrectly used /moveto dist \[#\]*

    *(ERROR) /makecamp \[radius <dist>\] was supplied incorrectly.*

    *(ERROR) You do not have an active camp.*

    *(ERROR) You cannot use this command with a player-camp active.*

    *(ERROR) You cannot use this command until you've established an altcamp location.*

    *(ERROR) Invalid player name and do not have a valid player target.*

    *(ERROR) You cannot makecamp yourself.*

    *(ERROR) Use /circle radius \[#\] to set radius.*

    *ERROR: Invalid 'option set' syntax ( option ) \[on\|off\|number\]*

    *ERROR: Not a valid command toggle ( option ).*

    *ERROR: Not a valid command set option ( option ).*

    *Error - Font must be between 1 and 10.*

    *ERROR: Invalid 'command set' parameter ( option )*

    *(ERROR) You cannot stick to yourself!*

    *You must specify something to stick to!*

    *(ERROR) /moveto loc \[ <Y> <X> \[z\] \] was supplied incorrectly.*

    *(ERROR) /makecamp loc \[ <Y> <X> \] was supplied incorrectly.*

    *(ERROR) Usage /circle loc \[ <Y> <X> \] \[other options\]*

    *(ERROR) Invalid SpawnID and do not have a valid target.*

    *(ERROR) /makecamp \[mindelay\|maxdelay\] \[#\] was supplied incorrectly.*
-   8388608 - arc randomization
      
    *Arcs Randomized! Max: # Min: #*
-   16777216 - pause / unpause
      
    *PAUSED* (from /command pause)

    *RESUMED* (from /command unpause)

## See Also

-   [MQ2MoveUtils Revision History](../history/mq2moveutils-v11-revisions.md)
-   [MQ2MoveUtils Older Versions](mq2moveutils.md)
-   [MQ2MoveUtils History](../history/mq2moveutils-history.md)
-   [MacroQuest2 Plugins](../documentation/macroquest2-plugins.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Data Types](../data-types/data-types.md)


