# TLO:Achievement

Provides access to achievements.

## Forms <a id="forms"></a>

| Type | Form | Description |
| :--- | :--- | :--- |
| \_\_[_achievement_](../data-types/datatype-achievement.md)_​_ | **Achievement\[**\#\|_Name_**\]** | Look up an achievement by name or by id. |
| _​_[_achievementmgr_](tlo-achievement.md#alert-type)_​_ | **Achievement** | Access the achievement manager which provides access to information about achievements |

## AchievementMgr Type <a id="alert-type"></a>

Provides access achievements, achievement categories, and other information surrounding the achievement system

<table>
  <thead>
    <tr>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Name</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-achievement.md"><em>achievement</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Achievement[</b>#|<em>Name</em><b>]</b>
        </td>
        <td style="text-align:left">Find an achievement by its ID or by its name.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="../data-types/datatype-achievement.md"><em>achievement</em></a><em>&#x200B;</em>
      </td>
      <td style="text-align:left"><b>AchievementByIndex[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Find an achievement by its <em>index</em>. See note about achievement indices
        <a
        href="tlo-achievement.md#note-about-achievement-indices">below</a>.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-int.md"><em>int</em></a><em>&#x200B;</em>
      </td>
      <td style="text-align:left"><b>AchievementCount</b>
      </td>
      <td style="text-align:left">The number of achievements in the manager.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-achievementcat.md"><em>achievementcat</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Category[</b>#|<em>Name</em><b>]</b>
        </td>
        <td style="text-align:left">
          <p>Find an achievement category by its id or by its name.</p>
          <p></p>
          <p>Note: If searching by name, only top-level categories are returned from
            the achievement manager.</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-achievementcat.md"><em>achievementcat</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>CategoryByIndex[</b>#<b>]</b>
        </td>
        <td style="text-align:left">Find an achievement category by its <em>index</em>. See note about achievement
          indices <a href="tlo-achievement.md#note-about-achievement-indices">below</a>.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-int.md"><em>int</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>CategoryCount</b>
        </td>
        <td style="text-align:left">The number of achievement categories in the manager.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-int.md"><em>int</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Points</b>
        </td>
        <td style="text-align:left">The total number of accumulated achievement points.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-int.md"><em>int</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>CompletedAchievements</b>
        </td>
        <td style="text-align:left">The number of completed achievements.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-int.md"><em>int</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>TotalAchievements</b>
        </td>
        <td style="text-align:left">The number of available achievements.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="../data-types/datatype-bool.md"><em>bool</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Ready</b>
        </td>
        <td style="text-align:left">Indicates that the manager has loaded all achievement data and is ready
          to be used.</td>
    </tr>
  </tbody>
</table>

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

