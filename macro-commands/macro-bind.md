## Description

<span style="color:red">#bind</span> Creates an ingame slash command that can be used to call the related sub routine
while the macro is running Instead of sending yourself a keyword to trigger a #event you can just type /saymana and it
will execute the function called "Sub Bind_SayMana"

## Use

-   **#bind_noparse** UpdateSomething /updatesomething
-   **#bind** SayMana /saymana

1.  bind gives a user a command they can use
2.  bind_noparse gives a user a command they can use that doesn't get parsed.

## Triggers On

Binds only get triggered / parsed on certain things, such as /invoke /varset /echo /call Sub. To trick binds to be
called often you can substitute your /doevents as a function like

    #bind TargetClosestNPC /near

    Sub Main
       /call Do_Events
    /return

    Sub Do_Events
       /doevents
    /return

    Sub Bind_TargetClosestNPC
        /echo Targeting the closest NPC becuase you typed /near
        /target ${NearestSpawn[npc]}
    /return

## Example

    #bind MyMana /MyMana

    Sub Main
     /declare CurMan int outer 0

     :loop
       /varset CurMan ${Me.CurrentMana}
       /doevents
       /delay 5
     /goto :loop
    /return

    Sub Bind_MyMana
      /call MyMana
    /return

    Sub MyMana
      /echo My Mana is ${CurMan}
    /return

## See Also

-   [Pound_Commands](pound-commands.md)
-   [Macro_Reference](../documentation/macro-reference.md)


