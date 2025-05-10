---
tags:
    - datatype
---
# `inifilesectionkey`

<!--dt-desc-start-->
This is the type for the referenced key in a specific section of an ini file.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='int', name='Count') }}

:   How many keys matching the Key[] index exist.

### {{ renderMember(type='bool', name='Exists') }}

:   Whether a specific key exists.

### {{ renderMember(type='string', name='Value') }}

:   The value for a specific key.  Accepts an Index to allow for returning a value if the key does not exist

### {{ renderMember(type='string', name='KeyAtIndex') }}

:   The name of the key at the specified index

### {{ renderMember(type='string', name='ValueAtIndex') }}

:   The value of the entry at the specified index
<!--dt-members-end-->

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

<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
