# DataType:dzmember

## Description

This DataType contains information on the members of the current dynamic zone instance

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_bool_](datatype-bool.md) | **Flagged** | Returns true if the dzmember can successfully enter the dz. } where x is either index or the name. |
| [_string_](datatype-string.md) | **Name** | The name of the member |
| [_string_](datatype-string.md) | **Status** | The status of the member - one of the following: Unknown, Online, Offline, In Dynamic Zone, Link Dead |
| '**'**[**string**](datatype-string.md) | **To String** | Same as **Name** |

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)
* [DataType:dynamiczone](datatype-dynamiczone.md)

