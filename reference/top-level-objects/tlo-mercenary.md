---
tags:
    - tlo
---
# `Mercenary`

<!--tlo-desc-start-->
Object used to get information about your mercenary.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='mercenary', name='Mercenary') }}
<!--tlo-forms-end-->

## Associated DataTypes

## [mercenary](../data-types/datatype-mercenary.md)
{%
  include-markdown "reference/data-types/datatype-mercenary.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-mercenary.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-mercenary.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-mercenary.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## Usage

```
/echo ${Mercenary.Stance}
```

Displays the current stance of the mercenary based on the type (Passive, Balanced, Aggressive, etc.)

```
/echo ${Mercenary.State}
```

Displays whether the mercenary is suspended or not.
<!--tlo-linkrefs-start-->
[mercenary]: ../data-types/datatype-mercenary.md
<!--tlo-linkrefs-end-->