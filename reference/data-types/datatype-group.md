---
tags:
    - datatype
---
# `group`

<!--dt-desc-start-->
Contains details about your group
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool AnyoneMissing
True if somebody in the group is offline, in some other zone, or just simply dead.
///

/// member | int CasterMercCount
The number of caster dps mercenaries in your group.
///

/// member | spawn Cleric
The first member of the group that is a cleric.
///

/// member | int GroupSize
The number of members in your group, including yourself.
///

/// member | int HealerMercCount
The number of healer mercenaries in your group.
///

/// member | int Injured[#]
The numbers of people in the group that has an hp percent lower than _#_.
///

/// member | groupmember Leader
The leader of the group.
///

/// member | int LowMana[#]
The number of people in the group that have a mana percent lower than _#_.
///

/// member | groupmember MainAssist
The main assist of the group, if one is assigned.
///

/// member | groupmember MainTank
The main tank of the group, if one is assigned.
///

/// member | groupmember MarkNpc
The group member who can mark NPCs, if one is assigned.
///

/// member | groupmember MasterLooter
The master looter of the group, if one is assigned.
///

/// member | int MeleeMercCount
The number of melee mercenaries in your group.
///

/// member | groupmember Member[#]
The _Nth_ member of your group. 0 is always you. 1 is the first person in the group list, etc.
///

/// member | int Members[Name]
The group member of your group identified by _Name_.
///

/// member | int Members
The total number of group members, excluding yourself.
///

/// member | int MercenaryCount
The total number of mercenaries that are in the group.
///

/// member | groupmember MouseOver
The name of the group member that the mouse is currently hovering over in the group window, if any.

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
///

/// member | groupmember Puller
The puller of the group, if one is assigned.
///

/// member | int TankMercCount
The number of tank mercenaries in your group.
///

### [string][string] `To String`

:   The number of members in the group, as a string.
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[groupmember]: datatype-groupmember.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
