---
tags:
    - tlo
---
# `If`


!!! warning

    The `If` TLO is used to provide inline condition expressions for macros. It is not recommended for
    use with Lua.

Executes an inline condiition, similar to a ternary expression in other languages.

## Forms

[_string_][string] **If**[_conditions_,_whentrue_,_whenfalse_]

:   Performs [Math.Calc][Math.Calc] on _conditions_, gives _whentrue_ if non-zero, gives _whenfalse_ if zero.

    !!! example

        If I am sitting, stand up. Otherwise, echo "I am not sitting down"

        ```
        /docommand ${If[${Me.Sitting},/stand,/echo I am not sitting down]}
        ```

[_string_][string] **If**[_conditions_\~_whentrue_\~_whenfalse_]

:   Alternate syntax, behaves the same as above but uses the \~ character as a separator instead of a comma.   

[string]: ../data-types/datatype-string.md
[Math.Calc]: ..//data-types/datatype-math.md#calc
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
