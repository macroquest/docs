## Description

This is the type for any buffs currently affecting you, both long duration and short duration (bard) buffs.

Inherits *[spell](datatype-spell.md)*.

## Members

|                                            |               |                                                                                                                                                                                                                                  |
|--------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**                                   | **Member**    | **Description**                                                                                                                                                                                                                  |
| *[int](datatype-int.md)*           | **Counters**  | The number of counters added by the buff                                                                                                                                                                                         |
| *[int](datatype-int.md)*           | **Dar**       | The remaining damage absorption of the buff (if any). *This is not entirely accurate, it will only show you to the Dar of your spell when it was initially cast, or what it was when you last zoned (whichever is more recent).* |
| *[ticks](datatype-ticks.md)*       | **Duration**  | The time remaining before the buff fades (not total duration)                                                                                                                                                                    |
| *[int](datatype-int.md)*           | **ID**        | The ID of the buff or shortbuff slot                                                                                                                                                                                             |
| *[int](datatype-int.md)*           | **Level**     | The level of the person that cast the buff on you (not the level of the spell)                                                                                                                                                   |
| *[float](datatype-float.md)*       | **Mod**       | The modifier to a bard song                                                                                                                                                                                                      |
| *[action](datatype-action.md)*     | **Remove**    | Removes the named/partial name buff                                                                                                                                                                                              |
| *[spell](datatype-spell.md)*       | **Spell**     | The spell                                                                                                                                                                                                                        |
| '**'[string](datatype-string.md)** | **To String** | Same as Name                                                                                                                                                                                                                     |

## Examples

` ${Me.Buff[Credence].Remove}`

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [DataType:character](datatype-character.md)


