---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `altability`

Contains all the data related to alternate abilities

## Members

| **Type**                                   | **Member**                | **Description**                                                           |
| ------------------------------------------ | ------------------------- | ------------------------------------------------------------------------- |
| [_int_](datatype-int.md)                   | **AARankRequired**        | Rank required to train                                                    |
| [_bool_](datatype-bool.md)                 | **CanTrain**              | Returns true/false on if the Alternative Ability can be trained           |
| [_string_](datatype-string.md)             | **Category**              | The name of the category that this AA belongs to.                         |
| [_int_](datatype-int.md)                   | **Cost**                  | Base cost to train                                                        |
| [_string_](datatype-string.md)             | **Description**           | Basic description                                                         |
| [_int_](datatype-int.md)                   | **Expansion**             | Expansion level for the ability.                                          |
| [_int_](datatype-int.md)                   | **Flags**                 | Flags value (Currently unknown?).                                         |
| [_int_](datatype-int.md)                   | **GroupID**               | ID of the AA group that this AA belongs to                                |
| [_int_](datatype-int.md)                   | **ID**                    | ID                                                                        |
| [_int_](datatype-int.md)                   | **Index**                 | Returns the index number of the Alternative Ability                       |
| [_int_](datatype-int.md)                   | **MaxRank**               | Max rank available in this ability                                        |
| [_int_](datatype-int.md)                   | **MinLevel**              | Minimum level to train                                                    |
| [_int_](datatype-int.md)                   | **MyReuseTime**           | Reuse time (in seconds) that takes into account any hastened AA abilities |
| [_string_](datatype-string.md)             | **Name**                  | Name                                                                      |
| [_int_](datatype-int.md)                   | **NextIndex**             | Returns the next index number of the Alternative Ability                  |
| [_int_](datatype-int.md)                   | **PointsSpent**           | Returns the amount of points spent on an AA                               |
| [_bool_](datatype-bool.md)                 | **Passive**               | Returns true/false on if the Alternative Ability is passive               |
| [_int_](datatype-int.md)                   | **Rank**                  | Returns the Rank of the AA                                                |
| [_altability_](datatype-altability.md)     | **RequiresAbility**       | Required ability (if any)                                                 |
| [_int_](datatype-int.md)                   | **RequiresAbilityPoints** | Points required in above ability                                          |
| [_int_](datatype-int.md)                   | **ReuseTime**             | Reuse time in seconds                                                     |
| [_string_](datatype-string.md)             | **ShortName**             | First line of button label (if any)                                       |
| [_string_](datatype-string.md)             | **ShortName2**            | Second line of button label (if any)                                      |
| [_spell_](datatype-spell.md)               | **Spell**                 | Spell used by the ability (if any)                                        |
| [_int_](datatype-int.md)                   | **Type**                  | Type (1-6)                                                                |
| [_string_](datatype-string.md)             | **To String**             | Same as **Name**                                                          |

### Example:

If the AA "Companion's Aegis" can be trained, buy the next index/rank of it

=== "MQScsript"

    ```
    /if (${AltAbility[Companion's Aegis].CanTrain}) {
        /alt buy ${AltAbility[Companion's Aegis].NextIndex}
    }
    ```

=== "Lua"

    ```lua
    if mq.TLO.AltAbility("Companion's Aegis").CanTrain() then
        mq.cmd.alt('buy '..mq.TLO.AltAbility("Companion's Aegis").NextIndex())
    end
    ```
