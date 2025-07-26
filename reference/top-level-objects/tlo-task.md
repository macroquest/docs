---
tags:
    - tlo
---
# `Task`

<!--tlo-desc-start-->
Object used to return information on a current Task.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='task', name='Task') }}
<!--tlo-forms-end-->

## Associated DataTypes

## [task](../data-types/datatype-task.md)
{%
  include-markdown "reference/data-types/datatype-task.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-task.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-task.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-task.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## [taskmember](../data-types/datatype-taskmember.md)
{%
  include-markdown "reference/data-types/datatype-taskmember.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-taskmember.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-taskmember.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-taskmember.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## [taskobjective](../data-types/datatype-taskobjective.md)
{%
  include-markdown "reference/data-types/datatype-taskobjective.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-taskobjective.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-taskobjective.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-taskobjective.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

```
/echo ${Task[1].Title}
```

Will return the name of the first task, or the current shared task if one exists.
<!--tlo-linkrefs-start-->
[task]: ../data-types/datatype-task.md
<!--tlo-linkrefs-end-->
