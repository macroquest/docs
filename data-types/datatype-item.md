## Description

Contains data about items

## Members

<table>
<tbody>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p><strong>Member</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AC</strong></p></td>
<td><p>AC value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AGI</strong></p></td>
<td><p>AGI value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Accuracy</strong></p></td>
<td><p>Accuracy</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Attack</strong></p></td>
<td><p>Attack value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Attuneable</strong></p></td>
<td><p>Attuneable?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugRestrictions</strong></p></td>
<td><p>Augment Restrictions</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Augs</strong></p></td>
<td><p>Number of augs on this item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugSlot1</strong></p></td>
<td><p>Aug slot 1</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugSlot2</strong></p></td>
<td><p>Aug slot 2</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugSlot3</strong></p></td>
<td><p>Aug slot 3</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugSlot4</strong></p></td>
<td><p>Aug slot 4</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugSlot5</strong></p></td>
<td><p>Aug slot 5</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AugType</strong></p></td>
<td><p>Augment Type</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Avoidance</strong></p></td>
<td><p>Avoidance</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>BuyPrice</strong></p></td>
<td><p>The cost to buy this item from active merchant</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>CastTime</strong></p></td>
<td><p>Spell effect's cast time (in seconds)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CHA</strong></p></td>
<td><p>CHA value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Charges</strong></p></td>
<td><p>Charges</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Clairvoyance</strong></p></td>
<td><p>Clairvoyance</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Class[</strong>#<strong>]</strong></p></td>
<td><p>Returns the #th long class name of the listed classes on an item. Items suitable for ALL classes will effectively have all 17 classes listed.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Classes</strong></p></td>
<td><p>The number of classes that can use the item. Items suitable for ALL classes will return 16.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CombatEffects</strong></p></td>
<td><p>CombatEffects</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Container</strong></p></td>
<td><p>Number of slots, if this is a container</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>DamageShieldMitigation</strong></p></td>
<td><p>Damage Shield Mitigation</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>DamShield</strong></p></td>
<td><p>Damage Shield value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Deity[</strong>#<strong>]</strong></p></td>
<td><p>Returns the #th deity of the listed deities on an item. Items with no deity restrictions will return NULL for all values of #.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Deities</strong></p></td>
<td><p>The number of deities that can use the item. Items with no deity restrictions will return 0.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>DEX</strong></p></td>
<td><p>DEX value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>DMGBonusType</strong></p></td>
<td><p>"None", "Magic", "Fire", "Cold", "Poison", "Disease"</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>DoTShielding</strong></p></td>
<td><p>DoT Shielding</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>EffectType</strong></p></td>
<td><p>Spell effect type (see below for spell effect types)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Endurance</strong></p></td>
<td><p>Endurance</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>EnduranceRegen</strong></p></td>
<td><p>Endurance regen</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-evolving.md">evolving</a></em></p></td>
<td><p><strong>Evolving</strong></p></td>
<td><p>Does this item have Evolving experience on?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>FreeStack</strong></p></td>
<td><p>The number of items needed to fill all the stacks of the item you have (with a stacksize of 20).<br />
If you have 3 stacks (1, 10, 20 in those stacks), you have room for 60 total and you have 31 on you, so <strong>FreeStack</strong> would return 29.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Haste</strong></p></td>
<td><p>Haste value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HealAmount</strong></p></td>
<td><p>HealAmount (regen?)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicAGI</strong></p></td>
<td><p>Heroic AGI value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicCHA</strong></p></td>
<td><p>Heroic CHA value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicDEX</strong></p></td>
<td><p>Heroic DEX value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicINT</strong></p></td>
<td><p>Heroic INT value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSTA</strong></p></td>
<td><p>Heroic STA value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSTR</strong></p></td>
<td><p>Heroic STR value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSvCold</strong></p></td>
<td><p>Heroic SvCold value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSvCorruption</strong></p></td>
<td><p>Heroic SvCorruption value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSvDisease</strong></p></td>
<td><p>Heroic SvDisease value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSvFire</strong></p></td>
<td><p>Heroic SvFire value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSvMagic</strong></p></td>
<td><p>Heroic SvMagic value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicSvPoison</strong></p></td>
<td><p>Heroic SvPoison value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HeroicWIS</strong></p></td>
<td><p>Heroic WIS value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HP</strong></p></td>
<td><p>HP value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>HPRegen</strong></p></td>
<td><p>HPRegen value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Icon</strong></p></td>
<td><p>Item Icon</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>ID</strong></p></td>
<td><p>Item ID</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>InstrumentMod</strong></p></td>
<td><p>Instrument Modifier Value</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>INT</strong></p></td>
<td><p>INT value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>InvSlot</strong></p></td>
<td><p>Inventory Slot Number (Historic and now deprecated, use ItemSlot and ItemSlot2)</p></td>
</tr>
<tr class="odd">
<td><p><em>item</em></p></td>
<td><p><strong>Item[</strong>#<strong>]</strong></p></td>
<td><p>Item in #th slot, if this is a container or has augs</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>ItemDelay</strong></p></td>
<td><p>Returns the delay of the weapon</p></td>
</tr>
<tr class="odd">
<td><p><em>item</em></p></td>
<td><p><strong>ItemLink[CLICKABLE]</strong></p></td>
<td><p>just prints the actual hexlink for an item (not clickable) unless [CLICKABLE] is included</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Items</strong></p></td>
<td><p>Number of items, if this is a container.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>ItemSlot</strong></p></td>
<td><p>Item Slot number see <a href="../general-information/slot-names.md">Slot Names</a></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>ItemSlot2</strong></p></td>
<td><p>Item Slot subnumber see <a href="../general-information/slot-names.md">Slot Names</a></p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>LDoNTheme</strong></p></td>
<td><p>"All", "Deepest Guk", "Miragul's", "Mistmoore", "Rujarkian", "Takish", "Unknown"</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Lore</strong></p></td>
<td><p>Lore?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Magic</strong></p></td>
<td><p>Magic?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Mana</strong></p></td>
<td><p>Mana value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>ManaRegen</strong></p></td>
<td><p>ManaRegen value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>MaxPower</strong></p></td>
<td><p>Max power on an power source</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>MerchQuantity</strong></p></td>
<td><p>Quantity of item active merchant has</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Name</strong></p></td>
<td><p>Name</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>NoDrop</strong></p></td>
<td><p>No Trade?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>NoRent</strong></p></td>
<td><p>Temporary?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Power</strong></p></td>
<td><p>Power left on power source</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Purity</strong></p></td>
<td><p>Purity of item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Race[</strong>#<strong>]</strong></p></td>
<td><p>Returns the #th long race name of the listed races on an item. Items suitable for ALL races will effectively have all 15 races listed.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Races</strong></p></td>
<td><p>The number of races that can use the item. Items suitable for ALL races will return 15.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>RequiredLevel</strong></p></td>
<td><p>Returns the Required Level of an item. Items with no required level will return 0.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>SellPrice</strong></p></td>
<td><p>Price to sell this item at this merchant</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Shielding</strong></p></td>
<td><p>Shielding</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Size</strong></p></td>
<td><p>Item size:<br />
1 SMALL<br />
2 MEDIUM<br />
3 LARGE<br />
4 GIANT</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>SizeCapacity</strong></p></td>
<td><p>If item is a container, size of items it can hold:<br />
1 SMALL<br />
2 MEDIUM<br />
3 LARGE<br />
4 GIANT</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-spell.md">spell</a></em></p></td>
<td><p><strong>Spell</strong></p></td>
<td><p>Spell effect</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>SpellDamage</strong></p></td>
<td><p>Spell damage</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>SpellShield</strong></p></td>
<td><p>SpellShield</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>STA</strong></p></td>
<td><p>STA value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Stack</strong></p></td>
<td><p>Number of items in the stack</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Stacks</strong></p></td>
<td><p>Number of stacks of the item in your inventory</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Stackable</strong></p></td>
<td><p>Stackable?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>StackCount</strong></p></td>
<td><p>The total number of the stackable item in your inventory</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>StackSize</strong></p></td>
<td><p>Maximum number if items that can be in the stack</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>STR</strong></p></td>
<td><p>STR value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>StrikeThrough</strong></p></td>
<td><p>StrikeThrough</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>StunResist</strong></p></td>
<td><p>Stun resist</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>svCold</strong></p></td>
<td><p>svCold value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>svCorruption</strong></p></td>
<td><p>svCorruption value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>svDisease</strong></p></td>
<td><p>svDisease value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>svFire</strong></p></td>
<td><p>svFire value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>svMagic</strong></p></td>
<td><p>svMagic value on item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>svPoison</strong></p></td>
<td><p>svPoison value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-ticks.md">ticks</a></em></p></td>
<td><p><strong>Timer</strong></p></td>
<td><p>Returns the number of ticks remaining on an item recast timer</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>TimerReady</strong></p></td>
<td><p>Returns the number of seconds remaining on an item recast timer</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Tradeskills</strong></p></td>
<td><p>Tradeskills?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Type</strong></p></td>
<td><p>Type</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Tribute</strong></p></td>
<td><p>Tribute value of the item</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Value</strong></p></td>
<td><p>Item value in coppers</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Weight</strong></p></td>
<td><p>Item weight</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>WIS</strong></p></td>
<td><p>WIS value on item</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-invslot.md">invslot</a></em></p></td>
<td><p><strong>WornSlot[</strong>#<strong>]</strong></p></td>
<td><p>The #th invslot this item can be worn in (fingers/ears count as 2 slots)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>WornSlot[</strong>name<strong>]</strong></p></td>
<td><p>Can item be worn in invslot with this <em>name</em>? (worn slots only)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>WornSlots</strong></p></td>
<td><p>The number of invslots this item can be worn in (fingers/ears count as 2 slots)</p></td>
</tr>
<tr class="odd">
<td><p>'<strong>'<a href="datatype-string.md">string</a></strong></p></td>
<td><p><strong>To String</strong></p></td>
<td><p>Same as <strong>Name</strong></p></td>
</tr>
</tbody>
</table>

## Spell Effect Types

*EffectType* will return one of the following:

-   **Click Inventory** - item has a right-click spell and can be cast from inventory
-   **Click Unknown** - item has an unknown right-click effect restriction
-   **Click Worn** - item has a right-click spell and must be equipped to click it
-   **Combat** - weapon has a proc
-   **Spell Scroll** - Scribeable spell scroll
-   **Worn** - item has a focus effect

## DisplayItem Index

**${DisplayItem}** now takes an index as an option parameter index can be 0-5 you can still just do ${DsiplayItem} and
it will just pick whatever you inspected last.

**Example:** /echo ${DisplayItem\[5\]}

-   Info = 1,
-   WindowTitle = 2,
-   AdvancedLore = 3,
-   MadeBy = 4,
-   Information = 5,
-   DisplayIndex = 6

**NOTE** There is a difference between .Info and .Information .Info contains for example: .Info can return text like;
this item is placable in yards, guild yards blah blah , This item can be used in tradeskills .Information can return
text like Item Information: Placing this augment into blah blah, this armor can only be used in blah blah

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:FindItem](../top-level-objects/tlo-finditem.md)
-   [TLO:FindItemBank](../top-level-objects/tlo-finditembank.md)
-   [TLO:DisplayItem](../top-level-objects/tlo-displayitem.md)
-   [DataType:invslot](datatype-invslot.md)
-   [DataType:character](datatype-character.md)
-   [DataType:corpse](datatype-corpse.md)


