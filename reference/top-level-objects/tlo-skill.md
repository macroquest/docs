---
tags:
    - tlo
---
# `Skill`

Object used to get information on your character's skills.

## Forms

### {{ renderMember(type='skill', name='Skill', params='name') }}

:   Retrieve skill by name

### {{ renderMember(type='skill', name='Skill', params='N') }}

:   Retrieve skill by number


## Usage

```
/echo ${Skill[1].ReuseTime}
```

Displays the reuse time of skill 1

```
/echo ${Skill[backstab].ID}
```

Displays the skill number of the backstab skill


[skill]: ../data-types/datatype-skill.md
