---
tags:
    - tlo
---
# `If`


!!! warning

    The `If` TLO is used to provide inline condition expressions for macros. It is not intended for
    use with Lua.

Executes an inline condiition, similar to a ternary expression in other languages.

## Forms

### {{ renderMember(type='string', name='If', params='conditions,whentrue,whenfalse', toc_label='If') }}

:   Performs [Math.Calc][Math.Calc] on `conditions`, gives `whentrue` if non-zero, gives `whenfalse` if zero.

    !!! example

        If I am sitting, stand up. Otherwise, echo "I am not sitting down"

        ```
        /docommand ${If[${Me.Sitting},/stand,/echo I am not sitting down]}
        ```

### [string][string] `If[conditions~whentrue~whenfalse]` { #if_alternate data-toc-label="If - Alternate Syntax" }

:   Alternate syntax, behaves the same as above but uses the \~ character as a separator instead of a comma.   

[string]: ../data-types/datatype-string.md
[Math.Calc]: ../data-types/datatype-math.md#Calc[n]
