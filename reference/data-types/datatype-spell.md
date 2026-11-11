---
tags:
    - datatype
---
# `spell`

<!--dt-desc-start-->
This is the type used for spell information.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int ActorTagId
???
///

/// member | float AERange
AE range (group spells use this for their range)
///

/// member | int Attrib
???
///

/// member | int AutoCast
???
///

/// member | int64 Base
???
///

/// member | int64 Base2
???
///

/// member | int BaseEffectsFocusCap
???
///

/// member | string BaseName
???
///

/// member | bool Beneficial
Returns true if the spell is beneficial (or beneficial group)
///

/// member | int BookIcon
Numeric ID of the Icon used to represent the spell.
///

/// member | int Calc
???
///

/// member | int CalcIndex
???
///

/// member | bool CanMGB
???
///

/// member | string CastByMe
???
///

/// member | string CastByOther
???
///

/// member | string CastOnAnother
Message when cast on others
///

/// member | string CastOnYou
Message when cast on yourself
///

/// member | timestamp CastTime
Cast time (unadjusted)
///

/// member | string Category
Name of the category the spell belongs to (e.g. "HP Buffs")
///

/// member | int CategoryID
Numeric ID of the category this spell belongs to
///

/// member | int64 CounterNumber
The number of counters that the spell adds
///

/// member | string CounterType
The resist counter. Will be one of "Disease", "Poison", "Curse" or "Corruption"
///

/// member | bool Deletable
Whether a spell can be deleted from the spell book
///

/// member | string Description
???
///

/// member | bool Dispellable
Whether a spell can be dispelled
///

/// member | ticks Duration
Duration of the spell (if any)
///

/// member | ticks DurationValue1
Duration of the spell (if any)
///

/// member | int DurationWindow
???
///

/// member | int EnduranceCost
???
///

/// member | ticks EQSpellDuration
???
///

/// member | string Extra
???
///

/// member | timestamp FizzleTime
Time to recover after fizzle
///

/// member | int GemIcon
Icon number of the spell. Example ${Spell\[blah].GemIcon}
///

/// member | bool HasSPA[#]
???
///

/// member | int HastePct
Percentage of haste, example of use ${Me.Hasted.HastePct} or ${Spell\[Speed of Milyex].HastePct}
///

/// member | int ID
Spell ID
///

/// member | bool IllusionOkWhenMounted
???
///

/// member | bool IsActiveAA
???
///

/// member | bool IsSkill
is this spell a skill?
///

/// member | bool IsSwarmSpell
Is this spell a Swarm spell?
///

/// member | int Level
Level
///

/// member | string Link[text]
Generate a clickable spell link. _text_ is optional and overrides the text of the link.
///

/// member | int Location
Appears to be max distance
///

/// member | int Mana
Mana cost (unadjusted)
///

/// member | int64 Max
???
///

/// member | int64 MaxLevel
???
///

/// member | int MinCasterLevel
Minimum level required by any class to cast this spell.
///

/// member | timestamp MyCastTime
Adjusted cast time
///

/// member | ticks MyDuration
???
///

/// member | float MyRange
Adjusted spell range, including focus effects, etc.
///

/// member | string Name
Spell Name
///

/// member | int NoExpendReagentID
???
///

/// member | int NumEffects
???
///

/// member | bool PreventsRegen
Returns true if the spell is a detrimental effect that prevents OOC regen
///

/// member | float PushBack
Push back amount
///

/// member | float Range
Maximum range to target (use **AERange** for AE and group spells)
///

/// member | int Rank
Returns either 1, 2 or 3 for spells and 4-30 for clickables and potions.
///

/// member | string RankName
Returns the spell/combat ability name rank character has.
///

/// member | int ReagentCount
???
///

/// member | int ReagentID
???
///

/// member | float RecastTime
Time to recast after successful cast
///

/// member | int RecastTimerID
???
///

/// member | timestamp RecoveryTime
Same as **FizzleTime**
///

/// member | int ResistAdj
Resist adjustment
///

/// member | string ResistType
The resist type of the spell. Will be one of the following:

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
///

/// member | string Restrictions
???
///

/// member | string Skill
The skil used by the spell. Will be one of the following:

* Abjuration
* Alteration
* Conjuration
* Divination
* Evocation
///

/// member | int SlowPct
Percentage of slow, example of use ${Target.Slowed.SlowPct} or ${Spell\[Slowing Helix].SlowPct}
///

/// member | int SpellGroup
???
///

/// member | int SpellIcon
Numeric ID of the Icon used to represent the spell.
///

/// member | string SpellType
The type of spell. Will be one of the following:

* Beneficial(Group)
* Beneficial
* Detrimental
* Unknown
///

/// member | bool Stacks[duration]
Does the selected spell stack with your current buffs (duration is in ticks)
///

/// member | bool StacksPet[duration]
Does the selected spell stack with your pet's current buffs (duration is in ticks)
///

/// member | bool StacksSpawn
???
///

/// member | bool StacksTarget
Does the selected spell stack with your target's current buffs
///

/// member | bool StacksWith[name]
alias for .WillStack - see entry for more details
///

/// member | bool StacksWithDiscs
???
///

/// member | string Subcategory
Name of the subcategory this spell belongs to (e.g. "Shielding")
///

/// member | int SubcategoryID
Numeric Id of the subcategory this spell belongs to.
///

/// member | int SubSpellGroup
???
///

/// member | string TargetType
The targeting method of the spell. Will be one of the following:

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
///

/// member | int TimeOfDay
???
///

/// member | spell Trigger
???
///

/// member | string WearOff
The "wear off" message
///

/// member | int WillLand
This is like stacks but without the duration check.  It's a clean: "Will this spell land."  Returns the slot it would land in.
///

/// member | int WillLandPet
Same as WillLand, but for your pet.
///

/// member | bool WillStack[name]
Does the selected spell stack with the specific SPELL _name_ DOES NOT work with AAs.
///

### [string][string] `(To String)`

:   Same as **Name**
<!--dt-members-end-->

## Methods

| Name           | Action                 |
| -------------- | ---------------------- |
| **Inspect**    | Opens the spell display window for this spell |


## Conversions

_Spell_ variables can be assigned the following types with **/vardata**:

* [_int_](datatype-int.md): Assigns the spell by spell id
* [_string_](datatype-string.md): Assigns the spell by spell name
* [_spell_](datatype-spell.md): Copies a spell stored in another var

_Spell_ variables can also be assigned an id or name with **/varset**. These conversions are equivalent to the [**Spell**](../top-level-objects/tlo-spell.md) TLO.

## Spell Ranks

Spell Example:

```
> /echo I have the ${Spell[Certitude].RankName} version of Certitude.
I have the Certitude Rk. II version of Ceritude.
```

Combat Ability Example:
```
> /echo My version of Rest is: ${Spell[Rest].RankName}
My version of Rest is: Rest Rk. II
```

To cast a spell with the proper rank, use the following:

```
/cast "${Spell[Vinespur].RankName}"
```

<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[spell]: datatype-spell.md
[string]: datatype-string.md
[ticks]: datatype-ticks.md
[timestamp]: datatype-timestamp.md
<!--dt-linkrefs-end-->
