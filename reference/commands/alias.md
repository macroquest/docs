---
tags:
    - command
---
# /alias

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/alias <aliasname> <command> | [list | reload | <aliasname> delete]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Creates custom command shortcuts. Aliases are saved in MacroQuest.ini and persist between sessions.
<!--cmd-desc-end-->
## Examples

| Command | Description |
| :--- | :--- |
| **/alias /hp /echo My health is ${Me.PctHPs}** | Creates an alias where typing /hp will display your current health percentage |
| **/alias list** | Lists all currently defined aliases |
| **/alias reload** | Reloads all aliases from MacroQuest.ini |
| **/alias** _**aliasname**_ **delete** | Deletes the specified alias |