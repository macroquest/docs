# MacroQuest.ini

## Overview

MacroQuest.ini is the configuration file used by MacroQuest. By default it is stored in the config folder in your MacroQuest directory.

## INI Sections

### [MacroQuest]

* Example

```ini
[MacroQuest]
MacroQuestWinClassName=__MacroQuestTray
MacroQuestWinName=MacroQuest
ToggleConsoleKey=ctrl+`
BossMode=
CycleNextWindow=
CyclePrevWindow=
ParserEngine=1
ShowMacroQuestConsole=1
```

### [Crash Handler]

* Example

```ini
[Crash Handler]
EnableCrashSubmissions=1
```

### [ItemDisplay]

* Example

```ini
[ItemDisplay]
LootButton=1
LucyButton=1
```

### [Aliases]

* Example

```ini
[Aliases]
/tloc=/echo ${If[${Target.ID},${Target.DisplayName}'s Location is ${Target.Y} ${Target.X} ${Target.Z},You do not have a target!]}
/yes=/multiline ; /squelch /notify LargeDialogWindow LDW_YesButton leftmouseup ; /squelch /notify LargeDialogWindow LDW_OKButton leftmouseup ; /squelch /notify ConfirmationDialogBox CD_Yes_Button leftmouseup ; /squelch /notify ConfirmationDialogBox CD_OK_Button leftmouseup ; /squelch /notify TradeWND TRDW_Trade_Button leftmouseup ; /squelch /notify GiveWnd GVW_Give_Button leftmouseup ; /squelch /notify ProgressionSelectionWnd ProgressionTemplateSelectAcceptButton leftmouseup ;
```

### [Plugins]

* Example

```ini
[Plugins]
; MacroQuest Defaults
mq2autologin=1
mq2bzsrch=1
mq2chatwnd=0
mq2custombinds=1
mq2eqbugfix=1
mq2itemdisplay=1
mq2labels=1
mq2lua=1
mq2map=1
```

### [Key Binds]

* Example

```ini
[Key Binds]
RANGED_Nrm=clear
RANGED_Alt=clear
MQ2CHAT_Nrm=.
MQ2CSCHAT_Nrm=/
NAVKEY_forward_Nrm=W
NAVKEY_forward_Alt=Up
NAVKEY_back_Nrm=S
NAVKEY_back_Alt=Down
NAVKEY_left_Nrm=A
```

### [Internal]

* Example

```ini
[Internal]
SpawnedProcess=aSdFOgl.exe
```

### [Caption Colors]

* Example

```ini
[Caption Colors]
PC=OFF
PC-Color=ff00ff
PCCon=OFF
PCPVPTeam=OFF
PCRaid=OFF
PCRaid-Color=ff7f
PCClass=OFF
```

### [FrameLimiter]

* Example

```ini
[FrameLimiter]
Enable=1
RenderInBackground=0
SaveByChar=1
```

### [Overlay]

* Example

```ini
[Overlay]
EnableViewports=0
CursorAttachment=1
```

### [AchievementsInspector]

* Example

```ini
[AchievementsInspector]
ShowCategories=1
ShowOpen=1
ShowLocked=1
ShowCompleted=1
ShowHidden=1
```

### [Console]

* Example

```ini
[Console]
PersistentCommandHistory=1
```
