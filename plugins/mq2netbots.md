## Description

MQ2NetBots was written by s0rcier and is found in the VIP forums
[here](https://macroquest2.com/phpBB3/viewtopic.php?t=12186)

-   MQ2NetBots provides linked MQ2EQBC clients a method of sharing status and statistics.
-   It makes that information available via Top-Level Object members for macro writers and HUD designers.

## Commands

-   **<span style="color:red">/netbots</span> \[ <span style="color:blue">on</span> \|
    <span style="color:blue">off</span> \]**

  
Turns MQ2NetBots functionality on or off

-   **<span style="color:red">/netbots</span> \[ <span style="color:blue">grab</span>=*on*\|*off* \]**

  
Receive status updates from other MQ2NetBots-enabled clients connected to the same EQBCS server.

-   **<span style="color:red">/netbots</span> \[ <span style="color:blue">send</span>=*on*\|*off* \]**

  
Broadcast status updates to the EQBCS server.

## Top-Level Object: ${NetBots}

### Forms

| **Type**        | **Form**                  | **Description**                            |
|-----------------|---------------------------|--------------------------------------------|
| *netbots*       | **NetBots**               | Returns information about your client      |
| *netbotsclient* | **NetBots\[***Name***\]** | Returns broadcast information about *Name* |

  
=== Data Types ===

| *netbots*                              |
|----------------------------------------|
| **Type**                               |
| *[string](../data-types/datatype-string.md)* |
| *[int](../data-types/datatype-int.md)*       |
| *[bool](../data-types/datatype-bool.md)*     |
| *[bool](../data-types/datatype-bool.md)*     |
| *[bool](../data-types/datatype-bool.md)*     |
| *[string](../data-types/datatype-string.md)* |

  
{\| border="1" cellpadding="2" cellspacing="0" width="600px" !colspan="3"\|*netbotsclient* \|-
\|style="background:#000000;color:#ffffff;text-align:left;width:15%;"\|**Type**
\|style="background:#000000;color:#ffffff;text-align:left;width:25%;"\|**Member Name**
\|style="background:#000000;color:#ffffff;text-align:left;"\|**Description** \|-
\|*[string](../data-types/datatype-string.md)* \|**Name** \|Name of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**Zone**
\|Zone ID of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**Instance** \|Instance ID of *Name* \|-
\|*[class](../data-types/datatype-class.md)* \|**Class** \|Class of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**Level**
\|Level of *Name* \|- \|*[float](../data-types/datatype-float.md)* \|**PctExp** \|Percent Experience of *Name* \|-
\|*[float](../data-types/datatype-float.md)* \|**PctAAExp** \|Percent AA Experience of *Name* \|-
\|*[float](../data-types/datatype-float.md)* \|**PctGroupLeaderExp** \|Percent Group Leader Experience of *Name* \|-
\|*[int](../data-types/datatype-int.md)* \|**CurrentHPs** \|Current Hitpoints of *Name* \|- \|*[int](../data-types/datatype-int.md)*
\|**MaxHPs** \|Total Hitpoints of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**PctHPs** \|Current Hitpoints
Percentage of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**CurrentEndurance** \|Current Endurance of *Name* \|-
\|*[int](../data-types/datatype-int.md)* \|**MaxEndurance** \|Total Endurance of *Name* \|- \|*[int](../data-types/datatype-int.md)*
\|**PctEndurance** \|Current Endurance Percentage of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**CurrentMana**
\|Current Mana of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**MaxMana** \|Total Mana of *Name* \|-
\|*[int](../data-types/datatype-int.md)* \|**PctMana** \|Current Mana Percentage of *Name* \|-
\|*[int](../data-types/datatype-int.md)* \|**PetID** \|Spawn ID of *Name*'s pet \|- \|*[int](../data-types/datatype-int.md)*
\|**PetHP** \|Hitpoints of *Name*'s pet \|- \|*[int](../data-types/datatype-int.md)* \|**TargetID** \|Spawn ID of *Name*'s
target \|- \|*[int](../data-types/datatype-int.md)* \|**TargetHP** \|Hitpoints of *Name*'s target \|-
\|*[spell](../data-types/datatype-spell.md)* \|**Casting** \|Spell *Name* is casting \|-
\|*[string](../data-types/datatype-string.md)* \|**State** \|

-   State of *Name*
-   STUN STAND SIT DUCK BIND FEIGN DEAD UNKNOWN

\|- \|*[bool](../data-types/datatype-bool.md)* \|**Attacking** \|Is *Name* attacking? \|- \|*[bool](../data-types/datatype-bool.md)*
\|**AFK** \|Is *Name* AFK? \|- \|*[bool](../data-types/datatype-bool.md)* \|**Binding** \|Is *Name* kneeling? \|-
\|*[bool](../data-types/datatype-bool.md)* \|**Ducking** \|Is *Name* ducking? \|- \|*[bool](../data-types/datatype-bool.md)*
\|**Feigning** \|Is *Name* feigning? \|- \|*[bool](../data-types/datatype-bool.md)* \|**Grouped** \|Is *Name* in a group? \|-
\|*[bool](../data-types/datatype-bool.md)* \|**Invis** \|Is *Name* invisible? \|- \|*[bool](../data-types/datatype-bool.md)*
\|**Levitating** \|Is *Name* levitating? \|- \|*[bool](../data-types/datatype-bool.md)* \|**LFG** \|Is *Name* LFG? \|-
\|*[bool](../data-types/datatype-bool.md)* \|**Mounted** \|Is *Name* on a mount? \|- \|*[bool](../data-types/datatype-bool.md)*
\|**Moving** \|Is *Name* moving? \|- \|*[bool](../data-types/datatype-bool.md)* \|**Raid** \|Is *Name* in a raid? \|-
\|*[bool](../data-types/datatype-bool.md)* \|**Sitting** \|Is *Name* sitting? \|- \|*[bool](../data-types/datatype-bool.md)*
\|**Standing** \|Is *Name* standing? \|- \|*[int](../data-types/datatype-int.md)* \|**FreeBuffSlots** \|Total free buff slots
of *Name* \|- \|*[bool](../data-types/datatype-bool.md)* \|**InZone** \|Is *Name* in the same zone? \|-
\|*[bool](../data-types/datatype-bool.md)* \|**InGroup** \|Is *Name* in the same group? \|-
\|*[string](../data-types/datatype-string.md)* \|**Leader** \|*Name*'s group leader \|- \|*[int](../data-types/datatype-int.md)*
\|**Updated** \|Timestamp of last update from *Name* \|- \|*[string](../data-types/datatype-string.md)* \|**Gem** \|All spells
*Name* has memorized \|- \|*[spell](../data-types/datatype-spell.md)* \|**Gem\[**#**\]** \|Spell *Name* has in slot # \|-
\|*[string](../data-types/datatype-string.md)* \|**Buff** \|All buffs *Name* has \|- \|*[spell](../data-types/datatype-spell.md)*
\|**Buff\[**#**\]** \|Buff *Name* has in buff slot # \|- \|*[string](../data-types/datatype-string.md)* \|**Duration**
\|Duration of all buffs *Name* has \|- \|*[int](../data-types/datatype-int.md)* \|**Duration\[**#**\]** \|Duration of buff
*Name* has in buff slot # \|- \|*[string](../data-types/datatype-string.md)* \|**ShortBuff** \|All short buffs *Name* has \|-
\|*[spell](../data-types/datatype-spell.md)* \|**ShortBuff\[**#**\]** \|ShortBuff *Name* has in buff slot # \|-
\|*[string](../data-types/datatype-string.md)* \|**PetBuff** \|All pet buffs *Name*'s pet has \|-
\|*[spell](../data-types/datatype-spell.md)* \|**PetBuff\[**#**\]** \|Pet buff *Name*'s pet has in pet buff slot # \|-
\|*[int](../data-types/datatype-int.md)* \|**TotalAA** \|Total AA of *Name* \|- \|*[int](../data-types/datatype-int.md)*
\|**UsedAA** \|Total spent AA of *Name* \|- \|*[int](../data-types/datatype-int.md)* \|**UnusedAA** \|Total unspent AA of
*Name* \|- \|*[int](../data-types/datatype-int.md)* \|**CombatState** \|Combat State of *Name* \|- \|}  
== Examples ==

-   Displays the duration remaining on the buff *Samwell* has in buff slot 4

  
    /echo ${NetBots[Samwell].Duration[4]}

## See Also

-   [MQ2EQBC](mq2eqbc.md)
-   [MQ2NetHeal](mq2netheal.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Data Types](../data-types/data-types.md)
-   [Plugins](../documentation/macroquest2-plugins.md)


