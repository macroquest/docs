---
tags:
    - command
---
# /plugin

## Syntax

**/plugin** _name_ **[ load | unload | toggle ] [noauto] | [list]**

## Description

The plugin command can be used to list all plugins currently loaded, to load a new plugin, or to unload a plugin that is already loaded. Loading a plugin will also add an entry to the **[Plugins]** section of the [MacroQuest.ini](../../main/macroquest.ini.md) file thereby loading it next session. Using the _noauto_ switch prevents this modification to MacroQuest.ini from occurring.

## Examples

`/plugin list`  

`/plugin mq2melee load`  

`/plugin mq2moveutils unload noauto`
