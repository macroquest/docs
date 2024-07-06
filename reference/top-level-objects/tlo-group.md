---
tags:
    - tlo
---
# `Group`

Access to all group-related information.

## Forms

### {{ renderMember(type='group', name='Group') }}

:   Retrieve information about your group

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

[group]: ../data-types/datatype-group.md
