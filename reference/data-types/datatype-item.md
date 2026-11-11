---
tags:
    - datatype
---
# `item` Type
<!--dt-desc-start-->
Contains the properties that describe an item.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int AC
AC value on item
///

/// member | int Accuracy
Accuracy
///

/// member | int AGI
AGI value on item
///

/// member | int Attack
Attack value on item
///

/// member | bool Attunable
Attunable?
///

/// member | int AugRestrictions
Augment Restrictions
///

/// member | int Augs
Number of augs on this item
///

/// member | augtype AugSlot
Retrieve the augment in the specified slot number.
///

/// member | int AugSlot1
Returns the type of agument in slot 1
///

/// member | int AugSlot2
Returns the type of agument in slot 2
///

/// member | int AugSlot3
Returns the type of agument in slot 3
///

/// member | int AugSlot4
Returns the type of agument in slot 4
///

/// member | int AugSlot5
Returns the type of agument in slot 5
///

/// member | int AugSlot6
Returns the type of agument in slot 6
///

/// member | int AugType
Augmentation slot type mask.
///

/// member | int Avoidance
Avoidance
///

/// member | BaneDMG
???
///

/// member | BaneDMGType
???
///

/// member | int64 BuyPrice
The cost to buy this item from active merchant
///

/// member | bool CanUse
TRUE if you can use the item, otherwise FALSE
///

/// member | float CastTime
Spell effect's cast time (in seconds)
///

/// member | int CHA
CHA value on item
///

/// member | int Charges
Charges
///

/// member | int Clairvoyance
Clairvoyance
///

/// member | string Class[N]
Returns the _Nth_ long class name of the listed classes on an item. Items suitable for ALL classes will effectively have all 17 classes listed.
///

/// member | int Classes
The number of classes that can use the item. Items suitable for ALL classes will return 16.
///

/// member | itemspell Clicky
Activatable spell effect, if any.
///

/// member | bool Collectible
TRUE if the item is a collectible, otherwise FALSE
///

/// member | Combinable
???
///

/// member | int CombatEffects
CombatEffects
///

/// member | int Container
Number of slots, if this is a container
///

/// member | int ContentSize
???
///

/// member | int Damage
Base Damage of the item
///

/// member | int DamageShieldMitigation
Damage Shield Mitigation
///

/// member | int DamShield
Damage Shield value on item
///

/// member | int Deities
The number of deities that can use the item. Items with no deity restrictions will return 0.
///

/// member | string Deity[N]
Returns the _Nth_ deity of the listed deities on an item. Items with no deity restrictions will return NULL for all values of _N_.
///

/// member | Delay
???
///

/// member | int DEX
DEX value on item
///

/// member | DMGBonus
???
///

/// member | string DMGBonusType
"None", "Magic", "Fire", "Cold", "Poison", "Disease"
///

/// member | int DoTShielding
DoT Shielding
///

