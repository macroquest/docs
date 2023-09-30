---
tags:
    - tlo
---
# `Friends`

Grants access to your friends dlist.

## Forms

### {{ renderMember(type='friends', name='Friends') }} 

:   Access friends data


## Associated DataTypes

### {{ renderMember(name='friends') }} 

## Members

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

        | Ech othe name of your first friend
        /echo ${Friends.Friend[1]}
        ```

    === "Lua"

        ```lua
        -- Echo the number of friends that you have
        print(mq.TLO.Friends())

        -- Echo the name of your firsrt friend
        print(mq.TLO.Friends.Friend(1)())
        ```
[string]: ../data-types/datatype-string.md
[bool]: ../data-types/datatype-bool.md
[friends]: #friends-type
