---
tags:
    - datatype
---
# `augtype` Type

Describes data about an augmentation slot in an item.

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_][bool] | **Empty** | True if the slot is empty |
| [_bool_][bool] | **Infusable** | True if this is a hidden energeian power source slot. |
| [_item_][item] | **Item** | The item socketed in this slot, if any. |
| [_string_][string] | **Name** | The name of the item socketed in this slot, if any. |
| [_int_](int) | **Slot** | Index of the augment slot. |
| [_int_](int) | **Solvent** | Item ID of the solvent used to remove this item, if any. |
| [_int_](int) | **Type** | Type of augment slot. |
| [_int_](int) | **Visible** | True if this slot is visible to the user. |

[int]: ./datatype-int.md
[bool]: ./datatype-bool.md
[string]: ./datatype-string.md
[item]: ./datatype-item.md
