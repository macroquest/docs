---
tags:
    - datatype
---
# `skill`

Data related to a particular skill

## Members

### {{ renderMember(type='bool', name='Activated') }}

:   Returns TRUE if the skill is an activatable skill (ie, an Ability)

### {{ renderMember(type='int', name='AltTimer') }}

:   Originally intended to tell whether a skill shares a timer with another skill, this is misnamed.  It returns the category of the skill:

    | Value | Meaning |
    | :--- | :--- |
    | 0 | Non Combat |
    | 1 | Combat |
    | 2 | Special |

### {{ renderMember(type='bool', name='Auto') }}

:   Returns TRUE if the skill has /autoskill on, FALSE if it does not.

### {{ renderMember(type='int', name='ID') }}

:   Skill number

### {{ renderMember(type='int', name='MinLevel') }}

:   Minimum level for your class

### {{ renderMember(type='string', name='Name') }}

:   Name of the skill

### {{ renderMember(type='int', name='ReuseTime') }}

:   Reuse timer _(what number format? ticks, seconds, deciseconds?)_

### {{ renderMember(type='int', name='SkillCap') }}

:   Skill cap based on your current level and class.

### {{ renderMember(type='int', name='StartingSkill') }}

:   Base skill level for your class

### [string][string] `To String`

:   Same as **Name**


[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
