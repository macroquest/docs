# Snare

Macro to automatically snare target

Works by: Checks to see if target has been snared since based upon if it is an NPC, % of health and checking the variable. When any mob dies, it resets the variable and only when a mob dies (or it wears off, which is extremely rare).

```text
#include spell_routines.inc

#Event EnsnareWornOff "#*#ensnare spell has worn off#*#" 
#Event Exp "#*#party experience!#*#" 
#Event Exp "#*#gain experience!#*#"
#Event Exp "#*#slain#*#"


Sub Main
    /echo 1...
    /declare Ensnared bool outer FALSE
    :loop
    |Snare check
    |/assist <<<<tank name>>>>
    /if (${Target.ID} && ${Target.PctHPs}<99 && !${Ensnared}) /call Ensnare 
    /doevents
    /delay 1s
    /goto :loop
/return

Sub Ensnare
    /call Cast "Ensnare" gem3 10s
    /if (${Macro.Return.Equal[CAST_SUCCESS]} || ${Macro.Return.Equal[CAST_IMMUNE]}) /varset Ensnared TRUE 
/return

Sub Event_Exp 
   /varset Ensnared FALSE 
/return 

Sub Event_EnsnareWornOff 
   /varset Ensnared FALSE 
/return
```

