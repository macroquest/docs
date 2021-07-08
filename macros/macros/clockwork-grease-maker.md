# Clockwork Grease Maker

This is a macro to make jars of clockwork grease, a very tedious combine. It does not deal well with subcombine failures yet, but is otherwise completely functional.

Paste this code into a file called grease.mac in your \macros directory, usually found under your release directory unless you have changed something:

`|/////////////////////////////////////////////////////////////////////////////`  
`| Grease.mac by dedpoet`  
`|`  
`| Attempts to make a Jar of Clockwork Grease until out of components.`  
`|`  
`| You will need the following items in your inventory: Water Flask, Block of`  
`| Clay, Small Jar Sketch, Quality Firing Sheet, Clockwork Grease. You will`  
`| need your last inventory slot open.`  
`|`  
`| Stand between the pottery wheel and the kiln and run grease.mac.`  
`|`  
`| This macro uses the pack subs written by Override and quite a bit of his`  
`| code. Also thanks to JJ for the shoves in the right direction with the`  
`| window stuff`  
`|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\`

`#turbo`

`#event CombineError "#*#There was no place to put that#*#"`  
`#event CombineError "#*#You cannot combine these items in this container type!#*#"`  
`#event CombineError "#*#did not accept these items#*#"`

`Sub Main`

`| Let's make an Unfired Small Container`  
`/call OpenPacks`  
`/delay 2s`

`:GreaseLoop`

`/itemtarget Pottery Wheel`  
`/face item`  
`/nomodkey /click left item`  
`/delay 1s`  
`/nomodkey /notify TradeSkillWnd COMBW_ExperimentButton leftmouseup`  
`/delay 1s`  
````/if \(!${FindItem\[=Water Flask\].InvSlot}\) /goto :Done``` /nomodkey /ctrl /itemnotify ${FindItem[=Water Flask].InvSlot} leftmouseup``    
`/nomodkey /itemnotify enviro1 leftmouseup`````  /if \(!${FindItem\[=Block of Clay\].InvSlot}\) /goto :Done``` /nomodkey /ctrl /itemnotify ${FindItem[=Block of Clay].InvSlot} leftmouseup``  
`/nomodkey /itemnotify enviro2 leftmouseup`

`/if (!${FindItem[=Small Jar Sketch].InvSlot}) /goto :Done`  
`/nomodkey /ctrl /itemnotify ${FindItem[=Small Jar Sketch].InvSlot} leftmouseup`  
`/nomodkey /itemnotify enviro3 leftmouseup`

`/combine enviro`  
`/delay 15`  
`/doevents`  
`/call ClearCursor`  
`/delay 5`  
`/nomodkey /keypress esc`  
`/delay 1s`

`| Let's make it into a Small Clay Jar`

`/itemtarget Kiln`  
`/nomodkey /click left item`  
`/delay 1s`  
`/nomodkey /notify TradeSkillWnd COMBW_ExperimentButton leftmouseup`  
`/delay 1s`

`/if (!${FindItem[=Unfired Small Container].InvSlot}) /goto :Done`  
`/nomodkey /ctrl /itemnotify ${FindItem[=Unfired Small Container].InvSlot} leftmouseup`  
`/nomodkey /itemnotify enviro1 leftmouseup`  
````` /if \(!${FindItem\[=Quality Firing Sheet\].InvSlot}\) /goto :Done``` /nomodkey /ctrl /itemnotify ${FindItem\[=Quality Firing Sheet\].InvSlot} leftmouseup````` /nomodkey /itemnotify enviro2 leftmouseup\`

`/combine enviro`  
`/delay 15`  
`/doevents`  
`/call ClearCursor`  
`/nomodkey /keypress esc`  
`/delay 1s`

`| Open our new jar and put 2 greases in it`  
````/itemnotify pack8 rightmouseup``` /delay 1s``````  /if \(!${FindItem\[=Clockwork Grease\].InvSlot}\) /goto :Done``` /nomodkey /ctrl /itemnotify ${FindItem[=Clockwork Grease].InvSlot} leftmouseup``  
`/nomodkey /itemnotify in pack8 1 leftmouseup`  
`/delay 5`

`/if (!${FindItem[=Clockwork Grease].InvSlot}) /goto :Done`  
`/nomodkey /ctrl /itemnotify ${FindItem[=Clockwork Grease].InvSlot} leftmouseup`  
`/nomodkey /itemnotify in pack8 2 leftmouseup`  
````` /combine pack8``` /delay 15````` /doevents```/call ClearCursor``  
`/delay 20`

`| We should have a grease. Let's start over.`  
`/goto :GreaseLoop`

`| When we run out of components.`  
`:Done`  
`/echo We're out of components. Ending macro.`  
`/beep`  
`/cleanup`  
`/end`  
`/return`

`sub ClearCursor`  
`:Loop`  
`/if (!${Cursor.ID}) /return`  
`/autoinv`  
`/delay 5`  
`/doevents`  
`/goto :Loop`  
`/return`

`Sub OpenPacks`  
`/declare bag int local 0`

`/newif (!${Window[InventoryWindow].Open}) /keypress inventory`  
`/delay 1`  
`/for bag 1 to 8 step 1`  
`/newif (!${Window[pack${bag}].Open}) /itemnotify pack${bag} rightmouseup`  
`/next bag`  
`/delay 1`  
`/return`

`Sub Event_CombineError`  
`/echo Combine error encountered. Ending macro.`  
`/beep`  
`/end`  
`/return`

