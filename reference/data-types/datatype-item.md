---
tags:
    - datatype
---
# `item` Type

Contains the properties that describe an item.

## Members

### [int][int] `AC`

:   AC value on item

### [int][int] `Accuracy`

:   Accuracy

### [int][int] `AGI`

:   AGI value on item

### `Artifact`

:   

### [int][int] `Attack`

:   Attack value on item

### [bool][bool] `Attuneable`

:   Attuneable?

### [int][int] `AugRestrictions`

:   Augment Restrictions

### [int][int] `Augs`

:   Number of augs on this item

### [augtype][augtype] `AugSlot`

:   Retrieve the augment in the specified slot number.

### [int][int] `AugSlot1`

:   Returns the type of agument in slot 1

### [int][int] `AugSlot2`

:   Returns the type of agument in slot 2

### [int][int] `AugSlot3`

:   Returns the type of agument in slot 3

### [int][int] `AugSlot4`

:   Returns the type of agument in slot 4

### [int][int] `AugSlot5`

:   Returns the type of agument in slot 5

### [int][int] `AugSlot6`

:   Returns the type of agument in slot 6

### [int][int] `AugType`

:   Augmentation slot type mask.

### [int][int] `Avoidance`

:   Avoidance

### `BaneDMG`

:   

### `BaneDMGType`

:   

### [int64][int64] `BuyPrice`

:   The cost to buy this item from active merchant

### `CanUse`

:   

### [float][float] `CastTime`

:   Spell effect's cast time (in seconds)

### [int][int] `CHA`

:   CHA value on item

### [int][int] `Charges`

:   Charges

### [int][int] `Clairvoyance`

:   Clairvoyance

### [string][string] `Class[N]`

:   Returns the _Nth_ long class name of the listed classes on an item. Items suitable for ALL classes will effectively have all 17 classes listed.

### [int][int] `Classes`

:   The number of classes that can use the item. Items suitable for ALL classes will return 16.

### [itemspell][itemspell] `Clicky`

:   Activatable spell effect, if any.

### `Collectible`

:   

### [int][int] `CombatEffects`

:   CombatEffects

### `Combinable`

:   

### [int][int] `Container`

:   Number of slots, if this is a container

### `ContentSize`

:   

### `Damage`

:   

### [int][int] `DamageShieldMitigation`

:   Damage Shield Mitigation

### [int][int] `DamShield`

:   Damage Shield value on item

### [int][int] `Deities`

:   The number of deities that can use the item. Items with no deity restrictions will return 0.

### [string][string] `Deity[N]`

:   Returns the _Nth_ deity of the listed deities on an item. Items with no deity restrictions will return NULL for all values of _N_.

### `Delay`

:   

### [int][int] `DEX`

:   DEX value on item

### `DMGBonus`

:   

### [string][string] `DMGBonusType`

:   "None", "Magic", "Fire", "Cold", "Poison", "Disease"

### [int][int] `DoTShielding`

:   DoT Shielding

### [string][string] `EffectType`

