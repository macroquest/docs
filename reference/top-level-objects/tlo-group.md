---
tags:
    - tlo
---
# `Group`

<!--tlo-desc-start-->
Access to all group-related information.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='group', name='Group') }}

:   Retrieve information about your group
<!--tlo-forms-end-->

## Usage

```
/echo ${Group.Leader.ID}
```

Echo Groupleader ID, if any.

```
/echo ${Group.Member[0]}
```

Echos your own name

```
`/echo ${Group.Member[1]}
```

Echos the next person on the list, after yourself.
<!--tlo-linkrefs-start-->
[group]: ../data-types/datatype-group.md
<!--tlo-linkrefs-end-->
