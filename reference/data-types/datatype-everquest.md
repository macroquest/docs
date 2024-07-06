---
tags:
    - datatype
---
# `everquest`

Data types related to the current EverQuest session.

## Members

### {{ renderMember(type='int', name='CharSelectList') }} 

:   Currently returns the zone ID the character is currently in

### {{ renderMember(type='bool', name='ChatChannel', params='channelname') }} 

:   Returns TRUE if _channelname_ is joined

### {{ renderMember(type='string', name='ChatChannel', params='#') }} 

:   Returns the name of chat channel _#_

### {{ renderMember(type='int', name='ChatChannels') }} 

:   Returns the number of channels currently joined

### {{ renderMember(type='string', name='CurrentUI') }} 

:   return a string representing the currently loaded UI skin

### {{ renderMember(type='bool', name='Foreground') }} 

:   Returns TRUE if EverQuest is in Foreground

### {{ renderMember(type='string', name='GameState') }} 

:   Shows the current game state. Values: CHARSELECT, INGAME, PRECHARSELECT, UNKNOWN

### {{ renderMember(type='int64', name='HWND') }} 

:   Window handle.

### {{ renderMember(type='bool', name='IsDefaultUILoaded') }} 

:   returns a bool true or false if the "Default" UI skin is the one loaded

### {{ renderMember(type='string', name='LastCommand') }} 

:   Last command entered

### {{ renderMember(type='window', name='LastMouseOver') }} 

:   Returns the last window you moused over

### {{ renderMember(type='string', name='LastTell') }} 

:   Name of last person to send you a tell

### {{ renderMember(type='bool', name='LayoutCopyInProgress') }} 

:   Returns TRUE if a layoutcopy is in progress and FALSE if not.

### {{ renderMember(type='bool', name='LClickedObject') }} 

:   Returns TRUE if an object has been left clicked

### {{ renderMember(type='string', name='LoginName') }} 

:   Your station name

### {{ renderMember(type='int', name='MaxBGFPS') }}

:   Maximum background FPS

### {{ renderMember(type='int', name='MaxFPS') }}

:   Maximum foreground FPS

### {{ renderMember(type='int', name='MouseX') }} 

:   Mouse's X location

### {{ renderMember(type='int', name='MouseY') }} 

:   Mouse's Y location

### {{ renderMember(type='string', name='Path') }} 

:   Path to the Everquest folder

### {{ renderMember(type='int', name='PID') }} 

:   Your current (Process ID)

### {{ renderMember(type='int', name='Ping') }} 

:   Your current ping

### {{ renderMember(type='int', name='Running') }} 

:   Running time of current MQ2 session, in milliseconds

### {{ renderMember(type='int', name='ScreenMode') }} 

:   Returns the screenmode as an integer, 2 is Normal and 3 is No Windows

### {{ renderMember(type='string', name='Server') }} 

:   Full name of your server

### {{ renderMember(type='int', name='PPriority') }} 

:   Returns the processor priority that Everquest is set to. Values: UNKNOWN, LOW, BELOW NORMAL, NORMAL, ABOVE NORMAL, HIGH, REALTIME

### {{ renderMember(type='float', name='UiScale') }}

:   Returns the current UI scale

### {{ renderMember(type='bool', name='ValidLoc', params='coorrdinates') }} 

:   Returns true if the given coordinates are valid.

### {{ renderMember(type='int', name='ViewportX') }} 

:   EverQuest viewport upper left (X) position

### {{ renderMember(type='int', name='ViewportXCenter') }} 

:   EverQuest viewport center (X) position

### {{ renderMember(type='int', name='ViewportXMax') }} 

:   EverQuest viewport lower right (X) position

### {{ renderMember(type='int', name='ViewportY') }} 

:   EverQuest viewport upper left (Y) position

### {{ renderMember(type='int', name='ViewportYCenter') }} 

:   EverQuest viewport center (Y) position

### {{ renderMember(type='int', name='ViewportYMax') }} 

:   EverQuest viewport lower right (Y) position

### {{ renderMember(type='string', name='WinTitle') }} 

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
