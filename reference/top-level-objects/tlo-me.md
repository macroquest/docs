---
tags:
    - tlo
---
# `Me`

Character object which allows you to get properties of you as a character.

## Forms

[_character_](../data-types/datatype-character.md) **Me**

:   Returns the character object which provides access to information about your own character.


    ${Me} is a character object, so has access to all the properties of the
    [character](../data-types/datatype-character.md) type. The [character](../data-types/datatype-character.md)
    type also has access to the properties of the [spawn](../data-types/datatype-spawn.md) type.

## Examples

```
/echo Current Mana: ${Me.PctMana}%
```
