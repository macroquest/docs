# TLO:Achievement

Provides access to achievements.

## Forms <a id="forms"></a>

| Type | Form | Description |
| :--- | :--- | :--- |
| \_\_[_achievement_](../data-types/datatype-achievement.md)_​_ | **Achievement\[**\# or _Name_**\]** | Look up an achievement by name or by id. |
| _​_[_achievementmgr_](tlo-achievement.md#alert-type)_​_ | **Achievement** | Access the achievement manager which provides access to information about achievements |

## AchievementMgr Type <a id="alert-type"></a>

Provides access achievements, achievement categories, and other information surrounding the achievement system

| Type | Name | Description |
| :--- | :--- | :--- |
| \_\_[_achievement_](../data-types/datatype-achievement.md)\_\_ | **Achievement\[**\#\|_Name_**\]** | Find an achievement by its ID or by its name. |
| [_achievement_](../data-types/datatype-achievement.md)_​_ | **AchievementByIndex\[**\#**\]** | Find an achievement by its _index_. See note about achievement indices [below](tlo-achievement.md#note-about-achievement-indices). |
| \_\_[_int_](../data-types/datatype-int.md)_​_ | **AchievementCount** | The number of achievements in the manager. |
| \_\_[_achievementcat_](../data-types/datatype-achievementcat.md)\_\_ | **Category\[**\#\|_Name_**\]** | Find an achievement category by its id or by its name. |
| \_\_[_achievementcat_](../data-types/datatype-achievementcat.md)\_\_ | **CategoryByIndex\[**\#**\]** | Find an achievement category by its _index_. See note about achievement indices [below](tlo-achievement.md#note-about-achievement-indices). |
| \_\_[_int_](../data-types/datatype-int.md)\_\_ | **CategoryCount** | The number of achievement categories in the manager. |
| \_\_[_int_](../data-types/datatype-int.md)\_\_ | **Points** | The total number of accumulated achievement points. |
| \_\_[_int_](../data-types/datatype-int.md)\_\_ | **CompletedAchievements** | The number of completed achievements. |
| \_\_[_int_](../data-types/datatype-int.md)\_\_ | **TotalAchievements** | The number of available achievements. |
| \_\_[_bool_](../data-types/datatype-bool.md)\_\_ | **Ready** | Indicates that the manager has loaded all achievement data and is ready to be used. |

## Usage <a id="usage"></a>

**Achievement\[**\#**\]** and **Achievement.Achievement\[**\#**\]** are equivalent and are provided for consistency. The primary way to access achievement information should be via id. Achievement IDs are unique and do not change.

To look up an achievement's ID, you can look up an achievement by name, or you can use the Achievements Inspector.

### Examples

In the following example, we will look up an achievement by name, and then print its ID.

{% tabs %}
{% tab title="MQScript" %}
```text
/echo ${Achievement[Master of Claws of Veeshan].ID}
```
{% endtab %}

{% tab title="Lua" %}
```lua
print(mq.TLO.Achievement("Master of Claws of Veeshan").ID())
```
{% endtab %}
{% endtabs %}

In the following example, we will print the completed status of achievement "**Wayfarers Brotherhood Adventurer's Stone \(Various 20+\)**"

{% tabs %}
{% tab title="MQScript" %}
```
/echo ${Achievement[500980300].Completed}
```
{% endtab %}

{% tab title="Lua" %}
```lua
print(mq.TLO.Achievement(500980300).Completed()
```
{% endtab %}
{% endtabs %}

### ‌Note About Achievement Indices

Achievements and categories can be looked up by index. This is significantly faster than looking up by id or name. However, these indices are **not** stable and will change from patch to patch, but they will not change during the session. If an achievement is being utilized in a script many times, it may be more performant to look up an achievement's index \(with its .Index member\) and then use that in subsequent queries.

