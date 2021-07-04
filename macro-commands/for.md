## Syntax

**<span style="color:red">/for</span> *varname* #1
<span style="color:blue">to</span>\|<span style="color:blue">downto</span> #2 \[<span style="color:blue">step</span>
#3\]**

  
**...**

**<span style="color:red">/next</span> *varname***

## Description

This runs all commands between the /for line and the /next line, after which it increments/decrements the *varname*
number (#1) by *step* number (#3) (default is 1) before running through the commands again. It will keep doing this
until the *varname* number equals #2. You can end a /for loop immediately with /break or try the next iteration with
/continue.

## Examples

**Simplest**

    /declare varname int local
    /for varname 1 to 5
        /echo ${varname}
    /next varname


    | Will output:
    |  1
    |  2
    |  3
    |  4
    |  5

**Using /continue**

    /declare varname int local
    /for varname 1 to 5
       /if ({$varname} == 3) /continue
       /echo ${varname}
    /next varname


    | Will output:
    |  1
    |  2
    |  4
    |  5

**Using /break**

    /declare varname int local
    /for varname 1 to 5
        /if (${varname} == 3) /break
        /echo ${varname}
    /next varname


    | Will output:
    |  1
    |  2

**With a pre-defined ending variable**

    /declare foo int local 5

    /declare varname int local
    /for varname 1 ${foo}
      /echo ${varname}
    /next varname

    | Will output:
    |  1
    |  2
    |  3
    |  4
    |  5

## See also

-   [/next](next.md)
-   [/while](while.md)
-   [/break](break.md)
-   [/continue](continue.md)
-   [Macro_Reference](../documentation/macro-reference.md)
-   [Slash Commands](../commands/slash-commands.md)

 
