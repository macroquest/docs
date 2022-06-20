---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `timer`

A timer data type is set in tenths of one second and counts down to zero; starting immediately after being set.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **OriginalValue** | Original value of the timer |
| [_int_](datatype-int.md) | **Value** | Current value of the timer |
| [_string_](datatype-string.md) | **To String** | Same as **Value** |

## Usage

Consider the following timer:

```
/declare BuffTimer timer local
/varset BuffTimer 360
```

BuffTimer will be equal to 0 in:

* 360 tenths of 1 second
* 36 seconds
* 6 ticks (a tick is 6 seconds)

Timers may also be set with an "s" (seconds) or an "m" (minutes) appended to the value. For example:

```
/varset BuffTimer 360s
```

This would set the timer to 3600 (360 * 10) tenths of 1 second

```
/varset BuffTimer 360m
```

This would set the timer to 216000 (360 * 60 * 10) tenths of 1 second

```text
sub main
    /declare myTimer timer local 100
    /while ( ${myTimer} ) {
        /echo ${myTimer}
        /delay 10
    }
/return
```

This would loop while myTimer is above 0

