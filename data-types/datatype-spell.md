## Description

This is the type used for spell information.

## Members

|                                              |                                  |                                                                                                   |
|----------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------|
| **Type**                                     | **Member**                       | **Description**                                                                                   |
| *[float](datatype-float.md)*         | **AERange**                      | AE range (group spells use this for their range)                                                  |
| *[string](datatype-string.md)*       | **CastOnAnother**                | Message when cast on others                                                                       |
| *[string](datatype-string.md)*       | **CastOnYou**                    | Message when cast on yourself                                                                     |
| *[timestamp](datatype-timestamp.md)* | **CastTime**                     | Cast time (unadjusted)                                                                            |
| *[string](datatype-string.md)*       | **CounterType**                  | The resist counter. Will be one of "Disease", "Poison", "Curse" or "Corruption"                   |
| *[int](datatype-int.md)*             | **CounterNumber**                | The number of counters that the spell adds                                                        |
| *[ticks](datatype-ticks.md)*         | **Duration**                     | Duration of the spell (if any)                                                                    |
| *[ticks](datatype-ticks.md)*         | **DurationValue1**               | Duration of the spell (if any)                                                                    |
| *[timestamp](datatype-timestamp.md)* | **FizzleTime**                   | Time to recover after fizzle                                                                      |
| *[int](datatype-int.md)*             | **GemIcon**                      | Icon number of the spell. Exmaple ${Spell\[blah\].GemIcon}                                        |
| *[int](datatype-int.md)*             | **HastePct**                     | Percentage of haste, example of use ${Me.Hasted.HastePct} or ${Spell\[Speed of Milyex\].HastePct} |
| *[int](datatype-int.md)*             | **ID**                           | Spell ID                                                                                          |
| *[bool](datatype-bool.md)*           | **IsSkill**                      | is this spell a skill?                                                                            |
| *[bool](datatype-bool.md)*           | **IsSwarmSpell**                 | Is this spell a Swarm spell?                                                                      |
| *[int](datatype-int.md)*             | **Level**                        | Level                                                                                             |
| *[int](datatype-int.md)*             | **Location**                     | Appears to be max distance                                                                        |
| *[int](datatype-int.md)*             | **Mana**                         | Mana cost (unadjusted)                                                                            |
| *[timestamp](datatype-timestamp.md)* | **MyCastTime**                   | Adjusted cast time                                                                                |
| *[float](datatype-float.md)*         | **MyRange**                      | Adjusted spell range, including focus effects, etc.                                               |
| *[string](datatype-string.md)*       | **Name**                         | Spell Name                                                                                        |
| *[float](datatype-float.md)*         | **PushBack**                     | Push back amount                                                                                  |
| *[float](datatype-float.md)*         | **Range**                        | Maximum range to target (use **AERange** for AE and group spells)                                 |
| *[int](datatype-int.md)*             | **Rank**                         | Returns either 1, 2 or 3 for spells and 4-30 for clickys and potions.                             |
| *[string](datatype-string.md)*       | **RankName**                     | Returns the spell/combat ability name rank character has.                                         |
| *[float](datatype-float.md)*         | **RecastTime**                   | Time to recast after successful cast                                                              |
| *[timestamp](datatype-timestamp.md)* | **RecoveryTime**                 | Same as **FizzleTime**                                                                            |
| *[int](datatype-int.md)*             | **ResistAdj**                    | Resist adjustment                                                                                 |
| *[string](datatype-string.md)*       | **ResistType**                   | See below for Resist Types                                                                        |
| *[string](datatype-string.md)*       | **Skill**                        | See below for Skill Types                                                                         |
| *[int](datatype-int.md)*             | **SlowPct**                      | Percentage of slow, example of use ${Target.Slowed.SlowPct} or ${Spell\[Slowing Helix\].SlowPct}  |
| *[int](datatype-int.md)*             | **SpellIcon**                    | Icon number of the spell. Exmaple ${Spell\[blah\].SpellIcon}                                      |
| *[string](datatype-string.md)*       | **SpellType**                    | "Beneficial(Group)", "Beneficial", "Detrimental" or "Unknown"                                     |
| *[bool](datatype-bool.md)*           | **Stacks\[**duration**\]**       | Does the selected spell stack with your current buffs (duration is in ticks)                      |
| *[bool](datatype-bool.md)*           | **StacksPet\[**duration**\]**    | Does the selected spell stack with your pet's current buffs (duration is in ticks)                |
| *[bool](datatype-bool.md)*           | **StacksTarget\[**duration**\]** | Does the selected spell stack with your target's current buffs (duration is in ticks)             |
| *[bool](datatype-bool.md)*           | **StacksWith\[**name**\]**       | alias for .WillStack - see entry for more details                                                 |
| *[string](datatype-string.md)*       | **TargetType**                   | See below for Target Types                                                                        |
| *[string](datatype-string.md)*       | **WearOff**                      | The "wear off" message                                                                            |
| *[bool](datatype-bool.md)*           | **WillStack\[**name**\]**        | Does the selected spell stack with the specific SPELL *name* DOES NOT work with AAs.              |
| '**'[string](datatype-string.md)**   | **To String**                    | Same as **Name**                                                                                  |

