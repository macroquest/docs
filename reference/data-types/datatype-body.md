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

!!! Example

    === "MQScript"

        Prints true if a summoned npc is targeted

        ```
        /echo ${Target.Body.Name.Equal[Undead Pet]}`
        ```

    === "Lua"

        Prints true if a summoned npc is targeted

        ```lua
        print(mq.TLO.Target.Boddy.Name === 'Undead Pet')
        ```
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
