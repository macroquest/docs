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
### {{ renderMember(type='int', name='ActorTagId') }}

:   ???

### {{ renderMember(type='float', name='AERange') }}

:   AE range (group spells use this for their range)

### {{ renderMember(type='int', name='Attrib') }}

:   ???

### {{ renderMember(type='int', name='AutoCast') }}

:   ???

### {{ renderMember(type='int64', name='Base') }}

:   ???

### {{ renderMember(type='int64', name='Base2') }}

:   ???

### {{ renderMember(type='int', name='BaseEffectsFocusCap') }}

:   ???

### {{ renderMember(type='string', name='BaseName') }}

:   ???

### {{ renderMember(type='bool', name='Beneficial') }}

:   ???

### {{ renderMember(type='int', name='BookIcon') }}

:   Numeric ID of the Icon used to represent the spell.

### {{ renderMember(type='int', name='Calc') }}

:   ???

### {{ renderMember(type='int', name='CalcIndex') }}

:   ???

### {{ renderMember(type='bool', name='CanMGB') }}

:   ???

### {{ renderMember(type='string', name='CastByMe') }}

:   ???

### {{ renderMember(type='string', name='CastByOther') }}

:   ???

### {{ renderMember(type='string', name='CastOnAnother') }}

:   Message when cast on others

### {{ renderMember(type='string', name='CastOnYou') }}

:   Message when cast on yourself

### {{ renderMember(type='timestamp', name='CastTime') }}

:   Cast time (unadjusted)

### {{ renderMember(type='string', name='Category') }}

:   Name of the category the spell belongs to (e.g. "HP Buffs")

### {{ renderMember(type='int', name='CategoryID') }}

:   Numeric ID of the category this spell belongs to

### {{ renderMember(type='int64', name='CounterNumber') }}

:   The number of counters that the spell adds

### {{ renderMember(type='string', name='CounterType') }}

:   The resist counter. Will be one of "Disease", "Poison", "Curse" or "Corruption"

### {{ renderMember(type='bool', name='Deletable') }}

:   Whether a spell can be deleted from the spell book

### {{ renderMember(type='string', name='Description') }}

:   ???

### {{ renderMember(type='bool', name='Dispellable') }}

:   Whether a spell can be dispelled

### {{ renderMember(type='ticks', name='Duration') }}

:   Duration of the spell (if any)

### {{ renderMember(type='ticks', name='DurationValue1') }}

:   Duration of the spell (if any)

### {{ renderMember(type='int', name='DurationWindow') }}

:   ???

### {{ renderMember(type='int', name='EnduranceCost') }}

:   ???

### {{ renderMember(type='ticks', name='EQSpellDuration') }}

:   ???

### {{ renderMember(type='string', name='Extra') }}

:   ???

### {{ renderMember(type='timestamp', name='FizzleTime') }}

:   Time to recover after fizzle

### {{ renderMember(type='int', name='GemIcon') }}

:   Icon number of the spell. Example ${Spell\[blah].GemIcon}

### {{ renderMember(type='bool', name='HasSPA', params='#') }}

:   ???

### {{ renderMember(type='int', name='HastePct') }}

:   Percentage of haste, example of use ${Me.Hasted.HastePct} or ${Spell\[Speed of Milyex].HastePct}

### {{ renderMember(type='int', name='ID') }}

:   Spell ID

### {{ renderMember(type='bool', name='IllusionOkWhenMounted') }}

:   ???

### {{ renderMember(type='bool', name='IsActiveAA') }}

:   ???

### {{ renderMember(type='bool', name='IsSkill') }}

:   is this spell a skill?

### {{ renderMember(type='bool', name='IsSwarmSpell') }}

:   Is this spell a Swarm spell?

### {{ renderMember(type='int', name='Level') }}

:   Level

### {{ renderMember(type='string', name='Link', params='text') }}

:   Generate a clickable spell link. _text_ is optional and overrides the text of the link.

### {{ renderMember(type='int', name='Location') }}

:   Appears to be max distance

### {{ renderMember(type='int', name='Mana') }}

:   Mana cost (unadjusted)

### {{ renderMember(type='int64', name='Max') }}

:   ???

### {{ renderMember(type='int64', name='MaxLevel') }}

:   ???

### {{ renderMember(type='int', name='MinCasterLevel') }}

