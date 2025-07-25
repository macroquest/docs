---
tags:
    - datatype
---
# `achievementmgr`

<!--dt-desc-start-->
Provides access achievements, achievement categories, and other information surrounding the achievement system.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='achievement', name='Achievement', params='#|Name') }}

:   Find an achievement by its ID or by its name.

### {{ renderMember(type='achievement', name='AchievementByIndex', params='#') }}

:   Find an achievement by its index.

### {{ renderMember(type='int', name='AchievementCount') }}

:   The number of achievements in the manager.

### {{ renderMember(type='achievementcat', name='Category', params='#|Name') }}

:   Find an achievement category by its id or by its name.Note: If searching by name, only top-level categories are returned from the achievement manager.

### {{ renderMember(type='achievementcat', name='CategoryByIndex', params='#') }}

:   Find an achievement category by its index.

### {{ renderMember(type='int', name='CategoryCount') }}

:   The number of achievement categories in the manager.

### {{ renderMember(type='int', name='Points') }}

:   The total number of accumulated achievement points.

### {{ renderMember(type='int', name='CompletedAchievement') }}

:   The number of completed achievements.

### {{ renderMember(type='int', name='TotalAchievement') }}

:   The number of available achievements.

### {{ renderMember(type='bool', name='Ready') }}

:   Indicates that the manager has loaded all achievement data and is ready to be used.
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[bool]: datatype-bool.md
[int]: datatype-int.md
<!--dt-linkrefs-end--> 