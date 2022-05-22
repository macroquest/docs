---
tags:
    - datatype
---

# `heading`

Represents a direction on a compass.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Clock** | The nearest clock direction, e.g. 1-12 |
| [_float_](datatype-float.md) | **Degrees** | Heading in degrees (same as casting to float) |
| [_float_](datatype-float.md) | **DegreesCCW** | Heading in degrees counter-clockwise (the way the rest of MQ2 and EQ uses it) |
| [_string_](datatype-string.md) | **Name** | The long compass direction, eg. "south", "south by southeast" |
| [_string_](datatype-string.md) | **ShortName** | The short compass direction, eg. "S", "SSE" |
| [_string_](datatype-string.md) | **(To String)** | Same as **ShortName** |
