---
tags:
    - datatype
---
# `float` Type
<!--dt-desc-start-->
Represents a single precision (32-bit) floatiang point number.

* A floating-point number is one which has a decimal component (_e.g. 1.01_)
* Members of this DataType generally manipulate the number's precision (_i.e. how many decimal places_)
* They all round correctly with the exception of _int_
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | string Centi
The number as a string with **two** places of precision, _i.e. ###.##_
///

/// member | string Deci
The number as a string with **one** place of precision, _i.e. ###.#_
///

/// member | int Int
Integer portion of the number truncated rather than rounded, _e.g. 12.779 returns 12_
///

/// member | string Milli
The number as a string with **three** places of precision, _i.e. ###.###_
///

/// member | string Precision[#]
The number as a string with # places of precision
///

/// member | string Prettify[precision]
Pretty print the number with commas, with optional _precision_ (defaults to two decimal points).
///

/// member | int Raw
Returns IEEE 754 representation of floating point value.
///

### [string][string] `To String`

:   Same as **Centi**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
