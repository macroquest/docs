---
tags:
    - datatype
---
# `raid`

Contains data on the current raid

## Members

| **Type** | **Member** | **Description**  |
| --- | --- | --- |
| [_float_](datatype-float.md) | **AverageLevel** | Average level of raid members (more accurate than in the window) |
| [_bool_](datatype-bool.md) | **Invited** | Have I been invited to the raid? |
| [_raidmember_](datatype-raidmember.md) | **Leader** | Raid leader |
| [_bool_](datatype-bool.md) | **Locked** | Returns TRUE if the raid is locked |
| [_string_](datatype-string.md) | **Looter**[_#_] | Specified looter name by number |
| [_int_](datatype-int.md) | **Looters** | Number of specified looters |
| [_int_](datatype-int.md) | **LootType** | <p>Loot type number:</p><ul><li>1 = Leader</li><li>2 = Leader & GroupLeader</li><li>3 = Leader & Assignments</li></ul> |
| [_raidmember_](datatype-raidmember.md) | **MainAssist** | Raid main assist |
| [_raidmember_](datatype-raidmember.md) | **MasterLooter** | Raid Master Looter |
| [_raidmember_](datatype-raidmember.md) | **Member**[_N_] | Raid member by number _N_ |
| [_raidmember_](datatype-raidmember.md) | **Member**[_name_] | Raid member by _name_. |
| [_int_](datatype-int.md) | **Members** | Total number of raid members |
| [_raidmember_](datatype-raidmember.md) | **Target** | Raid target (clicked in raid window) |
| [_int_](datatype-int.md) | **TotalLevels** | Sum of all raid member's levels |
| [_string_](datatype-string.md) | **(To String)** | None
