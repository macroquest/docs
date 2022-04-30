# Afcleric.mac - nils

## forum link

* [AFCleric.mac](https://macroquest.org/phpBB3/viewtopic.php?t=14508)

## nils downloads

* [AFCleric.mac - nils](http://members.shaw.ca/eqmq2/Macros/AFClericOct1707.zip)

## Required Plugins

* [MQ2Debuffs](https://macroquest.org/phpBB3/viewtopic.php?t=13495)
* [MQ2EQBC](https://macroquest.org/phpBB3/viewtopic.php?t=12147)
* [MQ2Exchange](https://macroquest.org/phpBB3/viewtopic.php?t=7603)
* [MQ2MoveUtils](https://macroquest.org/phpBB3/viewtopic.php?t=11732)

## Required Include Files

* [QuickBeg.inc](https://macroquest.org/phpBB3/viewtopic.php?t=12011)
* [Spell\_Routines.inc](https://macroquest.org/phpBB3/viewtopic.php?t=11656)
* [Wait4Rez.inc](https://macroquest.org/phpBB3/viewtopic.php?t=10119&highlight=wait4rez)
* Ninjadvloot.inc included with zip
* AFClericCCH.inc included with zip

## Previous Versions

* [Original AFCleric by Fantum409](https://macroquest.org/phpBB3/viewtopic.php?t=7567&highlight=afcleric)
* [AFCleric by DigitalMocking Jan.2005](https://macroquest.org/phpBB3/viewtopic.php?t=11779)

## Updates

Updated:

* Added aura support for a single aura.
* Added hammer routine.
* Apr.19/07
* Spell section in the ini file now requires Gem\#, item or alt for all gems except YaulpSpellGem and NukeOneGem, will

  change them in the next update. You will need to make the change to your ini file.

* Added looting, not tested but should work. Ini entry is useAutoLoot=TRUE/FALSE. Alias is /autoloot. I will put a

  link to the \*Ninjadvloot thread later for those not familiar with it and it's ini file.

* Added anchor support, resets automatically when you get the followstop command. /anchor
* Added 3 commands to the chat event, gheal, hot me and patch me, if you had them in the buff section you should take

  them out now.

* Removed the Resplendent Cure code, just use the CureStuff section in the ini now and you will need to be running

  MQ2Debuffs plugin. I set up the sample ini's CureStuff section to work a little better.

* Updated for Stacks change and updated for the newest QuickBeg
* Cleaned up a lot of /if statements, lots left to do yet. Most likely other changes that I don't remember and this

  version is not fully tested so let me know if I screwed something up.

* May 21/07
* Not sure what all I have done to this since it's last update but here is what I remember.
* UseWard should now work with named mobs, it should activate the Fervent Benediction and higher AA's.
* You should stand up after being hit with an FD spell.
* I changed the DoBuff routine so hopefully if asked for a group spell by more than one it should only cast it once.

  It is on a 2 minute timer before the next check for that spell, also resets if a different group spell is requested

  in that 2 minutes. It is not a great system but has helped so far by not looking as obvious by casting a group spell

  on the same group 2 or 3 times in a row.

* I changed the follow routine to use uw if you are underwater. If you zone into a water zone while following it will

  switch automatically but if following on land and then into water you will need to re-issue the follow command

* I was experimenting with Promised Renewal, the routine is still there and is hard coded to use gem8. I am not sure

  yet if I should just use the spell in place of complete healing or change my routine so it works better with it.

* Some new commands are:
* pop infusion will activate Infusion of the Faithful AA
* clickzone will click the nearest zone door book or whatever
* sayzone  will target senders target and say the zone text

example: /bc sayzone wish to go will target senders target and say wish to go

(bugged, tank's target is temporary fix)

## Commands

* /anchor /echo Setting Anchor
* /autoloot /echo ToggleVar Auto Looting,useAutoLoot,Settings,useAutoLoot,
* /automok /echo ToggleVar Auto MoK,UseAutoMok,Settings,UseAutoMok,
* /automount /echo Toggling AutoMount
* /autostun /echo ToggleVar Auto Stun,UseAutoStun,Settings,UseAutoStun,
* /buffbeg /echo ToggleVar Buff Begging,BegForBuffs,Settings,BegForBuffs,
* /buffradius /echo ToggleString Setting NPC Buff Radius,NPCBuffRadius,Settings,NPCBuffRadius,
* /casterhot /echo ToggleString Setting Caster Hot Pct,CasterHotPoint,Heal\_Percentages,CasterHotPoint,
* /casterpatch /echo ToggleString Setting Caster Patch Pct,CasterPatchPoint,Heal\_Percentages,CasterPatchPoint,
* /dacast /echo ToggleString Setting DA Cast Point,DaCastPoint,Heal\_Percentages,DaCastPoint,
* /defaultmt /echo ToggleString Setting Default MT,DefaultMT,Settings,DefaultMT,
* /doraidbuffs /echo ToggleVar Setting Raid Buffing,DoRaidBuffs,RaidBuffs,DoRaidBuffs,
* /divarb /echo ToggleString Setting Divine Arbitration Cast Point,DivArbPoint,Heal\_Percentages,DivArbPoint,
* /dobufftells /echo ToggleVar Do Buff Tells,DoBuffTells,DoBuffStuff,DoBuffTells,
* /docures /echo ToggleVar Auto Curing,DoCures,CureStuff,DoCures,
* /donukes /echo ToggleVar Using Nukes,DoNuke,NukeStuff,DoNuke,
* /meleemode /echo ToggleVar Melee Mode,MeleeMode,Settings,MeleeMode,
* /necshmpatch /echo ToggleString Setting Nec Shm Patch Pct,NecShmPatchPoint,Heal\_Percentages,NecShmPatchPoint,
* /nukeat /echo ToggleString Setting Nuke At,NukeAt,NukeStuff,NukeAt,
* /nukedelay /echo ToggleString Setting Nuke Delay,NukeDelay,NukeStuff,NukeDelay,
* /pethealpct /echo ToggleString Setting Pet Heal Pct,PetHealPoint,Pet\_Settings,PetHealPoint,
* /useaura /echo ToggleVar Setting use aura,UseAura,SelfBuffStuff,UseAura,
* /useda /echo ToggleVar Setting use DA,UseDA,DAStuff,UseDA,
* /usehammer /echo ToggleVar Using Hammer,UseHammer,Settings,UseHammer,
* /usehot /echo ToggleVar Using HoT,UseHot,Settings,UseHot,
* /userenewal /echo ToggleVar Use Promised Renewal,UseRenewal,Settings,UseRenewal
* /useyaulp /echo Toggling UseYaulp
* /useward /echo ToggleVar Use Ward,UseWard,Settings,UseWard
* /secondtank /echo ToggleString Setting Second Tank,SecondTank,Settings,SecondTank,
* /selfhealpct /echo ToggleString Setting Self Heal Pct,SelfHealPoint,Heal\_Percentages,SelfHealPoint,
* /tankhealpct /echo ToggleString Setting Tank Heal Pct,TankHealPoint,Heal\_Percentages,TankHealPoint,
* /toggletank /echo Setting new main tank to:
* /turnundead /echo ToggleVar Setting Turn Undead,TurnUndead,Settings,TurnUndead,
* /healspell /echo ToggleString Setting Heal Spell,HealSpell,Spells,HealSpell,
* undeadskin - cast Sunskin
* gheal - cast groupheal
* hot me - cast hotspell
* patch me - cast patchheal
* invisoff - click off inviso buff
* pop infusion - cast infusion AA
* foeoff - click off Flight of Eeagles
* follow - start following toon that issued the command - toon has to be on master list
* follow stop - stop following a toon
* clickzone - click nearest zoneline (book, zonedoor, etc.) - has to be within distance of 12
* sayzone - will target requestor's target and echo the following text sent with the command - currently uses tank's

  target (bugged, tank's target is temporary fix)

* mana check - report mana percent in channel
* slowcamp - sits and camps to desktop (fails if toon is on a mount)
* rezz me - will target and attempt to rezz the requestor's corpse, will use epic if available
* leaveraid - will disband you from a raid

## FAQ

* You can do /bc wod sym spell haste and it should cast them all in that order, usefull after rezzes and to do /bc mgb

  groupsym, can also be used this way to give more than one toon a command at the same time /bc focus symbolme p10 wod

* sayzone and clickzone

this works nice now although I have not tried clickzone on every type of zone there is I did try a lot and it never failed. You will find a new entry in your ini files usually in the first section called ZoneDelay, this delay is for sayzone so that your whole grope doesn't /say all at the same time. You will want the person who initializes the command to have the longest delay, here is how I have mine set up

Warrior 1 Cleric 10 Shaman 20 Druid 30 Enchanter 40 Ranger 50

So the warrior would say the text first, 1 second later the cleric would and every second after that another would until 5 seconds after giving the command my ranger would finaly say it.

* Nuking is automatic and the frequency depends on the NukeDelay that you set in the ini \(can be changed on the fly

  with /nukedelay \#\). Look for the NukeStuff section in your ini. Also if you look at Sub Nuke there is a line that

  will return out of that sub when your tanks hp's are below 80% and as stated earlier in this thread you can lower

  that if you feel comfortable nuking at less than that

* The conditions for the macro to give the /sit command are: AutoSit has to be true, your mana % has to be less than

  what you have SitAt set to, your not on a mount, your not casting, you don't have your yaulp buff on, you don't have

  your divine avatar buff on, you are standing, the nearest NPC is farther away than you have DistanceToSit set at,

  your hit points are greater than 80% and you are not following. If any one of those conditions are not met the macro

  will not do the /sit.

The only other times /sit is used is right after a rezz and that should keep you sitting until you have 500 mana. The other time is if you give the slowcamp command.

* The Moked event works perfectly. It does have some strict conditions, first you need to have the spell memmed and it

  has to be ready to cast, second your tank needs to be 90% or higher hps and third the mob has to be above 75% not to

  mention the macro has to be free to run the event and not in another function like healing someone in the group or

  whatever and your cleric needs to be able to see the DS spam. If all those conditions are true it will work every

  time. If you want to change the conditions edit Sub Event\_DamageShield but it has worked for me the way it is for

  almost 2 years.

* The mob you are fighting has to have a DS in order to for Sub Event\_DamageShield to be triggered, here are the 3 trigger lines
* event DamageShield "\#1\# was burned\#\*\#"
* event DamageShield "\#1\# was pierced by\#\*\#"
* event DamageShield "\#1\# was tormented\#\*\#"
* can I use \| to set up multiple tanks to watch?

It will only watch 1 tank the way it is set up and the tank doesn't need to be in your group. It would be able to watch 1 tank out of it's group and would also try to heal any in it's group in modes 2 and 3 and if they are a war, shd or pal it would try to use HealSpell first. The only other way would be for the other tanks to ask for a heal when they needed it, you could do that as a buff request or add another entry to the chat event for HealSpell but it may not be that reliable

* subroutine MedTime gets called if your mana is 98% or less

