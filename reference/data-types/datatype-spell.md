---
tags:
    - datatype
---
# `spell`

This is the type used for spell information.

## Members

| **Type**                             | **Member**                   | **Description**                                                                                                                |
| ------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [_float_](datatype-float.md)         | **AERange**                  | AE range (group spells use this for their range)                                                                               |
| | **Attrib** | |
| | **AutoCast** | |
| [_int64_](datatype-int64.md) | **Base** | |
| [_int64_](datatype-int64.md) | **Base2** | |
| | **BaseEffectsFocusCap** | |
| | **BaseName** | |
| | **Beneficial** | |
| | **BookIcon** | |
| | **Calc** | |
| | **CalcIndex** | |
| | **CanMGB** | |
| | **CastByMe** | |
| | **CastByOther** | |
| [_string_](datatype-string.md)       | **CastOnAnother**            | Message when cast on others                                                                                                    |
| [_string_](datatype-string.md)       | **CastOnYou**                | Message when cast on yourself                                                                                                  |
| [_timestamp_](datatype-timestamp.md) | **CastTime**                 | Cast time (unadjusted)                                                                                                         |
| | **Category** | |
| [_int64_](datatype-int64.md)         | **CounterNumber**            | The number of counters that the spell adds                                                                                     |
| [_string_](datatype-string.md)       | **CounterType**              | The resist counter. Will be one of "Disease", "Poison", "Curse" or "Corruption"                                                |
| [_bool_](datatype-string.md) | **Deletable** | Whether a spell can be deleted from the spell book |
| | **Description** | |
| [_bool_](datatype-string.md) | **Dispellable** | Whether a spell can be dispelled |
| [_ticks_](datatype-ticks.md)         | **Duration**                 | Duration of the spell (if any)                                                                                                 |
| [_ticks_](datatype-ticks.md)         | **DurationValue1**           | Duration of the spell (if any)                                                                                                 |
| | **DurationWindow** | |
| | **EnduranceCost** | |
| | **EQSpellDuration** | |
| | **Extra** | |
| [_timestamp_](datatype-timestamp.md) | **FizzleTime**               | Time to recover after fizzle                                                                                                   |
| [_int_](datatype-int.md)             | **GemIcon**                  | Icon number of the spell. Example ${Spell\[blah].GemIcon}                                                                      |
| | **HasSPA** | |
| [_int_](datatype-int.md)             | **HastePct**                 | Percentage of haste, example of use ${Me.Hasted.HastePct} or ${Spell\[Speed of Milyex].HastePct}                               |
| [_int_](datatype-int.md)             | **ID**                       | Spell ID                                                                                                                       |
| | **IllusionOkWhenMounted** | |
| | **IsActiveAA** | |
| [_bool_](datatype-bool.md)           | **IsSkill**                  | is this spell a skill?                                                                                                         |
| [_bool_](datatype-bool.md)           | **IsSwarmSpell**             | Is this spell a Swarm spell?                                                                                                   |
| [_int_](datatype-int.md)             | **Level**                    | Level                                                                                                                          |
| [_int_](datatype-int.md)             | **Location**                 | Appears to be max distance                                                                                                     |
| [_int_](datatype-int.md)             | **Mana**                     | Mana cost (unadjusted)                                                                                                         |
| [_int64_](datatype-int64.md) | **Max** | |
| [_int64_](datatype-int64.md) | **MaxLevel** | |
| [_timestamp_](datatype-timestamp.md) | **MyCastTime**               | Adjusted cast time                                                                                                             |
| | **MyDuration** | |
| [_float_](datatype-float.md)         | **MyRange**                  | Adjusted spell range, including focus effects, etc.                                                                            |
| [_string_](datatype-string.md)       | **Name**                     | Spell Name                                                                                                                     |
| | **NoExpendReagentID** | |
| | **NumEffects** | |
| [_float_](datatype-float.md)         | **PushBack**                 | Push back amount                                                                                                               |
| [_float_](datatype-float.md)         | **Range**                    | Maximum range to target (use **AERange** for AE and group spells)                                                              |
| [_int_](datatype-int.md)             | **Rank**                     | Returns either 1, 2 or 3 for spells and 4-30 for clickables and potions.                                                       |
| [_string_](datatype-string.md)       | **RankName**                 | Returns the spell/combat ability name rank character has.                                                                      |
| | **ReagentCount** | |
| | **ReagentID** | |
| [_float_](datatype-float.md)         | **RecastTime**               | Time to recast after successful cast                                                                                           |
| | **RecastTimerID** | |
| [_timestamp_](datatype-timestamp.md) | **RecoveryTime**             | Same as **FizzleTime**                                                                                                         |
| [_int_](datatype-int.md)             | **ResistAdj**                | Resist adjustment                                                                                                              |
| [_string_](datatype-string.md)       | **ResistType**               | See below for Resist Types                                                                                                     |
| | **Restrictions** | |
| [_string_](datatype-string.md)       | **Skill**                    | See below for Skill Types                                                                                                      |
| [_int_](datatype-int.md)             | **SlowPct**                  | Percentage of slow, example of use ${Target.Slowed.SlowPct} or ${Spell\[Slowing Helix].SlowPct}                                |
| | **SPA** | |
| | **SpellGroup** | |
| [_int_](datatype-int.md)             | **SpellIcon**                | Icon number of the spell. Exmaple ${Spell\[blah].SpellIcon}                                                                    |
| [_string_](datatype-string.md)       | **SpellType**                | "Beneficial(Group)", "Beneficial", "Detrimental" or "Unknown"                                                                  |
| [_bool_](datatype-bool.md)           | **Stacks**[ _duration_ ]     | Does the selected spell stack with your current buffs (duration is in ticks)                                                   |
| [_bool_](datatype-bool.md)           | **StacksPet**[ _duration_ ]  | Does the selected spell stack with your pet's current buffs (duration is in ticks)                                             |
| | **StacksSpawn** | |
| [_bool_](datatype-bool.md)           | **StacksTarget**             | Does the selected spell stack with your target's current buffs                                                                 |
| [_bool_](datatype-bool.md)           | **StacksWith**[ _name_ ]     | alias for .WillStack - see entry for more details                                                                              |
| | **StacksWithDiscs** | |
| | **Subcategory** | |
| | **SubSpellGroup** | |
| [_string_](datatype-string.md)       | **TargetType**               | See below for Target Types                                                                                                     |
| | **TimeOfDay** | |
| | **Trigger** | |
| [_string_](datatype-string.md)       | **WearOff**                  | The "wear off" message                                                                                                         |
| [_int_](datatype-int.md)             | **WillLand**                 | This is like stacks but without the duration check.  It's a clean: "Will this spell land."  Returns the slot it would land in. |
| [_int_](datatype-int.md)             | **WillLandPet**              | Same as WillLand, but for your pet.                                                                                            |
| [_bool_](datatype-bool.md)           | **WillStack**[ _name_ ]      | Does the selected spell stack with the specific SPELL _name_ DOES NOT work with AAs.                                           |
| [_string_](datatype-string.md)       | **(To String)**                | Same as **Name**                                                                                                               |

