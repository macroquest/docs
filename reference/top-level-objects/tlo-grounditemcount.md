---
tags:
    - tlo
---
# `GroundItemCount`

<!--tlo-desc-start-->
Access to all Groundspawn item count information.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='int', name='GroundItemCount') }}

:   Retrieve the count of items on the ground
<!--tlo-forms-end-->

## Usage

```
/echo There are ${GroundItemCount[apple]} Apples on the ground
```

Output: There are 5 Apples on the ground

```
/echo There are ${GroundItemCount} items on the ground in this zone.
```

Output: There are 12 items on the ground in this zone.
<!--tlo-linkrefs-start-->
[int]: ../data-types/datatype-int.md
<!--tlo-linkrefs-end-->
