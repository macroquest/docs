---
tags:
    - tlo
---
# `DynamicZone`

<!--tlo-desc-start-->
Provides access to properties of the current dynamic (instanced) zone.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='dynamiczone', name='DynamicZone') }}

:   Gives access to the information about the current dynamic zone.
<!--tlo-forms-end-->

## Associated DataTypes

## [dynamiczone](../data-types/datatype-dynamiczone.md)
{%
  include-markdown "reference/data-types/datatype-dynamiczone.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-dynamiczone.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-dynamiczone.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-dynamiczone.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## [dzmember](../data-types/datatype-dzmember.md)
{%
  include-markdown "reference/data-types/datatype-dzmember.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-dzmember.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-dzmember.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-dzmember.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## [dztimer](../data-types/datatype-dztimer.md)
{%
  include-markdown "reference/data-types/datatype-dztimer.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-dztimer.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-dztimer.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-dztimer.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## Usage

!!! example

    Echo the name of the dynamic zone

    ```
    /echo ${DynamicZone.Name}
    ```

<!--tlo-linkrefs-start-->
[dynamiczone]: ../data-types/datatype-dynamiczone.md
<!--tlo-linkrefs-end-->
