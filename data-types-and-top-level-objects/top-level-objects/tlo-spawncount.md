# TLO:SpawnCount

## Description

Object used to get information on the count(s\) of all spawns or specific spawn\(s). Uses the filters under [Spawn Search](../../general-information/spawn-search.md).

## Forms

|  |  |
| :--- | :--- |
| [_int_](../data-types/datatype-int.md) **SpawnCount** | Total number of spawns in current zone |
| [_int_](../data-types/datatype-int.md) **SpawnCount[**search string**]** | Total number of spawns in current zone matching the _search string_ |

## Access to Types

* [_int_](../data-types/datatype-int.md) **int**

## Examples

`/echo ${SpawnCount}`

Displays the count of all spawns.

`/echo ${SpawnCount[range 45 50]}`

Displays the count of all spawns in the level range of 45 to 50.

`/echo ${SpawnCount[npc radius 100]}`

Displays count of all NPCs within a radius of 100.

## See Also

* [Top-Level Objects](./)
* [int](../data-types/datatype-int.md)
* [Spawn Search](../../general-information/spawn-search.md)

