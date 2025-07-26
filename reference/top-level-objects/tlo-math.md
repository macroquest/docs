---
tags:
    - tlo
---
# Math
<!--tlo-desc-start-->
Creates a Math object which gives allows access to the math type members.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='math', name='Math') }}

:   Returns the math object which is used to perform math operations.
<!--tlo-forms-end-->

## Associated DataTypes

## [math](../data-types/datatype-math.md)
{%
  include-markdown "reference/data-types/datatype-math.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-math.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-math.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-math.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

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
<!--tlo-linkrefs-start-->
[math]: ../data-types/datatype-math.md
<!--tlo-linkrefs-end-->
