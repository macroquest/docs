<h2>

<i>Command List Overview:</i>

</h2>

Presentation format for RH commands can be found in the section labeled "Command List." Command names and parameters are
capitalized for emphasis, but it should be noted that they are not case-sensitive. The format for each command is shown
below:

<hr>

<b>COMMAND</b>  
  
<i>Syntax:</i>  
`/COMMAND <parameters>|<or other parameters> [<optional parameter>] LITERAL`  
  
<i>Description:</i>  
Command description...  
  
<i>Examples:</i>  
Example usages...  

<hr>

  
Within the syntax descriptions, a vertical line (or pipe) -- "\|" indicates an either/or choice. Any parameters enclosed
within \< \> symbols indicates a user-supplied value. Any parameters enclosed in \[ \] symbols is optional. Any
parameter information not enclosed within \< \> should be considered a literal expression (that is you enter THAT text,
commonly this is the word "ON" or "OFF" in conjunction with various commands).  

<h2>

<i>Command List:</i>

</h2>

The following is a list of RH commands:  

<hr>

<b>ADDMASTER</b>  
  
<i>Syntax:</i>  
`/addmaster <name>`  
  
<i>Description:</i>  
This command adds a "master" (an authorized remote controller) given the supplied name to the master control list stored
within the RHSettings.INI file. Whenever a "master" sends a tell to the rogue running RH, and the tell starts with a "/"
character, RH will execute the entire line of the tell. A maximum of 20 masters can be stored; after the 20th master is
stored, you'll be forced to delete one before you can add another.  
  
<i>Examples:</i>  
Add a master named Hootey:  
`/addmaster Hootey`  
Send a tell (as the master) to the rogue named Pokey, having the rogue target Mary and hug her and kiss her:  
`/tell pokey /multiline ; /target Mary ; /hug ; /kiss`  
Send a tell (as the master) to the rogue named Dokey, having the rogue camp:  
`/tell dokey /camp`  

<hr>

<b>AUTOASSIST</b>  
  
<i>Syntax:</i>  
`/autoassist ON|OFF|<main assist> [<%health>]`  
  
<i>Description:</i>  
Allows you to activate or deactivate automatically assisting a PC or NPC, as well as setting the name of the PC or NPC
you wish to assist. The "% health" parameter is a value from 1 to 99 designating the percentage health that your target
must reach before you engage. The percentage health is an optional parameter that defaults to 98%  
  
<i>Examples:</i>  
Assist someone named "Mywarriorfriend" when his (and your) target has 97% health or less:  
`/autoassist Mywarriorfriend 97`  
Turn autoassisting on and off respectively:  
`/autoassist on`  
`/autoassist off`  

<hr>

<b>AUTOCHICKEN</b>  
  
<i>Syntax:</i>  
`/autochicken ON|OFF|<nimble%> [ESCAPE]`  
  
<i>Description:</i>  
Provides you with automatic self-preservation. When activated, RH will execute the nimble discipline (if you have it)
whenever your health percentage reaches the "nimble%" parameter. If the word "Escape" is optionally supplied, if nimble
is unavailable (due to being blown or not purchased), this feature will cease combat and use your escape AA skill.  
  
<i>Examples:</i>  
Activate autochicken and try to use nimble if your health is at 20% or lower and escape if nimble used/blown:  
`/autochicken 20 escape`  
Turn autochicken on with default (previous) values or turn it off, respectively:  
`/autochicken on`  
`/autochicken off`  

<hr>

<b>AUTODISC1</b>  
  
<i>Syntax:</i>  
`/autodisc1 ON|OFF|<"discipline name"> <end%> <reuse>`  
  
<i>Description:</i>  
Establish an optional discipline to employ while fighting. The specified discipline (enclosed within " " if it's more
than one word!) will be executed any time you have at least "end%" amount of endurance. You must also specify the reuse
time of the discipline (minutes) as this information is currently unknown to MQ2 for the original combat disciplines.  
  
