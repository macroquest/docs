---
tags:
    - datatype
---
# `everquest`

<!--dt-desc-start-->
Data types related to the current EverQuest session.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int CharSelectList
Currently returns the zone ID the character is currently in
///

/// member | bool ChatChannel[channelname]
Returns TRUE if _channelname_ is joined
///

/// member | string ChatChannel[#]
Returns the name of chat channel _#_
///

/// member | int ChatChannels
Returns the number of channels currently joined
///

/// member | string CurrentUI
return a string representing the currently loaded UI skin
///

/// member | bool Foreground
Returns TRUE if EverQuest is in Foreground
///

/// member | string GameState
Shows the current game state. Values: CHARSELECT, INGAME, PRECHARSELECT, UNKNOWN
///

/// member | int64 HWND
Window handle.
///

/// member | bool IsDefaultUILoaded
returns a bool true or false if the "Default" UI skin is the one loaded
///

/// member | string LastCommand
Last command entered
///

/// member | window LastMouseOver
Returns the last window you moused over
///

/// member | string LastTell
Name of last person to send you a tell
///

/// member | bool LayoutCopyInProgress
Returns TRUE if a layoutcopy is in progress and FALSE if not.
///

/// member | bool LClickedObject
Returns TRUE if an object has been left clicked
///

/// member | string LoginName
Your station name
///

/// member | int MaxBGFPS
Maximum background FPS
///

/// member | int MaxFPS
Maximum foreground FPS
///

/// member | int MouseX
Mouse's X location
///

/// member | int MouseY
Mouse's Y location
///

/// member | string Path
Path to the Everquest folder
///

/// member | int PID
Your current (Process ID)
///

/// member | int Ping
Your current ping
///

/// member | int Running
Running time of current MQ2 session, in milliseconds
///

/// member | int ScreenMode
Returns the screenmode as an integer, 2 is Normal and 3 is No Windows
///

/// member | string Server
Full name of your server
///

/// member | int PPriority
Returns the processor priority that Everquest is set to. Values: UNKNOWN, LOW, BELOW NORMAL, NORMAL, ABOVE NORMAL, HIGH, REALTIME
///

/// member | float UiScale
Returns the current UI scale
///

/// member | bool ValidLoc[coorrdinates]
Returns true if the given coordinates are valid.
///

/// member | int ViewportX
EverQuest viewport upper left (X) position
///

/// member | int ViewportXCenter
EverQuest viewport center (X) position
///

/// member | int ViewportXMax
EverQuest viewport lower right (X) position
///

/// member | int ViewportY
EverQuest viewport upper left (Y) position
///

/// member | int ViewportYCenter
EverQuest viewport center (Y) position
///

/// member | int ViewportYMax
EverQuest viewport lower right (Y) position
///

/// member | string WinTitle
Titlebar text of the Everquest window.
///
<!--dt-members-end-->

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
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[string]: datatype-string.md
[window]: datatype-window.md
[worldlocation]: datatype-worldlocation.md
<!--dt-linkrefs-end-->
