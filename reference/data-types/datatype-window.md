---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `window`

This contains data related to the specified in-game window

Windows come in many forms, but all are represented with the generic **window** type. In some of the descriptions, a **bold** window type may be specified, which defines the behavior for that type of window.

## Members

| **Type**                           | **Member**                      | **Description**                                                                                                                                                                                          |
| ---------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [_argb_](datatype-argb.md)         | **BGColor**                     | Background color                                                                                                                                                                                         |
| [_bool_](datatype-bool.md)         | **Checked**                     | Returns TRUE if the button has been checked                                                                                                                                                              |
| [_window_](datatype-window.md)     | **Child**[_name_]               | Find a child window with the provided name                                                                                                                                                               |
| [_bool_](datatype-bool.md)         | **Children**                    | Returns TRUE if the window has children                                                                                                                                                                  |
| [_window_](datatype-window.md)     | **CurrentTab**                  | `TabBox`: Returns the `Page` window associated with the currently selected tab.                                                                                                                          |
| [_int_](datatype-int.md)           | **CurrentTabIndex**             | `TabBox`: Returns the index of the currently selected tab.                                                                                                                                               |
| [_bool_](datatype-bool.md)         | **Enabled**                     | Returns TRUE if the window is enabled                                                                                                                                                                    |
| [_window_](datatype-window.md)     | **FirstChild**                  | First child window                                                                                                                                                                                       |
| [_int_](datatype-int.md)           | **GetCurSel**                   | Index of the currently selected/highlighted item in a list or treeview                                                                                                                                   |
| [_int_](datatype-int.md)           | **Height**                      | Height in pixels                                                                                                                                                                                         |
| [_bool_](datatype-bool.md)         | **Highlighted**                 | Returns TRUE if the window is highlighted                                                                                                                                                                |
| [_bool_](datatype-bool.md)         | **HisTradeReady**               | Has the other person clicked the Trade button?                                                                                                                                                           |
| [_int_](datatype-int.md)           | **HScrollMax**                  | Horizontal scrollbar range                                                                                                                                                                               |
| [_int_](datatype-int.md)           | **HScrollPos**                  | Horizontal scrollbar position                                                                                                                                                                            |
| [_int_](datatype-int.md)           | **HScrollPct**                  | Horizontal scrollbar position in % to range from 0 to 100                                                                                                                                                |
| [_int_](datatype-int.md)           | **Items**                       | Number of items in a Listbox or Combobox                                                                                                                                                                 |
| [_string_](datatype-string.md)     | **List**[_N_,_y_]               | Get the text for the _Nth_ item in a list box. Only works on list boxes. Use of _y_ is optional and allows selection of the column of the window to get text from.                                       |
| [_int_](datatype-int.md)           | **List**[_text_,_y_]            | Find an item in a list box by partial match (use **window.List**[=_text_] for exact). Only works on list boxes. Use of _y_ is optional and allows selection of the column of the window to search in.    |
| [_bool_](datatype-bool.md)         | **Minimized**                   | Returns TRUE if the window is minimized                                                                                                                                                                  |
| [_bool_](datatype-bool.md)         | **MouseOver**                   | Returns TRUE if the mouse is currently over the window                                                                                                                                                   |
| [_bool_](datatype-bool.md)         | **MyTradeReady**                | Have I clicked the Trade button?                                                                                                                                                                         |
| [_string_](datatype-string.md)     | **Name**                        | Name of window piece, _e.g._ "ChatWindow" for top level windows, or the piece name for child windows.<br/><br/>_Note: this is custom ui dependent_                                                       |
| [_window_](datatype-window.md)     | **Next**                        | Next sibling window                                                                                                                                                                                      |
| [_bool_](datatype-bool.md)         | **Open**                        | Returns TRUE if the window is open                                                                                                                                                                       |
| [_window_](datatype-window.md)     | **Parent**                      | Parent window                                                                                                                                                                                            |
| [_string_](datatype-string.md)     | **ScreenID**                    | ScreenID of window piece.<br/><br/>_Note: This is **not** custom ui dependent, it must be the same on all UIs_                                                                                           |
| [_bool_](datatype-bool.md)         | **Siblings**                    | Returns TRUE if the window has siblings                                                                                                                                                                  |
| [_int_](datatype-int.md)           | **Style**                       | Window style code                                                                                                                                                                                        |
| [_int_](datatype-int.md)           | **TabCount**                    | `TabBox`: The number of tabs present in the TabBox.                                                                                                                                                      |
| [_window_](datatype-window.md)     | **Tab** [_#/Name_]              | `TabBox`: Looks up the `Page` window that matches the provided index or tab text.                                                                                                                        |
| [_string_](datatype-string.md)     | **Text**                        | Window's text.<br/><br/>`STMLBox`: returns the contents of the STML.<br/>`Page`: returns the name of the page's Tab.                                                                                     |
| [_string_](datatype-string.md)     | **Tooltip**                     | TooltipReference text                                                                                                                                                                                    |
| [_string_](datatype-string.md)     | **Type**                        | Type of window piece (Screen for top level windows, or Listbox, Button, Gauge, Label, Editbox, Slider, etc)                                                                                              |
| [_int_](datatype-int.md)           | **VScrollMax**                  | Vertical scrollbar range                                                                                                                                                                                 |
| [_int_](datatype-int.md)           | **VScrollPct**                  | Vertical scrollbar position in % to range from 0 to 100                                                                                                                                                  |
| [_int_](datatype-int.md)           | **VScrollPos**                  | Vertical scrollbar position                                                                                                                                                                              |
| [_int_](datatype-int.md)           | **Width**                       | Width in pixels                                                                                                                                                                                          |
| [_int_](datatype-int.md)           | **X**                           | Screen X position                                                                                                                                                                                        |
| [_int_](datatype-int.md)           | **Y**                           | Screen Y position                                                                                                                                                                                        |
| [_string_](datatype-string.md)     | **To String**                   | TRUE if window exists, FALSE if not                                                                                                                                                                      |

## Methods

| **Name**                            | Action                                                              |
| ----------------------------------- | ------------------------------------------------------------------- |
| **DoClose**                         | Does the action of closing a window                                 |
| **DoOpen**                          | Does the action of opening a window                                 |
| **LeftMouseDown**                   | Does the action of clicking the left mouse button down              |
| **LeftMouseHeld**                   | Does the action of holding the left mouse button                    |
| **LeftMouseHeldUp**                 | does the action of holding the left mouse button up                 |
| **LeftMouseUp**                     | Does the action of clicking the left mouse button up                |
| **RightMouseDown**                  | does the action of clicking the right mouse button                  |
| **RightMouseHeld**                  | Does the action of holding the right mouse button                   |
| **RightMouseHeldUp**                | Does the action of holding the right mouse button up                |
| **RightMouseUp**                    | Does the action of clicking the right mouse button up               |
| **Select**                          | Selects the specified window                                        |
| **SetCurrentTab** [ _# or Name_ ]   | If the window is a TabBox, set the current tab by index or by name. |

## Usage

`/invoke ${Window[MerchantWnd].DoOpen}`

Expected Result: the Merchant window window appears

`/echo ${Window[MerchantWnd].Open}`

Returns TRUE if a Merchant window is open

`/echo ${Window[windowname]}`

Returns TRUE if the WindowName exists, but doesn't have to be opened.

`/echo ${Window[MerchantWnd].Minimized}`

Returns TRUE if the Window is opened and minimized

`/echo ${Window[MerchantWnd/ItemList].List[=Water Flask,2]}`

Returns the index (int) of Water Flask in the merchant's item list. ",2" means scan the second column, since that's where the item names are.

`${Window[TradeskillWnd/RecipeList].List[=Inky Shadow Silk]}`

Find an item in the tradeskill item list box by the exact name Inky Shadow Silk

`${Window[TradeskillWnd/RecipeList].List[1]}`

Get the first-column text for the 1st item in the tradeskill item list box

`${Window[tradewnd].HisTradeReady}`

Return TRUE if the other person has clicked the Trade button in the Trade Window

`${Window[tradewnd].MyTradeReady}`

Return TRUE if I have clicked the Trade button in the Trade Window (TradeWnd)

`${Window[RewardSelectionWnd/RewardPageTabWindow].Tab[Brew for the Day].Child[RewardSelectionOptionList].List[2]}`

Returns the name of the 2nd option in the list of rewards for the tab titled "Brew for the Day"
