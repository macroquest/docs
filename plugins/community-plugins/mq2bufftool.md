# MQ2BuffTool

## Description

MQ2BuffTool was written by s0rcier and is found in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?t=11890). This plugin was written a replacement for his previous work, MQ2BuffUtils, offering an easier approach to buff management for the end user and less robotic interaction to be less detectable by others.

## Features

* XML Windows: fully resizable, cloasable, movable, lockable that remember their save location and states
* Buff Window List \(Self & Pet\): sorted by remaining duration on buff, with colorful visual effects \(red=detrimental,

  white=less then 1min, teal=less then 3mins, blue=less then 6mins or green if time left greater then 6mins\), toggle

  option to include songs or not in visual buff list, Buffs Free and Max Slot display and same for Short Duration,

  right or left clicking on the Self Buff window will add or remove buff to the block list

* Block Window List: sorted by buff name, colorful \(green means buff that will always been blocked, white for others\),

  toggle options for On/Off state and popups, Load and Save button to save or load settings, right or left clicking on

  selected buff will increase or decrease \# of free slots attached to it \(if number of free slots reach -1 it will

  remove that blocked buff\)

## Commands

### General

_The following parameters may be used by any of the three primary commands. For example purposes /block will be used._

* '''/block \[ /help \]

Displays help output

* '''/block \[ /load \]

Loads settings and blocked spells list from configuration file.

* '''/block \[ /save \]

Saves settings and blocked spells list to configuration file.

* '''/block \[ /block \]

Toggles scanning for blocked buffs on and off

* '''/block \[ /list \]

Displays a list of spells currently being blocked

* '''/block \[ /popup \]

Toggles display of popup messages

* '''/block \[ /window \]

Popups XML windows

### /block

* \*\*/block \[ \#\# \| -\#\#

  \] \[ _0_ \| _1_ \]\*\*

Blocks spell in buff slot \#\# \(for short duration use slot -\#\#\), always \(0\) or only if free slots/optionally \(1\)

* **/block \[ Name \] \[** _**0**_ **\|** _**1**_ **\]**

Blocks spell matching _Name_ , always \(0\) or only if free slots/optionally \(1\)

* _'/block \[_ setname''&lt;/span&gt; \]

Blocks spells from list _setname_ in configuration file

### /unblock

* \*\*/unblock \[ \#\# \|

  -\#\# \]\*\*

Removes blocked spell in buff slot \#\# \(for short duration use slot -\#\#\)

* **/unblock \[** _**Name**_ **\]**

Removes blocked spell matching _Name_

* **/unblock \[** _**setname**_ **\]**

Removes blocked spells from list _setname_ in configuration file

### /clickoff

* \*\*/clickoff \[ \#\# \|

  -\#\# \]\*\*

Clicks off spell in buff slot \#\# \(for short duration use slot -\#\#\)

* **/unblock \[** _**Name**_ **\]**

Clicks off spell matching _Name_

* **/unblock \[** _**setname**_ **\]**

Clicks off buffs from list _setname_ in configuration file

## Top-Level Object: ${Block}

| **Type** | **Member Name** | **Description** |
| :--- | :--- | :--- |
| [_int_](../../reference/data-types/datatype-int.md) | **Avail\[\***n**\*\]** | Number of free buff slots in _n_ \(where _n_ can be 1=buffs, 2=short duration, 3=pets\) |
| [_int_](../../reference/data-types/datatype-int.md) | **Count** | Number of buffs in blocked list |
| [_int_](../../reference/data-types/datatype-int.md) | **Maxim\[\***n**\*\]** | Number of total buff slots in _n_ \(where _n_ can be 1=buffs, 2=short duration, 3=pets\) |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Popup** | TRUE if popups are enabled |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Quiet** | Always TRUE if plugin is loaded |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Ready** | TRUE if plugin loaded, INGAME, and blocking active |
| [_int_](../../reference/data-types/datatype-int.md) | **Spell\[\***n**\*\]** | Number of available buff slots for _n_ \(where _n_ spell ID or spell name\), returns -1 if none found |
| [_int_](../../reference/data-types/datatype-int.md) | **Total** | Total number of buffs blocked by plugin this session |
| [_string_]() | **To String** | TRUE if INGAME |
