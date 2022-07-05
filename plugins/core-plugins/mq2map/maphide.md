---
tags:
   - command
---
# /maphide

## Syntax

**/maphide** _**spawnname**_ **\[reset\]**

## Description

This will hide _spawnname_ from the map. Hidden spawns are in effect until you reset /maphide, or the mapped spawns are regenerated \(such as changing certain map filters\).

## Examples

* Re-generates the spawn list

  ```text
  /maphide reset
  ```

* Hides all spawns level 39 and below

  ```text
  /maphide npc range 1-39
  ```
