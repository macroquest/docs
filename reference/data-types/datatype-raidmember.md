---
tags:
    - datatype
---
# `raidmember`

Data related to the specified raid member

## Members

### {{ renderMember(type='class', name='Class') }}

:   Raid member's class (works without being in zone)

### {{ renderMember(type='int', name='Group') }}

:   Current group number (or 0)

### {{ renderMember(type='bool', name='GroupLeader') }}

:   Returns TRUE if the member is a group leader

### {{ renderMember(type='int', name='Level') }}

:   Raid member's level (works without being in zone)

### {{ renderMember(type='bool', name='Looter') }}

:   Allowed to loot with current loot rules and looters?

### {{ renderMember(type='string', name='Name') }}

:   Raid member's name

### {{ renderMember(type='bool', name='RaidLeader') }}

:   Returns TRUE if the member is the raid leader

### {{ renderMember(type='spawn', name='Spawn') }}

:   Spawn object for this player if available (must be in zone)

### [string][string] `To String`

:   Same as **Name**

[bool]: datatype-bool.md
[class]: datatype-class.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
