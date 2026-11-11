---
tags:
    - datatype
---
# `merchant`

<!--dt-desc-start-->
This contains information related to the active merchant.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
This type inherits members from [_spawn_](datatype-spawn.md) if a merchant is active.

/// member | bool Full
Returns True if the merchant's inventory is full.
///

/// member | item Item[#]
Item number _#_ on the merchant's list.
///

/// member | item Item[name]
Find an item by partial name on the merchant's list. Prefix with "=" for an exact match.
///

/// member | int Items
Number of items on the merchant.
///

/// member | bool ItemsReceived
True if the merchant's item list has been populated.
///

/// member | float Markup
The number used to calculate the buy and sell value for an item. (This is what is changed by charisma and faction). This value is capped at 1.05.

- Amount you buy item for = Item Value * Markup
- Amount you sell item for = Item Value * (1/Markup)
///

/// member | bool Open
Returns True if the merchant window is open.
///

/// member | item SelectedItem
The currently selected item in the merchant window. Items can be selected by using [/selectitem](../commands/selectitem.md) or the `SelectItem` method
///

### [string][string] `(To String)`

:   Same as *Open*
<!--dt-members-end-->

## Methods

| Name | Action |
| :--- | :--- |
| **Buy**[_#_] | Buys \# of whatever is selected with **Merchant.SelectItem\[xxx]** |
| **CloseWindow** | Will close the merchant window |
| **OpenWindow** | Will open the merchant closest to you, or if you have a merchant target |
| **SelectItem**[_name_] | Select item by partial name match, case insensitive. Prefix _name_ with `=` for EXACT match |
| **Sell**[_count_] | Sell _count_ of selected item. See examples |

## Examples

Using Sell:

```
/selectitem "Diamond"
```

Will select a "Diamond" you can also do "=Diamond" to match EXACT name. Then you can the following command to sell 100 of it:

```
/invoke ${Merchant.Sell[100]}
```
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[int]: datatype-int.md
[item]: datatype-item.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
