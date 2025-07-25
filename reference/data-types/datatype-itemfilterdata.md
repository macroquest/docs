---
tags:
    - datatype
---
# `itemfilterdata`

<!--dt-desc-start-->
A collection of settings that together describe the loot filter for an item.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='bool', name='AutoRoll') }}

:   The Auto Roll state (dice icon).

### {{ renderMember(type='bool', name='Greed') }}

:   The Greed (GD) state.

### {{ renderMember(type='int', name='IconID') }}

:   The ID of the icon.

### {{ renderMember(type='int', name='ID') }}

:   The ID of the item.

### {{ renderMember(type='string', name='Name') }}

:   The Name of the item.

### {{ renderMember(type='bool', name='Need') }}

:   The Need (ND) state.

### {{ renderMember(type='bool', name='Never') }}

:   The Never (NV) state.

### {{ renderMember(type='int', name='Types') }}

:   Bit field representing all the loot filter flags for this item.

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end--> 