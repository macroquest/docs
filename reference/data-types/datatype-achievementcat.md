---
tags:
    - datatype
---
# `achievementcat`

Provides access to achievement categories. Achievements are organized hierarchically in the achievements window by categories.

While not required to access achievements, categories may be useful for enumerating lists of achievements.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | The unique ID for the category |
| [_string_](datatype-string.md) | **Name** | The category's display name |
| [_string_](datatype-string.md) | **Description** | The category's description |
| [_achievement_](datatype-achievement.md) | **Achievement[**\#\|_Name_**]** | Find an achievement in this category by its ID or name. |
| [_achievement_](datatype-achievement.md) | **AchievementByIndex[**\#**]** | Find an achievement by its index in this category. |
| [_int_](datatype-int.md) | **AchievementCount** | The number of achievements in this category. |
| [_achievementcat_](datatype-achievementcat.md) | **Category[**\#\|_Name_**]** | Find a child category in this category by its ID or name. |
| [_achievementcat_](datatype-achievementcat.md) | **CategoryByIndex** | Find a child category by its index in this category. |
| [_int_](datatype-int.md) | **CategoryCount** | The number of child categories in this category. |
| [_int_](datatype-int.md) | **Points** | The total earned points of achievements in this category. |
| [_int_](datatype-int.md) | **CompletedAchievements** | The number of achievements earned in this category and its subcategories |
| [_int_](datatype-int.md) | **TotalAchievements** | The total number of achievements in this category and its subcategories. |
| [_string_](datatype-string.md) | **ImageTextureName** | Name of the image texture that is used to represent this category in the Achievements Window. |
| [_int_](datatype-int.md) | **Index** | The index of the category in the achievement manager. For more information see [Achievement Indices](../top-level-objects/tlo-achievement.md#note-about-achievement-indices). |

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
