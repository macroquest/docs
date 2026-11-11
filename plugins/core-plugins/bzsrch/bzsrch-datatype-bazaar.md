---
tags:
   - datatype
---
# `bazaar`

<!--dt-desc-start-->
Datatype providing access to bazaar search results and status information.
<!--dt-desc-end-->

## Members
<!--dt-members-start-->
/// member | int Count
Number of search results available
///

/// member | bool Done
True if search operation has completed
///

/// member | bazaaritem Item[#]
Returns the name of the item at the specified index
///

/// member | bazaaritem SortedItem[#]
Returns the name of the item at the specified index from a sorted list, as you'd see it in the GUI.
///
<!--dt-members-end-->

<!--dt-linkrefs-start-->
[bazaaritem]: bzsrch-datatype-bazaaritem.md
[bool]: ../../../reference/data-types/datatype-bool.md
[int]: ../../../reference/data-types/datatype-int.md
<!--dt-linkrefs-end-->