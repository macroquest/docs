## Info

This DataType is not to be confused with the TLO:InvSlot which has been deprecated in favor of DataType:item:ItemSlot

### Members

|                                        |               |                                                                                            |
|----------------------------------------|---------------|--------------------------------------------------------------------------------------------|
| **Type**                               | **Member**    | **Description**                                                                            |
| *[int](datatype-int.md)*       | **ID**        | ID of this item slot (usable directly by [/itemnotify](../commands/itemnotify.md))             |
| *[item](datatype-item.md)*     | **Item**      | Item data for the item in this slot                                                        |
| *[string](datatype-string.md)* | **Name**      | For inventory slots not inside packs, the slot name, otherwise NULL                        |
| *invslot*                              | **Pack**      | Container that must be opened to access the slot with [/itemnotify](../commands/itemnotify.md) |
| *[int](datatype-int.md)*       | **Slot**      | Slot number inside the pack which holds the item, otherwise NULL                           |
| '**'[int](datatype-int.md)**   | **To String** | Same as **ID**                                                                             |

## Example

Bag is a defined variable in a for loop in this case:

    /if (${InvSlot[pack${Bag}].Item.Item[${Slot}].NoDrop}) {
        /echo I found a No Drop Item: \ag${InvSlot[pack${Bag}].Item.Item[${Slot}].Name}
        /return
    }

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   TLO:ItemSlot
-   [DataType:item](datatype-item.md)
-   [Slot Names](../general-information/slot-names.md)


