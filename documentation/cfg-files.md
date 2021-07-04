## Introduction

CFG files are files which contain commands to be run at certain times. The file must contain commands the same as you
would use them normally. Each command will be executed in order, however there are NO macro blocks, events, etc, in a
CFG file.

CFG files may be present in .\\Configs, in .\\ (Release), or potentially in the EverQuest directory. Note that the
*Release* would be the same as wherever your Macroquest.ini is.

You can manually load a CFG file while in-game using the [/loadcfg](../commands/loadcfg.md) command.

**The following CFG files will be loaded at the following times:**

|                               |                                                                                        |
|-------------------------------|----------------------------------------------------------------------------------------|
| **autoexec.cfg**              | Executed on the first pulse (when you reach character select, or when you are in game) |
| **charselect.cfg**            | Executed when you reach character select                                               |
| **zoned.cfg**                 | Executed after you finish zoning, but right before the map-specific config is executed |
| ***server_character*.cfg**    | Executed when a certain character enters the world                                     |
| '**'classname.cfg**           | Executed when char of 'classname' enters world. e.g., bard.cfg                         |
| ***mapshortname*.cfg**        | Executed when you zone into this zone                                                  |
| ***pluginname*-autoexec.cfg** | Executed when this plugin is loaded (after its initialization is complete)             |

## Examples

-   Example use of **zoned.cfg**:  
    \* You have a macro that wants to summon a mount (or cast SoW, etc), but should only attempt this in outdoor zones.
    In **zoned.cfg**, set a global variable to automatically set the zone to outdoor. Modify your macro to attempt to
    summon a horse at some appropriate point and capture a failed summon via /doevents. Reset the value of the variable
    to indoor and it will hold until you zone again.
    -   The newbie zones on the Progression servers have 100s of corpses all over, creating a lot of lag.

<!-- -->

    /if (${SpawnCount[corpse]}>150) /hidecorpse all

-   Example of a CFG file entry for a specific character:

<!-- -->

    /custombind add lootcorpse
    /custombind set lootcorpse /multiline ; /target corpse radius 17; /loot
    /bind lootcorpse f

-   Example of a specific zone CFG:

This will fix UI Corruption in The Devastion zone due to a massive (800+) number of spawns on the map.  
**devastation.cfg**

    /maphide npc 49


