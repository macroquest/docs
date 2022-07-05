---
tags:
    - datatype
---
# `invslot`

Data related to an inventory slot.

### Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | ID of this item slot (usable directly by [/itemnotify](../../reference/commands/itemnotify.md)) |
| [_item_](datatype-item.md) | **Item** | Item data for the item in this slot |
| [_string_](datatype-string.md) | **Name** | For inventory slots not inside packs, the slot name, otherwise NULL |
| [_invslot_](datatype-invslot.md) | **Pack** | Container that must be opened to access the slot with [/itemnotify](../../reference/commands/itemnotify.md) |
| [_int_](datatype-int.md) | **Slot** | Slot number inside the pack which holds the item, otherwise NULL |
| [_string_](datatype-string.md) | **To String** | Same as **ID** |

## Example

Bag is a defined variable in a for loop in this case:

```text
/if (${InvSlot[pack${Bag}].Item.Item[${Slot}].NoDrop}) {
    /echo I found a No Drop Item: \ag${InvSlot[pack${Bag}].Item.Item[${Slot}].Name}
    /return
}
```

