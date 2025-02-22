---
tags:
    - command
---
# /alias

## Syntax

**/alias** _aliasname_ _command_ **| [list | reload |** _aliasname_ **delete]**

## Description
Creates custom command shortcuts. Aliases are saved in MacroQuest.ini and persist between sessions.

## Examples

| Command | Description |
| :--- | :--- |
| **/alias /hp /echo My health is ${Me.PctHPs}** | Creates an alias where typing /hp will display your current health percentage |
| **/alias list** | Lists all currently defined aliases |
| **/alias reload** | Reloads all aliases from MacroQuest.ini |
| **/alias** _**aliasname**_ **delete** | Deletes the specified alias |