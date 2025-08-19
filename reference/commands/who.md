---
tags:
    - command
---
# /who

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/who [concolor | sort <metric> | all | <spawn search>]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Searches the current zone for spawns matching the specified [Spawn Search](../../reference/general/spawn-search.md) or other options.
<!--cmd-desc-end-->

## Options
**all**  
:  Scan all zones. (reverts to native /who command)  

**concolor**  
:  Displays the results in consider colors  

**sort** `{level | name | race | class | distance | guild | id}`  
:  Sort by this metric

## Examples

`/who range 65 70`
:  Shows players within level 65 to 70 in your zone.

`/who npc named`
:  Displays a List of The Named NPC in Zone

`/who npc named`
:  Displays a List of The Named NPC in Zone

`/who pc Cleric`
:  Displays a List of Player Clerics (Even if Anon or /role)

`/who npc pixtt`
:  Diplays a List of NPC's with pixtt in their name

`/who npc 64`
:  Displays a List of NPC's who are level 64

`/who pc 70`
:  Displays a List of PC's Who are level 70

`/who race human`
:  Displays a List of PC's Who are Human

`/who healer sort distance`
:  Displays healers in the zone, sorted by distance

`/who knight sort level`
:  Displays paladins and shadow knights in the zone, sorted by level

## See also

- [/whotarget](whotarget.md)
