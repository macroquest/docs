---
tags:
    - tlo
---
# `Mount`

Used to get information about items on your Mount keyring.


## Forms

### {{ renderMember(type='keyring', name='Mount') }}

:   Access to the Mount keyring.

### {{ renderMember(type='keyringitem', name='Mount', params='N') }}

:   Retrieves the item in your mount keyring by index.

### {{ renderMember(type='keyringitem', name='Mount', params='Name') }}

:   Retrieve the item in your mount keyring by name. A `=` can be prepended for an exact match.

[keyring]: ../data-types/datatype-keyring.md
[keyringitem]: ../data-types/datatype-keyringitem.md
