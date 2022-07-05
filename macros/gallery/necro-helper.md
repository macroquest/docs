---
tags:
   - macro
---
# Necro Helper

This is a simple helper macro I use when playing my necro toon. It does the following:

At top left of display (under the lag-o-meter)

* Displays your state: Sitting, standing, feign etc \(I wanted this mostly because the spectre animation when lich'ed

  isn't visibly different for sit/stand\)

* Displays class, level and %HP of selected mob/npc
* Tracks regular and AA experience
* Displays name of first GM found in zone
* Shows personal tribute status on/off
* Can also do a /gsay to tell your group what spells you are casting

In middle of screen

* Watches DoT spells cast on a mob and displays time left to run

**Important note. You need to update the code lines:**

`/varset SpellInfo >>> Your timer, your damage, your other text <<<`

&lt;/code&gt; to your preferences e.g.:

`/varset SpellInfo 2 minutes, 68 dpt, 70% snare`

&lt;/code&gt;

The macro code (for your **Release\Macros** directory):

`|`  
`| NecroHelper.mac by pw`  
`|`  
`| Usage:`  
`|`  
`| /macro NecroHelper`  
`|`  
`| For group use (will report your casting to group in /gsay):`  
`|`  
`| /macro NecroHelper 1`  
`|`  
`| This macro will react to spells cast on your target.`  
`| It displays the time remaining on the spell cast, the`  
`| spell cast, and the mob cast upon.`  
`| - Tracks XP and AAXP gained.`  
`| - (Optionally) Keeps group informed of your casting.`  
`|`  
`| Currently it will display 6 DoTs at once.`  
`| It will refresh any identical buff recast on the same mob`  
`| It fills in timer slots from top to bottom as available`  
`| Displays timer list full when max timers are running`  
`|`  
`| DoT timer Code taken from HudTimer by seagreen`  
`| XP tracker Code taken from perfect XP tracker by Raebis (with tweaks from Phoenix)`  
`|`

`#turbo 40`

`#event Exp "#*#party experience!!"`  
`#event Exp2 "You gain experience!!"`  
`#event Casting "You begin casting #1#"`  
`#event Fizzle "#*#Your spell fizzles#*#"`  
`#event Interrupt "#*#Your casting has been interrupted#*#"`  
`#event Interrupt "#*#Your spell is interrupted.#*#"`

`|`  
`| TODO: Need to add the full set of Necro Damage/debuff over time spells`  
`|`  
`| Each time an event is added for a new spell, you need a Sub Event_XXXX`  
`| below.`  
`|`

`#event EmbracingDarkness "#*#is engulfed in an embracing darkness#*#"`  
`#event FPOK "#*#is enveloped in a funeral pyre#*#"`  
`#event Splurt "#*#begins to splurt#*#"`  
`#event SaryrnKiss "#*#screams in torment#*#"`  
`#event GreaterImmobilize "#*#adheres to the ground#*#"`  
`#event Shackle "#*#is hindered by a shackle of spirit#*#"`  
`#event DarkPlague "#*#skin is covered in black spots#*#"`  
`#event DesecratingDarkness "#*#is covered in bubbling black shadows#*#"`  
`#event FoD "#*#is pierced by a dark fang#*#"`  
`#event PoM "#*#body is enveloped in the pyre of Mori#*#"`  
`#event ChaosVenom "#*#blood burns with the venom of chaos#*#"`  
`#event DarkNightmare "#*#mind is consumed in dark nightmares#*#"`  
`#event NightFire "#*#blood boils through#*#"`  
`#event DeathSilence "#*#stops moaning#*#"`  
`#event BOT "#*#veins turn a vile shade of green#*#"`  
`#event ChaosPlague "#*#muscles begin to decay#*#"`  
`#event GripOfMori "#*#staggers under the grip of Mori#*#"`  
`#event TormentOfShadows "#*#is gripped by shadows of fear and terror#*#"`  
`#event DarkHold "#*#stops moving#*#"`  
`#event CurseOfMortality "#*#recognizes their fragile mortality#*#"`  
`#event SeveransRot "#*#muscles begin to decay#*#"`  
`#event CoruscatingDarkness "#*#is covered in coruscating black shadows#*#"`  
`#event AshengatePyre "#*#body is consumed in a pyre of Ashengate#*#"`  
`#event VakkdrasSicklyMists "#*#chokes on a sickly green mist#*#"`  
`#event WiltingFoliage "#*#wilts#*#"`  
`#event EranonDecay "#*#muscles begin to decay#*#"`  
`#event AuroralDarkness "#*#is covered in coruscating black shadows#*#"`  
`#event VisziajPallidHaze "#*#chokes on a sickly green mist#*#"`  
`#event AnathemaOfLife "#*#recognizes their fragile mortality#*#"`  
`#event PyreOfTheLifeless "#*#is enveloped in the pyre of the lifeless#*#"`  
`#event SearingShadow "#*#is crossed by a searing shadow#*#"`  
`#event ReaversPyre "#*#in a pyre of cinders#*#"`  
`#event VenonVenom "#*#veins turn a vile shade of green#*#"`

`Sub Main`  
`/declare Exper float outer`  
`/declare AAExp float outer`  
`/declare LDRExp float outer`

`/varset Exper ${Me.PctExp}`  
`/varset AAExp ${Me.PctAAExp}`  
`/varset LDRExp ${Me.PctGroupLeaderExp}`

`/declare counter int outer`  
`/declare DebuffSpell string outer`  
`/declare LastSpell string outer`  
`/declare SpellType string outer`  
`/declare SpellInfo string outer`

`/declare HudArrayNPCName[6] string outer`  
`/declare HudArrayID[6] int outer`  
`/declare HudArraySpell[6] string outer`  
`/declare HudArrayDuration[6] string outer`  
`/declare HudArrayTime[6] float outer`  
`/declare groupmode bool outer`

`/for counter 1 to 6`  
`/varset HudArrayID[${counter}] -1`  
`/varset HudArraySpell[${counter}] none`  
`/varset HudArrayDuration[${counter}] none`  
`/varset HudArrayTime[${counter}] 0`  
`/varset HudArrayNPCName[${counter}] none`  
`/next counter`  
````````` /echo Necro Helper now ACTIVE \`````

`/if (${Param0}) {`  
`/echo Group mode`  
`/varset groupmode 1`  
`} else {`  
`/echo Not Group mode`  
`/varset groupmode 0`  
`}`

`:mainloop`

`/doevents`  
`/call CheckTimer`  
`/delay 1s`

`/goto :mainloop`  
`/return`

`|-----------------------------------------`  
`| Here's our first sub, tracking only grouped xp....`  
`|-----------------------------------------`

`Sub Event_Exp`  
`/varset AAExp ${Math.Calc[${Me.PctAAExp}-${AAExp}]}`  
`/varset Exper ${Math.Calc[${Me.PctExp}-${Exper}]}`  
`/varset LDRExp ${Math.Calc[${Me.PctGroupLeaderExp}-${LDRExp}]}`

`/echo EXP: ${Exper} (${Me.PctExp}%) - AAXP: ${AAExp} (${Me.PctAAExp}%) - LDRXP: ${LDRExp} (${Me.PctGroupLeaderExp})`  
`/popup ${Exper} (${Me.PctExp}%) - AAXP: ${AAExp} (${Me.PctAAExp}%) - LDRXP: ${LDRExp} (${Me.PctGroupLeaderExp})`  
`/varset Exper ${Me.PctExp}`  
`/varset AAExp ${Me.PctAAExp}`  
`/varset LDRExp ${Me.PctGroupLeaderExp}`  
`/return`

`|-----------------------------------------`  
`| Here's our second sub, tracking solo XP.`  
`| Since you dont get LExp when solo, removed the popup/echo.`  
`|-----------------------------------------`

`Sub Event_Exp2`  
`/varset AAExp ${Math.Calc[${Me.PctAAExp}-${AAExp}]}`  
`/varset Exper ${Math.Calc[${Me.PctExp}-${Exper}]}`  
`/varset LDRExp ${Math.Calc[${Me.PctGroupLeaderExp}-${LDRExp}]}`

`/echo EXP: ${Exper} (${Me.PctExp}%) - AAXP: ${AAExp} (${Me.PctAAExp}%)`  
`/popup ${Exper} (${Me.PctExp}%) - AAXP: ${AAExp} (${Me.PctAAExp}%)`  
`/varset Exper ${Me.PctExp}`  
`/varset AAExp ${Me.PctAAExp}`  
`/varset LDRExp ${Me.PctGroupLeaderExp}`  
`/return`

`|`  
`| TODO: Need to add the full set of Necro Damage/debuff over time spells`  
`| When adding new ones, be sure to spell the spell's name correctly in`  
`| the /varset line, otherwise the timer will not be calculated correctly.`  
`|`

`Sub Event_SaryrnKiss`  
`/varset DebuffSpell Saryrn's Kiss`  
`/varset SpellType DOT`  
`/varset SpellInfo 1 minute timer, 198 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_DesecratingDarkness`  
`/varset DebuffSpell Desecrating Darkness`  
`/varset SpellType SNARE`  
`/varset SpellInfo 2 minute timer, 96 damage per tick, 75% movement reduction`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_EmbracingDarkness`  
`/varset DebuffSpell Embracing Darkness`  
`/varset SpellType SNARE`  
`/varset SpellInfo 2 minute timer, 70 damage per tick, 70% movement reduction`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_FPOK`  
`/varset DebuffSpell Funeral Pyre of Kelador`  
`/varset SpellType DOT`  
`/varset SpellInfo 45 second timer, 310 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_BOT`  
`/varset DebuffSpell Blood of Thule`  
`/varset SpellType DOT`  
`/varset SpellInfo 45 second timer, 350 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_Splurt`  
`/varset DebuffSpell Splurt`  
`/varset SpellType DOT`  
`/varset SpellInfo 1.5 minute timer, 30-190 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_GreaterImmobilize`  
`/varset DebuffSpell Greater Immobilize`  
`/varset SpellType ROOT`  
`/varset SpellInfo 1 minute timer`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_Shackle`  
`/varset DebuffSpell Shackle of Spirit`  
`/varset SpellType SLOW`  
`/varset SpellInfo 3.5 minute timer, 70% attack speed reduction`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_DarkPlague`  
`/varset DebuffSpell Dark Plague`  
`/varset SpellType DOT`  
`/varset SpellInfo 2 minute timer, 180 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_FoD`  
`/varset DebuffSpell Fang of Death`  
`/varset SpellType DOT`  
`/varset SpellInfo 1 minute timer, 370 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_POM`  
`/varset DebuffSpell Pyre of Mori`  
`/varset SpellType DOT`  
`/varset SpellInfo 1 minute timer, 419 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_ChaosVenom`  
`/varset DebuffSpell Chaos Venom`  
`/varset SpellType DOT`  
`/varset SpellInfo 35 second timer, 460 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_DarkNightmare`  
`/varset DebuffSpell Dark Nightmare`  
`/varset SpellType DOT`  
`/varset SpellInfo 30 second timer, 591 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_NightFire`  
`/varset DebuffSpell Night Fire`  
`/varset SpellType DOT`  
`/varset SpellInfo 45 second timer, 335 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_DeathSilence`  
`/varset DebuffSpell Death's Silence`  
`/varset SpellType MEZZ`  
`/varset SpellInfo 30 second timer`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_ChaosPlague`  
`/varset DebuffSpell Chaos Plague`  
`/varset SpellType DOT`  
`/varset SpellInfo 1.5 minute timer, 249 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_GripOfMori`  
`/varset DebuffSpell Grip of Mori`  
`/varset SpellType DOT`  
`/varset SpellInfo 1 minute timer, 194 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_TormentOfShadows`  
`/varset DebuffSpell Torment of Shadows`  
`/varset SpellType SNARE`  
`/varset SpellInfo 1.5 minute timer, 75 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_DarkHold`  
`/varset DebuffSpell Dark Hold`  
`/varset SpellType MEZZ`  
`/varset SpellInfo Mezzed for up to 5 ticks`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_CurseOfMortality`  
`/varset DebuffSpell Curse of Mortality Rk. II`  
`/varset SpellType DOT`  
`/varset SpellInfo 30 second timer, 727 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_SeveransRot`  
`/varset DebuffSpell Severan's Rot Rk. II`  
`/varset SpellType DOT`  
`/varset SpellInfo 1 minute 30 second timer, 179-320 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_CoruscatingDarkness`  
`/varset DebuffSpell Coruscating Darkness Rk. II`  
`/varset SpellType SNARE`  
`/varset SpellInfo 2 minute timer, 118 damage per tick, 75% movement reduction`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_AshengatePyre`  
`/varset DebuffSpell Ashengate Pyre Rk. II`  
`/varset SpellType DOT`  
`/varset SpellInfo 30 second timer, 1013 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_VakkdrasSicklyMists`  
``/varset DebuffSpell Vakk`dra's Sickly Mists Rk. II``  
`/varset SpellType DOT`  
`/varset SpellInfo 45 second timer, 598 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_WiltingFoliage`  
`/varset DebuffSpell Wilting Foliage`  
`/varset SpellType DOT`  
`/varset SpellInfo 30 second timer, 698 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_EranonDecay`  
`/varset DebuffSpell Eranon's Decay`  
`/varset SpellType DOT`  
`/varset SpellInfo 1 minute 30 timer, 400 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_AuroralDarkness`  
`/varset DebuffSpell Auroral Darkness`  
`/varset SpellType DOT`  
`/varset SpellInfo 2 minutes, 137 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_VisziajPallidHaze`  
`/varset DebuffSpell Visziaj's Pallid Haze`  
`/varset SpellType DOT`  
`/varset SpellInfo 45 second timer, 695 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_AnathemaOfLife`  
`/varset DebuffSpell Anathema of Life Rk. II`  
`/varset SpellType DOT`  
`/varset SpellInfo 30 second timer, 845 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_PyreOfTheLifeless`  
`/varset DebuffSpell Pyre of the Lifeless`  
`/varset SpellType DOT`  
`/varset SpellInfo 54 second timer, 599 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_SearingShadow`  
`/varset DebuffSpell Searing Shadow`  
`/varset SpellType DOT`  
`/varset SpellInfo 90 second timer, 720 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_ReaversPyre`  
`/varset DebuffSpell Reaver's Pyre`  
`/varset SpellType DOT`  
`/varset SpellInfo 30 second timer, 1130 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub Event_VenonVenom`  
`/varset DebuffSpell Venonscale Venom`  
`/varset SpellType DOT`  
`/varset SpellInfo 42 second timer, 800 damage per tick`  
`/call SetupTimer`  
`/call ReportCast`  
`/return`

`Sub ReportCast`  
`/if (${LastSpell.Equal[${DebuffSpell}]}) {`  
`/echo ${DebuffSpell}`  
`/if (${groupmode}==1) {`  
`/delay 1s`  
`/gsay ${SpellType} on --> ${If[${Target.CleanName.NotEqual["NULL"]},${Target.CleanName},"Target"]} <-- with ${DebuffSpell}. ${SpellInfo}.`  
`}`  
`}`  
`/return`  
````` \|```\| Store the last spell name we cast in ${spellname}````` \|```Sub Event_Casting(String line, string spellname)``  
`/varset LastSpell ${spellname}`  
`/varset LastSpell ${LastSpell.Left[-1]}`  
`/return`

`|`  
`| Clear the last spell name on a fizzle`  
`|`  
`Sub Event_Fizzle`  
`/varset LastSpell none`  
`/return`

`|`  
`| Clear the last spell name on an interrupt`  
`|`  
`Sub Event_Interrupt`  
`/varset LastSpell none`  
`/return`

`|`  
`| Set up timer with ${DebuffSpell} on ${Target}`  
`| Will re-use a timer slot if same spell found on same target`  
`|`  
`Sub SetupTimer`  
`/declare duration int local`  
`|`  
`| Skip if someone else's cast`  
`|`  
`/if (!${LastSpell.Equal[${DebuffSpell}]}) /return`  
`|`  
`| IF SAME DEBUFF IS BEING RECAST ON EXISTING NPC IN TIMER ARRAY, REFRESH`  
`|`  
`/for counter 1 to 6`  
`/if (${HudArrayID[${counter}]}==${Target.ID} && ${DebuffSpell.Equal[${HudArraySpell[${counter}]}]}) {`  
`/varset HudArrayTime[${counter}] ${Math.Calc[${Time.SecondsSinceMidnight}+(${Spell[${DebuffSpell}].Duration}*6)]}`  
`/varset HudArraySpell[${counter}] ${DebuffSpell}`  
`/varset HudArrayNPCName[${counter}] ${Target.Name}`  
`/varset HudArrayID[${counter}] ${Target.ID}`  
`/return`  
`}`  
`/next counter`  
`|`  
`| SETUP NEW DEBUFF OF NPC IN OPEN SLOT`  
`|`  
`/varset counter 1`  
`:counterloop`  
`/if (${HudArrayID[${counter}]}==-1 && !(${Math.Calc[${HudArrayTime[${counter}]}-${Time.SecondsSinceMidnight}].Int}>0)) {`  
`/varset HudArrayTime[${counter}] ${Math.Calc[${Time.SecondsSinceMidnight}+(${Spell[${DebuffSpell}].Duration}*6)]}`  
`/varset HudArraySpell[${counter}] ${DebuffSpell}`  
`/varset HudArrayNPCName[${counter}] ${Target.Name}`  
`/varset HudArrayID[${counter}] ${Target.ID}`  
`} else {`  
`/if (${counter}>5) {`  
`/echo Debuff timer slots are full`  
`/return`  
`}`  
`/varcalc counter ${counter}+1`  
`/goto :counterloop`  
`}`  
`/return`

`|`  
`| Checks all timers`  
`| - clears timer slot when mob is dead or timer expired`  
`| - formats timer data to time left to run in hh:mm:ss format`  
`|`  
`Sub CheckTimer`  
`/declare duration int local`  
`/declare myhour string local`  
`/declare myminute string local`  
`/declare mysecond string local`

`/for counter 1 to 6`  
`/if (!${Spawn[${HudArrayID[${counter}]}].State.Equal[HOVER]} && ${Math.Calc[${HudArrayTime[${counter}]}-${Time.SecondsSinceMidnight}].Int}>0) {`  
`|`  
`| FORMAT DURATION TO 00:00:00`  
`|`  
`/varset duration ${Math.Calc[${HudArrayTime[${counter}]}-${Time.SecondsSinceMidnight}].Int}`  
````` /if (${duration}&gt;3600\) {``` /varset myhour ${Math.Calc[${duration}/3600\].Int}````` /varset duration ${Math.Calc\[\(\(${duration}/3600\)-${myhour})\*3600]}```} else {``  
`/varset myhour`  
`}`

`/if (${duration}>60) {`  
`/varset myminute ${Math.Calc[${duration}/60].Int}`  
`/varset duration ${Math.Calc[${Math.Calc[${Int[${duration}/60]}]} - ${Math.Calc[${myminute}]}*60]}`  
`/if (${myhour} && ${myminute}<0) /varset myminute 0${myminute}`  
`} else {`  
`/varset myminute`  
`}`

`/if (${duration}>=0) {`  
`/varset mysecond ${Int[${duration}/6]}`  
`/if (${myminute} && ${mysecond}<0) /varset mysecond 0${mysecond}`  
`} else {`  
`/varset mysecond 0`  
`}`  
`|`  
`| DISPLAY HH:MM:SS IF NEEDED`  
`|`  
`/if (${myhour.NotEqual[NULL]} && ${Int[${myhour}]} !=0) {`  
`/varset HudArrayDuration[${counter}] ${myhour}:${myminute}m:${mysecond}s`  
`} else /if (${myminute.NotEqual[NULL]}&& ${Int[${myminute}]} !=0) {`  
`/varset HudArrayDuration[${counter}] ${myminute}m:${mysecond}s`  
`} else /if (${mysecond.NotEqual[NULL]}) {`  
`/varset HudArrayDuration[${counter}] ${mysecond}s`  
`}`  
`} else {`  
`/varset HudArrayTime[${counter}]`  
`/varset HudArraySpell[${counter}] none`  
`/varset HudArrayNPCName[${counter}]`  
`/varset HudArrayID[${counter}] -1`  
`/varset HudArrayDuration[${counter}]`  
`}`  
`/next counter`  
`/return`

&lt;/code&gt;

You will also need these elements in your **MQ2HUD.ini** file (located in **Release** directory\) NOTE: this file may not be present - create a new one with your favourite text editor \(or notepad).

`[Elements]`  
`State=3,5,25,255,255,255,${Me.State}`  
`TargetLVLClass=3,5,35,255,255,255,${If[${Target.ID},${Target.Level} ${Target.Class} ${Target.PctHPs}%,]}`  
`RegExp=3,5,45,255,255,255,XP: ${Me.PctExp}%`  
`AAExp=3,5,55,255,255,255,AA: ${Me.PctAAExp}%`  
`Tribute=3,5,65,2,255,2,${If[${Me.TributeActive},Tribute is on,]}`  
`GM=3,5,75,255,2,2,${If[${Spawn[gm].ID},GM: ${Spawn[gm].Name},]}`  
````` HudTimer1=1,480,240,050,255,255,${If[${HudArraySpell\[1\].Equal\[none\]},,${HudArrayDuration\[1\]}\]}``` HudSpell1=1,530,240,255,255,255,${If\[${HudArraySpell\[1\].Equal\[none\]},,${HudArraySpell\[1\]}\]}````` HudTarget1=1,630,240,255,255,050,${If\[${HudArraySpell\[1\].Equal\[none\]},,${HudArrayNPCName\[1\]}]}\`

`HudTimer2=3,480,250,050,255,255,${If[${HudArraySpell[2].Equal[none]},,${HudArrayDuration[2]}]}`  
`HudSpell2=3,530,250,255,255,255,${If[${HudArraySpell[2].Equal[none]},,${HudArraySpell[2]}]}`  
`HudTarget2=3,630,250,255,255,050,${If[${HudArraySpell[2].Equal[none]},,${HudArrayNPCName[2]}]}`

`HudTimer3=3,480,260,050,255,255,${If[${HudArraySpell[3].Equal[none]},,${HudArrayDuration[3]}]}`  
`HudSpell3=3,530,260,255,255,255,${If[${HudArraySpell[3].Equal[none]},,${HudArraySpell[3]}]}`  
`HudTarget3=3,630,260,255,255,050,${If[${HudArraySpell[3].Equal[none]},,${HudArrayNPCName[3]}]}`

`HudTimer4=3,480,270,050,255,255,${If[${HudArraySpell[4].Equal[none]},,${HudArrayDuration[4]}]}`  
`HudSpell4=3,530,270,255,255,255,${If[${HudArraySpell[4].Equal[none]},,${HudArraySpell[4]}]}`  
`HudTarget4=3,630,270,255,255,050,${If[${HudArraySpell[4].Equal[none]},,${HudArrayNPCName[4]}]}`

`HudTimer5=3,480,280,050,255,255,${If[${HudArraySpell[5].Equal[none]},,${HudArrayDuration[5]}]}`  
`HudSpell5=3,530,280,255,255,255,${If[${HudArraySpell[5].Equal[none]},,${HudArraySpell[5]}]}`  
`HudTarget5=3,630,280,255,255,050,${If[${HudArraySpell[5].Equal[none]},,${HudArrayNPCName[5]}]}`  
````` HudTimer6=3,480,290,050,255,255,${If[${HudArraySpell\[6\].Equal\[none\]},,${HudArrayDuration\[6\]}\]}``` HudSpell6=3,530,290,255,255,255,${If\[${HudArraySpell\[6\].Equal\[none\]},,${HudArraySpell\[6\]}\]}````` HudTarget6=3,630,290,255,255,050,${If\[${HudArraySpell\[6\].Equal\[none\]},,${HudArrayNPCName\[6\]}]}```[MQ2HUD]``  
`Last=Elements`

&lt;/code&gt;

