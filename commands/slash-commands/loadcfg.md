# Loadcfg

## Syntax

**/loadcfg** _**filename**_

## Description

Loads the specified .cfg file.

* Plugins can use LoadCfgFile\(filename\)
* Some cfg files are loaded automatically. You may use /loadcfg to load them at your own desire.
  * **autoexec.cfg**

```text
Executed on the first pulse

-   **charselect.cfg**


Executed when you enter character select

-   **server_character.cfg**


Executed when this *character* on *server* enters the world

-   **mapshortname.cfg**


Executed upon entering the zone *mapshortname*

-   **pluginname-autoexec.cfg**


Executed when this plugin is loaded (after its initialization is complete)
```

## Examples

* **bertox\_mycharacter.cfg**

  Config file that will load for Mycharacter on the Bertox server when she first enters world.

* **oot.cfg, soldungb.cfg, soldunga.cfg, take.cfg**

  Config file that will load when entering a specific zone

[Return to Slash Commands](./)

