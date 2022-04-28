# MacroQuest2:Using

## Starting/Stopping

Once you have [compiled](macroquest-compiling.md) MQ successfully, you can launch it by changing to the Releases directory and opening [MacroQuest.exe](macroquest.exe.md). It doesn't matter if MQ is started while EverQuest is running or not.

If you do start it after you start EverQuest, you will have to wait a few seconds before it finishes loading and you see the results in-game.

MQ can be stopped from within game, by typing [/unload](../commands/slash-commands/unload.md). If you are running multiple sessions, you will have to do this in each session. After unloading, you can close the tray icon by right-clicking on it and chosing Exit.

### Multiple Sessions

MacroQuest becomes part of EverQuest when you play, and anything you do inside one session is physically and logically separate from all others (just like your two copies of EverQuest dont blend together). This means that if you load a plugin in one session, it's not going to automatically load in the other. However, when you load a plugin, it will automatically load the next time a MacroQuest session begins. If that happens to be a second EQ session launching, then it may appear to your untrained eye as applying the plugin loading to all running sessions. Likewise, if you run a macro in one session, it's not going to automatically load in others. And if you run a command in one session, it's not going to automatically run in others.

## EQ Commands that are enhanced

The following common EverQuest slash commands are enhanced by MacroQuest:

* [/cast](../commands/slash-commands/cast.md)
* [/charinfo](../commands/slash-commands/charinfo.md)
* [/help](../commands/slash-commands/help.md)
* [/location](../commands/slash-commands/location.md)
* [/target](../commands/slash-commands/mqtarget.md)
* [/who](../commands/slash-commands/who.md)
* [/whotarget](../commands/slash-commands/whotarget.md)

A full list is available in the [Slash Commands](../commands/slash-commands/) page.

## MQ-only Commands

The following commonly used slash commands are added by MacroQuest2:

* [/destroy](../commands/slash-commands/destroy.md)
* [/drop](../commands/slash-commands/drop.md)
* [/echo](../commands/slash-commands/echo.md)
* [/face](../commands/slash-commands/face.md)
* [/identify](../commands/slash-commands/identify.md)
* [/itemtarget](../commands/slash-commands/itemtarget.md)
* [/macro](../commands/slash-commands/macro.md)
* [/memspell](../commands/slash-commands/memspell.md)
* [/mqfont](../plugins/core-plugins/mq2chatwnd/mqfont.md)
* [/mqpause](../commands/slash-commands/mqpause.md)
* [/multiline](../commands/slash-commands/multiline.md)
* [/popup](../commands/slash-commands/popup.md)
* [/plugin](../commands/slash-commands/plugin.md)
* [/ranged](../commands/slash-commands/ranged.md)
* [/skills](../commands/slash-commands/skills.md)
* [/whofilter](../commands/slash-commands/whofilter.md)
* [/unload](../commands/slash-commands/unload.md)

A full list is available on the [Slash Commands](../commands/slash-commands/) page.

## MacroQuest.ini

* [NamingSpawn](namingspawn.md) Article about manipulating the ini

## Macros and Plugins

### Macros

You can load a macro with the following command:

``/macro`<arguments>``eg. /macro autobot\`

To end a macro, use this command:

`/endmacro`

See the [MacroQuest2:Macros](macroquest-macros.md) section for further information on macros, and [/macro](../commands/slash-commands/macro.md) and [/endmacro](../commands/slash-commands/endmacro.md) for starting and stopping.

### Plugins

MQ plugins are modular and can be loaded and unloaded on demand.

To load a plugin, type:

`/plugin`  
`eg. /plugin mq2melee`

To unload a plugin:

`/pluginunload`  
`eg. /plugin mq2melee unload`

See the [MacroQuest2:Plugins](macroquest-plugins.md) section for further information on plugins, and [/plugin](../commands/slash-commands/plugin.md) for starting and stopping.

## Custom UIs

The EverQuest UI can also be enhanced through the use of MQ2 information. Things like your Target's level and class can be added to your Target Window, buff timers to your Buffs Window and other stats like mana regen, HP regen, Accuracy and Strikethrough to your Player Window.

See the [Custom UIs](custom-uis.md) page for further information on what you can add, and how to do so.

## HUDs

MacroQuest can enable a custom Heads Up Display to show almost any kind of data on top of your UI. Instructions for configuration as well as further information can be found on the [MQ2HUD](../plugins/core-plugins/mq2hud/) page.

## CFG Files

See the [CFG Files](cfg-files.md) section for further information.

## Troubleshooting

* \*\*I don't see anything on the map, even though I compiled with no errors and I can see other MQ2 windows like the

  Chat window.\*\*

You need to load the [MQ2Map](../plugins/core-plugins/mq2map/) plugin using the command "/plugin MQ2Map" in-game.

* **When you execute /mapfilter with any options, all layers that were previously visible disappear.**

Krust UI issue, or bad mapfilter options.

* \*\*With MQ2 running, Monk's "Projection" ability cannot be seen and its title (xxxxxx's projection) is also not

  displayed\*\*

Use /showpet command to disable the pet filter.

