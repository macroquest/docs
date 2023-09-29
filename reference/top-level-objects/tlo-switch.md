---
tags:
    - tlo
---
# `Switch`

Object used when you want to find information on targetted doors or switches such as the portals in PoK.

## Forms

[_switch_](../data-types/datatype-switch.md) **Switch**

## Examples

```
${Switch[foo]}
```
Activates switch "foo"

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

