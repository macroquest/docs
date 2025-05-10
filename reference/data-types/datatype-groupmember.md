---
tags:
    - datatype
---
# `groupmember`

<!--dt-desc-start-->
Contains data on a specific group member
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
This type inherits members from [_spawn_ ](datatype-spawn.md)if the member is in the current zone.

### {{ renderMember(type='int', name='Index') }}

:   Which number in the group the member is

### {{ renderMember(type='bool', name='Leader') }}

:   TRUE if the member is the group's leader, FALSE otherwise

### {{ renderMember(type='int', name='Level') }}

:   The member's level

### {{ renderMember(type='bool', name='MainAssist') }}

:   TRUE if the member is designated as the group's Main Assist, FALSE otherwise

### {{ renderMember(type='bool', name='MainTank') }}

:   TRUE if the member is designated as the group's Main Tank, FALSE otherwise

### {{ renderMember(type='bool', name='MasterLooter') }}

:   TRUE if the member is designated as the group's Master Looter, FALSE otherwise

### {{ renderMember(type='bool', name='MarkNpc') }}

:   TRUE if the member is designated as the group roule Mark NPC, FALSE otherwise

### {{ renderMember(type='bool', name='Mercenary') }}

:   TRUE if the member is a mercenary, FALSE otherwise

### {{ renderMember(type='string', name='Name') }}

:   The name of the group member. This works even if they are not in the same zone as you.

### {{ renderMember(type='bool', name='Offline') }}

:   TRUE if the member is offline and FALSE if online

### {{ renderMember(type='bool', name='OtherZone') }}

:   TRUE if the member is online but in another zone and FALSE if online and in same zone as you.

### {{ renderMember(type='int', name='PctAggro') }}

:   ???

### {{ renderMember(type='bool', name='Present') }}

:   TRUE if the member is online and in same zone and FALSE if online and not in same zone as you.

### {{ renderMember(type='bool', name='Puller') }}

:   TRUE if the member is designated as the group's Puller, FALSE otherwise

### {{ renderMember(type='spawn', name='Spawn') }}

:   Accesses the group member's spawn. Not all members will have a spawn (if they are out of the zone).

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

## Examples

```
/echo ${Group.Member[0].Leader}
```

Echo TRUE if you are Group Leader.

```
/echo ${Group.Member[3].Puller}
```

Echo TRUE if Group Member 3 is marked as Role Puller
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
