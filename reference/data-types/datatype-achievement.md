---
tags:
    - datatype
---
# `achievement`

Provides the details about a single achievement and allows access to an achievement's objective.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | The achievement's unique ID. |
| [_string_](datatype-string.md) | **Name** | The achievement's name |
| [_string_](datatype-string.md) | **Description** | The achievement's description |
| [_int_](datatype-int.md) | **Points** | The point value for the achievement |
| [_achievementobj_](datatype-achievementobj.md) | **Objective[**\#\|_Description_**]** | Find an objective by its objective ID or Description. |
| [_achievementobj_](datatype-achievementobj.md) | **ObjectiveByIndex[**\#**]** | Find an objective by its visual ordering as displayed in the achievements window. |
| [_int_](datatype-int.md) | **ObjectiveCount** | The number of objectives in this achievement. |
| [_string_](datatype-string.md) | **Link[**_opt: Name_**]** | Generate an achievement link. An optional name can be provided to display in the achievement, otherwise the current character's name will be used. |
| [_int_](datatype-int.md) | **Index** | The index of the achievement. See [Achievement Indices](../top-level-objects/tlo-achievement.md#note-about-achievement-indices) for more information. |
| [_int_](datatype-int.md) | **IconID** | ID of the Achievement's Icon. See [Achievement Icon](datatype-achievement.md#achievement-icon) below. |
| [_string_](datatype-string.md) | **State** | The achievement state. See [Achievement State](datatype-achievement.md#achievement-state) below. |
| [_bool_](datatype-bool.md) | **Completed** | True if the achievement has been completed |
| [_bool_](datatype-bool.md) | **Open** | True if the achievement is open |
| [_bool_](datatype-bool.md) | **Locked** | True if the achievement is locked |
| [_bool_](datatype-bool.md) | **Hidden** | True if the achievement is hidden |
| [_time_](datatype-time.md) | **CompletedTime** | Calendar time when the achievement was completed. |

### Achievement State

An achievement has one of the following mutually exclusive states, accessed via **State**

| State | Description |
| :--- | :--- |
| OPEN | The achievement is available and not completed. |
| COMPLETED | The achievement has been completed |
| LOCKED | The achievement is "locked" and has criteria that must be completed to be unlocked. |
| HIDDEN | The achievement is hidden and not available to be earned. Hidden achievements include those that do not apply to the current character class. |

### Achievement Icon

Each achievement has an icon associated with it. This icon id represents a cell in the `A_DragItem` texture. To access the cell, subtract 500 from the icon id.

### Examples

Link an achievement into chat

=== "MQScript"

    ```text
    /say This is an achievement link: ${Achievement[2801001].Link}
    ```

=== "Lua"

    ```lua
    mq.cmdf("/say This is an achievement link: %s", mq.TLO.Achievement(2801001).Link())
    ```

Print a message if an achievement has been completed. This example also demonstrates how to properly use an achievement index.

=== "MQScript"

    ```text
    | 500980300 = Wayfarers Brotherhood Adventurer's Stone (Various 20+)
    /declare achievementIndex int local ${Achievement[500980300].Index}
    /echo ${achievementIndex}

    /if (${Achievement.AchievementByIndex[${achievementIndex}].Completed}) {
        /echo ${Achievement.AchievementByIndex[${achievementIndex}].Name} is completed on ${Achievement.AchievementByIndex[${achievementIndex}].CompletedTime.Date}
    } else {
        /echo ${Achievement.AchievementByIndex[${achievementIndex}].Name} is not completed!
    }
    ```

=== "Lua"

    ```lua
    -- 500980300 = Wayfarers Brotherhood Adventurer's Stone (Various 20+)
    local achievementIndex = mq.TLO.Achievement(500980300).Index()

    local achievement = mq.TLO.Achievement.AchievementByIndex(achievementIndex)
    if achievement.Completed() then
        printf('%s is completed on %s', achievement.Name(), achievement.CompletedTime.Date())
    else
        print(achievement.Name() .. ' is not completed!')
    end
    ```


Print how many humans you have left to kill for the "**I'm a People Person!**" achievement

=== "MQScript"

    ```
    | 11000028 = I'm a People Person!
    /if (${Achievement[11000028].Completed}) {
        /echo ${Achievement[11000028].Name} is complete!
    } else {
        | 300197 = Humans
        /if (!${Achievement[11000028].Objective[300197].Completed}) {
            /echo You have ${Math.Calc[${Achievement[11000028].Objective[300197].RequiredCount} - ${Achievement[11000028].Objective[300197].Count}].Int} humans left to kill!
        } else {
            /echo Done killing humans!
        }
    }
    ```

=== "Lua"

    ```lua
    local achievement = mq.TLO.Achievement("I'm a People Person!")

    if achievement.Completed() then
        print("Achievement completed!")
    else
        local objective = achievement.Objective("Humans")
        if not objective.Completed() then
            printf("You have %d humans left to kill!", objective.RequiredCount() - objective.Count())
        else
            print("Done killing humans!")
        end
    end
    ```

## Methods

| Name           | Action                 |
| -------------- | ---------------------- |
| **Inspect**    | Opens the achievement display window for this achievement |
