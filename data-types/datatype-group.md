## Description

Contains details about your group

## Members

|                                                  |                              |                                                                                                           |
|--------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Type**                                         | **Member**                   | **Description**                                                                                           |
| *[bool](datatype-bool.md)*               | **AnyoneMissing**            | TRUE if someone is missing in group, offline, in other zone or simply just dead                           |
| *[int](datatype-int.md)*                 | '''CasterMercCount           | count of how many Caster DPS mercenaries are in your group                                                |
| *[string](datatype-string.md)*           | '''Cleric                    | Will now return the cleric as a spawntype if a cleric is in the group (not a mercenary but a REAL cleric) |
| *[int](datatype-int.md)*                 | **GroupSize**                | Number of members in your group, including yourself                                                       |
| *[int](datatype-int.md)*                 | '''HealerMercCount           | count of how many Healer mercenaries are in your group                                                    |
| *[int](datatype-int.md)*                 | '''Injured\[XX\]             | Will return the numbers of people in the group that has a hp percent lower than 90                        |
| *[groupmember](datatype-groupmember.md)* | **Leader**                   | Data on the leader of the group                                                                           |
| *[groupmember](datatype-groupmember.md)* | **MainAssist**               | Data on the main assist of the group                                                                      |
| *[groupmember](datatype-groupmember.md)* | **MainTank**                 | Data on the main tank of the group                                                                        |
| *[groupmember](datatype-groupmember.md)* | **MarkNpc**                  | Data on the group member who can mark NPCs, if one is assigned                                            |
| *[groupmember](datatype-groupmember.md)* | **MasterLooter**             | Data on the Master Looter of the group, if one is assigned                                                |
| *[int](datatype-int.md)*                 | '''MeleeMercCount            | count of how many Melee DPS mercenaries are in your group                                                 |
| *[groupmember](datatype-groupmember.md)* | **Member\[**#**\]**          | Accesses #th member of your group; 0 is you, 1 is the first person in the group list, etc.                |
| *[int](datatype-int.md)*                 | **Member\[**name**\].Index** | Which number in the group the PC with *name* is                                                           |
| *[spawn](datatype-spawn.md)*             | **Member\[**#/name**\].Pet** | Returns the group members' pet name                                                                       |
| *[int](datatype-int.md)*                 | **Members**                  | Total number of group members, excluding yourself                                                         |
| *[int](datatype-int.md)*                 | **MercenaryCount**           | Count of how many Mercenaries are in the group                                                            |
| *[string](datatype-string.md)*           | **MouseOver**                | Returns the name of the group member your mouse is hovering over                                          |
| *[bool](datatype-bool.md)*               | **Offline**                  | will return a TRUE if offline, and FALSE if online                                                        |
| *[bool](datatype-bool.md)*               | **OtherZone**                | will return a Bool TRUE if online but in another zone and FALSE if online and in same zone as you.        |
| *[groupmember](datatype-groupmember.md)* | **Puller**                   | Data on the puller of the group                                                                           |
| *[int](datatype-int.md)*                 | '''TankMercCount             | count of how many Tank mercenaries are in your group                                                      |
| '**'[string](datatype-string.md)**       | **To String**                | Same as **Members**                                                                                       |

### Usage

`Usage1: /echo Im hovering my mouse over ${Group.MouseOver.Name} which has ths spawnid: ${Group.MouseOver.ID}`  
`Usage2: /bct ${Group.MouseOver.Name} hi there I dont want to change my target just to tell u: please heal ${Me.Mame}`  
`Usage3: /bct eqmule //casting "Complete Heal" -targetid|${Group.MouseOver.ID}`  
`Usage4: /bct ${Group.MouseOver.CleanName} //setprio 2`

Final Note: YOU CAN hover over your own name in the player window where u see your hp and it will return you.

In macro usage:

/if (${Group.Member\[Julio\].Index}) /smack Julio

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Group](../top-level-objects/tlo-group.md)
-   [DataType:groupmember](datatype-groupmember.md)


