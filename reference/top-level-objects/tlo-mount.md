---
tags:
    - tlo
---
# `Mount`

<!--tlo-desc-start-->
Used to get information about items on your Mount keyring.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='keyring', name='Mount') }}

:   Access to the Mount keyring.

### {{ renderMember(type='keyringitem', name='Mount', params='N') }}

:   Retrieves the item in your mount keyring by index.

### {{ renderMember(type='keyringitem', name='Mount', params='Name') }}

:   Retrieve the item in your mount keyring by name. A `=` can be prepended for an exact match.
<!--tlo-forms-end-->
<!--tlo-linkrefs-start-->
[keyring]: ../data-types/datatype-keyring.md
[keyringitem]: ../data-types/datatype-keyringitem.md
<!--tlo-linkrefs-end-->
