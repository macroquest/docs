## Description

Pet object

## Members

|                                        |                              |                                                                   |
|----------------------------------------|------------------------------|-------------------------------------------------------------------|
| **Type**                               | **Member**                   | **Description**                                                   |
| *[int](datatype-int.md)*       | **Buff\[buffname\]**         | Returns the slot# for buffname                                    |
| *[string](datatype-string.md)* | **Buff\[slot#\]**            | Prints name of the buff at slot#                                  |
| *[bool](datatype-bool.md)*     | **Combat**                   | Combat state                                                      |
| *[bool](datatype-bool.md)*     | **GHold**                    | GHold state                                                       |
| *[bool](datatype-bool.md)*     | **Hold**                     | Hold state                                                        |
| *[bool](datatype-bool.md)*     | **ReGroup**                  | ReGroup state                                                     |
| *[string](datatype-string.md)* | **Stance**                   | Returns the pet's current stance, (e.g. FOLLOW, GUARD)            |
| *[bool](datatype-bool.md)*     | **Stop**                     | Stop state                                                        |
| *[spawn](datatype-spawn.md)*   | **Target**                   | Returns the pet's current target.                                 |
| *[bool](datatype-bool.md)*     | **Taunt**                    | Taunt state                                                       |
| *[int](datatype-int.md)*       | **BuffDuration\[buffname\]** | Buff time remaining for pet buff \[buffname\] in miliseconds      |
| *[int](datatype-int.md)*       | **BuffDuration\[slot#\]**    | Buff time remaining for pet buff in slot \[slot#\] in miliseconds |
| *[bool](datatype-bool.md)*     | **Focus**                    | Focus state                                                       |

## Forms

-   *[pet](datatype-pet.md)* **Pet**

## Access to Types

-   *[pet](datatype-pet.md)* **pet**
-   *[spawn](datatype-spawn.md)* **spawn**

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Pet](../top-level-objects/tlo-pet.md)


