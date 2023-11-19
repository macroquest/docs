---
tags:
    - datatype
---
# `item` Type

Contains the properties that describe an item.

## Members

### {{ renderMember(type='int', name='AC') }} 

:   AC value on item

### {{ renderMember(type='int', name='Accuracy') }} 

:   Accuracy

### {{ renderMember(type='int', name='AGI') }} 

:   AGI value on item

### {{ renderMember(name='Artifact') }} 

:   

### {{ renderMember(type='int', name='Attack') }} 

:   Attack value on item

### {{ renderMember(type='bool', name='Attunable') }} 

:   Attunable?

### {{ renderMember(type='int', name='AugRestrictions') }} 

:   Augment Restrictions

### {{ renderMember(type='int', name='Augs') }} 

:   Number of augs on this item

### {{ renderMember(type='augtype', name='AugSlot') }} 

:   Retrieve the augment in the specified slot number.

### {{ renderMember(type='int', name='AugSlot1') }} 

:   Returns the type of agument in slot 1

### {{ renderMember(type='int', name='AugSlot2') }} 

:   Returns the type of agument in slot 2

### {{ renderMember(type='int', name='AugSlot3') }} 

:   Returns the type of agument in slot 3

### {{ renderMember(type='int', name='AugSlot4') }} 

:   Returns the type of agument in slot 4

### {{ renderMember(type='int', name='AugSlot5') }} 

:   Returns the type of agument in slot 5

### {{ renderMember(type='int', name='AugSlot6') }} 

:   Returns the type of agument in slot 6

### {{ renderMember(type='int', name='AugType') }} 

:   Augmentation slot type mask.

### {{ renderMember(type='int', name='Avoidance') }} 

:   Avoidance

### {{ renderMember(name='BaneDMG') }} 

:   

### {{ renderMember(name='BaneDMGType') }} 

:   

### {{ renderMember(type='int64', name='BuyPrice') }} 

:   The cost to buy this item from active merchant

### {{ renderMember(name='CanUse') }} 

:   

### {{ renderMember(type='float', name='CastTime') }} 

:   Spell effect's cast time (in seconds)

### {{ renderMember(type='int', name='CHA') }} 

:   CHA value on item

### {{ renderMember(type='int', name='Charges') }} 

:   Charges

### {{ renderMember(type='int', name='Clairvoyance') }} 

:   Clairvoyance

### {{ renderMember(type='string', name='Class', params='N') }} 

:   Returns the _Nth_ long class name of the listed classes on an item. Items suitable for ALL classes will effectively have all 17 classes listed.

### {{ renderMember(type='int', name='Classes') }} 

:   The number of classes that can use the item. Items suitable for ALL classes will return 16.

### {{ renderMember(type='itemspell', name='Clicky') }} 

:   Activatable spell effect, if any.

### {{ renderMember(name='Collectible') }} 

:   

### {{ renderMember(type='int', name='CombatEffects') }} 

:   CombatEffects

### {{ renderMember(name='Combinable') }} 

:   

### {{ renderMember(type='int', name='Container') }} 

:   Number of slots, if this is a container

### {{ renderMember(name='ContentSize') }} 

:   

### {{ renderMember(name='Damage') }} 

:   

### {{ renderMember(type='int', name='DamageShieldMitigation') }} 

:   Damage Shield Mitigation

### {{ renderMember(type='int', name='DamShield') }} 

:   Damage Shield value on item

### {{ renderMember(type='int', name='Deities') }} 

:   The number of deities that can use the item. Items with no deity restrictions will return 0.

### {{ renderMember(type='string', name='Deity', params='N') }} 

:   Returns the _Nth_ deity of the listed deities on an item. Items with no deity restrictions will return NULL for all values of _N_.

### {{ renderMember(name='Delay') }} 

:   

### {{ renderMember(type='int', name='DEX') }} 

:   DEX value on item

### {{ renderMember(name='DMGBonus') }} 

:   

### {{ renderMember(type='string', name='DMGBonusType') }} 

:   "None", "Magic", "Fire", "Cold", "Poison", "Disease"

### {{ renderMember(type='int', name='DoTShielding') }} 

:   DoT Shielding

### {{ renderMember(type='string', name='EffectType') }} 

