---
tags:
   - macro
---
# ModBot

## **ModBot - A Universal Bot Macro**

* Caster
* Melee
* Shrouds & MM's
* Mez, Charm, Heal, Melee, etc
* All classes supported
* Now supports mixed groups of MQ2 and Non-MQ2 users/players
* ModBot is under constant improvement effort, open to suggestions / additions / adjustments, etc

[**ModBot\_v3.x Source**](https://macroquest2.com/phpBB3/viewtopic.php?t=15313)

**General Note on Wiki Entries - Release ZIP packages vs. SVN Updates** - While the majority of entries in the Wiki apply to ModBot in general, there are always some entries that apply to changes, additional functionality, new commands, etc. that exist only in the "beta" files from the SVN repository. Please keep this note in the back of your mind as you work with the Wiki - if you come across a command, etc. that will just not seem to work for you (and you have already _thoroughly_ researched it, checked syntax, re-checked syntax, etc.), please take a moment to check your version of the module that it applies to - you may need to update.

### Using the SVN Repository

For those of you that would like to use the beta files off of the SVN repository, you have two options - use your browser to grab files or use a tool like TortoiseSVN to automate the process a bit. Using the browser is pretty self-explanatory, but TortoiseSVN requires a bit of set up. This process covers what is needed for the Windows version: Links to the browser access and to SVN can be found at the bottom of this post.. [http://www.macroquest2.com/phpBB3/viewtopic.php?f=49&t=15313](http://www.macroquest2.com/phpBB3/viewtopic.php?f=49&t=15313)

1. Download and install [[http://tortoisesvn.net/downloads.html](http://tortoisesvn.net/downloads.html)**TortoiseSVN**].
2. Create a folder on your system where you want to store the downloaded ModBot files.
3. Right click on your newly created folder and select _SVN Checkout_ (right above the TortoiseSVN entry).
4. In the menu that comes up, input the [**URL of repository**](http://tools.assembla.com/svn/kroak/) and then click

   OK.

Once you've clicked OK, the folder will populate with everything on SVN. Any time you want to update the folder to newest revision, simply right click on the folder and select _SVN Update_ from the Tortoise menu.

## How To

To use ModBot

1. Extract and place all included files from zip (all .mac and .inc files) into your MQ2 macro directory.
2. From inside EQ, type /macro modbot (e.g. /macro modbot OR /macro modbot raidmode).

   This will build, if it doesn't exist, your MB\_.ini file. Optional entries will make a

   MB\_\_.ini. Being shrouded on startup without using an option will use your race and class for the

   creation of an MB\_\_.ini file.

3. From inside EQ, end the macro by typing /endmac
4. Tab out of EQ, locate your new MB\_.ini file in your macro directory, and open it. You can use the editor

   of your choice, but Notepad will work just fine.

5. For every component of the macro you want to use, increase the respective "count", if you want two heals, set

   AHCount=2, if you want 2 debuffs, set ADCount=2, etc. After you have set your counts, save and close the INI file.

6. Tab back over into EQ and restart the macro (/macro modbot). This will now populate your INI file based on the count

   entries that you made in the previous step

7. End the macro again by typing /endmac
8. Open the INI file once more and "tweak" the newly created entries to fit your needs. When you are done, save and

   close the INI file.

9. Tab back over to EQ and restart the macro.

Your bot should now be just that, a BOT and will listen to your every command (assuming you are the master).

For examples of complete class ModBot INI files, please go to the [example INI page](https://macroquest.org/wiki/index.php/Modbot_Class_INI_Examples).

**Please Note!!** One thing to keep in mind throughout the configuration of the ModBot INI file: **keep your most critical and most used spells, activities, etc., first in their respective INI sections.** You don't want your mez spell as Debuff number 20, you don't want slow as debuff 10, you don't want a CBT based buff as buff 23, and you don't want CH as heal 1 (you want your most desperate heal as heal 1), etc. Configure your heals, buffs, debuffs, etc. in a highest priority first order.

## Reference to Understanding the ModBot WiKi

`- Replace this with the respective descriptor`
`Example 1 -_is luclin_bobby`
`Example 2 -is bobby`

`(text) - These are "comments" and should be removed when saving the respective file`
`Example 1 - Send=1 (If set to 1 it will send netbots information over the network) This text:`
``````*``\(If`````set`````` `to` `1` `it` `will` `send` `netbots` `information` `over` `the` ``````network)``\*`should NOT appear in the INI file`
````` [text\] - This is to show different options or series of options`````` Example 1 - /bc cast\[, %t, grp,, etc]\`\`

## Plugin Requirements & Examples

I suggest you have a good understanding of how to configure each of these plugins. Any misconfiguration can have an adverse affect on the performance of ModBot

[MQ2EQBC & EQBCS](https://macroquest2.com/phpBB3/viewtopic.php?t=12147&start=0) (/cheer OmniCtrl and ascii38 for this plugin)

* 2/15/14 - [EQBCS Wiki](https://macroquest.org/wiki/index.php/MQ2EQBC) (with current code maintained by PMS)

[MQ2Cast](https://macroquest2.com/phpBB3/viewtopic.php?t=12758) (/cheer A\_Enchanter\_00 for this plugin)
\* ModBot will create a saved spell set using MQ2cast called ModBot2 and this information is stored in the MQ2Cast.INI file
\* 2/15/14 - MQ2Cast 10.x (does not require MQ2BagWindows\) can be found [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=19294). [MQ2NetBots](https://macroquest2.com/phpBB3/viewtopic.php?t=12186&start=0) \(/cheer S0rcier for this plugin)
Please use this copy for now. [http://tools.assembla.com/kroak/export/474/plugs/MQ2NetBots.cpp](http://tools.assembla.com/kroak/export/474/plugs/MQ2NetBots.cpp) The latest versions posted in the MQ2Netbots thread are stripped down copies that didn't address the real reason for the plugin locking up.

* The settings are located in \_.ini in your MQ2 directory\)

`/netbots on grab=on send=on`

[MQ2Melee](https://macroquest2.com/phpBB3/viewtopic.php?t=12779&start=0) (/cheer S0rcier for this plugin)
\* The settings are located in \_.ini in your MQ2 directory\)

`/melee plugin=1`

[MQ2Bandolier](https://macroquest2.com/phpBB3/viewtopic.php?t=12793&start=0) (/cheer wassup for this plugin)

* If you plan to use item swapping and spell foci items, you may need to configure "sets"
* 2/15/14 - MQ2Exchange 3.00 and MQ2Bandolier 3.00 (no BagWindow) from Woobs can be found

  [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=19300&sid=bb1e3ea9163fad3229378c543b6147ee). You may

  still need to use MQ2BagWindow and Moveitem.h to get MQ2Melee to compile.

[MQ2MoveUtils](https://macroquest2.com/phpBB3/viewtopic.php?t=11732&start=0) (/cheer outlander for this plugin)

* 2/16/14 Current version maintained by PMS can be found

  [here](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=15909).

[MQ2Exchange](https://macroquest2.com/phpBB3/viewtopic.php?t=7603) (/cheer wassup for this plugin)

* 2/15/14 - MQ2Exchange 3.00 and MQ2Bandolier 3.00 (no BagWindow) from Woobs can be found

  [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=19300&sid=bb1e3ea9163fad3229378c543b6147ee). You may

  still need to use MQ2BagWindow and Moveitem.h to get MQ2Melee to compile.

[MQ2Twist](https://macroquest2.com/phpBB3/viewtopic.php?p=64181#64181) (For Bards. /cheer Cr4zyb4rd and others for this plugin\) \(May also want to look at pages later in the thread.)

* 2/15/14 - [Current MQ2Twist Code](https://macroquest2.com/phpBB3/viewtopic.php?p=158925#p158925) from gse7en \(use

  this or the one a few posts down from dewey2461\)

#### Deprecated Plugins (no longer used with ModBot)

[MQ2NetHeal](https://macroquest2.com/phpBB3/viewtopic.php?t=12312&start=0) (/cheer S0rcier for this plugin)
(Elsewhere in the fourms it is frequently suggested to not use this plugin: /plugin mq2netheal unload then /plugin mq2netbots)

* The settings are located in \_.ini in your MQ2 directory\)

`/netheal on grab=on send=on`
`/netcure on`

* Note, the mq2netheal plugin is deprecated, and no longer needed for current release of modbot. It will, however

  continue to function the same with or without the plugin.. For heal related help, you must specify on the forums if

  you're using it.

### Plugin INI Examples

Example \_.INI for MQ2NetBots, MQ2NetHeal, MQ2Melee:

`[MQ2NetBots]`
`Stat=1`
`Grab=1`
`Send=1`

`[MQ2NetHeal]`
`Stat=1`
`Grab=1`
`Send=1`
`[MQ2NetCure]`
`Watch=1`

`[MQ2Melee]`
`backstab=50`
`disarm=1`
`enrage=1`
`evade=1`
`facing=1`
`hide=1`
`infuriate=1`
`melee=200`
`meleepri=`
`meleesec=`
`petlock=1`
`petmend=20`
`petrange=75`
`pickpocket=1`
`plugin=1`
`poker=`
`resume=20`
`sneak=1`
`standup=1`
`stickrange=200`
`hideif=${If[${Select[${MakeCamp},off]} || !${Defined[CampStatus]},0,1]}`
`sneakif=${If[${Select[${MakeCamp},off]} || !${Defined[CampStatus]},0,1]}`
`stickcmd=hold ${If[${Target.Height}<5,10,${Math.Calc[${Target.Height}+7].Int}]} ${If[!${Me.GroupSize} ||`
`${Melee.AggroMode},moveback,${If[${Melee.BackStabbing},behind,!front]}]} ${If[${Me.Underwater},uw,]}`
`version=3.999`

Example MQ2MoveUtils.INI for MQ2MoveUtils:

`[Defaults]`
`AutoPause=on`
`BreakOnWarp=on`
`BreakDist=250.0`
`BreakOnGate=on`
`Verbosity=1`
`stuckDist=0.8`
`turnDirection=10.0`
`stuckCheck=5`
`StuckLogic=off`

Example MQ2Bandolier\_.ini for MQ2Bandolier:

`[ThisSet]`
`17=12345`
`13=23456`
`14=34567`

Example MQ2Cast.INI for MQ2Cast:

`[SpellSet..]`
`ModBot2=123|1 456|2 789|3`

## ModBot HUD

`[_]`
`Last=ModBotHUD`
`SkipParse=7`
`CheckINI=100`
`UpdateInBackGround=on`
`ClassHUD=on`
`ZoneHUD=on`

`[ModBotHUD]`
`Target= 3,060,210,225,225,225,${If[${Target.ID},Dis:${Int[${Target.Distance}]}-Lvl:${Target.Level}-${Target.Class.ShortName}-${Target.PctHPs}%,]}`
`Name1= 3,060,220,240,240,000,${If[${NetBots.Counts}>=1,${NetBots.Client.Arg[1]} ${NetBots[${NetBots.Client.Arg[1]}].Level} XP:${Int[${NetBots[${NetBots.Client.Arg[1]}].PctExp}]} AXP:${Int[${NetBots[${NetBots.Client.Arg[1]}].PctAAExp}]},NA]}`
`HP1= 3,060,230,255,100,100,HP:${If[${NetBots.Counts}>=1,${NetBots[${NetBots.Client.Arg[1]}].PctHPs},]}%`
`Mana1= 3,105,230,100,100,255,M:${If[${NetBots.Counts}>=1,${NetBots[${NetBots.Client.Arg[1]}].PctMana},]}%`
`End1= 3,145,230,255,234,008,E:${If[${NetBots.Counts}>=1,${NetBots[${NetBots.Client.Arg[1]}].PctEndurance},]}%`
`Pet1= 3,185,230,255,255,255,Pet:${If[${NetBots.Counts}>=1 && ${NetBots[${NetBots.Client.Arg[1]}].PetID}>0,${NetBots[${NetBots.Client.Arg[1]}].PetHP},]}%`
`Name2= 3,060,240,240,240,000,${If[${NetBots.Counts}>=2,${NetBots.Client.Arg[2]} ${NetBots[${NetBots.Client.Arg[2]}].Level} XP:${Int[${NetBots[${NetBots.Client.Arg[2]}].PctExp}]} AXP:${Int[${NetBots[${NetBots.Client.Arg[2]}].PctAAExp}]},NA]}`
`HP2= 3,060,250,255,100,100,HP:${If[${NetBots.Counts}>=2,${NetBots[${NetBots.Client.Arg[2]}].PctHPs},]}%`
`Mana2= 3,105,250,100,100,255,M:${If[${NetBots.Counts}>=2,${NetBots[${NetBots.Client.Arg[2]}].PctMana},]}%`
`End2= 3,145,250,255,234,008,E:${If[${NetBots.Counts}>=2,${NetBots[${NetBots.Client.Arg[2]}].PctEndurance},]}%`
`Pet2= 3,185,250,255,255,255,Pet:${If[${NetBots.Counts}>=2 && ${NetBots[${NetBots.Client.Arg[2]}].PetID}>0,${NetBots[${NetBots.Client.Arg[2]}].PetHP},]}%`
`Name3= 3,060,260,240,240,000,${If[${NetBots.Counts}>=3,${NetBots.Client.Arg[3]} ${NetBots[${NetBots.Client.Arg[3]}].Level} XP:${Int[${NetBots[${NetBots.Client.Arg[3]}].PctExp}]} AXP:${Int[${NetBots[${NetBots.Client.Arg[3]}].PctAAExp}]},NA]}`
`HP3= 3,060,270,255,100,100,HP:${If[${NetBots.Counts}>=3,${NetBots[${NetBots.Client.Arg[3]}].PctHPs},]}%`
`Mana3= 3,105,270,100,100,255,M:${If[${NetBots.Counts}>=3,${NetBots[${NetBots.Client.Arg[3]}].PctMana},]}%`
`End3= 3,145,270,255,234,008,E:${If[${NetBots.Counts}>=3,${NetBots[${NetBots.Client.Arg[3]}].PctEndurance},]}%`
`Pet3= 3,185,270,255,255,255,Pet:${If[${NetBots.Counts}>=3 && ${NetBots[${NetBots.Client.Arg[3]}].PetID}>0,${NetBots[${NetBots.Client.Arg[3]}].PetHP},]}%`
`Name4= 3,060,280,240,240,000,${If[${NetBots.Counts}>=4,${NetBots.Client.Arg[4]} ${NetBots[${NetBots.Client.Arg[4]}].Level} XP:${Int[${NetBots[${NetBots.Client.Arg[4]}].PctExp}]} AXP:${Int[${NetBots[${NetBots.Client.Arg[4]}].PctAAExp}]},NA]}`
`HP4= 3,060,290,255,100,100,HP:${If[${NetBots.Counts}>=4,${NetBots[${NetBots.Client.Arg[4]}].PctHPs},]}%`
`Mana4= 3,105,290,100,100,255,M:${If[${NetBots.Counts}>=4,${NetBots[${NetBots.Client.Arg[4]}].PctMana},]}%`
`End4= 3,145,290,255,234,008,E:${If[${NetBots.Counts}>=4,${NetBots[${NetBots.Client.Arg[4]}].PctEndurance},]}%`
`Pet4= 3,185,290,255,255,255,Pet:${If[${NetBots.Counts}>=4 && ${NetBots[${NetBots.Client.Arg[4]}].PetID}>0,${NetBots[${NetBots.Client.Arg[4]}].PetHP},]}%`
`Name5= 3,060,300,240,240,000,${If[${NetBots.Counts}>=5,${NetBots.Client.Arg[5]} ${NetBots[${NetBots.Client.Arg[5]}].Level} XP:${Int[${NetBots[${NetBots.Client.Arg[5]}].PctExp}]} AXP:${Int[${NetBots[${NetBots.Client.Arg[5]}].PctAAExp}]},NA]}`
`HP5= 3,060,310,255,100,100,HP:${If[${NetBots.Counts}>=5,${NetBots[${NetBots.Client.Arg[5]}].PctHPs},]}%`
`Mana5= 3,105,310,100,100,255,M:${If[${NetBots.Counts}>=5,${NetBots[${NetBots.Client.Arg[5]}].PctMana},]}%`
`End5= 3,145,310,255,234,008,E:${If[${NetBots.Counts}>=5,${NetBots[${NetBots.Client.Arg[5]}].PctEndurance},]}%`
`Pet5= 3,185,310,255,255,255,Pet:${If[${NetBots.Counts}>=5 && ${NetBots[${NetBots.Client.Arg[5]}].PetID}>0,${NetBots[${NetBots.Client.Arg[5]}].PetHP},]}%`
`Name6= 3,060,320,240,240,000,${If[${NetBots.Counts}>=6,${NetBots.Client.Arg[6]} ${NetBots[${NetBots.Client.Arg[6]}].Level} XP:${Int[${NetBots[${NetBots.Client.Arg[6]}].PctExp}]} AXP:${Int[${NetBots[${NetBots.Client.Arg[6]}].PctAAExp}]},NA]}`
`HP6= 3,060,330,255,100,100,HP:${If[${NetBots.Counts}>=6,${NetBots[${NetBots.Client.Arg[6]}].PctHPs},]}%`
`Mana6= 3,105,330,100,100,255,M:${If[${NetBots.Counts}>=6,${NetBots[${NetBots.Client.Arg[6]}].PctMana},]}%`
`End6= 3,145,330,255,234,008,E:${If[${NetBots.Counts}>=6,${NetBots[${NetBots.Client.Arg[6]}].PctEndurance},]}%`
`Pet6= 3,185,330,255,255,255,Pet:${If[${NetBots.Counts}>=6 && ${NetBots[${NetBots.Client.Arg[6]}].PetID}>0,${NetBots[${NetBots.Client.Arg[6]}].PetHP},]}%`

## ModBot Commands & Syntax

ModBot commands are executed in a few different ways:

* /bc
* /bc
* /bct
* /bct

Are probably most common but check out the EQBC Forum thread for more methods / features.

You can also configure an alias so you can run modbot on the character you control and execute ModBot commands.

To create the alias you must run this from the EQ prompt:

* /alias /mb /echo mb-

Or change the LoadAlias variable in MBCommon.inc [Settings] section from 0 to 1 if you've lost the alias in your Macroquest.ini

With this alias you can tell your bot locally what to do:

* /mb makecamp
* /mb buffup
* /mb letsroll
* /mb

### Command Reference

_Section Updated: June 7, 2009_

* **abort** \(Interrupts any cast in progress, Sets - DoHeals, DoDebuffs & DoMelee FALSE and follows the sender

  closely, usefull when you want to RUN away\)

* **addbuff "\\|\" ABSpellAlias ABTarType** \(Adds a new buff entry to the

  character's INI file.\)

  * You must restart the ModBot macro after executing the addbuff command in order to complete the adding of the

    buff entry.

  * The Spellname, etc. section can be entered directly \(e.g. \*/mb addbuff "Bone Mask of the Ancient Iksar\|item"

    iksar self_\) or, if adding a clicky, by holding the item on your cursor \(e.g._ /mb addbuff

    "${Cursor.Name}\|item" iksar self\*\). Please note that the quotes around the spellname\|gem section are required.

  * ABTarType will accept multiple targets if quotes are used \(e.g. \*/mb addbuff "Levitiation\|gem1" levi "war mnk

    rog"\*\).

  * addbuff execution will add ABGem, ABSpell, ABSpellAlias and ABTarType entries to the characters INI file. The

    remaining buff lines (ABSpellFociX, ABDurModX, etc.) will be added once you restart the ModBot macro \(the array

    size change (ABCount\) will also not increment until after re-start). For example, using these Bonemask example

    command, the following entires will be added to the INI file \(where "X" is equal to whatever the next numbered

    entry is in your advbuff section\):

ABGemX=item

ABSpellX=Bone Mask of the Ancient Iksar

ABSpellAliasX=iksar

ABTarTypeX=self

* **attack** (Sets DoMelee TRUE and forces bot to attack the TankName's target)
* **attack** (Sets DoMelee TRUE and forces bot to attack the target)

  \* Note: OffTank must be TRUE to use this option (I may remove this requirement though TBD)

  \* Example 1 - /bc attack badguy

  \* Example 2 = /bc attack badguy 100 20

* **buffup** (This will set DoBuffs & DoEvents TRUE & DoHeals FALSE)
* **campout** (Performs a /camp desktop and ends the macro)
* **cast  &lt;on/off&gt;** (This will disable or enable the spell associated with this alias)
* **cast [&lt;spawnname/id&gt; \&lt;%t&gt; \] \[&lt;spawnname/id&gt; \&lt;%t&gt; ] (infinte)**
  * If the spell is detrimental, CAST targets the requester's target.
  * If the spell is beneficial, it targets the sender or, if _grp_ is present, it casts buff on group members.
  * If _%t_ is present, it targets the requester's target.
  * The cast command will ignore INI settings for things like minmana, maxmana, recasts, buff debuff counters, etc.

    This command is mainly used for manual, "one off" type casts.

`Example 1 - /bc cast buffhp grp haste bob haste jane dmgshld bob`
`Example 2 - /bc cast dmgshld bob nuke tash`
`Example 3 - /bc cast slow "nasty add"`

* **doafk** [on, true, off, false, ]
* **dobuffbot** [on, true, off, false, ] \(Places the bot in "BuffBot Mode".

  Currently once set to on or true, it will NOT turn off and you MUST restart the macro to "quit" this mode. It will

  cast any spell alias on the requesting target. The requester must be a "master". Example: _/t buffhp_

* **dobuffs** [on, true, off, false, ]
* **docombines** (Toggle that turns docombines on/off \(default off). Docombines will check for an open tradeskill

  window with an enabled combine button (you have to select recipe), and will click the button. Upon a successful

  combine, Modbot's built in cursor handling takes over. Useful for tank to summon more arrows during fight. An

  associated event will fire and toggle docombines to FALSE when you run out of recipe components.\)

* **docures** [on, true, off, false, ]
* **dodebuffs** [on, true, off, false, ]
* **doevents** [on, true, off, false, ]
* **doforage** [on, true, off, false, ]
* **dofw** [on, true, off, false, ]
* **doheals** [on, true, off, false, ]
* **dolist** (Used to /bc out the existing "Do" status)
* **doloot** [on, true, off, false, ]
* **domelee** [on, true, off, false, ]
* **domount** [on, true, off, false, ] \(To cast a mount or not, used in conjunction

  with MountCast INI entry\)

* **dopet** [on, true, off, false, ] \(To cast a pet or not, used in conjunction

  with PetCast INI entry\)

* **dopull** [on, true, off, false, ] (not fully production yet)
* **dopull &lt;on/off/path&gt;** (Self explanatory. See the instructions on forums.)
* **doquest** [on,true,off,false] \(Default is TRUE. If set to FALSE, your looter will ignore items marked "quest"

  and still loot other items.\)

  * Can be used to add quest items to your loot.ini file. For example, while holding an item on cursor, \*/mb doquest

    4 Hair of the Dog\* will set the item you're holding to "=Quest\|4\|Hair of the Dog\|" in loot.ini.

  * Can also be used in conjunction with the _QuestOnly_ variable \(found in the setting section of the loot.ini

    file\). If both doquest and QuestOnly are set to TRUE, your toon will only loot quest items. Also note that if

    _QuestOnly_ is set to TRUE and doquest is set to FALSE, your toon will only loot cash off of mobs.

  * Please see the modloot section found

    [**here**](https://macroquest.org/wiki/index.php/Related_Include_Files#Modloot) for more information on the

    loot.ini file.

* **dosit** [on, true, off, false, ]
* **dosongs** [on, true, off, false, ] (used for bards only)
* **dotells** [on, true, off, false, ] \(Toggles a beep when tells are recieved from

  non-netbots toons. Useful for tells in background sessions\)

* **exclude \** \(Adds to alert list, to save list you must use the "save" option, otherwise

  it will not be written to the INI file\)

  * The exclude list is dynamic and will only exclude mobs that are present in the zone AND that are on the list.
  * If you want to force an exclude you must edit the INI file and place a "\#" in front of the mobs name \(e.g.

    ExcludeList=a dusty barrel\|a dark coffin\|\#a bitten victim\|a hollow tree\|, this will always force "a bitten

    victim" to be on the exclude list\)

  * Use the following commands from a character to add mobs to the exclude list \(Kroak suggested just tossing this

    in a two-line hotkey\):

    * _/bcaa //mb exclude ${Target.CleanName}_ Will write the exclusion to a string that is checked through the

      debuff loop

    * _/bcaa //mb exclude save_ Will write the exclusion in the mbcommon.ini and that exclusion includes the zone

      id, so mobs of the same name in a different zone are NOT excluded. You shouldn't have to re-run the macro

      after an exclude but if you do this in the midst of comabat or something, while mobs are near, it may not

      "take" as quickly.

  * For mob names with spaces in them, simply enter the name without any quotations. For example:
    * ''/bcaa //mb exclude a small bat
  * See the _Include_ command (found below) to temporarily remove a mob from the alert list

* **follow** (Follows the sender or )
* **follow close** (Follows the sender within 3 steps, very close)
* **give** (Calls the sub GiveCheck to hand an item to a toon or NPC.)
  * ItemCount is optional and will default to 1.
  * The give command can be used in conjunction with categories that have been defined in the loot.ini. For

    instance, if you have items marked 'SpellScroll' in your loot.ini, and the Category variable has "SpellScroll"

    included, you can issue the give command as follows: _/mb give Bob SpellScroll TRUE_. The result will be that

    all items on your toon that are marked with that category (SpellScroll\) in your loot.ini will be handed to Bob.)
* **goto**   (Bot will move to the loc given)
* **handin** \(Target an NPC or PC, get one item on your cursor, and all of that item will be handed to them and trade

  or give button pressed.\)

* **holdup** (This will set DoBuffs,DoDebuffs,DoEvents,DoMelee all to FALSE)
* **include**  (Removes  from alert list, this will not save to the INI file, see exclude save)
* **letsroll** (This will set DoBuffs,DoHeals,DoMelee,DoEvents,DoDebuffs TRUE)
* **makecamp** \(This will Makecamp at existing location. Use _/makecamp off_ or _/mb stop_ to toggle makecamp

  functionality off\)

* **mana** (Used to /bc out the existing Mana % of the bot)
* **mbpause** or **mbp** [on, true, off, false, ] \(Used to pause or unpause the

  macro\)

* **mbwayplay** \(Used to playback previously recorded paths / waypoints, through zones, doors, chaining

  paths, etc.\)

* **mbwayrec** (Used to record a path / waypoint.)
  * Once started, ducking for each location will add a waypoint to the path.
  * Sitting stops path recording and returns to modbot functions.
  * To add doors, chains, pull locations, etc. you'll need to edit the MBWayPlay.INI file
  * Further information about mbwayplay and mbwayrec (along with examples) can be found

    [**here**](https://macroquest.org/wiki/index.php/Related_Include_Files#ModMove) in the wiki.
* **offtank &lt;on/off&gt;** (Toggles offtanking for dealing with adds.)
* **script** \(This will allow you to run custom commands while the macro is running, or

  combine series of commands, see script examples in manual / rev notes\)

* **sell** \(You must be within range of a merchant in order to function, it will sell loot marked as

  "=SELL" in the loot.ini file\)

* **sell** \(With NPC targeted will attempt to sell all items marked "sell" in your lootIni file to

  target. Otherwise optional target name can be supplied.\)

* **setinivar** (This will find and change any setting in your .ini)
  * Note that this command will have trouble with script settings if you have more than one \(it will set the first

    C1= or whatever that it comes to.

  * Variables changed in the .ini are /varset with the macro running
  * Spells, gems, etc. will not be set unless you use the array correctly for . In other words,

    ADGem[1] is not the same as ADGem1:

    * Use ADGem[1] and this will set the ADGem1 .ini setting and varset the change to memory.
    * Use ADGem1 and it will only change the .ini.

  * This still has a problem finding variables in very long sections. If /echo ${Ini\[${IniFile},

    \]} is over the MAX\_STRING value - (You go LD typing that if it is\). - Stuff like ABGem[20] is almost never found. \(Still working on that.)

For example, Ligament Slice for a rogue was set up from in-game with these commands typed in to the MQ window (and the rogue was able to put it immediately to use):

/mb setinivar ADCount 4

_(restart macro - had 0 count before)_

/mb setinivar ADGem[1] alt

/mb setinivar ADSpell[1] Ligament Slice

/mb setinivar ADTarBegHP[1] 40

/mb setinivar ADTarCnt[1] 1

/mb setinivar ADTarType[1] 1

/mb setinivar ADAnnounce[1] /bc

/mb setinivar ADSpellAlias[1] snare

* **sing** \(Will sing this song and add the respective gem number to the Twist.List, it attempts to use

  detrimental as the qualifier to add it to combat songs, or rest songs\)

* **stop** (Will stop following and/or stop in place)
* **sung** \(Will remove this song from the respective Twist.List, it attempts to use detrimental as the

  qualifier to remove it from combat songs, or rest songs\)

## ModBot in game usage and commands

`Example commands:`
`/bc Bob follow me [This tells bob and only bob to follow me]`
`/bc cast dd [this tells every bot to cast the spell alias dd]`
`/bc shamandude cast buffsta grp buffhp focus grp buffhp %T [buffsta on the group, buffhp on the requester, focus on the group, buffhp on requesters target]`
`/bc necroguy makecamp [this tells "necroguy" to makecamp]`
`/bc campout [tells all bots to camp to desktop]`
`/bc exclude ${Target.CleanName} [tells all bots to add your target to the exclude / ignore list, toons will not attack any spawn with that name.]`
`/bc clericname dobuffs on [tells the cleric to set DoBuffs to true and will then begin buffing group]`
`/bc pallyguy cast bmb %t buffhp grp [bmb on requesters target, buffhp on the group]`

`Typical commands sequence for an EXP group:`
`/bc letsroll`
`/bc makecamp`
`You then begin to pull mobs and they will react accordingly.`

`Mobile Camp Example:`
`/bc follow`
`/bc buffup`
`[once ready zone into the instance]`
`/bc stop`
`/bc letsroll`
`[clear first room lets say]`
`/bc follow`
`[move to next room]`
`/bc makecamp`
`[etc, repeat]`

`Example movement options with or without invis`
`/bc mbp on`
`/bc follow`

`Make a EQBC Channel and do things like (using this technique you don't even have to be a master)`
`/bct mycoolchannelname //mb letsroll`
`/bct mycoolchannelname //mb campout`

## ModBot INI Settings

### PreFace Notes

* Spell Alias's must be unique across all alias's

  Obsolete? 06272011 -Changed - ?

`"cast" command usage now allows for multiple aliases. If you have several spells with the same alias, using /bc castwill now cast all spells marked.`
`Example, for shaman you can have Fo7, Talisman of Boar, Talisman of Wrulan, Talisman of Tribunal, ect.. all marked with "fullgroup". "/mb cast fullgroup" will`
`cast each spell in the order they are found in the .ini file.`
````` Buffing -```Group buffs can now be seperated to different classes, and will allow keeping the spell on netbots members in seperate groups from the caster with the inclusion of keyword````` "raid". Example -\`

```text
`ABSpell2=Focus of the Seventh`
`ABSpellFoci2=`
`ABDurMod2=50`
`ABSpellAlias2=fo7|grpfocus|fullgroup`
`ABAnnounce2=`
`ABSpellMinMana2=20`
`ABTarCnt2=2`
`ABTarType2=war shd pal rng mnk rog brd bst ber shm dru wiz mag enc nec raid`
`ABRecast2=FALSE`
`ABSpellIcon2=`
`ABPreCondition2=TRUE`
````` Note from the above example that clr is not included in the TarType.. My clerics have the spell blocked. Attempting to cast on them will cause a chain loop of ```casting until the cleric gets self buff on that doesn't "stack" with focus. - so watch spell stacking and make sure to set your toons accordingly.``
````` Old format of "self" will also work with no change if you don't want to buff other groups with the spell.
```

`Commands -`
`Tell commands will now check buff aliases, and don't need "cast" to ask for buffs.. "/tellfullgroup" from a non-master toon will make the shaman cast`
`every spell with that alias on the sender of the tell. Masters still require use of "cast". - This does allow guildies or whoever else knows your aliases to get`
`buffs easily.`
`/say is not affected and is still not enabled for modbot.`
````` Added "docommand" -```Master toons that aren't in netbots can now directly command toons. "/telldocommand /sit" will make the receiving toon sit, or execute any command after````` the "docommand" keyword. - Word of caution - You can cause macro errors with this if you aren't careful. The command sent is executed directly with /docommand in the macro.```A tell received of "/telldocommand /sit" will locally execute "/docommand /sit" Watch extra characters and or brackets.. - Because of the nature of this one,``
`the commanding toon MUST be listed in MasterList.`

* You should be familiar or at least capable of making MQ2Bandolier sets as they are used by MQ2Cast for "foci"

  items

* Please treat the Buff, Debuff, Event, Heal INI sections as a first in first out (FIFO). Highest priority to lowest

  priority, you don't want mez or slow as ADSpell12 but as ADSpell1. You don't want AHHeal1 as Complete Heal, you want

  AHHeal1 to be DA/DB (those are examples, use common sense)

* If you want to add some visual zip to your announcements (things are easy to miss in /bc..), you can use color

  coding and the like in any of your Announce settings. For example, \*ADAnnounce1=/bc [+r+\]Group Mez\[+x+]

  \&lt;\&lt;[+y+\] %t \[+x+\]&gt;&gt; with\[+g+\] %s \[+x+]\* will produce a line in the MQ chat window that is MUCH easier to

  see than the regular fonts.

* Rk. XX Usage - Heals, buffs, debuffs, and cures have code added to check your book and find the correct version of

  the spell you're using on startup of modbot. Rk. II and Rk. III are not needed, but only for these sections. If you

  upgrade a normal spell in these sections to Rk. II or III, restarting the macro will make the new spell work. Please

  note that this does not apply to discs, potionbelt, abilities, or PetCast at this time \(meaning you must include the

  Rk. XX in the spell name for these types\).

* Setting spell duration modifications (AHDurMod, ADDurMod, ABDurMod, AEDurMod) - Use the following formula to

  determine what number to set your DurMod at:

${Spell[X\].Duration} \* (${AHDurModX}+${Spell\[X].Duration}) == timer duration.

So if you want a 25% extension on the timer, set durmod to 25 to make ${Spell[X].Duration} \* 1.25 = timer. Modbot shouldn't re-cast if timer is still running.

### References

* tnt = TankName Target
* grp = group

### Settings Section [Settings]

* **DoMelee=TRUE\|FALSE**
* **DoHeals=TRUE\|FALSE**
* **DoBuffs=TRUE\|FALSE**
* **DoDebuffs=TRUE\|FALSE**
* **DoEvents=TRUE\|FALSE**
* **DoCures=TRUE\|FALSE**
* **DoPull=TRUE\|FALSE**
* **DoPet=TRUE\|FALSE**
  * Must have a buff entry for creating a pet (in the AdvBuff section - see note for ABTarType). Also see note for

    Cleric pets under PetCast below.
* **DoSit=TRUE\|FALSE**
* **DoLoot=TRUE\|FALSE**
* **DoFW=TRUE\|FALSE**
  * Should I cast spells for food and water. (see FoodSpell and DrinkSpell entries)
* **DoForage=TRUE\|FALSE**
* **ForageIni=name of ini file for forage**
  * Defaults to _forage.ini_. Please see the Related include files page for more information on the Forage.ini file.
* **DoAfk=TRUE\|FALSE**
* **DoMount=TRUE\|FALSE**
  * If set to TRUE, you must complete the _MountCast_ entry below.
* **MountCast=Spell/Item name/AA name\|gem \#,item,alt**
  * Use MQ2Cast syntax without quotes. Examples:
    * MountCast=Collapsable Roboboar\|item
* **MasterList=PC Name,PC Name**
  * Comma delimited list of names. Can also use _${NetBots.Client}_ to designate that any chars using NetBots can

    act as master. Examples:

    * MasterList=Bigbob,Sooper
    * MasterList=${NetBots.Client}
* **TankName=PC Name,PC Name**
  * Comma delimited list of names. This variable will also be set when you designate a character using either the

    Main Tank or Main Assist group roles.

  * Can also use ${Group.MainTank.Name} to auto set this to whomever is set in the group main tank role. Examples:
    * TankName=Billytank,Larrytank
    * TankName=${Group.MainTank.Name}
* **Radius=\#**
  * Radius that I will monitor for NPCs. If you are having issues with your characters not casting buffs, etc. while

    not in combat, try adjusting the Radius setting down a bit to make certain that they are not pickng non-aggro

    mobs in the surrounding area. Example:

    * Radius=100
* **ExcludeList=npcname\|npcname\|**
  * Pipe delimited names to exclude. Please note that you must have a Pipe "\|" at the end. Example:
    * ExcludeList=a hollow tree\|a broken barrel\|
* **SitAggroRadiusCheck=\#**
  * Radius to check for aggro to see if I can sit. Default is 75.
* **AfkMessage=afk message**
  * Enter a custom AFK message if desired (leave blank for no AFK message).
  * Default is "Not now, thanks".
* **DeathSlot=TRUE\|FALSE**
  * Will only be true if your bot needs to camp to desktop to save res timer. This way the macro will know if you

    died and had to camp out.
* **NetworkIni=Path and filename of ini file**
  * Option for a network based INI file for scripts and path playback (mbwayplay and mbwaypnt.ini file).
  * File must be prefixed by "Network-" or "Net-"
  * Example: _NetworkINI=X:\shared\modbot\mb\_network.ini_
* **TraderName=toon name\|bazaar trader**
  * For use with the Campout command. Example:
    * _/bc campout trader_ will log in whatever toon you have set in the TraderName variable.
  * Second argument (_\|bazaar trader_) will log in the toon and run the bazaar macro with the trader option \(or any

    other mac+options you want there.\)
* **FollowDistance=\#**
  * Designates how far you will stay from followee.
  * Default 20.
* **FollowStick=MQMoveUtils Options**
  * If using MQ2MoveUtils, enter the options that you would like to use. Default 20 hold uw. Example:
    * FollowStick=20 hold uw
* **PetAggro=TRUE\|FALSE**
  * TRUE - pet taunt on
  * FALSE - pet taunt off
* **PetAssist=[1]**
  * Assist and pet attack or not
* **PetFoci=[-bandolier\|petfoci]**
  * Any spell foci you want to swap in for this spell using MQ2Cast syntax, you must have previously created the set

    via the MQ2Bandolier plugin /createset command.
* **PetShrinkSpell=pet shrink spell name\|gem\#**
  * Spell to be used to shrink your pet. Leave blank if you don't want your pet shrunk. Example:
    * PetShrinkSpell=Tiny Companion\|gem9
* **GoMNuke/GoRMNuke/GoERMNuke/GoDERMNuke=[]**
  * GoMNuke, GoRMNuke, GoERMNuke and GoDERMnuke will only appear if the toon has the AA available upon startup.

    These settings only require the \* ALIAS \* of the debuff you want to be "cast" on the MA's target when the

    event fires. No script required.
* \*\*SummonFood=spell name,item name,alt

  name\|gem\#,item,alt&lt;/span&gt;\*\*

  * These entries appear when _DoFW_ is set to TRUE. Use MQ2Cast syntax for spell entry. Example:
    * SummonFood=Summon Food\|gem12

* \*\*SummonDrink=spell name,item name,alt

  name\|gem\#,item,alt&lt;/span&gt;\*\*

  * MQ2Cast syntax. Example:
    * SummonDrink=Summon Drink\|gem8

**Deprecated Entries**

* **DoAura**=[TRUE,FALSE] (Must have a completed AuraCast entry below) **DEPRICATED!!** Set up aura as a buff with

  'self aura' as the ABTarType.

* **AuraCast**=[\\|\,item,alt&gt;] (Example: Uber Aura\|gem3) - **DEPRICATED!** Set up aura

  as a buff with 'self aura' as ABTarType. Use MQ2Cast syntax without quotes.

* **PetCast=\|gem\&lt;\#&gt;\|(for Suspended Minion II)\]** \(PLEASE NOTE: As of 3.499 beta, PetCast is

  no longer needed. You can now add pet to "AB" section by setting ABTarTypeX=petspell (or petcast). Pets won't be

  cast unless DoBuffs and DoPet are true. Also shouldn't cast if in combat unless "cbt" is included in ABTarType. When

  used with modbuff, Persistent Minion is also used automatically if you have it, and no extra entry needed. Original

  entry: Spell to cast to create / recall pet. Example: _PetCast=Animate Dead\|gem8\|smii_ \(Mainly MQ2Cast syntax

  without quotes\)\)

  * Can also use for charming:
    * \[charm \&lt;NPC type 0=any 1=undead,vampyre 2=animal 3=summoned 4=\(specify name

      type\)&gt; \]

    * Example: _PetCast=charm 4 4 "lowland basilisk,a emerald drake"_
  * For Cleric Hammer type pets that you only want to cast / have while in combat, you MUST have DoPet set to False

    AND have PetCast=\|\,item,alt&gt;\)

### AdvMelee [Melee]

* **OffTank=TRUE\|FALSE**
  * False - attack the MA target only
  * True - assist MA and then not change targets
* **ACLeash=\#**
  * The farthest the bot will move from where he is to engage a mob. However if "TankName" stays within 20 steps,

    the bot will exceed this leash.
* **ACAssistPct=\#**
  * Assist when target HP is this or less. Melee characters will engage at this point and caster pets will be sent

    in.
* **ACManaPct=\#**
  * Stop assisting when Mana drops below this.
    * Set to 0 for melee only
    * Set to 101 for non-melee casters
* **ACAnnounce=channel**
  * Channel to announce in, or leave blank for no announce. Example:
    * _ACAnnounce=/bc_ Will announce in MQ/EQBC window
    * _ACAnnounce=/g_ Will announce in group chat
* **ACMeleeCmd=command**
  * Use to set MQ2Melee commands. Example:
    * _ACMeleeCmd=/melee plugin=1_
* **ACBefore=script**
  * Special script code to execute before you engage. Example:
    * \*ACBefore=/if \({ACMATarget} && {Spawn[{ACMATarget}\].Type.Equal\[NPC]} &&

      {Spawn[{ACMATarget}\].Distance3D}\&lt;={ACLeash} && {Me.CombatAbilityReady\[Sneak Attack]} && {Me.Invis} &&

      {Me.Sneaking} && {Me.PctEndurance}&gt;40 && !{Me.Moving}\) /call mbscript SneakAttack\*

    * _ACBefore=/if (!{Me.Pet.ID}) /casting ''{PetCast}''_ \&lt;-- cleric pet hammer example
* **ACAfter=script**
  * Special script code to execute after you leave combat. Uses same script format as ACBefore.

### AdvHeal Section [AdvHeal]

Please note that for FD class toons and ${Group.Puller} - If they are out of ACLeash range and not FD, they will not be healed (to prevent aggro on group), but only if healer is not in 'combat' combatstate. If you have the newest NetBots from SVN, another check will be done on the _NetBots[].CombatState_ that needs healing. If not in combat they will be healed.

For group heal spells, you must set the AHTarCnt to something greater than 1 in order for the spell to evaluate correctly (and be used as a "group" heal when more than one member of the group requires healing\). For instance, if you have AHTarCnt=3, then at least 3 members of your group will need to be below the HP level that you set in the AHClass line. A possible issue may arise when the cleric is in a loop state where a single heal is being fired \(AHHealMode\) - it may take a bit for it to realize the single heal should be stopped and the group heal cast instead. Depending on how you have it configured, the use of AHHealMode can force it to not even check the your group heal spell as it's being told to only check one \(the single heal\). If this is the case \(and not the desired result), perhaps use the group heal as the spell to check in AHHealMode.

* **AHCount=\#**
  * Number of heals you plan to have.
* **AHCheckTime=\#**
  * How often to check for heals in seconds.
* **AHHealOOBC=TRUE\|FALSE**
  * Do I heal characters outside of Netbots and EQBC (e.g. folks not running MQ2 or mercenaries.)

`AHHealOOBC`
`Thinking of an english name for that setting, all that comes up is "Heal Outside Of BC".`
`So, in other words, if the setting is FALSE, it won't heal anyone that's not on YOUR EQBC server with the netbots plugin set up correctly, even if they're in your group.`
`That is why I recommend you connect all toons and run modbot on all of them at least once, even if you don't plan to run it as a regular thing for the other toons.. It assures the plugins are set correctly.`
`If AHHealOOBC=TRUE, then modbot will heal group members and pets even if there's no netbots connection.`
`Out of group healing can only be done by the macro if there's a netbots connection, or if the other toon is a master and uses the cast command via /tell.`
`I do recommend AHHealOOBC=TRUE setting, but I still left the default FALSE so people could check their connections before setting TRUE.`

* **AHHealMode=\#\|\#\|\#**
  * 0 or 1 (off or on)\|Heal \#\|Timer
  * This will keep the toon in the heal loop after casting  to check for additional heals for the duration

    of .
* **AHInterruptLevel=\#**
  * Lowest interruptable spell. For example, AHHealSpell1 will never interrupt if this is set to 2.
* **AHClassPriority=class names**
  * Set class healing priority (e.g. if you're currently healing a chanter, you won't interrupt for a monk).
    * Allowed entires are: enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk \(or any combination

      thereof\)
* **AHAllowDismount=TRUE\|FALSE**
  * Designate whether your toon should dismount (or not) to interrupt a spell to cast a heal
  * TRUE - allow toon to dismount if necessary to interrupt a spell cast in order to fire off a heal.
  * FALSE - your toon will never dismount to interrupt a spell.
* **AHGem[x]=source**
  * Designate what the source of the spell is.
  * Valid entries: gem number, alt, ability, item, script, potionbelt
  * Note that 'potionbelt' does not require a slot number.
  * Examples:
    * _AHGem1=3_ Cast this spell from gem 3
    * _AHGem1=alt_ This spell is an alternative advancement ability
* **AHSpell[x]=source name**
  * Valid entries: spell name, item name, alternate ability name, ability name, script name
  * Examples:
    * _AHSpell1=Superior Healing_ This would be generally be paired with an AHGem1 entry indicating which spell

      gem to cast Superior Healing from.

    * _AHSpell1=Healing Thingy of Uberness_ This would be generally be paired with an AHGem1 entry indicating that

      the source of this spell is an item.
* **AHSpellFoci[x]=setname**
  * Bandolier set name to swap in before casting this heal.
  * Please see MQ2Bandolier and MQ2Cast to understand how to use swap sets.
* **AHDurMod[x]=\#\#**
  * Any spell extension percentage, e.g. 05 (for 5%\), 25 \(for 25%).
  * Due to how spell durations / extensions are calculated, you may need to enter extensions in excessive of 100%

    (e.g. a 25% extension would be entered here as 125). Check your results in game to make sure you have set the

    correct extension.
* **AHSpellMinMana[x]=\#**
  * Minimum mana percentage to have in order to attempt this heal (e.g. 05 \(for 5%\), 25 \(for 25%)
* **AHSpellAlias[x]=spell alias**
  * Alias name for the heal.
  * Please note that you can NOT have spaces in your alias names.
* **AHAnnounce[x]=channel**
  * Channel to announce in, or leave blank for no announce. See ACAnnounce description in the AdvMelee section for

    further explanation.
* **AHTarCnt[x]=\#**
  * Designate how many targets are required to cast this spell.
* **AHClass[x]=class name(s)**
  * Valid entries: pc pet group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec tnt mypet self

    (or some combination there of). Please see the MQ2NetHeal plugin for full options. Please also note the

    following combination restrictions:

    * _pc_ \&lt;-- will include pc's and mercs. Leave pet out to ONLY heal PC's and mercs.
    * _pet_ \&lt;-- will include pets. Leave pc option out for pet only heals.
    * _group_ \&lt;-- will exclude everyone that is not in your group
    * _hp0_ \&lt;-- set an overall health percentage for any named classes
    * _classnames (war, shd, etc.)_ \&lt;-- used to declare which classes this heal should apply to. Can also be

      combined with a health persentage (e.g. bst50).

    * _mypet_ to be used by itself (e.g. set up a seperate heal for your pet)
    * _tnt_ \&lt;-- Tankname target. Use for lifetap spells ONLY.
    * _self_ \&lt;-- Only use _self_ if the heal spell is SELF ONLY, or only to be cast on yourself. This setting is

      exclusive and other targets will not be checked for that spell.
* **AHPreCondition[x]=TRUE\|FALSE\|PR**
  * Defaults to TRUE
  * _PR_ (only to be used with NetBots) If AHPreCondition[x]=PR, then for that particular heal there will be a

    check on target (over NetBots) for any PR type spell. If target has a PR buff on, then the heal will be skipped.

    Please note that the PR setting does not currently account for the duration remaining of the PR buff.

    AHPreConditionX=PR will check for these spell ID's:

    * 9755 (Promised Renewal)
    * 9756 (Promised Renewal Rk. II)
    * 9757 (Promised Renewal Rk. III)
    * 18270 (Promised Recuperation)
    * 18271 (Promised Recuperation Rk. II)
    * 18272 Promised Recuperation Rk. III\)

### AdvDebuff Section [AdvDebuff]

* **ADCount=\#**
  * Number of debuffs you plan to have.
* **ADMobMax=\#**
  * This is the array size where the valid mob ID's are stored after found. The loop to find valid mobs uses

    SpawnCount, then stores the mobs it "finds" in the array. Setting this to 20 or 30 should be way more than

    enough ever. It is best to keep this setting (and therefor the array) relative small for memory purposes \(as

    well as for speed through the debuff loop\).

  * If your toons are ignoring NPCs, this number may be set too low. First thing to check!!
* **ADCheckTime=\#**
  * How often to check for debuffs in seconds.
  * "It's the forced delay or timer between allowing that section of the macro to execute again.. Set higher for

    toons you want to have more emphasis somewhere else.. Like a cleric can be 8 for debuffs and 0 for heals, but a

    shammy you'd want 0 for debuffs. 0 = no forced delay. Speed still varies depending on the size of the loops or

    how many heals, debuffs, ect are in each section." - toomanynames
* **ADAggroOnly=1\|0**
  * 1 - only add mobs to the mob list if someone in your group or in netbots is the mob's target. Only use this

    option on bots that cast on targets that are NOT the main assist's target (e.g. chanter mezzing adds).

  * Please note: _ADAggroOnly_ is not terribly reliable at times. If you are having issues with one of your bots

    auto-aggroing mobs (when they are not the tank), try setting ADAggroOnly=0 and then ADTarType=1 or 11.
* **ADHold=0\|1\|1\|**
  * 1=on 0=off\|Debuff spell \#\|Time to wait for debuff\|
  * This is used much like the AHHealMode setting, but only for type 12 debuffs. Sets a timer to hold the toon in

    the debuff loop (no buffs or events) until the debuff is complete.
* **ADGem[x]=source**
  * Designate what the source of the spell is.
  * Valid entries: gem number, alt, ability, item, script, potionbelt
  * Note that 'potionbelt' does not require a slot number.
  * Examples:
    * _ADGem1=3_ Cast this spell from gem 3
    * _ADGem1=alt_ This spell is an alternative advancement ability
* **ADSpell[x]=source name**
  * Valid entries: spell name, item name, alternate ability name, ability name, script name
  * Examples:
    * _ADSpell1=Ensnare_ This would be generally be paired with an ADGem1 entry indicating which spell gem to cast

      Ensnare from.

    * _ADSpell1=Bangy Thingy of Uberness_ This would be generally be paired with an ADGem1 entry indicating that

      the source of this spell is an item.
* **ADSpellFoci[x]=setname**
  * Bandolier set name to swap in before casting this spell. Please see MQ2Bandolier and MQ2Cast to understand how

    to use swap sets.
* **ADDurMod[x]=\#\#**
  * Any spell extension percentage, e.g. 05 (for 5%\), 25 \(for 25%).
  * Due to how spell durations / extensions are calculated, you may need to enter extensions in excess of 100% \(e.g.

    a 25% extension would be entered here as 125\). Check your results in game to make sure you have set the correct

    extension.
* **ADSpellAlias[x]=spell alias**
  * Alias name for the spell. Please note that you can NOT have spaces in your alias names.
* **ADAnnounce[x]=channel**
  * Channel to announce in, or leave blank for no announce. See ACAnnounce description in the AdvMelee section for

    further explanation.
* **ADSpellMinMana[x]=\#**
  * Minimum mana percentage to have in order to attempt this spell (e.g. 05 \(for 5%\), 25 \(for 25%)
* **ADSpellRecast[x]=\#**
  * Number of times to recast this spell for fizzles, interrupts, etc.
* **ADSpellCastonResist[x]=spell alias**
  * Should this spell be resisted, is there another alias to cast before another attempt of this spell.
  * Please note that if ADSpellCastonResist is defined, ADSpellRecast must be at least 1.
* **ADSpellDelay[x]=\#**
  * Number of seconds to wait between casts of this spell.
* **ADTarCnt[x]=\#**
  * Number of targets required to be present to cast this spell. If set to 0, this spell will not be auto-casted\)
* **ADTarType[x]=\#**
  * Designate one target type to cast this debuff on.
  * Valid target types:
    * 0 = All mobs
    * 1 = MA Target only
    * 2 = All except MA Target
    * 10 = All mobs before next spell
    * 11 = MA target only before next spell
    * 12 = All but MA target before next spell
  * Priority Debuffs (10, 11, 12\) should be placed first most \(prior to non-priorities). Meaning - settings of 10,

    11, and 12 need to be in top spells slots (ADGem1, ADGem2, etc)
* **ADTarBegHP[x]=\#**
  * The target must be equal or below this HP%.
* **ADTarEndHP[x]=\#**
  * The target must be equal or above this HP%
* **ADIfSpellImmune[x]=script name**
  * This is meant to be a pointer to a quick, one line script that is executed when a mob is immune to the spell you

    have cast. If you need to do something complicated, other scripts can be called from it. 'Param1' is now passed

    as the immune target's ID. An example where this would be useful is for chanter mez:

    * _/bc {TankName} //multiline ; /varset ACMATarget {Param1};/target id {Param1}_ will make your

      toon target the immune mob even if he was on another mob at the time.
* **ADUseHoTT[x]=\#**
  * This will cause the macro to /target the mob and check TargetOfTarget before casting and delay \# seconds before

    checking again if mob is skipped. If not a raid or group member, the macro will move on and recheck that mob for

    that debuff after the time has expired. Note that this will default to casting the debuff anyways if HoTT isn't

    available.
* **ADPreCondition[x]=one line script**
  * Whatever statement you add to this line needs to /return TRUE. i.e. - ADPreCondition1=/if ({This} && {That})

    /return TRUE. Only a TRUE return will allow the spell to cast, so script carefully, or leave the lines default.

Code:

`ADGem1=2`
`ADSpell1=Turgur's Insects`
`ADSpellFoci1=`
`ADDurMod1=0`
`ADSpellAlias1=slow`
`ADAnnounce1=/bc Slowed <<[+y+] %t [+x+]>> with[+g+] %s [+x+]`
`ADSpellMinMana1=10`
`ADSpellRecast1=2`
`ADSpellCastonResist1=malos`
`ADSpellDelay1=0`
`ADTarCnt1=1`
`ADTarType1=11`
`ADTarBegHP1=200`
`ADTarEndHP1=15`
`ADIfSpellImmune1=`
`ADUseHoTT1=0`
`ADPreCondition1=TRUE`

"Notice the ADTarBegHP1 setting. I have the same spell set with ADTarType2=12 directly after this one to make sure he slows adds. (sometimes he pulls em too..\) Everything else - mainly ACAssistPct is set to a lower value. Most around 95 or so. Buffs are a pita because if the debuff sub is called \(it is called first\) it won't cast the debuffs if there's any reason not to, then the macro runs through the whole buff loop before getting back to debuffs again.. Setting the ADTarBegHP at least over the level of all other functions at least attempts to keep the slow first. Also.. I find the macro works best if you always set your ACManaPct very low. Usually keep mine around 5 or so for every toon. I should change the default on that, but clearing targets and such is something your toon will do quite often if his mana is under that value." - Ptarp on the forums on Wed Mar 09, 2011 7:54 pm. \(edited into Wiki by Arblis)

### AdvBuff Section [AdvBuff]

If you want to cast single target buffs after group buffs, place all of your group buffs first.

* **ABCount=\#**
  * Number of buffs you plan to have.
* **ABMobMax=\#**
  * Max number of targets to track for buffs (do not include pets)
* **ABCheckTime=\#**
  * How often to check for buffs in seconds
* **ABGem[x]=source**
  * Designate what the source of the spell is.
  * Valid entries: gem number, alt, ability, item, script, potionbelt
  * Note that 'potionbelt' does not require a slot number.
  * Examples:
    * _ABGem1=3_ Cast this spell from gem 3
    * _ABGem1=alt_ This spell is an alternative advancement ability
* **ABSpell[x]=source name**
  * Valid entries: spell name, item name, alternate ability name, ability name, script name
  * Examples:
    * _ABSpell1=Minor Shielding_ This would be generally be paired with an ABGem1 entry indicating which spell gem

      to cast Minor Shielding from.

    * _ABSpell1=Uber Wand Thingy of Uberness_ This would be generally be paired with an ABGem1 entry indicating

      that the source of this spell is an item.
* **ABSpellFoci[x]=setname**
  * Bandolier set name to swap in before casting this spell.
  * Please see MQ2Bandolier and MQ2Cast to understand how to use swap sets.
* **ABDurMod[x]=\#\#**
  * Any spell extension percentage, e.g. 05 (for 5%\), 25 \(for 25%).
  * Due to how spell durations / extensions are calculated, you may need to enter extensions in excessive of 100%

    (e.g. a 25% extension would be entered here as 125). Check your results in game to make sure you have set the

    correct extension.
* **ABSpellAlias[x]=spell alias**
  * Enter an "alias" for the spell. This is often a short, easier to use name \(e.g. the alias for Spirit of the Wolf

    might be SoW\).

  * Please note that you can NOT have spaces in your alias names.
* **ABAnnounce[x]=channel**
  * Channel to announce in, or leave blank for no announce. See ACAnnounce description in the AdvMelee section for

    further explanation.

  * Annoucements also support formatting (makes it a bit easier to see in the MQ window). For example:
    * _ABAnnounce1=/bc [+r+\]Buffed\[+x+\] \&lt;\&lt;\[+y+\] %t \[+x+\]&gt;&gt; with\[+g+\] %s \[+x+]_
* **ABSpellMinMana[x]=\#**
  * Minimum mana percentage to have in order to attempt this spell (e.g. 05 \(for 5%\), 25 \(for 25%)
* **ABTarCnt[x]=\#**
  * Designate how many targets are required to cast this spell.
    * If set to 0, this spell will not be auto-casted. This is useful for spells that you want to call via alias

      to be cast manually.

    * For single cast spells (e.g. Spirit of Eagle), ABTarCnt will most often be set to 1.
    * For group spells (e.g. Flight of Eagles), you might set your ABTarCnt higher so that it only gets cast when

      there are more than 2 or 3 people in your group.
* **ABTarType[x]=target type**
  * Valid target types are as follows (please note which entries can be used with others and which are exclusive):
    * _ShortClassName_ Used for class specific buffs (ie. haste on "war"). Valid entries are: war shd pal rng mnk

      rog brd bst ber shm clr dru wiz mag enc nec. Note that any or all of these entries can be used at the same

      time.

    * _self_ Used for self only spells.
    * _grp_ for Group spells \(example needed, according to author self is mutually exclusive, so self grp won't

      work. grp can also not be the only target, so its safer to just list classes here!\)

    * _pet_ used to cast buffs on all pets in the group.
    * _mypet_ used to cast on only your pet. Please note that _pet_ and _mypet_ are mutually exclusive.
    * _cbt_ for spells to be casted during combat (e.g. an entry for Yaulp would be ABTarType1=self cbt). Please

      note that any NPC within radius that is not on your exclude list will cause 'cbt' buffs to fire. If you want

      to buff next to NPCs (and don't plan to kill them), use the _exclude_ command. If you later decide to kill

      whatever mob you've excluded, use the _include_ command to remove it from list. The macro does not check

      combat state of the tank for buffs.

    * _idle_ used with cbt for spells to be casted when in or out of combat \(e.g. if you wanted to keep Yaulp on

      at all times (in AND out of combat\), your entry would be ABTarType1=self cbt idle). Please note that _idle_

      is only used in ABTarType when _cbt_ is also used.

    * _aura_ used to cast an aura - must be used with _self_ (e.g. ABTarType1=self aura)
      * Note that Bard auras \*REQUIRE\* ABSpellAlias to be set up to cast, and modbuff will use CastCall to

        actually cast the aura.
    * _tank_ used to cast only on the designated group tank. Tank designation is keyed from either the TankName

      variable in the setting section (see above\) or by setting a toon to Main Tank \(Group.Maintank) using the

      Roles function.

    * _petspell_ used to set up an entry to create/cast a pet. Example:

''ABGem3=7

ABSpell3=Shambling Minion

ABSpellFoci3=

ABDurMod3=0

ABSpellAlias3=pet

ABAnnounce3=/bc Cooking up a pet

ABSpellMinMana3=10

ABTarCnt3=1

ABTarType3=**petspell**

ABRecast3=FALSE

ABSpellIcon3=

ABPreCondition3=TRUE''

* * Default entry: \*ABTarTypeX=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp

    pet cbt idle\*

    * Please note that the default entry includes settings that do not work together. Specifically, _tank_, _self_

      and _mypet_ are meant to be used by themselves. If you want to cast the same buff on yourself, your pet and

      the tank, create them as seperate buff entries.
* **ABRecast[x]=TRUE\|FALSE**
  * True is only really needed for single targets that are NOT in the group and/or on NetBots. Set ABRecast TRUE

    when you want the macro to use the spell worn off messages from EQ for the macro to know who to cast the buff

    on. This allows you to rebuff toons that are lower level for your normal buff set, or not in EQBC and not in

    group.

  * For the most part this shouldn't be needed for rebuffing if all of your toons are NetBots members. The macro

    actually checks the other toons in netbots and knows what their buffs are, whether the one they're trying to

    cast will stack, and the duration of the buff if the toon still has it on.
* **ABSpellIcon[x]=icon name**
  * Use when the spell icon has a different name than the actual spell \(e.g. the spell _Unity of Spirits_ has a

    spell icon of _Transcendent Foresight_. In fact, you could use any one of the four spell icons/names that Unity

    creates\).

    * Please note that if the name you have in ABSpellIcon doesn't evaluate to a spell name, the buff will be

      skipped. In other words, leave it blank if your spell doesn't need it.

### AdvEvent Section [AdvEvent]

* **AECount=\#**
  * Number of events you plan to have.
* **AECheckTime=\#**
  * How often to check for events in seconds
* **AECustomX=watch text**
  * Custom emote-triggered events driven by scripts.
  * Default is three blank entries (AECustom1=, AECustom2=, AECustom3=)
  * Please note that an earlier version of this variable populated AECustom1, AECustom2 and AECustom3 with random

    numbers in the ini file. The newwer version of AECustom now adds the three AECustomX entries but sets them as

    blank.\)

  * Each AECustomX entry, if defined, must have a corresponding script entry. For example, by defining

    _AECustom1=greater bloodmoon healing_ in the AdvEvent section, you would need a corresponding script defined

    that might read something like:

_[Script-AECustomEvent1]_

_Commands=1_

_C1=/bc cast stun_

* **AEGem[x]=source**
  * Designate what the source of the spell is.
  * Valid entries: gem number, alt, ability, item, script, potionbelt
  * Note that 'potionbelt' does not require a slot number.
  * Examples:
    * _AEGem1=3_ Cast this spell from gem 3
    * _AEGem1=alt_ This spell is an alternative advancement ability
* **AESpell[x]=source name**
  * Valid entries: spell name, item name, alternate ability name, ability name, script name
  * Examples:
    * _AESpell1=Minor Shielding_ This would be generally be paired with an ABGem1 entry indicating which spell gem

      to cast Minor Shielding from.

    * _AESpell1=Uber Wand Thingy of Uberness_ This would be generally be paired with an AEGem1 entry indicating

      that the source of this spell is an item.
* **AESpellFoci[x]=setname**
  * Bandolier set name to swap in before casting this spell.
  * Please see MQ2Bandolier and MQ2Cast to understand how to use swap sets.
* **AEDurMod[x]=\#\#**
  * Any spell extension percentage, e.g. 05 (for 5%\), 25 \(for 25%).
  * Due to how spell durations / extensions are calculated, you may need to enter extensions in excessive of 100%

    (e.g. a 25% extension would be entered here as 125). Check your results in game to make sure you have set the

    correct extension.
* **AEDelay[x]=\#**
  * How many seconds do I wait between casts of this spell.
* **AEEventMinMana[x]=\#**
  * My mana percentage must be at least this to complete this event.
* **AEEventMinHP[x]=\#**
  * My HP percentage must be at least this to complete this event.
* **AEMinMana[x]=\#**
  * The event target's mana percentage must be above this to complete this event.
* **AEMaxMana[x]=\#**
  * The event target's mana percentage must be below this to complete this event.
* **AEMinHP[x]=\#**
  * The event target's HP percentage must be above this to complete this event.
* **AEMaxHP[x]=\#**
  * The event target's HP percentage must be below this to complete this event.
* **AETarType[x]=target type**
  * Valid entries: war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self tnt (Less is better!)
* **AESpellAlias[x]=event alias**
  * Enter an "alias" for the event. This is often a short, easier to use name \(e.g. the alias for Spirit of the Wolf

    might be SoW\).

  * Please note that you can NOT have spaces in your alias names.
* **AEAnnounce[x]=channel**
  * Channel to announce in, or leave blank for no announce. See ACAnnounce description in the AdvMelee section for

    further explanation.

  * Annoucements also support formatting (makes it a bit easier to see in the MQ window). For example:
    * _ABAnnounce1=/bc [+r+\]Buffed\[+x+\] \&lt;\&lt;\[+y+\] %t \[+x+\]&gt;&gt; with\[+g+\] %s \[+x+]_
* **AETarCnt[x]=1\|0**
  * Settings are \*only\* either 1 (on\) or 0 \(off).

#### Examples

Shaman cannibalization example. In this case, settings like AEEventMinMana and AEMinMana both refer to the shaman as he is both the event triggerer as well as the target of the event:

`AEGem1=5`
`AESpell1=Cannibalize III`
`AESpellFoci1=`
`AEDurMod1=0`
`AEDelay1=0`
`AEEventMinMana1=0`
`AEEventMinHP1=30`
`AEMinMana1=0`
`AEMaxMana1=90`
`AEMinHP1=50`
`AEMaxHP1=100`
`AETarType1=self`
`AESpellAlias1=canni`
`AEAnnounce1=`

Necromancer mana feed example (where the necro is feeding mana to another character\). In this case, AEEventMinMana refers to the necro's mana and AEMinMana refer to the mana of the target \(as defined by AETarType):

`AEGem2=4`
`AESpell2=Rapacious Subvention`
`AESpellFoci2=`
`AEDurMod2=0`
`AEDelay2=0`
`AEEventMinMana2=50`
`AEEventMinHP2=50`
`AEMinMana2=20`
`AEMaxMana2=45`
`AEMinHP2=0`
`AEMaxHP2=100`
`AETarType2=clr enc`
`AESpellAlias2=manafeed`
`AEAnnounce2=/bc`

### AdvCure Section [AdvCure]

* **AQCount=\#**
  * Number of cures you plan to have.
* **AQCheckTime=\#**
  * How often to check for cures in seconds
* **AQGem[x]=source**
  * Designate what the source of the spell is.
  * Valid entries: gem number, alt, ability, item, script, potionbelt
  * Note that 'potionbelt' does not require a slot number.
  * Examples:
    * _AQGem1=3_ Cast this spell from gem 3
    * _AQGem1=alt_ This spell is an alternative advancement ability
* **AQSpell[x]=source name**
  * Valid entries: spell name, item name, alternate ability name, ability name, script name
  * Examples:
    * _AQSpell1=Minor Shielding_ This would be generally be paired with an ABGem1 entry indicating which spell gem

      to cast Minor Shielding from.

    * _AQSpell1=Uber Wand Thingy of Uberness_ This would be generally be paired with an AQGem1 entry indicating

      that the source of this spell is an item.
* **AQSpellFoci[x]=setname**
  * Bandolier set name to swap in before casting this spell.
  * Please see MQ2Bandolier and MQ2Cast to understand how to use swap sets (e.g. -bandolier\|)
* **AQSpellCureType[x]=cure type**
  * Valid entries (type of cure needed): Cursed, Diseased, Poisoned, EnduDrain, LifeDrain, ManaDrain, Blinded,

    CastingLevel, Charmed, Feared, Healing, Mesmerized, Resistance, Rooted, Silenced, Slowed, Snared, SpellCost,

    SpellSlowed, SpellDamage, Trigger, All

  * Set the cure type to the best match for the spell, but keep them in order of best cure first.
  * The first cure in your .ini matching the cure type needed (or if you set to "All") will be the first attempted

    spell.

  * Cures \*can\* always be interrupted by any heal spell, unless you're using a cure spell that's already listed in

    your heal section \(e.g. Cleric's "Word of XXX" line of spells may or may not interrupt for heals depending on

    where they are in your heal section\).

  * Modcure.inc will cast once per loop and then return to the main loop, so setting group cures (like Radiant Cure)

    toward the top would be best

  * Be specific on cure types to avoid recasting the same cure over and over if it won't cure you.
* **AQSpellMinMana[x]=\#**
  * Minimum mana to have in order to attempt this cure.
* **AQSpellRecast[x]=\#**
  * Number of times to recast this spell for fizzles, interrupts, etc.
* **AQTarCnt[x]=\#**
  * How many targets should be present to cast this spell, if set to 0, this spell will not be auto-casted.
* **AQTarType[x]=target type**
  * Valid target types are as follows (please note which entries can be used with others and which are exclusive):
    * _ShortClassName_ Used for class specific buffs (ie. haste on "war"). Valid entries are: war shd pal rng mnk

      rog brd bst ber shm clr dru wiz mag enc nec. Note that any or all of these entries can be used at the same

      time.

    * _self_ Used for self only spells.
    * _grp_ for Group spells (e.g. ABTarType1=self grp)
    * _pet_ used to cast buffs on all pets in the group.
    * _mypet_ used to cast on only your pet. Please note that _pet_ and _mypet_ are mutually exclusive.
    * _cbt_ for spells to be casted during combat (e.g. an entry for Yaulp would be ABTarType1=self cbt). Please

      note that any NPC within radius that is not on your exclude list will cause 'cbt' buffs to fire. If you want

      to buff next to NPCs (and don't plan to kill them), use the _exclude_ command. If you later decide to kill

      whatever mob you've excluded, use the _include_ command to remove it from list. The macro does not check

      combat state of the tank for buffs.

    * _idle_ used with cbt for spells to be casted when in or out of combat \(e.g. if you wanted to keep Yaulp on

      at all times (in AND out of combat\), your entry would be ABTarType1=self cbt idle). Please note that _idle_

      is only used in ABTarType when _cbt_ is also used.

    * _aura_ used to cast an aura - must be used with _self_ (e.g. ABTarType1=self aura)
      * Note that Bard auras \*REQUIRE\* ABSpellAlias to be set up to cast, and modbuff will use CastCall to

        actually cast the aura.
    * _tank_ used to cast only on the designated group tank. Tank designation is keyed from either the TankName

      variable in the setting section (see above\) or by setting a toon to Main Tank \(Group.Maintank) using the

      Roles function.
  * Default entry: \*ABTarTypeX=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp

    pet cbt idle\*

    * Please note that the default entry includes settings that do not work together. Specifically, _tank_, _self_

      and _mypet_ are meant to be used by themselves. If you want to cast the same buff on yourself, your pet and

      the tank, create them as seperate buff entries.
* **AQSpellAlias[x]=spell alias**
  * Enter an "alias" for the spell. This is often a short, easier to use name \(e.g. the alias for Radiant Cure might

    be RC\).

  * Please note that you can NOT have spaces in your alias names.
* **AQAnnounce[x]=channel**
  * Channel to announce in, or leave blank for no announce. See ACAnnounce description in the AdvMelee section for

    further explanation.

  * Annoucements also support formatting (makes it a bit easier to see in the MQ window). For example:
    * _ABAnnounce1=/bc [+r+\]Cured\[+x+\] \&lt;\&lt;\[+y+\] %t \[+x+\]&gt;&gt; with\[+g+\] %s \[+x+]_
* '''AQSpellCntr[x]=
  * Currently not used for anything, so don't worry about it :\)

### AdvPull Section [AdvPull]

This section is under development.

* **APCheckTime=\#**
  * Time (in seconds) to wait in between AdvPull executions. Default is 0.
* **APRadius=\#**
  * The distance around your target to check for more mobs as defined by APMobMax (basically, a check for adds).

    Default is 40.
* **APMobMax=\#**
  * The max amount of mobs (target + adds) you will allow before pulling. Default is 1. If there are less than

    APMobMax mobs within APRadius of your target, it will pull the mob.
* **APScript=**_**Scriptname**_
  * Name of script to define how you want to tag the mob (throw stone, ranged, item clicky, spell, etc) and executes

    when you have a mob targeted to pull. The script name must have at least 3 characters. Default is empty. \*\*YOU

    MUST CREATE A SCRIPT TO TAG THE MOB!\*\*

  * [Modbot Scripts](https://macroquest.org/wiki/index.php/ModBot#Scripts_and_ModBot_Variable_Usage)
* **APPath=**_**Pathname**_
  * The name of the path to run for pulling/movement, as defined in your MBWayPnt.ini \(See

    [ModMove](https://macroquest.org/wiki/index.php/Related_Include_Files#ModMove) for more details on creating

    a path\). The path name must be at least 3 characters. Default is empty.
* **APRetPath=**_**ReturnPathname**_
  * The name of the path to use to move back to camp. The path must be defined in your MBWayPnt.ini file. The path

    name must be at least 3 characters. Default is empty.

  * Mostly used for when the path back to camp is a different one than used to pull mobs \(ie, you go through a

    one-way wall to pull or intentionally fall off a ledge and have to run the long way back\). If you want to return

    the same way you came, you can just use WPLoop=TRUE in MBWayPnt.ini instead of having to set up a second path.
* **APBefore=**
  * Command or series of commands (with multiline) to execute before the rest of AdvPull section. Must be at least 3

    characters. Default is empty.
* **APAfter=**
  * Command or series of commands (with multiline) to execute after AdvPull has finished. Default is empty.
* **APAnnounce=**
  * A way to announce what you have pulled. Default is empty.
  * Note: This is not just a chat channel, but a place to put a full incoming message, ie:
    * _APAnnounce=/gsay Incoming -[ %t ]-_
* **APRetries=1**
  * Number of times to attempt to pull a mob in case it fails the first try (line of site, etc). This will strafe

    left and right on subsequent attempts. Default is 1.

## MBCommon.inc Settings

The location and name of MBCommon.inc can now be set by changing line 38 in Modbot.mac.

`/declare MBCommon string outer MBCommon.ini`

It defaults to the ./macros folder, but the line can be changed to any path.

### Settings Section

* **LoadAlias** [1,0] This is an on / off setting to load the "/alias /mb /echo MB-" alias for commands. It is set

  to 0 after first run when alias should be loaded, but you can set to 1 to add it back to your Macroquest.ini file if

  it gets deleted.

* **IniLocation** Path to your MB\_.ini files. Must end in / or  if changed from default.
* **LootIni** [Loot.ini] This setting can be used to change the location of your Loot.ini file as well as the name.
* **MBWayPntLocation** [MBWayPnt.ini] This setting can be used to change the location of your MBWayPnt.ini file as

  well as the name of the file.

* **CheckTargetDebuffs** [TRUE\|FALSE] This setting toggles on/off the ${Target.Buff} checking for debuffs

  (essentially this checks if the spell "Stacks" before casting.)

  * Each debuff listed in MBCommon.ini now has an 'OverwritesID=' entry. This entry is meant for a list of debuffs

    that the spell doesn't 'Stack' with, but you want the debuff to overwrite.

### Spell Section

* **Zone.ShortName** - List of mobs excluded for that zone in a pipe -"\|" delimited string. This setting is not

  present for any zones which you have nothing excluded.

  * Immune lists for each spell are saved in their own section along with a MaxLevel=[100] setting. Change to the

    max level of the spell.

  * As the macro finds mobs that are immune to the spell, the zone shortname is added to the entry as a variable

    along with the mob names in pipe delimited format.

  * Mobs that are marked immune to debuffs can be marked in MBCommon.ini with an asterisk to allow for some names

    that have only some immune, and some not. For example, Dreadspire has some body types with same names where some

    are immune to mez, and some not \(e.g. _an aid to the Seneschal_ - some body types with that mob name are immune

    to befuddle, and others aren't\). By adding an asterisk to the end of the name in the exclude section, the macro

    will repeat attempts to mez, etc. that mob type (rather than just marking them immune and not casting at all):

    _DreadspireImmune=\|an aid to the Seneschal\_\|\*

  * The ADIfSpellImmune script, if defined, will only run if the mob is found to be immune after cast, but the

    astrik will not be replaced, and the spell will only cast once allowing the spell to still attempt on the next

    mob it hasn't been cast on.

  * _Overwrites=_ list of debuffs that the spell doesn't 'Stack' with, but you want the debuff to overwrite. This

    does require user intervention, and there's no way to set it auto-set them.

  * _MaxLevel=_ maximum level of mob that can be affected by debuff

An entry in the spell section might look something like this:

`[Mystify]`
`MaxLevel=83`
`thalassius_bImmune=|a sea mephit defender||a sea mephit evoker|`
`OverwritesID=|14569|14570|14530|`

## ModBot Class INI Examples

[```ModBot`` ``Class`` ``INI`` ``Examples`` ``linked`` ``to`` ``another`` ``page```](https://macroquest.org/wiki/index.php/Modbot_Class_INI_Examples)

[```ModBot`` ``v4`` ``Class`` ``INI`` ``Examples`` ``linked`` ``to`` ``another`` ``page```](https://macroquest.org/wiki/index.php/Modbot_v4_Class_INI_Examples)

## Scripts and ModBot Variable Usage

ModBot allows VERY customizable sripts to such an extent you can actually program your own sub-procedures within your INI file. You can harness ANY global variable within ModBot to use with the scripts.
Scripts match MQ2 code to every extent, below are several examples of scripts and common variables one would use to create complex scripts

### Understanding scripts, syntax, example, how to

* Scripts General Info
  * Scripts can be difficult and there are some MQ2 commands that give scripts trouble. Keep this in mind and

    prepare to post you script code should you have problems.

  * No script can take more then 15 seconds to complete, however this can be modified in the code directly in the

    Sub MBScript or even changed in the script you create ({Timer} is the var)

  * Scripts are executed from top to bottom and you are allowed to use a label :Top (e.g. /goto :Top), in your

    script. The /goto :Top option allows for complex loops to take place directly from code in the INI file

  * If you use ANY INI generated ModBot global string variables that have spaces in your custom scripts they MUST be

    encapsulated by 2 apostrophies when used in the script, see PetCast example below.
* Reserved Characters

:\*These characters can not be used in scripts

::\*$ "

:\*'' Two apostrophies are for passing variables with spaces in script code. Use them to replace quotes.

* Syntax

`[Script-]`
`Commands=`
`C1=`
`.`
`Cn=`

What does a script look like in your INI file:

`[Script-HelloWorld]`
`Commands=2`
`C1=/echo Hello World`
`C2=/if ({Timer}>50) /varset Timer 5s`
`C3=/goto :Top`

In the example above it will echo to the MQ2ChatWindow "Hello World" for 5s. Notice how I do NOT use a $ to reference the "Timer" variable.

* How To use or launch a script

:\*/bc bob script HelloWorld

:\*You can set XXGem1=script and XXSpell=HelloWorld as a spell name for any of the spells you've configured in ModBot, and it will be triggered when that event, heal, etc would take place.

Please see the below examples for complex script code.

**Common Variables** (You can use ANY mq2 variable without the $, you can even CREATE new global vars and use them, all from the INI file via Scripts)

`{ACState} = If greater than 0, ModBot thinks you are in combat`
`{ACMATarget} = The target of the main assist`
`{CampStatus} = If greater than 0, means I've been given a /bc makecamp command`
`{FollowFlag} = If greater than 0, means I should be following something`
`{TankName} = The acting main assist`
`{Me}, {Spawn}, etc = See MQ2 Manual`

**Examples**
This example is triggered from an event OR a heal and it will remove the necro "Lich" spell:

`[AdvHeal]`
`AHGem3=Script`
`AHSpell3=DropLich`
`AHSpellFoci3=`
`AHDurMod3=0`
`AHSpellAlias3=droplich`
`AHSpellMinMana3=0`
`AHAnnounce3=/bc`
`AHTarCnt3=1`
`AHClass3=pc hp40 nec`

`[AdvEvent]`
`AEGem3=Script`
`AESpell3=DropLich`
`AESpellFoci3=`
`AEDurMod3=0`
`AEDelay3=0`
`AEEventMinMana3=100`
`AEEventMinHP3=40`
`AEMinMana3=20`
`AEMaxMana3=100`
`AEMinHP3=0`
`AEMaxHP3=90`
`AETarType3=tnt`
`AESpellAlias3=`
`AEAnnounce3=/bc`

`[Script-DropLich]`
`Commands=1`
`C1=/if ({Me.Buff[Lich].ID}) /notify BuffWindow Buff{Math.Calc[{Me.Buff[Lich].ID}-1].Int} leftmouseup`

This example is launched via the ACBefore command from the [Melee] section, I've got Sneak Attack bound to hotkey 6. What the bot will do is to trigger Sneak Attack, attempt proper position, backstab the mob, then revert to "normal"

`[Script-SneakAttack]`
`Commands=10`
`C1=/if ({Melee.Enable}) /melee plugin=0`
`C2=/if ({Me.CombatAbilityReady[Sneak Attack]}) /keypress 6`
`C3=/if (!{Me.Moving} && !{Stick.MoveBehind} && {Stick.Distance}!={Math.Calc[{Spawn[{ACMATarget}].MaxRangeTo}+5]}) /stick {Math.Calc[{Spawn[{ACMATarget}].MaxRangeTo}+5]} behind id {ACMATarget}`
`C4=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5`
`C5=/if ({Melee.BackAngle}>60 || {Melee.BackAngle}<-60) /goto :Top`
`C6=/if ({Target.Distance3D}>={Spawn[{ACMATarget}].MaxRangeTo}) /stick {Math.Calc[{Spawn[{ACMATarget}].MaxRangeTo}-5]} hold behind id {ACMATarget}`
`C7=/if ({Target.Distance3D}>={Spawn[{ACMATarget}].MaxRangeTo}-3) /goto :Top`
`C8=/delay 5`
`C9=/if ({Me.AbilityReady[Backstab]}) /doability backstab`
`C10=/melee plugin=1`

This example will confirm you are hidden and sneaking when I'm at "camp" and not sneaking when I'm in follow mode. It will also re-engage if MQ2Melee lost "stick" because of too much mob movement

`[Script-HideSneak]`
`Commands=4`
`C1=/if ({FollowFlag} && {Me.Sneaking}) /multiline ; /doability sneak;/return`
`C2=/if (!{FollowFlag} && !{ACState} && {Select[{MakeCamp},on]} && {Me.AbilityReady[Hide]} && !{Me.Moving} && !{Melee.Combat}) /multiline ; /doability Hide;/delay 5`
`C3=/if (!{FollowFlag} && !{ACState} && {Select[{MakeCamp},on]} && {Me.AbilityReady[Sneak]} && !{Me.AbilityReady[Hide]} && !{Me.Moving} && !{Melee.Combat}) /multiline ; /doability Sneak;/delay 5`
`C4=/if ({ACState} && {ACMATarget} && {Target.ID} && {Me.AbilityReady[Backstab]}) /keypress q`

Example of createing a new global var and an example of using it

`[Script-EventsOff]`
`Commands=2`
`C1=/if (!{Defined[CheckSlow]}) /declare CheckSlow int outer 1`
`C2=/if ({DoEvents}) /multiline ; /varset DoEvents FALSE;/varset CheckSlow 1`

`[Script-EventsOn]`
`Commands=2`
`C1=/if (!{Defined[CheckSlow]}) /declare CheckSlow int outer 3`
`C1=/if (!{DoEvents}) /multiline ; /varset DoEvents TRUE;/varcalc CheckSlow {CheckSlow}+1`

`[Script-IsSlowed]`
`Commands=3`
`C1=/if (!{Defined[CheckSlow]}) /multiline ; /varset DoEvents FALSE;/return`
`C2=/if ({CheckSlow}<=4) /varset DoEvents FALSE`
`C3=/if ({CheckSlow}>4) /varset DoEvents TRUE;/varset CheckSlow 1`

Example of using a ModBot global string. This will create a new pet, say when your existing pet is about to die

:\*Please note in the INI snippets below that the INI generated global string PetCast has a space so to pass this properly in the script,

you must encapsulated in quotes, script code uses apostrophies in place of quotes.

`[Settings]`
`PetCast=Invoke Death|gem1`

`[Script-NewPet]`
`Commands=4`
`C1=/multiline ; /casting ''{PetCast}'' -maxtries|5;/delay 2s`
`C2=/if ({Cast.Timing}>600) /goto :Top`
`C3=/multiline ; /if ({Me.Pet.ID}) /pet go away;/delay 2s !{Me.Casting.ID}`
`C4=/if (!{Me.Pet.ID}) /goto :Top`

Example of using PetCast for a cleric hammer, to be called from a ACBefore command

`[Settings]`
`DoPet=FALSE`
`PetCast=Unswerving hammer of awesomeness|gem1`
`[Melee]`
`ACBefore=/if (!{Me.Pet.ID} && {ACMATarget} && {Spawn[{ACMATarget}].Type.Equal[NPC]} && {Spawn[{ACMATarget}].Distance3D}<={ACLeash}) /call MBScript SumHam`
`[Script-SumHam]`
`Commands=2`
`C1=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5`
`C2=/if (!{Me.Pet.ID}) /multiline ; /casting ''{PetCast}'' -maxtries|2;/delay 3s`

Example of a CH script to be run from a non cleric .ini (warrior)

`I figure I might as well be posting some of the script versions of other macros that I've been seeing around, but written my own thing so I could just keep modbot running.`
````` Modbot script version of CH chain that seems to work, though might have problems I haven't noticed.... I use this with a hotkey from my tank -```"/mb script chain 50" (yes it's in MB\_tank.ini - NOT the cleric.ini.. ) It finds all clerics in netbots, then runs through the list telling each````` to cast CH after the delay you specify. This script does require the clerics to all be running modbot with an alias of CH for complete heal spell,```and connection to the same EQBCS server.``

```text
`Commands=13`
`C1=/multiline ; /declare clrlist string local;/declare x int local 1;/declare StopLoop bool local FALSE`
`C2=/if ({Spawn[{NetBots.Client.Arg[{x}]}].Class.ShortName.Equal[clr]}) /varset clrlist {clrlist} {NetBots.Client.Arg[{x}]}`
`C3=/if ({x} < {NetBots.Counts}) /multiline ; /varset a 1;/varcalc x {x}+1`
`C4=/echo Clerics: {clrlist} casting {Math.Calc[{Param1}/10]}s apart`
`C5=/varset x 0`
`C6=/varset Timer 100`
`C7=/varcalc x {x}+1`
`C8=/if ((!{Spawn[{clrlist.Arg[{x}]}].ID} || {NetBots[{clrlist.Arg[{x}]}].PctMana} < 3) && {x} <= {clrlist.Count[ ]}) /varset a 5`
`C9=/if ((!{Spawn[{clrlist.Arg[{x}]}].ID} || {NetBots[{clrlist.Arg[{x}]}].PctMana} < 3) && {x} > {clrlist.Count[ ]}) /varset a 4`
`C10=/bc {clrlist.Arg[{x}]} cast ch`
`C11=/delay {Param1}`
`C12=/if ({x}>{clrlist.Count[ ]}) /varset a 4`
`C13=/if (!{StopLoop}) /varset a 5`
`````  Posted By Ptarp Tue Apr 12, 2011 1:01 am. Moved to Wiki by Arblis\`

## Script Examples

[```Script`` ``examples`` ``linked`` ``to`` ``another`` ``page```](https://macroquest.org/wiki/index.php/Script_Examples)

## Related Include Files Information and Examples

[```Related`` ``Include`` ``files`` ``(modloot,`` ``AAPurchase,`` ``modmove,`` ``etc.)`` ``information`` ``and`` ``INI`` ``examples`` ``linked`` ``to`` ``another`` ``page```](https://macroquest.org/wiki/index.php/Related_Include_Files)

## Tips, Tricks and Troubleshooting

Here you will find a collection of little gems pulled from the ModBot thread. At some point, this may morph in to a handy little troubleshooting flowchart, but for now it will serve as kind of a tidbit catchall for things that would otherwise get lost in the hundreds of thread pages...

Please note- when you are posting on the forum for help (after reading this wiki of course!\) include the MQ2 version, winEQ version and the EQ install type \(Titanium / sod / UF)

`Although covered previously on the Wiki quite a few times - If you are having trouble with mobs keeping you from doing non combat things (buff, loot etc) try using the following:`
`exclude <mob name,save>`
````` "What I do.. (while targeted on the mob you want to ignore)```On my tank I have a hotkey. I target the mob to exclude and press it.``
`First line is /bcaa //mb exclude ${Target.CleanName}`
`second line - /bcaa //mb exclude save`
````` /echo ${ADMobCount} (use this after your exclude to see if the char in question has any mobs on the exclude list. Can be used with /bcaa to see all of your toons mobcounts)```If you fight near non-combatant mobs, always use the exclude command so the macro doesn't "see" them, and set your Radius= in your toon's .ini file to a minimum.``
`I normally keep mine at around 60 to 80 depending on what I'm doing. Remember you can "/varset Radius 50" or something in game with the mac running to find a happy medium." -Ptap Mon Sep 20, 2010 1:18 pm`

`It also sounds like an exclude hotkey, and pause hotkey would be your best friends.. Here's a few of the hotkeys I use.`

`_EQTitan.ini in your everquest folder.`
````` Code:```[Socials]``
`Page10Button1Name=TankName`
`Page10Button1Color=0`
`Page10Button1Line1=/bcaa //varset TankName ${Me.Name}`
`Page10Button7Name=Masters`
`Page10Button7Color=0`
`Page10Button7Line1=/bcaa //varset MasterList ${NetBots.Client}`
`Page10Button5Name=pause`
`Page10Button5Color=0`
`Page10Button5Line1=/bcaa //mb mbpause on`
`Page10Button11Name=unpause`
`Page10Button11Color=0`
`Page10Button11Line1=/bcaa //mb mbpause off`
`Page10Button6Name=follow`
`Page10Button6Color=0`
`Page10Button6Line1=/bca follow`
`Page10Button12Name=stop`
`Page10Button12Color=0`
`Page10Button12Line1=/bcaa //mb stop`
`Page10Button10Name=letsroll`
`Page10Button10Color=0`
`Page10Button10Line1=/bcaa //mb letsroll`
`Page2Button1Name=corpse`
`Page2Button1Color=0`
`Page2Button1Line1=/corpse`
`Page2Button6Name=sellitem`
`Page2Button6Color=0`
`Page2Button6Line1=/ini loot.ini ${Cursor.Name.Left[1]} "${Cursor.Name}" Sell`
`Page8Button1Name=include`
`Page8Button1Color=0`
`Page8Button1Line1=/bcaa //mb include ${Target.CleanName}`
`Page8Button1Line2=/pause 5`
`Page8Button1Line3=/bcaa //mb exclude save`
`Page8Button7Name=exclude`
`Page8Button7Color=0`
`Page8Button7Line1=/bcaa //mb exclude ${Target.CleanName}`
`Page8Button7Line2=/pause 5`
`Page8Button7Line3=/bcaa //mb exclude save`
`````
```

`I normally just keep my keys on page 10 and click from there, but as you can see there's include and exclude keys on pg 8 and another on pg2 I use for setting items to`
`"sell" in my loot.ini file.`
`The /bcaa stuff might not work for some depending on plugin versions, so that cn be replaced with a /bca and /mb on a second line. I find it very handy to have some keys I can`
`press quickly, and always either pause all my toons or exclude npcs before I go into areas that I don't want something attacked.`

`Having trouble with your background session toons not moving properly? You might try this:`
````` WinEQ=on```to the [Defaults] section of your mq2moveutils.ini.````` TrueHeading=off might help also in the same section, though I'm not sure if that's needed.\`

### Do your toons wander where they are not supposed to?

Thanks to Toomanynames for this tidbit:

Those who have toon wandering issues or whatnot - when you say "radius", what radius do you mean, modbot, melee, makecamp? There are actually three things that work together to make certain that your bots fight and return to a certain area - MQ2MoveUtils, MQ2Melee and the MB\_charname.ini file (from ModBot).

* **/makecamp x x x**
  * This is a MQ2MoveUtils setting that needs to be properly configured. For example:
    * /makecamp radius x leash=on (or something like that)
  * Please see the MQ2MoveUtils (PMS version)

    [[http://www.macroquest2.com/phpBB3/viewtopic.php?f=31&t=15909](http://www.macroquest2.com/phpBB3/viewtopic.php?f=31&t=15909)**thread**] and

    MQ2MoveUtils:v11 for more detailed information.
* **/melee x x x**
  * This is an MQ2Melee setting. Those ranges and settings come into play and must be set accordingly to work

    **WITH** modbot

  * Please see the MQ2Melee [[http://www.macroquest2.com/phpBB3/viewtopic.php?f=50&t=17045](http://www.macroquest2.com/phpBB3/viewtopic.php?f=50&t=17045)**thread**] for more

    detailed information.
* **Modbot INI**
  * Radius = the max the toon will "See" thiings
  * ACLeash = the max a toon will engage things

If you don't properly configure MQ2MoveUtils, MQ2Melee and ModBot and confirm those settings are within or compatible with ModBot "ranges" then you'll have issues.

