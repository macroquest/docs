## General

We know that every macro must have a Main Subroutine (see [Macro Reference](../documentation/macro-reference.md)). However custom
Subroutines can be created as a way of re-using common code, and as a way of separating code into logical blocks or
routines.

Subroutines start with a Sub line and end with a /return line. When it hits the /return line, it will pass control back
to the calling Sub, at the point right after it was called.

When a subroutine is called, it runs all of the commands within it immediately.

Accessing your subroutine from the Main or other sub can be done with the [/call](call.md) command. Take the
following example:

`Sub Main`  
`  /call TestSub`  
`  /echo This is the main sub`  
`/return`  
  
`Sub TestSub`  
`  /echo This is a sub`  
`/return`

This will echo the following into the MQ2 Chat Window:

`This is a sub`  
`This is the main sub`

## Passed Parameters

All macros accept parameters passed to them when called. The parameters can be defined in the Sub line, or if not
defined, they are available through the Param0, Param1, Param2...ParamN local variables while in the sub. If you don't
define the types of variables, they will default to strings. The following two examples will both output the same thing:

`Sub Echo1(One,Two)`  
`  /echo ${One} ${Two}`  
`/return`

`Sub Echo2`  
`  /echo ${Param0} ${Param1}`  
`/return`

**Note:** Any parameters passed to the sub are automatically declared as local variables for that Sub (no need to
[/declare](../commands/declare.md) them).

## Return Values

A return value for the sub can be added after the [/return](return.md) command, and can be accessed through
${Macro.Return} by the calling macro. Take this example:

`Sub Add(int A, int B)`  
`  /declare Sum int local ${Math.Calc[${A}+${B}]}`  
`/return ${Sum}`

This will take the two passed variables (A and B), add them together and return the result. To use it, you'd need call
it like so:

`Sub Main`  
`  /call Add 10 12`  
`  /echo ${Macro.Return}`  
`/return`

This would echo "22" in the MQ2 Chat Window.

Return values can be used in Subs as well as Event Subrouties called by [/doevents](doevents.md).


