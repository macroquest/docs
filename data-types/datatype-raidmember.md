## Description

Data related to the specified raid member

## Members

|                                            |                 |                                                             |
|--------------------------------------------|-----------------|-------------------------------------------------------------|
| **Type**                                   | **Member**      | **Description**                                             |
| *[class](datatype-class.md)*       | **Class**       | Raid member's class (works without being in zone)           |
| *[int](datatype-int.md)*           | **Group**       | Current group number (or 0)                                 |
| *[bool](datatype-bool.md)*         | **GroupLeader** | Returns TRUE if the member is a group leader                |
| *[int](datatype-int.md)*           | **Level**       | Raid member's level (works without being in zone)           |
| *[bool](datatype-bool.md)*         | **Looter**      | Allowed to loot with current loot rules and looters?        |
| *[string](datatype-string.md)*     | **Name**        | Raid member's name                                          |
| *[bool](datatype-bool.md)*         | **RaidLeader**  | Returns TRUE if the member is the raid leader               |
| *[spawn](datatype-spawn.md)*       | **Spawn**       | Spawn object for this player if available (must be in zone) |
| '**'[string](datatype-string.md)** | **To String**   | Same as **Name**                                            |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [DataType:raid](datatype-raid.md)


