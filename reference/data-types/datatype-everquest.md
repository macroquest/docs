---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `everquest`

Data types related to the current EverQuest session.

## Members

| **Type**                         | **Member**                           | **Description** |
| -------------------------------- | ------------------------------------ | --- |
| [_int_](datatype-int.md)         | **CharSelectList**                   | Currently returns the zone ID the character is currently in |
| [_bool_](datatype-bool.md)       | **ChatChannel**[_channelname_]       | Returns TRUE if _channelname_ is joined |
| [_string_](datatype-string.md)   | **ChatChannel**[_#_]                 | Returns the name of chat channel _#_ |
| [_int_](datatype-int.md)         | **ChatChannels**                     | Returns the number of channels currently joined |
| [_string_](datatype-string.md)   | **CurrentUI**                        | return a string representing the currently loaded UI skin |
| [_bool_](datatype-bool.md)       | **Foreground**                       | Returns TRUE if EverQuest is in Foreground |
| [_string_](datatype-string.md)   | **GameState**                        | Shows the current game state. Values: CHARSELECT, INGAME, PRECHARSELECT, UNKNOWN |
| [_int64_](datatype-int64.md)     | **HWND**                             | Window handle. |
| [_bool_](datatype-bool.md)       | **IsDefaultUILoaded**                | returns a bool true or false if the "Default" UI skin is the one loaded |
| [_string_](datatype-string.md)   | **LastCommand**                      | Last command entered |
| [_window_](datatype-window.md)   | **LastMouseOver**                    | Returns the last window you moused over |
| [_string_](datatype-string.md)   | **LastTell**                         | Name of last person to send you a tell |
| [_bool_](datatype-bool.md)       | **LayoutCopyInProgress**             | Returns TRUE if a layoutcopy is in progress and FALSE if not. |
| [_bool_](datatype-bool.md)       | **LClickedObject**                   | Returns TRUE if an object has been left clicked |
| [_string_](datatype-string.md)   | **LoginName**                        | Your station name |
| [_int_](datatype-int.md)         | **MouseX**                           | Mouse's X location |
| [_int_](datatype-int.md)         | **MouseY**                           | Mouse's Y location |
| [_string_](datatype-string.md)   | **Path**                             | Path to the Everquest folder |
| [_int_](datatype-int.md)         | **PID**                              | Your current (Process ID) |
| [_int_](datatype-int.md)         | **Ping**                             | Your current ping |
| [_int_](datatype-int.md)         | **Running**                          | Running time of current MQ2 session, in milliseconds |
| [_int_](datatype-int.md)         | **ScreenMode**                       | Returns the screenmode as an integer, 2 is Normal and 3 is No Windows |
| [_string_](datatype-string.md)   | **Server**                           | Full name of your server |
| [_int_](datatype-int.md)         | **PPriority**                        | Returns the processor priority that Everquest is set to. Values: UNKNOWN, LOW, BELOW NORMAL, NORMAL, ABOVE NORMAL, HIGH, REALTIME |
| [_bool_](datatype-bool.md)       | **ValidLoc**[_coorrdinates_]         | Returns true if the given coordinates are valid. |
| [_int_](datatype-int.md)         | **ViewportX**                        | EverQuest viewport upper left (X) position |
| [_int_](datatype-int.md)         | **ViewportXCenter**                  | EverQuest viewport center (X) position |
| [_int_](datatype-int.md)         | **ViewportXMax**                     | EverQuest viewport lower right (X) position |
| [_int_](datatype-int.md)         | **ViewportY**                        | EverQuest viewport upper left (Y) position |
| [_int_](datatype-int.md)         | **ViewportYCenter**                  | EverQuest viewport center (Y) position |
| [_int_](datatype-int.md)         | **ViewportYMax**                     | EverQuest viewport lower right (Y) position |
| [_string_](datatype-string.md)   | **WinTitle**                         | Titlebar text of the Everquest window. |

## Usage

!!! Example

    You can place the mouse over a window and then run the following command to see the name of the
    window that the mouse is hovering over:
    
    ```
    /echo ${EverQuest.LastMouseOver.Name}
    ```

!!! example

    Using EverQuest.ValidLoc:

    === "MQScript"

        ```
        | Will print TRUE or FALSE if the location is valid
        /echo ${EverQuest.ValidLoc[123 456 789]}
        ```

    === "Lua"

        ```lua
        -- Will print true or false if the location is valid
        print(mq.TLO.EverQuest.ValidLoc("123 456 789")())
        ```
