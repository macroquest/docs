---
tags:
    - datatype
---
# `pet`

<!--dt-desc-start-->
Pet object
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
This type inherits members from [_spawn_](datatype-spawn.md).

/// member | int Buff[buffname]
Returns the slot number for _buffname_
///

/// member | string Buff[slot]
Prints name of the buff at the given _slot_
///

/// member | int BuffDuration[buffname]
Buff time remaining for pet buff _buffname_ in miliseconds
///

/// member | int BuffDuration[slot]
Buff time remaining for pet buff in slot _slot_ in miliseconds
///

/// member | bool Combat
Combat state
///

/// member | buff FindBuff
???
///

/// member | bool Focus
Focus state
///

/// member | bool GHold
GHold state
///

/// member | bool Hold
Hold state
///

/// member | string Name
???
///

/// member | bool ReGroup
ReGroup state
///

/// member | string Stance
Returns the pet's current stance, (e.g. FOLLOW, GUARD)
///

/// member | bool Stop
Stop state
///

/// member | spawn Target
Returns the pet's current target.
///

/// member | bool Taunt
Taunt state
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[buff]: datatype-buff.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
