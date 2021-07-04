# DataType:CachedBuff

## Description

Allows checking if cached buffs on others have expired with out targeting

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_string_](datatype-string.md) | **CasterName** | Returns the name of the caster who applied the cached buff |
| [_int_](datatype-int.md) | **Count** | Returns the amount of buffs catched, or -1 it none |
| [_int_](datatype-int.md) | **Duration** | Returns the duration of the cached buff |
| [_int_](datatype-int.md) | **Slot** | Returns the buff slot the target had the buff in |
| [_int_](datatype-int.md) | **SpellID** | Returns the buff's spell ID |
|  |  |  |

### Example

-Previously Added: .CachedBuffCount to the spawn tlo. it returns -1 if no buffs are cached for the spawn or number of buffs cached.

-Previously Added: .CachedBuff\[x\] to the spawn tlo where x is a spellid if its a number and a spell name if not. It returns a MQ2CachedBuffType.

-Previously Added: .CachedBuff\[\#x\] to the spawn tlo where \#x is a buffslot between 1-97. It returns a MQ2CachedBuffType.

-Previously Added: .CachedBuff\[\*x\] to the spawn tlo where \*x is a index \(buffslots are not sorted\). It returns a MQ2CachedBuffType.

-Previously Added: .CachedBuff\[^x\] to the spawn tlo where ^x is a keyword. It returns a MQ2CachedBuffType.

`^x keywords: Slowed Rooted Mezzed Crippled Maloed Tashed Snared and Beneficial`

-Using CachedBuff to get buff info on targets, group members etc, only requires you to target the entity once. after thats done, buffs are cached. -The upside is obviously that we don't have to target back and forth constantly.

`Usage: well lets say you are a druid and you want to know if a group members sow buff has worn off, you can just check CachedBuff without having to retarget the group member.`  
`/echo ${Group.Member[2].CachedBuff[Spirit of Wolf].Duration}`

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Spawn](../top-level-objects/tlo-spawn.md)

