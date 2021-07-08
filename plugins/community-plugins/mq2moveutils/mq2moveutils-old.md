# MQ2MoveUtils \(old\)

## Description

**For updated plugin information see MQ2MoveUtils:v9.**  
The information below applies to the 7.0518 and earlier versions of MQ2MoveUtils.

MQ2MoveUtils is a very popular plugin which assists with most aspects of moving around within EQ. It has been worked on by a number of developers over the years \(tonio, CyberTech, Quagmire and Outlander\). For the history of this plugin and development notes please see [MQ2MoveUtils:History](mq2moveutils-history.md).

The old forum thread for MQ2MoveUtils can be found [here](https://macroquest2.com/phpBB3/viewtopic.php?t=11732), in the VIP forums. Source for the [version 7.0 MQ2MoveUtils](http://mq2.whyarewehappening.com/MQ2MoveUtils/archive/07.0518/) is available.

## Features

The main features of MQ2MoveUtils are as follows:

* **Stick:** This is the main use for this plugin and allows you to "stick" a certain distance from your target. It

  can be set to always stick behind the target, or always in front if you're tanking.

* **MoveTo:** Move to a certain point or target. This has some built-in logic that will allow it to move around

  obstacles.

* **MakeCamp:** You can set a spot as a "camp", so that you can return to it if you get too far away, or after combat,

  etc.

* **Circle:** Run in a circle.

## Commands

### /stick

* **/stick \[on\|off\]**

Turn stick on and off. The default for /stick is to stick at max melee range.

* **/stick \[hold\]**

Sticks to current target even if you lose/change target

* **/stick \[\]**

Stick at units to your target

* **/stick \[-\]**

Subtract the dist used from the current stick distance \(ie. it will put you units closer to your target\)

* **/stick \[%\]**

Stick at of max melee range from target. Eg. if max melee range is 20, then /stick 50% will stick you at 10 range

* **/stick \[behind\]**

Sticks you behind your target.

**\*Note:** Be careful with this option if you do not have the Health of Target's Target Leadership Ability. If you have HoTT active and you are the Target of your Target, then you will not try to get behind. However if you do not have this ability and you gain aggro, you will spin around very quickly as you try and get behind your target while it continues to face you.\*

* **/stick \[behindonce\]**

Get behind the target once then convert to a regular stick

* **/stick \[pin\]**

Sticks you to the side of the target, same considerations as /stick behind apply

* **/stick \[!front\]**

Sticks you anywhere but in front of the target, will only reposition you if you would be in front. Same considerations apply to this as the "behind" and "pin" options

* **/stick \[moveback\]**

Moveback will back your toon up to the current value, keeping you at a consistant distance from your target

* **/stick \[loose\]**

Uses a time delay so adjustments to your position do not occur as frequently, simulating a more human-like control

* **/stick \[uw\]**

This changes the facing of your toon, and is very useful under water, where you will try and follow the Z coordinate of the spawn you are facing

* **/stick \[id \]**

Allows you to stick to a specific spawn ID

* **/stick \[mpause\]**

By enabling mpause, manually moving your toon will not break stick and will rather put it on hold. When you are done manually moving, the /stick command will once again kick in and you will continue following the same target as before

* **/stick \[pause\|unpause\]**

Pause and unpause the stick command

* **/stick \[save\|load\]**

Some settings are stored in the INI file. This allows you to save your current preferences to the INI file, or load the saved preferences this file

* **/stick \[mindelay \]**

When used with /stick this delay is used when mpause is enabled to decide the smallest value to use to resume the /stick command after a manual move

* **/stick \[maxdelay \]**

When used with /stick this delay is used when mpause is enabled to decide the largest value to use to resume the /stick command after a manual move

### /moveto

* **/moveto \[loc Y X\|off\]**

Moves you to the specified location, or stops the current /moveto \(by using "/moveto off"\)

* **/moveto \[\]**

Sets the maximum distance from your moveto point that you consider acceptable. This option is here because it's not always possible to move to the **exact** point that you specify, so the plugin will move you to within units of the moveto point before stopping. Eg. if you use "/moveto 5", you will always move to within 5 units from your moveto point

* **/moveto \[-\]**

Subtract from the current moveto distance

* **/moveto \[mpause\]**

By enabling mpause, manually moving your toon will not break moveto and will rather put it on hold. When you are done manually moving, the /moveto command will once again kick in and you will continue moving to your moveto point

* **/moveto \[pause\|unpause\]**

Pause and unpause the moveto command

* **/moveto ID \[Spawn ID\]**

Moves to the specified Spawn ID or moves to your current target if no Spawn ID is provided

* **/moveto \[mindelay \]**

When used with /moveto this delay is used when mpause is enabled to decide the smallest value to use to resume the /moveto command after a manual move.

* **/moveto \[maxdelay \]**

When used with /moveto this delay is used when mpause is enabled to decide the largest value to use to resume the /moveto command after a manual move.

* **/moveto \[save\|load\]**

Save or load the moveto settings

### /makecamp

* **/makecamp \[on\|off\]**

Turns MakeCamp logic off or turns it on, using your current location as the anchor point

* **/makecamp \[ \]**

Turns MakeCamp logic on using the supplied Y,X location as the camp anchor point

* **/makecamp \[mindelay \]**

If outside the MakeCamp radius this is the minimum delay used before returning to a point within the camp radius

* **/makecamp \[maxdelay \]**

If outside the MakeCamp radius this is the maxium delay used before returning to a point within the camp radius

* **/makecamp \[leash\]**

Toggle the leash logic on and off. Leash is the maximum distance away from your camp anchor your toon will be allowed to go using another MQ2MoveUtils command such as /stick

* **/makecamp \[leash \]**

Turns leash logic ON and sets the leash length

* **/makecamp \[radius \]**

Sets the camp radius. This is the maximum distance you can be from the anchor point and still be considered "in camp"

* **/makecamp \[mpause\]**

By enabling mpause, manually moving your toon will not break makecamp and will rather put it on hold. When you are done manually moving, the /makecamp command will once again kick

* **/makecamp \[pause\|unpause\]**

Pause and unpause the MQ2MoveUtils makecamp functionality

* **/makecamp \[return\]**

Returns your toon to the camp immediatly

* **/makecamp \[save\|load\]**

Save or load the makecamp settings

### /circle

* **/circle \[on\|off\]**

Sets the anchor point to your current location, and uses the currently set radius

* **/circle \[on \]**

Sets the anchor point to your current location, and uses the specified

* **/circle \[ \]**

Sets Y,X anchor point around which to circle

* **/circle \[mpause\]**

By enabling mpause manually moving your toon will not break the circle but will instead put it on hold, when you get done manually moving the toon the /circle command will once again kick in.

* **/circle \[pause\|unpause\]**

Pause and unpause the /circle command

* **/circle \[drunken\]**

Does not move in a perfect circle but instead the circle is more human-like

* **/circle \[mindelay \]**

When used with /circle this delay is used when mpause is enabled to decide the smallest value to use to resume the /stick command after a manual move.

* **/circle \[maxdelay \]**

When used with /circle this delay is used when mpause is enabled to decide the largest value to use to resume the /stick command after a manual move.

* **/circle \[save\|load\]**

Save or load the circle settings from the INI file

## Top-Level Objects

### Stick

* [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) **${Stick}**

  _Same as ${Stick.Status} \(see below\)._

* [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) **${Stick.Status}**

  Return ON if currently sticking, OFF if not, or PAUSED if it is paused

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.Active}**

  Returns TRUE if currently sticking, FALSE if not

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.Behind}**

  Returns TRUE if behind target

