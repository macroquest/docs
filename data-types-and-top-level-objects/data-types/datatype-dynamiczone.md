# DataType:dynamiczone

Data for the current dynamic zone instance

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_dzmember_](datatype-dzmember.md) | **Leader** | The leader of the dynamic zone |
| [_bool_](datatype-bool.md) | **LeaderFlagged** | Returns true if the dzleader can successfully enter the dz (this also means the dz is actually Loaded.)

                                                  Example: `${DynamicZone.LeaderFlagged}` |
| [_int_](datatype-int.md) | **MaxMembers** | Maximum number of characters that can enter this dynamic zone |
| [_dzmember_](datatype-dzmember.md) | **Member\[**#**|**name**\]** | The dynamic zone member _#_ or _name_ |
| [_int_](datatype-int.md) | **Members** | Current number of characters in the dynamic zone |
| [_string_](datatype-string.md) | **Name** | The full name of the dynamic zone |
| [_int_](datatype-int.md) | **MaxTimers** | The number of timers present in **Timers** |
| [_dztimer_](datatype-dztimer.md) | **Timer[_\#_|_Name_]** | Access the list of current lockout timers. This is either an index from
                                                              1 to **MaxTimers**, or a Expedition|Event combination. Event is optional,
                                                              but if multiple Expeditions match, the timer with the earliest lockout
                                                              expiration will be returned.

                                                              **Example:**
                                                              
                                                              `/echo ${DynamicZone.Timer[Nagafen's Lair|Lord Nagafen].Timer.TimeDHM}`
          
                                                              Output: 2:10:24
| [_string_](datatype-string.md) | **To String** | Same as **Name** |

### Changelog

* July 9th, 2021: Added MaxTimers, Timer

