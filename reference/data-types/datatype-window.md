---
tags:
    - datatype
---
# `window`

This contains data related to the specified in-game window

Windows come in many forms, but all are represented with the generic **window** type. In some of the descriptions, a **bold** window type may be specified, which defines the behavior for that type of window.

## Members


### [argb][argb] `BGColor`

:   Background color of the window.


### [bool][bool] `Checked`

:   Returns `TRUE` if the button has been checked.


### [window](datatype-window.md) `Child[name]`

:   Find a child window with the provided name.

    Parameters:

    *   `name`: Name of a child window


### [bool][bool] `Children`

:   Returns `TRUE` if the window has children.


### [window](datatype-window.md) `CurrentTab`

:   Applies to: `TabBox`

    Returns the `Page` window associated with the currently selected tab.


### [int][int] `CurrentTabIndex`

:   Applies to: `TabBox`

    Returns the index of the currently selected tab.


### [bool][bool] `Enabled`

:   Returns `TRUE` if the window is enabled.


### [window](datatype-window.md) `FirstChild`

:   Returns the first child window in the window hierarchy.


### [int][int] `GetCurSel`

:   !!! info "Deprecation Notice"

        This member is deprecated and discouraged from continued use. Please use [SelectedIndex](#int-selectedindex) instead.

    Applies to: `Combobox`, `Listbox`, `TreeView`

    Index of the currently selected/higlighted item.


### [int][int] `Height`

:   Height of the window in pixels.


### [bool][bool] `Highlighted`

:   Returns `TRUE` if the window is the currently focused window.


### [bool][bool] `HisTradeReady`

:   Returns the following data from the trade window, regardless of what the current window object is:

    Has the other person clicked the Trade button?


### [int][int] `HScrollMax`

:   Horizontal scrollbar maximum position.


### [int][int] `HScrollPct`

:   Horizontal scroll bar current position as a percentage of the maximum position as a value from 0 to 100.


### [int][int] `HScrollPos`

:   Horizontal scroll bar current position.


### [int][int] `Items`

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Number of items in the list.


### [string][string] `List[Row,Col]`

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Get text for an item in the list by the specified row and column. If the column is not provided then the first column is used.

    Parameters:

    *   `Row`: Row index of the item in the list.
    *   `Col`: _[optional]_ Column index of the item in the list.


### [int][int] `List[Text,Col]`

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Search a list for an item by text. Returns the index of the first element that matches the given text string.

    Parameters:

    *   `Text`: Text to search for. Partial match is performed. Prefix with `=` to perform an exact match.
    *   `Col`: _[optional]_ Column index of the item in the item in the list. If not provided, the first column is searched.


### [bool][bool] `Minimized`

:   Returns `TRUE` if the window is minimized.


### [bool][bool] `MouseOver`

:   Returns `TRUE` if the mouse is currently over the window.


### [bool][bool] `MyTradeReady`

:   Returns the following data from the trade window, regardless of what the current window object is:

    Have I clicked the Trade button?


### [string][string] `Name`

:   Name of the window.

    _Note: this value may be affected by custom ui._


### [window](datatype-window.md) `Next`

:   Next sibling window in the window hierarchy.


### [bool][bool] `Open`

:   Returns `TRUE` if the window is open.


### [window](datatype-window.md) `Parent`

:   Returns the parent of this window, or `NULL` if this is a top level window.


### [string][string] `ScreenID`

:   ScreenID of the window piece.

    _Note: This is **not** custom ui dependent, it must be the same on all UIs._


### [int][int] `SelectedIndex`

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Index of the currently selected/higlighted item.


### [bool][bool] `Siblings`

:   Returns `TRUE` if the window has siblings.


### [int][int] `Style`

:   Returns an integer representing the window style bit flags.


### [int][int] `TabCount`

:   Applies to: `TabBox`

    The number of tabs present in the TabBox.


### [window](datatype-window.md) `Tab[Index]`

:   Applies to: `TabBox`

    Looks up the `Page` window that matches the provided tab index in the TabBox.


### [window](datatype-window.md) `Tab[Text]`

:   Applies to: `TabBox`

    Looks up the `Page` window that matches the provided tab text in the TabBox.


### [string][string] `Text`

:   The text of the window. The actual value varies by type of window:

    *   `STMLbox`: Returns the contents of the STML.
    *   `Page`: Returns the name of the page's Tab.


### [string][string] `Tooltip`

:   The tooltip text for the window. This value comes from the window's TooltipReference.


### [string][string] `Type`

:   The window's type. The type will determine the behavior of some of the other members.

    Can be one of:

    * `Screen`
    * `Listbox`
    * `Gauge`
    * `SpellGem`
    * `InvSlot`
    * `Editbox`
    * `Slider`
    * `Label`
    * `STMLbox`
    * `TreeView`
    * `Combobox`
    * `Page`
    * `TabBox`
    * `LayoutBox`
    * `HorizontalLayoutBox`
    * `VerticalLayoutBox`
    * `FinderBox`
    * `TileLayoutBox`
    * `Screen`
    * `HotButton`


### [int][int] `VScrollMax`

:   Vertical scrollbar maximum position.


### [int][int] `VScrollPct`

:   Vertical scroll bar current position as a percentage of the maximum position as a value from 0 to 100.


### [int][int] `VScrollPos`

:   Vertical scroll bar current position.


### [int][int] `Width`

:   Width of the window in pixels.


### [int][int] `X`

:   The X coordinate of the window's position, in pixels.


### [int][int] `Y`

:   The Y coordinate of the window's position, in pixels.


### [string][string] To String

:   `TRUE` if the window is open, `FALSE` if not, matching [Open](#bool-open)


## Methods


### `DoClose`

:   Close the window. Has the effect of hiding the window if it closed.


### `DoOpen`

:   Open the window. Has the effect of showing the window if it is hidden.


### `LeftMouseDown`

:   Send a `leftmousedown` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `LeftMouseHeld`

:   Send a `leftmouseheld` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.

### `LeftMouseHeldUp`

:   Send a `leftmouseheldup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `LeftMouseUp`

:   Send a `leftmouseup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `Move[X,Y,Width,Height]`

:   Move or resize the window.

### `RightMouseDown`

:   Send a `rightmousedown` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `RightMouseHeld`

:   Send a `rightmouseheld` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `RightMouseHeldUp`

:   Send a `rightmouseheldup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `RightMouseUp`

:   Send a `rightmouseup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### `Select[Index]`

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Selects the specified item in the list.

    Parameters:

    *   `Index`: The number index of the item to select


### `SetAlpha[Alpha]`

:   Set the alpha value for the window.

    Parameters:
    
    *   `Alpha`: The alpha value, a number between 0 and 255.


### `SetBGColor[Color]`

:   Set the background color.

    Parameters:
    
    *   `Color`: A hex string in the form "AARRGGBB"


### `SetCurrentTab[Index]`

:   Applies to: `TabBox`.

    Changes the current tab of the tab box.

    Parameters:

    *   `Index`: Either the text or the index of the tab to select. If text is provided, it is case insensitive.


### `SetFadeAlpha[Alpha]`

:   Set the faded alpha value for the window.

    Parameters:

    *   `Alpha`: The alpha value, a number between 0 and 255.


### `SetText[Text]`

:   Applies to: `EditBox`

    Changes the current text value of the edit box.

    Parameters:

    *   `Text`: The text to set to the edit box.


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


[argb]: datatype-argb.md
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