* [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) **${Stick.Distance}**

  The current stick distance

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.Loose}**

  Returns TRUE if stick loose is set

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.MoveBack}**

  Returns TRUE if stick is set to moveback

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.MoveBehind}**

  Returns TRUE if stick is set to move behind the target

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.MovePause}**

  Returns TRUE if stick movement is paused due to manual intervention

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.Paused}**

  Returns TRUE if stick has been paused with "/stick pause"

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.Pin}**

  Returns TRUE if /stick pin is being used

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Stick.Stopped}**

  Returns TRUE if you are stationary

### MoveTo

* [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) **${MoveTo}**

  Return ON if currently moving to a location, OFF if not, or PAUSED if it is paused

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${MoveTo.Moving}**

  Returns TRUE if moving to location, FALSE if not

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${MoveTo.Stopped}**

  Returns TRUE if stopped, FALSE if not

### MakeCamp

* [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) **${MakeCamp}**

  _Same as ${MakeCamp.Status} \(see below\)._

* [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) **${MakeCamp.Status}**

  Return ON if MakeCamp is enabled, OFF if it is not enabled or PAUSED if it is paused

* [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) **${MakeCamp.AnchorX}**

  The X Loc of the anchor point

* [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) **${MakeCamp.AnchorY}**

  The Y Loc of the anchor point

