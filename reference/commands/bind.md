---
tags:
    - command
---
# /bind

## Syntax

**/bind [list \| eqlist\] \| \[~\]name \[**_**keycombo**_ **\| clear]**

## Description

Bind a key combination to a specific key.

|  |  |
| :--- | :--- |
| **/bind list** | Lists all MQ2 binds |
| **/bind eqlist** | Lists all EverQuest binds |
| **/bind name** _**keycombo**_ | Binds name to the normal key combination _keycombo_ |
| **/bind ~name** _**keycombo**_ | Binds name to the alternate key combination _keycombo_ |
| **/bind name clear** | Clears the key combination from name |
| **/bind ~name clear** | Clears the alternate key combination from name |

**Note:** _keycombo_ can be any combination of "alt", "shift" and "ctrl" plus a key.

## Examples

|  |  |
| :--- | :--- |
| **/bind forward e** | Binds the forward command to key e |
| **/bind ~forward up** | Binds the forward command to alternate key uparrow |
| **/bind forward clear** | Clears the key used for the forward command |

**Note:** Changing EQ binds will not immediately update the display in the options window. Change the bind list selection in the options window to see the updated keys.
