---
tags:
    - command
---
# /captioncolor

## Syntax

**/captioncolor [list \|"name'' \[off \| on \| \# \# \#\]]**

## Description

Allows you to change the color of the captions that appear above the heads of PCs and NPCs, based on various factors.

**Note:** raid class colors can only be set through the raid options window.

## Settings

Below are the default settings for each of the possible Caption Colors:

|  |  |  |
| :--- | :--- | :--- |
| **Color Type** | **Default Setting** | **Description** |
| PC | OFF | Default color for PCs |
| PCCon | OFF | Color PCs by con color |
| PCPVPTeam | OFF | Color PCs by PVP Team color |
| PCRaid | OFF | Default color for all raid members |
| PCClass | OFF | Color PCs by class (raid settings) |
| PCGroup | OFF | Default color for group members |
| PCTrader | ON | Default color for PC traders: 255 127 0 |
| NPC | OFF | Default color for all NPCs |
| NPCCon | ON | Color NPCs by con color |
| NPCClass | OFF | Color NPCs by class (raid settings) |
| NPCMerchant | ON | Default color for NPC merchants: 255 127 0 |
| NPCBanker | ON | Default color for NPC banker: 200 0 255 |
| NPCAssist | ON | Default color for the main assist NPC: 255 255 0 |
| NPCMark | ON | Default color for marked NPCs: 255 255 0 |
| PetNPC | OFF | Default color for all pets with NPC owners |
| PetPC | OFF | Default color for all pets with PC owners |
| PetClass | OFF | Color pets by class |
| Corpse | OFF | Default color for corpses |
| CorpseClass | OFF | Color corpses by class |

## Examples

`/captioncolor list`  
`/captioncolor pcclass on`  
`/captioncolor pctrader on`  
`/captioncolor pctrader 255 128 0`
