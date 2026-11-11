---
tags:
    - datatype
---
# `body`

<!--dt-desc-start-->
Contains data about spawn [body types](../general/body-types.md)
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int ID
The ID of the body type
///

/// member | string Name
The full name of the body type
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

## Usage

!!! example

    Prints true if a summoned npc is targeted

    === "MQScript"

        ```
        /echo ${Target.Body.Name.Equal[Undead Pet]}`
        ```

    === "Lua"

        ```lua
        print(mq.TLO.Target.Boddy.Name === 'Undead Pet')
        ```
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
