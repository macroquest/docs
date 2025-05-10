---
tags:
    - tlo
---
# `Familiar`

<!--tlo-desc-start-->
Used to get information about items on your familiars keyring.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='keyring', name='Familiar') }}

:   Access to the familiar keyring.

### {{ renderMember(type='keyringitem', name='Familiar', params='N') }}

:   Retrieves the item in your familiar keyring by index.

### {{ renderMember(type='keyringitem', name='Familiar', params='Name') }}

:   Retrieve the item in your familiar keyring by name. A `=` can be prepended for an exact match.
<!--tlo-forms-end-->

## Examples

See Also: [keyring][keyring] and [keyringitem][keyringitem]
<!--tlo-linkrefs-start-->
[keyring]: ../data-types/datatype-keyring.md
[keyringitem]: ../data-types/datatype-keyringitem.md
<!--tlo-linkrefs-end-->
