---
tags:
   - command
---
# Mapfilter

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/mapfilter <filter> [show|hide] [color <R# G# B#>] 
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
This controls what appears or does not appear on the in-game map. There's a nice GUI for these filters in [/mqsettings](../../../reference/commands/mqsettings.md).
<!--cmd-desc-end-->
## Options

* **`help`** will show all current settings.
* _**`<filter>`**_ can be one of the following,

| filter | description |
| :--- | :--- |
| **All** | Shows/hides all map items **that have already been set to "show".** |
| **Aura** | Show/hide auras. |
| **Banner** | Show/hide guild banner. |
| **Campfire** | Show/hide campfire. |
| **CampRadius #** | Sets radius of camp circle to #.
| **CastRadius #** | Show a cast radius circle around your own spawn on the map. Set to "hide" or "0" to disable. |
| **Chest** | Show/hide chests. |
| **Corpse** | Master toggle to show/hide all corpses (PC and NPC). |
| **Custom** _**searchfilter**_ | Set a custom filter, which can contain any filtering arguments from the [Spawn Search](../../../reference/general/spawn-search.md) page. Note: The use of custom is a one time event, it is not persistent. |
| **Group** | Whether group members should be listed in another color. |
| **Ground** | Show/hide ground spawns. |
| **Marker** _`<filter> <shape> [#]`_ | Change the marker shape for specified spawns. Passing a number at the end will change shape size. Accepted shapes: none/triangle/square/diamond. |
| **Mercenary** | Show/hide mercenaries. |
| **Menu** | Enable or disable the right-click context menu |
| **Mount** | Show/hide mounts. |
| **Named** | Displays only 'named' NPCs, other NPCs are filtered out (not perfect). |
| **NormalLabels** | Toggles normal EQ (non-MQ2) label display. |
| **NPC** | Show/hide all NPCs. |
| **NPCConColor** | Whether the dots on the map should be the same as the NPCs con colors. |
| **NPCCorpse** | Show/hide NPC corpses. |
| **Object** | Show/hide destructible objects (as were implemented in Prophecy of Ro expansion), like catapults, tents, practice dummies, etc. |
| **PC** | Show/hide all Player Characters. |
| **PCConColor** | Whether the dots on the map should be the same as the PCs con colors. |
| **PCCorpse** | Show/hide Player corpses. |
| **Pet** | Show/hide pets. |
| **PullRadius #** | Sets radius of casting circle to # (omit or set to 0 to disable) |
| **SpellRadius #** | Show another radius circle around your own spawn. Functions the same way as **CastRadius**. |
| **Target** | Show your target in a different color. |
| **TargetLine** | Draw a line between yourself and your target. |
| **TargetMelee** | Draw a melee range circle around your target. |
| **TargetPath** | Draws EQ path to selected target. |
| **TargetRadius #** | Draw a radius of # around your target. Using "hide" or "0" will disable the TargetRadius circle. |
| **Timer** | Show/hide timers. |
| **Trigger** | Show/hide trigger locations. |
| **Trap** | Show/hide traps. |
| **Untargettable** | Show/hide untargettable spawns. |
| **Vector** | Display heading vectors. |

* **`show|hide`** will toggle the filter between show and hide.
* **`color <R# G# B#>`** will set the color for the filter. Omit the R# G# B# values to reset.

## Examples

This will set a red **CastRadius** circle around your own spawn on the MQ2 map.

`/mapfilter castradius color 255 0 0`

This will display all NPCs between level 60 and 65 within a radius of 50

`/mapfilter custom npc range 60 65 radius 50`

This will display all NPCs within a radius of 1000

`/mapfilter custom npc radius 1000`

This command can also be used at larger ranges by entering a larger number.

To restore the settings saved in your ini and remove your custom filters use the command without any parameters.

`/mapfilter custom`

## Troubleshooting

??? question "My map is no different than normal and `/mapfilter all` had no effect, what did I do wrong?"

    The `/mapfilter all show` command only affects map items that have *already* been individually set to "show". It does not enable all filters simultaneously as might be expected. You need to enable each desired filter type individually first (e.g., `/mapfilter npc show`, `/mapfilter pc show`, etc.) before `/mapfilter all show` will display them.
