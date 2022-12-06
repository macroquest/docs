---
tags:
    - datatype
---
# `tradeskilldepot`

This contains information related to a tradeskill depot.

## Members

| **Type** | **Member** | **Description**  |
| --- | --- | --- |
| [_int_](datatype-int.md) | **Count** | Returns the number of item stacks in the tradeskill depot. |
| [_int_](datatype-int.md) | **Capacity** | Returns the total capacity of the tradeskill depot. |
| [_bool_](datatype-bool.md) | **Enabled** | Returns whether the tradeskill depot is enabled or not. It requires the Night of Shadows expansion. |
| [_bool_](datatype-bool.md) | **ItemsReceived** | Returns whether the tradeskill depot has been populated with items. The window must be opened at least once for the depot to be populated with items. |
| [_item_](datatype-item.md) | **FindItem**[ _#_ ] | Find an item with the given item ID in the tradeskill depot. |
| [_item_](datatype-item.md) | **FindItem**[_name_] | Find an item by partial name in the tradeskill depot. Prefix with "=" for an exact match. |
| [_int_](datatype-int.md) | **FindItemCount**[ _#_ ] | Find the number of items with the given item ID in the tradeskill depot. |
| [_int_](datatype-int.md) | **FindItemCount**[_name_] | Find the number of items by partial name in the tradeskill depot. Prefix with "=" for an exact match. |
| [_item_](datatype-item.md) | **SelectedItem** | Returns the currently selected item in the tradeskill depot window. |

## Methods

| Name | Action |
| :--- | :--- |
| **SelectItem**[_name_] | Select an item with the given name |
| **WithdrawItem** | Withdraw the selected item from the tradeskill depot. Will create a quantity window if there is more than one item in the stack. |
| **WithdrawItem**[_name_] | Withdraw the given item name from the tradeskill depot. Will create a quantity window if there is more than one item in the stack. |
| **WithdrawStack** | Withdraw a full stack of the selected item from the tradeskill depot. |
| **WithdrawStack**[_name_] | Withdraw a full stack of the given item name from the tradeskill depot. |
