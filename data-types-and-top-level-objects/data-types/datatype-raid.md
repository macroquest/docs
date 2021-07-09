# DataType:raid

## Description

Contains data on the current raid

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_float_](datatype-float.md) | **AverageLevel** | Average level of raid members \(more accurate than in the window\) |
| [_bool_](datatype-bool.md) | **Invited** | Have I been invited to the raid? |
| [_raidmember_](datatype-raidmember.md) | **Leader** | Raid leader |
| [_bool_](datatype-bool.md) | **Locked** | Returns TRUE if the raid is locked |
| [_string_]() | **Looter\[**\#**\]** | Specified looter name by number |
| [_int_](datatype-int.md) | **Looters** | Number of specified looters |
| [_int_](datatype-int.md) | **LootType** | Loot type number:  1 Leader  2 Leader & GroupLeader  3 Leader & Specified |
| [_raidmember_](datatype-raidmember.md) | **MainAssist** | Raid main assist |
| [_raidmember_](datatype-raidmember.md) | **MasterLooter** | Raid Master Looter |
| [_raidmember_](datatype-raidmember.md) | **Member\[**\#**\]** | Raid member by number |
| [_raidmember_](datatype-raidmember.md) | **Member\[**name**\]** | Raid member by _name_ |
| [_int_](datatype-int.md) | **Members** | Total number of raid members |
| [_raidmember_](datatype-raidmember.md) | **Target** | Raid target \(clicked in raid window\) |
| [_int_](datatype-int.md) | **TotalLevels** | Sum of all raid members' levels |
| '**'**[**string**]() | **To String** | None |

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Raid](../top-level-objects/tlo-raid.md)
* [DataType:raidmember](datatype-raidmember.md)

