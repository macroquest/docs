---
tags:
    - datatype
---
# `group`

Contains details about your group

## Members

### {{ renderMember(type='bool', name='AnyoneMissing') }}

:   True if somebody in the group is offline, in some other zone, or just simply dead.

### {{ renderMember(type='int', name='CasterMercCount') }}

:   The number of caster dps mercenaries in your group.

### {{ renderMember(type='spawn', name='Cleric') }}

:   The first member of the group that is a cleric.

### {{ renderMember(type='int', name='GroupSize') }}

:   The number of members in your group, including yourself.

### {{ renderMember(type='int', name='HealerMercCount') }}

:   The number of healer mercenaries in your group.

### {{ renderMember(type='int', name='Injured', params='#') }}

:   The numbers of people in the group that has an hp percent lower than _#_.

### {{ renderMember(type='groupmember', name='Leader') }}

:   The leader of the group.

### {{ renderMember(type='int', name='LowMana', params='#') }}

:   The number of people in the group that have a mana percent lower than _#_.

### {{ renderMember(type='groupmember', name='MainAssist') }}

:   The main assist of the group, if one is assigned.

### {{ renderMember(type='groupmember', name='MainTank') }}

:   The main tank of the group, if one is assigned.

### {{ renderMember(type='groupmember', name='MarkNpc') }}

:   The group member who can mark NPCs, if one is assigned.

### {{ renderMember(type='groupmember', name='MasterLooter') }}

:   The master looter of the group, if one is assigned.

### {{ renderMember(type='int', name='MeleeMercCount') }}

:   The number of melee mercenaries in your group.

### {{ renderMember(type='groupmember', name='Member', params='#') }}

:   The _Nth_ member of your group. 0 is always you. 1 is the first person in the group list, etc.

### {{ renderMember(type='int', name='Members', params='Name') }}

:   The group member of your group identified by _Name_.

### {{ renderMember(type='int', name='Members') }}

:   The total number of group members, excluding yourself.

### {{ renderMember(type='int', name='MercenaryCount') }}

:   The total number of mercenaries that are in the group.

### {{ renderMember(type='groupmember', name='MouseOver') }}

:   The name of the group member that the mouse is currently hovering over in the group window, if any.

    !!! note

        You can hover over your own name in the player window where you see your hp and it will return you.

    ??? example "Examples"

        ```
        /echo Im hovering my mouse over ${Group.MouseOver.Name} which has ths spawnid: ${Group.MouseOver.ID}
        ```

        ```
        /bct ${Group.MouseOver.Name} hi there I dont want to change my target just to tell you: please heal ${Me.Mame}
        ```

        ```
        /bct soandso //casting "Complete Heal" -targetid|${Group.MouseOver.ID}
        ```

        ```
        /bct ${Group.MouseOver.CleanName} //setprio 2
        ```

### {{ renderMember(type='groupmember', name='Puller') }}

:   The puller of the group, if one is assigned.

### {{ renderMember(type='int', name='TankMercCount') }}

:   The number of tank mercenaries in your group.

### [string][string] `To String`

:   The number of members in the group, as a string.

[bool]: datatype-bool.md
[groupmember]: datatype-groupmember.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
