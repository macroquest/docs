---
tags:
    - datatype
---
# `augtype` Type

Describes data about an augmentation slot in an item.

## Members

### {{ renderMember(type='bool', name='Empty') }}

:   True if the slot is empty

### {{ renderMember(type='bool', name='Infusable') }}

:   True if this is a hidden energeian power source slot.

### {{ renderMember(type='item', name='Item') }}

:   The item socketed in this slot, if any.

### {{ renderMember(type='string', name='Name') }}

:   The name of the item socketed in this slot, if any.

### {{ renderMember(type='int', name='Slot') }}

:   Index of the augment slot.

### {{ renderMember(type='int', name='Solvent') }}

:   Item ID of the solvent used to remove this item, if any.

### {{ renderMember(type='int', name='Type') }}

:   Type of augment slot.

### {{ renderMember(type='int', name='Visible') }}

:   True if this slot is visible to the user.


[int]: ./datatype-int.md
[bool]: ./datatype-bool.md
[string]: ./datatype-string.md
[item]: ./datatype-item.md
