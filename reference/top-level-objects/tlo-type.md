---
tags:
    - tlo
---
# `Type`

<!--tlo-desc-start-->
Used to get information on data types.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='type', name='Type', params='Name') }}

:   Retrieve metadata about the type with given `Name`
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [type](../data-types/datatype-type.md)
{%
  include-markdown "reference/data-types/datatype-type.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-type.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-type.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-type.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->
## Usage

Determines if a member of a type exists:

```
/echo ${Type[spawn].Member[ID]}
```

Enumerate members of a type using a loop:

```
/for n 1 to 100
    /echo ${Type[spawn].Member[${n}]}
/next n
```
<!--tlo-linkrefs-start-->
[type]: ../data-types/datatype-type.md
<!--tlo-linkrefs-end-->
