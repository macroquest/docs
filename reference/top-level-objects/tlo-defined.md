---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Defined`

Determines whether a variable, array, or timer with this name exists. The variable, array or timer must not be enclosed with ${}.

## Forms

[_bool_](../data-types/datatype-bool.md) **Defined**[_name_]

:   Returns true if the given variable _name_ is defined.

## Examples

```
/if (${Defined[varname]}) {
    /echo ${varname}
}
```
