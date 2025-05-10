---
tags:
    - command
---
# /loadcfg

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/loadcfg <filename>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Loads the specified .cfg file. To use .cfg files, [see this guide](../../main/features/cfg-files.md).
<!--cmd-desc-end-->
## Notes

* Plugins can use LoadCfgFile(filename)
* Automatic config loading occurs for:

    - **autoexec.cfg** - Executed on first initialization

    - **charselect.cfg** - Runs at character selection screen

    - _server_character_**.cfg** (e.g. `bertox_lordsoth.cfg`) - Character-specific config

    - _mapshortname_**.cfg** (e.g. `oot.cfg`) - Zone-specific config

    - _pluginname_**-autoexec.cfg** (e.g. `MQ2Map-AutoExec.cfg`) - Plugin initialization config


## Examples

* **bertox\_mycharacter.cfg**

  Config file that will load for Mycharacter on the Bertox server when she first enters world.

* **oot.cfg, soldungb.cfg, soldunga.cfg, take.cfg**

  Config file that will load when entering a specific zone

