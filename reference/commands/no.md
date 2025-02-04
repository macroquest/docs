---
tags:
    - command
---
# /no

## Syntax

**/no**

## Description

Clicks "no" on in-game dialogues and popups. Technically not a command, this is an [/alias](alias.md) that's included by default.

## Examples
Here's what the alias is really doing behind the scenes. From your MacroQuest.ini, 

```ini
/no=/multiline ; /squelch /notify LargeDialogWindow LDW_NoButton leftmouseup ; /squelch /notify ConfirmationDialogBox CD_No_Button leftmouseup ; /squelch /notify ConfirmationDialogBox CD_Cancel_Button leftmouseup ; /squelch /notify TradeWND TRDW_Cancel_Button leftmouseup ; /squelch /notify GiveWnd GVW_Cancel_Button leftmouseup ; /squelch /notify ProgressionSelectionWnd ProgressionTemplateSelectCancelButton leftmouseup ; /squelch /notify TaskSelectWnd TSEL_DeclineButton leftmouseup ; /squelch /notify RaidWindow RAID_DeclineButton leftmouseup
```

