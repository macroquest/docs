---
tags:
    - tlo
---
# `MacroQuest`

<!--tlo-desc-start-->
Creates an object related to MacroQuest information.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='macroquest', name='MacroQuest') }}
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [macroquest](../data-types/datatype-macroquest.md)
{%
  include-markdown "reference/data-types/datatype-macroquest.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-macroquest.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-macroquest.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-macroquest.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->

## Usage

```
/echo ${MacroQuest.LastTell}
```

Returns the name of the last person that sent you a tell.

<!--tlo-linkrefs-start-->
[macroquest]: ../data-types/datatype-macroquest.md
<!--tlo-linkrefs-end-->
