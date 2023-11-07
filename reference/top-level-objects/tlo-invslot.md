---
tags:
    - tlo
---
# `InvSlot`

## Description

Object used to get information on a specific inventory slot.

## Forms

[_invslot_](../data-types/datatype-invslot.md) **InvSlot**[_N_]

:   Inventory slot by index _N_.

[_invslot_](../data-types/datatype-invslot.md) **InvSlot**[_slot name_]

:   Inventory slot matching _slot name_.

## Examples

```
/lua parse mq.TLO.InvSlot(1).Name()
leftear
```

See the datatype link for more information
