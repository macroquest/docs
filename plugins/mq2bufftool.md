## Description

MQ2BuffTool was written by s0rcier and is found in the VIP forums
[here](https://macroquest2.com/phpBB3/viewtopic.php?t=11890). This plugin was written a replacement for his previous
work, MQ2BuffUtils, offering an easier approach to buff management for the end user and less robotic interaction to be
less detectable by others.

## Features

-   XML Windows: fully resizable, cloasable, movable, lockable that remember their save location and states
-   Buff Window List (Self & Pet): sorted by remaining duration on buff, with colorful visual effects (red=detrimental,
    white=less then 1min, teal=less then 3mins, blue=less then 6mins or green if time left greater then 6mins), toggle
    option to include songs or not in visual buff list, Buffs Free and Max Slot display and same for Short Duration,
    right or left clicking on the Self Buff window will add or remove buff to the block list
-   Block Window List: sorted by buff name, colorful (green means buff that will always been blocked, white for others),
    toggle options for On/Off state and popups, Load and Save button to save or load settings, right or left clicking on
    selected buff will increase or decrease # of free slots attached to it (if number of free slots reach -1 it will
    remove that blocked buff)

## Commands

### General

*The following parameters may be used by any of the three primary commands. For example purposes /block will be used.*

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/help</span> \]

  
Displays help output

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/load</span> \]

  
Loads settings and blocked spells list from configuration file.

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/save</span> \]

  
Saves settings and blocked spells list to configuration file.

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/block</span> \]

  
Toggles scanning for blocked buffs on and off

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/list</span> \]

  
Displays a list of spells currently being blocked

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/popup</span> \]

  
Toggles display of popup messages

-   '''<span style="color:red">/block</span> \[ <span style="color:blue">/window</span> \]

  
Popups XML windows

### /block

-   **<span style="color:red">/block</span> \[ <span style="color:blue">##</span> \| <span style="color:blue">-##</span>
    \] \[ *0* \| *1* \]**

  
Blocks spell in buff slot ## (for short duration use slot -##), always (0) or only if free slots/optionally (1)

-   **<span style="color:red">/block</span> \[ <span style="color:blue">Name</span> \] \[ *0* \| *1* \]**

  
Blocks spell matching *Name* , always (0) or only if free slots/optionally (1)

-   *'<span style="color:red">/block</span> \[ <span style="color:blue">*setname''</span> \]

  
Blocks spells from list *setname* in configuration file

### /unblock

-   **<span style="color:red">/unblock</span> \[ <span style="color:blue">##</span> \|
    <span style="color:blue">-##</span> \]**

  
Removes blocked spell in buff slot ## (for short duration use slot -##)

-   **<span style="color:red">/unblock</span> \[ <span style="color:blue">*Name*</span> \]**

  
Removes blocked spell matching *Name*

-   **<span style="color:red">/unblock</span> \[ <span style="color:blue">*setname*</span> \]**

  
Removes blocked spells from list *setname* in configuration file

### /clickoff

-   **<span style="color:red">/clickoff</span> \[ <span style="color:blue">##</span> \|
    <span style="color:blue">-##</span> \]**

  
Clicks off spell in buff slot ## (for short duration use slot -##)

-   **<span style="color:red">/unblock</span> \[ <span style="color:blue">*Name*</span> \]**

  
Clicks off spell matching *Name*

-   **<span style="color:red">/unblock</span> \[ <span style="color:blue">*setname*</span> \]**

  
Clicks off buffs from list *setname* in configuration file

## Top-Level Object: ${Block}

| **Type**                               | **Member Name**      | **Description**                                                                                     |
|----------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------|
| *[int](../data-types/datatype-int.md)*       | **Avail\[***n***\]** | Number of free buff slots in *n* (where *n* can be 1=buffs, 2=short duration, 3=pets)               |
| *[int](../data-types/datatype-int.md)*       | **Count**            | Number of buffs in blocked list                                                                     |
| *[int](../data-types/datatype-int.md)*       | **Maxim\[***n***\]** | Number of total buff slots in *n* (where *n* can be 1=buffs, 2=short duration, 3=pets)              |
| *[bool](../data-types/datatype-bool.md)*     | **Popup**            | TRUE if popups are enabled                                                                          |
| *[bool](../data-types/datatype-bool.md)*     | **Quiet**            | Always TRUE if plugin is loaded                                                                     |
| *[bool](../data-types/datatype-bool.md)*     | **Ready**            | TRUE if plugin loaded, INGAME, and blocking active                                                  |
| *[int](../data-types/datatype-int.md)*       | **Spell\[***n***\]** | Number of available buff slots for *n* (where *n* spell ID or spell name), returns -1 if none found |
| *[int](../data-types/datatype-int.md)*       | **Total**            | Total number of buffs blocked by plugin this session                                                |
| *[string](../data-types/datatype-string.md)* | **To String**        | TRUE if INGAME                                                                                      |

  
== See Also ==

-   MQ2BuffUtils
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Data Types](../data-types/data-types.md)
-   [Plugins](../documentation/macroquest2-plugins.md)