:   Spell effect type ([see below](#spell-effect-types) for spell effect types)

### {{ renderMember(type='int', name='Endurance') }} 

:   Endurance

### {{ renderMember(type='int', name='EnduranceRegen') }} 

:   Endurance regen

### {{ renderMember(type='evolving', name='Evolving') }} 

:   Does this item have Evolving experience on?

### {{ renderMember(name='Expendable') }} 

:   

### {{ renderMember(type='itemspell', name='Familiar') }} 

:   Familiar spell effect, if any.

### {{ renderMember(name='FirstFreeSlot') }} 

:   

### {{ renderMember(type='itemspell', name='Focus') }} 

:   First focus effect, if any.

### {{ renderMember(type='itemspell', name='Focus2') }} 

:   Second focus effect, if any.

### {{ renderMember(name='FocusID') }} 

:   

### {{ renderMember(type='int', name='FreeStack') }} 

:   The number of items needed to fill all the stacks of the item you have (with a stacksize of 20\).  If you have 3 stacks \(1, 10, 20 in those stacks), you have room for 60 total and you have 31 on you, so **FreeStack** would return 29.

### {{ renderMember(type='int', name='Haste') }} 

:   Haste value on item

### {{ renderMember(type='int', name='HealAmount') }} 

:   HealAmount (regen?)

### {{ renderMember(name='Heirloiom') }} 

:   

### {{ renderMember(type='int', name='HeroicAGI') }} 

:   Heroic AGI value on item

### {{ renderMember(type='int', name='HeroicCHA') }} 

:   Heroic CHA value on item

### {{ renderMember(type='int', name='HeroicDEX') }} 

:   Heroic DEX value on item

### {{ renderMember(type='int', name='HeroicINT') }} 

:   Heroic INT value on item

### {{ renderMember(type='int', name='HeroicSTA') }} 

:   Heroic STA value on item

### {{ renderMember(type='int', name='HeroicSTR') }} 

:   Heroic STR value on item

### {{ renderMember(type='int', name='HeroicSvCold') }} 

:   Heroic SvCold value on item

### {{ renderMember(type='int', name='HeroicSvCorruption') }} 

:   Heroic SvCorruption value on item

### {{ renderMember(type='int', name='HeroicSvDisease') }} 

:   Heroic SvDisease value on item

### {{ renderMember(type='int', name='HeroicSvFire') }} 

:   Heroic SvFire value on item

### {{ renderMember(type='int', name='HeroicSvMagic') }} 

:   Heroic SvMagic value on item

### {{ renderMember(type='int', name='HeroicSvPoison') }} 

:   Heroic SvPoison value on item

### {{ renderMember(type='int', name='HeroicWIS') }} 

:   Heroic WIS value on item

### {{ renderMember(type='int', name='HP') }} 

:   HP value on item

### {{ renderMember(type='int', name='HPRegen') }} 

:   HPRegen value on item

### {{ renderMember(type='int', name='Icon') }} 

:   Item Icon

### {{ renderMember(type='int', name='ID') }} 

:   Item ID

### {{ renderMember(name='IDFile') }} 

:   

### {{ renderMember(name='IDFile2') }} 

:   

### {{ renderMember(type='itemspell', name='Illusion') }} 

:   Illusion spell effect, if any.

### {{ renderMember(type='float', name='InstrumentMod') }} 

:   Instrument Modifier Value

### {{ renderMember(name='InstrumentType') }} 

:   

### {{ renderMember(type='int', name='INT') }} 

:   INT value on item

### {{ renderMember(type='int', name='InvSlot') }} 

:   Inventory Slot Number (Historic and now deprecated, use ItemSlot and ItemSlot2)

### {{ renderMember(type='item', name='Item', params='N') }} 

:   Item in _Nth_ slot, if this is a container or has augs

### {{ renderMember(type='float', name='ItemDelay') }} 

:   Returns the delay of the weapon

### {{ renderMember(type='string', name='ItemLink', params='CLICKABLE') }} 

:   just prints the actual hexlink for an item (not clickable) unless \[CLICKABLE] is included

### {{ renderMember(type='int', name='Items') }} 

:   Number of items, if this is a container.

### {{ renderMember(type='int', name='ItemSlot') }} 

:   Item Slot number see [Slot Names](../../reference/general/slot-names.md)

### {{ renderMember(type='int', name='ItemSlot2') }} 

:   Item Slot subnumber see [Slot Names](../../reference/general/slot-names.md)

### {{ renderMember(name='LDoNCost') }} 

:   

### {{ renderMember(type='string', name='LDoNTheme') }} 

:   "All", "Deepest Guk", "Miragul's", "Mistmoore", "Rujarkian", "Takish", "Unknown"

### {{ renderMember(name='Level') }} 

:   

### {{ renderMember(name='Light') }} 

:   

### {{ renderMember(type='bool', name='Lore') }} 

:   Lore?

### {{ renderMember(name='LoreEquipped') }} 

:   

### {{ renderMember(name='LoreText') }} 

:   

### {{ renderMember(name='Luck') }} 

:   

### {{ renderMember(type='bool', name='Magic') }} 

:   Magic?

### {{ renderMember(type='int', name='Mana') }} 

:   Mana value on item

### {{ renderMember(type='int', name='ManaRegen') }} 

:   ManaRegen value on item

### {{ renderMember(name='MaxLuck') }} 

:   

### {{ renderMember(type='int', name='MaxPower') }} 

:   Max power on an power source

### {{ renderMember(type='int', name='MerchQuantity') }} 

:   Quantity of item active merchant has

### {{ renderMember(name='MinLuck') }} 

:   

### {{ renderMember(type='itemspell', name='Mount') }} 

:   Mount spell effect, if any.

### {{ renderMember(type='string', name='Name') }} 

:   Name

### {{ renderMember(name='NoDestroy') }} 

:   

### {{ renderMember(type='bool', name='NoDrop') }} 

:   No Trade?

### {{ renderMember(type='bool', name='NoRent') }} 

:   Temporary?

### {{ renderMember(name='NoTrade') }} 

:   Synonym for NoDrop

### {{ renderMember(name='Open') }} 

:   

### {{ renderMember(name='OrnamentationIcon') }} 

:   

### {{ renderMember(name='PctPower') }} 

:   

### {{ renderMember(name='PendingLore') }} 

:   

### {{ renderMember(type='int', name='Power') }} 

:   Power left on power source

### {{ renderMember(name='Prestige') }} 

:   

### {{ renderMember(type='itemspell', name='Proc') }} 

:   Combat proc effect.

### {{ renderMember(name='ProcRate') }} 

:   

### {{ renderMember(type='int', name='Purity') }} 

:   Purity of item

### {{ renderMember(name='Quality') }} 

:   

### {{ renderMember(name='Quest') }} 

:   

| [_string_](datatype-string.md) | **Race**[_N_] | Returns the _Nth_ long race name of the listed races on an item. Items suitable for ALL races will effectively have all 15 races listed. 
### {{ renderMember(type='int', name='Races') }} 

:   The number of races that can use the item. Items suitable for ALL races will return 15.

### {{ renderMember(name='Range') }} 

:   

### {{ renderMember(type='int', name='RecommendedLevel') }} 

:   Returns the Recommended Level of an item. Items with no recommended level will return 0.

### {{ renderMember(type='int', name='RequiredLevel') }} 

:   Returns the Required Level of an item. Items with no required level will return 0.

### {{ renderMember(type='itemspell', name='Scroll') }} 

:   Scroll effect, if any.

### {{ renderMember(type='int', name='SellPrice') }} 

:   Price to sell this item at this merchant

### {{ renderMember(type='int', name='Shielding') }} 

:   Shielding

### {{ renderMember(type='int', name='Size') }} 

:   Item size:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT

### {{ renderMember(type='int', name='SizeCapacity') }} 

:   If item is a container, size of items it can hold:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT

### {{ renderMember(name='Skill') }} 

:   

### {{ renderMember(name='SkillModMax') }} 

:   

### {{ renderMember(name='SkillModValue') }} 

:   

### {{ renderMember(name='SlotsUsedByItem') }} 

:   

### {{ renderMember(type='spell', name='Spell') }} 

:   Spell effect

### {{ renderMember(type='int', name='SpellDamage') }} 

:   Spell damage

### {{ renderMember(type='int', name='SpellShield') }} 

:   SpellShield

### {{ renderMember(type='int', name='STA') }} 

:   STA value on item

### {{ renderMember(type='int', name='Stack') }} 

:   Number of items in the stack

### {{ renderMember(type='bool', name='Stackable') }} 

:   Stackable?

### {{ renderMember(type='int', name='StackCount') }} 

:   The total number of the stackable item in your inventory

### {{ renderMember(type='int', name='Stacks') }} 

:   Number of stacks of the item in your inventory

### {{ renderMember(type='int', name='StackSize') }} 

:   Maximum number if items that can be in the stack

### {{ renderMember(type='int', name='STR') }} 

:   STR value on item

### {{ renderMember(type='int', name='StrikeThrough') }} 

:   StrikeThrough

### {{ renderMember(type='int', name='StunResist') }} 

:   Stun resist

### {{ renderMember(type='int', name='svCold') }} 

:   svCold value on item

### {{ renderMember(type='int', name='svCorruption') }} 

:   svCorruption value on item

### {{ renderMember(type='int', name='svDisease') }} 

:   svDisease value on item

### {{ renderMember(type='int', name='svFire') }} 

:   svFire value on item

### {{ renderMember(type='int', name='svMagic') }} 

:   svMagic value on item

### {{ renderMember(type='int', name='svPoison') }} 

:   svPoison value on item

### {{ renderMember(type='ticks', name='Timer') }} 

:   Returns the number of ticks remaining on an item recast timer

### {{ renderMember(type='int', name='TimerReady') }} 

:   Returns the number of seconds remaining on an item recast timer

### {{ renderMember(type='bool', name='Tradeskills') }} 

:   Tradeskills?

### {{ renderMember(type='int', name='Tribute') }} 

:   Tribute value of the item

### {{ renderMember(type='string', name='Type') }} 

:   Type

### {{ renderMember(type='int', name='Value') }} 

:   Item value in coppers

### {{ renderMember(type='int', name='Weight') }} 

:   Item weight

### {{ renderMember(name='WeightReduction') }} 

:   

### {{ renderMember(type='int', name='WIS') }} 

:   WIS value on item

### {{ renderMember(type='itemspell', name='Worn') }} 

:   Passive worn effect, if any.

| [_invslot_](datatype-invslot.md) | **WornSlot**[_N_] | The _Nth_ invslot this item can be worn in (fingers/ears count as 2 slots) 
### {{ renderMember(type='bool', name='WornSlot', params='name') }} 

:   Can item be worn in invslot with this _name_? (worn slots only)

### {{ renderMember(type='int', name='WornSlots') }} 

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
