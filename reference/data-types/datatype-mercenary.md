# DataType:mercenary

This is the type used for mercenaries.

## Members

This type inherits members from [_spawn_](datatype-spawn.md).

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **AAPoints** | AA Points spent on mercenary abilities |
| \_\_[_string_](datatype-string.md)\_\_ | **Stance** | Current stance of the mercenary |
| \_\_[_string_](datatype-string.md)\_\_ | **State** | Current state of the mercenary \(returns "DEAD","SUSPENDED","ACTIVE", or "UNKNOWN" |
| [_int_](datatype-int.md) | **StateID** | Current state ID of the mercenary as a number. |
| \_\_[_string_](datatype-string.md)\_\_ | **Index** | Index |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | Same as **Name** |

## Examples

Check on if you have an active mercenary, mercenary is a cleric, and if it's stance is NOT reactive.... then change it TO reactive.

```text
/if (${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Class.Name.Equal[Cleric]} && ${Mercenary.Stance.NotEqual[REACTIVE]}) {
    /stance reactive
}
```

