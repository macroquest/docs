## Description

Object that is used in finding spawns nearest to you.

## Forms

|                                                                           |                                                                                                 |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| *[spawn](../data-types/datatype-spawn.md)* **NearestSpawn\[**#**\]**            | The #th nearest spawn                                                                           |
| *[spawn](../data-types/datatype-spawn.md)* **NearestSpawn\[**search**\]**       | The nearest spawn matching this search string (see [Spawn Search](../general-information/spawn-search.md))     |
| *[spawn](../data-types/datatype-spawn.md)* **NearestSpawn\[**#**,**search**\]** | The #th nearest spawn matching this search string (see [Spawn Search](../general-information/spawn-search.md)) |

## Access to Types

-   *[spawn](../data-types/datatype-spawn.md)* **spawn**

## Examples

`  /echo ${NearestSpawn[npc radius 100 "orc pawn"]}`

Finds the npc containing orc pawn in its name that is within 100 of you.

`  /echo ${NearestSpawn[2]}`

Finds the closest spawn to you (${NearestSpawn\[1\]} will always match yourself).

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [spawn](../data-types/datatype-spawn.md)
-   [Spawn Search](../general-information/spawn-search.md)


