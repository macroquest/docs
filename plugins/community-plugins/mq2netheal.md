# MQ2NetHeal

## Description

MQ2NetHeal was written by s0rcier \(With Major Credits A\_Druid\_00 and pinkfloydx33\) and is found in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12312).

MQ2NetHeal is used to provide more flexible way for macros, plugins and huds designers to access those information about healing and curing.  
MQ2NetHeal has three sections. NetHeal,NetCure, and NetWorst.  
\* MQ2NetHeal provides linked MQ2EQBC clients a method of sharing status and statistics.

* It makes that information available via Top-Level Object members for macro writers and HUD designers.

## Commands

### /netheal

* \*\*/netheal \[ on \|

  off \]\*\*

Turns MQ2NetHeal functionality on or off

* **/netheal \[ grab=**_**on**_**\|**_**off**_ **\]**

Receive status updates from other MQ2NetHeal-enabled clients connected to the same EQBCS server.

* **/netheal \[ send=**_**on**_**\|**_**off**_ **\]**

Broadcast status updates to the EQBCS server.

* _\*/netheal \[_ hot\_\|\_da\*&lt;/span&gt; \] \[

  Time \] \[ List \]\*\*

Labels List with 'hot' or 'da' flag for set amount of time. \(Time is in milliseconds.\)

Recommended use :: ${Target.CleanName} for single target, Or ${NetWorst.Members} for NetWorst Query.

This is here for Macro control.

### /netcure

* \*\*/netcure \[ on \|

  off \]\*\*

Toggles watching networks for afflictions

* **/netcure \[ audio=**_**on**_**\|**_**off**_ **\]**

Toggles playing audio sound.

* **/netcure \[ popup=**_**on**_**\|**_**off**_ **\]**

Toggles popup alerts.

* **/netcure \[ quiet=**_**on**_**\|**_**off**_ **\]**

Toggles sending reports to MQ2 Window.

### /networst

* \*\*/networst \[ on \|

  off \]\*\*

Toggles watching for spawns health.

* **/networst \[ audio=**_**on**_**\|**_**off**_ **\]**

Toggles playing audio sound.

* **/networst \[ popup=**_**on**_**\|**_**off**_ **\]**

Toggles popup alerts.

* **/networst \[ quiet=**_**on**_**\|**_**off**_ **\]**

Toggles sending reports to MQ2 Window.

### /worst

* '''/worsttarget \[ Query \]

Targets the spawn that matchs Query.

* '''/worstcycle \[ Query \]

Cycles to the next spawn that matchs Query

Valid Query Parameters ::

radius,hp,pet,pc,group,self,fd,da,hot,war,clr,pal,rng,shd,dru,mnk,brd,rog,shm,nec,wiz,mag,enc,bst,ber,all or \#ID\#.

hp,all and short class names could be use with % ie: shm80 war60 hp80 all99.

## Top-Level Objects

### ${NetHeal}

* **All NetHeal TLOs can be used like : ${NetHeal\[X\].Name} Or ${NetHeal.Name\[Y\]}.**

Where X could be Name/ID or Y is a Numerical Indice on Last ${NetWorst.Request}.

* [_string_]() '''${NetHeal\[X\].Name}

Returns Name.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].ID}**

Return SpawnID.

* [_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) **${NetHeal\[X\].Distance}**

Return Distance.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].PctHPs}**

Return PctHPs.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${NetHeal\[X\].Pet}**

Return This is a Pet?

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].Class}**

Return Class.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${NetHeal\[X\].Feign}**

Returns TRUE if X or Y is a NEC,SHD,MNK Class.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${NetHeal\[X\].Canni}**

Returns TRUE if X or Y is a Cannibalize Class.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].Spawn}**

Return Spawn.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].da}**

Return da timer left.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].hot}**

Return hot timer left.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].ttl}**

Return 60000. -Currently Broken July 13th, 2009

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetHeal\[X\].Updated}**

Return how old is This?

### ${NetCure}

* **Correct parameters are.**
* **self,myself,pet,warder,spellid,spellidlist,${NetBots\[\].Buff}**  
* [_string_]() **${NetCure\[X\]}**

Return list of harmfull effects.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Detrimentals}**

Return \# of Detrimental Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Counters}**

Return \# of Counters.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Cursed}**

Return \# of Curse Counters.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Diseased}**

Return \# of Disease Counters.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Poisoned}**

Return \# of Poison Counters.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].EnduDrain}**

Return \# of Endurance Drain Per Tick.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].LifeDrain}**

Return \# of Life Drain Per Tick.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].ManaDrain}**

Return \# of Mana Drain Per Tick

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Blinded}**

Return \# Blind Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].CastingLevel}**

Return \# Reducing Casting Level.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Charmed}**

Return \# Charm Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Feared}**

Return \# Fear Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Healing}**

Return \# Reducing Healing Effectiveness.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Invulnerable}**

Return \# Invulnerability Spells

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Mesmerized}**

Return \# Memsmerize Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Resistance}**

Return \# Resist Debuff Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Rooted}**

Return \# Root Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) '''${NetCure\[X\].Silenced\)

Return \# Silence Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Slowed}**

Return \# Slow Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Snared}**

Return \# Snare Spells.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].SpellCost}**

Return \# Affecting Spell Mana Cost.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].SpellSlowed}**

Return \# Slowing Casting Speed.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].SpellDamage}**

Return \# Reducing Spell Damage.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetCure\[X\].Trigger}**

Return \# That Trigger Something.

### ${NetWorst}

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetWorst.Affects}**

Returns Last \# of People in Query Range.

* [_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) **${NetWorst.Average}**

Returns HP Average People in Last Query.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetWorst.Counter}**

Return Last \# of People Matching Last Query.

* [_string_]() **${NetWorst.Members}**

Return People SpawnID List of Last Query.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${NetWorst.Request\[X\]}**

Return \# of People Matching That Query.

**Valid Query Parameters** ::

radius,hp,pet,pc,group,self,fd,da,hot,war,clr,pal,rng,shd,dru,mnk,brd,rog,shm,nec,wiz,mag,enc,bst,ber,all or \#ID\#.

hp,all and short class names could be use with % ie: shm80 war60 hp80 all99.

## See Also

* [MQ2NetBots](mq2netbots.md)
* [Plugins](../../documentation/macroquest2-plugins.md)
* [Top-Level Objects](../../data-types-and-top-level-objects/top-level-objects/)

