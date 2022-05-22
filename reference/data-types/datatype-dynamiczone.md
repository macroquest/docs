---
tags:
    - datatype
---

# `dynamiczone`

Data for the current dynamic zone instance

See Also: [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](datatype-bool.md) | **InRaid** | ?? |
| [_dzmember_](datatype-dzmember.md) | **Leader** | The leader of the dynamic zone |
| [_bool_](datatype-bool.md) | **LeaderFlagged** | Returns true if the dzleader can successfully enter the dz (this also means the dz is actually Loaded.) |
| [_int_](datatype-int.md) | **MaxMembers** | Maximum number of characters that can enter this dynamic zone |
| [_int_](datatype-int.md) | **MaxTimers** | The number of timers present in **Timers** |
| [_dzmember_](datatype-dzmember.md) | **Member**[&nbsp;_#&nbsp;\|&nbsp;name_&nbsp;] | The dynamic zone member _#_ or _name_ |
| [_int_](datatype-int.md) | **Members** | Current number of characters in the dynamic zone |
| [_int_](datatype-int.md) | **MinMembers** | Minimum number of members required. |
| [_string_](datatype-string.md) | **Name** | The full name of the dynamic zone. |
| [_dztimer_](datatype-dztimer.md) | **Timer**[&nbsp;_#&nbsp;\|&nbsp;name_&nbsp;] | Access the list of current lockout timers. This is either an index from 1 to **MaxTimers**, or a "Expedition\|Event" combination. Event is optional, but if multiple Expeditions match, the timer with the earliest lockout expiration will be returned.
| [_string_](datatype-string.md) | **To String** | Same as **Name** |

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
