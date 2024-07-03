---
tags:
    - datatype
---
# `dynamiczone`

Data for the current dynamic zone instance

See Also: [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)

## Members

### {{ renderMember(type='bool', name='InRaid') }} 

:   ??

### {{ renderMember(type='dzmember', name='Leader') }} 

:   The leader of the dynamic zone

### {{ renderMember(type='bool', name='LeaderFlagged') }} 

:   Returns true if the dzleader can successfully enter the dz (this also means the dz is actually Loaded.)

### {{ renderMember(type='int', name='MaxMembers') }} 

:   Maximum number of characters that can enter this dynamic zone

### {{ renderMember(type='int', name='MaxTimers') }} 

:   The number of timers present in **Timers**

### {{ renderMember(type='dzmember', name='Member', params='#|name') }} 

:   The dynamic zone member _#_ or _name_

### {{ renderMember(type='int', name='Members') }} 

:   Current number of characters in the dynamic zone

### {{ renderMember(type='int', name='MinMembers') }} 

:   Minimum number of members required.

### {{ renderMember(type='string', name='Name') }} 

:   The full name of the dynamic zone.

### {{ renderMember(type='dztimer', name='Timer', params='#|name') }}

:   Access the list of current lockout timers. This is either an index from 1 to **MaxTimers**, or a "Expedition\|Event" combination. Event is optional, but if multiple Expeditions match, the timer with the earliest lockout expiration will be returned.

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
[dztimer]: datatype-dztimer.md
