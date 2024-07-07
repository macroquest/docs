---
tags:
    - tlo
---
# `Social`

Access data about socials (in-game macro buttons)

## Forms

### {{ renderMember(type='social', name='Social', params='Index') }}

:   Look up a social by its button index.

    Each page as 12 socials, so index 13 would be the first social on the page 2. There are a total of 120 socials.


## Usage

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