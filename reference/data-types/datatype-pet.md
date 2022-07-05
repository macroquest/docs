---
tags:
    - datatype
---
# `pet`

Pet object

## Members

This type inherits members from [_spawn_](datatype-spawn.md).

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Buff**[_buffname_] | Returns the slot number for _buffname_ |
| [_string_](datatype-string.md) | **Buff**[_slot_] | Prints name of the buff at the given _slot_ |
| [_int_](datatype-int.md) | **BuffDuration**[_buffname_] | Buff time remaining for pet buff _buffname_ in miliseconds |
| [_int_](datatype-int.md) | **BuffDuration**[_slot_] | Buff time remaining for pet buff in slot _slot_ in miliseconds |
| [_bool_](datatype-bool.md) | **Combat** | Combat state |
| | **FindBuff** | |
| [_bool_](datatype-bool.md) | **Focus** | Focus state |
| [_bool_](datatype-bool.md) | **GHold** | GHold state |
| [_bool_](datatype-bool.md) | **Hold** | Hold state |
| | **Name** | |
| [_bool_](datatype-bool.md) | **ReGroup** | ReGroup state |
| [_string_](datatype-string.md) | **Stance** | Returns the pet's current stance, (e.g. FOLLOW, GUARD) |
| [_bool_](datatype-bool.md) | **Stop** | Stop state |
| [_spawn_](datatype-spawn.md) | **Target** | Returns the pet's current target. |
| [_bool_](datatype-bool.md) | **Taunt** | Taunt state |
