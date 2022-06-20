---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# Math

Creates a Math object which gives allows access to the math type members.

## Forms

[_math_](../data-types/datatype-math.md) **Math**

:   Returns the math object which is used to perform math operations.

## Examples

```
/echo ${Math.Calc[3-1]}
```

Echoes 2.00

```
/echo ${Math.Calc[49%6+25]}
```

Echoes the result of 49 modulo 6 + 25, or 1 + 25

```
/echo ${Math.Sqrt[49]}
```

Echoes the square root of 49

```
/echo ${Math.Rand[500]}
```

Echoes a random number between 1 and 500

Math.Rand now takes an optional min argument so you can get a random number between 2 variables.

```
/echo ${Math.Rand[5,10]}
```

this would return a randum number between 5 and 10.
