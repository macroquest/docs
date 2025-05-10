---
tags:
    - tlo
---
# `Mercenary`

<!--tlo-desc-start-->
Object used to get information about your mercenary.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='mercenary', name='Mercenary') }}
<!--tlo-forms-end-->

## Usage

```
/echo ${Mercenary.Stance}
```

Displays the current stance of the mercenary based on the type (Passive, Balanced, Aggressive, etc.)

```
/echo ${Mercenary.State}
```

Displays whether the mercenary is suspended or not.
<!--tlo-linkrefs-start-->
[mercenary]: ../data-types/datatype-mercenary.md
<!--tlo-linkrefs-end-->