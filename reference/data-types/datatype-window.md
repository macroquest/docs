---
tags:
    - datatype
---
# `window`

<!--dt-desc-start-->
This contains data related to the specified in-game window

Windows come in many forms, but all are represented with the generic **window** type. In some of the descriptions, a **bold** window type may be specified, which defines the behavior for that type of window.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | argb BGColor
Background color of the window.
///


/// member | bool Checked
Returns `TRUE` if the button has been checked.
///

/// member | window Child[name]
Find a child window with the provided name.

Parameters:

*   `name`: Name of a child window
///


/// member | bool Children
Returns `TRUE` if the window has children.
///


/// member | window CurrentTab
Applies to: `TabBox`

Returns the `Page` window associated with the currently selected tab.
///


/// member | int CurrentTabIndex
Applies to: `TabBox`

Returns the index of the currently selected tab.
///


/// member | bool Enabled
Returns `TRUE` if the window is enabled.
///

/// member | window FirstChild
Returns the first child window in the window hierarchy.
///


/// member | int GetCurSel
!!! info "Deprecation Notice"

    This member is deprecated and discouraged from continued use. Please use [SelectedIndex](#SelectedIndex) instead.

Applies to: `Combobox`, `Listbox`, `TreeView`

Index of the currently selected/higlighted item.
///


/// member | int Height
Height of the window in pixels.
///


/// member | bool Highlighted
Returns `TRUE` if the window is the currently focused window.
///


/// member | bool HisTradeReady
Returns the following data from the trade window, regardless of what the current window object is:

Has the other person clicked the Trade button?
///

/// member | hotbuttonwindow HotButton
Applies to: `HotButton`

Returns the HotButton associated with this window object.
///

/// member | int HScrollMax
Horizontal scrollbar maximum position.
///


/// member | int HScrollPct
Horizontal scroll bar current position as a percentage of the maximum position as a value from 0 to 100.
///


/// member | int HScrollPos
Horizontal scroll bar current position.
///

/// member | invslotwindow InvSlot
Applies to: `InvSlot`

Returns the InvSlot associated with this window object.
///


/// member | int Items
Applies to: `Combobox`, `Listbox`, `TreeView`

Number of items in the list.
///


/// member | string List[Row,Col]
Applies to: `Combobox`, `Listbox`, `TreeView`

Get text for an item in the list by the specified row and column. If the column is not provided then the first column is used.

Parameters:

*   `Row`: Row index of the item in the list.
*   `Col`: _[optional]_ Column index of the item in the list.
///


/// member | int List[Text,Col]
Applies to: `Combobox`, `Listbox`, `TreeView`

Search a list for an item by text. Returns the index of the first element that matches the given text string.

Parameters:

*   `Text`: Text to search for. Partial match is performed. Prefix with `=` to perform an exact match.
*   `Col`: _[optional]_ Column index of the item in the item in the list. If not provided, the first column is searched.
///


/// member | bool Minimized
Returns `TRUE` if the window is minimized.
///


/// member | bool MouseOver
Returns `TRUE` if the mouse is currently over the window.
///


/// member | bool MyTradeReady
Returns the following data from the trade window, regardless of what the current window object is:

Have I clicked the Trade button?
///


/// member | string Name
Name of the window.

_Note: this value may be affected by custom ui._
///


/// member | window Next
Next sibling window in the window hierarchy.
///


/// member | bool Open
Returns `TRUE` if the window is open.
///


/// member | window Parent
Returns the parent of this window, or `NULL` if this is a top level window.
///


/// member | string ScreenID
ScreenID of the window piece.

_Note: This is **not** custom ui dependent, it must be the same on all UIs._
///


/// member | int SelectedIndex
Applies to: `Combobox`, `Listbox`, `TreeView`

Index of the currently selected/higlighted item.
///


/// member | bool Siblings
Returns `TRUE` if the window has siblings.
///

/// member | string Size
Returns the size of the window in the form of `width,height`.
///

/// member | int Style
Returns an integer representing the window style bit flags.
///


/// member | int TabCount
Applies to: `TabBox`

The number of tabs present in the TabBox.
///


/// member | window Tab[Index]
Applies to: `TabBox`

Looks up the `Page` window that matches the provided tab index in the TabBox.
///


/// member | window Tab[Text]
Applies to: `TabBox`

Looks up the `Page` window that matches the provided tab text in the TabBox.
///


/// member | string Text
The text of the window. The actual value varies by type of window:

*   `STMLbox`: Returns the contents of the STML.
*   `Page`: Returns the name of the page's Tab.
///


/// member | string Tooltip
The tooltip text for the window. This value comes from the window's TooltipReference.
///


/// member | string Type
The window's type. The type will determine the behavior of some of the other members.

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
///


/// member | int VScrollMax
Vertical scrollbar maximum position.
///


/// member | int VScrollPct
Vertical scroll bar current position as a percentage of the maximum position as a value from 0 to 100.
///


/// member | int VScrollPos
Vertical scroll bar current position.
///


/// member | int Width
Width of the window in pixels.
///

/// member | float Value
///


/// member | int X
The X coordinate of the window's position, in pixels.
///


/// member | int Y
The Y coordinate of the window's position, in pixels.
///


### [string][string] To String

:   `TRUE` if the window is open, `FALSE` if not, matching [Open](#Open)
<!--dt-members-end-->

## Methods


/// member | DoClose
Close the window. Has the effect of hiding the window if it closed.
///


/// member | DoOpen
Open the window. Has the effect of showing the window if it is hidden.
///


/// member | LeftMouseDown
Send a `leftmousedown` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | LeftMouseHeld
Send a `leftmouseheld` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///

/// member | LeftMouseHeldUp
Send a `leftmouseheldup` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | LeftMouseUp
Send a `leftmouseup` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | Move[X,Y,Width,Height]
Move or resize the window.
///

/// member | RightMouseDown
Send a `rightmousedown` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | RightMouseHeld
Send a `rightmouseheld` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | RightMouseHeldUp
Send a `rightmouseheldup` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | RightMouseUp
Send a `rightmouseup` event to the window.

Has the same effect as using the [/notify](../commands/notify.md) command on the window.
///


/// member | Select[Index]
Applies to: `Combobox`, `Listbox`, `TreeView`

Selects the specified item in the list.

Parameters:

*   `Index`: The number index of the item to select
///


/// member | SetAlpha[Alpha]
Set the alpha value for the window.

Parameters:

*   `Alpha`: The alpha value, a number between 0 and 255.
///


/// member | SetBGColor[Color]
Set the background color.

Parameters:

*   `Color`: A hex string in the form "AARRGGBB"
///


/// member | SetCurrentTab[Index]
Applies to: `TabBox`.

Changes the current tab of the tab box.

Parameters:

*   `Index`: Either the text or the index of the tab to select. If text is provided, it is case insensitive.
///


/// member | SetFadeAlpha[Alpha]
Set the faded alpha value for the window.

Parameters:

*   `Alpha`: The alpha value, a number between 0 and 255.
///


/// member | SetText[Text]
Applies to: `EditBox`

Changes the current text value of the edit box.

Parameters:

*   `Text`: The text to set to the edit box.
///


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

<!--dt-linkrefs-start-->
[argb]: datatype-argb.md
[bool]: datatype-bool.md
[float]: datatype-float.md
[hotbuttonwindow]: datatype-hotbuttonwindow.md
[int]: datatype-int.md
[invslot]: datatype-invslot.md
[invslotwindow]: datatype-invslotwindow.md
[string]: datatype-string.md
[window]: datatype-window.md
<!--dt-linkrefs-end-->
