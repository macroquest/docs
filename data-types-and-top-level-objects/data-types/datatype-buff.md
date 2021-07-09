# DataType:buff

This is the type for any buffs currently affecting you, both long duration and short duration buffs.

## Members

This type inherits members from [_spell_](datatype-spell.md).

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Counters** | The number of counters added by the buff |
| [_int_](datatype-int.md) | **Dar** | The remaining damage absorption of the buff \(if any\). _This is not entirely accurate, it will only show you to the Dar of your spell when it was initially cast, or what it was when you last zoned \(whichever is more recent\)._ |
| [_ticks_](datatype-ticks.md) | **Duration** | The time remaining before the buff fades \(not total duration\) |
| [_int_](datatype-int.md) | **ID** | The ID of the buff or shortbuff slot |
| [_int_](datatype-int.md) | **Level** | The level of the person that cast the buff on you \(not the level of the spell\) |
| [_float_](datatype-float.md) | **Mod** | The modifier to a bard song |
| [_spell_](datatype-spell.md) | **Spell** | The spell |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | Same as Name |

## Methods

| Name | Action |
| :--- | :--- |
| **Remove** | Removes the named/partial name buff |

## Examples

`${Me.Buff[Credence].Remove}`

