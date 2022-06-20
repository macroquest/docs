---
tags:
    - ref
    - slash
---
# /alert

## Syntax

**/alert [ add \| remove \] \# \[pc\|npc\|corpse\|any\] \[radius \#\] \[range** _**lowerlevel upperlevel**_**\] "spawnname" \[clear\|list \#]**

## Description

Used to manipulate alert lists which "watch" for spawns.

## Examples

|  |  |
| :--- | :--- |
| **/alert add 1 "spawnname"** | Adds spawn name to alert list 1 |
| **/alert clear 1** | Clears all members from alert list 1 |
| **/alert list 1** | Lists all members of alert list 1 |
| **/alert add 1 npc radius 300 "spawnname"** | Sets alert(1) to TRUE if "spawnname" is within radius of 300 from your location |
| **/alert add 2 npc range 30 200 "spawnname"** | Sets alert(2) to TRUE if any "spawnname" are within 30 to 200 range from your location |
| **/alert remove 1 id spawnID** | Removes the entry in alert list 1 for spawnID |
