---
tags:
    - tlo
---
# `Alert`

<!--tlo-desc-start-->
Provides access to spawn search filter criteria in alerts. Alerts are created using [/alert](../../reference/commands/alert.md).
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='alert', name='Alert', params='ID') }}

:   Retrieve information for the alert category by its id

### {{ renderMember(type='string', name='Alert') }}

:   Returns pipe `|` separated list of alert ids
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [alert](../data-types/datatype-alert.md)
{%
  include-markdown "reference/data-types/datatype-alert.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-alert.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-alert.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-alert.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## [alertlist](../data-types/datatype-alertlist.md)
{%
  include-markdown "reference/data-types/datatype-alertlist.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-alertlist.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-alertlist.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-alertlist.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->

## Usage

=== "MQScript"

    ```
    | Add an alert entry for Fippy to Alert list 1
    /alert add 1 Fippy

    | Will output 'Fippy'
    /echo ${Alert[1].List[0].Name}

    | Add an alert entry using our Spawn ID
    /alert add 1 id ${Me.ID}

    | Will output your Spawn ID
    /echo ${Alert[1].List[1].SpawnID}

    | Will output the number of alerts in list 1
    /echo ${Alert[1].Size}
    ```

=== "Lua"

    ```lua
    -- Add an alert entry for Fippy to Alert list 1
    mq.cmd('/alert add 1 Fippy')

    -- Will output 'Fippy'
    print(mq.TLO.Alert(1).List(0).Name())

    -- Add an alert entry using our Spawn ID
    mq.cmdf('/alert add 1 id %d', mq.TLO.Me.ID())

    -- Will output our Spawn ID
    print(mq.TLO.Alert(1).List(1).SpawnID())

    -- Will output the number of alerts in list 1
    print(mq.TLO.Alert(1).Size())
    ```
<!--tlo-linkrefs-start-->
[alert]: ../data-types/datatype-alert.md
[alertlist]: ../data-types/datatype-alertlist.md
[bool]: ../data-types/datatype-bool.md
[double]: ../data-types/datatype-double.md
[float]: ../data-types/datatype-float.md
[int]: ../data-types/datatype-int.md
[int64]: ../data-types/datatype-int64.md
[spawn]: ../data-types/datatype-spawn.md
[string]: ../data-types/datatype-string.md
<!--tlo-linkrefs-end-->
