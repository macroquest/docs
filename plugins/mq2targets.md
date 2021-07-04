## Introduction

MQ2Targets is a HUD Display-type spawn tracker with syntax similar to the [/where](../commands/where.md) command. Created by
DrunkDwarf.

### Links

-   **[MQ2Targets](https://macroquest2.com/phpBB3/viewtopic.php?t=12912)** source and discussion.

### Features

-   Search strings are saved per zone
-   Replace "add" with "notify" and it will popup a message for each spawn matching your search string
-   Can add as many search strings per zone as needed
-   Each HUD spawn matching the search shows by default Name, Level, Class, Distance, an arrow showing relative
    direction, and a compass heading
-   Use MQ2HUD-type syntax strings to determine HUD display elements to completely customize the HUD display for each
    spawn
-   Default is 5 spawns show, can modify using "/watch count #"
-   HUD will highlight spawn if it's the current target
-   Guild members highlighted in HUD
-   HUD list sorted by distance ascending

## Commands

-   **<span style="color:red">/watch</span> <span style="color:blue">add\|notify target</span>**
    -   Add the specified *target* from the watch list. The syntax for *target* is the same as that for the
        [/where](../commands/where.md) command. Using *notify* will add a pop-up for each spawn.

  
\* **<span style="color:red">/watch</span> <span style="color:blue">remove\|delete target\|#</span>**

-   -   Remove the specified *target* or entry *#* in the list.

  
\* **<span style="color:red">/watch</span> <span style="color:blue">sound id # soundfile.mp3</span>**

-   -   Assign *soundfile.mp3* to the id *#*

  
\* **<span style="color:red">/watch</span> <span style="color:blue">sound # target</span>**

-   -   Assign the sound from id *#* to the *target*

  
\* **<span style="color:red">/watch</span> <span style="color:blue">sound list</span>**

-   -   List sound associations

  
\* **<span style="color:red">/watch</span> <span style="color:blue">hud refresh\|*hudstring*</span>**

-   -   Refresh or modify the string to be displayed in the HUD. The following additional indicators can be used in the
        *hudstring*:
        -   **&clr** - this is replaced with ">\>" to show the current target, and turns on guild/corpse colors
        -   **&dst** - this is replaced with the distance to target plus +/- for Z-axis indication
        -   **&arr** - this is replaced with an arrow indicating direction to mob

  
\* **<span style="color:red">/watch</span> <span style="color:blue">showtarget</span>**

-   -   Toggle showing of the current target in the HUD.

  
\* **<span style="color:red">/watch</span> <span style="color:blue">speak</span>**

-   -   Toggle use of speech (see source page for additional instructions)

  
\* **<span style="color:red">/watch</span> <span style="color:blue">show #</span>**

-   -   Change the number of entries to show in the HUD

  
\* **<span style="color:red">/watch</span> <span style="color:blue">x\|y #</span>**

-   -   Change the leftmost (x) or topmost (y) pixel position of the HUD display

  
\* **<span style="color:red">/watch</span> <span style="color:blue">increment #</span>**

-   -   Change the spacing between spawns in the HUD to # pixels

  
\* **<span style="color:red">/watch</span> <span style="color:blue">togglechat</span>**

-   -   Toggles whether to output to a separate MQ2Targets window or use the MQ2Chat window

  
\* **<span style="color:red">/watch</span> <span style="color:blue">toggleway target\|#</span>**

-   -   Toggle use of the waypoint indicator for current target or spawn in index #

  
\* **<span style="color:red">/watch</span> <span style="color:blue">waypoint \[y\]</span>**

-   -   Toggles waypoint overlay. Optional *y* parameter sets the y pixel position on screen

  
\* **<span style="color:red">/watch</span> <span style="color:blue">loadmap</span>**

-   -   Imports all labels from the current map file

  
\* **<span style="color:red">/watch</span> <span style="color:blue">showmap</span>**

-   -   Show spawns loaded from current map file

  
\* **<span style="color:red">/watch</span> <span style="color:blue">help</span>**

-   -   Displays help and examples

  

## Examples

**/watch add paladin pc range 65 70  
** Show all Player character paladins between level 65 and 70 in current zone

**/watch add guild  
** Show everyone in your guild in current zone

**/watch add damlin lingering npc  
** Show when damlin in CoA pops (but not his corpse)'''

**/watch remove damlin lingering npc  
** Remove damlin from HUD tracking

**/watch list  
** Lists the current targets being watched for in current zone

**/watch show 10  
** Change the HUD display to track the 10 nearest targets

**/watch x 200  
** Display the leftmost edge of the HUD list at screen x position 200

**/watch y 50  
** Display the topmost edge of the HUD list at screen y position 50 **/watch increment 20  
** Change the spacing between spawns in the HUD to 20 pixels

**/watch notify hanvar  
** Pop up message if Hanvar spawns/despawns

**/watch remove 2  
** Removes search spawn criteria string #2 according to /watch list

**/watch hud ${Target.CleanName} ${Target.Level}${Target.Class.ShortName}(${Target.HeadingTo})${Target.Distance}&arr**

Targets are displayed as follows:

**Cleric01 75CLR(NNW)30.23-->**

**Hint:** It's probably easier to open MQ2Targets.ini and edit the HUDString key, similar to:

`HUDString=&clr${Target.CleanName}(${Target.Race}) ${Target.Level}${Target.Class.ShortName} ${Target.Distance}&arr(${Target.HeadingTo})`

## Known Issues

-   The "color" /watch parameters do nothing at this time, still thinking about how I want to implement this

## Plans

-   Add the /watch color functionality
-   Make HUD list clickable?
-   Add HUDString capability to the popup messages

## See Also

-   [MQ2 Plugins](../commands/plugin.md)


