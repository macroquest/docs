---
tags:
    - command
---
# /who

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/who <options>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Searches the current zone for the spawns matching the specified [Spawn Search](../../reference/general/spawn-search.md) _options_, with the addition of:

* all: Scan all zones. Note: this reverts to the native /who command.
* concolor: Displays the results in consider colors
* sort \: Sort by this metric
<!--cmd-desc-end-->
## Examples

* **/who npc named**

Displays a List of The Named NPC in Zone

* **/who pc Cleric**

Displays a List of Player Clerics (Even if Anon or /role)

* **/who npc pixtt**

Diplays a List of NPC's with pixtt in their name

* **/who npc 64**

Displays a List of NPC's who are level 64

* **/who pc 70**

Displays a List of PC's Who are level 70

* **/who race human**

Displays a List of PC's Who are Human

* **/whotarget (/whot)**

Displays a /who for your target, works on npc/pc shows even if role/anon, Shows if sneaking as well.

