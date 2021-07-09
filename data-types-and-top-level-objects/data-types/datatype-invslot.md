# DataType:invslot

## Info

This DataType is not to be confused with the TLO:InvSlot which has been deprecated in favor of DataType:item:ItemSlot

### Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_int_](datatype-int.md) | **ID** | ID of this item slot \(usable directly by [/itemnotify](../../commands/slash-commands/itemnotify.md)\) |
| [_item_](datatype-item.md) | **Item** | Item data for the item in this slot |
| [_string_]() | **Name** | For inventory slots not inside packs, the slot name, otherwise NULL |
| _invslot_ | **Pack** | Container that must be opened to access the slot with [/itemnotify](../../commands/slash-commands/itemnotify.md) |
| [_int_](datatype-int.md) | **Slot** | Slot number inside the pack which holds the item, otherwise NULL |
| '**'**[**int**](datatype-int.md) | **To String** | Same as **ID** |

## Example

Bag is a defined variable in a for loop in this case:

```text
/if (${InvSlot[pack${Bag}].Item.Item[${Slot}].NoDrop}) {
    /echo I found a No Drop Item: \ag${InvSlot[pack${Bag}].Item.Item[${Slot}].Name}
    /return
}
```

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* TLO:ItemSlot
* [DataType:item](datatype-item.md)
* [Slot Names](../../general-information/slot-names.md)

