# TLO:Achievement

Provides access to achievements.

## Forms

| Type | Form | Description |
| ---- | ---- | ---- |
| _[achievement](../data-types/datatype-achievement.md)_ | **Achievement[#\|Name]** | Look up an achievement by name or by id. |
| _[achievementmgr](#achievementmgr-type)_ | **Achievement** | Access the achievement manager which provides access to information about achievements |

## AchievementMgr Type

Provides access achievements, achievement categories, and other information surrounding the achievement system.

| Type | Name | Description |
| ---- | ---- | ---- |
| _[achievement](../data-types/datatype-achievement.md)_           | **Achievement[#\|Name]** |  Find an achievement by its ID or by its name.         |
| _[achievement](../data-types/datatype-achievement.md)_           | **AchivementByIndex[#]** |  Find an achievement by its index.                     |
| _[int](../data-types/datatype-int.md)_                           | **AchivementCount**      |  The number of achievements in the manager.            |
| _[achievementcat](../data-types/datatype-achievementcat.md)_     | **Category[#\|Name]**    |  Find an achievement category by its id or by its name.Note: If searching by name, only top-level categories are returned from the achievement manager.    |
| _[achievementcat](../data-types/datatype-achievementcat.md)_     | **CategoryByIndex[#]**   |  Find an achievement category by its index.            |
| _[int](../data-types/datatype-int.md)_                           | **CategoryCount**        |  The number of achievement categories in the manager.  |
| _[int](../data-types/datatype-int.md)_                           | **Points**               |  The total number of accumulated achievement points.    |
| _[int](../data-types/datatype-int.md)_                           | **CompletedAchivements** |  The number of completed achievements.    |
| _[int](../data-types/datatype-int.md)_                           | **TotalAchivements**     |  The number of available achievements.    |
| _[bool](../data-types/datatype-bool.md)_                         | **Ready**                |  Indicates that the manager has loaded all achievement data and is ready to be used.    |

## Usage

!!! warning
    Looking up achievements by name may not always return the correct achievement if multiple exist with the same name. Achievement IDs should be preferred over names as they don't change and are unique.

**Achievement[**#**]** and **Achievement.Achievement[**#**]** are equivalent and are provided for consistency. The primary way to access achievement information should be via id. Achievement IDs are unique and do not change.

To look up an achievement's ID, you can look up an achievement by name, or you can use the Achievements Inspector.

#### ‌Note About Achievement Indices

Achievements and categories can be looked up by index. This is significantly faster than looking up by id or name. However, these indices are **not** stable and will change from patch to patch, but they will not change during the session. If an achievement is being utilized in a script many times, it may be more performant to look up an achievement's index (with its .Index member) and then use that in subsequent queries.

See [Achievement Examples](../data-types/datatype-achievement.md#examples) for some examples of using indices for looking up achievements.

### Examples

In the following example, we will look up an achievement by name, and then print its ID.

=== "MQScript"

    ```text
    /echo ${Achievement[Master of Claws of Veeshan].ID}
    ```

=== "Lua"

    ```lua
    print(mq.TLO.Achievement("Master of Claws of Veeshan").ID())
    ```

In the following example, we will print the completed status of achievement "**Wayfarers Brotherhood Adventurer's Stone (Various 20+)**"

=== "MQScript"

    ```
    /echo ${Achievement[500980300].Completed}
    ```

=== "Lua"

    ```lua
    print(mq.TLO.Achievement(500980300).Completed())
    ```