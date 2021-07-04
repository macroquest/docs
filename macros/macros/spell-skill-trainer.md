# Spell Skill Trainer

This macro was originally published in the Macro Depot 3.0 Forum, and has been successfully used to max out spell casting skills \(abjuration, alteration, channeling, conjuration, divination, evocation, meditation and specializations\).

**Instructions**

Paste this code into a file called practice.mac in your **\macros** directory.

Memorize the spells you wish to cast to work on skill. I recommend using the highest level spell with the least amount of mana. I also suggest acquiring the following buffs from an enchanter: clarity \(or clarity 2\), gift of magic, insight \(+12wis +6int\) or brilliance \(+6wis +12int\), and intellectual superiority \(cuts down on fizzles\). Note, at level 46, the first 3 spells are replaced by Koadic's Endless Intellect \(aka KEI\).

I've also found it very helpful to work on these skills in the guild hall "jacuzzi" since a\) your buffs won't fade, and b\) the jacuzzi nearly double your mana regen.

Damage spells do not "take" on you for the most part, and if you should be working on conjuration with a summoning spell\(such as Halo of Light\), you do NOT need to delete the item! You cannot summon a 2nd halo, for example, however you will still get skillups.

`|/////////////////////////////////////////////////////////////////////////////////`  
`|`  
`| Spell Practice Macro`  
`| practice.mac`  
`| Author : JP5`  
`| Date : 2004-08-05 21:03pm GMT`  
`| Useage : /macro practice [gem#] [target]`  
`| Example : /macro practice 5 Gobartik`  
`| Description :`  
`| -> Target is optional. Default target is ${Me} when not defined.`  
`|`  
`| -> If you wish to stop practicing, hit ESC.`  
`|`  
`| -> When macro ends (with ESC or skill max), you will be given a report of your`  
`| skillups.`  
`|`  
`| -> As long as your DD doesn't do over 20% damage to yourself, you won't die`  
`| from nuking yourself...`  
`|`  
`|/////////////////////////////////////////////////////////////////////////////////`

`#event NotTakeHold "Your spell did not take hold."`  
`#event ClarityFades "The cool breeze fades."`  
`#event SkillUp "You have become better at #1#! (#2#)"`  
`#event ESC "You no longer have a target."`

`Sub Main`  
`/declare GemNumber int outer`  
`/declare PTarget string outer`

`/if (${Defined[Param0]}) {`

`/varset GemNumber ${Param0}`  
`/echo Practicing ${Spell[${Me.Gem[${GemNumber}]}].Skill}. Hit ESC at any time to end and see results.`  
`} else {`  
`````  /echo Usage: /macro practice \[gem\#\] \[target\]``` /echo Which spell would you like to practice?``  
`/endmacro`  
`}`

`/if (${Defined[Param1]}) {`  
`/varset PTarget ${Param1}`  
`} else {`  
`/echo No target defined. Defaulting to ${Me}.`  
`/varset PTarget ${Me}`  
`}`

`/declare MainSkillUp int outer 0`  
`/declare SecSkillUp int outer 0`

`:start`  
`/stand`  
`/target ${PTarget}`

`:bleh`  
`/doevents`  
`/if (${Me.SpellReady[${GemNumber}]}) {`  
`/if (${Me.Gem[${GemNumber}].Mana} > ${Me.CurrentMana}) {`  
`/sit`  
`/goto :medup`  
`}`  
`/if (${Me.PctHPs}<20) {`  
`/sit`  
`/echo Ending Macro. HPs are too low.`  
`/call Results`  
`}`  
`/if (${Me.State.NotEqual[STAND]}) {`  
`/stand`  
`/delay 1`  
`}`  
`/if (${Math.Calc[${Me.Level}*5+5]}==${Me.Skill[${Spell[${Me.Gem[${GemNumber}]}].Skill}]}) {`  
`/call Results`  
`}`  
`/goto :cast`  
`} else {`  
`/goto :bleh`  
`}`

`:cast`  
`/cast ${GemNumber}`  
`/goto :bleh`

`:medup`  
`/doevents`  
`/if (${Me.State.NotEqual[SIT]}) {`  
`/delay 10`  
`/sit`  
`}`  
`/if (${Me.CurrentMana}==${Me.MaxMana}) {`  
`/goto :start`  
`} else {`  
`/goto :medup`  
`}`

`/return`

`|-- Sub Event_ClarityFades`  
`Sub Event_ClarityFades`  
`:test`  
`/if (${Me.Class.Name.Equal[Enchanter]}) {`  
`/if (${Me.SpellReady[Clarity]}) {`  
`/if (${Me.CurrentMana}>${Spell[Clarity].Mana}) {`  
`/stand`  
`/cast Clarity`  
`} else {`  
`/sit`  
`/goto :test`  
`}`  
`} else {`  
`/goto :test`  
`}`  
`}`  
`/return`

`|-- Sub Event_NotTakeHold`  
`Sub Event_NotTakeHold`  
`/echo Macro ended. Invalid Target.`  
`/call Results`  
`/return`

`Sub Event_ESC`  
`/echo Macro Ended by user.`  
`/call Results`  
`/return`

`|-- Sub Event_SkillUp`  
`Sub Event_SkillUp(string Line, string SkillType, int SkillValue)`

`/if (${Spell[${Me.Gem[${GemNumber}]}].Skill.Equal[${SkillType}]}) {`  
`/varcalc MainSkillUp ${MainSkillUp}+1`  
`}`  
`/if (${Spell[${Me.Gem[${GemNumber}]}].Skill.NotEqual[${SkillType}]}) {`  
`/varcalc SecSkillUp ${SecSkillUp}+1`  
`}`

`/if (${Spell[${Me.Gem[${GemNumber}]}].Skill.Equal[${SkillType}]}) {`  
`/if (${Math.Calc[${Me.Level}*5+5]}==${SkillValue}) {`  
`/call Results`  
`}`  
`}`  
`/return`

`|-- Sub Results`  
`Sub Results`  
`/echo Results: ${Spell[${Me.Gem[${GemNumber}]}].Skill} (${Me.Skill[${Spell[${Me.Gem[${GemNumber}]}].Skill}]}) -- Total of ${MainSkillUp} skillups!`  
`/echo Total other skillups (not ${Spell[${Me.Gem[${GemNumber}]}].Skill}) -- ${SecSkillUp}.`  
`/endmacro`

`/return`

