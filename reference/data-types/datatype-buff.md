---
tags:
    - datatype
---
# `buff`

This is the type for any buffs currently affecting you, both long duration and short duration buffs.

## Members

This type inherits members from [_spell_](datatype-spell.md).

### [string][string] `Caster`

:   Name of the caster who cast the buff, if available.

### [int64][int64] `CountersCorruption`

:   The number of corruption counters.

### [int64][int64] `CountersCurse`

:   The number of curse counters.

### [int64][int64] `CountersDisease`

:   The number of disease counters.

### [int64][int64] `CountersPoison`

:   The number of poison counters.

### [int64][int64] `Dar`

:   The remaining damage absorption of the buff (if any). _This is not entirely accurate, it will only show you to the Dar of your spell when it was initially cast, or what it was when you last zoned (whichever is more recent)._

### [timestamp][timestamp] `Duration`

:   The time remaining before the buff fades (not total duration)

### [int][int] `HitCount`

:   

### [int][int] `ID`

:   The ID of the buff or shortbuff slot

### [int][int] `Level`

:   The level of the person that cast the buff on you (not the level of the spell)

### [float][float] `Mod`

:   The modifier to a bard song

### [spell][spell] `Spell`

:   The spell

### [int64][int64] `TotalCounters`

:   The total number of counters on the buff.

### [string][string] `To String`

:   Same as Name


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

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
