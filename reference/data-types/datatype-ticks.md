---
tags:
    - datatype
---
# `ticks` Type
<!--dt-desc-start-->
Represents a count of "ticks". Ticks are units of 6 seconds that are used to represent certain measurements of time in EverQuest.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int Hours
The number of hours in HH:MM:SS (0-23)
///

/// member | int Minutes
The number of minutes in HH:MM:SS (1-59)
///

/// member | int Seconds
The number of seconds in HH:MM:SS (1-59)
///

/// member | int TotalMinutes
The total number of minutes
///

/// member | int TotalSeconds
The total number of seconds
///

/// member | int Ticks
The value in ticks
///

/// member | string Time
Time in the form MM:SS
///

/// member | string TimeHMS
Time in the form HH:MM:SS (if there are no hours, the form will be MM:SS)
///

### [string][string] `To String`

:   Same as **Ticks**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
