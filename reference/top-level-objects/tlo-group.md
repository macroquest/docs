---
tags:
    - tlo
---
# `Group`

<!--tlo-desc-start-->
Access to all group-related information.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='group', name='Group') }}

:   Retrieve information about your group
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [group](../data-types/datatype-group.md)
{%
  include-markdown "reference/data-types/datatype-group.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-group.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-group.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-group.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## [groupmember](../data-types/datatype-groupmember.md)
{%
  include-markdown "reference/data-types/datatype-groupmember.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-groupmember.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-groupmember.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-groupmember.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->

## Usage

```
/echo ${Group.Leader.ID}
```

Echo Groupleader ID, if any.

```
/echo ${Group.Member[0]}
```

Echos your own name

```
/echo ${Group.Member[1]}
```

Echos the next person on the list, after yourself.
<!--tlo-linkrefs-start-->
[bool]: ../data-types/datatype-bool.md
[group]: ../data-types/datatype-group.md
[groupmember]: ../data-types/datatype-groupmember.md
[int]: ../data-types/datatype-int.md
[spawn]: ../data-types/datatype-spawn.md
[string]: ../data-types/datatype-string.md
<!--tlo-linkrefs-end-->
