---
tags:
    - tlo
---
# `Spell`

<!--tlo-desc-start-->
Object used to return information on a spell by name or by ID.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='spell', name='Spell') }}

:   Find spell by ID

### {{ renderMember(type='spell', name='Spell', params='Name') }}

:   Find spell by name
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [spell](../data-types/datatype-spell.md)
{%
  include-markdown "reference/data-types/datatype-spell.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-spell.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-spell.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-spell.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->

## Usage

```
/echo ${Spell[Splurt].ID}
```

Will return 1620

```
/echo ${Spell[1620].Duration}
```

Will return 16 (ie. 16 ticks)
<!--tlo-linkrefs-start-->
[spell]: ../data-types/datatype-spell.md
<!--tlo-linkrefs-end-->
