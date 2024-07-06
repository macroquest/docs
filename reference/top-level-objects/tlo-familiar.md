---
tags:
    - tlo
---
# `Familiar`

Used to get information about items on your familiars keyring.

## Forms

### {{ renderMember(type='keyring', name='Familiar') }}

:   Access to the familiar keyring.

### {{ renderMember(type='keyringitem', name='Familiar', params='N') }}

:   Retrieves the item in your familiar keyring by index.

### {{ renderMember(type='keyringitem', name='Familiar', params='Name') }}

:   Retrieve the item in your familiar keyring by name. A `=` can be prepended for an exact match.

## Examples

See Also: [keyring][keyring] and [keyringitem][keyringitem]

[keyring]: ../data-types/datatype-keyring.md
[keyringitem]: ../data-types/datatype-keyringitem.md
