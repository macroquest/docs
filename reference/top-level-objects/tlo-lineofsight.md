---
tags:
    - tlo
---
# `LineOfSight`

<!--tlo-desc-start-->
Object that is used to check if there is Line of Sight betwen two locations.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='bool', name='LineOfSight', params='y,x,z:y,x,z') }}

:   Check for line-of-sight between the two specified coordinates.
<!--tlo-forms-end-->

## Usage

```
/echo ${LineOfSight[20,40,-20:100,-300,70]}
```

Returns TRUE if Line of Sight is clear between the two locations
<!--tlo-linkrefs-start-->
[bool]: ../data-types/datatype-bool.md
<!--tlo-linkrefs-end-->
