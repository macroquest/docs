# Getting Started

## Starting/Stopping

Once you have [built](building.md) MQ successfully, you can launch it by changing to the Releases directory and opening [MacroQuest.exe](./macroquest-launcher.md). It doesn't matter if MQ is started while EverQuest is running or not.

If you do start it after you start EverQuest, you will have to wait a few seconds before it finishes loading and you see the results in-game.

MQ can be stopped from within game, by typing [/unload](../reference/commands/unload.md). If you are running multiple sessions, you will have to do this in each session. After unloading, you can close the tray icon by right-clicking on it and chosing Exit.

### Multiple Sessions

MacroQuest becomes part of EverQuest when you play, and anything you do inside one session is physically and logically separate from all others (just like your two copies of EverQuest dont blend together). This means that if you load a plugin in one session, it's not going to automatically load in the other. However, when you load a plugin, it will automatically load the next time a MacroQuest session begins. If that happens to be a second EQ session launching, then it may appear to your untrained eye as applying the plugin loading to all running sessions. Likewise, if you run a macro in one session, it's not going to automatically load in others. And if you run a command in one session, it's not going to automatically run in others.

## EQ Commands that are enhanced

The following common EverQuest slash commands are enhanced by MacroQuest:

* [/cast](../reference/commands/cast.md)
* [/char](../reference/commands/char.md)
* [/help](../reference/commands/help.md)
* [/location](../reference/commands/location.md)
* [/target](../reference/commands/mqtarget.md)
* [/who](../reference/commands/who.md)
* [/whotarget](../reference/commands/whotarget.md)

A full list is available in the [Slash Commands](../reference/commands/) page.

## MQ-only Commands

The following commonly used slash commands are added by MacroQuest:

* [/destroy](../reference/commands/destroy.md)
* [/drop](../reference/commands/drop.md)
* [/echo](../reference/commands/echo.md)
* [/face](../reference/commands/face.md)
* [/identify](../reference/commands/identify.md)
* [/itemtarget](../reference/commands/itemtarget.md)
* [/macro](../reference/commands/macro.md)
* [/memspell](../reference/commands/memspell.md)
* [/mqfont](../plugins/core-plugins/chatwnd/mqfont.md)
* [/mqpause](../reference/commands/mqpause.md)
* [/multiline](../reference/commands/multiline.md)
* [/popup](../reference/commands/popup.md)
* [/plugin](../reference/commands/plugin.md)
* [/ranged](../reference/commands/ranged.md)
* [/skills](../reference/commands/skills.md)
* [/whofilter](../reference/commands/whofilter.md)
* [/unload](../reference/commands/unload.md)

A full list is available on the [Slash Commands](../reference/commands/) page.

## MacroQuest.ini

* [NamingSpawn](features/namingspawn.md) Article about manipulating the ini

## Macros, Plugins, and Lua

### Macros

You can load a macro with the following command:

`/macro <arguments>` e.g. `/macro autobot`

To end a macro, use this command:

`/endmacro`

See the [Getting Started](../macros/getting-started.md) section for further information on macros, and [/macro](../reference/commands/macro.md) and [/endmacro](../reference/commands/endmacro.md) for starting and stopping.

### Plugins

MQ plugins are modular and can be loaded and unloaded on demand.

To load a plugin, type:

`/plugin`
`eg. /plugin mq2melee`

To unload a plugin:

`/pluginunload`
`eg. /plugin mq2melee unload`

See the [Plugins](../plugins/README.md) section for further information on plugins, and [/plugin](../reference/commands/plugin.md) for starting and stopping.

### Lua

You can start a Lua script with the following command:

`/lua run <arguments>` e.g. `/lua run eval`

You can stop a Lua script with the following command:

`/lua stop <arguments>` e.g. `/lua stop eval`

Lua is a more advanced scripting language than Macros, and is capable of running multiple scripts simultaneously.

For more information on Lua, see the [Lua](../lua/README.md) page.

## Custom UIs

The EverQuest UI can also be enhanced through the use of MQ2 information. Things like your Target's level and class can be added to your Target Window, buff timers to your Buffs Window and other stats like mana regen, HP regen, Accuracy and Strikethrough to your Player Window.

See the [Custom UIs](./features/custom-uis.md) page for further information on what you can add, and how to do so.

## HUDs

MacroQuest can enable a custom Heads Up Display to show almost any kind of data on top of your UI. Instructions for configuration as well as further information can be found on the [HUD](../plugins/core-plugins/hud/) page.

## CFG Files

See the [CFG Files](./features/cfg-files.md) section for further information.

## Troubleshooting

* \*\*I don't see anything on the map, even though I compiled with no errors and I can see other MQ2 windows like the

  Chat window.\*\*

You need to load the [Map](../plugins/core-plugins/map/) plugin using the command "/plugin Map" in-game.

* **When you execute /mapfilter with any options, all layers that were previously visible disappear.**

Krust UI issue, or bad mapfilter options.

* \*\*With MQ2 running, Monk's "Projection" ability cannot be seen and its title (xxxxxx's projection) is also not

  displayed\*\*

Use /showpet command to disable the pet filter.

