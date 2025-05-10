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
### {{ renderMember(type='int', name='Hours') }}

:   The number of hours in HH:MM:SS (0-23)

### {{ renderMember(type='int', name='Minutes') }}

:   The number of minutes in HH:MM:SS (1-59)

### {{ renderMember(type='int', name='Seconds') }}

:   The number of seconds in HH:MM:SS (1-59)

### {{ renderMember(type='int', name='TotalMinutes') }}

:   The total number of minutes

### {{ renderMember(type='int', name='TotalSeconds') }}

:   The total number of seconds

### {{ renderMember(type='int', name='Ticks') }}

:   The value in ticks

### {{ renderMember(type='string', name='Time') }}

:   Time in the form MM:SS

### {{ renderMember(type='string', name='TimeHMS') }}

:   Time in the form HH:MM:SS (if there are no hours, the form will be MM:SS)

### [string][string] `To String`

:   Same as **Ticks**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
