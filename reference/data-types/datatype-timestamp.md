---
tags:
    - datatype
---
# `timestamp`

A timestamp represented in milliseconds.

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Days** | Number of days remaining in the timestamp (3d 2h 23m will return 3) |
| [_float_](datatype-float.md) | **Float** | timestamp represented in remaining seconds (1hr 23 min 53 seconds will return 5033.00) |
| [_int64_](datatype-int64.md) | **Hours** | Number of hours remaining in the timestamp (1hr 23min 53 seconds will return 1) |
| [_int64_](datatype-int64.md) | **Minutes** | Number of Minutes remaining in the timestamp (1hr 23min 53 seconds will return 23) |
| [_int64_](datatype-int64.md) | **Raw** | Remaining time value represented in milliseconds |
| [_int64_](datatype-int64.md) | **Seconds** | Number of Seconds remaining in the timestamp (1hr 23min 53 seconds will return 53) |
| [_int64_](datatype-int64.md) | **Ticks** | Remaining time value represented in ticks |
| [_string_](datatype-string.md) | **TimeDHM** | Remaining time value formatted in D:H:M (Days:Hours:Minutes) |
| [_string_](datatype-string.md) | **TimeHMS** | Remaining time value formatted in H:M:S |
| [_string_](datatype-string.md) | **Time** | Remaining time value formatted in M:S |
| [_int64_](datatype-int64.md) | **TotalMinutes** | Total number of remaining minutes in the timestamp (1hr 23min 53 seconds will return 83) |
| [_int64_](datatype-int64.md) | **TotalSeconds** | Total number of remaining minutes in the timestamp (1hr 23min 53 seconds will return 5033) |
| [_string_](datatype-string.md) | **(To String)** | Same as **Raw** |

### Changelog

* July 9th, 2021: Added Days, TimeDHM
