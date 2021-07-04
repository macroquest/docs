# DataType:raidmember

## Description

Data related to the specified raid member

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_class_](datatype-class.md) | **Class** | Raid member's class \(works without being in zone\) |
| [_int_](datatype-int.md) | **Group** | Current group number \(or 0\) |
| [_bool_](datatype-bool.md) | **GroupLeader** | Returns TRUE if the member is a group leader |
| [_int_](datatype-int.md) | **Level** | Raid member's level \(works without being in zone\) |
| [_bool_](datatype-bool.md) | **Looter** | Allowed to loot with current loot rules and looters? |
| [_string_](datatype-string.md) | **Name** | Raid member's name |
| [_bool_](datatype-bool.md) | **RaidLeader** | Returns TRUE if the member is the raid leader |
| [_spawn_](datatype-spawn.md) | **Spawn** | Spawn object for this player if available \(must be in zone\) |
| '**'**[**string**](datatype-string.md) | **To String** | Same as **Name** |

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [DataType:raid](datatype-raid.md)

