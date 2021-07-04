## Syntax

**<span style="color:red">/substitute</span> <span style="color:blue">list</span>**  
**<span style="color:red">/substitute</span> \[ *<span style="color:blue">orig</span>*
<span style="color:blue">delete</span>\|*<span style="color:blue">new</span>* \]**

## Description

Allows you to create custom midline substitutions. They can be called from any alias or commandline by using the percent
sign (%).

-   Substitutions do not currently work in macros.
-   You don't use the percent signs when creating the substitutions or editing your config file.
-   You can use MQ's subsitutions without spaces around them (unlike EQ's!).
-   You can use EQ's wildcards (ie: %t) within your substitutions, however, you have to leave spaces around them (yes,
    they suck).
-   You cannot CURRENTLY replace EQ wildcards with MQ substitutions (eg. you can't make a replacement for %m).

## Example

    /substitute mom Mother
    /substitute omg Oh my god!
    /substitute k "%omg, kill %t before I tell your %mom"

  
If you typed "/say %k", it would produce:

    Oh my god!, kill targetname before I tell your Mother

[Return to Slash Commands](slash-commands.md)


