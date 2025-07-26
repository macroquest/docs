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

## Associated DataTypes

## [altability](../data-types/datatype-altability.md)
{%
  include-markdown "reference/data-types/datatype-altability.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-altability.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-altability.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-altability.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

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
