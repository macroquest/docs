---
tags:
    - datatype
---
# `macroquest`

<!--dt-desc-start-->
Data types related to the current MacroQuest session.  These also inherit from the [EverQuest Type](datatype-everquest.md).
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='bool', name='Anonymize') }}

:   Anonymize character data

### {{ renderMember(type='int', name='Build') }}

:   The build (client target) for MacroQuest

    | Value | Meaning |
    | :--- | :--- |
    | 1 | Live |
    | 2 | Test |
    | 3 | Beta |
    | 4 | Emu |

### {{ renderMember(type='string', name='BuildName') }}

:   The build (client target) name for MacroQuest:

    - "Live"
    - "Test"
    - "Beta"
    - "Emu"

### {{ renderMember(type='string', name='BuildDate') }}

:   Date that MacroQuest was built

### {{ renderMember(type='string', name='Error') }}

:   Last normal error message

### {{ renderMember(type='string', name='InternalName') }}

:   The internal name from MacroQuest("Next")

### {{ renderMember(type='string', name='MQ2DataError') }}

:   Last Macro parsing error message

### {{ renderMember(type='int', name='Parser') }}

:   Which parser engine is currently active

### {{ renderMember(type='string', name='Path', params='Option') }}

:   Retrieves the path to the specified location. If no path is provided, the root path
    of MacroQuest (where the MacroQuest.exe lives) is returned.

    !!! Important
        Be sure to use this member to access these paths, and do not hard code paths. These locations in MacroQuest are configurable and may not be in the default locations!

    | Option | Result |
    | :--- | :--- |
    | root | Returns the path to the root directory. |
    | config | Returns path to the config directory |
    | crashdumps | Returns the path to where crash dumps are stored |
    | logs | Returns the path to the logs directory |
    | mqini | Returns the path to MacroQuest.ini |
    | macros | Returns the path to the macros directory |
    | plugins | Returns the path to the plugins directory |
    | resources | Returns the path to the resources directory |

    If no path is provided, the root path is returned.

### {{ renderMember(type='string', name='SyntaxError') }}

:   Last syntax error message

### {{ renderMember(type='string', name='Version') }}

:   The full version of MacroQuest

### [string][string] `To String`

:   None
<!--dt-members-end-->

## Example

Get the path to the config directory.

```
/echo ${MacroQuest.Path[config]}
```
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
