---
tags:
    - tlo
---
# `Switch`

Object used when you want to find information on targetted doors or switches such as the portals in PoK.

## Forms

### {{ renderMember(type='switch', name='Switch') }}

:   Returns the currently targeted switch

### {{ renderMember(type='switch', name='Switch', params='ID') }}

:   Returns a switch matching the provided numeric ID

### {{ renderMember(type='switch', name='Switch', params='Search') }}

:   Based on the value of `Search`, return a switch:

    - `target`: Return the currently targeted switch
    - `nearest`: Return the nearest switch.
    - Otherwise, return switch by searching by name


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


[switch]: ../data-types/datatype-switch.md
