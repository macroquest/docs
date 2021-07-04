## Syntax

**<span style="color:red">/vardata</span> <span style="color:blue">varname</span> *newMQ2Datavalue***

## Description

Sets a variable directly to the end result of a MQ2Data string.  
\*To use this, **do not** put ${} around the outer data to parse.

-   This is more efficient than using */varset* as it skips a step
    -   */varset* first converts the MQ2Data to text, and then back to MQ2Data
    -   */vardata* converts directly through MQ2Data

## Examples

    /vardata MyFloat Math.Calc[${Me.X}+${Me.Y}]

    /vardata M_Assist Param0

    | using /vardata with non-basic data types

    /declare x int local
    /declare xSpawn spawn local
    /for x 1 to ${SpawnCount[pc]}
       /vardata xSpawn NearestSpawn[${x},pc]
       /echo ID:${xSpawn.ID} NAME:${xSpawn.Name}
    /next x

## See Also

-   [MQ2Data](../documentation/mq2data.md)
-   [/varset](varset.md)
-   [/varcalc](varcalc.md)

[Return to Slash Commands](../commands/slash-commands.md)

 
