## Description

This data type contains all the information about *your* character.

Inherits *[spawn](datatype-spawn.md)*.

## Members

|                                                |                                       |                                                                                                                                                                                     |
|------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**                                       | **Member**                            | **Description**                                                                                                                                                                     |
| *[int](datatype-int.md)*               | **AAExp**                             | AA exp as a raw number out of 10,000 (10,000=100%)                                                                                                                                  |
| *[int](datatype-int.md)*               | **AAPoints**                          | Unused AA points                                                                                                                                                                    |
| *[int](datatype-int.md)*               | **AAPointsSpent**                     | The number of points you have spent on AA abilities                                                                                                                                 |
| *[int](datatype-int.md)*               | **AAPointsTotal**                     | The total number of AA points you have                                                                                                                                              |
| *[int](datatype-int.md)*               | **AAVitality**                        | The total number of AA Vitality you have                                                                                                                                            |
| *[string](datatype-string.md)*         | **Ability\[**name**\]**               | Skill name assigned to this doability button                                                                                                                                        |
| *[int](datatype-int.md)*               | **Ability\[**#**\]**                  | The doability button number that the skill *name* is on                                                                                                                             |
| *[bool](datatype-bool.md)*             | **AbilityReady\[**#\|name**\]**       | Ability with this *name* or on this button *#* ready?                                                                                                                               |
| *[int](datatype-int.md)*               | **AccuracyBonus**                     | Accuracy bonus from gear and spells                                                                                                                                                 |
| *[spell](datatype-spell.md)*           | **ActiveDisc**                        | Returns a spell if melee discipline is active.                                                                                                                                      |
| *[int](datatype-int.md)*               | **ActiveFavorCost**                   | If Tribute is active, how much it is costing you every 10 minutes. Returns NULL if tribute is inactive.                                                                             |
| *[altability](datatype-altability.md)* | **AltAbility\[**#\|name**\]**         | Returns the total number of points you have spent in ability # or *name*                                                                                                            |
| *[bool](datatype-bool.md)*             | **AltAbilityReady\[**#\|name**\]**    | Alt ability *#* or *name* ready?                                                                                                                                                    |
| *[int](datatype-int.md)*               | **AltAbilityTimer\[**#\|name**\]**    | Alt ability reuse time remaining (in ticks) for ability *#* or *name*                                                                                                               |
| *[bool](datatype-bool.md)*             | **AltTimerReady**                     | Alternate timer ready? (Bash/Slam/Frenzy/Backstab). **Note: ${AbilityReady} works fine with most of these.**                                                                        |
| *[int](datatype-int.md)*               | **AGI**                               | Character Agility                                                                                                                                                                   |
| *[spawn](datatype-spawn.md)*           | **AggroLock**                         | spawn info for aggro lock player                                                                                                                                                    |
| *[bool](datatype-bool.md)*             | **AmIGroupLeader**                    | Am I the group leader?                                                                                                                                                              |
| *[bool](datatype-bool.md)*             | **AssistComplete**                    | returns true/false if the assist is complete                                                                                                                                        |
| *[int](datatype-int.md)*               | **AttackBonus**                       | Attack bonus from gear and spells                                                                                                                                                   |
| *[int](datatype-int.md)*               | **AttackSpeed**                       | Your Attack Speed. No haste spells/items = AttackSpeed of 100. A 41% haste item will result in an AttackSpeed of 141. This variable does not take into account spell or song haste. |
| *[string](datatype-string.md)*         | **Aura**                              | The aura effect name                                                                                                                                                                |
| *[bool](datatype-bool.md)*             | **AutoFire**                          | Is Autofire on?                                                                                                                                                                     |
| *[int](datatype-int.md)*               | **AvoidanceBonus**                    | Avoidance bonus from gear/spells                                                                                                                                                    |
| *[item](datatype-item.md)*             | **Bank\[**#**\]**                     | Item in this bankslot #                                                                                                                                                             |
| *[bool](datatype-bool.md)*             | **BardSongPlaying**                   | Is a bard song playing?                                                                                                                                                             |
| *[int](datatype-int.md)*               | **Book\[**name**\]**                  | Slot in your spellbook assigned to spell *name*.                                                                                                                                    |
| *[spell](datatype-spell.md)*           | **Book\[**#**\]**                     | Spell assigned to this slot # in your spellbook                                                                                                                                     |
| *[buff](datatype-buff.md)*             | **Buff\[**name**\]**                  | The buff with this name                                                                                                                                                             |
| *[buff](datatype-buff.md)*             | **Buff\[**#**\]**                     | The buff in this slot #                                                                                                                                                             |
| *[bool](datatype-bool.md)*             | '''Buyer                              | if you are an active buyer                                                                                                                                                          |
| *[bool](datatype-bool.md)*             | '''CanMount                           | for some indoor zones that where not flagged as nomount and added bazaar, nexus to zones where its ok to mount.                                                                     |
| *[int](datatype-int.md)*               | **CareerFavor**                       | Career favor/tribute                                                                                                                                                                |
| *[int](datatype-int.md)*               | **Cash**                              | Total cash on your character, expressed in coppers (eg. if you are carrying 100pp, **Cash** will return 100000)                                                                     |
| *[int](datatype-int.md)*               | **CashBank**                          | Total cash in your bank, expressed in coppers                                                                                                                                       |
| *[int](datatype-int.md)*               | **CHA**                               | Character Charisma                                                                                                                                                                  |
| *[int](datatype-int.md)*               | **Chronobines**                       | Chronobines on your character                                                                                                                                                       |
| *[int](datatype-int.md)*               | **ClairvoyanceBonus**                 | Clairvoyance Bonus                                                                                                                                                                  |
| *[bool](datatype-bool.md)*             | **Combat**                            | In combat?                                                                                                                                                                          |
| *[spell](datatype-spell.md)*           | **CombatAbility\[**#**\]**            | The name of Combat Ability # in your list (not the same as anyone else's list!)                                                                                                     |
| *[int](datatype-int.md)*               | **CombatAbility\[**name**\]**         | The number of Combat ability *name* in your list (not the same as anyone else's list!)                                                                                              |
| *[bool](datatype-bool.md)*             | **CombatAbilityReady\[**name\|#\]'''  | Is this Combat Ability ready?                                                                                                                                                       |
| *[int](datatype-int.md)*               | **CombatAbilityTimer\[**name\|#**\]** | The time remaining (in seconds) before the Combat Ability *name* is usable                                                                                                          |
| *[int](datatype-int.md)*               | **CombatEffectsBonus**                | Combat Effects bonus from gear and spells                                                                                                                                           |
| *[string](datatype-string.md)*         | **CombatState**                       | Returns one of the following: COMBAT, DEBUFFED, COOLDOWN, ACTIVE, RESTING, UNKNOWN                                                                                                  |
| *[int](datatype-int.md)*               | **Copper**                            | Copper on your character                                                                                                                                                            |
| *[int](datatype-int.md)*               | **CopperBank**                        | Copper in bank                                                                                                                                                                      |
| *[spell](datatype-spell.md)*           | **Corrupted**                         | Returns the name of the Corrupted debuff if you have one                                                                                                                            |
| *[int](datatype-int.md)*               | **CountBuffs**                        | Number of buffs you have, not including short duration buffs                                                                                                                        |
| *[int](datatype-int.md)*               | **CountersCurse**                     | Number of curse counters you have                                                                                                                                                   |
| *[int](datatype-int.md)*               | **CountersDisease**                   | Number of disease counters you have                                                                                                                                                 |
| *[int](datatype-int.md)*               | **CountersPoison**                    | Number of poison counters you have                                                                                                                                                  |
| *[int](datatype-int.md)*               | **CountSongs**                        | Number of songs you have                                                                                                                                                            |
| *[int](datatype-int.md)*               | **Counters**                          | Damage Absorption Counters Remaining                                                                                                                                                |
| *[int](datatype-int.md)*               | **CurrentEndurance**                  | Current endurance                                                                                                                                                                   |
| *[int](datatype-int.md)*               | **CurrentFavor**                      | Current favor/tribute                                                                                                                                                               |
| *[int](datatype-int.md)*               | **CurrentHPs**                        | Current hit points                                                                                                                                                                  |
| *[int](datatype-int.md)*               | **CurrentMana**                       | Current mana                                                                                                                                                                        |
| *[int](datatype-int.md)*               | **CurrentWeight**                     | Current weight                                                                                                                                                                      |
| *[spell](datatype-spell.md)*           | **Cursed**                            | Returns the name of the Curse debuff if you are effected by one                                                                                                                     |
| *[int](datatype-int.md)*               | **DamageShieldBonus**                 | Damage Shield bonus from gear and spells                                                                                                                                            |
| *[int](datatype-int.md)*               | **DamageShieldMitigationBonus**       | Damage Shield Mitigation bonus from gear and spells                                                                                                                                 |
| *[int](datatype-int.md)*               | **Dar**                               | Damage absorption remaining (eg. from Rune-type spells)                                                                                                                             |
| *[string](datatype-string.md)*         | **Diseased**                          | Returns the name of any Disease spell                                                                                                                                               |
| *[int](datatype-int.md)*               | **DEX**                               | Character Dexterity                                                                                                                                                                 |
| *[string](datatype-string.md)*         | **Dotted**                            | Returns name of first DoT on character.                                                                                                                                             |
| *[int](datatype-int.md)*               | **DoTShieldBonus**                    | DoT Shield bonus from gear and spells                                                                                                                                               |
| *[int](datatype-int.md)*               | **Doubloons**                         | Doubloons on your character                                                                                                                                                         |
| *[ticks](datatype-ticks.md)*           | **Downtime**                          | Downtime (Ticks left til combat timer end)                                                                                                                                          |
| *[int](datatype-int.md)*               | **Drunk**                             | Drunkenness level                                                                                                                                                                   |
| *[int](datatype-int.md)*               | **EbonCrystals**                      | Number of Ebon Crystals on your character                                                                                                                                           |
| *[int](datatype-int.md)*               | **EnduranceBonus**                    | Endurance bonus from gear and spells                                                                                                                                                |
| *[int](datatype-int.md)*               | **EnduranceRegen**                    | Endurance regen from the last tick                                                                                                                                                  |
| *[int](datatype-int.md)*               | **EnduranceRegenBonus**               | Endurance regen bonus                                                                                                                                                               |
| *[int](datatype-int.md)*               | **Exp**                               | Experience (out of 10,000)                                                                                                                                                          |
| *[int](datatype-int.md)*               | **ExpansionFlags**                    | Returns a numeric number representing which expansions your toon is flagged for                                                                                                     |
| *[int](datatype-int.md)*               | **Faycites**                          | Faycites on your character                                                                                                                                                          |
| *[fellowship](datatype-fellowship.md)* | **Fellowship**                        | Info about Fellowship                                                                                                                                                               |
| *[int](datatype-int.md)*               | **FreeBuffSlots**                     | Number of open buff slots (not counting the short duration buff slots)                                                                                                              |
| *[int](datatype-int.md)*               | **FreeInventory**                     | Number of free inventory spaces                                                                                                                                                     |
| *[int](datatype-int.md)*               | **FreeInventory\[#\]**                | Number of free inventory spaces of at least # size (giant=4)                                                                                                                        |
| *[int](datatype-int.md)*               | **Gem\[**name**\]**                   | Returns the slot # with the spell *name*                                                                                                                                            |
| *[spell](datatype-spell.md)*           | **Gem\[**#**\]**                      | The name of the spell in this slot #                                                                                                                                                |
| *[ticks](datatype-ticks.md)*           | **GemTimer\[**name\|#**\]**           | The timer for the spell with this *name* or in this gem *#*                                                                                                                         |
| *[int](datatype-int.md)*               | **Gold**                              | Gold on character                                                                                                                                                                   |
| *[int](datatype-int.md)*               | **GoldBank**                          | Gold in bank                                                                                                                                                                        |
| *[spawn](datatype-spawn.md)*           | **GroupAssistTarget**                 | Current group assist target                                                                                                                                                         |
| *[bool](datatype-bool.md)*             | **Grouped**                           | Grouped?                                                                                                                                                                            |
| *[int](datatype-int.md)*               | **GroupLeaderExp**                    | Group leadership experience (out of 330)                                                                                                                                            |
| *[int](datatype-int.md)*               | **GroupLeaderPoints**                 | Group leadership points                                                                                                                                                             |
| *[string](datatype-string.md)*         | **GroupList**                         | Returns a string of your group members (excluding you)                                                                                                                              |
| *[spawn](datatype-spawn.md)*           | **GroupMarkNPC\[**#**\]**             | Current group marked NPC (1-3)                                                                                                                                                      |
| *[int](datatype-int.md)*               | **GroupSize**                         | Size of group                                                                                                                                                                       |
| *[int](datatype-int.md)*               | **GukEarned**                         | Total LDoN points earned in Deepest Guk                                                                                                                                             |
| *[int](datatype-int.md)*               | **GuildID**                           | Returns the ID number of your guild                                                                                                                                                 |
| *[bool](datatype-bool.md)*             | **HaveExpansion\[**#**\]**            | Returns TRUE/FALSE if you have that expansion #                                                                                                                                     |
| *[int](datatype-int.md)*               | **Haste**                             | Total Combined Haste (worn and spell) as shown in Inventory Window stats                                                                                                            |
| *[int](datatype-int.md)*               | **HealAmountBonus**                   | Total Heal Amount bonus from gear                                                                                                                                                   |
| *[int](datatype-int.md)*               | **HeroicAGIBonus**                    | Total Heroic Agility bonus from gear                                                                                                                                                |
| *[int](datatype-int.md)*               | **HeroicCHABonus**                    | Total Heroic Charisma bonus from gear                                                                                                                                               |
| *[int](datatype-int.md)*               | **HeroicDEXBonus**                    | Total Heroic Dexterity bonus from gear                                                                                                                                              |
| *[int](datatype-int.md)*               | **HeroicINTBonus**                    | Total Heroic Intelligence bonus from gear                                                                                                                                           |
| *[int](datatype-int.md)*               | **HeroicSTABonus**                    | Total Heroic Stamina bonus from gear                                                                                                                                                |
| *[int](datatype-int.md)*               | **HeroicSTRBonus**                    | Total Heroic Strength bonus from gear                                                                                                                                               |
| *[int](datatype-int.md)*               | **HeroicWISBonus**                    | Total Heroic Wisdom bonus from gear                                                                                                                                                 |
| *[int](datatype-int.md)*               | **HPBonus**                           | Hit point bonus from gear and spells                                                                                                                                                |
| *[int](datatype-int.md)*               | **HPRegen**                           | Hit point regeneration from last tick                                                                                                                                               |
| *[int](datatype-int.md)*               | **HPRegenBonus**                      | HP regen bonus from gear and spells                                                                                                                                                 |
| *[int](datatype-int.md)*               | **Hunger**                            | Hunger level                                                                                                                                                                        |
| *[int](datatype-int.md)*               | **ID**                                | Spawn ID                                                                                                                                                                            |
| *[bool](datatype-bool.md)*             | **InInstance**                        | Returns TRUE/FALSE if you are in an instance.                                                                                                                                       |
| *[int](datatype-int.md)*               | **INT**                               | Character Intelligence                                                                                                                                                              |
| *[item](datatype-item.md)*             | **Inventory\[**#**\]**                | Item in this slot #                                                                                                                                                                 |
| *[item](datatype-item.md)*             | **Inventory\[**slotname**\]**         | Item in this *slotname* (inventory slots only). See [Slot Names](../general-information/slot-names.md) for a list of *slotnames*.                                                                  |
| *[string](datatype-string.md)*         | **Invulnerable**                      | Returns the invulnerable spell name on you, can be used with spell data type ex. ${Me.Invulnerable.Spell.ID}                                                                        |
| *[bool](datatype-bool.md)*             | **ItemReady\[XXX\]**                  | True/False on if the item is ready to cast.                                                                                                                                         |
| *[int](datatype-int.md)*               | **LADelegateMA**                      | Level of Delegate MA of the current group leader (not your own ability level)                                                                                                       |
| *[int](datatype-int.md)*               | **LADelegateMarkNPC**                 | Level of Delegate Mark NPC of the current group leader (not your own ability level)                                                                                                 |
| *[int](datatype-int.md)*               | **LAFindPathPC**                      | Level of Find Path PC of the current group leader (not your own ability level)                                                                                                      |
| *[int](datatype-int.md)*               | **LAHealthEnhancement**               | Level of Health Enhancement of the current group leader (not your own ability level)                                                                                                |
| *[int](datatype-int.md)*               | **LAHealthRegen**                     | Level of Health Regen of the current group leader (not your own ability level)                                                                                                      |
| *[int](datatype-int.md)*               | **LAHoTT**                            | Level of HoTT of the current group leader (not your own ability level)                                                                                                              |
| *[int](datatype-int.md)*               | **LAInspectBuffs**                    | Level of Inspect Buffs of the current group leader (not your own ability level)                                                                                                     |
| *[int](datatype-int.md)*               | **LAManaEnhancement**                 | Level of Mana Enhancement of the current group leader (not your own ability level)                                                                                                  |
| *[int](datatype-int.md)*               | **LAMarkNPC**                         | Level of Mark NPC of the current group leader (not your own ability level)                                                                                                          |
| *[int](datatype-int.md)*               | **LANPCHealth**                       | Level of NPC Health of the current group leader (not your own ability level)                                                                                                        |
| *[int](datatype-int.md)*               | **LAOffenseEnhancement**              | Level of Offense Enhancement of the current group leader (not your own ability level)                                                                                               |
| *[int](datatype-int.md)*               | **LASpellAwareness**                  | Level of Spell Awareness of the current group leader (not your own ability level)                                                                                                   |
| *[int](datatype-int.md)*               | **Language\[**language name**\]**     | The EQ language number of the specified language. See below for language/number table.                                                                                              |
| *[string](datatype-string.md)*         | **Language\[**language number**\]**   | Returns the EQ language name of the *language number* specified. See below for language/number table.                                                                               |
| *[int](datatype-int.md)*               | **LanguageSkill\[**language**\]**     | Your skill in *language*                                                                                                                                                            |
| *[int](datatype-int.md)*               | **LargestFreeInventory**              | Size of your largest free inventory space                                                                                                                                           |
| *[int](datatype-int.md)*               | **LargestFreeInventory**              | Size of your largest free inventory space                                                                                                                                           |
| *[timestamp](datatype-timestamp.md)*   | **LastZoned**                         | Returns a timestamp of last time you zoned                                                                                                                                          |
| *[int](datatype-int.md)*               | **LDoNPoints**                        | Available LDoN points                                                                                                                                                               |
| *[int](datatype-int.md)*               | **Level**                             | Character Level                                                                                                                                                                     |
| *[int](datatype-int.md)*               | **ManaBonus**                         | Mana bonus from gear and spells                                                                                                                                                     |
| *[int](datatype-int.md)*               | **ManaRegen**                         | Mana regeneration from last tick                                                                                                                                                    |
| *[int](datatype-int.md)*               | **ManaRegenBonus**                    | Mana regen bonus from gear and spells                                                                                                                                               |
| *[int](datatype-int.md)*               | **MaxBuffSlots**                      | Max number of buffs you can have on you. /echo ${Me.MaxBuffSlots}                                                                                                                   |
| *[int](datatype-int.md)*               | **MaxEndurance**                      | Max endurance                                                                                                                                                                       |
| *[int](datatype-int.md)*               | **MaxHPs**                            | Max hit points                                                                                                                                                                      |
| *[int](datatype-int.md)*               | **MaxMana**                           | Max mana                                                                                                                                                                            |
| *[string](datatype-string.md)*         | **Mercenary**                         | The state of your Mercenary, ACTIVE, SUSPENDED, or UNKNOWN (If it's dead). Returns NULL if you do not have a Mercenary.                                                             |
| *[string](datatype-string.md)*         | **MercenaryStance**                   | Current active mercenary stance as a string, default is NULL.                                                                                                                       |
| *[int](datatype-int.md)*               | **MirEarned**                         | Total LDoN points earned in Miragul's                                                                                                                                               |
| *[int](datatype-int.md)*               | **MMEarned**                          | Total LDoN points earned in Mistmoore                                                                                                                                               |
| *[bool](datatype-bool.md)*             | **Moving**                            | Moving? (including strafe)                                                                                                                                                          |
| *[string](datatype-string.md)*         | **Name**                              | First name                                                                                                                                                                          |
| *[int](datatype-int.md)*               | **NumGems**                           | Returns the amount of spell gems your toon has                                                                                                                                      |
| *[int](datatype-int.md)*               | **Orux**                              | Orux on your character                                                                                                                                                              |
| *[float](datatype-float.md)*           | **PctAAExp**                          | AA exp as a %                                                                                                                                                                       |
| *[int](datatype-int.md)*               | **PctAAVitality**                     | Percentage of AA Vitality your toon has                                                                                                                                             |
| *[int](datatype-int.md)*               | **PctAggro**                          | Your aggro percentage                                                                                                                                                               |
| *[int](datatype-int.md)*               | **PctEndurance**                      | Current endurance as a %                                                                                                                                                            |
| *[float](datatype-float.md)*           | **PctExp**                            | Experience as a %                                                                                                                                                                   |
| *[float](datatype-float.md)*           | **PctGroupLeaderExp**                 | Group leadership exp as a %                                                                                                                                                         |
| *[int](datatype-int.md)*               | **PctHPs**                            | Current HP as a %                                                                                                                                                                   |
| *[int](datatype-int.md)*               | **PctMana**                           | Current mana as a %                                                                                                                                                                 |
| *[float](datatype-float.md)*           | **PctRaidLeaderExp**                  | Raid leadership experience as a %                                                                                                                                                   |
| *[int](datatype-int.md)*               | **PctVitality**                       | Percentage of Vitality the toon has                                                                                                                                                 |
| *[spell](datatype-spell.md)*           | **PetBuff\[**#**\]**                  | The spell in this PetBuff slot #                                                                                                                                                    |
| *[int](datatype-int.md)*               | **PetBuff\[**name**\]**               | Finds PetBuff slot with the spell *name*                                                                                                                                            |
| *[int](datatype-int.md)*               | **Phosphenes**                        | Phosphenes on your character                                                                                                                                                        |
| *[int](datatype-int.md)*               | **Phosphites**                        | Phosphites on your character                                                                                                                                                        |
| *[int](datatype-int.md)*               | **Platinum**                          | Platinum on your character                                                                                                                                                          |
| *[int](datatype-int.md)*               | **PlatinumBank**                      | Platinum in bank                                                                                                                                                                    |
| *[int](datatype-int.md)*               | **PlatinumShared**                    | Platinum in shared bank                                                                                                                                                             |
| *[string](datatype-string.md)*         | **Poisoned**                          | Returns the name of any Poison spell                                                                                                                                                |
| *[int](datatype-int.md)*               | **RadiantCrystals**                   | Number of Radiant Crystals on your character                                                                                                                                        |
| *[spawn](datatype-spawn.md)*           | **RaidAssistTarget\[**#**\]**         | Current raid assist target (1-3)                                                                                                                                                    |
| *[int](datatype-int.md)*               | **RaidLeaderExp**                     | Raid leadership exp (out of 330)                                                                                                                                                    |
| *[int](datatype-int.md)*               | **RaidLeaderPoints**                  | Raid leadership points                                                                                                                                                              |
| *[spawn](datatype-spawn.md)*           | **RaidMarkNPC\[**#**\]**              | Current raid marked NPC (1-3)                                                                                                                                                       |
| *[bool](datatype-bool.md)*             | **RangedReady**                       | Ranged attack ready?                                                                                                                                                                |
| *[int](datatype-int.md)*               | **RujEarned**                         | Total LDoN points earned in Rujarkian                                                                                                                                               |
| *[bool](datatype-bool.md)*             | **Running**                           | Do I have auto-run turned on?                                                                                                                                                       |
| *[int](datatype-int.md)*               | **SecondaryPctAggro**                 | Secondary Percentage aggro                                                                                                                                                          |
| *[spawn](datatype-spawn.md)*           | **SecondaryAggroPlayer**              | spawninfo for secondary aggro player                                                                                                                                                |
| *[int](datatype-int.md)*               | **ShieldingBonus**                    | Shielding bonus from gear and spells                                                                                                                                                |
| *[bool](datatype-bool.md)*             | **Shrouded**                          | Am I Shrouded?                                                                                                                                                                      |
| *[string](datatype-string.md)*         | **Silenced**                          | Returns the name of the Silence type effect on you                                                                                                                                  |
| *[int](datatype-int.md)*               | **Silver**                            | Silver on your character                                                                                                                                                            |
| *[int](datatype-int.md)*               | **SilverBank**                        | Silver in bank                                                                                                                                                                      |
| *[action](datatype-action.md)*         | **Sit**                               | Causes toon to sit if not already                                                                                                                                                   |
| *[int](datatype-int.md)*               | **Skill\[**name\|#**\]**              | Skill level of skill with this *name* or *ID #*                                                                                                                                     |
| *[int](datatype-int.md)*               | **SkillCap\[**name\|#**\]**           | Skill cap of skill with this *name* or *ID #*                                                                                                                                       |
| *[buff](datatype-buff.md)*             | **Song\[**name**\]**                  | Finds song with this *name*                                                                                                                                                         |
| *[buff](datatype-buff.md)*             | **Song\[**#**\]**                     | The song in this slot #                                                                                                                                                             |
| *[spawn](datatype-spawn.md)*           | **Spawn**                             | The character's spawn                                                                                                                                                               |
| *[bool](datatype-bool.md)*             | **SpellInCooldown**                   | returns TRUE if you have a spell in cooldown and FALSE when not.                                                                                                                    |
| *[int](datatype-int.md)*               | **SpellDamageBonus**                  | Spell Damage bonus                                                                                                                                                                  |
| *[int](datatype-int.md)*               | **SpellRankCap**                      | your characters spell rank cap. if it returns: 1 = Rk. I spells 2 = Rk. II spells 3 = Rk. III spells                                                                                |
| *[bool](datatype-bool.md)*             | **SpellReady\[**name\|#**\]**         | Gem with this spell *name* or in this gem *#* ready to cast?                                                                                                                        |
| *[int](datatype-int.md)*               | **SpellShieldBonus**                  | Spell Shield bonus from gear and spells                                                                                                                                             |
| *[int](datatype-int.md)*               | **STA**                               | Character Stamina                                                                                                                                                                   |
| *[action](datatype-action.md)*         | **Stand**                             | causes toon to stand if not already                                                                                                                                                 |
| *[action](datatype-action.md)*         | **StopCast**                          | Causes toon to stop casting                                                                                                                                                         |
| *[int](datatype-int.md)*               | **STR**                               | Character Strength                                                                                                                                                                  |
| *[int](datatype-int.md)*               | **StrikeThroughBonus**                | Strikethrough bonus from gear and spells                                                                                                                                            |
| *[bool](datatype-bool.md)*             | **Stunned**                           | Am I stunned?                                                                                                                                                                       |
| *[int](datatype-int.md)*               | **StunResistBonus**                   | Stun Resist bonus from gear and spells                                                                                                                                              |
| *[string](datatype-string.md)*         | **Subscription**                      | Subscription type GOLD, FREE, (Silver?)                                                                                                                                             |
| *[int](datatype-int.md)*               | **SubscriptionDays**                  | Returns an int Usage: /echo I have ${Me.SubscriptionDays} left before my all access expires.                                                                                        |
| *[string](datatype-string.md)*         | **Surname**                           | Last name                                                                                                                                                                           |
| *[int](datatype-int.md)*               | **svChromatic**                       | Your character's lowest resist                                                                                                                                                      |
| *[int](datatype-int.md)*               | **svCold**                            | Character Cold Resist                                                                                                                                                               |
| *[int](datatype-int.md)*               | **svCorruption**                      | Character Corruption Resist                                                                                                                                                         |
| *[int](datatype-int.md)*               | **svDisease**                         | Character Disease Resist                                                                                                                                                            |
| *[int](datatype-int.md)*               | **svFire**                            | Character Fire Resist                                                                                                                                                               |
| *[int](datatype-int.md)*               | **svMagic**                           | Character Magic Resist                                                                                                                                                              |
| *[int](datatype-int.md)*               | **svPoison**                          | Character Poison Resist                                                                                                                                                             |
| *[int](datatype-int.md)*               | **svPrismatic**                       | The average of your character's resists                                                                                                                                             |
| *[int](datatype-int.md)*               | **TakEarned**                         | Total LDoN points earned in Takish                                                                                                                                                  |
| *[spawn](datatype-spawn.md)*           | **TargetOfTarget**                    | Target of Target (will only work when group or raid Target of Target is active; if not, it will return NULL)                                                                        |
| *[int](datatype-int.md)*               | **Thirst**                            | Thirst level                                                                                                                                                                        |
| *[bool](datatype-bool.md)*             | '''Trader                             | if you are an active Trader                                                                                                                                                         |
| *[bool](datatype-bool.md)*             | **TributeActive**                     | Tribute Active                                                                                                                                                                      |
| *[ticks](datatype-ticks.md)*           | **TributeTimer**                      | Tribute Timer                                                                                                                                                                       |
| *[bool](datatype-bool.md)*             | **UseAdvancedLooting**                | TRUE/FALSE if using advanced looting                                                                                                                                                |
| *[int](datatype-int.md)*               | **WIS**                               | Character Wisdom                                                                                                                                                                    |
| *[xtarget](datatype-xtarget.md)*       | **XTarget\[#\]**                      | Extended target data for the specified XTarget #. **Note: Passing no index to this returns the number of current extended targets.**                                                |
| *[int](datatype-int.md)*               | **Vitality**                          | Total amount of Vitality your toon has                                                                                                                                              |
| '**'[string](datatype-string.md)**     | **To String**                         | Same as **Name**                                                                                                                                                                    |

## Language Table

<table>
<tbody>
<tr class="odd">
<td><ul>
<li>1 Common Tongue</li>
<li>2 Barbarian</li>
<li>3 Erudian</li>
<li>4 Elvish</li>
<li>5 Dark Elvish</li>
</ul></td>
<td><ul>
<li>6 Dwarvish</li>
<li>7 Troll</li>
<li>8 Ogre</li>
<li>9 Gnomish</li>
<li>10 Halfling</li>
</ul></td>
<td><ul>
<li>11 Thieves Cant</li>
<li>12 Old Erudian</li>
<li>13 Elder Elvish</li>
<li>14 Froglok</li>
<li>15 Goblin</li>
</ul></td>
<td><ul>
<li>16 Gnoll</li>
<li>17 Combine Tongue</li>
<li>17 Elder Teir'Dal</li>
<li>19 Lizardman</li>
<li>20 Orcish</li>
</ul></td>
<td><ul>
<li>21 Faerie</li>
<li>22 Dragon</li>
<li>23 Elder Dragon</li>
<li>24 Dark Speech</li>
<li>25 Vah Shir</li>
</ul></td>
</tr>
</tbody>
</table>

### Examples

`/assist Eqmule `  
`/delay 5s ${Me.AssistComplete}==TRUE`

The delay will last either 5s OR until the assist is complete

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Me](../top-level-objects/tlo-me.md)
-   [spawn](datatype-spawn.md)
-   [Slot Names](../general-information/slot-names.md)

## Ref mq2-2010121\\MQ2Main\\MQ2DataTypes.h

Just putting this here because list above is incomplete and dont want to keep opening source...

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


