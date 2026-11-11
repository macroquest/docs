---
tags:
    - datatype
---
# `timestamp`

<!--dt-desc-start-->
A timestamp represented in milliseconds.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int Days
Number of days remaining in the timestamp (3d 2h 23m will return 3)
///

/// member | float Float
timestamp represented in remaining seconds (1hr 23 min 53 seconds will return 5033.00)
///

/// member | int64 Hours
Number of hours remaining in the timestamp (1hr 23min 53 seconds will return 1)
///

/// member | int64 Minutes
Number of Minutes remaining in the timestamp (1hr 23min 53 seconds will return 23)
///

/// member | int64 Raw
Remaining time value represented in milliseconds
///

/// member | int64 Seconds
Number of Seconds remaining in the timestamp (1hr 23min 53 seconds will return 53)
///

/// member | int64 Ticks
Remaining time value represented in ticks
///

/// member | string Time
Remaining time value formatted in M:S
///

/// member | string TimeDHM
Remaining time value formatted in D:H:M (Days:Hours:Minutes)
///

/// member | string TimeHMS
Remaining time value formatted in H:M:S
///

/// member | int64 TotalMinutes
Total number of remaining minutes in the timestamp (1hr 23min 53 seconds will return 83)
///

/// member | int64 TotalSeconds
Total number of remaining minutes in the timestamp (1hr 23min 53 seconds will return 5033)
///

### [string][string] `(To String)`

:   Same as **Raw**

<!--dt-members-end-->

### Changelog

* July 9th, 2021: Added Days, TimeDHM
<!--dt-linkrefs-start-->
[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
