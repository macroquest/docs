## Description

MQ2NetHeal was written by s0rcier (With Major Credits A_Druid_00
and pinkfloydx33) and is found in the VIP forums
[here](https://macroquest2.com/phpBB3/viewtopic.php?t=12312).  
  
MQ2NetHeal is used to provide more flexible way for macros, plugins and huds designers to access those information about
healing and curing.  
MQ2NetHeal has three sections. NetHeal,NetCure, and NetWorst.  
\* MQ2NetHeal provides linked MQ2EQBC clients a method of sharing status and statistics.

-   It makes that information available via Top-Level Object members for macro writers and HUD designers.

## Commands

### /netheal

-   **<span style="color:red">/netheal</span> \[ <span style="color:blue">on</span> \|
    <span style="color:blue">off</span> \]**

  
Turns MQ2NetHeal functionality on or off

-   **<span style="color:red">/netheal</span> \[ <span style="color:blue">grab</span>=*on*\|*off* \]**

  
Receive status updates from other MQ2NetHeal-enabled clients connected to the same EQBCS server.

-   **<span style="color:red">/netheal</span> \[ <span style="color:blue">send</span>=*on*\|*off* \]**

  
Broadcast status updates to the EQBCS server.

-   **<span style="color:red">/netheal</span> \[ <span style="color:blue">*hot*\|*da*</span> \] \[
    <span style="color:green">Time</span> \] \[ <span style="color:purple">List</span> \]**

  
Labels List with 'hot' or 'da' flag for set amount of time. (Time is in milliseconds.)

Recommended use :: ${Target.CleanName} for single target, Or ${NetWorst.Members} for NetWorst Query.

This is here for Macro control.  

### /netcure

-   **<span style="color:red">/netcure</span> \[ <span style="color:blue">on</span> \|
    <span style="color:blue">off</span> \]**

  
Toggles watching networks for afflictions

-   **<span style="color:red">/netcure</span> \[ <span style="color:blue">audio</span>=*on*\|*off* \]**

  
Toggles playing audio sound.

-   **<span style="color:red">/netcure</span> \[ <span style="color:blue">popup</span>=*on*\|*off* \]**

  
Toggles popup alerts.

-   **<span style="color:red">/netcure</span> \[ <span style="color:blue">quiet</span>=*on*\|*off* \]**

  
Toggles sending reports to MQ2 Window.  

### /networst

-   **<span style="color:red">/networst</span> \[ <span style="color:blue">on</span> \|
    <span style="color:blue">off</span> \]**

  
Toggles watching for spawns health.

-   **<span style="color:red">/networst</span> \[ <span style="color:blue">audio</span>=*on*\|*off* \]**

  
Toggles playing audio sound.

-   **<span style="color:red">/networst</span> \[ <span style="color:blue">popup</span>=*on*\|*off* \]**

  
Toggles popup alerts.

-   **<span style="color:red">/networst</span> \[ <span style="color:blue">quiet</span>=*on*\|*off* \]**

  
Toggles sending reports to MQ2 Window.  

### /worst

-   '''<span style="color:red">/worsttarget</span> \[ <span style="color:blue">Query</span> \]

  
Targets the spawn that matchs Query.

-   '''<span style="color:red">/worstcycle</span> \[ <span style="color:blue">Query</span> \]

  
Cycles to the next spawn that matchs Query

Valid Query Parameters ::

  
<span style="color:red">radius,hp,pet,pc,group,self,fd,da,hot,war,clr,pal,rng,shd,dru,mnk,brd,rog,shm,nec,wiz,mag,enc,bst,ber,all
or #ID#.</span>

<span style="color:blue">hp,all and short class names could be use with % ie: shm80 war60 hp80 all99.</span>

## Top-Level Objects

### ${NetHeal}

-   **All NetHeal TLOs can be used like : ${NetHeal\[X\].Name} Or ${NetHeal.Name\[Y\]}.**

  
Where X could be Name/ID or Y is a Numerical Indice on Last ${NetWorst.Request}.

-   *[string](../data-types/datatype-string.md)* '''${NetHeal\[X\].Name}

  
Returns Name.

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].ID}**

  
Return SpawnID.

-   *[float](../data-types/datatype-float.md)* **${NetHeal\[X\].Distance}**

  
Return Distance.

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].PctHPs}**

  
Return PctHPs.

-   *[bool](../data-types/datatype-bool.md)* **${NetHeal\[X\].Pet}**

  
Return This is a Pet?

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].Class}**

  
Return Class.

-   *[bool](../data-types/datatype-bool.md)* **${NetHeal\[X\].Feign}**

  
Returns TRUE if X or Y is a NEC,SHD,MNK Class.

-   *[bool](../data-types/datatype-bool.md)* **${NetHeal\[X\].Canni}**

  
Returns TRUE if X or Y is a Cannibalize Class.

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].Spawn}**

  
Return Spawn.

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].da}**

  
Return da timer left.

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].hot}**

  
Return hot timer left.

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].ttl}**

  
Return 60000. -Currently Broken July 13th, 2009

-   *[int](../data-types/datatype-int.md)* **${NetHeal\[X\].Updated}**

  
Return how old is This?

### ${NetCure}

-   **Correct parameters are.**
-   **self,myself,pet,warder,spellid,spellidlist,${NetBots\[<character>\].Buff}**  
      

<!-- -->

-   *[string](../data-types/datatype-string.md)* **${NetCure\[X\]}**

  
Return list of harmfull effects.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Detrimentals}**

  
Return # of Detrimental Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Counters}**

  
Return # of Counters.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Cursed}**

  
Return # of Curse Counters.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Diseased}**

  
Return # of Disease Counters.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Poisoned}**

  
Return # of Poison Counters.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].EnduDrain}**

  
Return # of Endurance Drain Per Tick.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].LifeDrain}**

  
Return # of Life Drain Per Tick.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].ManaDrain}**

  
Return # of Mana Drain Per Tick

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Blinded}**

  
Return # Blind Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].CastingLevel}**

  
Return # Reducing Casting Level.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Charmed}**

  
Return # Charm Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Feared}**

  
Return # Fear Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Healing}**

  
Return # Reducing Healing Effectiveness.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Invulnerable}**

  
Return # Invulnerability Spells

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Mesmerized}**

  
Return # Memsmerize Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Resistance}**

  
Return # Resist Debuff Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Rooted}**

  
Return # Root Spells.

-   *[int](../data-types/datatype-int.md)* '''${NetCure\[X\].Silenced)

  
Return # Silence Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Slowed}**

  
Return # Slow Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Snared}**

  
Return # Snare Spells.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].SpellCost}**

  
Return # Affecting Spell Mana Cost.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].SpellSlowed}**

  
Return # Slowing Casting Speed.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].SpellDamage}**

  
Return # Reducing Spell Damage.

-   *[int](../data-types/datatype-int.md)* **${NetCure\[X\].Trigger}**

  
Return # That Trigger Something.

### ${NetWorst}

-   *[int](../data-types/datatype-int.md)* **${NetWorst.Affects}**

  
Returns Last # of People in Query Range.

-   *[float](../data-types/datatype-float.md)* **${NetWorst.Average}**

  
Returns HP Average People in Last Query.

-   *[int](../data-types/datatype-int.md)* **${NetWorst.Counter}**

  
Return Last # of People Matching Last Query.

-   *[string](../data-types/datatype-string.md)* **${NetWorst.Members}**

  
Return People SpawnID List of Last Query.

-   *[int](../data-types/datatype-int.md)* **${NetWorst.Request\[X\]}**

  
Return # of People Matching That Query.

**Valid Query Parameters** ::

  
<span style="color:red">radius,hp,pet,pc,group,self,fd,da,hot,war,clr,pal,rng,shd,dru,mnk,brd,rog,shm,nec,wiz,mag,enc,bst,ber,all
or #ID#.</span>

<span style="color:blue">hp,all and short class names could be use with % ie: shm80 war60 hp80 all99.</span>

## See Also

-   [MQ2NetBots](mq2netbots.md)
-   [Plugins](../documentation/macroquest2-plugins.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)


