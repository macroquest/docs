---
tags:
    - datatype
---
# `achievementobj`

Represents a single objective of an achievement

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | The objective's unique ID. |
| [_string_](datatype-string.md) | **Description** | Text describing this objective. |
| [_int_](datatype-int.md) | **Count** | The current count recorded by the objective. |
| [_int_](datatype-int.md) | **RequiredCount** | The total count required to be complete the objective. For objectives that don't require a count, this will be zero. |
| [_bool_](datatype-bool.md) | **Completed** | True if the objective has been completed. |
| [_int_](datatype-int.md) | **Index** | Visual index of the objective as displayed in the achievement window. Can be used with **Achievement.ObjectiveByIndex**. |

### Example

List the objectives that are still left to complete the achievement "**Norrathian Explorer**":

=== "MQScript"
    ```
    /declare ach achievement local Norrathian Explorer

    /if (${ach.Completed}) {
        /echo ${ach.Name} is complete!
    } else {
        /echo The following objectives for ${ach.Name} are incomplete:
        /declare i int local
        /for i 1 to ${ach.ObjectiveCount} {
            /if (!${ach.ObjectiveByIndex[${i}].Completed}) {
                /echo ${ach.ObjectiveByIndex[${i}].Description}
            }
            /next i
        }
    }
    ```

=== "Lua"

    ```lua
    local achievement = mq.TLO.Achievement('Norrathian Explorer')

    if achievement.Completed() then
        print(string.format('%s complete!', achievement.Name()))
    else
        print(string.format('The following objectives for %s are incomplete:', achievement.Name()))
        for i = 1, achievement.ObjectiveCount() do
            local objective = achievement.ObjectiveByIndex(i)
            if not objective.Completed() then
                print(achievement.ObjectiveByIndex(i).Description())
            end
        end
    end
    ```
