---
tags:
    - tlo
---
# `DisplayItem`

<!--tlo-desc-start-->
Gives information on item windows
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='DisplayItem', name='DisplayItem') }}

### {{ renderMember(type='DisplayItem', name='DisplayItem', params='x') }}
:   Valid range 1-6. Returns information on one of the 6 possible item windows open.

### {{ renderMember(type='DisplayItem', name='DisplayItem', params='<itemname>') }}
:   Return the Item display window for the specified item name, if one exists.
<!--tlo-forms-end-->

## Associated DataTypes

## [DisplayItem](datatype-displayitem.md)
{%
  include-markdown "plugins/core-plugins/itemdisplay/datatype-displayitem.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/itemdisplay/datatype-displayitem.md') }}

<h2>Members</h2>
{%
  include-markdown "plugins/core-plugins/itemdisplay/datatype-displayitem.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "plugins/core-plugins/itemdisplay/datatype-displayitem.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

<!--tlo-linkrefs-start-->
[DisplayItem]: datatype-displayitem.md
<!--tlo-linkrefs-end-->
