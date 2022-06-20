---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Alias`

Provides a way to query whether a given alias exists. See [/alias](../commands/alias.md).

## Forms

| **Type** | **Form** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../data-types/datatype-bool.md) | **Alias**[ _Name_ ] | Returns bool indicating if named aliase exists |


## Usage Examples

=== "MQScript"

    ```
    | prints TRUE if the /yes alias exists
    /echo ${Alias[/yes]}
    ```

=== "Lua"

    ```lua
    -- prints true if the /yes alias exists
    print(mq.TLO.Alias('/yes')())
    ```
