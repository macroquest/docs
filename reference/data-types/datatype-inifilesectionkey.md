---
tags:
    - datatype
---
# `inifilesectionkey`

This is the type for the referenced key in a specific section of an ini file.  The Index passed to Key[] is optional.  Passing an Index means it will search for matches to that Index.  Not passing an Index references all keys for operations that allow it.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Count** | How many keys matching the Key[] index exist. |
| [_bool_](datatype-bool.md) | **Exists** | Whether a specific key exists. |
| [_string_](datatype-string.md) | **Value** | The value for a specific key.  Accepts an Index to allow for returning a value if the key does not exist |
| [_string_](datatype-string.md) | **KeyAtIndex** | The name of the key at KeyAtIndex[Index] |
| [_string_](datatype-string.md) | **ValueAtIndex** | The value at ValueAtIndex[Index] |

## Examples

Given the sample.ini file:

```ini
[Section1]
Key1=foo
Key2=bar
[Section2]
Key=foo
Key=bar
Key=foobar
Key4=foobarfour
```

!!! Example

    === "MQScript"

        How many keys are there in Section1?

        ```
        /echo ${Ini.File[Sample].Section[Section1].Key.Count}
        2
        ```

        How many keys named "Key" are there in Section2?

        ```
        /echo ${Ini.File[Sample].Section[Section2].Key[Key].Count}
        3
        ```

        What is the value of Key1 in Section1?

        ```
        /echo ${Ini.File[Sample].Section[Section1].Key[Key1].Value}
        foo
        ```

        What is the value of Key in Section2?

        ```
        /echo ${Ini.File[Sample].Section[Section2].Key[Key].Value}
        foo
        ```

        What is the value of the 2nd key named "Key" in Section 2?

        ```
        /echo ${Ini.File[Sample].Section[Section2].Key[Key].ValueAtIndex[2]}
        bar
        ```

        Get the value of Section2, Key5 and if it doesn't exist, return "foobarfive":

        ```
        /echo ${Ini.File[Sample].Section[Section2].Key[Key5].Value[foobarfive]}
        foobarfive
        ```

    === "Lua"

        How many keys are there in Section1?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section1").Key.Count())
        2
        ```

        How many keys named "Key" are there in Section2?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section2").Key("Key").Count())
        3
        ```

        What is the value of Key1 in Section1?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section1").Key("Key1").Value())
        foo
        ```

        What is the value of Key in Section2?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section2").Key("Key").Value())
        foo
        ```

        What is the value of the 2nd key named "Key" in Section 2?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section2").Key("Key").ValueAtIndex(2))
        bar
        ```

        Get the value of Section2, Key5 and if it doesn't exist, return "foobarfive":

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section2").Key("Key5").Value("foobarfive"))
        foobarfive
        ```



