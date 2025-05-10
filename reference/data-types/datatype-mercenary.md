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

### {{ renderMember(type='int', name='AAPoints') }}

:   AA Points spent on mercenary abilities

### {{ renderMember(type='string', name='Index') }}

:   Index

### {{ renderMember(type='string', name='Name') }}

:   Name of the mercenary

### {{ renderMember(type='string', name='Stance') }}

:   Current stance of the mercenary

### {{ renderMember(type='string', name='State') }}

:   Current state of the mercenary:

    - "DEAD"
    - "SUSPENDED"
    - "ACTIVE"
    - "UNKNOWN"

### {{ renderMember(type='int', name='StateID') }}

:   Current state ID of the mercenary as a number.

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
