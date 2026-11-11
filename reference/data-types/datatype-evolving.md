---
tags:
    - datatype
---
# `evolving`

<!--dt-desc-start-->
A DataType that deals with evolving items.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool ExpOn
Is evolving item experience turned on for this item?
///

/// member | float ExpPct
Percentage of experience that the item has gained
///

/// member | int Level
The level of the evolving item.
///

/// member | int MaxLevel
The maximum level of the evolving item
///

### [string][string] `To String`

:   Same as **ExpOn**
<!--dt-members-end-->

## Usage

!!! example

    === "MQScript"

        ```
        /echo ${FindItem[Blade of the Eclipse].Evolving.ExpPct}
        ```

    === "Lua"

        ```lua
        print(mq.TLO.FindItem("Blade of the Eclipse").Evolving.ExpPct())
        ```
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
