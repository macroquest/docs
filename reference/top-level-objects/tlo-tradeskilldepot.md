---
tags:
    - tlo
---
# `TradeskillDepot`

<!--tlo-desc-start-->
Object that interacts with the personal tradeskill depot, introduced in the Night of Shadows expansion.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='tradeskilldepot', name='TradeskillDepot') }}
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [tradeskilldepot](../data-types/datatype-tradeskilldepot.md)
{%
  include-markdown "reference/data-types/datatype-tradeskilldepot.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-tradeskilldepot.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-tradeskilldepot.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-tradeskilldepot.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->
## Examples

```
/echo ${TradeskillDepot.SelectedItem}
```

Echos the name of the currently selected item in the tradeskill depot window.
<!--tlo-linkrefs-start-->
[tradeskilldepot]: ../data-types/datatype-tradeskilldepot.md
<!--tlo-linkrefs-end-->
