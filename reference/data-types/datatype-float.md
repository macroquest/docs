---
tags:
    - datatype
---
# `float` Type

Represents a single precision (32-bit) floatiang point number.

* A floating-point number is one which has a decimal component (_e.g. 1.01_)
* Members of this DataType generally manipulate the number's precision (_i.e. how many decimal places_)
* They all round correctly with the exception of _int_

## Members

### [string][string] `Deci`

:   The number as a string with **one** place of precision, _i.e. ###.#_

### [string][string] `Centi`

:   The number as a string with **two** places of precision, _i.e. ###.##_

### [int][int] `Int`

:   Integer portion of the number truncated rather than rounded, _e.g. 12.779 returns 12_

### [string][string] `Milli`

:   The number as a string with **three** places of precision, _i.e. ###.###_

### [string][string] `Precision[#]`

:   The number as a string with # places of precision

### [string][string] `Prettify[precision]`

:   Pretty print the number with commas, with optional _precision_ (defaults to two decimal points).

### [int][int] `Raw`

:   Returns IEEE 754 representation of floating point value.

### [string][string] `To String`

:   Same as **Centi**

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
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
