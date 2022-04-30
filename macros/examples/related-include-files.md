# Related Include Files

## AAPurchase

Most of this information was copied directly from the original AAPurchase thread (a big thanks to three-p-o for this handy function!) The orignial AAPurchase thread can be found [**Here**](https://macroquest.org/phpBB3/viewtopic.php?t=15824).

AAPurchase will do the following:

* Purchase AA's based on an array created from an ini file \(this file is auto-created for you with the AAPurchase

  implementation in ModBot\).

* Allow you to specify how many levels of a skill to purchase.
* Skip any AA that you are too low to purchase at your level.
* Inform you that it was not able to purchase the skill yet and tell you how much you have and how much it costs.
* Inform you of the skill it purchased and how much it cost.
* Inform you that you were not able to purchase a skill yet and what level is requires.
* Inform you when a skill you have defined is maxed, and will skip to the next in the list.
* Inform you to define new AA's you when all current defined AA's are maxed.
* Detect if you do not have Fast AA Purchase on and confirm you want to purchase the AA.
* Allow you to define your own ini section so that you can add shroud abilities to purchase without losing your

  characters list to purchase (more on this in a later wiki update).

* Warn you when you have 27+ AA's banked.
* Switch you to 100% level XP when ou reach 30 banked AA's

How to use: An AA\_CharName.ini should automatically be created for you in your \Macros folder (using functionality created by spudman). The general layout of that file is:

`[AAtoBuy]`  
`AACount=[Number of AAs in the ini list]`  
`AA1=|#|M|S`

