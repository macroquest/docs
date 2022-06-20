---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Plugin`

Object that has access to members that provide information on a plugin.

## Forms

[_plugin_][plugin] **Plugin**[_name_]

:   Finds plugin by name, uses full name match, case insensitive.

[_plugin_][plugin] **Plugin**[_N_] 

:   Plugin by index, starting with 1 and stopping whenever the list runs out of plugins.


## Examples

To see if a plugin is loaded:

=== "MQScript"

    ```
    /if (${Plugin[MQ2MoveUtils].IsLoaded}) {
        /echo MQ2MoveUtils plugin is loaded!
    }
    ```

=== "Lua"

    ```lua
    if mq.TLO.Plugin('MQ2MoveUtils').IsLoaded() then
        print('MQ2MoveUtils plugin is loaded!')
    end
    ```

To load a plugin if needed:

=== "MQScript"

    ```
    /if (!${Plugin[MQ2MoveUtils].IsLoaded}) {
        /plugin MQ2MoveUtils noauto
        /if (!${Plugin[MQ2MoveUtils].IsLoaded}) {
            /echo To Use this macro you need to have MQ2MoveUtils Loaded
            /endmacro
        }
    }
    ```

[plugin]: ../data-types/datatype-plugin.md