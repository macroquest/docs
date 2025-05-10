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
### {{ renderMember(type='float', name='Float') }}

:   The number as a float (123 is represented as 123.0)

### {{ renderMember(type='double', name='Double') }}

:   The number as a double (123 is represented as 123.0)

### {{ renderMember(type='string', name='Hex') }}

:   The hex value of the integer (10 is represented as 0xA)

### {{ renderMember(type='int64', name='Reverse') }}

:   Endianness reversed

### {{ renderMember(type='int', name='LowPart') }}

:   Lower 32-bits of the value.

### {{ renderMember(type='int', name='HighPart') }}

:   Upper 32-bits of the value.

### {{ renderMember(type='string', name='Prettify', params='precision') }}

:   Pretty print the number with commas, with optional _precision_

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
