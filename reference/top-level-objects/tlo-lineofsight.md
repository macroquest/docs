---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `LineOfSight`

Object that is used to check if there is Line of Sight betwen two locations.

`Note: For ISXEQ all 6 parameters are required and will return NULL otherwise`

## Forms

* [_bool_](../data-types/datatype-bool.md) **LineOfSight[**y,x,z:y,x,z**]**
* [_bool_](../data-types/datatype-bool.md) **LineOfSight[**y,x,z,y,x,z**]** (For ISXEQ)

## Examples

```
/echo ${LineOfSight[20,40,-20:100,-300,70]}
```

Returns TRUE if Line of Sight is clear between the two locations
