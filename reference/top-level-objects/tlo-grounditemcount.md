---
tags:
    - tlo
---
# `GroundItemCount`

Access to all Groundspawn item count information.

## Forms

### {{ renderMember(type='int', name='GroundItemCount') }}

:   Retrieve the count of items on the ground

## Usage

```
/echo There are ${GroundItemCount[apple]} Apples on the ground
```

Output: There are 5 Apples on the ground

```
/echo There are ${GroundItemCount} items on the ground in this zone.
```

Output: There are 12 items on the ground in this zone.

[int]: ../data-types/datatype-int.md
