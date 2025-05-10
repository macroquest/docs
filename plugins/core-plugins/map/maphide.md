---
tags:
   - command
---
# /maphide

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/maphide [<spawnsearch> | reset | repeat] 
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
This will hide spawns from the map, using [Spawn search](../../../reference/general/spawn-search.md). Hidden spawns are in effect until you reset /maphide, or the mapped spawns are regenerated (such as changing certain map filters).
<!--cmd-desc-end-->
## Examples

* Re-generates the spawn list

  ```text
  /maphide reset
  ```

* Hides all spawns level 39 and below

  ```text
  /maphide npc range 1-39
  ```
