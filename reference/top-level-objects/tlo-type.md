---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Type`

Used to get information on data types.

## Forms

[_type_](../data-types/datatype-type.md) **Type**[_name_]

## Examples

Determines if a member of a type exists:

```
/echo ${Type[spawn].Member[ID]}
```

Enumerate members of a type using a loop:

```
/for n 1 to 100
    /echo ${Type[spawn].Member[${n}]}
/next n
```
