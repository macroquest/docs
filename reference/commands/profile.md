---
tags:
    - command
---
# /profile

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/profile <profile>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
This runs a macro just like [/mac](macro.md) does, but when the macro ends it will output a csv file of every subroutine that has been called, and how long it took. The file will be in Macros/profiles, named for the macro and the time it started.
<!--cmd-desc-end-->
## Settings

The output file contains one line per subroutine call, in the order they were called in. The columns are:


* **Command Count** - how many commands (lines) have been run from the start of the macro to now
* **Seconds Since Start** - how long the macro's been running
* **Stack Depth** - how many subroutines deep we are (Main is one, anything called from Main is 2, next call is 3, etc)
* **Subroutine** - Name of the sub
* **Subroutine (tabbed)** - Name of the sub, but with a few spaces for each increase in depth so it looks kinda tree like
* **Commands (inc Children)** - How many commands were executed by this sub and any subs it called
* **Commands (ex Children)** - How many commands were executed by just this subroutine, not including those executed by called subs
* **ms inc** - How long did this sub and its children take to run
* **ms ex** - How long did just this sub take to run, excluding time taken by its called subs
* **Called Children** - How many other subs were called by this sub (does not include subs called by children)
* **Return Value** - Value from /return if any
* **Arguments** - Arguments supplied to the sub, one per column

Goes nicely with a pivot table in excel.
