---
tags:
    - datatype
---
# `switch`

Data related to switches (levers, buttons, etc) in the zone

## Members

### {{ renderMember(type='heading', name='DefaultHeading') }}

:   Heading of "closed" switch

### {{ renderMember(type='float', name='DefaultX') }}

:   X coordinate of "closed" switch

### {{ renderMember(type='float', name='DefaultY') }}

:   Y coordinate of "closed" switch

### {{ renderMember(type='float', name='DefaultZ') }}

:   Z coordinate of "closed" switch

### {{ renderMember(type='float', name='Distance') }}

:   Distance from player to switch in (x,y)

### {{ renderMember(type='float', name='Distance3D') }}

:   Distance from player to switch in (x,y,z)

### {{ renderMember(type='heading', name='Heading') }}

:   Switch is facing this heading

### {{ renderMember(type='heading', name='HeadingTo') }}

:   Direction player must move to meet this switch

### {{ renderMember(type='int', name='ID') }}

:   Switch ID

### {{ renderMember(type='bool', name='IsTargeted') }}

:   Returns TRUE if the switch is targeted

### {{ renderMember(type='bool', name='LineOfSight') }}

:   Returns TRUE if the switch is in LoS

### {{ renderMember(type='string', name='Name') }}

:   Name

### {{ renderMember(type='bool', name='Open') }}

:   True if the switch is in the "open" state (State == 1)

### {{ renderMember(type='int', name='State') }}

:   The "state" of the switch.

### {{ renderMember(type='float', name='X') }}

:   X coordinate

### {{ renderMember(type='float', name='Y') }}

:   Y coordinate

### {{ renderMember(type='float', name='Z') }}

:   Z coordinate

### {{ renderMember(type='string', name='ToString') }}

:   Same as **ID**

[bool]: datatype-bool.md
[float]: datatype-float.md
[heading]: datatype-heading.md
[int]: datatype-int.md
[string]: datatype-string.md
