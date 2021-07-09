# MQ2NetBots

## Description

MQ2NetBots was written by s0rcier and is found in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12186)

* MQ2NetBots provides linked MQ2EQBC clients a method of sharing status and statistics.
* It makes that information available via Top-Level Object members for macro writers and HUD designers.

## Commands

* \*\*/netbots \[ on \|

  off \]\*\*

Turns MQ2NetBots functionality on or off

* **/netbots \[ grab=**_**on**_**\|**_**off**_ **\]**

Receive status updates from other MQ2NetBots-enabled clients connected to the same EQBCS server.

* **/netbots \[ send=**_**on**_**\|**_**off**_ **\]**

Broadcast status updates to the EQBCS server.

## Top-Level Object: ${NetBots}

### Forms

| **Type** | **Form** | **Description** |
| :--- | :--- | :--- |
| _netbots_ | **NetBots** | Returns information about your client |
| _netbotsclient_ | **NetBots\[\***Name**\*\]** | Returns broadcast information about _Name_ |

=== Data Types ===

| _netbots_ |
| :--- |
| **Type** |
| [_string_]() |
| [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) |
| [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) |
| [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) |
| [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) |
| [_string_]() |

{\| border="1" cellpadding="2" cellspacing="0" width="600px" !colspan="3"\|_netbotsclient_ \|- \|style="background:\#000000;color:\#ffffff;text-align:left;width:15%;"\|**Type** \|style="background:\#000000;color:\#ffffff;text-align:left;width:25%;"\|**Member Name** \|style="background:\#000000;color:\#ffffff;text-align:left;"\|**Description** \|- \|[_string_]() \|**Name** \|Name of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**Zone** \|Zone ID of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**Instance** \|Instance ID of _Name_ \|- \|[_class_](../../data-types-and-top-level-objects/data-types/datatype-class.md) \|**Class** \|Class of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**Level** \|Level of _Name_ \|- \|[_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) \|**PctExp** \|Percent Experience of _Name_ \|- \|[_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) \|**PctAAExp** \|Percent AA Experience of _Name_ \|- \|[_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) \|**PctGroupLeaderExp** \|Percent Group Leader Experience of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**CurrentHPs** \|Current Hitpoints of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**MaxHPs** \|Total Hitpoints of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**PctHPs** \|Current Hitpoints Percentage of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**CurrentEndurance** \|Current Endurance of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**MaxEndurance** \|Total Endurance of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**PctEndurance** \|Current Endurance Percentage of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**CurrentMana** \|Current Mana of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**MaxMana** \|Total Mana of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**PctMana** \|Current Mana Percentage of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**PetID** \|Spawn ID of _Name_'s pet \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**PetHP** \|Hitpoints of _Name_'s pet \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**TargetID** \|Spawn ID of _Name_'s target \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**TargetHP** \|Hitpoints of _Name_'s target \|- \|[_spell_](../../data-types-and-top-level-objects/data-types/datatype-spell.md) \|**Casting** \|Spell _Name_ is casting \|- \|[_string_]() \|**State** \|

* State of _Name_
* STUN STAND SIT DUCK BIND FEIGN DEAD UNKNOWN

\|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Attacking** \|Is _Name_ attacking? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**AFK** \|Is _Name_ AFK? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Binding** \|Is _Name_ kneeling? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Ducking** \|Is _Name_ ducking? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Feigning** \|Is _Name_ feigning? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Grouped** \|Is _Name_ in a group? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Invis** \|Is _Name_ invisible? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Levitating** \|Is _Name_ levitating? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**LFG** \|Is _Name_ LFG? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Mounted** \|Is _Name_ on a mount? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Moving** \|Is _Name_ moving? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Raid** \|Is _Name_ in a raid? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Sitting** \|Is _Name_ sitting? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**Standing** \|Is _Name_ standing? \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**FreeBuffSlots** \|Total free buff slots of _Name_ \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**InZone** \|Is _Name_ in the same zone? \|- \|[_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) \|**InGroup** \|Is _Name_ in the same group? \|- \|[_string_]() \|**Leader** \|_Name_'s group leader \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**Updated** \|Timestamp of last update from _Name_ \|- \|[_string_]() \|**Gem** \|All spells _Name_ has memorized \|- \|[_spell_](../../data-types-and-top-level-objects/data-types/datatype-spell.md) \|**Gem\[**\#**\]** \|Spell _Name_ has in slot \# \|- \|[_string_]() \|**Buff** \|All buffs _Name_ has \|- \|[_spell_](../../data-types-and-top-level-objects/data-types/datatype-spell.md) \|**Buff\[**\#**\]** \|Buff _Name_ has in buff slot \# \|- \|[_string_]() \|**Duration** \|Duration of all buffs _Name_ has \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**Duration\[**\#**\]** \|Duration of buff _Name_ has in buff slot \# \|- \|[_string_]() \|**ShortBuff** \|All short buffs _Name_ has \|- \|[_spell_](../../data-types-and-top-level-objects/data-types/datatype-spell.md) \|**ShortBuff\[**\#**\]** \|ShortBuff _Name_ has in buff slot \# \|- \|[_string_]() \|**PetBuff** \|All pet buffs _Name_'s pet has \|- \|[_spell_](../../data-types-and-top-level-objects/data-types/datatype-spell.md) \|**PetBuff\[**\#**\]** \|Pet buff _Name_'s pet has in pet buff slot \# \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**TotalAA** \|Total AA of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**UsedAA** \|Total spent AA of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**UnusedAA** \|Total unspent AA of _Name_ \|- \|[_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) \|**CombatState** \|Combat State of _Name_ \|- \|}  
== Examples ==

* Displays the duration remaining on the buff _Samwell_ has in buff slot 4

```text
/echo ${NetBots[Samwell].Duration[4]}
```

## See Also

* [MQ2EQBC](mq2eqbc/)
* [MQ2NetHeal](mq2netheal.md)
* [Top-Level Objects](../../data-types-and-top-level-objects/top-level-objects/)
* [Data Types](../../data-types-and-top-level-objects/data-types/)
* [Plugins](../../documentation/macroquest2-plugins.md)

