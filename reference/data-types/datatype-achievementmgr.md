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
/// member | achievement Achievement[#|Name]
Find an achievement by its ID or by its name.
///

/// member | achievement AchievementByIndex[#]
Find an achievement by its index.
///

/// member | int AchievementCount
The number of achievements in the manager.
///

/// member | achievementcat Category[#|Name]
Find an achievement category by its id or by its name.Note: If searching by name, only top-level categories are returned from the achievement manager.
///

/// member | achievementcat CategoryByIndex[#]
Find an achievement category by its index.
///

/// member | int CategoryCount
The number of achievement categories in the manager.
///

/// member | int Points
The total number of accumulated achievement points.
///

/// member | int CompletedAchievement
The number of completed achievements.
///

/// member | int TotalAchievement
The number of available achievements.
///

/// member | bool Ready
Indicates that the manager has loaded all achievement data and is ready to be used.
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[bool]: datatype-bool.md
[int]: datatype-int.md
<!--dt-linkrefs-end--> 