## Spell Ranks

```
/echo I have the ${Spell[Certitude].RankName} version of Certitude. - Spell
```

Outputs: `I have the Certitude Rk. II version of Ceritude.`

`/cast "${Spell[Vinespur].RankName}"` in your macro will cast the proper rank, since its going to be resolved as /cast "Vinespur Rk. II"

```
/echo My version of Rest is: ${Spell[Rest].RankName} - Combat ability
```

Outputs: `My version of Rest is: Rest Rk. II`

## Resist Types

**ResistType** will be one of the following:

* Chromatic
* Corruption
* Cold
* Disease
* Fire
* Magic
* Poison
* Unresistable
* Prismatic
* Unknown

## Spell Types

**SpellType** will be one of the following:

* Beneficial(Group)
* Beneficial
* Detrimental
* Unknown

## Target Types

**TargetType** will be one of the following:

* AE PC v1
* AE PC v2
* AE Summoned
* AE Undead
* Animal
* Beam
* Caster PB NPC
* Caster PB PC
* Chest
* Corpse
* Directional AE
* Free Target
* Group v1
* Group v2
* Hatelist
* Hatelist2
* LifeTap
* Line of Sight
* No Pets
* None
* PB AE
* Pet
* Pet Owner
* Pet2
* Plant
* Self
* Single
* Single Friendly (or Target's Target)
* Single in Group
* Special Muramites
* Summoned
* Target of Target
* Target_AE_No_Players_Pets
* Targeted AE
* Targeted AE Tap
* Uber Dragons
* Uber Giants
* Undead
* Unknown

## Skill Types

**Skill** will be one of the following:

* Abjuration
* Alteration
* Conjuration
* Divination
* Evocation
