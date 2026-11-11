---
tags:
    - datatype
---
# `itemfilterdata`

<!--dt-desc-start-->
A collection of settings that together describe the loot filter for an item.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool AutoRoll
The Auto Roll state (dice icon).
///

/// member | bool Greed
The Greed (GD) state.
///

/// member | int IconID
The ID of the icon.
///

/// member | int ID
The ID of the item.
///

/// member | string Name
The Name of the item.
///

/// member | bool Need
The Need (ND) state.
///

/// member | bool Never
The Never (NV) state.
///

/// member | int Types
Bit field representing all the loot filter flags for this item.
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end--> 