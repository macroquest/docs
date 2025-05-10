---
tags:
    - datatype
---
# `inifile`

<!--dt-desc-start-->
This is the type for the ini file that was referenced from [TLO:Ini](../top-level-objects/tlo-ini.md)
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='bool', name='Exists') }}

:   Whether the ini file exists or not.

### {{ renderMember(type='inifilesection', name='Section', params='opt: Section') }}

:   A reference to the named or unnamed section of this ini file.

    The index is optional. Passing an index means it will search for matches to that index. Not passing an index references all sections for operations that allow it.
<!--dt-members-end-->

## Examples

!!! Example

    Does the file "sample.ini" exist?

    === "MQScript"

        ```
        /echo ${Ini.File[sample].Exists}
        ```

    === "Lua"

        ```lua
        mq.TLO.Ini.File("sample").Exists()
        ```
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[inifilesection]: datatype-inifilesection.md
<!--dt-linkrefs-end-->
