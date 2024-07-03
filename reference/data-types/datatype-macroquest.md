---
tags:
    - datatype
---
# `macroquest`

Data types related to the current MacroQuest2 session.  These also inherit from the [EverQuest Type](datatype-everquest.md).

## Members

### {{ renderMember(type='bool', name='Anonymize') }}

:   Anonymize character data

### {{ renderMember(type='int', name='Build') }} 

:   The build (client target) for MQ2Main.dll (1 - Live, 2 - Test, 3 - Beta, 4 - Emu)

### {{ renderMember(type='string', name='BuildName') }} 

:   The build (client target) name for MQ2Main.dll (Live, Test, Beta, Emu)

### {{ renderMember(type='string', name='BuildDate') }} 

:   Date that MQ2Main.dll was built

### {{ renderMember(type='string', name='Error') }} 

:   Last normal error message

### {{ renderMember(type='string', name='InternalName') }} 

:   The internal name from MQ2Main.dll ("Next")

### {{ renderMember(type='string', name='MQ2DataError') }} 

:   Last MQ2Data parsing error message

### {{ renderMember(type='int', name='Parser') }} 

:   Which parser engine is currently active

### {{ renderMember(type='string', name='Path', params='Option') }} 

:   Directory that Macroquest.exe launched from.  When passed root/config/crashdumps/logs/mqini/macros/plugins/resources, returns the respective path

### {{ renderMember(type='string', name='SyntaxError') }} 

:   Last syntax error message

### {{ renderMember(type='string', name='Version') }} 

:   The full version of MQ2Main.dll

### [string][string] `To String`

:   None


## Example

```
/echo ${MacroQuest.Path[config]}
```

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: ../data-types/datatype-spell.md
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
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
