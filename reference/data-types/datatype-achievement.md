---
tags:
    - datatype
---
# `achievement`

Provides the details about a single achievement and allows access to an achievement's objective.

## Members

### [int][int] `ID`

:   The achievement's unique ID.

### [string][string] `Name`

:   The achievement's name

### [string][string] `Description`

:   The achievement's description

### [int][int] `Points`

:   The point value for the achievement

### [achievementobj][achievementobj] `Objective[#|Description]`

:   Find an objective by its objective ID or Description.

### [achievementobj][achievementobj] `ObjectiveByIndex[#]`

:   Find an objective by its visual ordering as displayed in the achievements window.

### [int][int] `ObjectiveCount`

:   The number of objectives in this achievement.

### [string][string] `Link[opt: Name]`

:   Generate an achievement link. An optional name can be provided to display in the achievement, otherwise the current character's name will be used.

### [int][int] `Index`

:   The index of the achievement. See [Achievement Indices](../top-level-objects/tlo-achievement.md#note-about-achievement-indices) for more information.

### [int][int] `IconID`

:   ID of the Achievement's Icon. See [Achievement Icon](datatype-achievement.md#achievement-icon) below.

### [string][string] `State`

:   The achievement state. See [Achievement State](datatype-achievement.md#achievement-state) below.

### [bool][bool] `Completed`

:   True if the achievement has been completed

### [bool][bool] `Open`

:   True if the achievement is open

### [bool][bool] `Locked`

:   True if the achievement is locked

### [bool][bool] `Hidden`

:   True if the achievement is hidden

### [time][time] `CompletedTime`

:   Calendar time when the achievement was completed.


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
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
