---
tags:
    - command
---
# /if

## Syntax

```eqcommand
/if ( <formula> ) {
<commands>
} [ else [/if ( <formula> ) ] {
<...>
} ]
```

## Description

This will run all _commands_ between the braces ( {} ) if _formula_ evaluates to something other than 0.

* _Formulas_ are numeric operations ONLY. You must use MQ2Data string comparison to turn strings comparisons into

  numeric operations (eg. Using .Equal or .NotEqual).

* You may use && and \|\| freely within _formula_, which will be evaluated down to a single term before proceeding.
* Multiple _commands_ may be included within the braces.
* There is no need to use ${Math.Calc[]} in /if statements, since the formula is automatically converted into

  numeric operations.

* _Else_ and _else /if_ can be used to further refine how/which _commands_ are run.
* This will not work on some older versions of MQ2 (IE Jan 25, 2004) You will get a "Failed to parse /if command"

## Examples

```text
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
```

[Return to Slash Commands](..//)

