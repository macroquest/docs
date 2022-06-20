---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Group`

Access to all group-related information.

## Forms

* [_group_](../data-types/datatype-group.md) **Group**

## Examples

`/echo ${Group.Leader.ID}`

Echo Groupleader ID, if any.

`/echo ${Group.Member[0]}`

Echo's your own name

`/echo ${Group.Member[1]}`

Echo's the next person on the list, after yourself.
