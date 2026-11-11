---
tags:
    - datatype
---
# `dynamiczone`

<!--dt-desc-start-->
Data for the current dynamic zone instance

See Also: [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool InRaid
??
///

/// member | dzmember Leader
The leader of the dynamic zone
///

/// member | bool LeaderFlagged
Returns true if the dzleader can successfully enter the dz (this also means the dz is actually Loaded.)
///

/// member | int MaxMembers
Maximum number of characters that can enter this dynamic zone
///

/// member | int MaxTimers
The number of timers present in **Timers**
///

/// member | dzmember Member[#|name]
The dynamic zone member _#_ or _name_
///

/// member | int Members
Current number of characters in the dynamic zone
///

/// member | int MinMembers
Minimum number of members required.
///

/// member | string Name
The full name of the dynamic zone.
///

/// member | dztimer Timer[#|name]
Access the list of current lockout timers. This is either an index from 1 to **MaxTimers**, or a "Expedition\|Event" combination. Event is optional, but if multiple Expeditions match, the timer with the earliest lockout expiration will be returned.
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

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
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[dzmember]: datatype-dzmember.md
[dztimer]: datatype-dztimer.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
