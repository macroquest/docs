---
tags:
    - tlo
---
# `Friends`

<!--tlo-desc-start-->
Grants access to your friends dlist.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='friends', name='Friends') }}

:   Access friends data
<!--tlo-forms-end-->

## datatype `friends`

### {{ renderMember(type='bool', name='Friend', params='name') }}

:   Returns TRUE if _name_ is on your friend list

### {{ renderMember(type='string', name='Friend', params='#') }}

:   Returns the name of friend list member _\#_

### [string][string] `To String`

:   Number of friends on your friends list



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
[friends]: #datatype-friends
<!--tlo-linkrefs-end-->