<i>Examples:</i>  
Turn discipline #1 on, set it to employ the duelist discipline if it's ready and you have at least 40 endurance (and
specify that the re-use time on duelist is 30 minutes):  
`/autodisc1 Duelist 40 30`  
Turn discipline #1 on, set it to employ the deadly precision discipline if it's ready and you have at least 60 endurance
(and specify that the re-use time on deadly precision is 5 minutes):  
`/autodisc1 "Deadly Precision" 60 5`  
Turn off the disc1, but retain settings:  
`/autodisc1 off`  
Reactivate disc1 using existing settings:  
`/autodisc1 on`  

<hr>

<b>AUTODISC2</b>  
  
<i>Syntax:</i>  
`/autodisc2 ON|OFF|<"discipline name"> <end%> <reuse>`  
  
<i>Description:</i>  
Establish an optional discipline to employ while fighting. The specified discipline (enclosed within " " if it's more
than one word!) will be executed any time you have at least "end%" amount of endurance. You must also specify the reuse
time of the discipline (minutes) as this information is currently unknown to MQ2 for the original combat disciplines.  
  
<i>Examples:</i>  
Turn discipline #2 on, set it to employ the duelist discipline if it's ready and you have at least 40 endurance (and
specify that the re-use time on duelist is 30 minutes):  
`/autodisc2 Duelist 40 30`  
Turn discipline #2 on, set it to employ the deadly precision discipline if it's ready and you have at least 60 endurance
(and specify that the re-use time on deadly precision is 5 minutes):  
`/autodisc2 "Deadly Precision" 60 5`  
Turn off the disc, but retain settings:  
`/autodisc2 off`  
Reactivate disc using existing settings:  
`/autodisc2 on`  

<hr>

<b>AUTOEVADE</b>  
  
<i>Syntax:</i>  
`/autoevade`  
  
<i>Description:</i>  
Toggles automatic evade abilities while fighting on or off. If on, they'll be turned off (and vice versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>AUTOFOLLOW</b>  
  
<i>Syntax:</i>  
`/autofollow [<name>] [<distance>]`  
  
