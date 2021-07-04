## Description

Contains all the data related to alternate abilities

## Members

|                                            |                           |                                                                 |
|--------------------------------------------|---------------------------|-----------------------------------------------------------------|
| **Type**                                   | **Member**                | **Description**                                                 |
| *[int](datatype-int.md)*           | **AARankRequired**        | Rank required to train                                          |
| *[bool](datatype-bool.md)*         | **CanTrain**              | Returns true/false on if the Alternative Ability can be trained |
| *[int](datatype-int.md)*           | **Cost**                  | Base cost to train                                              |
| *[string](datatype-string.md)*     | **Description**           | Basic description                                               |
| *[int](datatype-int.md)*           | **ID**                    | ID                                                              |
| *[int](datatype-int.md)*           | **Index**                 | Returns the index number of the Alternative Ability             |
| *[int](datatype-int.md)*           | **MaxRank**               | Max rank available in this ability                              |
| *[int](datatype-int.md)*           | **MinLevel**              | Minimum level to train                                          |
| *[int](datatype-int.md)*           | **MyReuseTime**           | Reuse time with any hastened AA abilties                        |
| *[string](datatype-string.md)*     | **Name**                  | Name                                                            |
| *[int](datatype-int.md)*           | **NextIndex**             | Returns the next index number of the Alternative Ability        |
| *[int](datatype-int.md)*           | **PointsSpent**           | Returns the amount of points spent on an AA                     |
| *[bool](datatype-bool.md)*         | **Passive**               | Returns true/false on if the Alternative Ability is passive     |
| *altability*                               | **RequiresAbility**       | Required ability (if any)                                       |
| *[int](datatype-int.md)*           | **Rank**                  | Returns the Rank of the AA                                      |
| *[int](datatype-int.md)*           | **RequiresAbilityPoints** | Points required in above ability                                |
| *[int](datatype-int.md)*           | **ReuseTime**             | Reuse time in seconds                                           |
| *[string](datatype-string.md)*     | **ShortName**             | Short name                                                      |
| *[spell](datatype-spell.md)*       | **Spell**                 | Spell used by the ability (if any)                              |
| *[int](datatype-int.md)*           | **Type**                  | Type (1-6)                                                      |
| '**'[string](datatype-string.md)** | **To String**             | Same as **Name**                                                |

### Example

|                                                                                                           |                                                                                 |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Example/Usage**                                                                                         | **Output/Result**                                                               |
| ''/if (${AltAbility\[Companion's Aegis\].CanTrain}) /alt buy ${AltAbility\[Companion's Aegis\].NextIndex} | ''' if the AA "Companion's Aegis" can be trained, buy the next index/rank of it |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:AltAbility](../top-level-objects/tlo-altability.md)
-   [DataType:character](datatype-character.md)


