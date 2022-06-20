---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Friends`

Grants access to your friends dlist.

## Forms

| **Type** | **Form** | **Description** |
| :--- | :--- | :--- |
| [_friends_](#friends-type) | **Friends** | Access friends data |

## Associated DataTypes

### `friends` Type

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../data-types/datatype-bool.md) | **Friend**[_name_] | Returns TRUE if _name_ is on your friend list |
| [_string_](../data-types/datatype-string.md) | **Friend**[_#_] | Returns the name of friend list member _\#_ |
| [_string_](../data-types/datatype-string.md) | **To String** | Number of friends on your friends list |


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
