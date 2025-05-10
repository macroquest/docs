---
tags:
    - tlo
---
# `Skill`

<!--tlo-desc-start-->
Object used to get information on your character's skills.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='skill', name='Skill', params='name') }}

:   Retrieve skill by name

### {{ renderMember(type='skill', name='Skill', params='N') }}

:   Retrieve skill by number
<!--tlo-forms-end-->

## Usage

```
/echo ${Skill[1].ReuseTime}
```

Displays the reuse time of skill 1

```
/echo ${Skill[backstab].ID}
```

Displays the skill number of the backstab skill

<!--tlo-linkrefs-start-->
[skill]: ../data-types/datatype-skill.md
<!--tlo-linkrefs-end-->
