---
tags:
    - datatype
---
# `social`

<!--dt-desc-start-->
Data related to an Everquest social macro.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='string', name='Cmd', params='opt: lineNo') }}

:   Command lines of social. Provide `lineNo` (line number) to retrieve individual lines. If
    line number is omitted, then the full list of commands will be returned as a single string
    with multiple lines.

### {{ renderMember(type='int', name='Color') }}

:   Retrieves the social button's RGB color as an integer.

### {{ renderMember(type='string', name='Name') }} 

:   Name of the social.
<!--dt-members-end-->

## Example

!!! Example

    Retrieve the name of the third social on the first page

    === "MQScript"

        ```text
        /echo ${Social[3].Name}
        ```

    === "Lua"

        ```lua
        print(mq.TLO.Social(3).Name())
        ```

<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
