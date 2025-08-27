---
tags:
    - tlo
---
# `Friends`

<!--tlo-desc-start-->
Grants access to your friends list.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='friend', name='Friends') }}

:   Access friends data
<!--tlo-forms-end-->

## Associated DataTypes

## [friend](../data-types/datatype-friend.md)
{%
  include-markdown "reference/data-types/datatype-friend.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-friend.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-friend.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-friend.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}



## Usage

!!! example

    === "MQScript"

        ```
        | Echo the number of friends that you have
        /echo ${Friends}

        | Echo the name of your first friend
        /echo ${Friends.Friend[1]}
        ```

    === "Lua"

        ```lua
        -- Echo the number of friends that you have
        print(mq.TLO.Friends())

        -- Echo the name of your firsrt friend
        print(mq.TLO.Friends.Friend(1)())
        ```
<!--tlo-linkrefs-start-->
[string]: ../data-types/datatype-string.md
[bool]: ../data-types/datatype-bool.md
[friend]: ../data-types/datatype-friend.md
<!--tlo-linkrefs-end-->
