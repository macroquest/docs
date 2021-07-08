# DRShmbot

## dRShmbot

Author: DeathlyRanja Alias: dR~ Date: 12/05/2006

Credit where its due:

`Basis of this script is Version: v0.5c by Hubba`  
`Shambot Version 1.0c by Ranma`  
`Version 2.0c by thread_001`  
`Version 3.0+ to 3.3 by IonCache`  
`Version 3.4+ to Current, By DeathlyRanja`

dRShmbot is a fairly complex Shaman macro. It is not finish or in any way finalized, so many more updates will come.

`This macro offers:`  
`Intelligent Healing Code`  
`Spell Gem Optimization`  
`Dynamic Mana Preservation`  
`Mob Debuffing(Malo/Slow/Cripple/Root/Nuke/Dot)`  
`Self/Group Buffing(Panther/Avatar/Buffs)`  
`TSS Regen Support`  
`User Settings for almost all variables to customize`  
`Pet Routines`

## Request Space

This area is reserved for user requests. Feel free to hit the edit button to your right and add to this. I will add as I can.

Requesting links for the below listed .inc - Could not find them with searches on MQ2 forums or wiki.

## To Do List

`To Do List:`  
`Fix 'Spell Worn Off' for dots,buffs,debuffs,etc.`  
`Add Command Queuing`  
`Add Flee Routine`  
`Fix Buff Stacking Issues and checks upon casting`  
`Fix Healing Interrupts -- currently removed`  
`Clean up code`  
`Add GoM GoRM events and cast preferences during those events`

`Correct targetting issues with detrimental and beneficial spells.`  
`Add a new targetting array`  
`Add INI support`

### Future to do List

Specific Buffing Instructions Rework the targeting Sub Routine Add more targets to the targetting array and allow for user specified amount of targets to track

## How To Use

To use this macro, you must have these files in your macros directory: DRShmbot.mac dREvents.inc dRSubs.inc

To start the macro, type: /mac DRShmbot.mac \_\_

Tank Name and Master Name are optional. They are **NOT** required but must be set in the INI for the bot to function correctly if not provided.

The macro will create an INI file for you to customize called, dR\_ToonsName.ini, in your macro directory. \(Ex. dR\_Bobshaman.ini\)

