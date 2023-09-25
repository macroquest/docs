---
tags:
    - datatype
---
# `dynamiczone`

Data for the current dynamic zone instance

See Also: [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)

## Members

### [bool][bool] `InRaid`

:   ??

### [dzmember][dzmember] `Leader`

:   The leader of the dynamic zone

### [bool][bool] `LeaderFlagged`

:   Returns true if the dzleader can successfully enter the dz (this also means the dz is actually Loaded.)

### [int][int] `MaxMembers`

:   Maximum number of characters that can enter this dynamic zone

### [int][int] `MaxTimers`

:   The number of timers present in **Timers**

### [dzmember][dzmember] `Member[&nbsp;#&nbsp;|&nbsp;name&nbsp;]`

:   The dynamic zone member _#_ or _name_

### [int][int] `Members`

:   Current number of characters in the dynamic zone

### [int][int] `MinMembers`

:   Minimum number of members required.

### [string][string] `Name`

:   The full name of the dynamic zone.

| [_dztimer_](datatype-dztimer.md) | **Timer**[&nbsp;_#&nbsp;\|&nbsp;name_&nbsp;] | Access the list of current lockout timers. This is either an index from 1 to **MaxTimers**, or a "Expedition\|Event" combination. Event is optional, but if multiple Expeditions match, the timer with the earliest lockout expiration will be returned.
### [string][string] `To String`

:   Same as **Name**


## Usage

!!! example

    Example usage of **Timer**

    === "MQScript"

        ```
        | Example output: 2:10:24
        /echo ${DynamicZone.Timer[Nagafen's Lair|Lord Nagafen].Timer.TimeDHM}
        ```

    === "Lua"

        ```lua
        -- Example output: 2:10:24
        print(mq.TLO.DynamicZone.Timer("Nagafen's Lair|Lord Nagafen").Timer.TimeDHM())
        ```


## Changelog

* January 19th, 2022: Added MinMembers
* July 9th, 2021: Added MaxTimers, Timer
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
