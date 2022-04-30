# MQ2Debuffs

## Description

This plugin is designed to help with curing detrimental effects. It is used to reports harmful effects, number of curse/disease/poison counters and various other detrimentals.

Author: PinkFloyd33 Author: s0rcier Version: 1.2 Date: 20061223 v2.0 - Eqmule 07-22-2016 - Added string safety.

## MQ2Debuffs

MQ2Debuffs was posted to the VIP section of MQ2 by pinkfloydx33 you can read the thread by following [This Link.](https://macroquest.org/phpBB3/viewtopic.php?f=50&t=13495&hilit=debuff) \(VIP REQUIRED\)

Updated Apr 03, 2016 by Trevyn [here](https://macroquest.org/phpBB3/viewtopic.php?f=50&t=13495&hilit=debuff&start=15) Updated July 22, 2016 by EQMule: included in MQ2Update

## TLO

`Debuff (bool True if you have debuffs on that have counters on them, false if not)`  
`Debuff.Poisoned (int # of poison counters on you)`  
`Debuff.Diseased (int # of disease counters on you)`  
`Debuff.Cursed (int # of curse counters on you)`  
`Debuff.Corrupted (int # of corruption counters on you)`  
`Debuff.Poisons (int # of poison spells affecting you)`  
`Debuff.Diseases (int # of disease spells affecting you)`  
`Debuff.Curses (int # of curse spells affecting you)`  
`Debuff.Corruptions (int # of corruption spells affecting you)`  
`Debuff.Count (int # of debuffs that need cured, does not include snare)`  
`Debuff.HPDrain (int Amount of HP you are losing per tick from debuffs. This value is POSITIVE)`  
`Debuff.HPDrain[X] (int X= Disease, Poison, Curse, All: Number of specific counters effecting HP)`  
`Debuff.ManaDrain (int Amount of Mana you are losing per tick from debuffs. This value is POSITIVE)`  
`Debuff.ManaDrain[X] (int X= Disease, Poison, Curse, All: Number of specific counters effecting Mana)`  
`Debuff.EnduranceDrain (int Amount of Endurance you are losing per tick from debuffs. This value is POSITIVE)`  
`Debuff.EnduranceDrain[X] (int X= Disease, Poison, Curse, All: Number of specific counters effecting Endurance)`  
`Debuff.Slowed (bool True if you are Slowed (melee attacks), False if not)`  
`Debuff.SpellSlowed (bool True if you are SpellSlowed (spell haste reduction), False if not)`  
`Debuff.Snared (bool True if your are Snared, False if not)`  
`Debuff.ManaCost (bool True if your Spell Mana Cost has been raised, False if not)`  
`Debuff.CastingLevel (bool True if your Effective Casting Level has been reduced, False if not)`  
`Debuff.HealingEff (bool True if your Healing Effectiveness has been reduced, False if not)`  
`Debuff.SpellDmgEff (bool True if your Spell Damage Effectiveness has been reduced, False if not)`  
`Debuff.Blind (bool True if you are blind)`  
`Debuff.Charmed (bool True if you are charmed)`  
`Debuff.Feared (bool True if you are feared)`  
`Debuff.Silenced (bool True if you are silenced)`  
`Debuff.Invulnerable (bool True if you are invulnerable)`  
`Debuff.Detrimentals (bool True if you have any detrimental effects on you)`  
`Debuff.Counters (int # of poison/disease/curse/corruption counters on yourself)`  
`Debuff.Rooted (bool True if you are rooted)`

`The TLO has been enhanced, revamped, recored, to be able to get Debuff Informations others then selfbuff.`

`Debuff.X or Debuff[self].X or Debuff[myself].X : return infos for buff from self.`  
`Debuff[pet].X or Debuff[warder].X : return infos for buff from pet.`  
`Debuff[2899].X : return infos for buff for spell "feeblemind".`  
`Debuff[5682].X : return infos for buff for spell "Chains of Anguish".`  
`Debuff[5682 2899 887].X : return infos for buff from this bufflistid.`
