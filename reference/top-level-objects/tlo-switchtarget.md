---
tags:
  - tlo
---
# `SwitchTarget`

<!--tlo-desc-start-->
Object used to return information on your switch target. Replaces DoorTarget
<!--tlo-desc-end-->

## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='switch', name='SwitchTarget') }}

:   True if switch (aka door) targeted

<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [`switch`](../data-types/datatype-switch.md)
{% include-markdown "reference/data-types/datatype-switch.md" start="<!--dt-desc-start-->" end="<!--dt-desc-end-->" trailing-newlines=false %} {{ readMore('reference/data-types/datatype-switch.md') }}
:    <h3>Members</h3>
    {% include-markdown "reference/data-types/datatype-switch.md" start="<!--dt-members-start-->" end="<!--dt-members-end-->" %}
    {% include-markdown "reference/data-types/datatype-switch.md" start="<!--dt-linkrefs-start-->" end="<!--dt-linkrefs-end-->" %}
    <!--tlo-datatypes-end-->

## Examples

!!! example
    `/echo ${SwitchTarget.ID}`
    : Returns the ID of the door targeted.

<!--tlo-linkrefs-start-->
[switch]: ../data-types/datatype-switch.md
<!--tlo-linkrefs-end-->