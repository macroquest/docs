---
tags:
    - tlo
---
# `Spell`

<!--tlo-desc-start-->
Object used to return information on a spell by name or by ID.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='spell', name='Spell') }}

:   Find spell by ID

### {{ renderMember(type='spell', name='Spell', params='Name') }}

:   Find spell by name
<!--tlo-forms-end-->

## Usage

```
/echo ${Spell[Splurt].ID}
```

Will return 1620

```
/echo ${Spell[1620].Duration}
```

Will return 16 (ie. 16 ticks)
<!--tlo-linkrefs-start-->
[spell]: ../data-types/datatype-spell.md
<!--tlo-linkrefs-end-->
