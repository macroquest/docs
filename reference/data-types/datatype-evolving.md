---
tags:
    - datatype
---
# `evolving`

A DataType that deals with evolving items.

## Members

### [bool][bool] `ExpOn`

:   Is evolving item experience turned on for this item?

### [float][float] `ExpPct`

:   Percentage of experience that the item has gained

### [int][int] `Level`

:   The level of the evolving item.

### [int][int] `MaxLevel`

:   The maximum level of the evolving item

### [string][string] `To String`

:   Same as **ExpOn**


## Usage

!!! example

    === "MQScript"

        ```
        /echo ${FindItem[Blade of the Eclipse].Evolving.ExpPct}
        ```

    === "Lua"

        ```lua
        print(mq.TLO.FindItem("Blade of the Eclipse").Evolving.ExpPct())
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