After the INI file is created, it will end the macro and you **MUST** edit the new INI file. Then you can restart the macro\(You will not need to edit it after it has been set once unless you need to change a setting.

This macro **DOES NOT REQUIRE ANY PLUGIN** but it will use MQ2EQBC if you want it to. However, there is no support for it on this macro at this time.

## Commands and Aliases

None at this time.

## Dynamic Mana

More to be posted later.

## Spell Gem Optimization

Add to your macro before main loop:

`/declare numGem int outer`  
`/declare OWgem int outer`  
`/call GemOpt`

#### Subs for use within macro

_/call GemMem ${SpellGem} ${SpellName} ${SpellGemState} ${MOWState}_

`ex. /call GemMem ${NukeGem} ${Nuke} ${NukeStatus} TRUE`  
`/call GemMem 4 "Ice Spear of Solist" TRUE FALSE`  
`/call GemMem 0 "Complete Healing" FALSE ${CHAlwaysOW}`  
`/call GemMem 9 "Ancient: Hallowed Light" ${KeepAH} ${AHOverWrite}`

* SpellNameHere must be a string, SpellGemHere must be a integer, SpellGemState must be TRUE/FALSE
  * FALSE means that the spell will stay until a spell is memmed over top of it within the macro by the user or

    manually deleted.

  * TRUE flags the gem as switchable. Spells will be memmed to the least used switchable slot
* SpellGemHere
  * when it equals 0, means that the sub will memorize into the first switchable gem it finds that is available.
  * If no gems are available, it finds the switchable gem that has not been cast in the longest time
  * Each timer for each switchable gem is set to a default of five minutes. Lowest timer will be overwritten, or

    first in list if multiple timers are at 0
* MOWState is just a TRUE/FALSE constant that tells the sub to overwrite it if no gems can be switched and you don't

  want to use the OWgem

**IF you want the timer function to work correctly, you must add this line directly after casts in your macro**

`/if (${Macro.Return.Equal[CAST_SUCCESS]}) /call GemTimer ${Me.Gem[<${SpellThatWasCast}>]}`

_/call GemEdit ${SpellName - OR - SpellGem}_

`ex. /if (${SpGem[1,2]}) /call GemEdit 1`  
`/call GemEdit "Complete Healing"`  
`/call GemEdit ${QuickHeal}`  
`/if (${Nuke.Equal[${SpGem[${NukeGem},1]}]}) /call GemEdit ${NukeGem}`

* This sub is used to switch states of memorized spells or spell gems. IF the spell name isnt found, no change will

  occur. This state will be changed next time a gem will be memorized, therefore no need to mindlessly call GemFind

## dRShmbot Ini Settings

_**Sample Ini**_

`[DRShmBot]`  
`UseMq2EQBC=FALSE(TRUE if you want macro to use MQ2EQ Box Chat Plugin) -- You must also have the EQBCS server running.`

`[General]`  
`UseMount=FALSE(TRUE if you want to use a mount)`  
`MountItem=NULL(Set this to the name of the item you wish to use. Ex. MountItem=Small Black Drum)`  
`MSRL=##(Set this value to the percent of Mana that bot will sit at when not in combat, TSS regen is active and mana is below the`  
`set value)`  
`HSRL=##(Set this value to the percent of HP that bot will sit at when not in combat, TSS regen is active and HP is below the set`  
`value)`  
`UseCanniAA=TRUE(Set to False if you do not wish to use canni AA, or do not have it yet.)`  
`Verbose=FALSE(Set to TRUE if you want the bot to announce heals/debuffs/etc into group/channel.)`  
`DoLoot=FALSE(Set to TRUE if you want the bot to loot for you)`  
`AutoFollowDist=##(Set this value to distance that bot will stay within when following its AutoFollow Target)`

`[DynMana]`  
`DynManaTimer=50(This value is the time in deciseconds between mana checks before making changes to HP Stops/Starts)Default is`  
`50dS or 5 Seconds`  
`PercentCarry=60(This value is the percentage of carry-over from 1 Mana Tier to another. Do not alter this unless you understand`  
`what you are doing. Read Dynamic Mana section if you want to further understand this function.)`  
`DetriHPIncrease=20(Set this to the percentage that you want detrimental HP Increases to increase by. Ex. SPantherHP=70 but`  
`increases by 20% on each tier.)`  
`DetriHPDecrease=15(Same as above)`  
`BeneHPIncrease=15(etc)`  
`BeneHPDecrease=10(etc)`

`[PrimarySpells]`  
`SwapGem=9(Set this to the gem number that you want to use for swapping spells. This may be removed in the near future with`  
`the implementation of GemOpt.inc)`  
`HP2MP=Ancestral Bargain Rk. II(Set this to the Canni spell you want to use. Quotes are not needed.)`  
`HP2MPGem=1(Set this to the spell gem you want Canni to use.)`  
`Slow=Balance of Discord(refer above)`  
`SlowGem=2(refer above)`  
`Malo=Malosinise(refer above)`  
`MaloGem=3(refer above)`  
`DoTOne=Juju(refer above)`  
`DoTOneGem=4(refer above)`  
`Nuke=Sting of the Queen(refer above)`  
`NukeGem=5(refer above)`  
`QuickHeal=Ahnkaul's Mending(refer above)`  
`QuickHealGem=6(refer above)`  
`HealOverTime=Halcyon Breeze(refer above)`  
`HoTGem=7(refer above)`  
`DoTTwo=Ahnkaul's Spear of Venom(refer above)`  
`DoTTwoGem=8(refer above)`  
`HP2MPState=FALSE(NEW VARS) -- FALSE means that the spell will not be switched out when another spell is called for memorization. TRUE means that if`  
`the another spell is called for memorization, and there isnt a free gem available, the new spell will be memmed over`  
`top of this one.`  
`SlowState=FALSE`  
`MaloState=TRUE`  
`DoTState=TRUE`  
`NukeState=TRUE`  
`QuickHealState=FALSE`  
`HoTState=FALSE`  
`DoTTwoState=TRUE`

`SecondarySpells`  
`Pet=Kyrah's Faithful`  
`Cripple=Crippling Spasm`  
`Root=Greater Immobilize`  
`Panther=Spirit of the Leopard`  
`GroupPanther=Talisman of the Panther Rk. II`  
`Avatar=Ferine Avatar`  
`GroupAvatar=Champion`  
`Haste=Swift like the Wind`  
`GroupHaste=Talisman of Celerity`  
`Focus=Dire Focusing`  
`GroupFocus=Talisman of the Dire`  
`Charisma=Unfailing Reverance`  
`Dexterity=Mortal Deftness`  
`GroupDex=Talisman of the Raptor`  
`Strength=Preternatural Foresight`  
`GroupSTR=Talisman of Foresight`  
`Agility=Preternatural Foresight`  
`GroupAGI=Talisman of Foresight`  
`Stamina=Spirit of Fortitude`  
`GroupSTA=Talisman of Fortitude`  
`Regen=Spirit of the Stoic One`  
`GroupRegen=Talisman of the Stoic One`  
`Primal=Primal Essence`  
`PrDrResist=Protection of Wishka Rk. II`  
`ArmorClass=Ancestral Bulwark`  
`Movement=Spirit of Bih'li`  
`Levitate=Levitation`  
`Invis=Spirit Veil`  
`Shrink=Shrink`  
`GroupShrink=Tiny Terror`  
`Grow=Grow`  
`SeeInvis=Acumen`  
`Gate=Gate`  
`Food=Summon Food`  
`Drink=Summon Drink`

`[CombatVars]`  
`AssistRange=100(Set this to the distance MA must within for bot to assist for target)`  
`StartCombatHP=98(Set this to the distance target npc must be within to start combat subs)`  
`StartDoTHP=0(Set this to the value that mob HP must be under to start function)`  
`EndDoTMP=100(Set this to the value that bot mp must be above in order to do this function)`  
`StartRootHP=0(Set this to the value that mob HP must be under to start function)`  
`EndRootMP=100(Set this to the value that bot mp must be above in order to do this function)`  
`StartNukeHP=90(Set this to the value that mob HP must be under to start function)`  
`EndNukeMP=50(Set this to the value that bot mp must be above in order to do this function)`  
`EndPantherHP=100(Set this to the value that target hp must be above in order to do this function)`  
`StartSitMP=0(Set this to the percent of MP bot must be below to sit)`  
`EndBuffMP=100(Set this to the percent of MP bot must be above to buff)`  
`StopCanniHP=3500(Set this to the amount of HP bot must be above to canni)`  
`AssistDelay=3(Set this value to the delay in deciseconds before bot will assist main assist to get a target)`  
`TimetoRecast=5s(Set this to a value in seconds that bot will continue to try to recast a spell)`

`Healing`  
`UseQuickHeals=TRUE`  
`UseHealOverTime=TRUE`  
`UseGroupHoT=FALSE`  
`DoHealTank=TRUE`  
`DoHealGroup=TRUE`  
`DoHealPets=FALSE`  
`HealPriority=2(Healing modes -- 0 = Default, heal normally /\/\ 1 = Tank Priority, heal tank before all others /\/\`  
`2 = Tank and Shaman Priority, heal self and tank before all others)`  
`StartGroupHoTHP=0(Group HoT -- integer is the average hp level of the group)`  
`CasterHealHP=50(start heal on class type when hp is below value)`  
`CasterHoTHP=60`  
`MeleeHealHP=40`  
`MeleeHoTHP=60`  
`TankHealHP=50`  
`TankHoTHP=70`  
`PetHealHP=30`  
`PetHoTHP=50`  
`SelfHealHP=50`  
`SelfHoTHP=60`

`[Debuff]`  
`UseMalo=TRUE`  
`UseSlow=TRUE`  
`UseCripple=FALSE`  
`SlowOnlyOnce=FALSE(bot will only attempt to slow one time if TRUE)`  
`MaxSlowAttempts=3`  
`UseRoot=FALSE`  
`UseDots=FALSE`  
`UseNukes=TRUE`

`[Buffing]`  
`UseBuffs=FALSE`  
`UseRebuffs=TRUE`  
`UsePanther=FALSE`  
`UseGroupPanther=FALSE`  
`PantherGroup=FALSE`  
`PantherPets=FALSE`  
`UseAvatar=TRUE`  
`UseGroupAvatar=FALSE`

`[Pet-Familiar]`  
`UsePet=TRUE`  
`BuffMyPet=FALSE`  
`BuffOtherPets=FALSE`

