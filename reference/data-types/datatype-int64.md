---
tags:
    - datatype
---
# `int64` Type

<!--dt-desc-start-->
Represents a 64-bit integer. Can hold values from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | float Float
The number as a float (123 is represented as 123.0)
///

/// member | double Double
The number as a double (123 is represented as 123.0)
///

/// member | string Hex
The hex value of the integer (10 is represented as 0xA)
///

/// member | int64 Reverse
Endianness reversed
///

/// member | int LowPart
Lower 32-bits of the value.
///

/// member | int HighPart
Upper 32-bits of the value.
///

/// member | string Prettify[precision]
Pretty print the number with commas, with optional _precision_
///

### [string][string] `(To String)`

:   The number as a string
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[double]: datatype-double.md
[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
