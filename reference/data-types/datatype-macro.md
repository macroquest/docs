---
tags:
    - datatype
---
# `macro`

<!--dt-desc-start-->
The Macro DataType deals with the macro currently running, and nothing else.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | string CurCommand
list the current line number, macro name, and code of the macro being processed
///

/// member | int CurLine
The current line number of the macro being processed
///

/// member | string CurSub
The current subroutine
///

/// member | bool isOuterVariable
true if the provided parameter is a defined outer variable
///

/// member | bool isTLO
true if the provided parameter an existing TLO
///

/// member | int MemUse
How much memory the macro is using
///

/// member | string Name
The name of the macro currently running
///

/// member | int Params
The number of parameters that were passed to the current subroutine
///

/// member | bool Paused
NULL if no macro running, FALSE if mqpause is off, TRUE if mqpause is on
///

/// member | string Return
The value that was returned by the last completed subroutine
///

/// member | int64 RunTime
How long the macro has been running (in seconds)
///

/// member | int StackSize
StackSize?
///

/// member | varies Variable
returns the value given the name of Macro variable. The type of this member depends on the type of the variable being accessed.
///
<!--dt-members-end-->

## Methods

| Method Name | Action |
| :--- | :--- |
| Undeclared | List all undeclared variables |
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
[varies]: ../../macros/variables.md
<!--dt-linkrefs-end-->
