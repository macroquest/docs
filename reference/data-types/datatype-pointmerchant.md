---
tags:
  - datatype
---
# `pointmerchant`

<!--dt-desc-start-->
Contains information about point merchants, such as LDON merchants. Inherits [spawn](datatype-spawn.md) when merchant active.
<!--dt-desc-end-->

## Members
<!--dt-members-start-->
### {{ renderMember(type='pointmerchantitem', name='Item', params='#|name') }}

:   

### {{ renderMember(type='string', name='To String') }}

:   Returns TRUE if merchant window is visible, otherwise FALSE

<!--dt-members-end-->

## Examples

!!! example
    `/echo ${PointMerchant}`
    :  Returns true if the LDON Merchant window is open and FALSE if not.

!!! example
    `/echo ${PointMerchant.Item[1].Price}`
    : Returns the Price for index 1 or whatever index Ebon Hammer is in if you do it by name.

!!! example
    `/echo ${PointMerchant.Item[Ebon Hammer].Price}`
    : Returns the Price for Ebon Hammer.

<!--dt-linkrefs-start-->
[pointmerchantitem]: datatype-pointmerchantitem.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
