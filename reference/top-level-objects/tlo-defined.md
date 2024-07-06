---
tags:
    - tlo
---
# `Defined`

Determines whether a variable, array, or timer with this name exists. The variable, array or timer must not be enclosed with ${}.

## Forms

### {{ renderMember(type='bool', name='Defined', params='Name') }}

:   Returns true if the given variable _name_ is defined.


## Usage

```
/if (${Defined[varname]}) {
    /echo ${varname}
}
```

[bool]: ../data-types/datatype-bool.md
