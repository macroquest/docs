---
tags:
    - datatype
---
# `skill`

<!--dt-desc-start-->
Data related to a particular skill
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool Activated
Returns TRUE if the skill is an activatable skill (ie, an Ability)
///

/// member | int AltTimer
Originally intended to tell whether a skill shares a timer with another skill, this is misnamed.  It returns the category of the skill:

| Value | Meaning |
| :--- | :--- |
| 0 | Non Combat |
| 1 | Combat |
| 2 | Special |
///

/// member | bool Auto
Returns TRUE if the skill has /autoskill on, FALSE if it does not.
///

/// member | int ID
Skill number
///

/// member | int MinLevel
Minimum level for your class
///

/// member | string Name
Name of the skill
///

/// member | int ReuseTime
Reuse timer _(what number format? ticks, seconds, deciseconds?)_
///

/// member | int SkillCap
Skill cap based on your current level and class.
///

/// member | int StartingSkill
Base skill level for your class
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
