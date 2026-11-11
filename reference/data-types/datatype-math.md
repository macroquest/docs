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
/// member | float Abs[n]
The absolute value of the result of _n_
///

/// member | float Acos[n]
Arccosine of _n_ (in degrees)
///

/// member | float Asin[n]
Arcsine of _n_ (in degrees)
///

/// member | float Atan[n]
Arctangent of _n_ (in degrees)
///

/// member | float Calc[n]
Performs a mathematical calculation _n_
///

/// member | int Clamp[n, min, max]
Clamps the value _n_ such that _min _<= _n_ <= _max_
///

/// member | float Cos[n]
Cosine of _n_ (in degrees)
///

/// member | int Dec[hex]
Decimal value of a hexidecimal string
///

/// member | float Distance[y,x,z:y,x,z]
<ul><li>Calculates the distance between two points on the map</li><li>1, 2, or 3 dimensions may be provided</li><li>Defaults to your character's current location</li></ul>
///

/// member | string Hex[n]
Returns hexidecimal value of [_int_](datatype-int.md) _n_
///

/// member | int Not[n]
Bitwise complement of _n_
///

/// member | int Rand[n]
Random integer. Rand\[5] range 0 to 4. Rand\[100,200] range 100 to 199
///

/// member | float Sin[n]
Sine of _n_ (in degrees)
///

/// member | float Sqrt[n]
Square root of _n_
///

/// member | float Tan[n]
Tangent of _n_ (in degrees)
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
