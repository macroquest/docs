---
tags:
    - tlo
---
# `Defined`

<!--tlo-desc-start-->
Determines whether a variable, array, or timer with this name exists. The variable, array or timer must not be enclosed with ${}.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='bool', name='Defined', params='Name') }}

:   Returns true if the given variable _name_ is defined.
<!--tlo-forms-end-->

## Usage

```
/if (${Defined[varname]}) {
    /echo ${varname}
}
```
<!--tlo-linkrefs-start-->
[bool]: ../data-types/datatype-bool.md
<!--tlo-linkrefs-end-->
