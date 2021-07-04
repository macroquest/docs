# DataType:character

## Description

This data type contains all the information about _your_ character.

Inherits [_spawn_](datatype-spawn.md).

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_int_](datatype-int.md) | **AAExp** | AA exp as a raw number out of 10,000 \(10,000=100%\) |
| [_int_](datatype-int.md) | **AAPoints** | Unused AA points |
| [_int_](datatype-int.md) | **AAPointsSpent** | The number of points you have spent on AA abilities |
| [_int_](datatype-int.md) | **AAPointsTotal** | The total number of AA points you have |
| [_int_](datatype-int.md) | **AAVitality** | The total number of AA Vitality you have |
| [_string_](datatype-string.md) | **Ability\[**name**\]** | Skill name assigned to this doability button |
| [_int_](datatype-int.md) | **Ability\[**\#**\]** | The doability button number that the skill _name_ is on |
| [_bool_](datatype-bool.md) | **AbilityReady\[**\#\|name**\]** | Ability with this _name_ or on this button _\#_ ready? |
| [_int_](datatype-int.md) | **AccuracyBonus** | Accuracy bonus from gear and spells |
| [_spell_](datatype-spell.md) | **ActiveDisc** | Returns a spell if melee discipline is active. |
| [_int_](datatype-int.md) | **ActiveFavorCost** | If Tribute is active, how much it is costing you every 10 minutes. Returns NULL if tribute is inactive. |
| [_altability_](datatype-altability.md) | **AltAbility\[**\#\|name**\]** | Returns the total number of points you have spent in ability \# or _name_ |
| [_bool_](datatype-bool.md) | **AltAbilityReady\[**\#\|name**\]** | Alt ability _\#_ or _name_ ready? |
| [_int_](datatype-int.md) | **AltAbilityTimer\[**\#\|name**\]** | Alt ability reuse time remaining \(in ticks\) for ability _\#_ or _name_ |
| [_bool_](datatype-bool.md) | **AltTimerReady** | Alternate timer ready? \(Bash/Slam/Frenzy/Backstab\). **Note: ${AbilityReady} works fine with most of these.** |
| [_int_](datatype-int.md) | **AGI** | Character Agility |
| [_spawn_](datatype-spawn.md) | **AggroLock** | spawn info for aggro lock player |
| [_bool_](datatype-bool.md) | **AmIGroupLeader** | Am I the group leader? |
| [_bool_](datatype-bool.md) | **AssistComplete** | returns true/false if the assist is complete |
| [_int_](datatype-int.md) | **AttackBonus** | Attack bonus from gear and spells |
| [_int_](datatype-int.md) | **AttackSpeed** | Your Attack Speed. No haste spells/items = AttackSpeed of 100. A 41% haste item will result in an AttackSpeed of 141. This variable does not take into account spell or song haste. |
| [_string_](datatype-string.md) | **Aura** | The aura effect name |
| [_bool_](datatype-bool.md) | **AutoFire** | Is Autofire on? |
| [_int_](datatype-int.md) | **AvoidanceBonus** | Avoidance bonus from gear/spells |
| [_item_](datatype-item.md) | **Bank\[**\#**\]** | Item in this bankslot \# |
| [_bool_](datatype-bool.md) | **BardSongPlaying** | Is a bard song playing? |
| [_int_](datatype-int.md) | **Book\[**name**\]** | Slot in your spellbook assigned to spell _name_. |
| [_spell_](datatype-spell.md) | **Book\[**\#**\]** | Spell assigned to this slot \# in your spellbook |
| [_buff_](datatype-buff.md) | **Buff\[**name**\]** | The buff with this name |
| [_buff_](datatype-buff.md) | **Buff\[**\#**\]** | The buff in this slot \# |
| [_bool_](datatype-bool.md) | '''Buyer | if you are an active buyer |
| [_bool_](datatype-bool.md) | '''CanMount | for some indoor zones that where not flagged as nomount and added bazaar, nexus to zones where its ok to mount. |
| [_int_](datatype-int.md) | **CareerFavor** | Career favor/tribute |
| [_int_](datatype-int.md) | **Cash** | Total cash on your character, expressed in coppers \(eg. if you are carrying 100pp, **Cash** will return 100000\) |
| [_int_](datatype-int.md) | **CashBank** | Total cash in your bank, expressed in coppers |
| [_int_](datatype-int.md) | **CHA** | Character Charisma |
| [_int_](datatype-int.md) | **Chronobines** | Chronobines on your character |
| [_int_](datatype-int.md) | **ClairvoyanceBonus** | Clairvoyance Bonus |
| [_bool_](datatype-bool.md) | **Combat** | In combat? |
| [_spell_](datatype-spell.md) | **CombatAbility\[**\#**\]** | The name of Combat Ability \# in your list \(not the same as anyone else's list!\) |
| [_int_](datatype-int.md) | **CombatAbility\[**name**\]** | The number of Combat ability _name_ in your list \(not the same as anyone else's list!\) |
| [_bool_](datatype-bool.md) | **CombatAbilityReady\[**name\|\#\]''' | Is this Combat Ability ready? |
| [_int_](datatype-int.md) | **CombatAbilityTimer\[**name\|\#**\]** | The time remaining \(in seconds\) before the Combat Ability _name_ is usable |
| [_int_](datatype-int.md) | **CombatEffectsBonus** | Combat Effects bonus from gear and spells |
| [_string_](datatype-string.md) | **CombatState** | Returns one of the following: COMBAT, DEBUFFED, COOLDOWN, ACTIVE, RESTING, UNKNOWN |
| [_int_](datatype-int.md) | **Copper** | Copper on your character |
| [_int_](datatype-int.md) | **CopperBank** | Copper in bank |
| [_spell_](datatype-spell.md) | **Corrupted** | Returns the name of the Corrupted debuff if you have one |
| [_int_](datatype-int.md) | **CountBuffs** | Number of buffs you have, not including short duration buffs |
| [_int_](datatype-int.md) | **CountersCurse** | Number of curse counters you have |
| [_int_](datatype-int.md) | **CountersDisease** | Number of disease counters you have |
| [_int_](datatype-int.md) | **CountersPoison** | Number of poison counters you have |
| [_int_](datatype-int.md) | **CountSongs** | Number of songs you have |
| [_int_](datatype-int.md) | **Counters** | Damage Absorption Counters Remaining |
| [_int_](datatype-int.md) | **CurrentEndurance** | Current endurance |
| [_int_](datatype-int.md) | **CurrentFavor** | Current favor/tribute |
| [_int_](datatype-int.md) | **CurrentHPs** | Current hit points |
| [_int_](datatype-int.md) | **CurrentMana** | Current mana |
| [_int_](datatype-int.md) | **CurrentWeight** | Current weight |
| [_spell_](datatype-spell.md) | **Cursed** | Returns the name of the Curse debuff if you are effected by one |
| [_int_](datatype-int.md) | **DamageShieldBonus** | Damage Shield bonus from gear and spells |
| [_int_](datatype-int.md) | **DamageShieldMitigationBonus** | Damage Shield Mitigation bonus from gear and spells |
| [_int_](datatype-int.md) | **Dar** | Damage absorption remaining \(eg. from Rune-type spells\) |
| [_string_](datatype-string.md) | **Diseased** | Returns the name of any Disease spell |
| [_int_](datatype-int.md) | **DEX** | Character Dexterity |
| [_string_](datatype-string.md) | **Dotted** | Returns name of first DoT on character. |
| [_int_](datatype-int.md) | **DoTShieldBonus** | DoT Shield bonus from gear and spells |
| [_int_](datatype-int.md) | **Doubloons** | Doubloons on your character |
| [_ticks_](datatype-ticks.md) | **Downtime** | Downtime \(Ticks left til combat timer end\) |
| [_int_](datatype-int.md) | **Drunk** | Drunkenness level |
| [_int_](datatype-int.md) | **EbonCrystals** | Number of Ebon Crystals on your character |
| [_int_](datatype-int.md) | **EnduranceBonus** | Endurance bonus from gear and spells |
| [_int_](datatype-int.md) | **EnduranceRegen** | Endurance regen from the last tick |
| [_int_](datatype-int.md) | **EnduranceRegenBonus** | Endurance regen bonus |
| [_int_](datatype-int.md) | **Exp** | Experience \(out of 10,000\) |
| [_int_](datatype-int.md) | **ExpansionFlags** | Returns a numeric number representing which expansions your toon is flagged for |
| [_int_](datatype-int.md) | **Faycites** | Faycites on your character |
| [_fellowship_](datatype-fellowship.md) | **Fellowship** | Info about Fellowship |
| [_int_](datatype-int.md) | **FreeBuffSlots** | Number of open buff slots \(not counting the short duration buff slots\) |
| [_int_](datatype-int.md) | **FreeInventory** | Number of free inventory spaces |
| [_int_](datatype-int.md) | **FreeInventory\[\#\]** | Number of free inventory spaces of at least \# size \(giant=4\) |
| [_int_](datatype-int.md) | **Gem\[**name**\]** | Returns the slot \# with the spell _name_ |
| [_spell_](datatype-spell.md) | **Gem\[**\#**\]** | The name of the spell in this slot \# |
| [_ticks_](datatype-ticks.md) | **GemTimer\[**name\|\#**\]** | The timer for the spell with this _name_ or in this gem _\#_ |
| [_int_](datatype-int.md) | **Gold** | Gold on character |
| [_int_](datatype-int.md) | **GoldBank** | Gold in bank |
| [_spawn_](datatype-spawn.md) | **GroupAssistTarget** | Current group assist target |
| [_bool_](datatype-bool.md) | **Grouped** | Grouped? |
| [_int_](datatype-int.md) | **GroupLeaderExp** | Group leadership experience \(out of 330\) |
| [_int_](datatype-int.md) | **GroupLeaderPoints** | Group leadership points |
| [_string_](datatype-string.md) | **GroupList** | Returns a string of your group members \(excluding you\) |
| [_spawn_](datatype-spawn.md) | **GroupMarkNPC\[**\#**\]** | Current group marked NPC \(1-3\) |
| [_int_](datatype-int.md) | **GroupSize** | Size of group |
| [_int_](datatype-int.md) | **GukEarned** | Total LDoN points earned in Deepest Guk |
| [_int_](datatype-int.md) | **GuildID** | Returns the ID number of your guild |
| [_bool_](datatype-bool.md) | **HaveExpansion\[**\#**\]** | Returns TRUE/FALSE if you have that expansion \# |
| [_int_](datatype-int.md) | **Haste** | Total Combined Haste \(worn and spell\) as shown in Inventory Window stats |
| [_int_](datatype-int.md) | **HealAmountBonus** | Total Heal Amount bonus from gear |
| [_int_](datatype-int.md) | **HeroicAGIBonus** | Total Heroic Agility bonus from gear |
| [_int_](datatype-int.md) | **HeroicCHABonus** | Total Heroic Charisma bonus from gear |
| [_int_](datatype-int.md) | **HeroicDEXBonus** | Total Heroic Dexterity bonus from gear |
| [_int_](datatype-int.md) | **HeroicINTBonus** | Total Heroic Intelligence bonus from gear |
| [_int_](datatype-int.md) | **HeroicSTABonus** | Total Heroic Stamina bonus from gear |
| [_int_](datatype-int.md) | **HeroicSTRBonus** | Total Heroic Strength bonus from gear |
| [_int_](datatype-int.md) | **HeroicWISBonus** | Total Heroic Wisdom bonus from gear |
| [_int_](datatype-int.md) | **HPBonus** | Hit point bonus from gear and spells |
| [_int_](datatype-int.md) | **HPRegen** | Hit point regeneration from last tick |
| [_int_](datatype-int.md) | **HPRegenBonus** | HP regen bonus from gear and spells |
| [_int_](datatype-int.md) | **Hunger** | Hunger level |
| [_int_](datatype-int.md) | **ID** | Spawn ID |
| [_bool_](datatype-bool.md) | **InInstance** | Returns TRUE/FALSE if you are in an instance. |
| [_int_](datatype-int.md) | **INT** | Character Intelligence |
| [_item_](datatype-item.md) | **Inventory\[**\#**\]** | Item in this slot \# |
| [_item_](datatype-item.md) | **Inventory\[**slotname**\]** | Item in this _slotname_ \(inventory slots only\). See [Slot Names](../../general-information/slot-names.md) for a list of _slotnames_. |
| [_string_](datatype-string.md) | **Invulnerable** | Returns the invulnerable spell name on you, can be used with spell data type ex. ${Me.Invulnerable.Spell.ID} |
| [_bool_](datatype-bool.md) | **ItemReady\[XXX\]** | True/False on if the item is ready to cast. |
| [_int_](datatype-int.md) | **LADelegateMA** | Level of Delegate MA of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LADelegateMarkNPC** | Level of Delegate Mark NPC of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAFindPathPC** | Level of Find Path PC of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAHealthEnhancement** | Level of Health Enhancement of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAHealthRegen** | Level of Health Regen of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAHoTT** | Level of HoTT of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAInspectBuffs** | Level of Inspect Buffs of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAManaEnhancement** | Level of Mana Enhancement of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAMarkNPC** | Level of Mark NPC of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LANPCHealth** | Level of NPC Health of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LAOffenseEnhancement** | Level of Offense Enhancement of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **LASpellAwareness** | Level of Spell Awareness of the current group leader \(not your own ability level\) |
| [_int_](datatype-int.md) | **Language\[**language name**\]** | The EQ language number of the specified language. See below for language/number table. |
| [_string_](datatype-string.md) | **Language\[**language number**\]** | Returns the EQ language name of the _language number_ specified. See below for language/number table. |
| [_int_](datatype-int.md) | **LanguageSkill\[**language**\]** | Your skill in _language_ |
| [_int_](datatype-int.md) | **LargestFreeInventory** | Size of your largest free inventory space |
| [_int_](datatype-int.md) | **LargestFreeInventory** | Size of your largest free inventory space |
| [_timestamp_](datatype-timestamp.md) | **LastZoned** | Returns a timestamp of last time you zoned |
| [_int_](datatype-int.md) | **LDoNPoints** | Available LDoN points |
| [_int_](datatype-int.md) | **Level** | Character Level |
| [_int_](datatype-int.md) | **ManaBonus** | Mana bonus from gear and spells |
| [_int_](datatype-int.md) | **ManaRegen** | Mana regeneration from last tick |
| [_int_](datatype-int.md) | **ManaRegenBonus** | Mana regen bonus from gear and spells |
| [_int_](datatype-int.md) | **MaxBuffSlots** | Max number of buffs you can have on you. /echo ${Me.MaxBuffSlots} |
| [_int_](datatype-int.md) | **MaxEndurance** | Max endurance |
| [_int_](datatype-int.md) | **MaxHPs** | Max hit points |
| [_int_](datatype-int.md) | **MaxMana** | Max mana |
| [_string_](datatype-string.md) | **Mercenary** | The state of your Mercenary, ACTIVE, SUSPENDED, or UNKNOWN \(If it's dead\). Returns NULL if you do not have a Mercenary. |
| [_string_](datatype-string.md) | **MercenaryStance** | Current active mercenary stance as a string, default is NULL. |
| [_int_](datatype-int.md) | **MirEarned** | Total LDoN points earned in Miragul's |
| [_int_](datatype-int.md) | **MMEarned** | Total LDoN points earned in Mistmoore |
| [_bool_](datatype-bool.md) | **Moving** | Moving? \(including strafe\) |
| [_string_](datatype-string.md) | **Name** | First name |
| [_int_](datatype-int.md) | **NumGems** | Returns the amount of spell gems your toon has |
| [_int_](datatype-int.md) | **Orux** | Orux on your character |
| [_float_](datatype-float.md) | **PctAAExp** | AA exp as a % |
| [_int_](datatype-int.md) | **PctAAVitality** | Percentage of AA Vitality your toon has |
| [_int_](datatype-int.md) | **PctAggro** | Your aggro percentage |
| [_int_](datatype-int.md) | **PctEndurance** | Current endurance as a % |
| [_float_](datatype-float.md) | **PctExp** | Experience as a % |
| [_float_](datatype-float.md) | **PctGroupLeaderExp** | Group leadership exp as a % |
| [_int_](datatype-int.md) | **PctHPs** | Current HP as a % |
| [_int_](datatype-int.md) | **PctMana** | Current mana as a % |
| [_float_](datatype-float.md) | **PctRaidLeaderExp** | Raid leadership experience as a % |
| [_int_](datatype-int.md) | **PctVitality** | Percentage of Vitality the toon has |
| [_spell_](datatype-spell.md) | **PetBuff\[**\#**\]** | The spell in this PetBuff slot \# |
| [_int_](datatype-int.md) | **PetBuff\[**name**\]** | Finds PetBuff slot with the spell _name_ |
| [_int_](datatype-int.md) | **Phosphenes** | Phosphenes on your character |
| [_int_](datatype-int.md) | **Phosphites** | Phosphites on your character |
| [_int_](datatype-int.md) | **Platinum** | Platinum on your character |
| [_int_](datatype-int.md) | **PlatinumBank** | Platinum in bank |
| [_int_](datatype-int.md) | **PlatinumShared** | Platinum in shared bank |
| [_string_](datatype-string.md) | **Poisoned** | Returns the name of any Poison spell |
| [_int_](datatype-int.md) | **RadiantCrystals** | Number of Radiant Crystals on your character |
| [_spawn_](datatype-spawn.md) | **RaidAssistTarget\[**\#**\]** | Current raid assist target \(1-3\) |
| [_int_](datatype-int.md) | **RaidLeaderExp** | Raid leadership exp \(out of 330\) |
| [_int_](datatype-int.md) | **RaidLeaderPoints** | Raid leadership points |
| [_spawn_](datatype-spawn.md) | **RaidMarkNPC\[**\#**\]** | Current raid marked NPC \(1-3\) |
| [_bool_](datatype-bool.md) | **RangedReady** | Ranged attack ready? |
| [_int_](datatype-int.md) | **RujEarned** | Total LDoN points earned in Rujarkian |
| [_bool_](datatype-bool.md) | **Running** | Do I have auto-run turned on? |
| [_int_](datatype-int.md) | **SecondaryPctAggro** | Secondary Percentage aggro |
| [_spawn_](datatype-spawn.md) | **SecondaryAggroPlayer** | spawninfo for secondary aggro player |
| [_int_](datatype-int.md) | **ShieldingBonus** | Shielding bonus from gear and spells |
| [_bool_](datatype-bool.md) | **Shrouded** | Am I Shrouded? |
| [_string_](datatype-string.md) | **Silenced** | Returns the name of the Silence type effect on you |
| [_int_](datatype-int.md) | **Silver** | Silver on your character |
| [_int_](datatype-int.md) | **SilverBank** | Silver in bank |
| [_action_](datatype-action.md) | **Sit** | Causes toon to sit if not already |
| [_int_](datatype-int.md) | **Skill\[**name\|\#**\]** | Skill level of skill with this _name_ or _ID \#_ |
| [_int_](datatype-int.md) | **SkillCap\[**name\|\#**\]** | Skill cap of skill with this _name_ or _ID \#_ |
| [_buff_](datatype-buff.md) | **Song\[**name**\]** | Finds song with this _name_ |
| [_buff_](datatype-buff.md) | **Song\[**\#**\]** | The song in this slot \# |
| [_spawn_](datatype-spawn.md) | **Spawn** | The character's spawn |
| [_bool_](datatype-bool.md) | **SpellInCooldown** | returns TRUE if you have a spell in cooldown and FALSE when not. |
| [_int_](datatype-int.md) | **SpellDamageBonus** | Spell Damage bonus |
| [_int_](datatype-int.md) | **SpellRankCap** | your characters spell rank cap. if it returns: 1 = Rk. I spells 2 = Rk. II spells 3 = Rk. III spells |
| [_bool_](datatype-bool.md) | **SpellReady\[**name\|\#**\]** | Gem with this spell _name_ or in this gem _\#_ ready to cast? |
| [_int_](datatype-int.md) | **SpellShieldBonus** | Spell Shield bonus from gear and spells |
| [_int_](datatype-int.md) | **STA** | Character Stamina |
| [_action_](datatype-action.md) | **Stand** | causes toon to stand if not already |
| [_action_](datatype-action.md) | **StopCast** | Causes toon to stop casting |
| [_int_](datatype-int.md) | **STR** | Character Strength |
| [_int_](datatype-int.md) | **StrikeThroughBonus** | Strikethrough bonus from gear and spells |
| [_bool_](datatype-bool.md) | **Stunned** | Am I stunned? |
| [_int_](datatype-int.md) | **StunResistBonus** | Stun Resist bonus from gear and spells |
| [_string_](datatype-string.md) | **Subscription** | Subscription type GOLD, FREE, \(Silver?\) |
| [_int_](datatype-int.md) | **SubscriptionDays** | Returns an int Usage: /echo I have ${Me.SubscriptionDays} left before my all access expires. |
| [_string_](datatype-string.md) | **Surname** | Last name |
| [_int_](datatype-int.md) | **svChromatic** | Your character's lowest resist |
| [_int_](datatype-int.md) | **svCold** | Character Cold Resist |
| [_int_](datatype-int.md) | **svCorruption** | Character Corruption Resist |
| [_int_](datatype-int.md) | **svDisease** | Character Disease Resist |
| [_int_](datatype-int.md) | **svFire** | Character Fire Resist |
| [_int_](datatype-int.md) | **svMagic** | Character Magic Resist |
| [_int_](datatype-int.md) | **svPoison** | Character Poison Resist |
| [_int_](datatype-int.md) | **svPrismatic** | The average of your character's resists |
| [_int_](datatype-int.md) | **TakEarned** | Total LDoN points earned in Takish |
| [_spawn_](datatype-spawn.md) | **TargetOfTarget** | Target of Target \(will only work when group or raid Target of Target is active; if not, it will return NULL\) |
| [_int_](datatype-int.md) | **Thirst** | Thirst level |
| [_bool_](datatype-bool.md) | '''Trader | if you are an active Trader |
| [_bool_](datatype-bool.md) | **TributeActive** | Tribute Active |
| [_ticks_](datatype-ticks.md) | **TributeTimer** | Tribute Timer |
| [_bool_](datatype-bool.md) | **UseAdvancedLooting** | TRUE/FALSE if using advanced looting |
| [_int_](datatype-int.md) | **WIS** | Character Wisdom |
| [_xtarget_](datatype-xtarget.md) | **XTarget\[\#\]** | Extended target data for the specified XTarget \#. **Note: Passing no index to this returns the number of current extended targets.** |
| [_int_](datatype-int.md) | **Vitality** | Total amount of Vitality your toon has |
| '**'**[**string**](datatype-string.md) | **To String** | Same as **Name** |

## Language Table

<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <ul>
          <li>1 Common Tongue</li>
          <li>2 Barbarian</li>
          <li>3 Erudian</li>
          <li>4 Elvish</li>
          <li>5 Dark Elvish</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>6 Dwarvish</li>
          <li>7 Troll</li>
          <li>8 Ogre</li>
          <li>9 Gnomish</li>
          <li>10 Halfling</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>11 Thieves Cant</li>
          <li>12 Old Erudian</li>
          <li>13 Elder Elvish</li>
          <li>14 Froglok</li>
          <li>15 Goblin</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>16 Gnoll</li>
          <li>17 Combine Tongue</li>
          <li>17 Elder Teir&apos;Dal</li>
          <li>19 Lizardman</li>
          <li>20 Orcish</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>21 Faerie</li>
          <li>22 Dragon</li>
          <li>23 Elder Dragon</li>
          <li>24 Dark Speech</li>
          <li>25 Vah Shir</li>
        </ul>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

### Examples

`/assist Eqmule`  
`/delay 5s ${Me.AssistComplete}==TRUE`

The delay will last either 5s OR until the assist is complete

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Me](../top-level-objects/tlo-me.md)
* [spawn](datatype-spawn.md)
* [Slot Names](../../general-information/slot-names.md)

## Ref mq2-2010121\MQ2Main\MQ2DataTypes.h

Just putting this here because list above is incomplete and dont want to keep opening source...

```text
class MQ2CharacterType : public MQ2Type
{
public:
    enum CharacterMembers
    {
        CountSongs = 2,
        MaxBuffSlots = 3,
        Exp = 4,
        Spawn = 5,
        Dar = 6,
        AAExp = 7,
        AAPoints = 8,
        CurrentHPs = 10,
        MaxHPs = 11,
        HPRegen = 12,
        PctHPs = 13,
        CurrentMana = 14,
        MaxMana = 15,
        ManaRegen = 16,
        PctMana = 17,
        Buff = 18,
        Song = 19,
        Book = 20,
        Skill = 21,
        Ability = 22,
        Cash = 24,
        CashBank = 25,
        PlatinumShared = 26,
        Grouped = 27,
        HPBonus = 28,
        ManaBonus = 29,
        GukEarned = 30,
        MMEarned = 31,
        RujEarned = 32,
        TakEarned = 33,
        MirEarned = 34,
        LDoNPoints = 35,
        CurrentFavor = 36,
        CareerFavor = 37,
        Endurance = 38,
        Inventory = 39,
        Bank = 40,
        Combat = 42,
        FreeInventory = 43,
        Gem = 44,
        SpellReady = 45,
        Drunk = 50,
        STR = 51,
        STA = 52,
        CHA = 53,
        DEX = 54,
        INT = 55,
        AGI = 56,
        WIS = 57,
        svMagic = 58,
        svFire = 59,
        svCold = 60,
        svPoison = 61,
        svDisease = 62,
        Hunger = 63,
        Thirst = 64,
        BaseSTR = 65,
        BaseSTA = 66,
        BaseCHA = 67,
        BaseDEX = 68,
        BaseINT = 69,
        BaseAGI = 70,
        BaseWIS = 71,
        PracticePoints = 72,
        PctExp = 73,
        PctAAExp = 74,
        Moving = 75,
        AbilityReady = 76,
        PetBuff = 77,
        Platinum = 78,
        Gold = 79,
        Silver = 80,
        Copper = 81,
        PlatinumBank = 82,
        GoldBank = 83,
        SilverBank = 84,
        CopperBank = 85,
        Stunned = 88,
        RangedReady = 89,
        AltTimerReady = 90,
        MaxEndurance = 91,
        PctEndurance = 92,
        AltAbility = 93,
        AltAbilityReady = 94,
        AltAbilityTimer = 95,
        CombatAbility = 96,
        CombatAbilityTimer = 97,
        LargestFreeInventory = 98,
        TargetOfTarget = 99,
        RaidAssistTarget = 100,
        GroupAssistTarget = 101,
        RaidMarkNPC = 102,
        GroupMarkNPC = 103,
        CountBuffs = 104,
        LanguageSkill = 105,
        EnduranceBonus = 106,
        CombatEffectsBonus = 107,
        ShieldingBonus = 108,
        SpellShieldBonus = 109,
        AvoidanceBonus = 110,
        AccuracyBonus = 111,
        StunResistBonus = 112,
        StrikeThroughBonus = 113,
        AttackBonus = 114,
        HPRegenBonus = 115,
        ManaRegenBonus = 116,
        DamageShieldBonus = 117,
        DoTShieldBonus = 118,
        AttackSpeed = 119,
        GroupList = 120,
        AmIGroupLeader = 121,
        CurrentEndurance = 122,
        EnduranceRegen = 123,
        FreeBuffSlots = 124,
        CurrentWeight = 125,
        AAPointsSpent = 126,
        AAPointsTotal = 127,
        TributeActive = 128,
        CombatAbilityReady = 129,
        Running = 130,
        GroupSize = 131,
        TributeTimer = 132,
        RadiantCrystals = 133,
        EbonCrystals = 134,
        Shrouded = 135,
        AutoFire = 136,
        Language = 137,
        Aura = 138,
        LAMarkNPC = 139,
        LANPCHealth = 140,
        LADelegateMA = 141,
        LADelegateMarkNPC = 142,
        LAInspectBuffs = 143,
        LASpellAwareness = 144,
        LAOffenseEnhancement = 145,
        LAManaEnhancement = 146,
        LAHealthEnhancement = 147,
        LAHealthRegen = 148,
        LAFindPathPC = 149,
        LAHoTT = 150,
        ActiveFavorCost = 151,
        CombatState = 152,
        svCorruption = 153,
        svPrismatic = 154,
        svChromatic = 155,
        Doubloons = 156,
        Orux = 157,
        Phosphenes = 158,
        Phosphites = 159,
        Fellowship = 160,
        Downtime = 161,
        DamageShieldMitigationBonus = 162,
        HeroicSTRBonus = 163,
        HeroicINTBonus = 164,
        HeroicWISBonus = 165,
        HeroicAGIBonus = 166,
        HeroicDEXBonus = 167,
        HeroicSTABonus = 168,
        HeroicCHABonus = 169,
        HealAmountBonus = 170,
        SpellDamageBonus = 171,
        ClairvoyanceBonus = 172,
        EnduranceRegenBonus = 173,
        Counters = 174,
        Faycites = 175,
        Chronobines = 176,
        Mercenary = 177,
        XTarget = 178,
        Haste = 179,
        MercenaryStance = 180,
        SkillCap = 181,
        GemTimer = 182,
        HaveExpansion = 183,
        PctAggro = 184,
        SecondaryPctAggro = 185,
        SecondaryAggroPlayer = 186,
        AggroLock = 187,
        ZoneBound = 188,
        ZoneBoundX = 189,
        ZoneBoundY = 190,
        ZoneBoundZ = 191,
        PctMercAAExp = 192,
        MercAAExp = 193,
        Subscription = 194,
        AAPointsAssigned = 195,
        AltCurrency = 196,
        ActiveDisc = 197,
        Commemoratives = 198,
        Nobles = 199,
        Zoning = 200,
        InInstance = 201,
        Instance = 202,
        MercListInfo = 203,
        UseAdvancedLooting = 204,
        Fists = 205,
        EnergyCrystals = 206,
        PiecesofEight = 207,
        SpellInCooldown = 208,
        Slowed = 209,
        Rooted = 210,
        Mezzed = 211,
        Crippled = 212,
        Malod = 213,
        Tashed = 214,
        Snared = 215,
        Hasted = 216,
        Aego = 217,
        Skin = 218,
        Focus = 219,
        Regen = 220,
        Symbol = 221,
        Clarity = 222,
        Pred = 223,
        Strength = 224,
        Brells = 225,
        SV = 226,
        SE = 227,
        HybridHP = 228,
        Growth = 229,
        Shining = 230,
        Beneficial = 231,
        DSed = 232,
        RevDSed = 233,
        Charmed = 234,
        CursorPlatinum = 235,
        CursorGold = 236,
        CursorSilver = 237,
        CursorCopper = 238,
        Diseased = 239,
        Poisoned = 240,
        Cursed = 241,
        Corrupted = 242,
        Krono = 243,
        XTargetSlots = 244,
        AssistComplete = 245,
        ItemReady = 246,
        NumGems = 247,
        Vitality = 248,
        PctVitality = 249,
        AAVitality = 250,
        PctAAVitality = 251,
        GuildID = 252,
        ExpansionFlags = 253,
        SPA = 254,
        BoundLocation = 255,
        SkillBase = 256,
    };
    enum CharacterMethods
    {
        Stand,
        Sit,
        Dismount,
        StopCast,
    };
```

