---
tags:
    - tlo
---
# `AltAbility`

<!--tlo-desc-start-->
!!! danger

    This AltAbility TLO is for accessing the full database of alternate abilities.

    If you want to access alternate abilities associated with your character, use `Me.AltAbility` instead.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='altability', name='AltAbility', params='Number') }}

:   Look up an AltAbility by its altability id.

### {{ renderMember(type='altability', name='AltAbility', params='Name') }}

:   Look up an AltAbility by its name.
<!--tlo-forms-end-->

## Usage

=== "MQScript"

    ```
    | Prints the pre-requisite AA ability needed to train Combat Stability
    /echo ${AltAbility[Combat Stability].RequiresAbility}
    ```

=== "Lua"

    ```lua
    -- Prints the pre-requisite AA ability needed to train Combat Stability
    print(mq.TLO.AltAbility('Combat Stability').RequiresAbility())
    ```
<!--tlo-linkrefs-start-->
[altability]: ../data-types/datatype-altability.md
<!--tlo-linkrefs-end-->
