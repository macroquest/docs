## Syntax

**<span style="color:red">/if</span> ( *formula* ) {**

  
***commands***

**} \[ <span style="color:blue">else</span> \[<span style="color:red">/if</span> (*formula*)\] { \]**

  
**...**

**}**

## Description

This will run all *commands* between the braces ( {} ) if *formula* evaluates to something other than 0.

-   *Formulas* are numeric operations ONLY. You must use MQ2Data string comparison to turn strings comparisons into
    numeric operations (eg. Using .Equal or .NotEqual).
-   You may use && and \|\| freely within *formula*, which will be evaluated down to a single term before proceeding.
-   Multiple *commands* may be included within the braces.
-   There is no need to use ${Math.Calc\[\]} in /if statements, since the formula is automatically converted into
    numeric operations.
-   *Else* and *else /if* can be used to further refine how/which *commands* are run.
-   This will not work on some older versions of MQ2 (IE Jan 25, 2004) You will get a "Failed to parse /if command"

## Examples

    /if (${Target.ID}) {
     /call Cast "Complete Healing" gem1
    }

    /if (${Target.ID}) {
     /echo I have a target
    } else {
     /echo No target
    }

    /if (${Target.CleanName.Equal[Banker Denton]}) {
     /echo Banker targeted
    } else /if (${Target.CleanName.Equal[Ward Toft]}) {
     /echo Ward targeted
    } else {
     /echo Banker or Ward not targeted
    }

[Return to Slash Commands](../commands/slash-commands.md)

 
