---
tags:
    - tlo
---
# `LineOfSight`

Object that is used to check if there is Line of Sight betwen two locations.

## Forms

### {{ renderMember(type='bool', name='LineOfSight', params='y,x,z:y,x,z') }}

:   Check for line-of-sight between the two specified coordinates.


## Usage

```
/echo ${LineOfSight[20,40,-20:100,-300,70]}
```

Returns TRUE if Line of Sight is clear between the two locations

[bool]: ../data-types/datatype-bool.md
