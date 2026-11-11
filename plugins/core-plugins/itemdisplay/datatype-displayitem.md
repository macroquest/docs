---
tags:
   - datatype
---
# `displayitem`

<!--dt-desc-start-->
Holds members that can control and return status on item display windows. This datatype inherits all members from the **[item]** datatype.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | string Info
Returns details from the item. Note that this is different from the "Information" member.
///

/// member | string WindowTitle
Returns the title of the window
///

/// member | string AdvancedLore
Displays lore text
///

/// member | string MadeBy
Displays the maker of the crafted item
///

/// member | bool Collected
///

/// member | bool CollectedReceived
///

/// member | bool Scribed
///

/// member | bool ScribedReceived
///

/// member | string Information
Returns the "item information" text from the item window.
///

/// member | int DisplayIndex
Shows the index number of the item window
///

/// member | window Window
Gives access to the **[window]** datatype, allowing you to do things like `/invoke ${DisplayItem[5].Window.DoClose}`
///

/// member | item Item
Gives access to the **[item]** datatype, although its members are already inherited. e.g. `/echo ${DisplayItem[2].Item.HP}`
///

/// member | DisplayItem Next
///
<!--dt-members-end-->

<!--dt-linkrefs-start-->
[DisplayItem]: datatype-displayitem.md
[bool]: ../../../reference/data-types/datatype-bool.md
[int]: ../../../reference/data-types/datatype-int.md
[item]: ../../../reference/data-types/datatype-item.md
[string]: ../../../reference/data-types/datatype-string.md
[window]: ../../../reference/data-types/datatype-window.md
<!--dt-linkrefs-end-->
