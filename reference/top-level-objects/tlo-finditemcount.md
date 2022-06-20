---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `FindItemCount`

Count of items on character by partial name match. Using =name will find an exact match only.

## Forms

|  |  |
| :--- | :--- |
| [_int_](../data-types/datatype-int.md) **FindItemCount[**name**]** | Count of items on character by partial name match |
| [_int_](../data-types/datatype-int.md) **FindItemCount[**=name**]** | Count of items on character by exact name match |

## Examples

`/echo ${FindItemCount[=Water Flask]}`

Echoes the number of Water Flasks you have in your inventory.

`/echo ${FindItemCount["=${SomeItem}"]}`

Echoes the number of an item as defined by a string. Note the placement of the quotes, it is important.
