---
tags:
  - tlo
---
# `PointMerchant`

<!--tlo-desc-start-->
Access to point merchants (such as those found in LDoN) when a window is open.
<!--tlo-desc-end-->

## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='pointmerchant', name='PointMerchant') }}

:   Returns TRUE if point merchant window is open

<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [`pointmerchant`](../data-types/datatype-pointmerchant.md)
{% include-markdown "reference/data-types/datatype-pointmerchant.md" start="<!--dt-desc-start-->" end="<!--dt-desc-end-->" trailing-newlines=false %} {{ readMore('reference/data-types/datatype-pointmerchant.md') }}

<h3>Members</h3>
{% include-markdown "reference/data-types/datatype-pointmerchant.md" start="<!--dt-members-start-->" end="<!--dt-members-end-->" %}
{% include-markdown "reference/data-types/datatype-pointmerchant.md" start="<!--dt-linkrefs-start-->" end="<!--dt-linkrefs-end-->" %}


## [`pointmerchantitem`](../data-types/datatype-pointmerchantitem.md)
{% include-markdown "reference/data-types/datatype-pointmerchantitem.md" start="<!--dt-desc-start-->" end="<!--dt-desc-end-->" trailing-newlines=false %} {{ readMore('reference/data-types/datatype-pointmerchantitem.md') }}

<h3>Members</h3>
{% include-markdown "reference/data-types/datatype-pointmerchantitem.md" start="<!--dt-members-start-->" end="<!--dt-members-end-->" %}
{% include-markdown "reference/data-types/datatype-pointmerchantitem.md" start="<!--dt-linkrefs-start-->" end="<!--dt-linkrefs-end-->" %}
<!--tlo-datatypes-end-->

## Examples

!!! example
    `/echo ${PointMerchant.Item[1].Price}`
    `/echo ${PointMerchant.Item[Ebon Hammer].Price}`
    : Returns the Price for index 1 or whatever index Ebon Hammer is in if you do it by name.

<!--tlo-linkrefs-start-->
[pointmerchant]: ../data-types/datatype-pointmerchant.md
<!--tlo-linkrefs-end-->