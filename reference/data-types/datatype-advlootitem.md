---
tags:
    - datatype
---
# `advlootitem`

<!--dt-desc-start-->
Represents a discrete item being looted in an AdvLoot window.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='bool', name='AlwaysGreed') }}

:   The Always Greed (AG) state of the item.

### {{ renderMember(type='bool', name='AlwaysNeed') }}

:   The Always Need (AN) state of the item.

### {{ renderMember(type='bool', name='AutoRoll') }}

:   The Auto Roll state (dice icon) of the item.

### {{ renderMember(type='spawn', name='Corpse') }}

:   The spawn representing the corpse that is being looted, if available.

### {{ renderMember(type='bool', name='FreeGrab') }}

:   Indicates that the item is free grab.

### {{ renderMember(type='bool', name='Greed') }}

:   The Greed (GD) state of the item.

### {{ renderMember(type='int', name='IconID') }}

:   The ID of the icon for the item.

### {{ renderMember(type='int64', name='ID') }}

:   The ID of the item.

### {{ renderMember(type='int', name='Index') }}

:   The positional index of the item.

### {{ renderMember(type='string', name='Name') }}

:   The name of the item.

### {{ renderMember(type='bool', name='Need') }}

:   The Need (ND) state of the item.

### {{ renderMember(type='bool', name='Never') }}

:   The Never (NV) state of the item.

### {{ renderMember(type='bool', name='No') }}

:   The No state of the item.

### {{ renderMember(type='bool', name='NoDrop') }}

:   Indicates if the item is NO DROP.

### {{ renderMember(type='int', name='StackSize') }}

:   The size of the stack of items being looted.

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end--> 