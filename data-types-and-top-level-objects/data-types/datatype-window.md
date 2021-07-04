# DataType:window

## Description

This contains data related to the specified in-game window

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_argb_](datatype-argb.md) | **BGColor** | Background color |
| [_bool_](datatype-bool.md) | **Checked** | Returns TRUE if the button has been checked |
| _window_ | **Child\[**name**\]** | Child with this name |
| [_bool_](datatype-bool.md) | **Children** | Returns TRUE if the window has children |
| [_action_](datatype-action.md) | **DoClose** | Does the ction of closing a window |
| [_action_](datatype-action.md) | **DoOpen** | Does the action of opening a window |
| [_bool_](datatype-bool.md) | **Enabled** | Returns TRUE if the window is enabled |
| _window_ | **FirstChild** | First child window |
| [_int_](datatype-int.md) | **GetCurSel** | Int of the currently selected/highlighted item in a list or treeview |
| [_int_](datatype-int.md) | **Height** | Height in pixels |
| [_bool_](datatype-bool.md) | **Highlighted** | Returns TRUE if the window is highlighted |
| [_bool_](datatype-bool.md) | **HisTradeReady** | Has the other person clicked the Trade button? |
| [_int_](datatype-int.md) | **HScrollMax** | Horizontal scrollbar range |
| [_int_](datatype-int.md) | **HScrollPos** | Horizontal scrollbar position |
| [_int_](datatype-int.md) | **HScrollPct** | Horizontal scrollbar position in % to range from 0 to 100 |
| [_int_](datatype-int.md) | **Items** | Number of items in a Listbox or Combobox |
| [_action_](datatype-action.md) | **LeftMouseDown** | Does the action of clicking the left mouse button down |
| [_action_](datatype-action.md) | **LeftMouseHeld** | Does the action of holding the left mouse button |
| [_action_](datatype-action.md) | **LeftMouseHeldUp** | does the action of holding the left mouse button up |
| [_action_](datatype-action.md) | **LeftMouseUp** | Does the action of clicking the left mouse button up |
| [_string_](datatype-string.md) | **List\[**\#**,**y**\]** | Get the text for the \#th item in a list box. Only works on list boxes. Use of ,y is optional and allows selection of the column of the window to get text from. |
| [_int_](datatype-int.md) | **List\[**text**,**y**\]** | Find an item in a list box by partial match \(use **window.List\[**=text**\]** for exact\). Only works on list boxes. Use of ,y is optional and allows selection of the column of the window to search in. |
| [_bool_](datatype-bool.md) | **Minimized** | Returns TRUE if the window is minimized |
| [_bool_](datatype-bool.md) | **MouseOver** | Returns TRUE if the mouse is currently over the window |
| [_bool_](datatype-bool.md) | **MyTradeReady** | Have I clicked the Trade button? |
| [_string_](datatype-string.md) | **Name** | Name of window piece, _e.g._ "ChatWindow" for top level windows, or the piece name for child windows. **Note:** this is Custom UI dependent |
| _window_ | **Next** | Next sibling window |
| [_bool_](datatype-bool.md) | **Open** | Returns TRUE if the window is open |
| _window_ | **Parent** | Parent window |
| [_action_](datatype-action.md) | **RightMouseDown** | does the action of clicking the right mouse button |
| [_action_](datatype-action.md) | **RightMouseHeld** | Does the action of holding the right mouse button |
| [_action_](datatype-action.md) | **RightMouseHeldUp** | Does the action of holding the right mouse button up |
| [_action_](datatype-action.md) | **RightMouseUp** | Does the action of clicking the right mouse button up |
| [_action_](datatype-action.md) | **Select** | Selects the specified window |
| [_string_](datatype-string.md) | **ScreenID** | ScreenID of window piece. **Note:** This is _not_ Custom UI dependent, it must be the same on all UIs |
| [_bool_](datatype-bool.md) | **Siblings** | Returns TRUE if the window has siblings |
| [_int_](datatype-int.md) | **Style** | Window style code |
| [_string_](datatype-string.md) | **Text** | Window's text |
| [_string_](datatype-string.md) | **Tooltip** | TooltipReference text |
| [_string_](datatype-string.md) | **Type** | Type of window piece \(Screen for top level windows, or Listbox, Button, Gauge, Label, Editbox, Slider, etc\) |
| [_int_](datatype-int.md) | **VScrollMax** | Vertical scrollbar range |
| [_int_](datatype-int.md) | **VScrollPct** | Vertical scrollbar position in % to range from 0 to 100 |
| [_int_](datatype-int.md) | **VScrollPos** | Vertical scrollbar position |
| [_int_](datatype-int.md) | **Width** | Width in pixels |
| [_int_](datatype-int.md) | **X** | Screen X position |
| [_int_](datatype-int.md) | **Y** | Screen Y position |
| '**'**[**bool**](datatype-bool.md) | **To String** | TRUE if window exists, FALSE if not |

## Examples

`/echo ${Window[somewindow].Child[somechild].DoOpen}`

Expected Result: it will echo TRUE and open it.

`/echo ${Window[MerchantWnd].Open}`

Returns TRUE if a Merchant window is open

`/echo ${Window[windowname]}`

Returns TRUE if the WindowName exists, but doesn't have to be opened.

`/echo ${Window[MerchantWnd].Minimized}`

Returns TRUE if the Window is opened and minimized

`/echo ${Window[MerchantWnd].Child[ItemList].List[=Water Flask,2]}`

Returns the index \(int\) of Water Flask in the merchant's item list. ",2" means scan the second column, since that's where the item names are.

`${Window[TradeskillWnd].Child[RecipeList].List[=Inky Shadow Silk]}`

Find an item in the tradeskill item list box by the exact name Inky Shadow Silk

`${Window[TradeskillWnd].Child[RecipeList].List[1]}`

Get the first-column text for the 1st item in the tradeskill item list box

`${Window[tradewnd].HisTradeReady}`

Return TRUE if the other person has clicked the Trade button in the Trade Window

`${Window[tradewnd].MyTradeReady}`

Return TRUE if I have clicked the Trade button in the Trade Window \(TradeWnd\)

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Window](../top-level-objects/tlo-window.md)
* [DataType:argb](datatype-argb.md)

