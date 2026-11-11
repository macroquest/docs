---
tags:
    - datatype
---
# `heading`

<!--dt-desc-start-->
Represents a direction on a compass.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int Clock
The nearest clock direction, e.g. 1-12
///

/// member | float Degrees
Heading in degrees (same as casting to float)
///

/// member | float DegreesCCW
Heading in degrees counter-clockwise (the way the rest of MQ2 and EQ uses it)
///

/// member | string Name
The long compass direction, eg. "south", "south by southeast"
///

/// member | string ShortName
The short compass direction, eg. "S", "SSE"
///

### [string][string] `(To String)`

:   Same as **ShortName**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
