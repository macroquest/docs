---
tags:
    - tlo
---
# `Me`

<!--tlo-desc-start-->
Character object which allows you to get properties of you as a character.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='character', name='Me') }}

:   Returns the character object which provides access to information about your own character.

    ${Me} is a character object, so has access to all the properties of the
    [character](../data-types/datatype-character.md) type. The [character](../data-types/datatype-character.md)
    type also has access to the properties of the [spawn](../data-types/datatype-spawn.md) type.
<!--tlo-forms-end-->

## Usage

```
/echo Current Mana: ${Me.PctMana}%
```
<!--tlo-linkrefs-start-->
[character]: ../data-types/datatype-character.md
<!--tlo-linkrefs-end-->
