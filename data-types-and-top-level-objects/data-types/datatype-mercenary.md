# DataType:mercenary

## Description

This is the type used for mercenaries.

This type inherits no other types.

* [_spawn_](datatype-spawn.md) **spawn**

## Members

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| **Type** | **Member** | **Description** | **Example** |
| [_int_](datatype-int.md) | **AAPoints** | AA Points spent on mercenary abilities | ${Mercenary.AAPoints} |
| [_string_]() | **Stance** | Current stance of the mercenary | ${Mercenary.Stance.Equal\[Balanced\]} |
| [_string_]() | **State** | Current state of the mercenary \(returns "DEAD","SUSPENDED","ACTIVE", or "UNKNOWN" | ${Mercenary.State.Equal\[SUSPENDED\]} |
| [_int_](datatype-int.md) | **StateID** | Current state ID of the mercenary as a number. | ${Mercenary.StateID} |
| [_string_]() | **Index** | Index | ${Mercenary.Index} |
| '**'**[**string**]() | **To String** | Same as **Name** |  |

## Examples

Check on if you have an active mercenary, mercenary is a cleric, and if it's stance is NOT reactive.... then change it TO reactive.

`/if (${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Class.Name.Equal[Cleric]} && ${Mercenary.Stance.NotEqual[REACTIVE]}) {`  
`/stance reactive`  
`}`

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [Spawn Search](../../general-information/spawn-search.md)
* [DataType:spawn](datatype-spawn.md)

