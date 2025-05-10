---
tags:
    - datatype
---
# `inifilesection`

<!--dt-desc-start-->
This is the type for the referenced section of an ini file.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='int', name='Count') }}

:   How many sections matching the Section[] index exist.

### {{ renderMember(type='bool', name='Exists') }}

:   Whether a specific section exists.

### {{ renderMember(type='inifilesectionkey', name='Key', params='opt: Key') }}

:   A reference to the named or unnamed key in this specific ini file section.

    The index is optional. Passing an index means it will reference all keys that match that index. Not passing an index references all keys for operations that allow it.
<!--dt-members-end-->

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
        | Prints 3
        /echo ${Ini.File[Sample].Section.Count}
        ```

        How many sections named "Section1" are there?

        ```
        | Orints 2
        /echo ${Ini.File[Sample].Section[Section1].Count}
        ```

        Does "Section3" exist?

        ```
        | Prints FALSE
        /echo ${Ini.File[Sample].Section[Section3].Exists}
        ```

    === "Lua"

        How many sections are there?

        ```lua
        -- prints 3
        print(mq.TLO.Ini.File("Sample").Section.Count())
        ```

        How many sections named "Section1" are there?

        ```lua
        -- prints 2
        print(mq.TLO.Ini.File("Sample").Section("Section1").Count())
        ```

        Does "Section3" exist?

        ```lua
        -- prints false
        print(mq.TLO.Ini.File("Sample").Section("Section3").Exists())
        ```
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[int]: datatype-int.md
<!--dt-linkrefs-end-->
