---
tags:
    - tlo
---
# `Spell`

Object used to return information on a spell by name or by ID.

## Forms

### {{ renderMember(type='spell', name='Spell') }}

:   Find spell by ID

### {{ renderMember(type='spell', name='Spell', params='Name') }}

:   Find spell by name


## Usage

```
/echo ${Spell[Splurt].ID}
```

Will return 1620

```
/echo ${Spell[1620].Duration}
```

Will return 16 (ie. 16 ticks)

[spell]: ../data-types/datatype-spell.md
