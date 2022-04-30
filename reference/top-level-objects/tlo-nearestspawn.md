# TLO:NearestSpawn

## Description

Object that is used in finding spawns nearest to you.

## Forms

|  |  |
| :--- | :--- |
| [_spawn_](../data-types/datatype-spawn.md) **NearestSpawn[**\#**]** | The \#th nearest spawn |
| [_spawn_](../data-types/datatype-spawn.md) **NearestSpawn[**search**]** | The nearest spawn matching this search string (see [Spawn Search](../../reference/general/spawn-search.md)) |
| [_spawn_](../data-types/datatype-spawn.md) **NearestSpawn[**\#**,**search**]** | The \#th nearest spawn matching this search string (see [Spawn Search](../../reference/general/spawn-search.md)) |

## Access to Types

* [_spawn_](../data-types/datatype-spawn.md) **spawn**

## Examples

`/echo ${NearestSpawn[npc radius 100 "orc pawn"]}`

Finds the npc containing orc pawn in its name that is within 100 of you.

`/echo ${NearestSpawn[2]}`

Finds the closest spawn to you (${NearestSpawn[1]} will always match yourself).
