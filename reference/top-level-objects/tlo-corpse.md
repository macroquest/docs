---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Corpse`

Access to objects of type corpse, which is the currently active corpse (ie. the one you are looting).

## Forms

* [_corpse_](../data-types/datatype-corpse.md) **Corpse**: Corpse you are looting.

## Examples

`/if (${Corpse.Open}) {`  
`/echo Corpse is open, proceeding with looting`  
`}`
