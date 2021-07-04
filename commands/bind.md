## Syntax

**<span style="color:red">/bind</span> \[<span style="color:blue">list</span> \|
<span style="color:blue">eqlist</span>\] \| \[\~\]<span style="color:blue">name</span> \[*keycombo* \|
<span style="color:blue">clear</span>\]**

## Description

Bind a key combination to a specific key.

|                             |                                                        |
|-----------------------------|--------------------------------------------------------|
| **/bind list**              | Lists all MQ2 binds                                    |
| **/bind eqlist**            | Lists all EverQuest binds                              |
| **/bind name *keycombo***   | Binds name to the normal key combination *keycombo*    |
| **/bind \~name *keycombo*** | Binds name to the alternate key combination *keycombo* |
| **/bind name clear**        | Clears the key combination from name                   |
| **/bind \~name clear**      | Clears the alternate key combination from name         |

  
**Note:** *keycombo* can be any combination of "alt", "shift" and "ctrl" plus a key.  

## Examples

|                         |                                                    |
|-------------------------|----------------------------------------------------|
| **/bind forward e**     | Binds the forward command to key e                 |
| **/bind \~forward up**  | Binds the forward command to alternate key uparrow |
| **/bind forward clear** | Clears the key used for the forward command        |

**Note:** Changing EQ binds will not immediately update the display in the options window. Change the bind list
selection in the options window to see the updated keys.

## See Also

-   [Slash_Commands](slash-commands.md)
-   [/custombind](custombind.md)
-   [/dumpbinds](dumpbinds.md)


