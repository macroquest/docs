---
tags:
    - tlo
---
# `Corpse`

<!--tlo-desc-start-->
Access to objects of type corpse, which is the currently active corpse (ie. the one you are looting).
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='corpse', name='Corpse') }}

:   Corpse you are looting.
<!--tlo-forms-end-->

## Usage

```
/if (${Corpse.Open}) {
    /echo Corpse is open, proceeding with looting
}
```
<!--tlo-linkrefs-start-->
[corpse]: ../data-types/datatype-corpse.md
<!--tlo-linkrefs-end-->
