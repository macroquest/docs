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
### {{ renderMember(type='argb', name='BGColor') }}

:   Background color of the window.


### {{ renderMember(type='bool', name='Checked') }}

:   Returns `TRUE` if the button has been checked.

### {{ renderMember(type='window', name='Child', params='name') }}

:   Find a child window with the provided name.

    Parameters:

    *   `name`: Name of a child window


### {{ renderMember(type='bool', name='Children') }}

:   Returns `TRUE` if the window has children.


### {{ renderMember(type='window', name='CurrentTab') }}

:   Applies to: `TabBox`

    Returns the `Page` window associated with the currently selected tab.


### {{ renderMember(type='int', name='CurrentTabIndex') }}

:   Applies to: `TabBox`

    Returns the index of the currently selected tab.


### {{ renderMember(type='bool', name='Enabled') }}

:   Returns `TRUE` if the window is enabled.

### {{ renderMember(type='window', name='FirstChild') }}

:   Returns the first child window in the window hierarchy.


### {{ renderMember(type='int', name='GetCurSel') }}

:   !!! info "Deprecation Notice"

        This member is deprecated and discouraged from continued use. Please use [SelectedIndex](#int-selectedindex) instead.

    Applies to: `Combobox`, `Listbox`, `TreeView`

    Index of the currently selected/higlighted item.


### {{ renderMember(type='int', name='Height') }}

:   Height of the window in pixels.


### {{ renderMember(type='bool', name='Highlighted') }}

:   Returns `TRUE` if the window is the currently focused window.


### {{ renderMember(type='bool', name='HisTradeReady') }}

:   Returns the following data from the trade window, regardless of what the current window object is:

    Has the other person clicked the Trade button?

### {{ renderMember(type='hotbuttonwindow', name='HotButton') }}

:   Applies to: `HotButton`

    Returns the HotButton associated with this window object.

### {{ renderMember(type='int', name='HScrollMax') }}

:   Horizontal scrollbar maximum position.


### {{ renderMember(type='int', name='HScrollPct') }}

:   Horizontal scroll bar current position as a percentage of the maximum position as a value from 0 to 100.


### {{ renderMember(type='int', name='HScrollPos') }}

:   Horizontal scroll bar current position.

### {{ renderMember(type='invslotwindow', name='InvSlot') }}

:   Applies to: `InvSlot`

    Returns the InvSlot associated with this window object.


### {{ renderMember(type='int', name='Items') }}

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Number of items in the list.


### {{ renderMember(type='string', name='List', params='Row,Col') }}

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Get text for an item in the list by the specified row and column. If the column is not provided then the first column is used.

    Parameters:

    *   `Row`: Row index of the item in the list.
    *   `Col`: _[optional]_ Column index of the item in the list.


### {{ renderMember(type='int', name='List', params='Text,Col') }}

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Search a list for an item by text. Returns the index of the first element that matches the given text string.

    Parameters:

    *   `Text`: Text to search for. Partial match is performed. Prefix with `=` to perform an exact match.
    *   `Col`: _[optional]_ Column index of the item in the item in the list. If not provided, the first column is searched.


### {{ renderMember(type='bool', name='Minimized') }}

:   Returns `TRUE` if the window is minimized.


### {{ renderMember(type='bool', name='MouseOver') }}

:   Returns `TRUE` if the mouse is currently over the window.


### {{ renderMember(type='bool', name='MyTradeReady') }}

:   Returns the following data from the trade window, regardless of what the current window object is:

    Have I clicked the Trade button?


### {{ renderMember(type='string', name='Name') }}

:   Name of the window.

    _Note: this value may be affected by custom ui._


### {{ renderMember(type='window', name='Next') }}

:   Next sibling window in the window hierarchy.


### {{ renderMember(type='bool', name='Open') }}

:   Returns `TRUE` if the window is open.


### {{ renderMember(type='window', name='Parent') }}

:   Returns the parent of this window, or `NULL` if this is a top level window.


### {{ renderMember(type='string', name='ScreenID') }}

:   ScreenID of the window piece.

    _Note: This is **not** custom ui dependent, it must be the same on all UIs._


### {{ renderMember(type='int', name='SelectedIndex') }}

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Index of the currently selected/higlighted item.


### {{ renderMember(type='bool', name='Siblings') }}

:   Returns `TRUE` if the window has siblings.

### {{ renderMember(type='string', name='Size') }}

:   Returns the size of the window in the form of `width,height`.

### {{ renderMember(type='int', name='Style') }}

:   Returns an integer representing the window style bit flags.


### {{ renderMember(type='int', name='TabCount') }}

:   Applies to: `TabBox`

    The number of tabs present in the TabBox.


### {{ renderMember(type='window', name='Tab', params='Index') }}

:   Applies to: `TabBox`

    Looks up the `Page` window that matches the provided tab index in the TabBox.


### {{ renderMember(type='window', name='Tab', params='Text') }}

:   Applies to: `TabBox`

    Looks up the `Page` window that matches the provided tab text in the TabBox.


### {{ renderMember(type='string', name='Text') }}

:   The text of the window. The actual value varies by type of window:

    *   `STMLbox`: Returns the contents of the STML.
    *   `Page`: Returns the name of the page's Tab.


### {{ renderMember(type='string', name='Tooltip') }}

:   The tooltip text for the window. This value comes from the window's TooltipReference.


### {{ renderMember(type='string', name='Type') }}

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


### {{ renderMember(type='int', name='VScrollMax') }}

:   Vertical scrollbar maximum position.


### {{ renderMember(type='int', name='VScrollPct') }}

:   Vertical scroll bar current position as a percentage of the maximum position as a value from 0 to 100.


### {{ renderMember(type='int', name='VScrollPos') }}

:   Vertical scroll bar current position.


### {{ renderMember(type='int', name='Width') }}

:   Width of the window in pixels.

### {{ renderMember(type='float', name='Value') }}

:

### {{ renderMember(type='int', name='X') }}

:   The X coordinate of the window's position, in pixels.


### {{ renderMember(type='int', name='Y') }}

:   The Y coordinate of the window's position, in pixels.


### [string][string] To String

:   `TRUE` if the window is open, `FALSE` if not, matching [Open](#bool-open)
<!--dt-members-end-->

## Methods


### {{ renderMember(name='DoClose') }}

:   Close the window. Has the effect of hiding the window if it closed.


### {{ renderMember(name='DoOpen') }}

:   Open the window. Has the effect of showing the window if it is hidden.


### {{ renderMember(name='LeftMouseDown') }}

:   Send a `leftmousedown` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='LeftMouseHeld') }}

