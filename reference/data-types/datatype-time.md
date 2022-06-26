---
tags:
    - datatype
---
# `time` Type

Represents a unit of clock time.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **Date** | Date in the format MM/DD/YYYY |
| [_int_](datatype-int.md) | **Day** | Day of the month |
| [_int_](datatype-int.md) | **DayOfWeek** | Day of the week (1=sunday to 7=saturday) |
| [_int_](datatype-int.md) | **Hour** | Hour (0-23) |
| [_int_](datatype-int.md) | **Hour12** | Hour (0-11) |
| [_int_](datatype-int.md) | **Minute** | Minute (0-59) |
| [_int_](datatype-int.md) | **Month** | Month of the year (1-12) |
| [_bool_](datatype-bool.md) | **Night** | Gives true if the current hour is considered "night" in EQ (7:00pm-6:59am) |
| [_int_](datatype-int.md) | **Second** | Second (0-59) |
| [_int_](datatype-int.md) | **SecondsSinceMidnight** | Number of seconds since midnight |
| [_string_](datatype-string.md) | **Time12** | Time in 12-hour format (HH:MM:SS) |
| [_string_](datatype-string.md) | **Time24** | Time in 24-hour format (HH:MM:SS) |
| [_int_](datatype-int.md) | **Year** | Year |
| [_string_](datatype-string.md) | **(To String)** | Same as **Time24** |

