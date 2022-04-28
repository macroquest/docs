# DataType:heading

Data related to a specific spawn heading

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Clock** | The nearest clock direction, e.g. 1-12 |
| [_float_](datatype-float.md) | **Degrees** | Heading in degrees (same as casting to float) |
| [_float_](datatype-float.md) | **DegreesCCW** | Heading in degrees counter-clockwise (the way the rest of MQ2 and EQ uses it) |
| \_\_[_string_](datatype-string.md)\_\_ | **Name** | The long compass direction, eg. "south", "south by southeast" |
| \_\_[_string_](datatype-string.md)\_\_ | **ShortName** | The short compass direction, eg. "S", "SSE" |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | Same as **ShortName** |

