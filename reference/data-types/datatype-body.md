---
tags:
    - datatype
---
# `body`

Contains data about spawn body types

## Members

### {{ renderMember(type='int', name='ID') }}

:   The ID of the body type

### {{ renderMember(type='string', name='Name') }}

:   The full name of the body type

### [string][string] `To String`

:   Same as **Name**


## Usage

!!! example

    Prints true if a summoned npc is targeted

    === "MQScript"

        ```
        /echo ${Target.Body.Name.Equal[Undead Pet]}`
        ```

    === "Lua"

        ```lua
        print(mq.TLO.Target.Boddy.Name === 'Undead Pet')
        ```

[int]: datatype-int.md
[string]: datatype-string.md
