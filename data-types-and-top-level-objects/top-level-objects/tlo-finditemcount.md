# TLO:FindItemCount

## Description

Count of items on character by partial name match. Using =name will find an exact match only.

## Forms

|  |  |
| :--- | :--- |
| [_int_](../data-types/datatype-int.md) **FindItemCount\[**name**\]** | Count of items on character by partial name match |
| [_int_](../data-types/datatype-int.md) **FindItemCount\[**=name**\]** | Count of items on character by exact name match |

## Access to Types

* [_int_](../data-types/datatype-int.md) **int**

## Examples

`/echo ${FindItemCount[=Water Flask]}`

Echoes the number of Water Flasks you have in your inventory.

`/echo ${FindItemCount["=${SomeItem}"]}`

Echoes the number of an item as defined by a string. Note the placement of the quotes, it is important.

## See Also

* [Top-Level Objects](./)
* [int](../data-types/datatype-int.md)

