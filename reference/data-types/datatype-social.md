---
tags:
    - datatype
---
# `social`

Data related to an Everquest social macro.

## Members

### {{ renderMember(type='string', name='Cmd', params='opt: lineNo') }}

:   Command lines of social. Provide `lineNo` (line number) to retrieve individual lines. If
    line number is omitted, then the full list of commands will be returned as a single string
    with multiple lines.

### {{ renderMember(type='int', name='Color') }}

:   Retrieves the social button's RGB color as an integer.

### {{ renderMember(type='string', name='Name') }} 

:   Name of the social.


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


[int]: datatype-int.md
[string]: datatype-string.md
