---
tags:
    - datatype
---
# `achievementcat`

Provides access to achievement categories. Achievements are organized hierarchically in the achievements window by categories.

While not required to access achievements, categories may be useful for enumerating lists of achievements.

## Members

### {{ renderMember(type='int', name='ID') }} 

:   The unique ID for the category

### {{ renderMember(type='string', name='Name') }} 

:   The category's display name

### {{ renderMember(type='string', name='Description') }} 

:   The category's description

### {{ renderMember(type='achievement', name='Achievement', params='#|Name') }} 

:   Find an achievement in this category by its ID or name.

### {{ renderMember(type='achievement', name='AchievementByIndex', params='#') }} 

:   Find an achievement by its index in this category.

### {{ renderMember(type='int', name='AchievementCount') }} 

:   The number of achievements in this category.

### {{ renderMember(type='achievementcat', name='Category', params='#|Name') }} 

:   Find a child category in this category by its ID or name.

### {{ renderMember(type='achievementcat', name='CategoryByIndex') }} 

:   Find a child category by its index in this category.

### {{ renderMember(type='int', name='CategoryCount') }} 

:   The number of child categories in this category.

### {{ renderMember(type='int', name='Points') }} 

:   The total earned points of achievements in this category.

### {{ renderMember(type='int', name='CompletedAchievements') }} 

:   The number of achievements earned in this category and its subcategories

### {{ renderMember(type='int', name='TotalAchievements') }} 

:   The total number of achievements in this category and its subcategories.

### {{ renderMember(type='string', name='ImageTextureName') }} 

:   Name of the image texture that is used to represent this category in the Achievements Window.

### {{ renderMember(type='int', name='Index') }} 

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