:   Send a `leftmouseheld` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.

### {{ renderMember(name='LeftMouseHeldUp') }}

:   Send a `leftmouseheldup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='LeftMouseUp') }}

:   Send a `leftmouseup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='Move', params='X,Y,Width,Height') }}

:   Move or resize the window.

### {{ renderMember(name='RightMouseDown') }}

:   Send a `rightmousedown` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='RightMouseHeld') }}

:   Send a `rightmouseheld` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='RightMouseHeldUp') }}

:   Send a `rightmouseheldup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='RightMouseUp') }}

:   Send a `rightmouseup` event to the window.

    Has the same effect as using the [/notify](../commands/notify.md) command on the window.


### {{ renderMember(name='Select', params='Index') }}

:   Applies to: `Combobox`, `Listbox`, `TreeView`

    Selects the specified item in the list.

    Parameters:

    *   `Index`: The number index of the item to select


### {{ renderMember(name='SetAlpha', params='Alpha') }}

:   Set the alpha value for the window.

    Parameters:

    *   `Alpha`: The alpha value, a number between 0 and 255.


### {{ renderMember(name='SetBGColor', params='Color') }}

:   Set the background color.

    Parameters:

    *   `Color`: A hex string in the form "AARRGGBB"


### {{ renderMember(name='SetCurrentTab', params='Index') }}

:   Applies to: `TabBox`.

    Changes the current tab of the tab box.

    Parameters:

    *   `Index`: Either the text or the index of the tab to select. If text is provided, it is case insensitive.


### {{ renderMember(name='SetFadeAlpha', params='Alpha') }}

:   Set the faded alpha value for the window.

    Parameters:

    *   `Alpha`: The alpha value, a number between 0 and 255.


### {{ renderMember(name='SetText', params='Text') }}

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
