# DataType:evolving

A DataType that deals with evolving items.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](datatype-bool.md) | **ExpOn** | Is evolving item experience turned on for this item? |
| [_float_](datatype-float.md) | **ExpPct** | Percentage of experience that the item has gained |
| [_int_](datatype-int.md) | **Level** | The level of the evolving item. |
| [_int_](datatype-int.md) | **MaxLevel** | The maximum level of the evolving item |
| [_string_](datatype-string.md) | **To String** | Same as **ExpOn** |

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
