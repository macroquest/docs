# GemOpt.inc

## Spell Gem Optimization Include

### VIP ONLY

Welcome to the Wiki for GemOpt.inc by DeathlyRanja

This wiki will cover the little knowledge needed to run a macro with this include.

## What does this do?

This include file allows the macro to control the use of spell gems and how they are memorized. The include will monitor the spell gems and user setting emOpt -- This function sets up the include file and has no user interaction at all except in the beginning of the macro. This sub/function must be called before your main loop.

GemMem -- Memorizes the spell, remembers spell data, recognizes how long the spell has been memorized and if it has been flagged by the user as a gem that is allowed to be switched out. GemMem may call GemDMem if there is a spell in the slot and the spell gem is switchable or the user wants to overwrite the gem that is there anyway.

GemDMem -- Simple ... It dememorizes the spell in whatever slot chosen(1-9)

GemEdit -- This sub routine takes the spell name or gem-number and switches it from switchable/not-switchable to not-switchable/switchable

GemTimer -- A subroutine to be called after spell casts if you want the include to monitor the usage of the spell. Spells often will not be replaced by spells that aren't cast as often.

GemFind -- A subroutine to scan the spell information, stored user-responses and available/used gems to find a suitable gem for memorization.

Putting all these functions together, this include micromanages the use of spell gems within a routine. Instead of using something like /call cast 4 "Shrink" 5s, You can use this instead /if (${Me.Gem[${ShrinkSpell}\]}) /call cast ${Me.Gem\[${ShrinkSpell}]} ${ShrinkSpell} 5s.

## Why use this?

As said before, this can allow you to dynamically assign spell gems to make a macro more flexible. Is it easier to code and use, probably not... for the moment. Can it be improved, YES!

This isn't for the weak of heart. This include will allow you to do really awesome things without alot of effort on your part.

## Usage

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

## Code

If you want access to the code for this include, you must donate to the dev's. They do alot and require nothing. If you can't get $10 out of your budget, you should sell your plat, your soul or wife/husband. If you get the code from someone else and your not a VIP, may your soul rot in hell while cherubs mutilate your unidentifiable corpse.

If you paid, you may of course just follow this link!!

[Spell Gem Optimization Include](https://macroquest2.com/phpBB3/viewtopic.php?t=13340) Note: This currently goes to the DRShmBot Page