:   Minimum level required by any class to cast this spell.

### {{ renderMember(type='timestamp', name='MyCastTime') }}

:   Adjusted cast time

### {{ renderMember(type='ticks', name='MyDuration') }}

:   ???

### {{ renderMember(type='float', name='MyRange') }}

:   Adjusted spell range, including focus effects, etc.

### {{ renderMember(type='string', name='Name') }}

:   Spell Name

### {{ renderMember(type='int', name='NoExpendReagentID') }}

:   ???

### {{ renderMember(type='int', name='NumEffects') }}

:   ???

### {{ renderMember(type='float', name='PushBack') }}

:   Push back amount

### {{ renderMember(type='float', name='Range') }}

:   Maximum range to target (use **AERange** for AE and group spells)

### {{ renderMember(type='int', name='Rank') }}

:   Returns either 1, 2 or 3 for spells and 4-30 for clickables and potions.

### {{ renderMember(type='string', name='RankName') }}

:   Returns the spell/combat ability name rank character has.

### {{ renderMember(type='int', name='ReagentCount') }}

:   ???

### {{ renderMember(type='int', name='ReagentID') }}

:   ???

### {{ renderMember(type='float', name='RecastTime') }}

:   Time to recast after successful cast

### {{ renderMember(type='int', name='RecastTimerID') }}

:   ???

### {{ renderMember(type='timestamp', name='RecoveryTime') }}

:   Same as **FizzleTime**

### {{ renderMember(type='int', name='ResistAdj') }}

:   Resist adjustment

### {{ renderMember(type='string', name='ResistType') }}

:   The resist type of the spell. Will be one of the following:

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

### {{ renderMember(type='string', name='Restrictions') }}

:   ???

### {{ renderMember(type='string', name='Skill') }}

:   The skil used by the spell. Will be one of the following:

    * Abjuration
    * Alteration
    * Conjuration
    * Divination
    * Evocation

### {{ renderMember(type='int', name='SlowPct') }}

:   Percentage of slow, example of use ${Target.Slowed.SlowPct} or ${Spell\[Slowing Helix].SlowPct}

### {{ renderMember(type='int', name='SpellGroup') }}

:   ???

### {{ renderMember(type='int', name='SpellIcon') }}

:   Numeric ID of the Icon used to represent the spell.

### {{ renderMember(type='string', name='SpellType') }}

:   The type of spell. Will be one of the following:

    * Beneficial(Group)
    * Beneficial
    * Detrimental
    * Unknown

### {{ renderMember(type='bool', name='Stacks', params='duration') }}

:   Does the selected spell stack with your current buffs (duration is in ticks)

### {{ renderMember(type='bool', name='StacksPet', params='duration') }}

:   Does the selected spell stack with your pet's current buffs (duration is in ticks)

### {{ renderMember(type='bool', name='StacksSpawn') }}

:   ???

### {{ renderMember(type='bool', name='StacksTarget') }}

:   Does the selected spell stack with your target's current buffs

### {{ renderMember(type='bool', name='StacksWith', params='name') }}

:   alias for .WillStack - see entry for more details

### {{ renderMember(type='bool', name='StacksWithDiscs') }}

:   ???

### {{ renderMember(type='string', name='Subcategory') }}

:   Name of the subcategory this spell belongs to (e.g. "Shielding")

### {{ renderMember(type='int', name='SubcategoryID') }}

:   Numeric Id of the subcategory this spell belongs to.

### {{ renderMember(type='int', name='SubSpellGroup') }}

:   ???

### {{ renderMember(type='string', name='TargetType') }}

:   The targeting method of the spell. Will be one of the following:

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

### {{ renderMember(type='int', name='TimeOfDay') }}

:   ???

### {{ renderMember(type='spell', name='Trigger') }}

:   ???

### {{ renderMember(type='string', name='WearOff') }}

:   The "wear off" message

### {{ renderMember(type='int', name='WillLand') }}

:   This is like stacks but without the duration check.  It's a clean: "Will this spell land."  Returns the slot it would land in.

### {{ renderMember(type='int', name='WillLandPet') }}

:   Same as WillLand, but for your pet.

### {{ renderMember(type='bool', name='WillStack', params='name') }}

:   Does the selected spell stack with the specific SPELL _name_ DOES NOT work with AAs.

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
