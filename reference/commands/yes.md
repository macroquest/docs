---
tags:
    - command
---
# /yes

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/yes
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Clicks "yes" on in-game dialogues and popups. Technically not a command, this is an [/alias](alias.md) that's included by default.
<!--cmd-desc-end-->
## Examples
Here's what the alias is really doing behind the scenes. From your MacroQuest.ini, 

```ini
/yes=/multiline ; /squelch /notify LargeDialogWindow LDW_YesButton leftmouseup ; /squelch /notify LargeDialogWindow LDW_OKButton leftmouseup ; /squelch /notify ConfirmationDialogBox CD_Yes_Button leftmouseup ; /squelch /notify ConfirmationDialogBox CD_OK_Button leftmouseup ; /squelch /notify TradeWND TRDW_Trade_Button leftmouseup ; /squelch /notify GiveWnd GVW_Give_Button leftmouseup ; /squelch /notify ProgressionSelectionWnd ProgressionTemplateSelectAcceptButton leftmouseup ; /squelch /notify TaskSelectWnd TSEL_AcceptButton leftmouseup ; /squelch /notify RaidWindow RAID_AcceptButton leftmouseup
```

