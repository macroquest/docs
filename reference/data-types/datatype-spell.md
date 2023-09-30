---
tags:
    - datatype
---
# `spell`

This is the type used for spell information.

## Members

### {{ renderMember(type='float', name='AERange') }} 

:   AE range (group spells use this for their range)

### {{ renderMember(name='Attrib') }} 

:   

### {{ renderMember(name='AutoCast') }} 

:   

### {{ renderMember(type='int64', name='Base') }} 

:   

### {{ renderMember(type='int64', name='Base2') }} 

:   

### {{ renderMember(name='BaseEffectsFocusCap') }} 

:   

### {{ renderMember(name='BaseName') }} 

:   

### {{ renderMember(name='Beneficial') }} 

:   

### {{ renderMember(name='BookIcon') }} 

:   

### {{ renderMember(name='Calc') }} 

:   

### {{ renderMember(name='CalcIndex') }} 

:   

### {{ renderMember(name='CanMGB') }} 

:   

### {{ renderMember(name='CastByMe') }} 

:   

### {{ renderMember(name='CastByOther') }} 

:   

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

### {{ renderMember(name='Description') }} 

:   

### {{ renderMember(type='bool', name='Dispellable') }} 

:   Whether a spell can be dispelled

### {{ renderMember(type='ticks', name='Duration') }} 

:   Duration of the spell (if any)

### {{ renderMember(type='ticks', name='DurationValue1') }} 

:   Duration of the spell (if any)

### {{ renderMember(name='DurationWindow') }} 

:   

### {{ renderMember(name='EnduranceCost') }} 

:   

### {{ renderMember(name='EQSpellDuration') }} 

:   

### {{ renderMember(name='Extra') }} 

:   

### {{ renderMember(type='timestamp', name='FizzleTime') }} 

:   Time to recover after fizzle

### {{ renderMember(type='int', name='GemIcon') }} 

:   Icon number of the spell. Example ${Spell\[blah].GemIcon}

### {{ renderMember(name='HasSPA') }} 

:   

### {{ renderMember(type='int', name='HastePct') }} 

:   Percentage of haste, example of use ${Me.Hasted.HastePct} or ${Spell\[Speed of Milyex].HastePct}

### {{ renderMember(type='int', name='ID') }} 

:   Spell ID

### {{ renderMember(name='IllusionOkWhenMounted') }} 

:   

### {{ renderMember(name='IsActiveAA') }} 

:   

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

:   

### {{ renderMember(type='int64', name='MaxLevel') }} 

:   

### {{ renderMember(type='int', name='MinCasterLevel') }} 

:   Minimum level required by any class to cast this spell.

### {{ renderMember(type='timestamp', name='MyCastTime') }} 

:   Adjusted cast time

### {{ renderMember(name='MyDuration') }} 

:   

### {{ renderMember(type='float', name='MyRange') }} 

:   Adjusted spell range, including focus effects, etc.

### {{ renderMember(type='string', name='Name') }} 

:   Spell Name

### {{ renderMember(name='NoExpendReagentID') }} 

:   

### {{ renderMember(name='NumEffects') }} 

:   

### {{ renderMember(type='float', name='PushBack') }} 

:   Push back amount

### {{ renderMember(type='float', name='Range') }} 

:   Maximum range to target (use **AERange** for AE and group spells)

### {{ renderMember(type='int', name='Rank') }} 

:   Returns either 1, 2 or 3 for spells and 4-30 for clickables and potions.

### {{ renderMember(type='string', name='RankName') }} 

:   Returns the spell/combat ability name rank character has.

### {{ renderMember(name='ReagentCount') }} 

:   

### {{ renderMember(name='ReagentID') }} 

:   

### {{ renderMember(type='float', name='RecastTime') }} 

:   Time to recast after successful cast

### {{ renderMember(name='RecastTimerID') }} 

:   

### {{ renderMember(type='timestamp', name='RecoveryTime') }} 

:   Same as **FizzleTime**

### {{ renderMember(type='int', name='ResistAdj') }} 

:   Resist adjustment

### {{ renderMember(type='string', name='ResistType') }} 

:   See below for Resist Types

### {{ renderMember(name='Restrictions') }} 

:   

### {{ renderMember(type='string', name='Skill') }} 

:   See below for Skill Types

### {{ renderMember(type='int', name='SlowPct') }} 

:   Percentage of slow, example of use ${Target.Slowed.SlowPct} or ${Spell\[Slowing Helix].SlowPct}

### {{ renderMember(name='SpellGroup') }} 

:   

### {{ renderMember(type='int', name='SpellIcon') }} 

:   Numeric ID of the Icon used to represent the spell.

### {{ renderMember(type='string', name='SpellType') }} 

:   "Beneficial(Group)", "Beneficial", "Detrimental" or "Unknown"

### {{ renderMember(type='bool', name='Stacks', params='duration') }} 

:   Does the selected spell stack with your current buffs (duration is in ticks)

### {{ renderMember(type='bool', name='StacksPet', params='duration') }} 

:   Does the selected spell stack with your pet's current buffs (duration is in ticks)

### {{ renderMember(name='StacksSpawn') }} 

:   

### {{ renderMember(type='bool', name='StacksTarget') }} 

:   Does the selected spell stack with your target's current buffs

### {{ renderMember(type='bool', name='StacksWith', params='name') }} 

:   alias for .WillStack - see entry for more details

### {{ renderMember(name='StacksWithDiscs') }} 

:   

### {{ renderMember(type='string', name='Subcategory') }} 

:   Name of the subcategory this spell belongs to (e.g. "Shielding")

### {{ renderMember(type='int', name='SubcategoryID') }} 

:   Numeric Id of the subcategory this spell belongs to.

### {{ renderMember(name='SubSpellGroup') }} 

:   

### {{ renderMember(type='string', name='TargetType') }} 

:   See below for Target Types

### {{ renderMember(name='TimeOfDay') }} 

:   

### {{ renderMember(name='Trigger') }} 

:   

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
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
