---
tags:
    - datatype
---
# `achievementcat`

<!--dt-desc-start-->
Provides access to achievement categories. Achievements are organized hierarchically in the achievements window by categories.

While not required to access achievements, categories may be useful for enumerating lists of achievements.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | achievement Achievement[#|Name]
Find an achievement in this category by its ID or name.
///

/// member | achievement AchievementByIndex[#]
Find an achievement by its index in this category.
///

/// member | int AchievementCount
The number of achievements in this category.
///

/// member | achievementcat Category[#|Name]
Find a child category in this category by its ID or name.
///

/// member | achievementcat CategoryByIndex
Find a child category by its index in this category.
///

/// member | int CategoryCount
The number of child categories in this category.
///

/// member | int CompletedAchievements
The number of achievements earned in this category and its subcategories
///

/// member | string Description
The category's description
///

/// member | int ID
The unique ID for the category
///

/// member | string ImageTextureName
Name of the image texture that is used to represent this category in the Achievements Window.
///

/// member | int Index
The index of the category in the achievement manager. For more information see [Achievement Indices](../top-level-objects/tlo-achievement.md#usage).
///

/// member | string Name
The category's display name
///

/// member | int Points
The total earned points of achievements in this category.
///


/// member | int TotalAchievements
The total number of achievements in this category and its subcategories.
///
<!--dt-members-end-->

### Examples

List the unearned achievements in the **EverQuest / Exploration** category:

=== "MQScript"

    ```text
    /declare cat achievementcat local
    /vardata cat Achievement.Category[EverQuest].Category[Exploration]

    /echo Unearned achievements in the ${cat.Name} category:
    /declare i int local
    /for i 1 to ${cat.AchievementCount} {
        /if (!${cat.AchievementByIndex[${i}].Completed}) {
            /echo ${cat.AchievementByIndex[${i}].Name}
        }
        /next i
    }
    ```

=== "Lua"

    ```lua
    local category = mq.TLO.Achievement.Category('EverQuest').Category('Exploration')
    for i = 1, category.AchievementCount() do
        local achievement = category.AchievementByIndex(i)
        if not achievement.Completed() then
            print(achievement.Name())
        end
    end
    ```
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
<!--dt-linkrefs-end-->
