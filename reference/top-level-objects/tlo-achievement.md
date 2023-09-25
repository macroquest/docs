---
tags:
    - tlo
---
# `Achievement`

Provides access to achievements.

## Forms

### [achievement][achievement] `Achievement[#|Name]`

:   Look up an achievement by name or by id.

### [achievementmgr][achievementmgr] `Achievement`

:   Access the achievement manager which provides access to information about achievements


## Associated DataTypes

### `achievementmgr` Type

Provides access achievements, achievement categories, and other information surrounding the achievement system.

### [Type][Type] `Name`

:   Description

### [achievement][achievement] `Achievement[#|Name]`

:   Find an achievement by its ID or by its name.

### [achievement][achievement] `AchievementByIndex[#]`

:   Find an achievement by its index.

### [int][int] `AchievementCount`

:   The number of achievements in the manager.

### [achievementcat][achievementcat] `Category[#|Name]`

:   Find an achievement category by its id or by its name.Note: If searching by name, only top-level categories are returned from the achievement manager.

### [achievementcat][achievementcat] `CategoryByIndex[#]`

:   Find an achievement category by its index.

### [int][int] `CategoryCount`

:   The number of achievement categories in the manager.

### [int][int] `Points`

:   The total number of accumulated achievement points.

### [int][int] `CompletedAchievement`

:   The number of completed achievements.

### [int][int] `TotalAchievement`

:   The number of available achievements.

### [bool][bool] `Ready`

:   Indicates that the manager has loaded all achievement data and is ready to be used.



## Usage

!!! warning
    Looking up achievements by name may not always return the correct achievement if multiple exist with the same name. Achievement IDs should
    be preferred over names as they don't change and are unique.

???+ note "Note About Achievement Indices"

    Achievements and categories can be looked up by index. This is significantly faster than looking up by
    id or name. However, these indices are **not** stable and will change from patch to patch,
    but they will not change during the session.

    If an achievement is being utilized in a script many times, it may be more performant to look up an
    achievement's index (with its .Index member) and then use that in subsequent queries.

    See [Achievement Examples](../data-types/datatype-achievement.md#examples) for some examples of using
    indices for looking up achievements.


**Achievement**[ _#_ ] and **Achievement.Achievement**[ _#_ ] are equivalent and are provided for consistency. The primary way to access achievement information should be via id. Achievement IDs are unique and do not change.

To look up an achievement's ID, you can look up an achievement by name, or you can use the Achievements Inspector.


### Usage Examples

=== "MQScript"

    ```text
    | Look up an achievement by name, and then print its ID.
    /echo ${Achievement[Master of Claws of Veeshan].ID}

    | print the completed status of achievement
    | "Wayfarers Brotherhood Adventurer's Stone (Various 20+)"
    /echo ${Achievement[500980300].Completed}
    ```

=== "Lua"

    ```lua
    -- Look up an achievement by name, and then print its ID.
    print(mq.TLO.Achievement("Master of Claws of Veeshan").ID())

    -- print the completed status of achievement
    -- "Wayfarers Brotherhood Adventurer's Stone (Various 20+)"
    print(mq.TLO.Achievement(500980300).Completed())
    ```
[int]: ../data-types/datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: ../data-types/datatype-bool.md
[time]: datatype-time.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
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
[double]: datatype-double.md
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