## Example

` /echo I have the ${Spell[Certitude].RankName} version of Certitude. - Spell`  
` Outputs:[MQ2] I have the Certitude Rk. II version of Ceritude.`

` /cast "${Spell[Vinespur].RankName}" in your macro will cast it, since its  going to be resolved as /cast "Vinespur Rk. II"`

` /echo My version of Rest is: ${Spell[Rest].RankName} - Combat ability`  
` Outputs: [MQ2] My version of Rest is: Rest Rk. II`

## Resist Types

**ResistType** will be one of the following:

<table>
<tbody>
<tr class="odd">
<td><p>:* Chromatic</p>
<p>:* Corruption</p>
<p>:* Cold</p>
<p>:* Disease</p>
<p>:* Fire</p></td>
<td><p>:* Magic</p>
<p>:* Poison</p>
<p>:* Unknown</p>
<p>:* Unresistable</p>
<p>:* Prismatic</p></td>
</tr>
</tbody>
</table>

## Target Types

**TargetType** will be one of the following:

<table>
<tbody>
<tr class="odd">
<td><p>:* AE PC v1</p>
<p>:* AE PC v2</p>
<p>:* AE Summoned</p>
<p>:* AE Undead</p>
<p>:* Animal</p></td>
<td><p>:* Corpse</p>
<p>:* Group v1</p>
<p>:* Group v2</p>
<p>:* LifeTap</p>
<p>:* Line of Sight</p></td>
<td><p>:* PB AE</p>
<p>:* Pet</p>
<p>:* Plant</p>
<p>:* Self</p>
<p>:* Single</p></td>
<td><p>:* Summoned</p>
<p>:* Targeted AE</p>
<p>:* Targeted AE Tap</p>
<p>:* Uber Dragons</p>
<p>:* Uber Giants</p></td>
<td><p>:* Undead</p>
<p>:* Unknown</p></td>
</tr>
</tbody>
</table>

## Skill Types

**Skill** will be one of the following:

:\* Abjuration

:\* Alteration

:\* Conjuration

:\* Divination

:\* Evocation

## MyDuration

MyDuration is a custom mod located [here](https://macroquest2.com/phpBB3/viewtopic.php?t=13007). It is not supported
by the developers, nor included in the zip release.

|                                      |                |                            |
|--------------------------------------|----------------|----------------------------|
| **Type**                             | **Member**     | **Description**            |
| *[ticks](datatype-ticks.md)* | **MyDuration** | Adjusted Duration (if any) |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Spell](../top-level-objects/tlo-spell.md)

## Data Dump as of 07/31/20

-   ID
-   Address
-   AERange
-   Attrib
-   AutoCast
-   Base
-   Base2
-   BaseName
-   Beneficial
-   BookIcon
-   Calc
-   CalcIndex
-   CanMGB
-   CastByMe
-   CastByOther
-   Caster
-   CastOnAnother
-   CastOnYou
-   CastTime
-   Category
-   CounterNumber
-   CounterType
-   Deletable
-   Description
-   Duration
-   DurationValue1
-   DurationWindow
-   EnduranceCost
-   EQSpellDuration
-   Extra
-   FizzleTime
-   GemIcon
-   HasSPA
-   HastePct
-   IllusionOkWhenMounted
-   IsActiveAA
-   IsSkill
-   IsSwarmSpell
-   Level
-   Location
-   Mana
-   Max
-   MaxLevel
-   MyCastTime
-   MyDuration
-   MyRange
-   Name
-   NewStacks
-   NewStacksWith
-   NoExpendReagentID
-   NumEffects
-   PushBack
-   Range
-   Rank
-   RankName
-   ReagentCount
-   ReagentID
-   RecastTime
-   RecastTimerID
-   RecoveryTime
-   ResistAdj
-   ResistType
-   Restrictions
-   Skill
-   SlowPct
-   SPA
-   SpellGroup
-   SpellIcon
-   SpellType
-   Stacks
-   StacksPet
-   StacksSpawn
-   StacksTarget
-   StacksWith
-   StacksWithDiscs
-   Subcategory
-   SubSpellGroup
-   Target
-   TargetType
-   TimeOfDay
-   Trigger
-   WearOff
-   WillStack


