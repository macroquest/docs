---
tags:
    - tlo
---
# `Ini`

Reads value(s) from an ini file located in a relative or absolute path.

## Forms

[_string_](../data-types/datatype-string.md) **Ini**[_filename_,_section_,_key_,_default_]

:   The _section_, _key_, and _default_ do not need to be given. If _section_ or _key_ are not given, multiple values are read.

    _Section_ and _key_ may be set to -1 to skip them and give a new value.

    If the ini is located in a directory other than the root Macros directory is located, you can use
    a DOS-style filepath (relative or absolute) to locate the ini. If the macro accessing the ini
    is in the same non-root directory, you will still to provide the (relative or absolute) filepath.

[_ini_](../data-types/datatype-ini.md) **Ini**

:   When passed with no parameters to Ini[] the more robust form of the Ini TLO is used.  See below and the reference
    to the [Key](../data-types/datatype-inifilesectionkey.md) datatype for further usage.

## Examples

If sample.ini contains:

```ini
[SectionOne]
key1=foo
key2=bar
[SectionTwo]
key3=foobar
```

```
/echo ${Ini[sample.ini,SectionOne,key1]}
```

foo

```
/echo ${Ini[sample.ini,SectionOne]}
```

key1|key2||

```
/echo ${Ini[..\sample.ini]}
```

SectionOne|SectionTwo||

If sample.ini is in \Macros\iniTest folder:

```
/echo ${Ini[sample.ini]}
```

NULL

```
/echo ${Ini[iniTest\sample.ini]}
```

SectionOne|SectionTwo||

# `Ini` (Robust Usage)

The above form of Ini usage is usable or most tasks, but a more robust usage exists.  In the more robust form `${Ini}` returns 
an [IniType](../data-types/datatype-ini.md) instead of a string.  This allows for dealing with duplicate keys as well as looping through a section by index.

## Examples

If sample.ini contains:

```ini
[SectionOne]
key1=foo
key=bar
key=foobar
```

```
> /echo ${Ini.File[sample].Section.Count}
1
> /echo ${Ini.File[sample].Section[SectionOne].Key.Count}
3
> /echo ${Ini.File[sample].Section[SectionOne].Key[key].Count}
2
> /echo ${Ini.File[sample].Section[SectionOne].Key[key1].Value}
foo
> /echo ${Ini.File[sample].Section[SectionOne].Key[key].ValueAtIndex[2]}
foobar
> /echo ${Ini.File[sample].Section[SectionOne].Key.ValueAtIndex[2]}
bar
```


[int]: ../data-types/datatype-int.md
[string]: ../data-types/datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: ../data-types/datatype-bool.md
[time]: datatype-time.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: ../data-types/datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: ../data-types/datatype-float.md
[buff]: datatype-buff.md
[spawn]: ../data-types/datatype-spawn.md
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
[double]: ../data-types/datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
[taskmember]: datatype-task.md
[achievementmgr]: #achievementmgr-type
[itemfilterdata]: #itemfilterdata-type
[advlootitem]: #advlootitem-type
[alert]: #alert-type
[alertlist]: #alertlist-type
[friends]: #friends-type
