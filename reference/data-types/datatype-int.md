---
tags:
    - datatype
---
# `int` Type

Represents a 32-bit integer. Can hold values from -2,147,483,648 to 2,147,483,647.

## Members

### {{ renderMember(type='float', name='Float') }}

:   The number as a float (123 is represented as 123.0)

### {{ renderMember(type='double', name='Double') }}

:   The number as a double (123 is represented as 123.0)

### {{ renderMember(type='string', name='Hex') }}

:   The hex value of the integer (10 is represented as 0xA)

### {{ renderMember(type='int', name='Reverse') }}

:   Endianness reversed

### {{ renderMember(type='int', name='LowPart') }}

:   Lower 16-bits of the value.

### {{ renderMember(type='int', name='HighPart') }}

:   Upper 16-bits of the value.

### {{ renderMember(type='string', name='Prettify', params='precision') }}

:   Pretty print the number with commas, with optional _precision_

### [string][string] `(To String)`

:   The number as a string

[double]: datatype-double.md
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
