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

:   Originally intended to tell whether a skill shares a timer with another skill, this is misnamed.  It returns the category of the skill:  0 - Non Combat, 1 - Combat, 2 - Special

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

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: ../data-types/datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
