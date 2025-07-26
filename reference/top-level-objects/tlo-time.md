---
tags:
    - tlo
---
# `Time`

<!--tlo-desc-start-->
Object used to return information on real time, not game time.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='time', name='Time') }}
<!--tlo-forms-end-->

## Associated DataTypes

## [time](../data-types/datatype-time.md)
{%
  include-markdown "reference/data-types/datatype-time.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-time.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-time.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-time.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

```
/echo ${Time.DayOfWeek}
```

Returns the day of the week
<!--tlo-linkrefs-start-->
[time]: ../data-types/datatype-time.md
<!--tlo-linkrefs-end-->
