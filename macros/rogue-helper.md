<h1>

Rogue Helper v6.0 Documentation

</h1>

RH.mac was originally designed to take some button mashing out of playing a rogue while raiding. This macro will execute
"smart" backstabbing, constant evading (optionally), auto hiding and sneaking while not fighting, automatically avoid
enrage riposte damage, stop fighting if you get below a certain health percentage, employ your chosen Strike discipline
before wading into combat, and was later expanded to include a vast amount of other features.  
  
The latest versions of RH will also automatically assist specified tanks in a cascading fashion, automatically stick to
a target (via internal code or using the MoveUtils plugin, smartly), will strafe in the most logical direction, display
experience totals after combat, and optionally return after combat to a specified stake (or anchor) point.  
  
In addition to various combat abilities (along with their tunable parameters), RH also provides some rogue tools:
multiple body dragging, self corpse looting, as well as a fully customizable item clicker (with the capability to
automatically refresh self-clicked buffs), and automatic looting.  
  
A full list of features, their command syntax, and examples of how to use those commands is provided alphabetically
below.

<h2>

<i>Important Notice:</i>

</h2>

RH will <i><b>not function correctly</b></i>, particularly in combat and more specifically with strike execution, unless
you do the following things before using the macro:

1.  Make sure you have autoattack on assist OFF (/assist off)
2.  Modify your HOTKEY assist button to be ONLY an assist command and the following line:  
      
    `/echo Seeking a Victim...`  
      
    In other words, make a hotkey with the following two lines:  
      
    `/assist main`  
    `/echo Seeking a Victim...`  
      

If you fail to do these things, RH will function poorly!

If your rogue still fails to assist your tank, try /Stick Off

<h2>

<i>Features:</i>

</h2>

RH provides you, the rogue, with an enormous amount of power. RH can do just about anything a rogue would need to do and
can do almost all of it automatically. The following section briefly lists the features and capabilities that RH
provides.

-   Backstab while autoattack is on.
-   Evade (optional) whenever hide is available during combat.
-   Hide and sneak (optional) while not fighting.
-   Pick the pockets of your enemies while fighting.
-   Avoid riposte damage by disabling autoattack whenever enrage is detected and you're facing the target (if autoassist
    is on, autoattack is turned back on after the enrage wears off).
-   Cease fighting when the rogue's health drops below a certain point.
-   Open combats with a strike discipline (if hiding and sneaking and sufficient endurance is available).
-   Automatically stick (maneuver behind) engaged targets in a VERY human-like way.
    -   You can specify how near you stick to the mob as a percentage of the maximum range to hit the target.
    -   You will "circle strafe" around targets in the smallest arc to find the target's rear.
    -   RH will try to back up and randomly move around obstacles if it gets stuck.
    -   If you suddenly find yourself tanking, sticking will be disabled to prevent you from dancing around the target
        indefinitely.
    -   Sticking will automatically take advantage of the MQ2MoveUtils plugin if it's loaded.
-   Experience changes in regular, AA, and Group Leadership are reported as a percentage delta (change) after every
    experience gain.
-   Create a virtual leash for your rogue and attach it to an NPC or player or to a virtual stake in the ground.
    -   You can customize the length of the leash.
    -   If your (or RH) tries to move you beyond the leash length, you will be yanked back to the maximum length.
    -   When not fighting, you'll return to the stake or the leash holder.
-   Automatically assist another player and make ready to strike or auto attack when the target reaches a certain health
    percentage.
    -   Up to three (3) assists can be specified..
    -   RH will cycle through all three assists, trying to assist each and stop when it finds that one of them is
        targeting an NPC.
    -   You can specify "main" as the first or main assist, and RH will follow raid-set main assists instead.
    -   Aggression level can optionally be controlled by RH (how soon to assist).
    -   RH can stay on an existing target until it's dead, or optionally engage a new target if the main assist chooses
        one.
-   Drag an unlimited number of corpses (command line driven).
-   Completely loot your own corpse.
-   Automatically click items.
    -   You can define clickable items and use a command to have RH "fetch" them, use them, and put them back.
    -   Specified clickable effects can be designated as persistent (KEEPUP), and RH will automatically find the item
        and activate it's effect when the previously employed effect wears off.
    -   You can define which spells don't stack with your clickable items to prevent persistent effects from bouncing
        off of superior spells.
-   Ninjaloot any NPC corpses that are around you (after something dies).
-   Automatically scan and disarm traps.
-   Improved autofollow (far better than EQ's) which actually allows you to follow players in dungeons or follow NPCs,
    all at a specified range.
-   Conditionally swap weapons after a specified proc-effect occurs in combat, be it a player buff or a detrimental
    target debuff.
-   Fight in 3D-mode while swimming (target acquisition while underwater is inhumanly perfect).
-   Determine when to take evasive action, including nimble discipline and potentially escape.
-   Automatically employ two configurable disciplines of your choice (duelist, deadly precision, kinesthetics, etc.)
-   Completely control macro output, both where it's displayed and the volume of text generated.

  

<h2>

[Rogue Helper Command List](https://macroquest2.com/wiki/index.php/Rogue_Helper_Command_List)

</h2>


