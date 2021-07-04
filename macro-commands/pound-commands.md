## Definition

Pound commands are pre-execution commands that are not run during the macro. These commands will be run before the Main
sub is run, and are traditionally located at the beginning of the macro file.

Click on the list below to see more in-depth descriptions.

-   [bind](macro-bind.md)
-   [chat](chat.md)
-   [define](define.md)
-   [event](event.md)
-   [include](include.md)
-   [turbo](turbo.md)
-   [warning](warning.md)

## example

    #warning

    #include Ninjadvloot.inc
    #include Spell_Routines.inc
    #include Defense.inc

    #turbo 80

    #CHAT BC
    #CHAT RAIDSAY
    #CHAT GROUPSAY

    #Event AddCombatSong    "[MQ2] AddCombatSong #1#"
    #Event Experience       "#*#You gain party experience#*#"
    #Event AddAlertCommon   "[MQ2] AddAlertCommon #1#"
    #Event WornOff          "#*#Your #1# spell has worn off of #2#."


