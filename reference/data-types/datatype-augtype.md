---
tags:
    - datatype
---
# `augtype` Type

<!--dt-desc-start-->
Describes data about an augmentation slot in an item.
<!--dt-desc-end-->

## Members
<!--dt-members-start-->
/// member | bool Empty
True if the slot is empty
///

/// member | bool Infusable
True if this is a hidden energeian power source slot.
///

/// member | item Item
The item socketed in this slot, if any.
///

/// member | string Name
The name of the item socketed in this slot, if any.
///

/// member | int Slot
Index of the augment slot.
///

/// member | int Solvent
Item ID of the solvent used to remove this item, if any.
///

/// member | int Type
Type of augment slot.
///

/// member | int Visible
True if this slot is visible to the user.
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: ./datatype-int.md
[bool]: ./datatype-bool.md
[string]: ./datatype-string.md
[item]: ./datatype-item.md
<!--dt-linkrefs-end-->
