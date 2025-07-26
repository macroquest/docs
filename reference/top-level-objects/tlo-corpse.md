---
tags:
    - tlo
---
# `Corpse`

<!--tlo-desc-start-->
Access to objects of type corpse, which is the currently active corpse (ie. the one you are looting).
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='corpse', name='Corpse') }}

:   Corpse you are looting.
<!--tlo-forms-end-->

## Associated DataTypes

## [corpse](../data-types/datatype-corpse.md)
{%
  include-markdown "reference/data-types/datatype-corpse.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-corpse.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-corpse.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-corpse.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

```
/if (${Corpse.Open}) {
    /echo Corpse is open, proceeding with looting
}
```
<!--tlo-linkrefs-start-->
[corpse]: ../data-types/datatype-corpse.md
<!--tlo-linkrefs-end-->
