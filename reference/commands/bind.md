---
tags:
    - command
---
# /bind

## Syntax

**/bind [~]**_name_ **[** _keycombo_ **| clear] | [list | eqlist]**

## Description

Bind a key combination to a specific key.

|  |  |
| :--- | :--- |
| **/bind list** | Lists all MQ binds |
| **/bind eqlist** | Lists all EverQuest binds |
| **/bind** _name_ _keycombo_ | Binds name to the normal key combination _keycombo_ |
| **/bind ~**_name_ _keycombo_ | Binds name to the alternate key combination _keycombo_ |
| **/bind** _name_ **clear** | Clears the key combination from name |
| **/bind ~**_name_ **clear** | Clears the alternate key combination from name |

**Note:** _keycombo_ can be any combination of "alt", "shift" and "ctrl" plus a key.

## Examples

|  |  |
| :--- | :--- |
| **/bind forward e** | Binds the forward command to key e |
| **/bind ~forward up** | Binds the forward command to alternate key uparrow |
| **/bind forward clear** | Clears the key used for the forward command |

**Note:** Changing EQ binds will not immediately update the display in the options window. Change the bind list selection in the options window to see the updated keys.
