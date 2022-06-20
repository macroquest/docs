---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `merchant`

This contains information related to the active merchant.

## Members

This type inherits members from [_spawn_](datatype-spawn.md) if a merchant is active.

| **Type** | **Member** | **Description**  |
| --- | --- | --- |
| [_bool_](datatype-bool.md) | **Full** | Returns True if the merchant's inventory is full. |
| [_int_](datatype-int.md) | **Items** | Number of items on the merchant. |
| [_item_](datatype-item.md) | **Item**[ _#_ ] | Item number _#_ on the merchant's list. |
| [_item_](datatype-item.md) | **Item**[_name_] | Find an item by partial name on the merchant's list. Prefix with "=" for an exact match. |
| [_float_](datatype-float.md) | **Markup** | <p>The number used to calculate the buy and sell value for an item. (This is what is changed by charisma and faction). This value is capped at 1.05.</p><br><ul><li>Markup * Item Value = Amount you buy item for</li><li>Item Value * (1/Markup) = Amount you sell item for</li></ul> |
| [_bool_](datatype-bool.md) | **Open** | Returns True if the merchant window is open. |
| [_item_](datatype-item.md) | **SelectedItem** | The currently selected item in the merchant window. Items can be selected by using [/selectitem](../commands/selectitem.md) |
| [_bool_](datatype-bool.md) | **ItemsReceived** | True if the merchant's item list has been populated. |
| [_string_](datatype-string.md) | **(To String)** | Same as *Open* |

## Methods

| Name | Action |
| :--- | :--- |
| **Buy**[_#_] | Buys \# of whatever is selected with **Merchant.SelectItem\[xxx]** |
| **OpenWindow** | Will open the merchant closest to you, or if you have a merchant target |
| **CloseWindow** | Will close the merchant window |
| **SelectItem**[_name_] | Select item by partial name match, case insensitive. Prefix _name_ with `=` for EXACT match |
| **Sell**[_count_] | Sell _count_ of selected item. See examples |

## Examples

Using `${Merchant.Sell[#]}`:

```
/selectitem "Diamond"
```

Will select a "Diamond" you can also do "=Diamond" to match EXACT name. Then you can the following command to sell 100 of it:

```
/invoke ${Merchant.Sell[100]}
```
