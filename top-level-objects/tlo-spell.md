## Description

Object used to return information on a spell by name or by ID.

## Forms

|                                                            |                    |
|------------------------------------------------------------|--------------------|
| *[spell](../data-types/datatype-spell.md)* **Spell\[**n**\]**    | Find spell by ID   |
| *[spell](../data-types/datatype-spell.md)* **Spell\[**name**\]** | Find spell by name |

## Access to Types

-   *[spell](../data-types/datatype-spell.md)* **spell**

## Examples

`  /echo ${Spell[Splurt].ID} `

Will return 1620

`  /echo ${Spell[1620].Duration}`

Will return 16 (ie. 16 ticks)

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [spell](../data-types/datatype-spell.md)


