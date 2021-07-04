## Syntax

**<span style="color:red">/caption</span> <span style="color:blue">list</span> \| <span style="color:blue">type</span>
*value* \| <span style="color:blue">update</span> # \| <span style="color:blue">MQCaptions</span> \[ on \| off \]**

## Description

Sets the custom captions from in-game. Using this command will also change the ini settings for the particular level.

EQ itself constantly updates the name of every spawn in the zone, even though only a small portion of those are
displayed. Using /caption allows you to modify how many spawn captions updated. The default setting for /caption update
is 35.

Player1 through Player4 in MacroQuest.ini are directly related to which /shownames level you use.

    Player1 is linked to /shownames 1
    Player2 is linked to /shownames 2
    Player3 is linked to /shownames 3
    Player4 is linked to /shownames 4

## Examples

    Player1=${If[${NamingSpawn.Trader},Trader,]}${If[${NamingSpawn.Invis},(${NamingSpawn.DisplayName})

-   Use "\\n" to add a new line when setting captions
-   To use the default (EQ settings) clear the specific setting(Player1-Player4) in the ini using:
      
        /caption Player1
-   You can also configure Player1 - Player4 from the EQ client using:
      
        /caption Player# configsettings

  
\*Sets the number of nearest spawns for MQ2 to update the name of each pass to 20. By default, this is 35.

\*:

    /caption update 20

  
\*When using MQCaption if no parameter is given, the default parameter is off

-   Look at the Macroquest.ini file in the zip file under \[Captions\] for examples of configuring Player1-Player4.

## See Also

-   [NamingSpawn](../documentation/namingspawn.md)
-   [MacroQuest.ini](../macroquest.ini.md)

[Return to Slash Commands](slash-commands.md)


