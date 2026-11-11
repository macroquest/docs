---
tags:
    - datatype
---
# `mercenary`

<!--dt-desc-start-->
This is the type used for mercenaries.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
This type inherits members from [_spawn_](datatype-spawn.md).

/// member | int AAPoints
AA Points spent on mercenary abilities
///

/// member | string Index
Index
///

/// member | string Name
Name of the mercenary
///

/// member | string Stance
Current stance of the mercenary
///

/// member | string State
Current state of the mercenary:

- "DEAD"
- "SUSPENDED"
- "ACTIVE"
- "UNKNOWN"
///

/// member | int StateID
Current state ID of the mercenary as a number.
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

## Examples

!!! Example

    Check on if you have an active mercenary, mercenary is a cleric, and if it's stance is NOT reactive.... then change it TO reactive.

    ```text
    /if (${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Class.Name.Equal[Cleric]} && ${Mercenary.Stance.NotEqual[REACTIVE]}) {
        /stance reactive
    }
    ```
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
