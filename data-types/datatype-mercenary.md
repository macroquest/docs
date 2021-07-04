## Description

This is the type used for mercenaries.

This type inherits no other types.

-   *[spawn](datatype-spawn.md)* **spawn**

## Members

|                                            |               |                                                                                   |                                       |
|--------------------------------------------|---------------|-----------------------------------------------------------------------------------|---------------------------------------|
| **Type**                                   | **Member**    | **Description**                                                                   | **Example**                           |
| *[int](datatype-int.md)*           | **AAPoints**  | AA Points spent on mercenary abilities                                            | ${Mercenary.AAPoints}                 |
| *[string](datatype-string.md)*     | **Stance**    | Current stance of the mercenary                                                   | ${Mercenary.Stance.Equal\[Balanced\]} |
| *[string](datatype-string.md)*     | **State**     | Current state of the mercenary (returns "DEAD","SUSPENDED","ACTIVE", or "UNKNOWN" | ${Mercenary.State.Equal\[SUSPENDED\]} |
| *[int](datatype-int.md)*           | **StateID**   | Current state ID of the mercenary as a number.                                    | ${Mercenary.StateID}                  |
| *[string](datatype-string.md)*     | **Index**     | Index                                                                             | ${Mercenary.Index}                    |
| '**'[string](datatype-string.md)** | **To String** | Same as **Name**                                                                  |                                       |

## Examples

Check on if you have an active mercenary, mercenary is a cleric, and if it's stance is NOT reactive.... then change it TO reactive.  

`/if (${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Class.Name.Equal[Cleric]} && ${Mercenary.Stance.NotEqual[REACTIVE]}) {`  
`    /stance reactive`  
`}`

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Spawn Search](../general-information/spawn-search.md)
-   [DataType:spawn](datatype-spawn.md)


