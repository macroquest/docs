# TLO:Spawn

## Description

Object used to get information on a specific spawn. Uses the filters under [Spawn Search](../../general-information/spawn-search.md).

## Forms

|  |  |
| :--- | :--- |
| [_spawn_](../data-types/datatype-spawn.md) **Spawn[**\#**]** | Spawn matching ID \# |
| [_spawn_](../data-types/datatype-spawn.md) **Spawn[**search string**]** | Any spawns matching _search string_ |

## Access to Types

* [_spawn_](../data-types/datatype-spawn.md) **spawn**

## Examples

`/echo ${Spawn[1000]}`

Displays the name of the spawn with id number 1000.

`/target ${Spawn[npc radius 500 trakanon]}`

Targets the npc with the name Trakanon only if within a radius of 500.

## See Also

* [Top-Level Objects](./)
* [spawn](../data-types/datatype-spawn.md)
* [Spawn Search](../../general-information/spawn-search.md)

