---
tags:
    - tlo
---
# `Merchant`

<!--tlo-desc-start-->
Object that interacts with the currently active merchant.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='merchant', name='Merchant') }}
<!--tlo-forms-end-->

## Associated DataTypes

## [merchant](../data-types/datatype-merchant.md)
{%
  include-markdown "reference/data-types/datatype-merchant.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-merchant.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-merchant.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-merchant.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

```
/echo ${Merchant.Name}
```

Echos the name of the currently open merchant.
<!--tlo-linkrefs-start-->
[merchant]: ../data-types/datatype-merchant.md
<!--tlo-linkrefs-end-->