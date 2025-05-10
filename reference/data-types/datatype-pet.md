---
tags:
    - datatype
---
# `pet`

<!--dt-desc-start-->
Pet object
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
This type inherits members from [_spawn_](datatype-spawn.md).

### {{ renderMember(type='int', name='Buff', params='buffname') }}

:   Returns the slot number for _buffname_

### {{ renderMember(type='string', name='Buff', params='slot') }}

:   Prints name of the buff at the given _slot_

### {{ renderMember(type='int', name='BuffDuration', params='buffname') }}

:   Buff time remaining for pet buff _buffname_ in miliseconds

### {{ renderMember(type='int', name='BuffDuration', params='slot') }}

:   Buff time remaining for pet buff in slot _slot_ in miliseconds

### {{ renderMember(type='bool', name='Combat') }}

:   Combat state

### {{ renderMember(type='buff', name='FindBuff') }}

:   ???

### {{ renderMember(type='bool', name='Focus') }}

:   Focus state

### {{ renderMember(type='bool', name='GHold') }}

:   GHold state

### {{ renderMember(type='bool', name='Hold') }}

:   Hold state

### {{ renderMember(type='string', name='Name') }}

:   ???

### {{ renderMember(type='bool', name='ReGroup') }}

:   ReGroup state

### {{ renderMember(type='string', name='Stance') }}

:   Returns the pet's current stance, (e.g. FOLLOW, GUARD)

### {{ renderMember(type='bool', name='Stop') }}

:   Stop state

### {{ renderMember(type='spawn', name='Target') }}

:   Returns the pet's current target.

### {{ renderMember(type='bool', name='Taunt') }}

:   Taunt state
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[buff]: datatype-buff.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
