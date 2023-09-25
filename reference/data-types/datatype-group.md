---
tags:
    - datatype
---
# `group`

Contains details about your group

## Members

[_bool_](datatype-bool.md) **AnyoneMissing**

:   True if somebody in the group is offline, in some other zone, or just simply dead.

[_int_](datatype-int.md) **CasterMercCount**

:   The number of caster dps mercenaries in your group.

[_spawn_](datatype-spawn.md) **Cleric**

:   The first member of the group that is a cleric.

[_int_](datatype-int.md) **GroupSize**

:   The number of members in your group, including yourself.

[_int_](datatype-int.md) **HealerMercCount**

:   The number of healer mercenaries in your group.

[_int_](datatype-int.md) **Injured**[ _#_ ]

:   The numbers of people in the group that has an hp percent lower than _#_.

[_groupmember_](datatype-groupmember.md) **Leader**

:   The leader of the group.

[_int_](datatype-int.md) **LowMana**[ _#_ ]

:   The number of people in the group that have a mana percent lower than _#_.

[_groupmember_](datatype-groupmember.md) **MainAssist**

:   The main assist of the group, if one is assigned.

[_groupmember_](datatype-groupmember.md) **MainTank**

:   The main tank of the group, if one is assigned.

[_groupmember_](datatype-groupmember.md) **MarkNpc**

:   The group member who can mark NPCs, if one is assigned.

[_groupmember_](datatype-groupmember.md) **MasterLooter**

:   The master looter of the group, if one is assigned.

[_int_](datatype-int.md) **MeleeMercCount**

:   The number of melee mercenaries in your group.

[_groupmember_](datatype-groupmember.md) **Member**[ _N_ ]

:   The _Nth_ member of your group. 0 is always you. 1 is the first person in the group list, etc.

[_int_](datatype-int.md) **Member**[ _Name_ ]

:   The group member of your group identified by _Name_.

[_int_](datatype-int.md) **Members**

:   The total number of group members, excluding yourself.

[_int_](datatype-int.md) **MercenaryCount** 

:   The total number of mercenaries that are in the group.

[_groupmember_](datatype-groupmember.md) **MouseOver**

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

[_groupmember_](datatype-groupmember.md) **Puller**

:   The puller of the group, if one is assigned.

[_int_](datatype-int.md) **TankMercCount**

:   The number of tank mercenaries in your group.

[_string_](datatype-string.md) **(To String)**

:   The number of members in the group, as a string.
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