* the name of the AA (e.g. Combat Stability)
* _\#_ the maximum level of this AA to purchase (do not use in combination with the 'M' parameter)
* _M_ indicates that you want to purchase this AA to its maximum level possible
* _S_ indicates that you want to skip purchasing this AA (if you don't hae enough AA points saved) and check the next

  AA

Example:

`[AAtoBuy]`  
`AACount=4`  
`AA1=Combat Agility|2`  
`AA2=Combat Stability|M`  
`AA3=Fury of Magic|M|S`  
`AA4=Teleport Bind|M`

* AA1 would be the first AA you want to train. AA2 would be the second. Add more to your hearts content. There is no

  max limit, but it will take longer to run, especially if you do not clean up the list removing those you have

  already maxed.

* AA1 (Combat Agility\) would purchase until it reached level 2 \(of 28 possible) and then skip to the next AA to

  purchase in the list.

* The 'M' parameter for AA2 would tell it to purchase Combat Stability to the max ability level. AAPurchase will

  continue to save AAs and purchase levels until you have maxed out what you can buy of this AA. Only then will it

  move on to checking AAs further down the list.

* The 'M\|S' parameters for AA3 would tell it to purchase Fury of Magic to its max level. If you don't have enough AA

  points to purchase the next level of Fury of Magic, the 'S' parameter would cause it to skip to the next AA to buy

  (Teleport Bind\) and purchase that instead \(assuming you have enough AA points saved for that).

Additional Info:

* Change this to change which channel you send your notifications to (e.g. /bc , /echo , /mqlog): \#define

  def_channel\_ /echo

* From fearless: If you want to know who is training what when using /mqlog use this Code: \#define def_channel\_

  "/mqlog $\[Me.Name}"

* If you want to see what your bots are up to (and you have Netbots loaded...), use the following command:
  * /echo ${NetBots[CharName].PctAAExp} (there's also a TypeMember\(PctExp); in the plugin. Depending on the

    Netbots version you have there's also TotalAA, UsedAA, and UnusedAA.\)

[**Return to main ModBot Wiki**](https://macroquest.org/wiki/index.php/ModBot)

## Forage

Note: More information needed for this section - feel free to add!!

* -1 means keep all no matter how many you have. 0 is destroy. Any positive number is how many to keep.

## Modloot

Modloot was originally based on Forking's Loot.inc (original thread can be found [**here**](https://macroquest.org/phpBB3/viewtopic.php?t=15180)\), but several sections have had complete rewrites and no longer even resemble the original \(though they have been made to be backwards compatible for the older options).

The creation of the initial Loot.ini file (found in the \Macros folder\) is triggered by setting 'DoLoot=TRUE' in your MB\_CharName.ini file. The location of the Loot.ini file \(as well as its name) can be changed using the 'Loot.ini=' section in MBCommon.ini.

While looting is enabled (DoLoot=TRUE), your bot will automatically attempt to loot whenever there are corpses within CorpseRadius and no mobs within the MobsTooClose radius.

Once activated, looting will start up with some default actions:

* The first time an item is found, it will be added to the Loot.ini file under it's associated alphabetical section.
* Depending on the item's particular flag type, it will be set to either Keep or Ignore:
  * Nodrop items are set to Ignore (item will be left on corpse).
  * Quest flag items are set to Ignore (item will be left on corpse).
  * Most other items are set to Keep (item will be looted).

The resulting Loot.ini file can be customized to loot and dispose of items in a more efficient manner (rather than just keeping or ignoring something).

The basic format of the modloot 'Loot.ini' file is as follows:

### Settings Section - [Settings]

* **LootMobs**=[TRUE,FALSE] (set by DoLoot in MB\_CharName.ini)
* **CorpseRadius**=[Radius \#] (The default radius within which to search for corpses to loot. Default to 100.)
* **MobsTooClose**=[Radius \#] \(The default radius within which it will watch for other mobs before looting \(prevents

  looting when there are still mobs in camp\). Default to 50.\)

* **CorpseRotTime**=[Corpse rot time in seconds] (The time before corpses rot. Default 440s.) ??
* **ReportLoot**=[TRUE,FALSE] (Report \(or not\) looting activities to the defined LootChannel)
* **LootChannel**=[desired loot channel] (Channel on which looting actions will be announced \(e.g. "bc")
* **Category**=[cat1,cat2,etc.] \(Used to specify loot categories. Each argument added to 'Category' will add a

  variable to modbot. For example, 'Category=Smithing,Tailoring' would result in two new entries in the loot.ini file

  on the next run of modbot:

`Category=Smithing,Tailoring`  
`Smithing=`  
`Tailoring=`

If desired, the new entries can then be modified to define which toons can loot which types of items. ${NetBots.Client} will make sure all toons will loot the item if the category is only to be used with other commands. Please note that you are not required to define toon names for this (thus allowing a single looter to loot all items):

`Category=Smithing,Tailoring`  
`Smithing=ToonName1,ToonName2`  
`Tailoring=ToonName1`

After the Category entires have been defined, items can be marked in the Items section as belonging to a particular category:

`Rhenium Ore=Smithing`

Categories can also be used with other commands. For instance:

_/mb getbank Smithing TRUE_ \&lt;-- will search your bank for all items marked 'Smithing' and place them on your toon until you run out of room. The True\|False option is Stacks or Singles.

_/mb give Smithing TRUE \#_ \&lt;-- will give \# of Stacks (TRUE\|FALSE) of Smithing items to .

* **KeepScript**=[ScriptName] \(Allows you to define a full script that can be used to add extra options or checks

  before looting. You can now also set item names as =Script in your loot.ini file to use this option. Please note

  that the script will also run for all items marked 'Sell' to allow for checking values. If your script decides to

  loot the item, you will need to call the appropriate sub from your script. For example \(this was meant only to run

  for 'Sell' option, but can be expanded.\):

`[Script-ValueCheck]`  
`Commands=1`  
`C1=/if (!{Corpse.Item[{Param1}].Value} || {Corpse.Item[{Param1}].Value} && {Corpse.Item[{Param1}].Value}>1000) /call LootItem {Param1} Keep Right`

A '/call LootItem {Param1} Destroy Left' will destroy the item. Doing nothing, or exiting the script will result in item left on corpse

* **QuestOnly**=[TRUE,FALSE] \(Defaults to FALSE. To be used with DoQuest so the toon will only loot quest items. If

  this is true and doquest is false, the bot will only loot cash off mob.\)

### Items Section - []

* =[\|\|\|] (Tells modloot what to do with the item.)
  * can equal Keep, Destroy, Ignore, Quest or CategoryName. Please note that \| cannot be

    used at the same time as ToonName and/or Category.

    * _Raw Diamond=ToonName_ \&lt;-- Only ToonName will loot Raw Diamonds \(can be used in conjunction with Keep and

      Quantity\).

    * _Raw Diamond=Keep_ \&lt;-- Keeps all Raw Diamonds
    * _Raw Diamond=Keep\|10_ \&lt;-- Keeps Raw Diamonds until you have 10 of them. After that it leaves them on the

      corpse.

    * _Raw Diamond=Destroy_ \&lt;-- Loots Raw Diamonds and then destroys them.
    * _Raw Diamond=Ignore_ \&lt;-- Does not loot Raw Diamonds (leaves them on the corpse).
    * _Crate of Supplies=Quest\|10\|Gathering from the Goblins_ \&lt;--Specifies that the looter MUST have the quest

      'Gathering from the Goblins' in order to loot this item. In this case, the looter will only loot 10 'Crate

      of Supplies'. Note that the _Quest_ action should be used in conjunction with the parameter

      (defined as 'Gathering from the Goblins' in the example).

    * _Raw Diamond=Script_ \&lt;-- Runs the script that is defined in the 'KeepScript=' varible in the Settings

      section.

    * _Raw Diamond=Sell_ \&lt;-- Item will be looted and, when told, will be sold to a vendor.

  * Allows you to specify which toon you want to loot a particular item by using =.
  * \&lt;\# of item to loot&gt; Used with the 'Quest' and 'Keep' actions and defines how many of the item to loot. Once you

    have looted this amount, you will not loot anymore of this item. It is possible to simply use

    '=Quest\|10' without defining a quest name - this will produce an /echo about proper syntax for

    Quest\|x\| usage to include the quest name, but that is harmless, and item is still looted.

  * Tells modloot to only loot this item if you have the quest named .

A typical Loot.ini file might look like:

`[Settings]`  
`LootMobs=TRUE`  
`CorpseRadius=100`  
`MobsTooClose=50`  
`CorpseRotTime=440s`  
`ReportLoot=FALSE`  
`LootChannel=bc`  
`Category=Tradeskill,Spellscroll`  
`Tradeskill=Toon1Name,Toon2Name`  
`Spellscroll=Toon1Name,Toon2Name`  
`KeepScript=`  
`QuestOnly=FALSE`  
`[C]`  
`Curzon=Destroy`  
`Crystallized Mephit Horn=Keep`  
`Crate of Supplies=Quest|10|Gathering from the Goblins`  
`[R]`  
`Rough Efreeti Beard=Keep`  
`Russet Oxide=Keep`  
`[S]`  
`Spell: Siphon Essence Rk. II=Spellscroll`  
`Spell: Phase March Rk. II=Spellscroll`  
`Spell: Halcyon Zephyr Rk. II=Spellscroll`

[**Return to main ModBot Wiki**](https://macroquest.org/wiki/index.php/ModBot)

## ModMove

Use the functions in ModMove to run a path for pulling, selling, etc.

As mentioned in the main wiki, the primary command for interacting with modmove is /mbwayplay

### ModMove Commands

**mbwayplay (u,d,b,e\) \(t,f\) \(c\)** \(Used to playback previously recorded paths / waypoints, through zones, doors, chaining paths, etc.)

* **u**: (up) enter at the closest "waypoint" and then go "up" it
* **d**: (down) enter at the closest "waypoint" and then go "down" it
* **b**: (begin) start at the first waypoint
* **e**: (end) start at the last waypoint
* **t**: zone (t)rue - zone at the end of the path
* **f**: zone (f)alse - do not zone at the end of the path
* **c**: look for another path to (c\)hain \(this is optional)

**mbwayrec** (Used to record a path / waypoint. Once started, ducking at each location will add a waypoint to the path \(note that you need to add at least two waypoints \(start and finish?\) while running the path or it will not record\). Sitting stops path recording and returns to modbot functions. In order to add doors, chains, pull locations, etc. you'll need to edit the MBWayPlay.INI file)

* sell  (sell to the vendor - please see the section on modloot to know how to automate the sell process)
* door (open a door)
* pull (perform pull actions)

An option exists for a network based INI file for scripts and path playback (mbwayplay and mbwaypnt.ini file), if you use this option, your commands must be prefixed by "Network-" or "Net-". Set the location of your network INI file [Settings] section of your modbot INI:

`NetworkINI=X:\shared\modbot\mb_network.ini`

This would be an example of using your network based INI file:

`[DoPath]`  
`WPLoop=FALSE`  
`WPCount=1`  
`WP1=600 200`

`[Script-GoThere]`  
`Commands=2`  
`C1=/call mbwayplay net-dopath u`  
`C2=/call Buy`_```water`` ``flask```_`75 yenny`

### ModMove Examples

#### Example 1

`[example1]`  
`WPCount=5`  
`WP1=-912.25 2725.55`  
`WP2=-818.70 2627.16 sell magus`  
`WP3=-735.19 2674.32 door`  
`WP4=-805.75 2687.67 pull`  
`WP5=-912.25 2725.55`  
`[example2]`  
`WPCount=5`  
`WP1=-912.25 2725.55`  
`WP2=-818.70 2627.16 door`  
`WP3=-735.19 2674.32`  
`WP4=-805.75 2687.67 door`  
`WP5=-912.25 2725.55 example3 b t c`  
`[example3]`  
`WPCount=5`  
`WP1=-912.25 2725.55 example2 e`  
`WP2=-818.70 2627.16`  
`WP3=-735.19 2674.32 door`  
`WP4=-805.75 2687.67`  
`WP5=-912.25 2725.55 example4 e`  
`[example4]`  
`WPCount=5`  
`WP1=-912.25 2725.55`  
`WP2=-818.70 2627.16 door`  
`WP3=-735.19 2674.32 sell magus`  
`WP4=-805.75 2687.67`  
`WP5=-912.25 2725.55 example3 e t c`

An example mbwayplay command using the above sample ini file might be as follows:

`/mb mbwayplay example2 b t c`

This command would:

* (b)egin running a path called "example2".
* (t)rue to zone, so it looks to zone \(by the way, this is the same code that is used to zone when a bot is following

  a master\)

* (c\)hain paths, so at the end of the path it looks for another path \(in this case path:example3). The chained path

  would adhere to the same parameters you supplied for the original path (\(b\)egin, \(t\)rue to zone, and \(c)hain at the

  end\). So after the bot zones it looks for example3 and essentially runs this command: _/mb mbwayplay example3 b t c_

#### Example 2

You can run, zone, magus, doors, etc all through the mbwaypnt.ini file, here are some path examples, chaining path points together, and zone via a magus.

Here is how I chain pull paths together, in this case my APPath=Temple, this paticular one goes through a zone and depending on what my war has available for AE agro it will change is next path to templec or templeb.

`[Temple]`  
`WPLoop=TRUE`  
`WPCount=8`  
`WP1=-487.57 84.80`  
`WP2=-457 135.50`  
`WP3=-376.89 134.42 pull`  
`WP4=-342.92 185.42 pull`  
`WP5=-416.90 134.60 pull`  
`WP6=-423 135.50 pull`  
`WP7=-457 135.50`  
`WP8=-487.57 84.80 pull ${If[${Me.AltAbilityReady[Rampage]},TempleC,TempleB]}`  
`[TempleB]`  
`WPLoop=TRUE`  
`WPCount=16`  
`WP1=-493.40 107.57 pull`  
`WP2=-472.93 80.30`  
`WP3=-473.26 -8.07`  
`WP4=-473.26 -46.44`  
`WP5=-511.04 -40.25`  
`WP6=-540.99 -39.14`  
`WP7=-558.42 -56.79`  
`WP8=-558.51 -142.49 pull`  
`WP9=-557.79 -89.31`  
`WP10=-557.40 -57.87`  
`WP11=-542.29 -40.36`  
`WP12=-509.79 -40.31`  
`WP13=-472.97 -46.15`  
`WP14=-472.37 -7.35`  
`WP15=-472.23 73.72`  
`WP16=-479.21 98.21 pull`  
`[TempleC]`  
`WPLoop=TRUE`  
`WPCount=20`  
`WP1=-493.40 107.57 pull`  
`WP2=-472.93 80.30`  
`WP3=-473.26 -8.07`  
`WP4=-473.26 -46.44`  
`WP5=-511.04 -40.25`  
`WP6=-540.99 -39.14`  
`WP7=-597.76 -30.52`  
`WP8=-597.92 10.08`  
`WP9=-597.92 76.81`  
`WP10=-597.92 116.82`  
`WP11=-586.76 158.24 pull`  
`WP12=-597.32 111.05`  
`WP13=-597.92 10.08`  
`WP14=-597.76 -30.52`  
`WP15=-540.99 -39.14`  
`WP16=-511.04 -40.25`  
`WP17=-473.26 -46.44`  
`WP18=-473.26 -8.07`  
`WP19=-472.93 80.30`  
`WP20=-493.40 107.57 pull`

#### Example 3

For chaining across zones etc, this first one is one I used a lot doing LDoN's: /bct bob mbwayplay lfldongf b t c. To get him to go back you just /bct bob mbwayplay gftobb e t c

`[LFldonGF]`  
`WPCount=9`  
`WP1=-399.03 3640.92`  
`WP2=-387.84 1478.23`  
`WP3=-591.79 1209.10`  
`WP4=-379.89 -288.79`  
`WP5=335.06 -1134.56`  
`WP6=1976.01 -1141.98`  
`WP7=2109.76 -1113.65`  
`WP8=2156.90 -1209.03`  
`WP9=2166.85 -1206.41 GFtoBB b t c`  
`[GFtoBB]`  
`WPCount=8`  
`WP1=-2617.36 -1119.23 LFldonGF e`  
`WP2=-2251.29 -883.97`  
`WP3=-2028.63 -441.74`  
`WP4=-1747.35 1992.63`  
`WP5=-1541.93 2516.40`  
`WP6=-1571.55 2639.27`  
`WP7=-1636.02 2632.32`  
`WP8=-1637.63 2639.13 BBGFWayfarer e`  
`[BBGFWayfarer]`  
`WPCount=6`  
`WP1=-1101.67 -2476.26`  
`WP2=-1126.61 -2939.00`  
`WP3=-1125.30 -3054.35`  
`WP4=-1244.40 -3088.79`  
`WP5=-1315.14 -3053.25`  
`WP6=-1311.01 -3083.58 GFtoBB e t c`

#### Example 4

Here is an example of using a magus: /bct bob mbwayplay tonedaria b t c nedaria

`[ToNedaria]`  
`WPCount=3`  
`WP1=625.62 -178.34`  
`WP2=537.80 -99.15`  
`WP3=604.30 7.34 nedaria b`  
`[Nedaria]`  
`WPCount=10`  
`WP1=1142.86 1135.75`  
`WP2=1391.06 704.39`  
`WP3=1285.54 -266.96`  
`WP4=1299.90 -388.21`  
`WP5=1362.44 -465.12`  
`WP6=1461.15 -475.80`  
`WP7=1546.51 -496.26`  
`WP8=1581.54 -567.51`  
`WP9=1597.32 -628.35`  
`WP10=1659.85 -625.32`

[**Return to main ModBot Wiki**](https://macroquest.org/wiki/index.php/ModBot)

