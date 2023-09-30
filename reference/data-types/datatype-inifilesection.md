---
tags:
    - datatype
---
# `inifilesection`

This is the type for the referenced section of an ini file.  The Index passed to Section[] is optional.  Passing an Index means it will search for matches to that Index.  Not passing an Index references all sections for operations that allow it.

## Members

### {{ renderMember(type='int', name='Count') }} 

:   How many sections matching the Section[] index exist.

### {{ renderMember(type='bool', name='Exists') }} 

:   Whether a specific section exists.

### {{ renderMember(type='inifilesectionkey', name='Key') }} 

:   A reference to the named or unnamed key in this specific ini file section.


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
        /echo ${Ini.File[Sample].Section.Count}
        3
        ```

        How many sections named "Section1" are there?

        ```
        /echo ${Ini.File[Sample].Section[Section1].Count}
        2
        ```

        Does "Section3" exist?

        ```
        /echo ${Ini.File[Sample].Section[Section3].Exists}
        FALSE
        ```

    === "Lua"

        How many sections are there?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section.Count())
        3
        ```

        How many sections named "Section1" are there?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section1").Count()}
        2
        ```

        Does "Section3" exist?

        ```lua
        print(mq.TLO.Ini.File("Sample").Section("Section3").Exists()}
        false
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
[inifilesectionkey]: datatype-inifilesectionkey.md
