---
tags:
    - tlo
---
# `Float`

<!--tlo-desc-start-->
Creates a float object from n.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='float', name='Float', params='n') }}

:   Returns a float with value _n_.
<!--tlo-forms-end-->

## Usage

```
/echo ${Float[12.345].Deci}
```

Creates a float object of 12.345 and truncates the decimal to one decimal place.
<!--tlo-linkrefs-start-->
[float]: ../data-types/datatype-float.md
<!--tlo-linkrefs-end-->
