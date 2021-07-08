# MQ2Targets

## Introduction

MQ2Targets is a HUD Display-type spawn tracker with syntax similar to the [/where](../../commands/slash-commands/where.md) command. Created by DrunkDwarf.

### Links

* [**MQ2Targets**](https://macroquest2.com/phpBB3/viewtopic.php?t=12912) source and discussion.

### Features

* Search strings are saved per zone
* Replace "add" with "notify" and it will popup a message for each spawn matching your search string
* Can add as many search strings per zone as needed
* Each HUD spawn matching the search shows by default Name, Level, Class, Distance, an arrow showing relative

  direction, and a compass heading

* Use MQ2HUD-type syntax strings to determine HUD display elements to completely customize the HUD display for each

  spawn

* Default is 5 spawns show, can modify using "/watch count \#"
* HUD will highlight spawn if it's the current target
* Guild members highlighted in HUD
* HUD list sorted by distance ascending

## Commands

* **/watch add\|notify target**
  * Add the specified _target_ from the watch list. The syntax for _target_ is the same as that for the

    [/where](../../commands/slash-commands/where.md) command. Using _notify_ will add a pop-up for each spawn.

\* **/watch remove\|delete target\|\#**

* * Remove the specified _target_ or entry _\#_ in the list.

\* **/watch sound id \# soundfile.mp3**

* * Assign _soundfile.mp3_ to the id _\#_

\* **/watch sound \# target**

* * Assign the sound from id _\#_ to the _target_

\* **/watch sound list**

* * List sound associations

\* **/watch hud refresh\|**_**hudstring**_

* * Refresh or modify the string to be displayed in the HUD. The following additional indicators can be used in the

    _hudstring_:

    * **&clr** - this is replaced with "&gt;&gt;" to show the current target, and turns on guild/corpse colors
    * **&dst** - this is replaced with the distance to target plus +/- for Z-axis indication
    * **&arr** - this is replaced with an arrow indicating direction to mob

\* **/watch showtarget**

* * Toggle showing of the current target in the HUD.

\* **/watch speak**

* * Toggle use of speech \(see source page for additional instructions\)

\* **/watch show \#**

* * Change the number of entries to show in the HUD

\* **/watch x\|y \#**

* * Change the leftmost \(x\) or topmost \(y\) pixel position of the HUD display

\* **/watch increment \#**

* * Change the spacing between spawns in the HUD to \# pixels

\* **/watch togglechat**

* * Toggles whether to output to a separate MQ2Targets window or use the MQ2Chat window

\* **/watch toggleway target\|\#**

* * Toggle use of the waypoint indicator for current target or spawn in index \#

\* **/watch waypoint** **\[y\]**

* * Toggles waypoint overlay. Optional _y_ parameter sets the y pixel position on screen

\* **/watch loadmap**

* * Imports all labels from the current map file

\* **/watch showmap**

* * Show spawns loaded from current map file

\* **/watch help**

* * Displays help and examples

## Examples

**/watch add paladin pc range 65 70**  
Show all Player character paladins between level 65 and 70 in current zone

**/watch add guild**  
Show everyone in your guild in current zone

**/watch add damlin lingering npc**  
Show when damlin in CoA pops \(but not his corpse\)'''

**/watch remove damlin lingering npc**  
Remove damlin from HUD tracking

**/watch list**  
Lists the current targets being watched for in current zone

**/watch show 10**  
Change the HUD display to track the 10 nearest targets

**/watch x 200**  
Display the leftmost edge of the HUD list at screen x position 200

**/watch y 50**  
Display the topmost edge of the HUD list at screen y position 50 **/watch increment 20**  
Change the spacing between spawns in the HUD to 20 pixels

**/watch notify hanvar**  
Pop up message if Hanvar spawns/despawns

**/watch remove 2**  
Removes search spawn criteria string \#2 according to /watch list

**/watch hud ${Target.CleanName} ${Target.Level}${Target.Class.ShortName}\(${Target.HeadingTo}\)${Target.Distance}&arr**

Targets are displayed as follows:

**Cleric01 75CLR\(NNW\)30.23--&gt;**

**Hint:** It's probably easier to open MQ2Targets.ini and edit the HUDString key, similar to:

`HUDString=&clr${Target.CleanName}(${Target.Race}) ${Target.Level}${Target.Class.ShortName} ${Target.Distance}&arr(${Target.HeadingTo})`

## Known Issues

* The "color" /watch parameters do nothing at this time, still thinking about how I want to implement this

## Plans

* Add the /watch color functionality
* Make HUD list clickable?
* Add HUDString capability to the popup messages

## See Also

* [MQ2 Plugins](../../commands/slash-commands/plugin.md)

