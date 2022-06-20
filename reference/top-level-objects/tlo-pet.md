---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Pet`

Pet object which allows you to get properties of your pet.

## Forms

[_pet_](../data-types/datatype-pet.md) **Pet**

:   Provides access to your current Pet. The [pet](../data-types/datatype-pet.md) type extends from spawn, and as such 
    has access to the properties of the [spawn](../data-types/datatype-spawn.md) type as well.

## Examples

```
/echo My Pet's Stance is currently set to: ${Pet.Stance}
```

```
/echo My Pet's Name: ${Pet.CleanName}%
```

```
/echo My Pet's Target has gone Berserk! ${Pet.Target.IsBerserk}
```
