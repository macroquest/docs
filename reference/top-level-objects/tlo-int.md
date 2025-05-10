---
tags:
    - tlo
---
# `Int`

<!--tlo-desc-start-->
Object that creates an integer from n.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='int', name='Int') }}

:   Parses whatever value for _n_ is provided and converts it into an [int].
<!--tlo-forms-end-->

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
<!--tlo-linkrefs-start-->
[int]: ../data-types/datatype-int.md
<!--tlo-linkrefs-end-->
