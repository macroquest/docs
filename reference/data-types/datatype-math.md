---
tags:
    - datatype
---
# `math`

<!--dt-desc-start-->
This DataType performs various mathematical calculations. In the following members, _n_ is any formula that consists of valid [Operators](../../macros/operators.md).
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='float', name='Abs', params='n') }}

:   The absolute value of the result of _n_

### {{ renderMember(type='float', name='Acos', params='n') }}

:   Arccosine of _n_ (in degrees)

### {{ renderMember(type='float', name='Asin', params='n') }}

:   Arcsine of _n_ (in degrees)

### {{ renderMember(type='float', name='Atan', params='n') }}

:   Arctangent of _n_ (in degrees)

### {{ renderMember(type='float', name='Calc', params='n') }}

:   Performs a mathematical calculation _n_

### {{ renderMember(type='int', name='Clamp', params='n, min, max') }}

:   Clamps the value _n_ such that _min _<= _n_ <= _max_

### {{ renderMember(type='float', name='Cos', params='n') }}

:   Cosine of _n_ (in degrees)

### {{ renderMember(type='int', name='Dec', params='hex') }}

:   Decimal value of a hexidecimal string

### {{ renderMember(type='float', name='Distance', params='y,x,z:y,x,z') }}

:   <ul><li>Calculates the distance between two points on the map</li><li>1, 2, or 3 dimensions may be provided</li><li>Defaults to your character's current location</li></ul>

### {{ renderMember(type='string', name='Hex', params='n') }}

:   Returns hexidecimal value of [_int_](datatype-int.md) _n_

### {{ renderMember(type='int', name='Not', params='n') }}

:   Bitwise complement of _n_

### {{ renderMember(type='int', name='Rand', params='n') }}

:   Random integer. Rand\[5] range 0 to 4. Rand\[100,200] range 100 to 199

### {{ renderMember(type='float', name='Sin', params='n') }}

:   Sine of _n_ (in degrees)

### {{ renderMember(type='float', name='Sqrt', params='n') }}

:   Square root of _n_

### {{ renderMember(type='float', name='Tan', params='n') }}

:   Tangent of _n_ (in degrees)
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
