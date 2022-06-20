---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Skill`

Object used to get information on your character's skills.

## Forms

[_skill_][skill] **Skill**[_name_]

:   Retrieve skill by name

[_skill_][skill] **Skill**[_N_]

:   Retrieve skill by number

## Examples

```
/echo ${Skill[1].ReuseTime}
```

Displays the reuse time of skill 1

```
/echo ${Skill[backstab].ID}
```

Displays the skill number of the backstab skill


[skill]: ../data-types/datatype-skill.md
