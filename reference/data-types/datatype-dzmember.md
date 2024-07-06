---
tags:
    - datatype
---
# `dzmember`

This DataType contains information on the members of the current dynamic zone instance

See Also: [DataType:dynamiczone](./datatype-dynamiczone.md), [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)

## Members

### {{ renderMember(type='bool', name='Flagged') }}

:   Returns true if the dzmember can successfully enter the dz. where x is either index or the name.

### {{ renderMember(type='string', name='Name') }}

:   The name of the member

### {{ renderMember(type='string', name='Status') }}

:   The status of the member - one of the following: Unknown, Online, Offline, In Dynamic Zone, Link Dead

### [string][string] `To String`

:   Same as **Name**

[bool]: datatype-bool.md
[string]: datatype-string.md
