---
tags:
    - datatype
---
# `tradeskilldepot`

This contains information related to a tradeskill depot.

## Members

### {{ renderMember(type='int', name='Capacity') }}

:   Returns the total capacity of the tradeskill depot.

### {{ renderMember(type='int', name='Count') }}

:   Returns the number of item stacks in the tradeskill depot.

### {{ renderMember(type='bool', name='Enabled') }}

:   Returns whether the tradeskill depot is enabled or not. It requires the Night of Shadows expansion.

### {{ renderMember(type='item', name='FindItem', params='#') }}

:   Find an item with the given item ID in the tradeskill depot.

### {{ renderMember(type='item', name='FindItem', params='name') }}

:   Find an item by partial name in the tradeskill depot. Prefix with "=" for an exact match.

### {{ renderMember(type='int', name='FindItemCount', params='#') }}

:   Find the number of items with the given item ID in the tradeskill depot.

### {{ renderMember(type='int', name='FindItemCount', params='name') }}

:   Find the number of items by partial name in the tradeskill depot. Prefix with "=" for an exact match.

### {{ renderMember(type='bool', name='ItemsReceived') }}

:   Returns whether the tradeskill depot has been populated with items. The window must be opened at least once for the depot to be populated with items.

### {{ renderMember(type='item', name='SelectedItem') }}

:   Returns the currently selected item in the tradeskill depot window.


## Methods

| Name | Action |
| :--- | :--- |
| **DepositItem** | Deposit the item on cursor into the tradeskill depot. |
| **SelectItem**[_name_] | Select an item with the given name |
| **WithdrawItem** | Withdraw the selected item from the tradeskill depot. Will create a quantity window if there is more than one item in the stack. |
| **WithdrawItem**[_name_] | Withdraw the given item name from the tradeskill depot. Will create a quantity window if there is more than one item in the stack. |
| **WithdrawStack** | Withdraw a full stack of the selected item from the tradeskill depot. |
| **WithdrawStack**[_name_] | Withdraw a full stack of the given item name from the tradeskill depot. |

[int]: datatype-int.md
[bool]: datatype-bool.md
[item]: datatype-item.md
