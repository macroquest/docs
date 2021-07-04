## Syntax

**<span style="color:red">/break</span>**

## Description

End a /for or /while loop immediately.

## Example

     /for varname 1 to 5
       /if ({$varname} == 3) /break
       /echo ${varname}
     /next varname

Will output:

     1
     2

## See also

-   [/for](for.md)


