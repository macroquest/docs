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

See this page "[For](for.md) " for additional information

## See Also

-   [For](for.md)
-   [Macro_Reference](../documentation/macro-reference.md)
-   [Slash Commands](../commands/slash-commands.md)

 
