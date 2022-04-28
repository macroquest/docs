# DataType:achievement

Provides the details about a single achievement and allows access to an achievement's objective.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | The achievement's unique ID. |
| \_\_[_string_](datatype-string.md)\_\_ | **Name** | The achievement's name |
| \_\_[_string_](datatype-string.md)\_\_ | **Description** | The achievement's description |
| [_int_](datatype-int.md) | **Points** | The point value for the achievement |
| \_\_[_achievementobj_](datatype-achievementobj.md)\_\_ | **Objective[**\#\|_Description_**]** | Find an objective by its objective ID or Description. |
| \_\_[_achievementobj_](datatype-achievementobj.md)\_\_ | **ObjectiveByIndex[**\#**]** | Find an objective by its visual ordering as displayed in the achievements window. |
| [_int_](datatype-int.md) | **ObjectiveCount** | The number of objectives in this achievement. |
| \_\_[_string_](datatype-string.md)\_\_ | **Link[**_opt: Name_**]** | Generate an achievement link. An optional name can be provided to display in the achievement, otherwise the current character's name will be used. |
| [_int_](datatype-int.md) | **Index** | The index of the achievement. See [Achievement Indices](../top-level-objects/tlo-achievement.md#note-about-achievement-indices) for more information. |
| [_int_](datatype-int.md) | **IconID** | ID of the Achievement's Icon. See [Achievement Icon](datatype-achievement.md#achievement-icon) below. |
| \_\_[_string_](datatype-string.md)\_\_ | **State** | The achievement state. See [Achievement State](datatype-achievement.md#achievement-state) below. |
| \_\_[_bool_](datatype-bool.md)\_\_ | **Completed** | True if the achievement has been completed |
| \_\_[_bool_](datatype-bool.md)\_\_ | **Open** | True if the achievement is open |
| \_\_[_bool_](datatype-bool.md)\_\_ | **Locked** | True if the achievement is locked |
| \_\_[_bool_](datatype-bool.md)\_\_ | **Hidden** | True if the achievement is hidden |
| \_\_[_time_](../top-level-objects/tlo-time.md)\_\_ | **CompletedTime** | Calendar time when the achievement was completed. |

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

{% tabs %}
{% tab title="MQScript" %}
```text
/say This is an achievement link: ${Achievement[2801001].Link}
```
{% endtab %}

{% tab title="Lua" %}
```lua
mq.cmdf("/say This is an achievement link: %s", mq.TLO.Achievement(2801001).Link())
```
{% endtab %}
{% endtabs %}

Print a message if an achievement has been completed. This example also demonstrates how to properly use an achievement index.

{% tabs %}
{% tab title="MQScript" %}
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
{% endtab %}

{% tab title="Lua" %}
```lua
-- 500980300 = Wayfarers Brotherhood Adventurer's Stone (Various 20+)
local achievementIndex = mq.TLO.Achievement(500980300).Index()

local achievement = mq.TLO.Achievement.AchievementByIndex(achievementIndex)
if achievement.Completed() then
    print(string.format('%s is completed on %s', achievement.Name(), achievement.CompletedTime.Date()))
else
    print(achievement.Name() .. ' is not completed!')
end
```
{% endtab %}
{% endtabs %}

Print how many humans you have left to kill for the "**I'm a People Person!**" achievement

{% tabs %}
{% tab title="MQScript" %}
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
{% endtab %}

{% tab title="Lua" %}
```lua
local achievement = mq.TLO.Achievement("I'm a People Person!")

if achievement.Completed() then
    print("Achievement completed!")
else
    local objective = achievement.Objective("Humans")
    if not objective.Completed() then
        print(string.format("You have %d humans left to kill!", objective.RequiredCount() - objective.Count()))
    else
        print("Done killing humans!")
    end
end
```
{% endtab %}
{% endtabs %}

