---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `mercenary`

This is the type used for mercenaries.

## Members

This type inherits members from [_spawn_](datatype-spawn.md).

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **AAPoints** | AA Points spent on mercenary abilities |
| [_string_](datatype-string.md) | **Stance** | Current stance of the mercenary |
| [_string_](datatype-string.md) | **State** | Current state of the mercenary \(returns "DEAD","SUSPENDED","ACTIVE", or "UNKNOWN" |
| [_int_](datatype-int.md) | **StateID** | Current state ID of the mercenary as a number. |
| [_string_](datatype-string.md) | **Index** | Index |
| [_string_](datatype-string.md) | **To String** | Same as **Name** |

## Examples

Check on if you have an active mercenary, mercenary is a cleric, and if it's stance is NOT reactive.... then change it TO reactive.

```text
/if (${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Class.Name.Equal[Cleric]} && ${Mercenary.Stance.NotEqual[REACTIVE]}) {
    /stance reactive
}
```

