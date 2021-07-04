## Syntax

**<span style="color:red">/timed</span> <span style="color:blue">#</span> *command***

## Description

Executes *command* after a specified duration, given in deciseconds.  
  
**Notes**

-   This does not pause successive commands.
-   The first argument must be a literal integer (e.g. 2)
    -   It is not parsed for MQ2Data, so the following **will not work**

      
        /timed ${Math.Calc[1+1]} /echo This does not work

    -   An exception to this being the use of /docommand in combination with /timed

      
        /docommand /timed ${Math.Calc[1+1]} /echo This works

## Examples

    /timed 10 /echo 1 second has passed

[Return to Slash Commands](slash-commands.md)


