---
tags:
    - datatype
---
# `inifile`

This is the type for the ini file that was referenced from `${Ini}`

## Members

### {{ renderMember(type='bool', name='Exists') }} 

:   Whether the ini file exists or not.

### {{ renderMember(type='inifilesection', name='Section') }} 

:   A reference to the named or unnamed section of this ini file.


## Examples

!!! Example

    === "MQScript"

        Does the file "sample.ini" exist?

        ```
        /echo ${Ini.File[sample].Exists}
        ```

    === "Lua"

        Does the file "sample.ini" exist?

        ```lua
        mq.TLO.Ini.File("sample").Exists()
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
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
