---
tags:
    - datatype
---
# `dztimer`

Provides information about a dynamic zone lockout timer

See Also: [DataType:dynamiczone](./datatype-dynamiczone.md), [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)

## Members

### [Type][Type] `Name`

:   Description

### [string][string] `ExpeditionName`

:   The name of the expedition

### [string][string] `EventName`

:   The name of the event

### [timestamp][timestamp] `Timer`

:   The timestamp indicating when this lockout expires

### [int][int] `EventID`

:   ID of the event. These values are only unique per Expedition. Non-event lockouts (Replay Timer) will have a -1 event id.

| [_string_](datatype-string.md) | **To String** | Returns the string formatted as `"ExpeditionName|EventName"` |

### Changelog

* July 9th, 2021: Initial version
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
