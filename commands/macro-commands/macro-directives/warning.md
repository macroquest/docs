# \#warning

## Description

\#warning

Add it at the top of your macro, and you will get warnings if there are undeclared variables used in it.

AGAIN: IMPORTANT: Undeclared variables will slow down macro performance a LOT if they are used over and over, so, fix your macros.

## Use

With \#warning added to your macro, the macro will be issue a warning (either in the MQ window or chat window) when it run in to an undefined, and pause. The warning will list the macro line number and line language, so you can go in a fix the macro.

A lot of times this is a matter of using [\[TLO:Defined\|${Defined\[\]}\]]

As in ${blah} only gets defined in a specific situation... as such the old way of just

`/if (${blah}) /dosomething`

will cause a lot of extra CPU usage. Using \#warning will pause the macro and tell you where the problem is, so you can either change the macro to avoid the problem, or simply:

```text
/if (${Defined[${blah}]} {
    /if (${blah}) /dosomething
    }
```

## See Also

* [Pound\_Commands](./)
* [Macro\_Reference](../../../documentation/macro-reference.md)
* [TLO:Defined](../../../data-types-and-top-level-objects/top-level-objects/tlo-defined.md)

