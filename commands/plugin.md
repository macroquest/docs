## Syntax

**<span style="color:red">/plugin</span> <span style="color:blue">list</span>**

**<span style="color:red">/plugin</span> <span style="color:blue">name</span> \[<span style="color:blue">load</span> \|
<span style="color:blue">unload</span>\]**

**<span style="color:red">/plugin</span> <span style="color:blue">name</span> \[<span style="color:blue">load</span> \|
<span style="color:blue">unload</span>\] \[<span style="color:blue">noauto</span>\]**

## Description

The plugin command can be used to list all plugins currently loaded, to load a new plugin, or to unload a plugin that is
already loaded.

Loading a plugin will also add an entry to the **\[Plugins\]** section of the
[MacroQuest.ini](../macroquest.ini.md) file. Next time MQ2 is started that plugin will be loaded automatically.  
Likewise, unloading a plugin will remove it from MacroQuest.ini. Using the *noauto* switch prevents this modification to
MacroQuest.ini from occurring.

## Examples

`/plugin list`  
`/plugin mq2melee load`  
`/plugin mq2moveutils unload noauto`

## See Also

-   [MacroQuest2:Plugins](../documentation/macroquest2-plugins.md)
-   [MacroQuest.ini](../macroquest.ini.md)


