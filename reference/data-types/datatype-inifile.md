---
tags:
    - datatype
---
# `inifile`

This is the type for the ini file that was referenced from `${Ini}`

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](datatype-bool.md) | **Exists** | Whether the ini file exists or not. |
| [_inifilesection_](datatype-inifilesection.md) | **Section** | A reference to the named or unnamed section of this ini file. |

## Examples

!!! Example

    === "MQScript"

        Does the file "sample.ini" exist?

        ```
        /echo ${Ini.File[sample].Exists}
        ```

    === "Lua"

        Does the file "sample.ini" exist?

        ```lua
        mq.TLO.Ini.File("sample").Exists()
        ```

