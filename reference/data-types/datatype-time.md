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
### {{ renderMember(type='string', name='Date') }}

:   Date in the format MM/DD/YYYY

### {{ renderMember(type='int', name='Day') }}

:   Day of the month

### {{ renderMember(type='int', name='DayOfWeek') }}

:   Day of the week (1=sunday to 7=saturday)

### {{ renderMember(type='int', name='Hour') }}

:   Hour (0-23)

### {{ renderMember(type='int', name='Hour12') }}

:   Hour (0-11)

### {{ renderMember(type='int', name='Millisecond') }}

:   Millisecond (0-999)

### {{ renderMember(type='int64', name='MillisecondsSinceEpoch') }}

:   Number of milliseconds since the epoch (January 1, 1970)

### {{ renderMember(type='int', name='MillisecondsSinceMidnight') }}

:   Number of milliseconds since midnight

### {{ renderMember(type='int', name='Minute') }}

:   Minute (0-59)

### {{ renderMember(type='int', name='Month') }}

:   Month of the year (1-12)

### {{ renderMember(type='bool', name='Night') }}

:   Gives true if the current hour is considered "night" in EQ (7:00pm-6:59am)

### {{ renderMember(type='int', name='Second') }}

:   Second (0-59)

### {{ renderMember(type='int', name='SecondsSinceMidnight') }}

:   Number of seconds since midnight

### {{ renderMember(type='string', name='Time12') }}

:   Time in 12-hour format (HH:MM:SS)

### {{ renderMember(type='string', name='Time24') }}

:   Time in 24-hour format (HH:MM:SS)

### {{ renderMember(type='int', name='Year') }}

:   Year

### [string][string] `(To String)`

:   Same as **Time24**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
