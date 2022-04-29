# DataType:item

Contains data about items

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **AC** | AC value on item |
| [_int_](datatype-int.md) | **AGI** | AGI value on item |
| [_int_](datatype-int.md) | **Accuracy** | Accuracy |
| [_int_](datatype-int.md) | **Attack** | Attack value on item |
| [_bool_](datatype-bool.md) | **Attuneable** | Attuneable? |
| [_int_](datatype-int.md) | **AugRestrictions** | Augment Restrictions |
| [_int_](datatype-int.md) | **Augs** | Number of augs on this item |
| [_int_](datatype-int.md) | **AugSlot1** | Aug slot 1 |
| [_int_](datatype-int.md) | **AugSlot2** | Aug slot 2 |
| [_int_](datatype-int.md) | **AugSlot3** | Aug slot 3 |
| [_int_](datatype-int.md) | **AugSlot4** | Aug slot 4 |
| [_int_](datatype-int.md) | **AugSlot5** | Aug slot 5 |
| [_int_](datatype-int.md) | **AugType** | Augment Type |
| [_int_](datatype-int.md) | **Avoidance** | Avoidance |
| [_int_](datatype-int.md) | **BuyPrice** | The cost to buy this item from active merchant |
| [_float_](datatype-float.md) | **CastTime** | Spell effect's cast time (in seconds) |
| [_int_](datatype-int.md) | **CHA** | CHA value on item |
| [_int_](datatype-int.md) | **Charges** | Charges |
| [_int_](datatype-int.md) | **Clairvoyance** | Clairvoyance |
| \_\_[_string_](datatype-string.md)\_\_ | **Class[**\#**]** | Returns the \#th long class name of the listed classes on an item. Items suitable for ALL classes will effectively have all 17 classes listed. |
| [_int_](datatype-int.md) | **Classes** | The number of classes that can use the item. Items suitable for ALL classes will return 16. |
| [_int_](datatype-int.md) | **CombatEffects** | CombatEffects |
| [_int_](datatype-int.md) | **Container** | Number of slots, if this is a container |
| [_int_](datatype-int.md) | **DamageShieldMitigation** | Damage Shield Mitigation |
| [_int_](datatype-int.md) | **DamShield** | Damage Shield value on item |
| [_string_](datatype-string.md)\_\_ | **Deity[**\#**]** | Returns the \#th deity of the listed deities on an item. Items with no deity restrictions will return NULL for all values of \#. |
| [_int_](datatype-int.md) | **Deities** | The number of deities that can use the item. Items with no deity restrictions will return 0. |
| [_int_](datatype-int.md) | **DEX** | DEX value on item |
| [_string_](datatype-string.md)\_\_ | **DMGBonusType** | "None", "Magic", "Fire", "Cold", "Poison", "Disease" |
| [_int_](datatype-int.md) | **DoTShielding** | DoT Shielding |
| [_string_](datatype-string.md)\_\_ | **EffectType** | Spell effect type (see below for spell effect types) |
| [_int_](datatype-int.md) | **Endurance** | Endurance |
| [_int_](datatype-int.md) | **EnduranceRegen** | Endurance regen |
| [_evolving_](datatype-evolving.md) | **Evolving** | Does this item have Evolving experience on? |
| [_int_](datatype-int.md) | **FreeStack** | The number of items needed to fill all the stacks of the item you have (with a stacksize of 20\).  If you have 3 stacks \(1, 10, 20 in those stacks), you have room for 60 total and you have 31 on you, so **FreeStack** would return 29. |
| [_int_](datatype-int.md) | **Haste** | Haste value on item |
| [_int_](datatype-int.md) | **HealAmount** | HealAmount (regen?) |
| [_int_](datatype-int.md) | **HeroicAGI** | Heroic AGI value on item |
| [_int_](datatype-int.md) | **HeroicCHA** | Heroic CHA value on item |
| [_int_](datatype-int.md) | **HeroicDEX** | Heroic DEX value on item |
| [_int_](datatype-int.md) | **HeroicINT** | Heroic INT value on item |
| [_int_](datatype-int.md) | **HeroicSTA** | Heroic STA value on item |
| [_int_](datatype-int.md) | **HeroicSTR** | Heroic STR value on item |
| [_int_](datatype-int.md) | **HeroicSvCold** | Heroic SvCold value on item |
| [_int_](datatype-int.md) | **HeroicSvCorruption** | Heroic SvCorruption value on item |
| [_int_](datatype-int.md) | **HeroicSvDisease** | Heroic SvDisease value on item |
| [_int_](datatype-int.md) | **HeroicSvFire** | Heroic SvFire value on item |
| [_int_](datatype-int.md) | **HeroicSvMagic** | Heroic SvMagic value on item |
| [_int_](datatype-int.md) | **HeroicSvPoison** | Heroic SvPoison value on item |
| [_int_](datatype-int.md) | **HeroicWIS** | Heroic WIS value on item |
| [_int_](datatype-int.md) | **HP** | HP value on item |
| [_int_](datatype-int.md) | **HPRegen** | HPRegen value on item |
| [_int_](datatype-int.md) | **Icon** | Item Icon |
| [_int_](datatype-int.md) | **ID** | Item ID |
| [_float_](datatype-float.md) | **InstrumentMod** | Instrument Modifier Value |
| [_int_](datatype-int.md) | **INT** | INT value on item |
| [_int_](datatype-int.md) | **InvSlot** | Inventory Slot Number (Historic and now deprecated, use ItemSlot and ItemSlot2) |
| _item_ | **Item[**\#**]** | Item in \#th slot, if this is a container or has augs |
| [_float_](datatype-float.md) | **ItemDelay** | Returns the delay of the weapon |
| \_\_[_string_](datatype-string.md)\_\_ | **ItemLink[CLICKABLE\]** | just prints the actual hexlink for an item (not clickable) unless \[CLICKABLE] is included |
| [_int_](datatype-int.md) | **Items** | Number of items, if this is a container. |
| [_int_](datatype-int.md) | **ItemSlot** | Item Slot number see [Slot Names](../../general-information/slot-names.md) |
| [_int_](datatype-int.md) | **ItemSlot2** | Item Slot subnumber see [Slot Names](../../general-information/slot-names.md) |
| [_string_](datatype-string.md)\_\_ | **LDoNTheme** | "All", "Deepest Guk", "Miragul's", "Mistmoore", "Rujarkian", "Takish", "Unknown" |
| [_bool_](datatype-bool.md) | **Lore** | Lore? |
| [_bool_](datatype-bool.md) | **Magic** | Magic? |
| [_int_](datatype-int.md) | **Mana** | Mana value on item |
| [_int_](datatype-int.md) | **ManaRegen** | ManaRegen value on item |
| [_int_](datatype-int.md) | **MaxPower** | Max power on an power source |
| [_int_](datatype-int.md) | **MerchQuantity** | Quantity of item active merchant has |
| [_string_](datatype-string.md)\_\_ | **Name** | Name |
| [_bool_](datatype-bool.md) | **NoDrop** | No Trade? |
| [_bool_](datatype-bool.md) | **NoRent** | Temporary? |
| [_int_](datatype-int.md) | **Power** | Power left on power source |
| [_int_](datatype-int.md) | **Purity** | Purity of item |
| [_string_](datatype-string.md)\_\_ | **Race[**\#**]** | Returns the \#th long race name of the listed races on an item. Items suitable for ALL races will effectively have all 15 races listed. |
| [_int_](datatype-int.md) | **Races** | The number of races that can use the item. Items suitable for ALL races will return 15. |
| [_int_](datatype-int.md) | **RequiredLevel** | Returns the Required Level of an item. Items with no required level will return 0. |
| [_int_](datatype-int.md) | **SellPrice** | Price to sell this item at this merchant |
| [_int_](datatype-int.md) | **Shielding** | Shielding |
| [_int_](datatype-int.md) | **Size** | Item size:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT |
| [_int_](datatype-int.md) | **SizeCapacity** | If item is a container, size of items it can hold:  1 SMALL  2 MEDIUM  3 LARGE  4 GIANT |
| [_spell_](datatype-spell.md) | **Spell** | Spell effect |
| [_int_](datatype-int.md) | **SpellDamage** | Spell damage |
| [_int_](datatype-int.md) | **SpellShield** | SpellShield |
| [_int_](datatype-int.md) | **STA** | STA value on item |
| [_int_](datatype-int.md) | **Stack** | Number of items in the stack |
| [_int_](datatype-int.md) | **Stacks** | Number of stacks of the item in your inventory |
| [_bool_](datatype-bool.md) | **Stackable** | Stackable? |
| [_int_](datatype-int.md) | **StackCount** | The total number of the stackable item in your inventory |
| [_int_](datatype-int.md) | **StackSize** | Maximum number if items that can be in the stack |
| [_int_](datatype-int.md) | **STR** | STR value on item |
| [_int_](datatype-int.md) | **StrikeThrough** | StrikeThrough |
| [_int_](datatype-int.md) | **StunResist** | Stun resist |
| [_int_](datatype-int.md) | **svCold** | svCold value on item |
| [_int_](datatype-int.md) | **svCorruption** | svCorruption value on item |
| [_int_](datatype-int.md) | **svDisease** | svDisease value on item |
| [_int_](datatype-int.md) | **svFire** | svFire value on item |
| [_int_](datatype-int.md) | **svMagic** | svMagic value on item |
| [_int_](datatype-int.md) | **svPoison** | svPoison value on item |
| [_ticks_](datatype-ticks.md) | **Timer** | Returns the number of ticks remaining on an item recast timer |
| [_int_](datatype-int.md) | **TimerReady** | Returns the number of seconds remaining on an item recast timer |
| [_bool_](datatype-bool.md) | **Tradeskills** | Tradeskills? |
| [_string_](datatype-string.md)\_\_ | **Type** | Type |
| [_int_](datatype-int.md) | **Tribute** | Tribute value of the item |
| [_int_](datatype-int.md) | **Value** | Item value in coppers |
| [_int_](datatype-int.md) | **Weight** | Item weight |
| [_int_](datatype-int.md) | **WIS** | WIS value on item |
| [_invslot_](datatype-invslot.md) | **WornSlot[**\#**]** | The \#th invslot this item can be worn in (fingers/ears count as 2 slots) |
| [_bool_](datatype-bool.md) | **WornSlot[**name**]** | Can item be worn in invslot with this _name_? (worn slots only) |
| [_int_](datatype-int.md) | **WornSlots** | The number of invslots this item can be worn in (fingers/ears count as 2 slots) |
| [_string_](datatype-string.md)\_\_ | **To String** | Same as **Name** |

## Spell Effect Types

_EffectType_ will return one of the following:

* **Click Inventory** - item has a right-click spell and can be cast from inventory
* **Click Unknown** - item has an unknown right-click effect restriction
* **Click Worn** - item has a right-click spell and must be equipped to click it
* **Combat** - weapon has a proc
* **Spell Scroll** - Scribeable spell scroll
* **Worn** - item has a focus effect

| :warning: WARNING                                                 |
|-------------------------------------------------------------------|
| This next section needs to be moved to the MQ2ItemDisplay article |

## DisplayItem Index

**${DisplayItem}** now takes an index as an option parameter index can be 0-5 you can still just do ${DsiplayItem} and it will just pick whatever you inspected last.

**Example:** /echo ${DisplayItem[5]}

* Info = 1,
* WindowTitle = 2,
* AdvancedLore = 3,
* MadeBy = 4,
* Information = 5,
* DisplayIndex = 6

**NOTE:** There is a difference between .Info and .Information .Info contains for example: .Info can return text like; this item is placable in yards, guild yards blah blah , This item can be used in tradeskills .Information can return text like Item Information: Placing this augment into blah blah, this armor can only be used in blah blah

