# DataType:evolving

## Description

A DataType that deals with evolving items.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_float_](datatype-float.md) | **ExpPct** | Percentage of experience that the item has gained |
| [_bool_](datatype-bool.md) | **ExpOn** | Is evolving item experience turned on for this item? |
| [_int_](datatype-int.md) | **Level** | The level of the evolving item. |
| [_int_](datatype-int.md) | **MaxLevel** | The maximum level of the evolving item |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | Same as **ExpOn** |

## Examples

`/echo ${FindItem[Blade of the Eclipse].Evolving.ExpPct}`

