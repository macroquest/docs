# `#warning`

Add it at the top of your macro, and you will get warnings if there are undeclared variables used in it.

With `#warning` added to your macro, the macro will be issue a warning when it run in to an undefined, and pause.
The warning will list the macro line number and line language, so you can go in a fix the macro.

A common source of problems is using a variable that might not exist in an `if` statement to check if it has a value.

Instead, you can determine if a variable is defined by using the [Defined TLO](../top-level-objects/tlo-defined.md).

For example, the following is how you would check if a variable exists before being used.

```text
/if (${Defined[SomeVariable]} {
    /if (${SomeVariable})  {
        /echo SomeVariable exists.
    }
}
```
