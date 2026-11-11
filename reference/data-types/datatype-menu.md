---
tags:
  - datatype
---
# `menu`

<!--dt-desc-start-->
Returns information about visible menus. Inherits [window](datatype-window.md) when a menu is open.
<!--dt-desc-end-->

## Members
<!--dt-members-start-->

/// member | int NumVisibleMenus
returns number of currently visible menus. Ordinarily this is going to be 1 if a menu is showing and 0 if not.
///

/// member | int CurrMenu
returns the index for the currently visible menu. Ordinarily this will be 0 if a menu is open and -1 if not
///

/// member | string Name
returns the name of the menu or the first item's name.
///

/// member | int NumItems
returns number of items in the currently open menu.
///

/// member | string Items[#]
returns the Itemname specified by Index
///

/// member | string To String
If no menu open, returns "No Menu Open". It returns the first menu item's name when a menu is open
///

<!--dt-members-end-->

## Methods

**Select**
:   Clicks a menu item.

## Examples
<!--dt-examples-start-->
`/invoke ${Menu.Select[open the door]}`
- Clicks the menu item "open the door"

`/echo ${Menu.Name}`

- Output: Shabby Lobby Door

`/echo ${Menu.NumItems}`

- Output: 4

`/echo ${Menu.Items[2]}`

- Output: Adjust Placement
<!--dt-examples-end-->

<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
