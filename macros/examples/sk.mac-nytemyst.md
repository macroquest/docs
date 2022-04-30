# Sk.mac - nytemyst

## Forum Link

* [sk.mac - Nytemyst](https://macroquest.org/phpBB3/viewtopic.php?t=16348)

## Description

This macro is mainly for high level shadow knights, but possible for low levels to use. this macro is designed with the toon having the ROF Expansion. This macro is not meant to go out and pull but instead more like "guard" the camp that you're currently at. Will attempt to use aggro spells and range items to aggro mobs from a distance that you have set.

## Required Plugins

* [MQ2Exchange](https://macroquest.org/phpBB3/viewtopic.php?t=16436)
* [MQ2MoveUtils](https://macroquest.org/phpBB3/viewtopic.php?t=11732)
* [MQ2Melee](https://macroquest.org/phpBB3/viewtopic.php?t=12779) This one is optional and not really needed but

  the macro will not do little things like bash,or put pet on hold. You will need to turn off all stick settings on

  the plugin as they will interfere with the macro.

* [MQ2BagWindow](https://macroquest.org/phpBB3/viewtopic.php?f=50&t=17035&hilit=mq2bagwindow) This is required to

  cast items in bags without having the bag opened.

## Required Include Files

General.inc - All the macros made/updated by me will use this include. Contains common features all the macros use to ease in updating functions and features to all the macros instead of updating each macro seperatly. Will be included with the zip.

* [Spell\_Routines.inc](https://macroquest.org/phpBB3/viewtopic.php?t=11656)
* [Ninjadvloot.inc](https://macroquest.org/phpBB3/viewtopic.php?t=12578&postdays=0&postorder=asc&start=0)

If you don't want to use Ninjadvloot.inc you can comment out or delete these lines.

`#include ninjadvloot.inc - Line 11`  
`/call SetupAdvLootVars- Line 35`  
`/if (${DoLoot} && !${Me.Moving} && !${Me.Invis}) /call LootMobs - Line 54`

* [AAPurchase.inc](https://macroquest.org/phpBB3/viewtopic.php?f=49&t=15824)

If you don't want to use AAPurchase.inc You can comment out or delete these lines.

`#include AAPurchase.inc - Line 10`  
`/call AAInit - Line 37`

## Updates

## Commands

* /radius \# - Sets the distance for checking mobs
* /aggro On/Off - If this is set to off then the macro will not aggro anything and just do buffs.
* /usepet On/Off - If this is on, then the macro will create a pet and haste it.
* /dps On/Off - If this on then it will not cast any aggro spells or try to taunt and just do dps spells. Must set an

  MA on this mode.

* /ma name - This changes the ma to the person designated when in dps mode.
* /sticksetting \# - This changes the stick range you will stick at. DPS MODE ONLY.
* /assistdistance \# - This changes how close the mob must be before you engage. DPS MODE ONLY
* /assistat \# - This changes at what % of health before engaging. DPS MODE ONLY
* /doloot On/Off - This changes where you will loot corpses or not.
* /checknames On/Off - This changes whether you want to check for a name or a mezz immuned mob that went in to camp

  while currently fighting something else. If it's on it will change target to the name or mezzimmune. If it's off it

  won't target the name or mezzimmune until the current target is dead.

* /Dot On/Off - Turns dotting on or off.
* /leash On/Off - If this is set to off the toon will not leash back to the current stake point.
* /leashlength \# - This changes how far away you have to be from the stake to leash back.
* /autoadjustexp On/Off - This turns on or off whether you want it to monitor your XP level and switch between Level

  and AA.

* /maintexplvl \# - This changes the amount of Level xp that is required before the toon is automatically switched over

  to AA - Autoadjustexp Open is require to be turned on.

* /autosit On/Off - Turns auto sitting on or off.

## Ini Samples

`NameList`  
`[Discord_raid]`  
`Name=|Pallorax the soul slayer|a gelidran rift slave|a pyrilen rift slave|Venom Lord Ksathrax|Mindshear Acolyte|Venomous projection|a venom protector|Mindshear Avatar|`

`MezzImmuneList`  
`[korascian_raid]`  
`MezzImmune=|a crystalline nexiont|`

`IgnoreList`  
`[Oldcommons]`  
`Exclude=|Peron ThreadSpinner|Innkeep Dolman|Innkeep Olissa|Innkeep Redthorn|`

Tip for adding mobs into this list without manually into the INI. Create a hotkey like so.

`/named ${Target.CleanName}`  
`/exclude ${Target.CleanName}`  
`/mezzimmune ${Target.CleanName}`

This allows you to add to those lists for any mob you're target while the macro is running.

-Note No spell below requires you to put in the Ranks unless it's mentioned to do so. With the exception of buffs no spell is membed before hand. You must have it already memed if you want to use it.

`SK_Bobby.ini`  
`[Settings]`  
`RangeItem=Huntsman's Ethereal Quiver - This is the item that does the actually summoning`  
`RangeItemSummon=Ethereal Arrow - This is the item that is actually summoned.`  
`MobRadius=10 - How far you want to look for mobs.`  
`Aggro=0 - Whether to aggro mobs or not.`  
`ItemShrink=Earring of Diminutiveness - Item you use to shrink yourself.`  
`CheckNames=1 - If set to 0 the macro will not switch targets if a name, or mezzimmune mob comes into camp after you already are fighting a mob.`  
`UsePet=0 - Whether to summon a pet.`  
`DpsMode=0 - If set to 1 will turn on DPS Mode. In Dps mode it will assist another toon and not try to aggro and only do dps type abilities.`  
`MainAssist=somebody - Main person you will assist while in DPS Mode`  
`SecondAssist=somebody - If main person is not in zone or dead.`  
`TrippleAssist=somebody - If second person is not in zone or dead.`  
`EventsMaster=somebody - If you are using my events.inc. This is the person you will send a tell to saying you just received and emote. This is meant for raids.`  
`StickSetting=35 - Sets how close you want to stick to the mob - DPS MODE ONLY`  
`AssistDistance=80 - How close the mob must be before you will assist - DPS MODE ONLY`  
`AssistAt=97 - What % of HP the mob must before you attack. - DPS MODE ONLY`  
`UseIRC=0 - Whether to join IRC or not.`  
`DoLoot=0 - Turns on autolooting if you are using ninjaadvloot.inc`  
`DoDot=0 - Turns Dotting on or off`  
`NumOfDots=1 - How many Dots you will be casting.`  
`[Spells]`  
`SteelyStance=Steely Stance - Temporary HP buff you want to cast during combat.`  
`SkinBuff=Malarian Skin - Skin proc buff you want to cast during combat.`  
`WithStand=WithStand - Withstand style Disc to use right before mob comes into camp.`  
`BladeStrike=Gouging Blade - Blade strike style disc to use during combat.`  
`CrimesonBlade=Crimson Blade - Crimson Blade style disc to use during names.`  
`DefensiveDisc=Malarian Carapace - Defensive disc to use when fighting a name.`  
`HateSpell1=Terror of Jelvalak - Main hate spell and hate spell used to do initial aggro.`  
`HateSpell2=Terror of the Soulbleeder - Second hate spell.`  
`HateSpell3=Terror of Vergalid - 3rd Hate spell.`  
`AeHateSpell1=Burst of Spite - Main AE aggro spell.`  
`AeHateSpell2=Revile - Second AE Aggro spell.`  
`AeHateSpell3=Vilify - Third AE Aggro spell.`  
`AeHateSpell4=Dread Gaze - Fourth AE aggro Spell.`  
`NukeSpell1=Malarian Spear - Main Nuke Spell.`  
`NukeSpell2=Rotmarrow Spear - Second Nuke Spell.`  
`ChallengeSpell=Charge for Power - Spell used For temporary aggro and AC`  
`ChallengeSpellRecourse=Charge for Power Recourse rk. ii - This is the resource you get when you challengespell is successful. You must put the RANK here if version 2 or 3.`  
`LifeTapSpell1=Touch of Tharoff - Main lifetap spell`  
`LifeTapSpell2=Touch of Kildrukaun - Second Lifetap spell`  
`LifeTapSpell3=Touch of Severan - Third lifetap spell`  
`DireImplication=Dire Implication - Emergency Lifetap Spell`  
`HpTapSpell=Touch of Lanys - Lifetap spell that increases your aggro and Max Health Temporarily.`  
`HpTapSpellRecourse=Gift of Lanys - The resource you receive by casting your HpTapSpell. You must put in the RANK here if version 2 or 3`  
`BondSpell=Bond of Laarthik - LifeTap Dot Spell.`  
`BondSpellRecourse=Bond of Laarthik recourse rk. iii - Resource you receive by casting your Lifetap Dot. You must put in the RANK here if version 2 or 3.`  
`ManaTapSpell1=Laarthik's bite - Main Manatap Spell`  
`ManaTapSpell2=Ancient: Bite of Muram - Second ManaTap Spell`  
`PetSpell=Minion of Sebilis - Spell to summon your pet.`  
`PetSpellHaste=Gift of Sathir - Spell to haste your pet.`  
`RespiteDisc=Rest - Disc using when low on endurance`  
`Dot1=Changeme - Name of the Dot you will be casting`  
`BuffGem=12 - Gem where you want all your buff spells to use when buffing`  
`[SelfBuffs]`  
`NumSelfBuff=1 - Amount of self buffs you will be casting`  
`SelfBuff1=ChangeMe - Name of the Spell,item, or alt.`  
`SelfType1=ChangeMe - can gem1,1,alt,or item`  
`[ITEMS]`  
`ClickyBP=Elegant Soulrender Breastplate - The name of the Group or Raid BP for that expansion.`  
`[GeneralSettings]`  
`DoLeash=1 - Turns leashing on or off.`  
`Leashlength=25 - How far away from the stake you must be before it leashes back.`  
`AutoExpAdjust=1 - Whether to switch to AA or level automatically.`  
`MaintExpLvl=20 - What % of level XP before switching to AA`  
`MaxLevel=100 - Max level the toon can reach`  
`MasterList=NULL - What toons are allowed to send the bot a tell with a / command such as /say hi and the bot will do the command.`  
`Autosit=1 - Turns auto sitting on or off.`  
`RelayTells=0 - Turns relaying tells to BC on or of`  
`AutoBalance=0 - Turns autobalancing of a group of Mobs HP - DPS MODE ONLY - Leave off currently doesn't work.`  
`AutoBalanceHPCheck=5 - % of health differemce before considered unbalanced.`  
`DoFood=0 - Turns summoning turkey or milk on or off.`

## Bot Flow

After starting the macro if you do not have Aggro turned on or dps mode turned on it will just buff itself. If you have aggro on it's first going to look for mobs in a 50 radius range. It will automatically choose a name,mezzimmune, or the lowest HP mob within that radius.

If there are no mobs in a 50 range radius then the macro will check if it has rez affects on. If so the macro will just buff itself and not try to aggro anything beyond the 50 radius. For mobs beyond the 50 radius it will look for mobs at a distance you set under "Mobradius". It will grab the highest level ,Named,mezzimmune mob and work it's way down.

Macro does the initial aggro in 2 ways and both will be attempted to use. Will try to cast the first hate spell you have set in the ini and will try to use any range item like bow and arrow. If a mob goes into camp before you pulled enters camp it will switch to mob that's in camp. If the mob takes more then 20 seconds the camp the macro will clear the target, ignore that mob from pulling for 60 seconds and look for something else. If that mob eventually makes it into camp it will aggro the mob whether the timer is up or not.

Once mob in camp it will stick to the mob. Use numerous Discs and spells such as demand for power,withstand,bite aa. Will constantly monitor health and will do lifetaps to keep it's self up. Will also nuke and dot. If it encounters a name it will using all tanking disciplines as well as dps disciples that stack with the tanking ones. Will use AA snare on any mobs that are trying to flee. Will keep any Skin or steely stance buffs up during combat.

If more then one mop is in camp it will use ae aggro. If more then 3 mobs in camp and the health drops to low it will attempt to use deflection disc.

