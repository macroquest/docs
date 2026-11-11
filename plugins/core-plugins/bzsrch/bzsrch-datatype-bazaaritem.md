---
tags:
   - datatype
---
# `bazaaritem`

<!--dt-desc-start-->
Represents an individual item in bazaar search results, providing access to item details and trader information.
<!--dt-desc-end-->

## Members
<!--dt-members-start-->
/// member | string Name
The name of the item.
///

/// member | string FullName
Full item name including special characters (e.g. `Burynai Burial Regalia (Caza)`)
///

/// member | string Trader
The name of the trader selling the item.
///

/// member | int Price
Price per unit
///

/// member | int Quantity
Available quantity from this trader **per stack**. If the item id is stackable, this will return the stack size. If the item id is not stackable, this will return 1.
///

/// member | int ItemID
EQ item ID number
///
<!--dt-members-end-->  

## Methods

| Name       | Action                                |
| ---------- | ------------------------------------- |
| **Select** | Selects item in bazaar search window  |

## Examples

!!! Example "bazaaritem"
    === "MQScript"
        ```text
        /echo ${Bazaar.SortedItem[2].Price}
        /echo ${Bazaar.Item[1].Quantity}
        /echo ${Bazaar.SortedItem[5].ItemID}
        /echo ${Bazaar.Item[20].Trader}
        /echo ${Bazaar.SortedItem[5].Name}
        /invoke ${Bazaar.Item[1].Select}
        /echo ${Bazaar.Item[3].FullName}
        ```

    === "Lua"
        ```lua
        print(mq.TLO.Bazaar.SortedItem(2).Price())
        print(mq.TLO.Bazaar.Item(1).Quantity())
        print(mq.TLO.Bazaar.SortedItem(5).ItemID())
        print(mq.TLO.Bazaar.Item(20).Trader())
        print(mq.TLO.Bazaar.SortedItem(5).Name())
        mq.TLO.Bazaar.Item(1).Select()
        print(mq.TLO.Bazaar.Item(3).FullName())
        ```
<!--dt-linkrefs-start-->  
[int]: ../../../reference/data-types/datatype-int.md
[string]: ../../../reference/data-types/datatype-string.md
<!--dt-linkrefs-end-->  