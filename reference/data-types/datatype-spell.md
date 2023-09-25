---
tags:
    - datatype
---
# `spell`

This is the type used for spell information.

## Members

### [float][float] `AERange`

:   AE range (group spells use this for their range)

### `Attrib`

:   

### `AutoCast`

:   

### [int64][int64] `Base`

:   

### [int64][int64] `Base2`

:   

### `BaseEffectsFocusCap`

:   

### `BaseName`

:   

### `Beneficial`

:   

### `BookIcon`

:   

### `Calc`

:   

### `CalcIndex`

:   

### `CanMGB`

:   

### `CastByMe`

:   

### `CastByOther`

:   

### [string][string] `CastOnAnother`

:   Message when cast on others

### [string][string] `CastOnYou`

:   Message when cast on yourself

### [timestamp][timestamp] `CastTime`

:   Cast time (unadjusted)

### [string][string] `Category`

:   Name of the category the spell belongs to (e.g. "HP Buffs")

### [int][int] `CategoryID`

:   Numeric ID of the category this spell belongs to

### [int64][int64] `CounterNumber`

:   The number of counters that the spell adds

### [string][string] `CounterType`

:   The resist counter. Will be one of "Disease", "Poison", "Curse" or "Corruption"

### [bool][bool] `Deletable`

:   Whether a spell can be deleted from the spell book

### `Description`

:   

### [bool][bool] `Dispellable`

:   Whether a spell can be dispelled

### [ticks][ticks] `Duration`

:   Duration of the spell (if any)

### [ticks][ticks] `DurationValue1`

:   Duration of the spell (if any)

### `DurationWindow`

:   

### `EnduranceCost`

:   

### `EQSpellDuration`

:   

### `Extra`

:   

### [timestamp][timestamp] `FizzleTime`

:   Time to recover after fizzle

### [int][int] `GemIcon`

:   Icon number of the spell. Example ${Spell\[blah].GemIcon}

### `HasSPA`

:   

### [int][int] `HastePct`

:   Percentage of haste, example of use ${Me.Hasted.HastePct} or ${Spell\[Speed of Milyex].HastePct}

### [int][int] `ID`

:   Spell ID

### `IllusionOkWhenMounted`

:   

### `IsActiveAA`

:   

### [bool][bool] `IsSkill`

:   is this spell a skill?

### [bool][bool] `IsSwarmSpell`

:   Is this spell a Swarm spell?

### [int][int] `Level`

:   Level

### [string][string] `Link[text]`

:   Generate a clickable spell link. _text_ is optional and overrides the text of the link.

### [int][int] `Location`

:   Appears to be max distance

### [int][int] `Mana`

:   Mana cost (unadjusted)

### [int64][int64] `Max`

:   

### [int64][int64] `MaxLevel`

:   

### [int][int] `MinCasterLevel`

:   Minimum level required by any class to cast this spell.

### [timestamp][timestamp] `MyCastTime`

:   Adjusted cast time

### `MyDuration`

:   

### [float][float] `MyRange`

:   Adjusted spell range, including focus effects, etc.

### [string][string] `Name`

:   Spell Name

### `NoExpendReagentID`

:   

### `NumEffects`

:   

### [float][float] `PushBack`

:   Push back amount

### [float][float] `Range`

:   Maximum range to target (use **AERange** for AE and group spells)

### [int][int] `Rank`

:   Returns either 1, 2 or 3 for spells and 4-30 for clickables and potions.

### [string][string] `RankName`

:   Returns the spell/combat ability name rank character has.

### `ReagentCount`

:   

### `ReagentID`

:   

### [float][float] `RecastTime`

:   Time to recast after successful cast

### `RecastTimerID`

:   

### [timestamp][timestamp] `RecoveryTime`

:   Same as **FizzleTime**

### [int][int] `ResistAdj`

:   Resist adjustment

### [string][string] `ResistType`

:   See below for Resist Types

### `Restrictions`

:   

### [string][string] `Skill`

:   See below for Skill Types

### [int][int] `SlowPct`

:   Percentage of slow, example of use ${Target.Slowed.SlowPct} or ${Spell\[Slowing Helix].SlowPct}

### `SpellGroup`

:   

### [int][int] `SpellIcon`

:   Numeric ID of the Icon used to represent the spell.

### [string][string] `SpellType`

:   "Beneficial(Group)", "Beneficial", "Detrimental" or "Unknown"

### [bool][bool] `Stacks[duration]`

:   Does the selected spell stack with your current buffs (duration is in ticks)

### [bool][bool] `StacksPet[duration]`

:   Does the selected spell stack with your pet's current buffs (duration is in ticks)

### `StacksSpawn`

:   

### [bool][bool] `StacksTarget`

:   Does the selected spell stack with your target's current buffs

### [bool][bool] `StacksWith[name]`

:   alias for .WillStack - see entry for more details

### `StacksWithDiscs`

:   

### [string][string] `Subcategory`

:   Name of the subcategory this spell belongs to (e.g. "Shielding")

### [int][int] `SubcategoryID`

:   Numeric Id of the subcategory this spell belongs to.

### `SubSpellGroup`

:   

### [string][string] `TargetType`

:   See below for Target Types

### `TimeOfDay`

:   

### `Trigger`

:   

### [string][string] `WearOff`

:   The "wear off" message

### [int][int] `WillLand`

:   This is like stacks but without the duration check.  It's a clean: "Will this spell land."  Returns the slot it would land in.

### [int][int] `WillLandPet`

:   Same as WillLand, but for your pet.

### [bool][bool] `WillStack[name]`

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