* [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) **${MakeCamp.CampRadius}**

  The current camp radius

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${MakeCamp.Leash}**

  Returns TRUE if the leash is enabled, FALSE if not

* [_float_](../../../data-types-and-top-level-objects/data-types/datatype-float.md) **${MakeCamp.LeashLength}**

  The length of the leash

* [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) **${MakeCamp.MaxDelay}**

  The maximum delay before resuming /makecamp functionality after manual intervention

* [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) **${MakeCamp.MinDelay}**

  The minimum delay before resuming /makecamp functionality after manual intervention

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${MakeCamp.Returning}**

  Returns TRUE if returning to camp, FALSE if not

## INI File

A default INI file is created \(if it doesn't exist\) when you issue one of the "save" commands \(eg. /stick save, /moveto save, etc\).

The \[Defaults\] section contains global defaults for all users. New sections can be added with character names as titles to override the default values. An example INI file is below, with explanations of the options underneath:

`[Defaults]`  
`AutoPause=on`  
`BreakOnWarp=on`  
`BreakDist=250.0`  
`BreakOnGate=on`  
`Verbosity=1`  
`ManualPause=on`  
`MinDelay=500`  
`MaxDelay=5000`  
`CampRadius=0.0`  
`LeashLength=0.0`  
`StuckLogic=on`  
`stuckCheck=5`  
`stuckDist=0.1`

* **AutoPause \[on/off\]**

This enables or disables the automatic pause on cast feature. This does not apply to bards, since they can move while singing.

* **BreakOnWarp \[on/off\]**

With _BreakOnWarp_ on, any movement will be terminated if the target moves too far away. See _BreakDist_ to set the distance.

* **BreakDist**

This sets how far away the target has to be before it will be considered too far away to continue following.

* **BreakOnGate \[on/off\]**

This enables/disables monitoring chat for "_TargetName_ Gates". Movement will be terminated if it determines that the target has gated.

* **ManualPause \[on/off\]**

Stores your preference for the mPause functionality built into the various commands.

* **MinDelay** and **MaxDelay**

Stores your preference for the resuming after manual move. These values are also used to return to camp at the end of a /stick or /moveto command when using /makecamp.

* **CampRadius**

This is the default value used for /makecamp radius.

* **LeashLength**

This is the default value used for /makecamp leash length

* **StuckLogic \[on/off\]**

Enable or disable the logic used to determine if you are stuck behind an object when using /stick or /moveto.

* **stickCheck**

The number of pulses that are averaged out to come up with the _stuckDist_ comparison number.

* **stuckDist**

This is the average distance covered during the the last _stickCheck_ pulses to use as a comparison. Eg. if you normally would average .5 distance units covered in a 5 pulse period, then if your average drops down to .1 moved in the last 5 pulses then you are probably stuck and the stuck logic should kick in.

## Troubleshooting

* You can see a list of options for each of the commands by typing the command and then "help". Eg. /stick help,

  /moveto help, etc.

## See Also

* [MQ2MoveUtils:History](mq2moveutils-history.md)
* MQ2MoveUtils:v9
* [Plugins](../../../documentation/macroquest2-plugins.md)
* [Top-Level Objects](../../../data-types-and-top-level-objects/top-level-objects/)

