---
tags:
    - datatype
---
# `time` Type
<!--dt-desc-start-->
Represents a unit of clock time.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | string Date
Date in the format MM/DD/YYYY
///

/// member | int Day
Day of the month
///

/// member | int DayOfWeek
Day of the week (1=sunday to 7=saturday)
///

/// member | int Hour
Hour (0-23)
///

/// member | int Hour12
Hour (0-11)
///

/// member | int Millisecond
Millisecond (0-999)
///

/// member | int64 MillisecondsSinceEpoch
Number of milliseconds since the epoch (January 1, 1970)
///

/// member | int MillisecondsSinceMidnight
Number of milliseconds since midnight
///

/// member | int Minute
Minute (0-59)
///

/// member | int Month
Month of the year (1-12)
///

/// member | bool Night
Gives true if the current hour is considered "night" in EQ (7:00pm-6:59am)
///

/// member | int Second
Second (0-59)
///

/// member | int SecondsSinceMidnight
Number of seconds since midnight
///

/// member | string Time12
Time in 12-hour format (HH:MM:SS)
///

/// member | string Time24
Time in 24-hour format (HH:MM:SS)
///

/// member | int Year
Year
///

### [string][string] `(To String)`

:   Same as **Time24**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
