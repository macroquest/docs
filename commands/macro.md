## Syntax

**<span style="color:red">/macro</span> *<span style="color:blue">filename</span>* \[ *param0* \[ *param1* \[...\]\]\]**

## Description

Starts running a macro. Optional parameters can be added to the end of the /macro line, and the parameters will be
passed to Sub Main within that macro.

**Notes**

-   Calling a macro from another macro will end the calling macro.  
-   **<span style="color:red">Invoking a /macro from within a macro will cause the first line to be skipped in the new
    macro. Deal with it.</span>**

## Examples

    /macro mymacro

    /macro mymacro "water flask" "metal bits"

## See Also

-   [Macros (about macros in general)](../documentation/macroquest2-macros.md)
-   [Macro (Top-Level Object)](../top-level-objects/tlo-macro.md)
-   [DataType:Macro](../data-types/datatype-macro.md)

[Return to Slash Commands](slash-commands.md)


