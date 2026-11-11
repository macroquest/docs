---
tags:
    - datatype
---
# `advlootitem`

<!--dt-desc-start-->
Represents a discrete item being looted in an AdvLoot window.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool AlwaysGreed
The Always Greed (AG) state of the item.
///

/// member | bool AlwaysNeed
The Always Need (AN) state of the item.
///

/// member | bool AutoRoll
The Auto Roll state (dice icon) of the item.
///

/// member | spawn Corpse
The spawn representing the corpse that is being looted, if available.
///

/// member | bool FreeGrab
Indicates that the item is free grab.
///

/// member | bool Greed
The Greed (GD) state of the item.
///

/// member | int IconID
The ID of the icon for the item.
///

/// member | int64 ID
The ID of the item.
///

/// member | int Index
The positional index of the item.
///

/// member | string Name
The name of the item.
///

/// member | bool Need
The Need (ND) state of the item.
///

/// member | bool Never
The Never (NV) state of the item.
///

/// member | bool No
The No state of the item.
///

/// member | bool NoDrop
Indicates if the item is NO DROP.
///

/// member | int StackSize
The size of the stack of items being looted.
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end--> 