# MacroQuest.ini

## Overview

MacroQuest.ini is the configuration file used by MacroQuest. By default it is stored in the config folder in your MacroQuest directory. Many settings can be configured via a GUI with the [/mqsettings](../reference/commands/mqsettings.md) command.

## INI Sections

### [MacroQuest]

!!! example "[MacroQuest]"
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
    NetworkPeerPort=7781
    ```

### [Crash Handler]

!!! example "[Crash Handler]"
    ```ini
    [Crash Handler]
    EnableCrashSubmissions=1
    ```

### [Aliases]

!!! example "[Aliases]"
    The `/yes` and `/no` aliases are created to accept and decline in-game dialogs, and the `/tloc` alias is created to show the location of the target.
    ```ini
    [Aliases]
    /tloc=/echo ${If[${Target.ID},${Target.DisplayName}'s Location is ${Target.Y} ${Target.X} ${Target.Z},You do not have a target!]}
    /yes=/multiline ; /squelch /notify LargeDialogWindow LDW_YesButton leftmouseup ; /squelch /notify LargeDialogWindow LDW_OKButton leftmouseup ; /squelch /notify ConfirmationDialogBox CD_Yes_Button leftmouseup ; /squelch /notify ConfirmationDialogBox CD_OK_Button leftmouseup ; /squelch /notify TradeWND TRDW_Trade_Button leftmouseup ; /squelch /notify GiveWnd GVW_Give_Button leftmouseup ; /squelch /notify ProgressionSelectionWnd ProgressionTemplateSelectAcceptButton leftmouseup ; /squelch /notify TaskSelectWnd TSEL_AcceptButton leftmouseup ; /squelch /notify RaidWindow RAID_AcceptButton leftmouseup
    /no=/multiline ; /squelch /notify LargeDialogWindow LDW_NoButton leftmouseup ; /squelch /notify ConfirmationDialogBox CD_No_Button leftmouseup ; /squelch /notify ConfirmationDialogBox CD_Cancel_Button leftmouseup ; /squelch /notify TradeWND TRDW_Cancel_Button leftmouseup ; /squelch /notify GiveWnd GVW_Cancel_Button leftmouseup ; /squelch /notify ProgressionSelectionWnd ProgressionTemplateSelectCancelButton leftmouseup ; /squelch /notify TaskSelectWnd TSEL_DeclineButton leftmouseup ; /squelch /notify RaidWindow RAID_DeclineButton leftmouseup
    ```

### [Plugins]

!!! example "[Plugins]"
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

!!! example "[Key Binds]"
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

!!! example "[Internal]"
    ```ini
    [Internal]
    SpawnedProcess=aSdFOgl.exe
    ```

### [Caption Colors]

!!! example "[Caption Colors]"
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

!!! example "[FrameLimiter]"
    ```ini
    [FrameLimiter]
    Enable=1
    RenderInBackground=0
    SaveByChar=1
    ```

### [Overlay]

!!! example "[Overlay]"
    ```ini
    [Overlay]
    EnableViewports=0
    CursorAttachment=1
    ```

### [AchievementsInspector]

!!! example "[AchievementsInspector]"
    ```ini
    [AchievementsInspector]
    ShowCategories=1
    ShowOpen=1
    ShowLocked=1
    ShowCompleted=1
    ShowHidden=1
    ```

### [Console]

!!! example "[Console]"
    ```ini
    [Console]
    PersistentCommandHistory=1
    ```

### [NetworkPeers]

!!! example "[NetworkPeers]"
    ```
    [NetworkPeers]
    192.168.4.5=0
    192.168.4.6=8177
    ```