:   Spell effect type ([see below](#spell-effect-types) for spell effect types)

### [int][int] `Endurance`

:   Endurance

### [int][int] `EnduranceRegen`

:   Endurance regen

### [evolving][evolving] `Evolving`

:   Does this item have Evolving experience on?

### `Expendable`

:   

### [itemspell][itemspell] `Familiar`

:   Familiar spell effect, if any.

### `FirstFreeSlot`

:   

### [itemspell][itemspell] `Focus`

:   First focus effect, if any.

### [itemspell][itemspell] `Focus2`

:   Second focus effect, if any.

### `FocusID`

:   

### [int][int] `FreeStack`

:   The number of items needed to fill all the stacks of the item you have (with a stacksize of 20\).  If you have 3 stacks \(1, 10, 20 in those stacks), you have room for 60 total and you have 31 on you, so **FreeStack** would return 29.

### [int][int] `Haste`

:   Haste value on item

### [int][int] `HealAmount`

:   HealAmount (regen?)

### `Heirloiom`

:   

### [int][int] `HeroicAGI`

:   Heroic AGI value on item

### [int][int] `HeroicCHA`

:   Heroic CHA value on item

### [int][int] `HeroicDEX`

:   Heroic DEX value on item

### [int][int] `HeroicINT`

:   Heroic INT value on item

### [int][int] `HeroicSTA`

:   Heroic STA value on item

### [int][int] `HeroicSTR`

:   Heroic STR value on item

### [int][int] `HeroicSvCold`

:   Heroic SvCold value on item

### [int][int] `HeroicSvCorruption`

:   Heroic SvCorruption value on item

### [int][int] `HeroicSvDisease`

:   Heroic SvDisease value on item

### [int][int] `HeroicSvFire`

:   Heroic SvFire value on item

### [int][int] `HeroicSvMagic`

:   Heroic SvMagic value on item

### [int][int] `HeroicSvPoison`

:   Heroic SvPoison value on item

### [int][int] `HeroicWIS`

:   Heroic WIS value on item

### [int][int] `HP`

:   HP value on item

### [int][int] `HPRegen`

:   HPRegen value on item

### [int][int] `Icon`

:   Item Icon

### [int][int] `ID`

:   Item ID

### `IDFile`

:   

### `IDFile2`

:   

### [itemspell][itemspell] `Illusion`

:   Illusion spell effect, if any.

### [float][float] `InstrumentMod`

:   Instrument Modifier Value

### `InstrumentType`

:   

### [int][int] `INT`

:   INT value on item

### [int][int] `InvSlot`

:   Inventory Slot Number (Historic and now deprecated, use ItemSlot and ItemSlot2)

### [item][item] `Item[N]`

:   Item in _Nth_ slot, if this is a container or has augs

### [float][float] `ItemDelay`

:   Returns the delay of the weapon

### [string][string] `ItemLink[CLICKABLE]`

:   just prints the actual hexlink for an item (not clickable) unless \[CLICKABLE] is included

### [int][int] `Items`

:   Number of items, if this is a container.

### [int][int] `ItemSlot`

:   Item Slot number see [Slot Names](../../reference/general/slot-names.md)

### [int][int] `ItemSlot2`

:   Item Slot subnumber see [Slot Names](../../reference/general/slot-names.md)

### `LDoNCost`

:   

### [string][string] `LDoNTheme`

:   "All", "Deepest Guk", "Miragul's", "Mistmoore", "Rujarkian", "Takish", "Unknown"

### `Level`

:   

### `Light`

:   

### [bool][bool] `Lore`

:   Lore?

### `LoreEquipped`

:   

### `LoreText`

:   

### `Luck`

:   

### [bool][bool] `Magic`

:   Magic?

### [int][int] `Mana`

:   Mana value on item

### [int][int] `ManaRegen`

:   ManaRegen value on item

### `MaxLuck`

:   

### [int][int] `MaxPower`

:   Max power on an power source

### [int][int] `MerchQuantity`

:   Quantity of item active merchant has

### `MinLuck`

:   

### [itemspell][itemspell] `Mount`

:   Mount spell effect, if any.

### [string][string] `Name`

:   Name

### `NoDestroy`

:   

### [bool][bool] `NoDrop`

:   No Trade?

### [bool][bool] `NoRent`

:   Temporary?

### `NoTrade`

:   Synonym for NoDrop

### `Open`

:   

### `OrnamentationIcon`

:   

### `PctPower`

:   

### `PendingLore`

:   

### [int][int] `Power`

:   Power left on power source

### `Prestige`

:   

### [itemspell][itemspell] `Proc`

:   Combat proc effect.

### `ProcRate`

:   

### [int][int] `Purity`

:   Purity of item

### `Quality`

:   

### `Quest`

:   

| [_string_](datatype-string.md) | **Race**[_N_] | Returns the _Nth_ long race name of the listed races on an item. Items suitable for ALL races will effectively have all 15 races listed. 
### [int][int] `Races`

:   The number of races that can use the item. Items suitable for ALL races will return 15.

### `Range`

:   

### [int][int] `RecommendedLevel`

:   Returns the Recommended Level of an item. Items with no recommended level will return 0.

### [int][int] `RequiredLevel`

:   Returns the Required Level of an item. Items with no required level will return 0.

### [itemspell][itemspell] `Scroll`

:   Scroll effect, if any.

### [int][int] `SellPrice`

:   Price to sell this item at this merchant

### [int][int] `Shielding`

:   Shielding

### [int][int] `Size`

:   Item size:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT

### [int][int] `SizeCapacity`

:   If item is a container, size of items it can hold:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT

### `Skill`

:   

### `SkillModMax`

:   

### `SkillModValue`

:   

### `SlotsUsedByItem`

:   

### [spell][spell] `Spell`

:   Spell effect

### [int][int] `SpellDamage`

:   Spell damage

### [int][int] `SpellShield`

:   SpellShield

### [int][int] `STA`

:   STA value on item

### [int][int] `Stack`

:   Number of items in the stack

### [bool][bool] `Stackable`

:   Stackable?

### [int][int] `StackCount`

:   The total number of the stackable item in your inventory

### [int][int] `Stacks`

:   Number of stacks of the item in your inventory

### [int][int] `StackSize`

:   Maximum number if items that can be in the stack

### [int][int] `STR`

:   STR value on item

### [int][int] `StrikeThrough`

:   StrikeThrough

### [int][int] `StunResist`

:   Stun resist

### [int][int] `svCold`

:   svCold value on item

### [int][int] `svCorruption`

:   svCorruption value on item

### [int][int] `svDisease`

:   svDisease value on item

### [int][int] `svFire`

:   svFire value on item

### [int][int] `svMagic`

:   svMagic value on item

### [int][int] `svPoison`

:   svPoison value on item

### [ticks][ticks] `Timer`

:   Returns the number of ticks remaining on an item recast timer

### [int][int] `TimerReady`

:   Returns the number of seconds remaining on an item recast timer

### [bool][bool] `Tradeskills`

:   Tradeskills?

### [int][int] `Tribute`

:   Tribute value of the item

### [string][string] `Type`

:   Type

### [int][int] `Value`

:   Item value in coppers

### [int][int] `Weight`

:   Item weight

### `WeightReduction`

:   

### [int][int] `WIS`

:   WIS value on item

### [itemspell][itemspell] `Worn`

:   Passive worn effect, if any.

| [_invslot_](datatype-invslot.md) | **WornSlot**[_N_] | The _Nth_ invslot this item can be worn in (fingers/ears count as 2 slots) 
### [bool][bool] `WornSlot[name]`

:   Can item be worn in invslot with this _name_? (worn slots only)

### [int][int] `WornSlots`

:   The number of invslots this item can be worn in (fingers/ears count as 2 slots)

### [string][string] `(To String)`

:   Same as **Name**


## Methods

| Name           | Action                 |
| -------------- | ---------------------- |
| **Inspect**    | Opens the item display window for this item |


### Spell Effect Types

**EffectType** will return one of the following values:

`Click Inventory`

:   Item has a right-click effect and can be used from the inventory.

`Click Unknown`

:   Item has an unknown right-click effect restriction.

`Click Worn`

:   Item has a right-click effect and must be equipped to use it.

`Combat`

:   Item has a combat proc effect.

`Spell Scroll`

:   Item is a scribable spell scroll, and the effect is the spell that will be scribed.

`Worn`

:   Item has an effect that is persistent while worn (focus effect).

## DisplayItem Index

!!! warning

    This section needs to be moved to the MQ2ItemDisplay article

**${DisplayItem}** now takes an index as an option parameter index can be 0-5 you can still just do ${DsiplayItem} and it will just pick whatever you inspected last.

**Example:** /echo ${DisplayItem[5]}

* Info = 1,
* WindowTitle = 2,
* AdvancedLore = 3,
* MadeBy = 4,
* Information = 5,
* DisplayIndex = 6

**NOTE:** There is a difference between .Info and .Information .Info contains for example: .Info can return text like; this item is placable in yards, guild yards blah blah , This item can be used in tradeskills .Information can return text like Item Information: Placing this augment into blah blah, this armor can only be used in blah blah

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
