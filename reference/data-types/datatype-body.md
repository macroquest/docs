---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `body`

Contains data about spawn body types

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | The ID of the body type |
| [_string_](datatype-string.md) | **Name** | The full name of the body type |
| [_string_](datatype-string.md) | **To String** | Same as **Name** |

## Usage

!!! Example

    === "MQScript"

        Prints true if a summoned npc is targeted

        ```
        /echo ${Target.Body.Name.Equal[Undead Pet]}`
        ```

    === "Lua"

        Prints true if a summoned npc is targeted

        ```lua
        print(mq.TLO.Target.Boddy.Name === 'Undead Pet')
        ```
