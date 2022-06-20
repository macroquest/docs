---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Spell`

Object used to return information on a spell by name or by ID.

## Forms

[_spell_][spell] **Spell**[_N_]

:   Find spell by ID

[_spell_][spell] **Spell**[_name_]

:   Find spell by name

## Examples

```
/echo ${Spell[Splurt].ID}
```

Will return 1620

```
/echo ${Spell[1620].Duration}
```

Will return 16 (ie. 16 ticks)

[spell]: ../data-types/datatype-spell.md
