# DataType:dynamiczone

## Description

Data for the current dynamic zone instance

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_dzmember_](datatype-dzmember.md) | **Leader** | The leader of the dynamic zone |
| [_bool_](datatype-bool.md) | **LeaderFlagged** | Returns true if the dzleader can successfully enter the dz \(this also means the dz is actually Loaded.\) Example: ${DynamicZone.LeaderFlagged} |
| [_int_](datatype-int.md) | **MaxMembers** | Maximum number of characters that can enter this dynamic zone |
| [_dzmember_](datatype-dzmember.md) | **Member\[**\#**\|**name**\]** | The dynamic zone member _\#_ or _name_ |
| [_int_](datatype-int.md) | **Members** | Current number of characters in the dynamic zone |
| [_string_](datatype-string.md) | **Name** | The full name of the dynamic zone |
| '**'**[**string**](datatype-string.md) | **To String** | Same as **Name** |

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)
* [DataType:dzmember](datatype-dzmember.md)