<i>Description:</i>  
This command will activate autofollowing, which will stay active until your target changes (to nothing, yourself, or
anything else). If an RH event is detected (such as a situation where autoassist is warranted, or looting, for example)
autofollow will be deactivated automatically and the interrupting activity will take place. You need not specify range
or target (it will use the current target if one isn't specified).  
  
<i>Examples:</i>  
Activate autofollow on Chichihooah and stay within 20 feet of her:  
`/autofollow chichihooah 20`  

<hr>

<b>AUTOHS</b>  
  
<i>Syntax:</i>  
`/autohs`  
  
<i>Description:</i>  
Toggles automatic hide and sneak abilities while not fighting on or off. If on, they'll be turned off (and vice
versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>AUTONINJA</b>  
  
<i>Syntax:</i>  
`/autoninja OFF|DROP|DROPABLE|ALL [<range>]`  
  
<i>Description:</i>  
This command will activate automatic NPC corpse looting whenever you are awarded experience. The first parameter can be
set to ALL (which will loot everything on a corpse), DROP or DROPABLE (which will only loot non-NODROP flagged items),
or OFF (which disables corpse looting). The optional range parameter determines how far away RH will "look" for a corpse
from your position at time of experience award (default is 50 feet).  
  
<i>Examples:</i>  
Turn on ninjalooting and get everything that drops (use default range):  
`/autoninja all`  
Turn on ninjalooting and get only tradable items; only seek corpses no farther than 20 feet away:  
`/autoninja drop 20`  
Turn off ninjalooting:  
`/autoninja off`  

<hr>

<b>AUTOPICK</b>  
  
<i>Syntax:</i>  
`/autopick`  
  
<i>Description:</i>  
Toggles automatic pickpocketing abilities while fighting on or off. If on, they'll be turned off (and vice versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>AUTOSTICK</b>  
  
<i>Syntax:</i>  
`/autostick`  
  
<i>Description:</i>  
Toggles automatic sticking to targets while fighting them. Autosticking implies staying behind the target as well,
unless obstructed by an object preventing you from getting behind it or while tanking. Do not confuse /autoassist and
/autostick--these are mutually exclusive features that may be used independently of each other.  
  
<i>Examples:</i>  
N/A  

<hr>

<b>AUTOTRAPS</b>  
  
<i>Syntax:</i>  
`/autotraps`  
  
<i>Description:</i>  
Toggles automatic trap negotiation while not in combat. This feature will look for both box and floor traps, and disarm
them when it finds one. If the feature is on, it will be turned off (and vice versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>CHANNEL</b>  
  
<i>Syntax:</i>  
`/channel <channel>`  
  
<i>Description:</i>  
With this command, you can control where RH directs it's output. Status information and general RH operations text will
go to whatever channel you set. In essence, whatever text you supply here is suffixed after a "/" and then output
strings are appended afterwards. "Echo" is the default channel. Creative users can use the IRC plugin and set the
channel to "I" to send RH output to an existing IRC channel.  
  
<i>Examples:</i>  
Redirect RH output to chat channel 1:  
`/channel 1`  
Redirect RH output to an irc channel (assuming you've loaded the MQ2IRC plugin and already joined a channel):  
`/channel i`  
Restore RH output to the MQ2 window (echo channel):  
`/channel echo`  

<hr>

<b>CLOSENESS</b>  
  
<i>Syntax:</i>  
`/closeness <%hitrange>`  
  
<i>Description:</i>  
With this command you can set the percentage of the maximum range used in order to reach your target while autosticking.
For some zones (Kael for example) the reported range is incorrect and too large--for such zones, set the closeness range
to a smaller value such as 20 or 30. For most zones, 70% is adequate.  
  
<i>Examples:</i>  
Set the closeness value to 30%:  
`/closeness 30`  

<hr>

<b>DRAG</b>  
  
<i>Syntax:</i>  
`/drag <body1> <body2> ... <bodyN>`  
  
<i>Description:</i>  
Drag corpses. You must supply one or more player names as parameters (unlimited). In order to stop dragging bodies,
target yourself (F1).  
  
<i>Examples:</i>  
Drag your friends Booger and Chooger:  
`/drag booger chooger`  

<hr>

<b>DYNAGGRO</b>  
  
<i>Syntax:</i>  
`/dynaggro`  
  
<i>Description:</i>  
Toggles whether or not RH should be responsible for the your rogue's aggression level (only meaningful if you're using
/autoassist). This feature will LOWER the percentage at which autoassist will fire by 1% if you were attacked during any
given fight. If you were not attacked on the most recent fight, it will RAISE the percentage at which autoassist will
fire by 1%. The assist percentage never stabilizes--it will always either go up or down after every fight. When using
this command, if the feature is on, it will be turned off (and vice versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>DYNCLOSE</b>  
  
<i>Syntax:</i>  
`/dynclose`  
  
<i>Description:</i>  
Toggles whether or not RH should be responsible for the temporary automatic adjustment of the closeness to target
(requires /autostick to be on). This feature will move you 20% closer to the target every two seconds, until you're in
swinging range. Original closeness value is restored when the current target is killed. When using this command, if the
feature is on, it will be turned off (and vice versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>ENDFLOOR</b>  
  
<i>Syntax:</i>  
`/endfloor <%endurance>`  
  
<i>Description:</i>  
With this command you can set the percentage of your endurance that is required in order for you to continue to initiate
a fight with the strike discipline. When your endurance drops below this percentage value, you'll only autoattack when
starting a fight.  
  
<i>Examples:</i>  
Set the strike endurance floor to 75%:  
`/endfloor 75`  

<hr>

<b>IBOUNCE</b>  
  
<i>Syntax:</i>  
`/ibounce <itemalias> <"Spell Name"&#62`  
  
<i>Description:</i>  
This command is part of a set of three commands used to manage clickable items and their effects. This particular
command allows you to set and store which spell effects do not stack with the spell effect created by a given clickable
item. You may store an unlimited number of spell effects that "bounce off" of a given clickable item's effect. When RH
maintains your clickable buffs, it will consult your existing buffs looking for these bounce spells prior to trying to
re-click the conflicting item. Enclose spell names in double quotes (" ")! The item in question must be aliased with the
/iset command prior to using this command.  
  
<i>Examples:</i>  
Set two bounce effects for an item aliased as simply "ring" (perhaps a Coldain's Hero Ring), particularly Shield of
Spikes and Shield of Thorns:  
`/ibounce ring "Shield of Spikes"`  
`/ibounce ring "Shield of Thorns"`  

<hr>

<b>ICLICK</b>  
  
<i>Syntax:</i>  
`/iclick <itemalias>`  
  
<i>Description:</i>  
This command is part of a set of three commands used to manage clickable items and their effects. This particular
command allows you to request RH to invoke the clickable effect for a given item. If you're not wearing the item, RH
will fetch it, click it, put it back in it's original container (in it's original spot) and close the container. The
item in question must be aliased with the /iset command prior to using this command.  
  
<i>Examples:</i>  
Have RH fetch the item aliased as "ring" (perhaps a Coldain's Hero Ring), and click it to invoke it's effect:  
`/iclick ring`  

<hr>

<b>ISET</b>  
  
<i>Syntax:</i>  
`/iset <itemalias> KEEPUP|NOKEEPUP <"Item Name">`  
  
<i>Description:</i>  
This command is part of a set of three commands used to manage clickable items and their effects. This particular
command allows you to set and store an item alias for a given clickable item. You also can specify whether or not you
want RH to automatically try to maintain the spell effect of this item. If a superior spell effect doesn't stack with
the item's effect, you should use the /ibounce command to specify said spells.  
  
<i>Examples:</i>  
Have RH alias "ring" for your Coldain's Hero Ring, and also indicate you wish RH to maintain the Shield of the Eighth,
if possible:  
`/iset ring keepup "Coldain Hero's Insignia Ring"`  

<hr>

<b>LEASH</b>  
  
<i>Syntax:</i>  
`/leash OFF|<distance> <master>`  
  
<i>Description:</i>  
With the leash command, you can dynamically create one of two types of leashes and tether yourself to it: a stake-bound
leash or a master-bound leash. If you specify just a distance and no master, /leash will drive a "stake" in the ground
at your current position, and return to this point after you finish a combat. If you specify both distance and a master,
after combats you'll return to the "master's" side, regardless of where the master is located. If you indicate OFF as a
parameter instead of a distance, leashing will be turned off.  
  
<i>Examples:</i>  
Create a 200 foot leash that is attached to a virtual stake:  
`/leash 200`  
Create a 250 foot leash that is attached to your warrior buddy named Booger:  
`/leash 250 booger`  
Turn all leashing off:  
`/leash off`  

<hr>

<b>LEASHFLEX</b>  
  
<i>Syntax:</i>  
`/leashflex <%length>`  
  
<i>Description:</i>  
With this command you can set the threshold of when RH considers you to be "close enough" to the stake or master to stop
moving toward it. If you set the leash flexibility very low (1), you'll return to the leash and nearly be on top of the
stake or master. If you set the leash flexibility very high (100), you'll never return to the stake or master, but you
won't go beyond your leash length when autosticking either.  
  
<i>Examples:</i>  
Set the leash flexibility to 50% of the leash's length:  
`/leashflex 50`  

<hr>

<b>LOOTMYCORPSE</b>  
  
<i>Syntax:</i>  
`/lootmycorpse`  
  
<i>Description:</i>  
With this command, you request RH to loot your entire corpse. Be warned that it's not aware of whether or not you've
received a resurrection yet or not! If you're body is too far away or lag is too intense, it will abort with an
appropriate failure message.  
  
<i>Examples:</i>  
N/A  

<hr>

<b>MAINASSIST</b>  
  
<i>Syntax:</i>  
`/mainassist <player>`  
  
<i>Description:</i>  
This command is part of a set of three commands used to designate who you should autoassist, assuming you've activated
the autoassist feature. This particular command sets the main assist (the main assist is also settable via /autoassist;
however using autoassist both sets the main assist AND turns autoassist on--this command will only set the main
assist).  
  
<i>Examples:</i>  
Make your buddy warrior "Booger" your main assist (but don't turn on autoassist):  
`/mainassist booger`  

<hr>

<b>PAUSE</b>  
  
<i>Syntax:</i>  
`/pause`  
  
<i>Description:</i>  
The pause command suspends all of RH's operations. Use this if you want to temporarily disable RH without unloading
it.  
  
<i>Examples:</i>  
N/A  

<hr>

<b>REMMASTER</b>  
  
<i>Syntax:</i>  
`/addmaster <name>`  
  
<i>Description:</i>  
This command removes a "master" (an authorized remote controller) given the supplied name from the master control list
stored within the RHSettings.INI file. It is a complimentary function to the ADDMASTER command.  
  
<i>Examples:</i>  
Remove the master named Hootey:  
`/remmaster Hootey`  

<hr>

<b>RHHELP</b>  
  
<i>Syntax:</i>  
`/rhhelp`  
  
<i>Description:</i>  
This command will give you a very terse list of all of RH's commands and their abbreviated syntax. It is NO substitute
for this manual!  
  
<i>Examples:</i>  
N/A  

<hr>

<b>SECONDASSIST</b>  
  
<i>Syntax:</i>  
`/secondassist <player>`  
  
<i>Description:</i>  
This command is part of a set of three commands used to designate who you should autoassist, assuming you've activated
the autoassist feature. This particular command sets the secondary assist. If the main assist dies, zones, or linkdies,
RH will cascade to the secondary assist as a backup and will reinstate the main assist whenever they're alive or
reconnect again.  
  
<i>Examples:</i>  
Make the dastardly shadowknight "Drevil" your secondary assist:  
`/secondassist drevil`  

<hr>

<b>STATUS</b>  
  
<i>Syntax:</i>  
`/status`  
  
<i>Description:</i>  
The status command will show you the current state of all of RH's relevant functions (ON or OFF as TRUE or FALSE) as
well as any user-defined values for those thresholds (endurance floors, stick distances, etc.)  
  
<i>Examples:</i>  
N/A  

<hr>

<b>STICKDIST</b>  
  
<i>Syntax:</i>  
`/stickdist <range_to_target> <range_to_tank>`  
  
<i>Description:</i>  
With this command, you can regulate how close you must be to both your current target or the main assist in order to
continue (or begin) autosticking to a given target. If you find yourself farther than the specified range to target or
you've wandered farther than the specified range to your tank/mainassist, you will stop sticking to the target. This
command is mostly useful to prevent you from chasing down runners when the main assist does not (or should not) as well
as not running after mobs that recently gated far, far away.  
  
<i>Examples:</i>  
Set the maximum distance you'll pursue a mob at to 50 feet and the maximum "wander" distance from the tank to 100
feet:  
`/stickdist 50 100`  

<hr>

<b>STOPFIGHT</b>  
  
<i>Syntax:</i>  
`/stopfight <%health>`  
  
<i>Description:</i>  
With this command, you can control when RH turns off autoattack. Whenever your health reaches the specified percentage
health parameter, RH will stop fighting.  
  
<i>Examples:</i>  
Cease combat when your health reaches 20% of it's maximum:  
`/stopfight 20`  

<hr>

<b>STRIKEDISC</b>  
  
<i>Syntax:</i>  
`/strikedisc <strikeskill>`  
  
<i>Description:</i>  
This command allows you to set your best available strike skill. The default skill is Assassin's Strike, but should you
be lower level or been lucky enough to obtain later strike discipline books, this is the command you use to set the
appropriate strike skill name. The name of the skill only has to be unique enough to differentiate it from other strike
skills (i.e. ancient, kyv, or assassin are all fine).  
  
<i>Examples:</i>  
Set the strike skill to be used to "Kyv's Strike":  
`/strikedisc kyv`  

<hr>

<b>TARGETSWITCH</b>  
  
<i>Syntax:</i>  
`/targetswitch`  
  
<i>Description:</i>  
Toggles whether or not RH should automatically choose a new target if the main assist does, or if it should "finish off"
the current target. If your main assist is also the puller, you may want target switching OFF, as it will be expected
that you finish off the last one before the next one is arrives. When using this command, if the feature is on, it will
be turned off (and vice versa).  
  
<i>Examples:</i>  
N/A  

<hr>

<b>THIRDASSIST</b>  
  
<i>Syntax:</i>  
`/thirdassist <player>`  
  
<i>Description:</i>  
This command is part of a set of three commands used to designate who you should autoassist, assuming you've activated
the autoassist feature. This particular command sets the tertiary assist. If the main assist and secondary assist die,
zone, or linkdie, RH will cascade to the tertiary assist as a backup's backup and will reinstate the main assist
whenever they're alive or reconnect again.  
  
<i>Examples:</i>  
Make your friendly paladin "Goodytwoshoes" your tertiary assist:  
`/thirdassist goodytwoshoes`  

<hr>

<b>VERBOSITY</b>  
  
<i>Syntax:</i>  
`/verbosity 0|1|2`  
  
<i>Description:</i>  
With this command, you determine the level of text output that RH generates. A verbosity level of '0' will only output
command switching information, but RH operational output will be almost completely silent. Verbosity level 1 shows all
major RH activity. Verbosity level 2 shows everything, including ancillary RH background operations. The default is 2.  
  
<i>Examples:</i>  
Make RH almost completely mute:  
`/verbosity 0`  
Have RH output all information possible:  
`/verbosity 2`  

<hr>

<b>WEAPONSWITCH</b>  
  
<i>Syntax:</i>  
`/weaponswitch OFF|<weapon1> <"switch text"> <weapon2>`  
  
<i>Description:</i>  
With this command, you can have RH automatically choose between two different weapons, depending on a settable
situation. At the end of a combat, RH will restore `weapon1` to your grasp. Whenever the supplied "switch text" is
encountered (usually this the proc message, be it personal buff or target debuff) the weapon will be swapped out for
`weapon2`. WEAPONSWITCH is also smart enough to determine if the weapon procs a buff (in which case you'd probably like
it to only switch back to `weapon1` when the proc'ed buff wears off rather than after you finish off the mob. It handles
this automatically. Make sure you do not typo the name of the weapons, or the switch text; also, the switch text does
not need to be complete, but should be as complete as possible to not accidentally swap weapons around if someone speaks
the trigger text. Weapons will be retrieved and deposited in any containers they come from (or on your character).
Alternately, you can specify OFF as the first parameter to stop weaponswitching.  
  
<i>Examples:</i>  
Use Locustlure as your default weapon, but switch to the Horn of Hsagra if Locustlure procs:  
`/weaponswitch Locustlure "yawns." "The Horn of Hsagra"`  
Use the Dart of Immobility as your default weapon, but switch to Ifir if your Dart procs:  
`/weaponswitch "Dart of Immobility" "screams as poison" "Ifir, Dagger of Fire"`  
Use a Primal Spear as your default weapon until you receive avatar, but switch to Ifir if your primal proc'ed and you
still have avatar:  
`/weaponswitch "Primal Velium Spear" "Your body screams" "Ifir, Dagger of Fire"`  
Turn off weaponswitching:  
`/weaponswitch OFF`


