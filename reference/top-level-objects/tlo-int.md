---
tags:
    - tlo
---
# `Int`

Object that creates an integer from n.

## Forms

### {{ renderMember(type='int', name='Int') }}

:   Parses whatever value for _n_ is provided and converts it into an [int].

## Usage

```
/echo ${Int[123].Hex}
```

Echos the result of the conversion of 123 to an int in hexadecimal.

```
/echo ${Int[textstringhere]}
```

Echos a zero - useful if passing a string to a macro or subroutine that could be a text string or a number and you want to do different actions depending on what you recieve

```
/echo ${Int[123]}
```

Echos 123

[int]: ../data-types/datatype-int.md
