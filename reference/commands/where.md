---
tags:
    - command
---
# /where

## Syntax

```eqcommand
/where [ pc | npc ] [ <spawnname> ]
```

## Description

Lists where the closest PC, NPC or _spawnname_ is. The message returned is:

```text
The closest 'spawnname' is a level # <race> <class> and <distance> away to the <direction>, Z difference = #.##.
```

## Examples

```text
 /where                   Lists the closest PC or NPC
 /where pc                Lists the closest PC
 /where npc               Lists the closest NPC
 /where npc "orc pawn"    Lists where the closest orc pawn is
```

