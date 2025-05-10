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
### {{ renderMember(type='int', name='Clock') }}

:   The nearest clock direction, e.g. 1-12

### {{ renderMember(type='float', name='Degrees') }}

:   Heading in degrees (same as casting to float)

### {{ renderMember(type='float', name='DegreesCCW') }}

:   Heading in degrees counter-clockwise (the way the rest of MQ2 and EQ uses it)

### {{ renderMember(type='string', name='Name') }}

:   The long compass direction, eg. "south", "south by southeast"

### {{ renderMember(type='string', name='ShortName') }}

:   The short compass direction, eg. "S", "SSE"

### [string][string] `(To String)`

:   Same as **ShortName**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
