---
tags:
    - tlo
---
# `Switch`

<!--tlo-desc-start-->
Object used when you want to find information on targetted doors or switches such as the portals in PoK.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='switch', name='Switch') }}

:   Returns the currently targeted switch

### {{ renderMember(type='switch', name='Switch', params='ID') }}

:   Returns a switch matching the provided numeric ID

### {{ renderMember(type='switch', name='Switch', params='Search') }}

:   Based on the value of `Search`, return a switch:

    - `target`: Return the currently targeted switch
    - `nearest`: Return the nearest switch.
    - Otherwise, return switch by searching by name
<!--tlo-forms-end-->

## Usage

```
${Switch[foo]}
```
Access switch "foo"

```
${Switch[foo].Heading}
```
Access "foo" [_switch_](../data-types/datatype-switch.md) datatype members


### Actions on current /doortarget
```
/echo ${Switch.Heading}
/echo ${Switch.Open}
```

Access the current doortarget [_switch_](../data-types/datatype-switch.md) datatype members directly
Returns TRUE or FALSE

<!--tlo-linkrefs-start-->
[switch]: ../data-types/datatype-switch.md
<!--tlo-linkrefs-end-->
