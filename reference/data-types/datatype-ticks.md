---
tags:
    - datatype
---

# `ticks` Type

Represents a count of "ticks". Ticks are units of 6 seconds that are used to represent certain measurements of time in EverQuest.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Hours** | The number of hours in HH:MM:SS (0-23) |
| [_int_](datatype-int.md) | **Minutes** | The number of minutes in HH:MM:SS (1-59) |
| [_int_](datatype-int.md) | **Seconds** | The number of seconds in HH:MM:SS (1-59) |
| [_int_](datatype-int.md) | **TotalMinutes** | The total number of minutes |
| [_int_](datatype-int.md) | **TotalSeconds** | The total number of seconds |
| [_int_](datatype-int.md) | **Ticks** | The value in ticks |
| [_string_](datatype-string.md) | **Time** | Time in the form MM:SS |
| [_string_](datatype-string.md) | **TimeHMS** | Time in the form HH:MM:SS (if there are no hours, the form will be MM:SS) |
| [_string_](datatype-string.md) | **To String** | Same as **Ticks** |

