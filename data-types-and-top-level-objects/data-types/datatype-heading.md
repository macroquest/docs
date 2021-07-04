# DataType:heading

## Description

Data related to a specific spawn heading

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_int_](datatype-int.md) | **Clock** | The nearest clock direction, e.g. 1-12 |
| [_float_](datatype-float.md) | **Degrees** | Heading in degrees \(same as casting to float\) |
| [_float_](datatype-float.md) | **DegreesCCW** | Heading in degrees counter-clockwise \(the way the rest of MQ2 and EQ uses it\) |
| [_string_](datatype-string.md) | **Name** | The long compass direction, eg. "south", "south by southeast" |
| [_string_](datatype-string.md) | **ShortName** | The short compass direction, eg. "S", "SSE" |
| '**'**[**string**](datatype-string.md) | **To String** | Same as **ShortName** |

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Heading](../top-level-objects/tlo-heading.md)
* [DataType:spawn](datatype-spawn.md)
* [DataType:ground](datatype-ground.md)
* [DataType:switch](datatype-switch.md)

