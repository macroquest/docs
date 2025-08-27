---
tags:
    - tlo
---
# `Macro`

<!--tlo-desc-start-->
Information about the macro that's currently running. 
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='macro', name='Macro') }}

:   Returns an object related to the macro that is currently running.

    !!! example

        ```
        /echo This macro has been running for: ${Macro.RunTime} seconds
        ```
<!--tlo-forms-end-->

## Associated DataTypes

## [macro](../data-types/datatype-macro.md)
{%
  include-markdown "reference/data-types/datatype-macro.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-macro.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-macro.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-macro.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

    <!--tlo-linkrefs-start-->
    [macro]: ../data-types/datatype-macro.md
    <!--tlo-linkrefs-end-->
