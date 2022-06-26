---
tags:
    - datatype
---
# `groupmember`

Contains data on a specific group member

## Members

this type inherits members from [_spawn_ ](datatype-spawn.md)if the member is in the current zone.

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Index** | Which number in the group the member is |
| [_bool_](datatype-bool.md) | **Leader** | TRUE if the member is the group's leader, FALSE otherwise |
| [_int_](datatype-int.md) | **Level** | The member's level |
| [_bool_](datatype-bool.md) | **MainAssist** | TRUE if the member is designated as the group's Main Assist, FALSE otherwise |
| [_bool_](datatype-bool.md) | **MainTank** | TRUE if the member is designated as the group's Main Tank, FALSE otherwise |
| [_bool_](datatype-bool.md) | **Mercenary** | TRUE if the member is a mercenary, FALSE otherwise |
| [_string_](datatype-string.md) | **Name** | The name of the group member. This works even if they are not in the same zone as you. |
| [_bool_](datatype-bool.md) | **Offline** | TRUE if the member is offline and FALSE if online |
| [_bool_](datatype-bool.md) | **OtherZone** | TRUE if the member is online but in another zone and FALSE if online and in same zone as you. |
| [_bool_](datatype-bool.md) | **Present** | TRUE if the member is online and in same zone and FALSE if online and not in same zone as you. |
| [_bool_](datatype-bool.md) | **Puller** | TRUE if the member is designated as the group's Puller, FALSE otherwise |
| [_spawn_](datatype-spawn.md) | **Spawn** | Accesses the group member's spawn. Not all members will have a spawn (if they are out of the zone). |
| [_string_](datatype-string.md) | **To String** | Same as **Name** |

## Examples

`/echo ${Group.Member[0].Leader}`

Echo TRUE if you are Group Leader.

`/echo ${Group.Member[3].Puller}`

Echo TRUE if Group Member 3 is marked as Role Puller

