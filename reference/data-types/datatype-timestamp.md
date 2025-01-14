---
tags:
    - datatype
---
# `timestamp`

A timestamp represented in milliseconds.

## Members

### {{ renderMember(type='int', name='Days') }}

:   Number of days remaining in the timestamp (3d 2h 23m will return 3)

### {{ renderMember(type='float', name='Float') }}

:   timestamp represented in remaining seconds (1hr 23 min 53 seconds will return 5033.00)

### {{ renderMember(type='int64', name='Hours') }}

:   Number of hours remaining in the timestamp (1hr 23min 53 seconds will return 1)

### {{ renderMember(type='int64', name='Minutes') }}

:   Number of Minutes remaining in the timestamp (1hr 23min 53 seconds will return 23)

### {{ renderMember(type='int64', name='Raw') }}

:   Remaining time value represented in milliseconds

### {{ renderMember(type='int64', name='Seconds') }}

:   Number of Seconds remaining in the timestamp (1hr 23min 53 seconds will return 53)

### {{ renderMember(type='int64', name='Ticks') }}

:   Remaining time value represented in ticks

### {{ renderMember(type='string', name='Time') }}

:   Remaining time value formatted in M:S

### {{ renderMember(type='string', name='TimeDHM') }}

:   Remaining time value formatted in D:H:M (Days:Hours:Minutes)

### {{ renderMember(type='string', name='TimeHMS') }}

:   Remaining time value formatted in H:M:S

### {{ renderMember(type='int64', name='TotalMinutes') }}

:   Total number of remaining minutes in the timestamp (1hr 23min 53 seconds will return 83)

### {{ renderMember(type='int64', name='TotalSeconds') }}

:   Total number of remaining minutes in the timestamp (1hr 23min 53 seconds will return 5033)

### [string][string] `(To String)`

:   Same as **Raw**


### Changelog

* July 9th, 2021: Added Days, TimeDHM

[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
