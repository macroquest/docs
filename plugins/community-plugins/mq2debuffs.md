# MQ2Debuffs

## Description

This plugin is designed to help with curing detrimental effects. It is used to reports harmful effects, number of curse/disease/poison counters and various other detrimentals.

Author: PinkFloyd33 Author: s0rcier Version: 1.2 Date: 20061223 v2.0 - Eqmule 07-22-2016 - Added string safety.

## MQ2Debuffs

MQ2Debuffs was posted to the VIP section of MQ2 by pinkfloydx33 you can read the thread by following [This Link.](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=13495&hilit=debuff) (VIP REQUIRED)

Updated Apr 03, 2016 by Trevyn [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=13495&hilit=debuff&start=15) Updated July 22, 2016 by EQMule: included in MQ2Update

## Top-Level Object: ${Debuff}

| **Type** | **Member Name** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../../reference/data-types/datatype-bool.md) | **${Debuff}** | True if yo uhave debuffs on that have counters on them, false if not. |
| [_int_](../../reference/data-types/datatype-int.md) | **Poisoned** | # of poison counters on you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Diseased** | # of disease counters on you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Cursed** | # of curse counters on you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Corrupted** | # of corruption counters on you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Poisons** | # of poison spells affecting you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Diseases** | # of disease spells affecting you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Curses** | # of curse spells affecting you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Corruptions** | # of corruption spells affecting you. |
| [_int_](../../reference/data-types/datatype-int.md) | **Count** | # of debuffs that need cured, does not include snare. |
| [_int_](../../reference/data-types/datatype-int.md) | **HPDrain** | Amount of HP you are losing per tick from debuffs. This value is POSITIVE. |
| [_int_](../../reference/data-types/datatype-int.md) | **HPDrain[Disease\|Poison\|Curse\|All]** | Number of specific counters effecting HP. |
| [_int_](../../reference/data-types/datatype-int.md) | **ManaDrain** | Amount of Mana you are losing per tick from debuffs. This value is POSITIVE. |
| [_int_](../../reference/data-types/datatype-int.md) | **ManaDrain[Disease\|Poison\|Curse\|All]** | Number of specific counters effecting Mana. |
| [_int_](../../reference/data-types/datatype-int.md) | **EnduranceDrain** | Amount of Endurance you are losing per tick from debuffs. This value is POSITIVE. |
| [_int_](../../reference/data-types/datatype-int.md) | **EnduranceDrain[Disease\|Poison\|Curse\|All]** | Number of specific counters effecting Endurance. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Slowed** | True if you are Slowed (melee attacks), False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Snared** | True if your are Snared, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ManaCost** | True if your Spell Mana Cost has been raised, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **CastingLevel** | True if your Effective Casting Level has been reduced, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **HealingEff** | True if your Healing Effectiveness has been reduced, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **SpellDmgEff** | True if your Spell Damage Effectiveness has been reduced, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Blind** | True if you are Blind, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Charmed** | True if you are Charmed, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Feared** | True if you are Feared, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Silenced** | True if you are Silenced, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Invulnerable** | True if you are Invulnerable, False if not. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Detrimentals** | True if you have any detrimental effects on you, False if not. |
| [_int_](../../reference/data-types/datatype-int.md) | **Counters** | # of poison/disease/curse/corruption counters on yourself. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Rooted** | True if you are Rooted, False if not. |

`The TLO has been enhanced, revamped, recored, to be able to get Debuff Informations others then selfbuff.`

`Debuff.X or Debuff[self].X or Debuff[myself].X : return infos for buff from self.`<br>
`Debuff[pet].X or Debuff[warder].X : return infos for buff from pet.`<br>
`Debuff[2899].X : return infos for buff for spell "feeblemind".`<br>
`Debuff[5682].X : return infos for buff for spell "Chains of Anguish".`<br>
`Debuff[5682 2899 887].X : return infos for buff from this bufflistid.`<br>
