---
tags:
    - datatype
---
# `inifilesection`

This is the type for the referenced section of an ini file.  The Index passed to Section[] is optional.  Passing an Index means it will search for matches to that Index.  Not passing an Index references all sections for operations that allow it.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Count** | How many sections matching the Section[] index exist. |
| [_bool_](datatype-bool.md) | **Exists** | Whether a specific section exists. |
| [_inifilesectionkey_](datatype-inifilesectionkey.md) | **Key** | A reference to the named or unnamed key in this specific ini file section. |

## Examples

Given the sample.ini file:

```ini
[Section1]
Key1=foo
Key2=bar
[Section1]
Key1=bar
Key2=foo
[Section2]
Key=foo
Key=bar
Key=foobar
```

!!! Example

    === "MQScript"

        How many sections are there?

        ```
        /echo ${Ini.File[Sample].Section.Count}
        3
        ```

        How many sections named "Section1" are there?

        ```
        /echo ${Ini.File[Sample].Section[Section1].Count}
        2
        ```

        Does "Section3" exist?

        ```
        /echo ${Ini.File[Sample].Section[Section3].Exists}
        FALSE
        ```

    === "Lua"

        How many sections are there?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section.Count())
        3
        ```

        How many sections named "Section1" are there?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section1").Count()}
        2
        ```

        Does "Section3" exist?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section3").Exists()}
        false
        ```

