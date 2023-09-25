---
tags:
    - datatype
---
# `everquest`

Data types related to the current EverQuest session.

## Members

### [int][int] `CharSelectList`

:   Currently returns the zone ID the character is currently in

### [bool][bool] `ChatChannel[channelname]`

:   Returns TRUE if _channelname_ is joined

### [string][string] `ChatChannel[#]`

:   Returns the name of chat channel _#_

### [int][int] `ChatChannels`

:   Returns the number of channels currently joined

### [string][string] `CurrentUI`

:   return a string representing the currently loaded UI skin

### [bool][bool] `Foreground`

:   Returns TRUE if EverQuest is in Foreground

### [string][string] `GameState`

:   Shows the current game state. Values: CHARSELECT, INGAME, PRECHARSELECT, UNKNOWN

### [int64][int64] `HWND`

:   Window handle.

### [bool][bool] `IsDefaultUILoaded`

:   returns a bool true or false if the "Default" UI skin is the one loaded

### [string][string] `LastCommand`

:   Last command entered

### [window][window] `LastMouseOver`

:   Returns the last window you moused over

### [string][string] `LastTell`

:   Name of last person to send you a tell

### [bool][bool] `LayoutCopyInProgress`

:   Returns TRUE if a layoutcopy is in progress and FALSE if not.

### [bool][bool] `LClickedObject`

:   Returns TRUE if an object has been left clicked

### [string][string] `LoginName`

:   Your station name

### [int][int] `MouseX`

:   Mouse's X location

### [int][int] `MouseY`

:   Mouse's Y location

### [string][string] `Path`

:   Path to the Everquest folder

### [int][int] `PID`

:   Your current (Process ID)

### [int][int] `Ping`

:   Your current ping

### [int][int] `Running`

:   Running time of current MQ2 session, in milliseconds

### [int][int] `ScreenMode`

:   Returns the screenmode as an integer, 2 is Normal and 3 is No Windows

### [string][string] `Server`

:   Full name of your server

### [int][int] `PPriority`

:   Returns the processor priority that Everquest is set to. Values: UNKNOWN, LOW, BELOW NORMAL, NORMAL, ABOVE NORMAL, HIGH, REALTIME

### [bool][bool] `ValidLoc[coorrdinates]`

:   Returns true if the given coordinates are valid.

### [int][int] `ViewportX`

:   EverQuest viewport upper left (X) position

### [int][int] `ViewportXCenter`

:   EverQuest viewport center (X) position

### [int][int] `ViewportXMax`

:   EverQuest viewport lower right (X) position

### [int][int] `ViewportY`

:   EverQuest viewport upper left (Y) position

### [int][int] `ViewportYCenter`

:   EverQuest viewport center (Y) position

### [int][int] `ViewportYMax`

:   EverQuest viewport lower right (Y) position

### [string][string] `WinTitle`

:   Titlebar text of the Everquest window.


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
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
