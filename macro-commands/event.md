## Description

event is used to specify strings to be triggered after you do /doevents

## Tutorial

<http://www.macroquest2.com/phpBB3/viewtopic.php?f=47&t=20199>

### Tutorial Macro

    #event stuff "[MQ2] Ant Bat Cat Dog Emu"
    #event stuff "[MQ2] Ant #*# Cat"
    #event stuff "[MQ2] |${Me.Name}| is cool"
    #event stuff "[MQ2] eqmule is #1#"

    sub main
       /echo starting ${Macro.Name}
       :loop
          /delay 1s
          /doevents
       /goto :loop
    /return

    sub event_stuff(Line, word1, word2, word3, word4)
       /echo ${word1}, ${word2}
    /return

### Triggering your sub event_stuff

This code will watch EQ chat for an exact message of "\[MQ2\] Ant Bat Cat Dog Emu" when /doevents is called it will
trigger the sub event_stuff.

/doevents will process all your events since the last time it was done If the event happened 5 times since the last
/doevents then it will execute your sub 5 times

It needs to be exact, nothing in front or behind of your string. If you received a tell it would not trigger but if you
see it as an /echo (because /echo shows \[MQ2\] as first word in chat) then it will trigger

### Multiple events calling same sub

You can have multiple triggers if you use the same event_name with different strings it will trigger. Because everything
in the example is #event stuff it will trigger the sub each time it sees it

### Using wildcard

You can use wildcards via #\*#

`#event stuff "[MQ2] Ant #*# Cat" `

This would trigger with **/echo Ant Bird Cat**

**/echo Ant Bird Cat Dog** Would not trigger because there is no wildcard after Cat

`#event stuff "[MQ2] Ant #*# Cat #*#" `

This would trigger for **/echo Ant Bird Cat** and **/echo Ant Bird Cat Dog**

### Using parsed datatypes

In the string for event_name you can use datatypes with \|${DataType}\|

`#event stuff "[MQ2] |${Me.Name}| is cool" `

Assuming your in game name is LamahHerder... This would call sub event_stuff if **/echo LamahHerder is cool**

### Passing a variable

In the string for event_name you can use #int# to pass a variable to the event_name sub

    #event stuff "[MQ2] #1# the mq2 dev is #2#"

    sub event_stuff(Line, word1, word2, word3, word4)
       /echo ${word1}, ${word2}
    /return

For **/echo eqmule the mq2 dev is awesome**

This would have ${word1}=eqmule and ${word2}=awesome as a local string variable in sub event_stuff

## Example Macro with Known Hit Messages

-   <http://www.macroquest2.com/phpBB3/viewtopic.php?f=47&t=20198&p=173345#p173345>

<!-- -->

    | hitsmode Normal
    #Event hitSuccess         "You backstab #1# for #2# #*# of damage."
    #Event hitSuccess         "You bash #1# for #2# #*# of damage."
    #Event hitSuccess         "You bite #1# for #2# #*# of damage."
    #Event hitSuccess         "You claw #1# for #2# #*# of damage."
    #Event hitSuccess         "You crush #1# for #2# #*# of damage."
    #Event hitSuccess         "You frenzy on #1# for #2# #*# of damage."
    #Event hitSuccess         "You gore #1# for #2# #*# of damage."
    #Event hitSuccess         "You hit #1# for #2# #*# of damage."
    #Event hitSuccess         "You kick #1# for #2# #*# of damage."
    #Event hitSuccess         "You maul #1# for #2# #*# of damage."
    #Event hitSuccess         "You pierce #1# for #2# #*# of damage."
    #Event hitSuccess         "You punch #1# for #2# #*# of damage."
    #Event hitSuccess         "You rend #1# for #2# #*# of damage."
    #Event hitSuccess         "You shoot #1# for #2# #*# of damage."
    #Event hitSuccess         "You slash #1# for #2# #*# of damage."
    #Event hitSuccess         "You slice #1# for #2# #*# of damage."
    #Event hitSuccess         "You smash #1# for #2# #*# of damage."
    #Event hitSuccess         "You stab #1# for #2# #*# of damage."
    #Event hitSuccess         "You sting #1# for #2# #*# of damage."
    #Event hitSuccess         "You strike #1# for #2# #*# of damage."
    #Event hitSuccess         "You sweep #1# for #2# #*# of damage."

    | hitsmode Abbreviated
    #Event hitSuccess         "backstab #1# for #2# #*# of damage."
    #Event hitSuccess         "bash #1# for #2# #*# of damage."
    #Event hitSuccess         "bite #1# for #2# #*# of damage."
    #Event hitSuccess         "claw #1# for #2# #*# of damage."
    #Event hitSuccess         "crush #1# for #2# #*# of damage."
    #Event hitSuccess         "frenzy on #1# for #2# #*# of damage."
    #Event hitSuccess         "gore #1# for #2# #*# of damage."
    #Event hitSuccess         "hit #1# for #2# #*# of damage."
    #Event hitSuccess         "kick #1# for #2# #*# of damage."
    #Event hitSuccess         "maul #1# for #2# #*# of damage."
    #Event hitSuccess         "pierce #1# for #2# #*# of damage."
    #Event hitSuccess         "punch #1# for #2# #*# of damage."
    #Event hitSuccess         "rend #1# for #2# #*# of damage."
    #Event hitSuccess         "shoot #1# for #2# #*# of damage."
    #Event hitSuccess         "slash #1# for #2# #*# of damage."
    #Event hitSuccess         "slice #1# for #2# #*# of damage."
    #Event hitSuccess         "smash #1# for #2# #*# of damage."
    #Event hitSuccess         "stab #1# for #2# #*# of damage."
    #Event hitSuccess         "sting #1# for #2# #*# of damage."
    #Event hitSuccess         "strike #1# for #2# #*# of damage."
    #Event hitSuccess         "sweep #1# for #2# #*# of damage."

    | Spells and Procs
    #Event hitSuccess         "#1# has taken #2# damage from your #3#."
    #Event hitSuccess         "#1# was hit by non-melee for #2# #*# of damage."
    #Event hitSuccess         "|${Me}| hit #1# for #2# #*# of non-melee damage."

    | Pet hit's
    #Event hitSuccess         "|${Me.Pet.CleanName}| backstabs #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| bashes #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| bites #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| claws #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| crushes #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| frenzies on #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| gores #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| hit #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| hits #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| kicks #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| mauls #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| pierces #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| punches #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| rends #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| shoots #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| slashes #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| slices #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| smashes #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| stabs #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| stings #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| strikes #1# for #2# #*# of damage."
    #Event hitSuccess         "|${Me.Pet.CleanName}| sweeps #1# for #2# #*# of damage."

    Sub Main
        /echo This Macro loops and triggers an event with an /echo when you hit something!
        
        :loop
            /doevents
            /delay 10
        /goto :loop
        
    /return

    Sub Event_hitSuccess(Line, hitTarget, hitDMG, hitType)
        /echo [${hitTarget}] - [${hitDMG}] - [${hitType}]
        /doevents flush
        /delay 10
    /return

## See Also

-   [Pound_Commands](pound-commands.md)
-   [Custom_Events](../macros/custom-events.md)
-   [Macro_Reference](../documentation/macro-reference.md)


