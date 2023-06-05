---
tags:
    - tlo
---
# `If`


!!! warning

    The `If` TLO is used to provide inline condition expressions for macros. It is not recommended for
    use with Lua.

Executes an inline condiition, similar to a ternary expression in other languages.

## Forms

[_string_][string] **If**[_conditions_,_whentrue_,_whenfalse_]

:   Performs [Math.Calc][Math.Calc] on _conditions_, gives _whentrue_ if non-zero, gives _whenfalse_ if zero.

    !!! example

        If I am sitting, stand up. Otherwise, echo "I am not sitting down"

        ```
        /docommand ${If[${Me.Sitting},/stand,/echo I am not sitting down]}
        ```

[_string_][string] **If**[_conditions_\~_whentrue_\~_whenfalse_]

:   Alternate syntax, behaves the same as above but uses the \~ character as a separator instead of a comma.   
:   Note that \~ is the default alternate separator.  This can be changed by placing IfAltDelimiter in MacroQuest.ini under the [MacroQuest] section.   
:   E.g.:   IfAltDelimiter=|   

[string]: ../data-types/datatype-string.md
[Math.Calc]: ..//data-types/datatype-math.md#calc
