---
tags:
    - command
---
# /where

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/where [ pc | npc ] [ <spawnname> ]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Lists where the closest PC, NPC or _spawnname_ is. The message returned is:

```text
The closest 'spawnname' is a level # <race> <class> and <distance> away to the <direction>, Z difference = #.##.
```
<!--cmd-desc-end-->
## Examples

```text
 /where                   Lists the closest PC or NPC
 /where pc                Lists the closest PC
 /where npc               Lists the closest NPC
 /where npc "orc pawn"    Lists where the closest orc pawn is
```

