## Syntax

**<span style="color:red">/varcalc</span> <span style="color:blue">varname</span> *formula***

## Description

-   Sets a variable directly to the numeric result of a calculation (*formula*)
-   Keep in mind that the type of the variable may itself reject this value depending on what you give it
-   **This will not work on strings!**

## Examples

    /varcalc MyInt 1+2*2+1
    /varcalc MyInt 1+(2*2)+1

    /varcalc MyInt ${MyInt}+6

## See Also

-   [MQ2DataVars](../documentation/mq2datavars.md) for further information on variables.

[Return to Slash Commands](../commands/slash-commands.md)

 
