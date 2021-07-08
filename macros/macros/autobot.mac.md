# AutoBot.mac

## Description

[AutoBot.mac](https://macroquest2.com/phpBB3/viewtopic.php?t=12712) by A\_Druid\_00 is a versatile [macro](../../documentation/macroquest2-macros.md) for automating a lot of tasks for your character in group, raid and solo situations.

## Requirements

[AutoBot.mac](https://macroquest2.com/phpBB3/viewtopic.php?t=12712) does not run on a default [MQ2 compilation](../../documentation/macroquest2-compiling.md), it has a few extra dependencies. Some of the below items are [Plugins](../../commands/slash-commands/plugin.md) and need to be compiled, just like MacroQuest2. Please read the appropriate documentation for each plugin. The Include files should be added to the same directory that AutoBot will be run from.

[Plugins](../../commands/slash-commands/plugin.md):

* [MQ2MoveUtils](https://macroquest2.com/phpBB3/viewtopic.php?t=11732) by Outlander

  This is so the macro knows about stick, /makecamp, and /moveto. Check out the

  [wiki](https://macroquest2.com/wiki/index.php/MQ2MoveUtils).

* [MQ2Exchange](https://macroquest2.com/phpBB3/viewtopic.php?t=7603) by Wassup

  This is so that item swapping, casting, and swapping back will work

* [MQ2Debuffs](https://macroquest2.com/phpBB3/viewtopic.php?t=13495) by pinkfloydx33

  This is so the macro can keep track of your debuff counters.

* [MQ2Melee](https://macroquest2.com/phpBB3/viewtopic.php?t=12779) by s0rcier

  So as to properly configure melee/ranged combat and various options thereof, check out the

  [wiki](https://macroquest2.com/wiki/index.php/MQ2Melee).

Includes Files:

* [Wait4Rez.inc](wait4rez.inc.md) Handles pre-rez situations.  
* [spell\_routines.inc](spell-routines.inc.md) Handles spell casting, from gems, items and AAs.  
* QuickBeg2.inc Handles buff begging.  
* [Ninjadvloot.inc](ninjadvloot.inc.md) Handles looting.  

## Getting Started

Pointers for AutoBot stuffs. \(We should make a multi-boxing wiki sometime, we could link it here...\)

In addition to the documentation for the various plugins used directly by AutoBot \(see links in [Requirements](https://macroquest2.com/wiki/index.php/AutoBot.mac#Requirements)\) The following is useful info on other plugins you can use to enhance your AutoBot experience.

[MQ2Clip](https://macroquest2.com/phpBB3/viewtopic.php?t=7692) by Vaft, Cr4zyb4rd, et al.  
Manages the clip plane of backgrounded sessions. Your CPU will thank you.

[MQ2FPS](https://macroquest2.com/phpBB3/viewtopic.php?t=8346) by Lax.  
Helps manage framerates of EQ sessions, greatly helps multi-botting... Check out the [wiki](https://macroquest2.com/wiki/index.php/MQ2FPS)

[MQ2Eqbc](https://macroquest2.com/phpBB3/viewtopic.php?t=12147) by Omnictrl  
Is an alternative way to communicate with your bots.  
Configure your EQBC.ini with the following:  
\[Last Connect\]  
Server=192.168.1.101 \(This must be edited to match the ip and port you have the server listening to\)  
Port=2112  
\[Settings\]  
AutoConnect=1  
AllowControl=1

You will also need to change the channel setting in your AutoBot.ini from "i say" to "bc" to use it for bot to bot communication. Don't forget that if you are getting identify spam that you check loot.ini and QB2Settings.ini for any i say or i msg commands. QB2Settings.ini defaults to i msg and needs to be changed if using EQBC. Recommend [MQ2NetBots](https://macroquest2.com/phpBB3/viewtopic.php?t=12186), [MQ2NetStat](https://macroquest2.com/phpBB3/viewtopic.php?t=12186), and [MQ2NetHeal](https://macroquest2.com/phpBB3/viewtopic.php?t=12312&highlight=mq2netheal) to go along with this. More information available on [Page 59](https://macroquest2.com/phpBB3/viewtopic.php?t=11619&postdays=0&postorder=asc&highlight=eqbc+autobot&start=870) of the original AutoBot thread.

## Using AutoBot.mac

1\) The main macro file, 'yyy.mac' \(called 'RaidDruid.mac' in the .zip file\) can be named to 'AutoBot.mac' or 'AnythingYouWant.mac'.  
2\) To start the macro in EverQuest with MQ2 running; type '/macro yyy.mac  
Note: The first time you run the macro, it will generate an ini file called RD\_xxx.ini  
3\) Configure your RD\_xxx.ini, where 'xxx' is your character name.  
3a\) Peruse through [RDCommon.ini](rdcommon.ini.md) and add in any mobs you might want to have certains spells ignore. I tend to put Guild Lobby and PoK NPCs as immune to mez, makes life simpler when walking around and I forget to pause my bots.  
4\)Restart Autobot after configuring RD\_xxx.ini.  
5\) Enjoy the show.

## Bot Commands

There are a few non-alias \(no / required\) commands available to Autobot. These commands will cause the bots to respond to a few general status/movement commands without the obvious /alias, for easy use in a group setting. Bots will only respond to commands sent by someone in the MasterList  
**buffqueue**  
This command has your bot respond in your ChatChannel with the \# of buffs left in his "buff queue". Handy for deciding whether to continue pulling/crawling after a group wipe. Keep in mind that some longer cast spells such as Night's Dark Terror for enchanters have extremely long recast times, and so can sit in the queue for a while.  
**follow**  
This command will have your bots /stick to you. They will sit to med if needed and within your LeashLength. They will also break off to attack if /domelee is turned on and the MA is fighting something. They will also service buff requests and do debuffing if applicable and they are not moving.  
**mana**  
All bots with a mana pool bigger than 0 will report their current % mana in your /chatchannel.  
**medtime**  
All bots with a mana pool bigger than 0 will report their currently estimated time to full mana based on their current Mana Regen divided by their mana level.  
**move up**  
This command tells your bots to move up to your current location. If they are set to /makecamp, they will reset their camp X and Y loc to your current position. If they are following, they will resume following once they reach your position \(This is handy for positioning your bots in front of doors/bridges before moving through/across them\)  
**stop**  
This command tells the bots to stop following wherever they happen to be standing.

## Slash Commands

[AutoBot.mac](https://macroquest2.com/phpBB3/viewtopic.php?t=11619) comes with a great set of predefined [Slash Commands](../../commands/slash-commands/) for easy and fast in-game configuration.  
Uber macro pause/unpause hotkey \(bound to  for me, unlike normal EQ hotkeys 1-10, it works even while casting\) Add the following lines to [MQ2CustomBinds](https://macroquest2.com/wiki/index.php/MQ2CustomBinds).txt:

`name=StartPauseDB`  
`down=/docommand ${If[!${Macro.Name.Equal[RaidDruid.mac]}, /mac RaidDruid.mac, /varset RDPause ${If[${RDPause}==1,0,1]}]}`  
`up=`

Then in game type _/bind StartPauseDB \_ to bind that to your _\_ key. When pressed your _\_ key will start AutoBot if it's not already started. If it's already running it will toggle the pause on the macro.

Here's a full list, divided into sub-sections for each category of [Slash Commands](../../commands/slash-commands/) there are \(Each toggle alias works by itself, or will take an argument of ON/OFF, TRUE/FALSE, or 1/0\):

### Melee

* **/domelee**

  Toggles automatic engaging of the MA's target in melee.\(Must have the plugin

  [MQ2Melee](https://macroquest2.com/phpBB3/viewtopic.php?t=12221) configured properly\)

### General

* **/addalert ${Target.CleanName}**

  Adds targetted NPC to the list which will be ignored in the RDCommon.ini and will perform normally when near these

  npc's not treating them as hostile. ${Target.CleanName} can also be replaced with the name of the mob typed out or

  the ini file can be manually edited.

* **/assistdelay**

  Sets the amount of time the bot will wait between MA assists. \(Ex. /assistdelay 5s\)

* **/assistma**

  Toggles assisting of your designated MA1, MA2, and MA3. Turning this off essentially disables Melee, Nuking, DoTing,

  and Debuffing

* **/autoninja**

  Toggles auto looting of the nearest corpse after each XP gained message. Will only loot droppable items. Must have

  the plugin [MQ2MoveUtils](https://macroquest2.com/phpBB3/viewtopic.php?t=11732) for this to work.

* **/autosit**

  Toggles auto sitting to med. Not much to say here.

* **/chatchannel**

  Sets the chat channel the bot reports to, \(Ex. /chatchannel "i say"�\)

* **/docanni**

  Toggles auto casting of your cannibalization spell when below your MedPct and above your CanniHPs. Also works for

  wizard harvest, mana robe, and necromancer Lich spells.

* **/doyaulp**

  Toggles auto casting of your yaulp spell when below your MedPct and there are NPCs within your NPCRadius.

* **/engagehps**

  Sets the % of the mobs HPs you want to start melee/debuffing/dotting/nuking \(Ex. /engagehps 95\)

* **/ma1**

  Assigns a PC as Main Assist 1. \(Ex. /ma1 BoDuke\)

* **/ma2**

  Assigns a PC as Main Assist 2. \(Ex. /ma2 LukeDuke\)

* **/ma3**

  Assigns a PC as Main Assist 3. \(Ex. /ma3 DaisyDuke\)

* **/leashlength**

  Sets the distance your bot will allow itself to get from his follow target before resuming follow \(Ex.

  /leashlength 25\)

* **/listspells**

  Returns a list of all configured Spell Sets in your ini.

* **/loadini "IniFileName"**

  Loads a pre-configured ini file.

* **/medpct**

  Sets the % of Mana you want to sit or summon your horse at. \(Ex. /medpct 50\)

* **/npcradius**

  Sets the Radius \(in feet\) around you that you want to watch NPCs using Assist healing and Assisting the MA \(Ex.

  /npcradius 200\)

* **/npczradius**

  Sets the Radius \(in feet\) above/below you that you want to watch NPCs using Assist healing and Assisting the MA \(Ex.

  /npczradius 200\)

* **/rdpause**

  Toggles AutoBot's active functions on and off.

* **/relaytells**

  Toggles automatic reporting of tells sent to the bot in your configured /chatchannel

* **/reportevents**

  Toggles automatic reporting of your bot's status messages such as low food/drink, stunned/unstunned, encumbered,

  etc.

* **/reportmana**

  Toggles automatic reporting of your mana status if you get below the medpct, only reports once before going above

  the medpct.

* **/reportmanapct**

  Defines the point at which you want to start reporting your mana status to your chat channel.

* **/reporttoggles**

  Toggles automatic reporting of your toggle status of any /commands you send your bot in the ChatChannel.

* **/reportwow**

  Toggles automatic reporting of Wrath of the Wild on the MA

* **/saveini "IniFileName"**

  Creates an ini file named "IniFileName"

* **/sitdelay**

  Sets the amount of time you want to wait before sitting after casting any spell that might be considered aggro. \(Ex.

  /sitdelay 5s\)

* **/stophps**

  Sets the % of the mob's HPs you want to stop nuking and debuffing. \(Ex. /stophps 10\)

* **/usemount**

  Toggles automatic mount summoning at your /medpct, if this is off and /autosit is on, it will sit to med instead of

  summoning a mount.

* **/npcradchk**

  Sets the Radius \(in feet\) around you that defines how close mobs are allow before you stop buffing to avoid aggro

  \(Ex. /npcradchk 100\)

### Healing

* **/aeheal**

  Toggles on AE Healing. This creates an array of every PC within PCRadius, and cycles through every one of them,

  checking their HPs against your defined HealPct, and casts heals if appropriate. Super handy on mobs with AE Rampage

  or AE Damage effects.

* **/assistheal**

  Toggles on Assist Healing. This creates an array of every NPC within NPCRadius, and assists them to find the target

  of their aggression, and heals that target if necessary. Super handy for general clearing on raids before getting to

  named. Also causes target to constantly ping-pong wildly all over the place trying to find a target to heal

* **/cancelpct**

  Set this to the percentage of HPs you want AutoBot to cancel heals at. \(Ex. /cancelpct 90\)

* **/checkgroup**

  Sets the number of seconds you'd like to wait between HP evaluations

* **/divarbhps**

  Sets the % HPs you want to cast Divine Arbitration at if a groupmember gets below it \(Ex. /divarbhps 25\)

* **/healchannel**

  Sets the channel your bots use to report heals when they are cast.

* **/healfd**

  Toggles healing of FD classes \(SK, Necro, Monk\) only while they are FD \(Ex. /healfd ON will only heal if they are

  FD\)

* **/healgroup**

  Toggles healing of your group. With this on, it will heal groupmembers that are below HealPct

* **/healmefirst**

  Toggles healing of yourself over any group members. If you are mid-cast to heal someone else and your HPs fall below

  the HealPct, you will cancel it and heal yourself first. Self preservation at its finest.

* **/healpct**

  Sets the % of HPs you want to heal other PCs at. \(ex. /healpct 70\)

* **/healpets**

  Toggles healing of any pets in the group if they are below the PetHealPct

* **/healramp**

  Toggles automatic healing of your Rampage tank anytime a RAMPAGE message is detected.

* **/interrupt**

  Toggles interrupting debuffs/nukes/dots to heal group members. Some people like to just let their group members die

  instead of ducking a nuke to heal them. This is for those people!

* **/pcradius**

  Sets the Radius \(in feet\) around you that you want to watch PC HPs using AE healing \(Ex. /pcradius 200\)

* **/pczradius**

  Sets the Radius \(in feet\) above and below you that you want to watch PC HPs using AE healing \(Ex. /pczradius 50\)

* **/pethealpct**

  Sets the % of HPs you will heal pets at. \(Ex. /pethealpct 40\)

* **/ramptank**

  Sets the Rampage Tank that you check whenever a RAMPAGE message is seen with /healramp on. \(Ex. /ramptank

  UncleJesse\)

* **/reportheals**

  Toggles automatic reporting of heals in the ChatChannel

* **/reportinterrupts**

  Toggles automatic reporting of interrupts to heal in the ChatChannel

* **/reportsotw**

  Toggles automatic reporting of Spirit of the Wood in the ChatChannel

* **/sotw**

  Toggle auto casting of Spirit of the Wood

* **/sotwpct**

  Set this to the average group HP percentage you want it to auto cast Spirit of the Wood at. \(Ex. /sotwpct 75\)

* **/tankhealpct**

  Sets the % you start Chealing. Due to some predictive logic the Cheal may start earlier. Set this to the abslute

  floor you want to start CH at.

* **/usech**

  Toggles using your Cheal spell on MA1 on or off. It will monitor the tank's HPs and if he's taking enough damage to

  be dead in less than 20 seconds, it will duck out of whatever RD is currently doing and start a CH. If the tank's

  HPs stop falling and level off above the TankHealPct, it will cancel CH and wait until the tank's HPs fall again.

* **/usedivarb**

  Toggles using your divine arbitration or cleric epic 1.5 \(if you have it\) when a group member falls below the

  DivArbHPs.

* **/waittocancel**

  Toggle. When turned on, this will wait until your heals have less than .5 seconds left before making the decison to

  cancel the heal.

### Buffing

AutoBot queues buff requests and casts them when appropriate. It will not cast buffs unless there are no mobs within 20 feet of the bot, it's not in combat, and it's not moving. It will hold onto those buff requests until you are no longer moving, not in combat, and there are no mobs within 20 feet. If you zone, all stored buffs are flushed, and you have to beg again.  
By default the bot only listens for /tells and IRC chat for buffing. If you want him to listen in other channels, you need to add **\#chat group** to listen in group, or **\#chat chat** to listen in EQ's chat channels; to the RaidDruid.mac file under the **\#chat tell** line right near the top of the macro. More information on the \#chat function can be found in the MacroQuest [manual](https://macroquest2.com/includes/wassup/manual.php).

**Aliases:**

* **/buff "Spell Name/Alias" \[Name \| Group\]**

  Use this alias to send a buff command to your bot, will also accept buff aliases. You can use this to cast items and

  AAs as well as spells. If you specify Group instead of a name, it will buff your whole group with that spell, if it

  is a single target spell. In addition, you can cast it on any spawn including NPCs, Pets, Corpses, etc. \(Ex. /buff

  "Steeloak Skin"� Bob, or /buff Oak Bob if oak is an alias for steeloak skin\). If the /buff command utilizes a DoBuff

  alias, the buff request is queued and will not be performed during combat. If the Spell/AA/item name itself is used

  in the /buff command it is cast immediately. \(Ex. /buff "Exodus" would fire right away, while /buff "Evac" would

  not\). \*\*WARNING: YOUR BOTS WILL NOT WATCH THE GROUP'S HPS OR ANYTHING ELSE WHILE EXECUTING A /BUFF COMMAND, USE IT

  WHEN YOU KNOW YOU DON'T NEED TO BE DOING ANYTHING ELSE IMPORTANT LIKE HEALING\*\*

* **/dobuffs**

  Toggles automatic casting of buff requests made via /tell

* **/dobufftells**

  Toggles sending automatic replies to buff requests made via /tell

* **/refreshbuffs**

  Toggles automatic refreshing of buffs. Only buffs that are set to refresh in the ini will be refreshed.

* **/reportdobuffs**

  Toggles automatic reporting of buffs in the ChatChannel

* **/reportselfbuffs**

  Toggles automatic reporting of self buffs in the ChatChannel

* **/selfbuff**

  Toggles Self Buffing. Useful if you happen to be in an environment where having all your self buffs up puts you over

  the limit

* **/wow**

  Toggles automatic casting of Wrath of the Wild on your designated MA. I figure an extra 650 damage every 4 minutes

  cant hurt, since its mana free and all.

### Debuffing

* **/debuff**

  Toggles Auto debuffing. Pretty much all there is to say about that

* **/debuffchannel**

  Sets the channel your bots will use to report debuffs

* **/dot**

  Toggle Auto DoTing of mobs

* **/mez**

  Toggles Auto mezzing for those places where mez==bad

* **/reportdebuffs**

  Toggles reporting of debuffs in the ChatChannel

* **/reportdots**

  Toggles automatic report of DoTs in the ChatChannel

* **/reportmez**

  Toggles automatic report of Mezzes in the ChatChannel

* **/usehott**

  Toggles using the Health of Target's Target Leadership ability to determine a mob's aggro.

### Nuking

* **/nuke**

  Toggles Auto Nuking the MA's target.

* **/nukedelay**

  Sets the delay between chain nuking. If your tank sucks, or are in a kite group raise this delay to prevent agro.

* **/nukeset**

  Returns the current spell set \# you are nuking from.

### Pet

* **/petbuff**

  Toggles automatic buffing of your pet

* **/usepet**

  Toggles automatic summoning and sending in of pet to melee.

### Curing

This portion of the macro requires the [MQ2Debuffs](https://macroquest2.com/phpBB3/viewtopic.php?t=13495) plugin by pinkfloydx33. See the [requirements](https://macroquest2.com/wiki/index.php/AutoBot.mac#Requirements).

* **/docures**

  Toggles auto-curing on and off.

* **/reportcures**

  Toggles auto-cure reporting on and off.

### Bard

This portion of the macro makes use of the [MQ2Twist](https://macroquest2.com/phpBB3/viewtopic.php?t=8895) \(See [MQ2Twist wiki](https://macroquest2.com/wiki/index.php/MQ2Twist)\) and [MQ2BardSwap](https://macroquest2.com/phpBB3/viewtopic.php?t=9178) plugins.

* **/addcombatsong \|""**

  Adds the Alias or Song Name to the combat twist if a slot is available.

* **/addrestsong \|""**

  Adds the Alias or Song Name to the rest twist if a slot is available.

* **/autorestoff**

  When turned on it watches with each loop to see if any npc's are within the radius defined and will switch off rest

  songs if any are detected

* **/autorestradius**

  Sets the radius at which your bard will stop twisting when NPCs are present

* **/combatsongs on\|off**

  Enables or Disables automatically twisting the combat twist temporarily.

* **/delcombatsong \|""**

  Removes the Alias or Song Name from the combat twist present.

* **/delrestsong \|""**

  Removes the Alias or Song Name from the rest twist if present.

* **/listsongs combat\|rest\|all**

  Lists the songs set to be twisted for the given twist type.

* **/songalias "Song Name"**

  Creates an alias for the given song name \(must be in quotes if it has a space\).

## INI entries

.ini files will be automatically created and populated with default values if they do not exist.

### \[MeleeStuff\]

**DoMelee=1** _\(Set by /domelee\)_  
**DoRanged=1** _\(0=Don't use ranged attacks, 1=Use Ranged attacks\)_  
**StickArgs=10 pin** _\(Set by /stickargs\)_  
**DiscTotal=1** _\(Set this to the total number of melee disciplines you have defined\)_  
**UseDiscs=1** _\(0=Don't Disc, 1=Use Discs\)_  
**DiscName1=Furious Discipline** _\(Set this to the name of the Discipline you want to use\)_  
**DiscType1=0** _\(0=Defensive, 1=Offensive\)_  
**DiscEndurance1=10** _\(Set this to the % endurance you want to be above when triggering this disc\)_  
**DiscMinHPs1=10** _\(Set this to the min HPs of the mob or yourself that you want to trigger this disc at.\)_  
**DiscMaxHPs1=90** _\(Set this to the max HPs of the mob or yourself that you want to trigger this disc at.\)_  
**DiscSpawnCount1=2** _\(Set this to the \# of mobs you want to have in melee range before triggering this disc.\)_

### \[Settings\]

**LeashLength=25** _\(Set by /leashlength\)_  
**NPCRadius=75** _\(Set by /npcradius\)_  
**NPCZRadius=100** _\(Set by /npczradius\)_  
**PCRadius=200** _\(Set by /pcradius\)_  
**PCZRadius=100** _\(Set by /pczradius\)_  
**AutoNinja=0** _\(Set by /autoninja, 0=off and 1=on\)_  
**FoodSpell=Abundant Food** _\(Set this to the name of the spell/item/alt you use to summon food\)_  
**FoodGem=gem1** _\(Set this to gem\#, item, or alt; as applicable to summon food\)_  
**DrinkSpell=Abundant Drink** _\(Set this to the name of the spell/item/alt you use to summon drink\)_  
**DrinkGem=gem1** _\(Set this to gem\#, item, or alt; as applicable to summon food\)_  
**AutoSit=1** _\(Set by /autosit, 0=off and 1=on\)_  
**SitDelay=5s** _\(Set by /sitdelay\)_  
**UseMount=1** _\(Set by /usemount, 0=off and 1=on\)_  
**MountItem=Black Rope Bridle** _\(This is the item you use to summon your mount\)_  
**MedPct=50** _\(Set by /medpct\)_  
**UseRods=0** _\(Set by /userods\)_  
**RodMana=50** _\(Set this to the % mana you want to be below before clicking your mod rods\)_  
**RodSpell=Rod of Mystical Transvergance** _\(Set this to the spell you use to summon mod rods\)_  
**RodGem=gem1** _\(Set this to gem you want to cast this from, or put item for items, alt for AAs\)_  
**GatherPct=10** _\(Set this to the % mana you want to use your Gather Mana\)_  
**NPCRadChk=100** _\(Set by /npcradchk\)_

### \[GeneralStuff\]

**ChatChannel=i say** _\(Set by /chatchannel\)_  
**MasterList=\|AlGore\|BobDole\|DanQuayle\|** _\(This is the list of people you want to be able to send you commands\)_  
**AssistMA=1** _\(Set by /assistma, 0=off and 1=on\)_  
**AssistDelay=5s** _\(Set by /assistdelay\)_  
**MA1=HappyGilmore** _\(Set by /ma1\)_  
**MA2=BillyMadison** _\(Set by /ma2\)_  
**MA3=MrDeeds** _\(Set by /ma3\)_  
**EngageHPs=95** _\(Set by /engagehps\)_  
**StopHPs=20** _\(Set by /stophps\)_  
**ReportEvents=1** _\(Set by /reportevents\)_  
**ReportToggles=1** _\(Set by /reporttoggles\)_  
**RelayTells=1** _\(Set by /relaytells\)_  
**ReportMana=1** _\(Set by /reportmana\)_  
**ReportManaPct=50** _\(Set by /reportmanapct\)_  
**SpellSetTotal=1** _\(Set this to the \# of unique spell sets you have defined for nukes/debuffs\)_  
**SpellSet1=SomeSpellSetName** _\(Put the name of the Spell Set you want to memorize when you die while using this spell set here. Needs to match the name of the spell set you have saved in EQ to work properly\)_  
**CanniTotal=1** _\(Set this to the total cannibalization/harvest AAs/items/spells you want to check and cast\)_  
**DoCanni=1** _\(Set this to 1 if you want to use your Canni AAs/items/spells when you fall below your medpct\)_  
**CanniSpell1=Harvest** _\(Set this to the name of your canni aa/item/spell. This section also works for Lich and any other Canni type spells that have a buff icon\)_  
**CanniGem1=gem6** _\(Set this to spell gem you want to cast your canni spell from, or put alt if an AA, or item if its an item\)_  
**CanniHPs1=0** _\(Set this to the % HPs you want to stop using your canni AA at\)_  
**DoWoW=1** _\(Set by /wow, 0=off and 1=on\)_  
**ReportWoW=1** _\(Set by /reportwow\)_  
**DoYaulp=1** _\(Set this to 1 if you want to use Yaulp when mobs are close by instead of sitting\)_  
**YaulpSpell1=Yaulp VII** _\(Set this to the name of your Yaulp spell\)_  
**YaulpGem1=gem6** _\(Set this to spell gem you want to cast your Yaulp spell from\)_

### \[HealStuff\]

**ReportHeals=1** _\(Set by /reportheals\)_  
**ReportInterrupts=1** _\(Set by /reportinterrupts\)_  
**HealChannel=echo** _\(Set by /healchannel\)_  
**HealMeFirst=1** _\(Set by /healmefirst\)_  
**HealFD=0** _\(Set by /healFD, 1 only heals FD classes while FD, 0 heals normally\)_  
**GroupHealing=1** _\(Set by /healgroup, 0=off and 1=on\)_  
**CheckGroupInterval=3** _\(Set by /checkgroup, and sets how often you check group HP levels for healing\)_  
**AutoInterrupt=1** _\(Set by /interrupt, 0=off and 1=on\)_  
**RampHealing=0** _\(Set by /healramp, 0=off and 1=on\)_  
**RampTank=BigDaddy** _\(Set by /ramptank\)_  
**AEHealing=0** _\(Set by /aeheal, 0=off and 1=on\)_  
**AssistHealing=0** _\(Set by /assistheal, 0=off and 1=on\)_  
**HealPct=30** _\(Set by /healpct\)_  
**CancelPct=90** _\(Set by /cancelpct\)_  
**WaitToCancel=1** _\(Set by /waittocancel\)_  
**FastHeal=Chlorotrope** _\(This is your fast healing spell\)_  
**FastHealGem=gem2** _\(This is the gem you cast your Fast Heal from if it's not memmed already\)_  
**UseCH=1** _\(Use Chealing... or not, 1 for on, 0 for not\)_  
**TankHealPct=70** _\(This is the % you heal MA1 at\)_  
**TankHeal=Karana's Renewal** _\(Heal spell to use on the tank... usually your Cheal\) **MUST** be defined and a different spell than FastHeal, even if not used._  
**TankHealGem=gem8** _\(Spell slot for your tank heal spell\)_  
**PetHealing=1** _\(Set by /healpets\)_  
**PetHealPct=50** _\(Set by /pethealpct\)_  
**PetHeal=Karana's Renewal** _\(Put the name of the spell you wish to use to heal your group's pets here\)_  
**PetHealGem=gem1** _\(Put the gem you wish to cast your pet heal from if its not memmed\)_  
**DoSotW=1** _\(Set by /sotw, 0=off and 1=on\)_  
**ReportSotW=1** _\(Set by /reportsotw\)_  
**SotWAA=Spirit of the Grove** _\(This is the Actual Alt ability you have, set it to whichever one you have\)_  
**SotWPct=80** _\(Set by /sotwpct\)_  
**UseDivArb=0** _\(Set by /usedivarb\)_  
**DivArbHPs=20** _\(Set by /divarbhps\)_  
**UseBDA=0** _\(Set this to 1 if you want to cast Bestow Divine Aura on groupmembers when Divine Arbitration is not up\)_

### \[CureStuff\]

**CureTotal=1** _\(Put your total number of cure spells here\)_  
**DoCures=0** _\(0=Don't Cure, 1=Cure\)_  
**ReportCures=0** _\(0=Don't Report, 1=Report\)_  
**CureSpell1=Resplendent Cure** _\(Put the name of the item, alt, or spell you use to cure with here\)_  
**CureGem1=alt** _\(Put item for item, alt for AA, or the gem\# you want to use to cure with here\)_  
**CurseCounters1=50** _\(Set this to the \# of curse counters you want this to react to \(For example if the spell cures 25 curse counters and you want it to only cure if it can do it in 2 casts or less, set it to 50\)\)_  
**DiseaseCounters1=50** _\(Set this to the \# of Disease counters you want this to react to \(For example if the spell cures 25 Disease counters and you want it to only cure if it can do it in 2 casts or less, set it to 50\)\)_  
**PoisonCounters1=50** _\(Set this to the \# of Poison counters you want this to react to \(For example if the spell cures 25 Poison counters and you want it to only cure if it can do it in 2 casts or less, set it to 50\)\)_

### \[SelfBuffStuff\]

**SelfBuffTotal=9** _\(Put your total number of self buffs here\)_  
**SelfBuffs=1** _\(Set by /selfbuff, 0=off and 1=on\)_  
**ReportSelfBuffs=1** _\(Set by /reportselfbuffs\)_  
**SelfBuffRecheck=10s** _\(Sets how often you check to see if your self buffs are going to fade\)_  
**SelfBuff1=Shrunken Goblin Skull Earring** _\(This is the name of the item or spell you use for self buff 1\)_  
**SelfBuffIcon1=Grim Aura** _\(This is the name of self buff 1 as it shows up in your buff window\)_  
**SelfBuffGem1=item** _\(This is the gem you cast self buff 1 from, if it's an item put item, if it's an AA put alt\)_  
**SelfBuffCount1=14** _\(Put the number of buffs you would like to stop casting this buff after, i.e if you want to leave a couple buff slots open, set your self buffs up so that the could is never equal to your max number of buff slots\)_

### \[DoBuffStuff\]

**DoBuffTotal=10** _\(Put the total number of DoBuff entries you have here\)_  
**DoBuffs=1** _\(Set by /dobuffs, 0=off and 1=on\)_  
**ReportDoBuffs=1** _\(Set by /reportdobuffs\)_  
**DoBuffTells=0** _\(Set by /dobufftells\)_  
**RefreshBuffs=1** _\(Set by /refreshbuffs\)_  
**DoBuff1=Woven Grass Boots** _\(Put the name of the item, aa, or spell you cast this buff with here\)_  
**DoBuffIcon1=Spirit of Wolf** _\(This is the name of dobuff 1 as it would show up in your buff window\)_  
**DoBuffGem1=item** _\(This is the gem you cast dobuff 1 from, if it's an item put item, if it's an AA put alt\)_  
**DoBuffMana1=0** _\(Set this to the % mana you'd like to be above before handling this buff request\)_  
**DoBuffAliases1=SoW\|Spirit\|** _\(This is the string of different buff messages you want the druid bot to respond to, separated by the \|. Make sure to have a \| for each buff, as it needs to count them to find out how many buff request strings to check for. Also be mindful of spaces, as the buff request will not be registered without the preceding and trailing spaces defined in the alias. Ex: If the alias were set up as \| Rune \|. "I could use a Rune right about now" would trigger the request while "Rune" alone would not, unless the alias is actually defined with no spaces as \|Rune\|\)._  
**DoBuffRefresh1=1** _\(Set this to 1 if you want to refresh this buff when it wears off\)_  
**BattleBuff1=FALSE** _\(Set this to TRUE if you would like to cast this buff with mobs nearby and/or in Combat.\)_  
**BuffGem=gem3** _\(Set this to the spell gem you want to cast your /buff commands from\)_

### \[DebuffStuff\]

**DebuffTotal=3** _\(Put the total number of Debuff entries you have here\)_  
**DoDebuffs=1** _\(Set by /debuff, 0=off and 1=on\)_  
**DoDoTs=1** _\(Set by /dot, 0=off and 1=on\)_  
**DoMez=1** _\(Set by /mez, 0=off and 1=on\)_  
**DoManaTaps=1** _\(0=off and 1=on\)_  
**ReportDebuffs=1** _\(Set by /reportdebuffs\)_  
**ReportDoTs=1** _\(Set by /reportdots\)_  
**ReportMez=1** _\(Set by /reportmez\)_  
**DebuffChannel=echo** _\(Set by /debuffchannel\)_  
**UseHoTT=1** _\(0=off and 1=on\)_  
**MaxMobs=1** _\(Set this to the maximum number of mobs you would like AutoBot to keep track of\)_  
**AllDebuffsFirst=1** _\(Set this to 1 if you want to land all your debuffs on each mob before moving on to debuff the next\)_  
**DebuffMAFirst=1** _\(Set this to 1 if you want to land all your debuffs on the MA's target before moving on to any adds\)_  
**DebuffSpell1=Hand of Ro** _\(Put the name of the item, aa, or spell you cast this debuff with here\)_  
**DebuffIcon1=Hand of Ro** _\(This is the name of debuff 1 as it would show up in your buff window\)_  
**DebuffGem1=gem5** _\(This is the gem you cast debuff 1 from, if it's an item put item, if it's an AA put alt\)_  
**DebuffMana1=1** _\(Set this is to the % mana you would like to stop casting this debuff at.\)_  
**DebuffHPs1=1** _\(Set this is to the % HPs you would like to start casting this debuff at.\)_  
**DebuffStopHPs1=1** _\(Set this is to the % HPs you would like to stop casting this debuff at.\)_  
**DebuffRecast1=3** _\(Set by /debuffrecast\)_  
**DebuffSpellSet1=1** _\(This is the spell set you want to cast this debuff with. 0=all spell sets, 1=spell set \#1, etc.\)_  
**DebuffMAOnly1=1** _\(Set this is to 1 if you want to land this debuff on the MA's target only, and exclude adds.\)_  
**DebuffNamedOnly1=1** _\(Set this is to 1 if you want to land this debuff on named targets only, and not normal XP mobs.\)_  
**DebuffMessage1=%Target Debuffed by %Spell** _\(This is your custom debuff message when you successfully land a debuff. Use %Target to report the target's name, %Spell to report the spell name, and %Duration to report the duration of the spell you just landed\) Or set to None for no message._  
**SpellType1=1** _\(Set this is to 0 for debuffs, 1 for DoTs, 2 for Mez, and 3 for Mana Tap spells\)_  
**DebuffCondition1=TRUE** _\(Code conditions can be put here such as "{Target.Body.Name.Equal\[Undead\]} or !{Target.Buff\[Turgur's Swarm\].ID} Default is TRUE \)_

### \[NukeStuff\]

**NukeTotal=1** _\(Set this to the number of nukes you have defined\)_  
**DoNukes=1** _\(Set by /nuke, 0=off and 1=on\)_  
**NukeDelay=1** _\(Sets the delay in re-casting nukes, usefull when you have sucky tanks with low agro. Format for a 10 second delay is either 10s or 100\)_  
**WhichNuke=1** _\(Sets which nuke to use 1=SpellSet \#1, etc.\)_  
**Nuke1=Solstice Strike** _\(Set this to the name of the Nuke you want to cast\)_  
**NukeGem1=gem7** _\(Set this to gem\#, \# being the gem you want to mem this nuke in\)_  
**NukeSpellSet1=1** _\(Set this to the spell set you want to be using to cast this nuke\)_  
**NukeStartHPs1=100** _\(Set this to the % of the mob's HPs you want to start dropping bombs on it. Some classes might want to use a smaller nuke when a mob gets under say 30% HPs, in order to prevent wasting mana\)_  
**NukeStopHPs1=30** _\(Set this to the % HPs you want to stop nuking with this spell at\)_  
**NukeMaxMana1=30** _\(The highest % mana you want to be when using this nuke. Most of us will want this at 100%, but some classes \(such as wizards\) might want to switch out to a small nuke when under 50m, and use a bigger one when over 50m.\)_  
**NukeMinMana1=30** _\(Set this to the lowest % mana you want to be before you stop nuking. Essentially this is where most of us set our mana reserve for other duties such as healing, debuffing, etc. For wizards though, this provides the ability to stop nuking with one spell, and start nuking with another spell below this % using the same % for MaxMana\)_  
**GoMNuke1=0** _\(Set this to 0 if you don't want to cast this Nuke when Gift of Mana is up. Set it to 1, and it will use this nuke when GoM is up. Another addition mainly for wizards, it provides them the opportunity to get a 1 mana cost monster nuke off, instead of wasting it on a crappy lure or something. If set to 1, it will stop debuffing in favor of nuking while Gift of Mana is up. If you want to get your debuffing done over all else, then leave this at 0. Your bots will still heal and mez normally if set to 1, but debuffs are ignored as long as the buff is up\)_  
**DoConcussion=1** _\(0=Don't Concussion, 1=Do Concussion\)_  
**ConcussionSpell=Concussion** _\(Set this to the name of the Item, Alt, or Spell you use for Concussion\)_  
**ConcussionGem=gem1** _\(Set this to Item for items, Alt for AAs, or gem\# for Spells\)_

### \[PetStuff\]

**UsePet=1** _\(Set by /usepet\)_  
**PetMana=10** _\(Set this to the % mana you'd like to be above before casting your pet.\)_  
**KillFlappy1=1** _\(0=Keep your familiar, 1=Kill your Familiar\)_  
**PetFocus=Some focus item** _\(Set this to the item you want to equip before casting your pet\)_  
**PetSpell=Nature Walkers Behest** _\(Set this to your Pet spell\)_  
**PetGem=gem4** _\(Set this to the gem you want to cast your pet from\)_  
**PetBuffTotal=1** _\(Set this to the total number of pet buffs you want to cast\)_  
**DoPetBuffs=1** _\(1=pet buffing on, 0= pet buffing off\)_  
**ReportPetBuffs=1** _\(1=pet buffing reporting on, 0= pet buffing reporting off\)_  
**PetBuffRecheck=10s** _\(Set this to how often you'd like to re-check your pet's buffs for wearing off\)_  
**PetBuff1=Pet Buff Item/Spell name**  
**PetBuffIcon1=Pet Buff Item/Spell Icon name**  
**PetBuffGem1=Pet Buff Item/Spell Gem name**  
**PetShrink=1** _\(1=pet shrinking on, 0=pet shrinking off\)_  
**PetShrinkSpell=Tiny Companion** _\(Set this to the Name of the spell/aa/item you use to shrink your pet\)_  
**PetShrinkGem=gem4** _\(Set this to the gem you want to shrink your pet from\)_  
**PetItemTotal=1** _\( Your total number of pet item buffs. If you have 2 weapons you want to summon, you currently have to define the same weapon twice, so set this accordingly\)_  
**PetItemSpell1=Blazing Stone of Demise** _\( The name of the spell/aa/item you want to summon with\)_  
**PetItemGem1=item** _\(gem\# for spells, item for items, alt for AAs.\)_

### \[HolyShit\]

**TotalShit=1** _\(Set this to the total number of HolyShit Abilities you have defined\)_  
**DoHolyShit=1** _\(1=On, 0=Off\)_  
**HolyShit1=Oaken Guard** _\(Name of Item/AA/Spell/disc to use\)_  
**HolyShitGem1=gem9** _\(Put the HolyShit Gem\#, alt, item, or skill\)_  
**HolyShitHp1=70** _\(HP level you want to be below before triggering this ability\)_  
**HolyShitType1=0** _\(0=Just cast, 1=Target yourself, 2=Target the mob hitting you, 3=Ability like "Lay Hands"\)_  
**HolyShitRUN1=0** _\(1=Attempt to run away from the mob towards the MA after casting this spell. 0=stand there and do nothing after casting\)_

### \[Bard\]

**DoBardSwap=False** _\(Enables_ [_Bardswap plugin_](https://macroquest2.com/phpBB3/viewtopic.php?t=9178) _automatically on startup if set to True\)_  
**DoBardMeleeSwap=False** _\(Enables_ [_Bardswap_](https://macroquest2.com/phpBB3/viewtopic.php?t=9178) _to swap in melee weapons as well automatically on startup if set to True\)_  
**AutoRestOff=0** _\(Set with /autorestoff\)_  
**AutoRestRadius=125** _\(Set with /autorestradius\)_

### \[Bard-Combat\]

**SongsArray1-8=Song Name** \*\(Set via /addcombatsong \|. Removed with /delcombatsong

\|. Add in extra entries as you gain spell gems.\)\*

### \[Bard-Rest\]

**SongsArray9-18=Song Name** \*\(Set via /addrestsong \|. Removed with /delrestsong

\|.\*

### \[Bard-Aliases\]

**aliasname=songname** _\(Set via /songalias "song name"\)._ Songalias is basically to make it easier to change your combat/rest lineup on the fly with /addrestsong alias.

## Troubleshooting/FAQ

* **On I set my ini to service XXXX skill/spell/aa but its not working**  

got something spelled wrong or not filled out properly. check the examples again.

* **On Dots/Debuffs that don't work, but \(possibly\) used to**  

If in a group/raid with HoTT leadership skill set UseHoTT=1 in the ini file. If HoTT is not avialable you must set UseHoTT=0. Check to see the MaxMobs=5 is appropraite to the number of NPC's around you. Monsters that are green or sitting/laying down will never be debuffed/dotted.

* **On Buff requests not being serviced**  

Unless you indicate that you want the buff executed in combat the bot will not service the buff if there are NPC's nearby. You can have the macro ignore certain npcs that we know for certain arnt kos by adding their names in the RDCommon.ini .Alternatly the NPC check radius is adjustable in the ini. Also make sure that the buff name is spelled correctly just how it looks in the info window. Lastly make sure that the alias's are correct. in the example ini's it looks like this "\| convicton \| viction \| convic \|", however if you have it set up like that, the buff requester for all intents and purposes needs to put that word in a sentence. if you have the ini looking like this "\|convicton\|viction\|convic\|" with no spaces in between the " \| " then the bot will reconize and ackowlege any tell that has any of the word alias's it sees.

* **On Bot will assist but wont engage when set to**  

The bigest thing you do to fix that is increase the NPCRadius=120, Also, consider verifiying, and tweaking the following as well. NPCZRadius=120, AssistMA=TRUE, , DoMelee=TRUE, AssistDelay=0s, MA1=Chuck\_Norris, EngageHPs=101. aso remember that other options may be fighting for servicing. looting, selfbuffing, debuffing, buffing, etc.. so if melee is priority, turn everything but assisting off. also make sure that mq2melee is set up right. type /melee to bring up its console and see whats set and whats not. same thing goes. if your not a pet class turn off all that other stuff to prevent any chance of conflicts.

* **On Cant load selo's into the ini**  

Selos uses a "\`\`\`\`\`\`\`\`\`\`\`\`" located to the left of the 1 key.

* **On incorrectly mezed Targets \(also known as: Oh why does my chanter mez my MA's target?\)**  

You need to properly set the target for the BOT by the Leader AA, or /varset MATarget ${Target.ID} as explained in "On target acquisition"

* **On automatically mezzing NPCs when you don't want to**  

Set /rdpause on the BOT you want to stop auto debuffing \(rdpause stops all automatic activity\), type "/rdpause on" \(minus quotes\) into your command channel to stop auto-activity on multiple BOT's at once, or add the NPC you wish to not mez to the immune/ignore list in RDCommon.ini. You will need to know the spell ID for the spell you wish not to cast and this can be found by ${Spell\[My Mez Spell Name Here\].ID} \(Use /echo in front of ${Spell\[My Mez Spell Name Here\].ID} if your typing it in EQ\)

* **On Target acquisition**  

AutoBot acquires the Main Assist's \(MA\) target in a number of ways.

1\) By setting the MA in the bot's ini file and the assist delay, the macro will attempt to acquire the target of the MA after the set time.

2\) By using the Delegate Main Assist leadership AA, the bot will acquire the MA's target that way.

3\) By manually setting the MA's target using /varset MATarget ${Target.ID} in whatever channel your bots listen to commands in.

* **On non-working clickies**  

If you have a clicky with no recast timer that isn't working. \(Such as Time's Antithesis, Veil of Lost Hopes, et al...\) The odds are you have an old version of MQ2. As of the 20th of Dec Zip, these issues have been fixed. if you don't know what version of the zip you have, try simply running /echo ${FindItem\[item name\].Timer} and seeing what value it returns. Anything other than zero is Bad\(tm\) and denotes an out-of-date zip file. Update, update, update! Also your last inventory slot must NOT be a bag. Clickies usable from inventory, even if usable in other slots, will be used from base inventory slot 8.

* **On out-of-date alias lists**  

If you are attempting to reload your alias to your macroquest.ini. You must remove the Version=X.XX from RD\_common.ini. Doing this will make the Version mismatch appear and reload all the alias's

* **On healing not working**  
* **On heals that never cancel even though target's health goes above CancelPct**  

Tankheal must be defined as a valid spell and different than FastHeal=, even if you are not using Tankheals \(UseCH setting\).

* **On Green \(non-XP\) corpses that are not auto looted**  

These are not looted automatically. To trigger looting, at any time, send your bot "You gain party experience!" in whatever channel it is set to monitor.

* **On late/not reliable buffs**  

Bots will not buff in combat. Also it will not sit to memorize buffs if a NPC is within a certain range, although using a horse remedies this.

* **On non-refreshing buffs on bots themselves**  

Buffs from the \[DoBuffStuff\] or buff command are not rebuffed on the same bot that cast them, because you dont get a buff wear off message when they wear off yourself. If you want certain buffs kept up on your bot, you should use \[SelfBuffStuff\] section.

* **On bots that keep targeting some npc, even though it hasn't been told it to assist and kill it**  

Your MA could have a corpse close, and that is being assisted to get a target. Or you could be using an old version of autobot.

* **On non-following bots**  

Target someone and type /stick. If that doesnt work you have issues with [MQ2MoveUtils](https://macroquest2.com/phpBB3/viewtopic.php?t=11732).

* **On Clerics that spam Complete Heals and interrupt them all**  

Make sure you have UseDivArb set to 0 if you dont have that AA. // There's more to this than just the DivArb setting... but this might be one issue\

* **On non-attacking pets/bots**  

Check your MQ2Melee settings\(the wiki for it is [here](https://macroquest2.com/wiki/index.php/MQ2Melee)\). You need a properly configured MQ2Melee for your pets/bots to attack and do other various melee-related tasks.

* **On items being identified**  

You aren't using the IRC plugin. By default /i is mapped to /identify.

* **No slash commands work or error: "DoCommand - Couldn't parse '/...' "**

This usually happens when you update MQ2 and overwrite the macroquest.ini file. This file contains all the aliases \(ie. the slash commands\). To fix, delete the Version=X.XX line in RD\_Common.ini, which will write all the aliases back to the macroquest.ini file when you restart Autobot. In general, you do not need to overwrite the Macroquest.ini file when updating MQ2.

* **When your bot doesn't mem spells**  

Your ini is set up wrong. Your XXXXGem\#= entry needs to read "gem\#", not just \#. At least, 9 times out of 10 that's the problem. Check one of the sample ini files for an example.

* **On My bots dont aquire targets when everything is set up properly**  

Each toon needs a breastplate, it has to do with the way autobot checks deaths and runs the auto accept rez feature, it also disables assisting, for a good reason...

