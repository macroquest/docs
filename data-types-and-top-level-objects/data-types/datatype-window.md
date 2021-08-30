# DataType:window

This contains data related to the specified in-game window

Windows come in many forms, but all are represented with the generic **window** type. In some of the descriptions, a **bold** window type may be specified, which defines the behavior for that type of window.

## Members

<table>
  <thead>
    <tr>
      <th style="text-align:left"><b>Type</b>
      </th>
      <th style="text-align:left"><b>Member</b>
      </th>
      <th style="text-align:left"><b>Description</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><a href="datatype-argb.md"><em>argb</em></a>
      </td>
      <td style="text-align:left"><b>BGColor</b>
      </td>
      <td style="text-align:left">Background color</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Checked</b>
      </td>
      <td style="text-align:left">Returns TRUE if the button has been checked</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-window.md"><em>window</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Child[ </b><em>name</em><b> ]</b>
        </td>
        <td style="text-align:left">Find a child window with the provided name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Children</b>
      </td>
      <td style="text-align:left">Returns TRUE if the window has children</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-window.md"><em>window</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>CurrentTab</b>
        </td>
        <td style="text-align:left"><b>TabBox:</b> Returns the <b>Page</b> window associated with the currently
          selected tab.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentTabIndex</b>
      </td>
      <td style="text-align:left"><b>TabBox</b>: Returns the index of the currently selected tab.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Enabled</b>
      </td>
      <td style="text-align:left">Returns TRUE if the window is enabled</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-window.md"><em>window</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>FirstChild</b>
        </td>
        <td style="text-align:left">First child window</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GetCurSel</b>
      </td>
      <td style="text-align:left">Index of the currently selected/highlighted item in a list or treeview</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Height</b>
      </td>
      <td style="text-align:left">Height in pixels</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Highlighted</b>
      </td>
      <td style="text-align:left">Returns TRUE if the window is highlighted</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>HisTradeReady</b>
      </td>
      <td style="text-align:left">Has the other person clicked the Trade button?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HScrollMax</b>
      </td>
      <td style="text-align:left">Horizontal scrollbar range</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HScrollPos</b>
      </td>
      <td style="text-align:left">Horizontal scrollbar position</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HScrollPct</b>
      </td>
      <td style="text-align:left">Horizontal scrollbar position in % to range from 0 to 100</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Items</b>
      </td>
      <td style="text-align:left">Number of items in a Listbox or Combobox</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>List[ </b>#<b>, </b>y<em><b> </b></em><b>]</b>
        </td>
        <td style="text-align:left">Get the text for the <code>#</code>th item in a list box. Only works on
          list boxes. Use of <code>y</code> is optional and allows selection of the
          column of the window to get text from.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>List[ </b>text<b>, </b>y<b> ]</b>
      </td>
      <td style="text-align:left">Find an item in a list box by partial match (use <b>window.List[</b>=text<b>]</b> for
        exact). Only works on list boxes. Use of <code>y</code> is optional and allows
        selection of the column of the window to search in.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Minimized</b>
      </td>
      <td style="text-align:left">Returns TRUE if the window is minimized</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>MouseOver</b>
      </td>
      <td style="text-align:left">Returns TRUE if the mouse is currently over the window</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>MyTradeReady</b>
      </td>
      <td style="text-align:left">Have I clicked the Trade button?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Name</b>
        </td>
        <td style="text-align:left">
          <p>Name of window piece, <em>e.g.</em> &quot;ChatWindow&quot; for top level
            windows, or the piece name for child windows.</p>
          <p>&lt;b&gt;&lt;/b&gt;</p>
          <p><b>Note:</b> this is Custom UI dependent</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-window.md"><em>window</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Next</b>
        </td>
        <td style="text-align:left">Next sibling window</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Open</b>
      </td>
      <td style="text-align:left">Returns TRUE if the window is open</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-window.md"><em>window</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Parent</b>
        </td>
        <td style="text-align:left">Parent window</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>ScreenID</b>
        </td>
        <td style="text-align:left">
          <p>ScreenID of window piece.</p>
          <p>&lt;b&gt;&lt;/b&gt;</p>
          <p><b>Note:</b> This is <em>not</em> Custom UI dependent, it must be the same
            on all UIs</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Siblings</b>
      </td>
      <td style="text-align:left">Returns TRUE if the window has siblings</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Style</b>
      </td>
      <td style="text-align:left">Window style code</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>TabCount</b>
      </td>
      <td style="text-align:left"><b>TabBox:</b> The number of tabs present in the TabBox.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-window.md"><em>window</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Tab[ </b># or Name <b>]</b>
        </td>
        <td style="text-align:left"><b>TabBox:</b> Looks up the <b>Page</b> window that matches the provided
          index or tab text.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Text</b>
        </td>
        <td style="text-align:left">
          <p>Window&apos;s text.</p>
          <p></p>
          <p><b>STMLBox:</b> returns the contents of the STML.</p>
          <p><b>Page</b>: returns the name of the page&apos;s Tab.</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Tooltip</b>
        </td>
        <td style="text-align:left">TooltipReference text</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Type</b>
        </td>
        <td style="text-align:left">Type of window piece (Screen for top level windows, or Listbox, Button,
          Gauge, Label, Editbox, Slider, etc)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>VScrollMax</b>
      </td>
      <td style="text-align:left">Vertical scrollbar range</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>VScrollPct</b>
      </td>
      <td style="text-align:left">Vertical scrollbar position in % to range from 0 to 100</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>VScrollPos</b>
      </td>
      <td style="text-align:left">Vertical scrollbar position</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Width</b>
      </td>
      <td style="text-align:left">Width in pixels</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>X</b>
      </td>
      <td style="text-align:left">Screen X position</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Y</b>
      </td>
      <td style="text-align:left">Screen Y position</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>To String</b>
        </td>
        <td style="text-align:left">TRUE if window exists, FALSE if not</td>
    </tr>
  </tbody>
</table>

## Methods

| **Name** | Action |
| :--- | :--- |
| **DoClose** | Does the action of closing a window |
| **DoOpen** | Does the action of opening a window |
| **LeftMouseDown** | Does the action of clicking the left mouse button down |
| **LeftMouseHeld** | Does the action of holding the left mouse button |
| **LeftMouseHeldUp** | does the action of holding the left mouse button up |
| **LeftMouseUp** | Does the action of clicking the left mouse button up |
| **RightMouseDown** | does the action of clicking the right mouse button |
| **RightMouseHeld** | Does the action of holding the right mouse button |
| **RightMouseHeldUp** | Does the action of holding the right mouse button up |
| **RightMouseUp** | Does the action of clicking the right mouse button up |
| **Select** | Selects the specified window |
| **SetCurrentTab\[** \# or Name **\]** | If the window is a TabBox, set the current tab by index or by name. |

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

