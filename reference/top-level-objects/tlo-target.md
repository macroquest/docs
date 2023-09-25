---
tags:
    - tlo
---
# `Target`

Object used to get information about your current target.

## Forms

[_spawn_](../data-types/datatype-spawn.md) **Target**

:   Returns the spawn object for the current target.


!!! warning "Note"

    These examples are not specific to target but work on any spawn type.

!!! note

    To display the target's unique name as sent by EQ use `${Target}` or `${Target.Name}`

    This will return `a_commander01` on a living mob or `a_commander's_corpse0` on a dead mob.

    To display the target's clean name (also similar to %t on living mobs) use
    `${Target.CleanName}` or `${Target.DisplayName}`

    This will return `a commander` on a living mob or `a commander's corpse` on a dead mob.

    To display the name as used by '%t' on a corpse use the `${Target.DisplayName}`

    This will return `a commander` when the corpse is targetted.

!!! example

    To display the spell ID of the snare debuff use ${Target.Snared.ID}

    ```
    /echo ${Target.Snared.ID}
    ```

    Example of using new Slowed target datatype

    ```
    /echo ${Target.Slowed.Name} will fade in ${Target.Slowed.Duration.TotalSeconds}s
    ```

    returns "Tepid Deeds will fade in 114s"

    Example of using new Mezzed target datatype

    ```
    /echo ${Target} will break mezz in ${Target.Mezzed.Duration.TotalSeconds}s`
    ```

    returns "a\_pyre\_beetle48 will break mezz in 66s"

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
