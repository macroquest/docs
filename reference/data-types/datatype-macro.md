---
tags:
    - datatype
---
# `macro`

The Macro DataType deals with the macro currently running, and nothing else.

## Members

### {{ renderMember(type='string', name='CurCommand') }}

:   list the current line number, macro name, and code of the macro being processed

### {{ renderMember(type='int', name='CurLine') }}

:   The current line number of the macro being processed

### {{ renderMember(type='string', name='CurSub') }}

:   The current subroutine

### {{ renderMember(type='bool', name='isOuterVariable') }}

:   true if the provided parameter is a defined outer variable

### {{ renderMember(type='bool', name='isTLO') }}

:   true if the provided parameter an existing TLO

### {{ renderMember(type='int', name='MemUse') }}

:   How much memory the macro is using

### {{ renderMember(type='string', name='Name') }}

:   The name of the macro currently running

### {{ renderMember(type='int', name='Params') }}

:   The number of parameters that were passed to the current subroutine

### {{ renderMember(type='bool', name='Paused') }}

:   NULL if no macro running, FALSE if mqpause is off, TRUE if mqpause is on

### {{ renderMember(type='string', name='Return') }}

:   The value that was returned by the last completed subroutine

### {{ renderMember(type='int64', name='RunTime') }}

:   How long the macro has been running (in seconds)

### {{ renderMember(type='int', name='StackSize') }}

:   StackSize?

### {{ renderMember(type='varies', name='Variable') }}

:   returns the value given the name of Macro variable. The type of this member depends on the type of the variable being accessed.


## Methods

| Method Name | Action |
| :--- | :--- |
| Undeclared | List all undeclared variables |

[bool]: datatype-bool.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
