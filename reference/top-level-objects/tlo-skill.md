# TLO:Skill

## Description

Object used to get information on your character's skills.

## Forms

|  |  |
| :--- | :--- |
| [_skill_](../data-types/datatype-skill.md) **Skill[**\#**]** | Retrieve skill by number |
| [_skill_](../data-types/datatype-skill.md) **Skill[**name**]** | Retrieve skill by name |

## Access to Types

* [_skill_](../data-types/datatype-skill.md) **skill**

## Examples

`/echo ${Skill[1].ReuseTime}`

Displays the reuse time of skill 1

`/echo ${Skill[backstab].ID}`

Displays the skill number of the backstab skill
