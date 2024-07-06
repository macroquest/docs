---
tags:
    - tlo
---
# `Corpse`

Access to objects of type corpse, which is the currently active corpse (ie. the one you are looting).

## Forms

### {{ renderMember(type='corpse', name='Corpse') }}

:   Corpse you are looting.


## Usage

```
/if (${Corpse.Open}) {
    /echo Corpse is open, proceeding with looting
}
```

[corpse]: ../data-types/datatype-corpse.md
