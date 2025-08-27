---
tags:
    - tlo
---
# `Achievement`

<!--tlo-desc-start-->
Provides access to achievements.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='achievement', name='Achievement', params='#|Name') }}

:   Look up an achievement by name or by id.

### {{ renderMember(type='achievementmgr', name='Achievement') }}

:   Access the achievement manager which provides access to information about achievements
<!--tlo-forms-end-->

## Associated DataTypes

## [achievementmgr](../data-types/datatype-achievementmgr.md)
{%
  include-markdown "reference/data-types/datatype-achievementmgr.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-achievementmgr.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-achievementmgr.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-achievementmgr.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}



## Usage

!!! warning
    Looking up achievements by name may not always return the correct achievement if multiple exist with the same name. Achievement IDs should
    be preferred over names as they don't change and are unique.

???+ note "Note About Achievement Indices"

    Achievements and categories can be looked up by index. This is significantly faster than looking up by
    id or name. However, these indices are **not** stable and will change from patch to patch,
    but they will not change during the session.

    If an achievement is being utilized in a script many times, it may be more performant to look up an
    achievement's index (with its .Index member) and then use that in subsequent queries.

    See [Achievement Examples](../data-types/datatype-achievement.md#examples) for some examples of using
    indices for looking up achievements.


**Achievement**[ _#_ ]` and **Achievement.Achievement**[ _#_ ] are equivalent and are provided for consistency. The primary way to access achievement information should be via id. Achievement IDs are unique and do not change.

To look up an achievement's ID, you can look up an achievement by name, or you can use the Achievements Inspector.


### Usage Examples

=== "MQScript"

    ```text
    | Look up an achievement by name, and then print its ID.
    /echo ${Achievement[Master of Claws of Veeshan].ID}

    | print the completed status of achievement
    | "Wayfarers Brotherhood Adventurer's Stone (Various 20+)"
    /echo ${Achievement[500980300].Completed}
    ```

=== "Lua"

    ```lua
    -- Look up an achievement by name, and then print its ID.
    print(mq.TLO.Achievement("Master of Claws of Veeshan").ID())

    -- print the completed status of achievement
    -- "Wayfarers Brotherhood Adventurer's Stone (Various 20+)"
    print(mq.TLO.Achievement(500980300).Completed())
    ```
<!--tlo-linkrefs-start-->
[int]: ../data-types/datatype-int.md
[bool]: ../data-types/datatype-bool.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
[achievementmgr]: ../data-types/datatype-achievementmgr.md
<!--tlo-linkrefs-end-->
