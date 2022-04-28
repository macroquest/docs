# TLO:Spell

## Description

Object used to return information on a spell by name or by ID.

## Forms

|  |  |
| :--- | :--- |
| [_spell_](../data-types/datatype-spell.md) **Spell[**n**]** | Find spell by ID |
| [_spell_](../data-types/datatype-spell.md) **Spell[**name**]** | Find spell by name |

## Access to Types

* [_spell_](../data-types/datatype-spell.md) **spell**

## Examples

`/echo ${Spell[Splurt].ID}`

Will return 1620

`/echo ${Spell[1620].Duration}`

Will return 16 (ie. 16 ticks)

## See Also

* [Top-Level Objects](./)
* [spell](../data-types/datatype-spell.md)

