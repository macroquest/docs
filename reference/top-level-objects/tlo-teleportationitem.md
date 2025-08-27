---
tags:
  - tlo
---
# `TeleportationItem`

<!--tlo-desc-start-->
Returns data on the teleportation item in your keyring.
<!--tlo-desc-end-->

## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='keyringitem', name='TeleportationItem', params='#') }}

:   Retrieves the item in your keyring by index

### {{ renderMember(type='keyringitem', name='TeleportationItem', params='name') }}

:   Retrieves the item in your keyring by name. A = can be prepended for an exact match.

### {{ renderMember(type='keyring', name='TeleportationItem') }}

:   

<!--tlo-forms-end-->

## Associated DataTypes
## [`keyring`](../data-types/datatype-keyring.md)
{% include-markdown "reference/data-types/datatype-keyring.md" start="<!--dt-desc-start-->" end="<!--dt-desc-end-->" trailing-newlines=false %} {{ readMore('reference/data-types/datatype-keyring.md') }}
:    <h3>Members</h3>
    {% include-markdown "reference/data-types/datatype-keyring.md" start="<!--dt-members-start-->" end="<!--dt-members-end-->" %}
    {% include-markdown "reference/data-types/datatype-keyring.md" start="<!--dt-linkrefs-start-->" end="<!--dt-linkrefs-end-->" %}

## [`keyringitem`](../data-types/datatype-keyringitem.md)
{% include-markdown "reference/data-types/datatype-keyringitem.md" start="<!--dt-desc-start-->" end="<!--dt-desc-end-->" trailing-newlines=false %} {{ readMore('reference/data-types/datatype-keyringitem.md') }}
:    <h3>Members</h3>
    {% include-markdown "reference/data-types/datatype-keyringitem.md" start="<!--dt-members-start-->" end="<!--dt-members-end-->" %}
    {% include-markdown "reference/data-types/datatype-keyringitem.md" start="<!--dt-linkrefs-start-->" end="<!--dt-linkrefs-end-->" %}

    <!--tlo-linkrefs-start-->
    [keyring]: ../data-types/datatype-keyring.md
    [keyringitem]: ../data-types/datatype-keyringitem.md
    <!--tlo-linkrefs-end-->