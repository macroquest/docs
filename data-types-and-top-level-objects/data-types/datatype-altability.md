# DataType:altability

Contains all the data related to alternate abilities

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **AARankRequired** | Rank required to train |
| [_bool_](datatype-bool.md) | **CanTrain** | Returns true/false on if the Alternative Ability can be trained |
| [_int_](datatype-int.md) | **Cost** | Base cost to train |
| \_\_[_string_](datatype-string.md)\_\_ | **Description** | Basic description |
| [_int_](datatype-int.md) | **ID** | ID |
| [_int_](datatype-int.md) | **Index** | Returns the index number of the Alternative Ability |
| [_int_](datatype-int.md) | **MaxRank** | Max rank available in this ability |
| [_int_](datatype-int.md) | **MinLevel** | Minimum level to train |
| [_int_](datatype-int.md) | **MyReuseTime** | Reuse time with any hastened AA abilties |
| \_\_[_string_](datatype-string.md)\_\_ | **Name** | Name |
| [_int_](datatype-int.md) | **NextIndex** | Returns the next index number of the Alternative Ability |
| [_int_](datatype-int.md) | **PointsSpent** | Returns the amount of points spent on an AA |
| [_bool_](datatype-bool.md) | **Passive** | Returns true/false on if the Alternative Ability is passive |
| \_\_[_altability_](datatype-altability.md)\_\_ | **RequiresAbility** | Required ability \(if any\) |
| [_int_](datatype-int.md) | **Rank** | Returns the Rank of the AA |
| [_int_](datatype-int.md) | **RequiresAbilityPoints** | Points required in above ability |
| [_int_](datatype-int.md) | **ReuseTime** | Reuse time in seconds |
| \_\_[_string_](datatype-string.md)\_\_ | **ShortName** | Short name |
| [_spell_](datatype-spell.md) | **Spell** | Spell used by the ability \(if any\) |
| [_int_](datatype-int.md) | **Type** | Type \(1-6\) |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | Same as **Name** |

### Example:

If the AA "Companion's Aegis" can be trained, buy the next index/rank of it

{% tabs %}
{% tab title="MQScript" %}
```text
/if (${AltAbility[Companion's Aegis].CanTrain}) {
    /alt buy ${AltAbility[Companion's Aegis].NextIndex}
}
```
{% endtab %}

{% tab title="Lua" %}
```lua
if mq.TLO.AltAbility("Companion's Aegis").CanTrain() then
    mq.cmd.alt('buy '..mq.TLO.AltAbility("Companion's Aegis").NextIndex()
end
```
{% endtab %}
{% endtabs %}

