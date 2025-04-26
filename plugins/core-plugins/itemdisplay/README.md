---
tags:
   - plugin
---
# ItemDisplay

This plugin shows spell information and item data in their respective display windows. It can also show custom notes. 

## Commands

{{ embedCommand('plugins/core-plugins/itemdisplay/itemdisplay.md') }}
{{ embedCommand('plugins/core-plugins/itemdisplay/inote.md') }}

## INI File

Settings can be configured via GUI as well with the [mqsettings](../../../reference/commands/mqsettings.md) command.

```ini
[Notes]
; section for item notes
0014905=mushroom makes me feel good
; this is a note I made for the item "Mushroom" id 0014905, which will appear in the item display window. It's helpful to remember this fact! 
[Settings]
LootButton=1
; the loot button is on
LucyButton=1
; the lucy button is on, too
ShowSpellInfoOnSpells=0
; Toggle extra info on the spell window
ShowSpellsInfoOnItems=0
; Toggle extra info on item window
```

## Top-Level Objects

{{ embedMQType('plugins/core-plugins/itemdisplay/tlo-displayitem.md') }}

## Datatypes

{{ embedMQType('plugins/core-plugins/itemdisplay/datatype-displayitem.md') }}
