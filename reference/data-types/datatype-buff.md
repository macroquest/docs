---
tags:
    - datatype
---
# `buff`

This is the type for any buffs currently affecting you, both long duration and short duration buffs.

## Members

This type inherits members from [_spell_](datatype-spell.md).

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **Caster** | Name of the caster who cast the buff, if available. |
| [_int64_](datatype-int64.md) | **CountersCorruption** | The number of corruption counters. |
| [_int64_](datatype-int64.md) | **CountersCurse** | The number of curse counters. |
| [_int64_](datatype-int64.md) | **CountersDisease** | The number of disease counters. |
| [_int64_](datatype-int64.md) | **CountersPoison** | The number of poison counters. |
| [_int64_](datatype-int64.md) | **Dar** | The remaining damage absorption of the buff (if any). _This is not entirely accurate, it will only show you to the Dar of your spell when it was initially cast, or what it was when you last zoned (whichever is more recent)._ |
| [_ticks_](datatype-ticks.md) | **Duration** | The time remaining before the buff fades (not total duration) |
| [_int_](datatype-int.md) | **HitCount** | |
| [_int_](datatype-int.md) | **ID** | The ID of the buff or shortbuff slot |
| [_int_](datatype-int.md) | **Level** | The level of the person that cast the buff on you (not the level of the spell) |
| [_float_](datatype-float.md) | **Mod** | The modifier to a bard song |
| [_spell_](datatype-spell.md) | **Spell** | The spell |
| [_int64_](datatype-int64.md) | **TotalCounters** | The total number of counters on the buff. |
| [_string_](datatype-string.md) | **To String** | Same as Name |

## Methods

| Name | Action |
| :--- | :--- |
| **Remove** | Removes the named/partial name buff |

## Examples

!!! Example

    === "MQScript"

        Remove the buff named "Credence"

        ```
        /invoke ${Me.Buff[Credence].Remove}
        ```
    
    === "Lua"

        Remove the buff named "Crerdence"

        ```lua
        mq.TLO.Me.Buff("Credence").Remove()
        ```

