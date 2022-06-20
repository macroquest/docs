---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `FindItemBank`

Find item in bank by partial name match. Using =name will find an exact match only.

Of note: The FindItemBank with ItemSlot REQUIRES that bank item containers be open to function correctly. Due to potential exploits the command will not work if the bank containers are closed. This is in contrast to FindItem functionality with character containers, where ItemSlot was designed to allow inventory management without opening containers.

## Forms

|  |  |
| :--- | :--- |
| [_item_](../data-types/datatype-item.md) **FindItemBank[**name**]** | Returns item in your bank by partial name match |
| [_item_](../data-types/datatype-item.md) **FindItemBank[**=name**]** | Returns item in your bank by exact name match |

## Examples

`/echo ${FindItemBank[=Swirling Shadows]}`

This is a simple example with little use, but If the item is found, the name of the item will be echoed

`/echo ${FindItemBank[=Swirling Shadows].ItemSlot}`

Will return Bank's item slot
