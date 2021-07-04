# AAPurchase.inc

## Description

This macro will do the following:  
-Purchase AA's based on an array created from an ini file.

`-Allow you to specify how many levels of a skill to purchase.`  
`-Skip any AA that you are too low to purchase at your level.`  
`-Inform you that it was not able to purchase the skill yet and tell you how much you have and how much it costs.`  
`-Inform you of the skill it purchased and how much it cost.`  
`-Inform you that you were not able to purchase a skill yet and what level is requires.`  
`-Inform you when a skill you have defined is maxed, and will skip to the next in the list.`  
`-Inform you to define new AA's you when all current defined AA's are maxed.`  
`-Will detect if you do not have Fast AA Purchase on and cconfirm you want to purchase the AA.`  
`-Allows you to define your own ini section so that you can add shroud abilities to purchase without losing your characters list to purchase.`  
`-Warn you when you have 27+ AA's banked.`  
`-Switch you to 100% level XP when ou reach 30 banked AA's`

You can find the latest version of in [this post.](https://macroquest2.com/phpBB3/viewtopic.php?f=49&t=15824&hilit=AAPurchase.INC)

## Usage

-Create an AA\_CharacterName.ini and place the following in it.

`[AAtoBuy]`  
`AACount=2`  
`AA1=Combat Agility|2`  
`AA2=Combat Stability|M`  
`````  \`

-- Thanks Spudman for creating a dump macro that will dump all your non maxed AA's. You can get it here [http://macroquest2.com/phpBB2/viewtopic.php?p=139521\#139521](http://macroquest2.com/phpBB2/viewtopic.php?p=139521#139521)

`-AACount would be the number of total AA's you are adding to the ini file.`  
`-AA1 would be the first AA you want to train. AA2 would be the second. Add more to your hearts content. There is no max limit. But it will take longer to run, especially if you do not clean up the list removing those you have already maxed.`  
`-The |2 would tell it to only purchase to ability level 2. For instance AC would purchase until it reached 2/28 and then skip to the next in the list.`  
`-The |M would tell it to purchase to the max ability level.`  
`-Add "#include AAPurchase.inc" into your macro.`  
`-Add "/call AAInit" or "/call AAInit inisection" into the initialization section of your macro.`  
`This should allow for autodetection of earned AA's and trigger the purchase sub.`  
`That is it.`

However, if you earn AA's while zoning the autodetection will not work. If that is the case:

`-Add "/call AAPicker" anywhere into your main loop.`

## Macro Version

If you want to run the include as a macro create the below:

`AAPurchase.mac`  
`````  \#include AAPurchase.inc``` Sub Main(IniSection)``  
`/call AAInit ${IniSection}`  
`/call AAPicker`  
`/return`  
`````  \`

and then just run '/mac AAPurcahse' or optionally '/mac AAPurcahse inisection' to load a shroud's abilities that you defined in the 'inisection' you entered.

## Advanced

Change this to change which channel you send your notifications to.

`Ex: /bc , /echo , /mqlog`  
`#define def_channel_ /echo`  
`````  \`

Also from fearless, if you want to know who is training what when using /mqlog use this

`#define def_channel_ "/mqlog $[Me.Name}"`  
 ``

