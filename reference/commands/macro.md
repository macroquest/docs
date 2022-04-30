# /macro

## Syntax

**/macro** _**filename**_ **[** _**param0**_ **\[** _**param1**_ **\[...\]\]]**

## Description

Starts running a macro. Optional parameters can be added to the end of the /macro line, and the parameters will be passed to Sub Main within that macro.

**Notes**

* Calling a macro from another macro will end the calling macro.  
* \*\*Invoking a /macro from within a macro will cause the first line to be skipped in the new

  macro. Deal with it.&lt;/span&gt;\*\*

## Examples

```text
/macro mymacro

/macro mymacro "water flask" "metal bits"
```