/// member | string EffectType
Spell effect type ([see below](datatype-item.md#spell-effect-types) for spell effect types)
///

/// member | int Endurance
Endurance
///

/// member | int EnduranceRegen
Endurance regen
///

/// member | evolving Evolving
Does this item have Evolving experience on?
///

/// member | bool Expendable
???
///

/// member | itemspell Familiar
Familiar spell effect, if any.
///

/// member | int FirstFreeSlot
???
///

/// member | itemspell Focus
First focus effect, if any.
///

/// member | itemspell Focus2
Second focus effect, if any.
///

/// member | FocusID
???
///

/// member | int FreeStack
The number of items needed to fill all the stacks of the item you have (with a stacksize of 20).

If you have 3 stacks (1, 10, 20 in those stacks), you have room for 60 total and you have 31 on you, so **FreeStack** would return 29.
///

/// member | int Haste
Haste value on item
///

/// member | int HealAmount
HealAmount (regen?)
///

/// member | bool Heirloom
???
///

/// member | int HeroicAGI
Heroic AGI value on item
///

/// member | int HeroicCHA
Heroic CHA value on item
///

/// member | int HeroicDEX
Heroic DEX value on item
///

/// member | int HeroicINT
Heroic INT value on item
///

/// member | int HeroicSTA
Heroic STA value on item
///

/// member | int HeroicSTR
Heroic STR value on item
///

/// member | int HeroicSvCold
Heroic SvCold value on item
///

/// member | int HeroicSvCorruption
Heroic SvCorruption value on item
///

/// member | int HeroicSvDisease
Heroic SvDisease value on item
///

/// member | int HeroicSvFire
Heroic SvFire value on item
///

/// member | int HeroicSvMagic
Heroic SvMagic value on item
///

/// member | int HeroicSvPoison
Heroic SvPoison value on item
///

/// member | int HeroicWIS
Heroic WIS value on item
///

/// member | int HP
HP value on item
///

/// member | int HPRegen
HPRegen value on item
///

/// member | int Icon
Item Icon
///

/// member | int ID
Item ID
///

/// member | IDFile
???
///

/// member | IDFile2
???
///

/// member | itemspell Illusion
Illusion spell effect, if any.
///

/// member | float InstrumentMod
Instrument Modifier Value
///

/// member | InstrumentType
???
///

/// member | int INT
INT value on item
///

/// member | int InvSlot
Inventory Slot Number (Historic and now deprecated, use ItemSlot and ItemSlot2)
///

/// member | item Item[N]
Item in _Nth_ slot, if this is a container or has augs
///

/// member | float ItemDelay
Returns the delay of the weapon
///

/// member | string ItemLink[CLICKABLE]
just prints the actual hexlink for an item (not clickable) unless \[CLICKABLE] is included
///

/// member | int Items
Number of items, if this is a container.
///

/// member | int ItemSlot
Item Slot number see [Slot Names](../../reference/general/slot-names.md)
///

/// member | int ItemSlot2
Item Slot subnumber see [Slot Names](../../reference/general/slot-names.md)
///

/// member | LDoNCost
???
///

/// member | string LDoNTheme
"All", "Deepest Guk", "Miragul's", "Mistmoore", "Rujarkian", "Takish", "Unknown"
///

/// member | Level
???
///

/// member | Light
???
///

/// member | bool Lore
Lore?
///

/// member | bool LoreEquipped
Lore Equipped?
///

/// member | LoreText
???
///

/// member | int Luck
???
///

/// member | bool Magic
Magic?
///

/// member | int Mana
Mana value on item
///

/// member | int ManaRegen
ManaRegen value on item
///

/// member | int MaxLuck
???
///

/// member | int MaxPower
Max power on an power source
///

/// member | int MerchQuantity
Quantity of item active merchant has
///

/// member | int MinLuck
???
///

/// member | itemspell Mount
Mount spell effect, if any.
///

/// member | string Name
Name
///

/// member | bool NoDestroy
///

/// member | bool NoDrop
No Trade?
///

/// member | bool NoRent
Temporary?
///

/// member | bool NoTrade
Synonym for NoDrop
///

/// member | int Open
???
///

/// member | int OrnamentationIcon
???
///

/// member | float PctPower
???
///

/// member | PendingLore
???
///

/// member | int Power
Power left on power source
///

/// member | bool Prestige
Prestige item?
///

/// member | itemspell Proc
Combat proc effect.
///

/// member | ProcRate
???
///

/// member | int Purity
Purity of item
///

/// member | Quality
???
///

/// member | bool Quest
Quest item?
///

/// member | string Race[N]
Returns the _Nth_ long race name of the listed races on an item. Items suitable for all races will effectively have all 15 races listed.
///


/// member | int Races
The number of races that can use the item. Items suitable for ALL races will return 15.
///

/// member | int Range
???
///

/// member | int RecommendedLevel
Returns the Recommended Level of an item. Items with no recommended level will return 0.
///

/// member | int RefCount
???
///

/// member | int RequiredLevel
Returns the Required Level of an item. Items with no required level will return 0.
///

/// member | itemspell Scroll
Scroll effect, if any.
///

/// member | int SellPrice
Price to sell this item at this merchant
///

/// member | int Shielding
Shielding
///

/// member | int Size
Item size:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT
///

/// member | int SizeCapacity
If item is a container, size of items it can hold.

| Value | Meaning |
| 1 | SMALL |
| 2 | MEDIUM |
| 3 | LARGE |
| 4 | GIANT |
///

/// member | Skill
???
///

/// member | int SkillModMax
???
///

/// member | int SkillModValue
???
///

/// member | int SlotsUsedByItem
???
///

/// member | spell Spell
Spell effect
///

/// member | int SpellDamage
Spell damage
///

/// member | int SpellShield
SpellShield
///

/// member | int STA
STA value on item
///

/// member | int Stack
Number of items in the stack
///

/// member | bool Stackable
Stackable?
///

/// member | int StackCount
The total number of the stackable item in your inventory
///

/// member | int Stacks
Number of stacks of the item in your inventory
///

/// member | int StackSize
Maximum number if items that can be in the stack
///

/// member | int STR
STR value on item
///

/// member | int StrikeThrough
StrikeThrough
///

/// member | int StunResist
Stun resist
///

/// member | Summoned
???
///

/// member | int svCold
svCold value on item
///

/// member | int svCorruption
svCorruption value on item
///

/// member | int svDisease
svDisease value on item
///

/// member | int svFire
svFire value on item
///

/// member | int svMagic
svMagic value on item
///

/// member | int svPoison
svPoison value on item
///

/// member | ticks Timer
Returns the number of ticks remaining on an item recast timer
///

/// member | int TimerReady
Returns the number of seconds remaining on an item recast timer
///

/// member | bool Tradeskills
Tradeskills?
///

/// member | int Tribute
Tribute value of the item
///

/// member | string Type
Type
///

/// member | int Value
Item value in coppers
///

/// member | int Weight
Item weight
///

/// member | WeightReduction
???
///

/// member | int WIS
WIS value on item
///

/// member | itemspell Worn
Passive worn effect, if any.
///

/// member | invslot WornSlot[N]
The _Nth_ invslot this item can be worn in (fingers/ears count as 2 slots)
///

/// member | bool WornSlot[name]
Can item be worn in invslot with this _name_? (worn slots only)
///

/// member | int WornSlots
The number of invslots this item can be worn in (fingers/ears count as 2 slots)
///

### [string][string] `(To String)`

:   Same as **Name**

<!--dt-members-end-->

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

    This section needs to be moved to the ItemDisplay article

**${DisplayItem}** now takes an index as an option parameter index can be 0-5 you can still just do ${DsiplayItem} and it will just pick whatever you inspected last.

**Example:** /echo ${DisplayItem[5]}

* Info = 1,
* WindowTitle = 2,
* AdvancedLore = 3,
* MadeBy = 4,
* Information = 5,
* DisplayIndex = 6

**NOTE:** There is a difference between .Info and .Information .Info contains for example: .Info can return text like; this item is placable in yards, guild yards blah blah , This item can be used in tradeskills .Information can return text like Item Information: Placing this augment into blah blah, this armor can only be used in blah blah
<!--dt-linkrefs-start-->
[augtype]: datatype-augtype.md
[bool]: datatype-bool.md
[evolving]: datatype-evolving.md
[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[invslot]: datatype-invslot.md
[item]: datatype-item.md
[itemspell]: datatype-itemspell.md
[spell]: datatype-spell.md
[string]: datatype-string.md
[ticks]: datatype-ticks.md
<!--dt-linkrefs-end-->
