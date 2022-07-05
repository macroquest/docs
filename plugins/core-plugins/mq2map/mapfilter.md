---
tags:
   - plugin
---
# Mapfilter

## Syntax

**/mapfilter help\|**_**option**_ **\[show\|hide\] \[color R\# G\# B\#\]**

## Description

This controls what appears or does not appear on the in-game map provided by [MQ2Map](./).

* **Help** will show all current settings.
* _**Option**_ can be one of the following followed by "show" or "hide". If no show/hide argument is given, it will

  toggle the setting between show and hide.

|  |  |
| :--- | :--- |
| **All** | Shows/hides all map items **that have already been set to "show".** |
| **Aura** | Show/hide auras. |
| **Banner** | Show/hide guild banner. |
| **Campfire** | Show/hide campfire. |
| **CastRadius \#** | Show a cast radius circle around your own spawn on the map. Set to "hide" or "0" to disable. |
| **Chest** | Show/hide chests. |
| **Corpse** | Master toggle to show/hide all corpses \(PC and NPC\). |
| **Custom** _**searchfilter**_ | Set a custom filter, which can contain any filtering arguments from the [Spawn Search](../../../reference/general/spawn-search.md) page. |
| **Group** | Whether group members should be listed in another color. |
| **Ground** | Show/hide ground spawns. |
| **Merceneary** | Show/hide mercenaries. |
| **Menu** | Enable or disable the right-click context menu |
| **Mount** | Show/hide mounts. |
| **Named** | Displays only 'named' NPCs, other NPCs are filtered out \(not perfect\). |
| **NormalLabels** | Toggles normal EQ \(non-MQ2\) label display. |
| **NPC** | Show/hide all NPCs. |
| **NPCConColor** | Whether the dots on the map should be the same as the NPCs con colors. |
| **NPCCorpse** | Show/hide NPC corpses. |
| **Object** | Show/hide destructible objects \(as were implemented in Prophecy of Ro expansion\), like catapults, tents, practice dummies, etc. |
| **PC** | Show/hide all Player Characters. |
| **PCConColor** | Whether the dots on the map should be the same as the PCs con colors. |
| **PCCorpse** | Show/hide Player corpses. |
| **Pet** | Show/hide pets. |
| **SpellRadius \#** | Show another radius circle around your own spawn. Functions the same way as **CastRadius**. |
| **Target** | Show your target in a different color. |
| **TargetLine** | Draw a line between yourself and your target. |
| **TargetMelee** | Draw a melee range circle around your target. |
| **TargetRadius \#** | Draw a radius of \# around your target. Using "hide" or "0" will disable the TargetRadius circle. |
| **Timer** | Show/hide timers. |
| **Trigger** | Show/hide trigger locations. |
| **Trap** | Show/hide traps. |
| **Vector** | Display heading vectors. |
| **Untargettable** | Show/hide untargettable spawns. |

* Any of the above options can have "color R\# G\# B\#" added to them, to set the color for that specific option. Omit

  the R\# G\# B\# values to reset them back to default.

**Note:** The use of custom is a one time event, it is not persistent.

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

**Question:**

My map is no different than normal and /mapfilter all had no effect, what did I do wrong?

**Answer:**

Each individual filter needs to be turned on individually, _/mapfilter all show_ does not toggle all filters to "show" as might be expected.
