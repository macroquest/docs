---
tags:
    - tlo
---
# `Ground`

<!--tlo-desc-start-->
Object which references the ground spawn item you have targeted.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='ground', name='Ground') }}

:   Access currently targeted ground item.
<!--tlo-forms-end-->

## Associated DataTypes

## [ground](../data-types/datatype-ground.md)
{%
  include-markdown "reference/data-types/datatype-ground.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-ground.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-ground.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-ground.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## Usage

```
/echo ${Ground.Distance}
```

Echos the distance to the ground item you have targeted.
<!--tlo-linkrefs-start-->
[ground]: ../data-types/datatype-ground.md
<!--tlo-linkrefs-end-->
