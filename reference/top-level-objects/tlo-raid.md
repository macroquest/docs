---
tags:
    - tlo
---
# `Raid`

<!--tlo-desc-start-->
Object that has access to members that provide information on your raid.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='raid', name='Raid') }}
<!--tlo-forms-end-->

## Associated DataTypes

## [raid](../data-types/datatype-raid.md)
{%
  include-markdown "reference/data-types/datatype-raid.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-raid.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-raid.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-raid.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## [raidmember](../data-types/datatype-raidmember.md)
{%
  include-markdown "reference/data-types/datatype-raidmember.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-raidmember.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-raidmember.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-raidmember.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

```
/echo ${Raid.Members}
```

Echos the number of members in your raid

<!--tlo-linkrefs-start-->
[raid]: ../data-types/datatype-raid.md
<!--tlo-linkrefs-end-->