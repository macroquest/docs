---
tags:
    - datatype
---
# `achievementcat`

Provides access to achievement categories. Achievements are organized hierarchically in the achievements window by categories.

While not required to access achievements, categories may be useful for enumerating lists of achievements.

## Members

### [int][int] `ID`

:   The unique ID for the category

### [string][string] `Name`

:   The category's display name

### [string][string] `Description`

:   The category's description

### [achievement][achievement] `Achievement[#|Name]`

:   Find an achievement in this category by its ID or name.

### [achievement][achievement] `AchievementByIndex[#]`

:   Find an achievement by its index in this category.

### [int][int] `AchievementCount`

:   The number of achievements in this category.

### [achievementcat][achievementcat] `Category[#|Name]`

:   Find a child category in this category by its ID or name.

### [achievementcat][achievementcat] `CategoryByIndex`

:   Find a child category by its index in this category.

### [int][int] `CategoryCount`

:   The number of child categories in this category.

### [int][int] `Points`

:   The total earned points of achievements in this category.

### [int][int] `CompletedAchievements`

:   The number of achievements earned in this category and its subcategories

### [int][int] `TotalAchievements`

:   The total number of achievements in this category and its subcategories.

### [string][string] `ImageTextureName`

:   Name of the image texture that is used to represent this category in the Achievements Window.

### [int][int] `Index`

:   The index of the category in the achievement manager. For more information see [Achievement Indices](../top-level-objects/tlo-achievement.md#note-about-achievement-indices).


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
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
