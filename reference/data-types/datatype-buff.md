---
tags:
    - datatype
---
# `buff`

<!--dt-desc-start-->
This is the type for any buffs currently affecting you, both long duration and short duration buffs.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
This type inherits members from [_spell_](datatype-spell.md).

/// member | string Caster
Name of the caster who cast the buff, if available.
///

/// member | int64 CountersCorruption
The number of corruption counters.
///

/// member | int64 CountersCurse
The number of curse counters.
///

/// member | int64 CountersDisease
The number of disease counters.
///

/// member | int64 CountersPoison
The number of poison counters.
///

/// member | int64 Dar
The remaining damage absorption of the buff (if any). _This is not entirely accurate, it will only show you to the Dar of your spell when it was initially cast, or what it was when you last zoned (whichever is more recent)._
///

/// member | timestamp Duration
The time remaining before the buff fades (not total duration)
///

/// member | int HitCount
?
///

/// member | int ID
The ID of the buff or shortbuff slot
///

/// member | int Level
The level of the person that cast the buff on you (not the level of the spell)
///

/// member | float Mod
The modifier to a bard song
///

/// member | spell Spell
The spell
///

/// member | int64 TotalCounters
The total number of counters on the buff.
///

### [string][string] `To String`

:   Same as Name
<!--dt-members-end-->

## Methods

| Name | Action |
| :--- | :--- |
| **Remove** | Removes the named/partial name buff |

## Examples

!!! example

    Remove the buff named "Credence"


    === "MQScript"

        ```
        /invoke ${Me.Buff[Credence].Remove}
        ```

    === "Lua"

        ```lua
        mq.TLO.Me.Buff("Credence").Remove()
        ```
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
[bool]: datatype-bool.md
[timestamp]: datatype-timestamp.md
[spell]: datatype-spell.md
[int64]: datatype-int64.md
[float]: datatype-float.md
<!--dt-linkrefs-end-->
