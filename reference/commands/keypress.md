---
tags:
    - ref
    - slash
---
# /keypress

## Syntax

**/keypress** _**name**_ **[hold]**

note: /keypress usage outside of a macro is not recommended nor consistent

## Description

Press the key _name_. This is used strictly for keys that are mapped by the EQ client, however /keypress will work with EQ binds as well as MQ2 binds (see [/bind](bind.md)).

/keypress does not actually press the key, it merely emulates the key being pressed, so it will not interfere with typing.

## Examples

### Virtual Keyboard

Example of pressing a virtual keyboard keycombo

```text
 /keypress shift+b            Send the keypress shift+b
 /keypress h                  Send the keypress of the letter h (default EQUI-Keybind this will hail)
 /keypress i                  Send the keypress of the letter i (default EQUI-Keybind this will open inventory)
```

### EQUI-Keybindings

Example using EQUI-Keybindings keypress with in game keybindings (like in options window)

```text
 /keypress jump               Taps the key mapped as the jump key   
 /keypress forward hold       Holds down the mapped forward key 
 /keypress forward            Releases the mapped forward key after /keypress forward hold
 /keypress OPEN_INV_BAGS      Opens all bags
 /keypress HAIL               Do the Hail command
 /keypress NETSTAT            Toggle the NETSTAT indicator (green ping thingy top left)
```

### Send keypress to window

Will type "x" into the active chat window

`/keypress x chat Will type "x" into the active chat window`

## Virtual Keyboard Layout

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Esc | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | Prnt\_Scrn | Scroll\_Lock |  |
| \` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | - | = | Backspace | Insert | Home |
| Tab | Q | W | E | R | T | Y | U | I | O | P | [ | ] | \ | Delete | End |
| Caps\_Lock | A | S | D | F | G | H | J | K | L | ; | ' | Enter |  |  |  |
| Shift | Z | X | C | V | B | N | M | , | . | / | Right\_Shift |  | Up |  | Num\_1 |
| Ctrl | Alt | Space | Right\_Alt | Right\_Ctrl | Left | Down | Right | Num\_0 |  | Num\_Del |  |  |  |  |  |

## EQUI Keybindings List

* Note these are LamahHerders keybindings so what they are set as defaultEQ is different... sowy

```text
EQ Binds
--------------
[AUTORUN] Nrm:R Alt:clear
[JUMP] Nrm:Space Alt:clear
[FORWARD] Nrm:E Alt:Up
[BACK] Nrm:D Alt:Down
[RIGHT] Nrm:F Alt:Right
[LEFT] Nrm:S Alt:Left
[STRAFE_LEFT] Nrm:clear Alt:clear
[STRAFE_RIGHT] Nrm:clear Alt:clear
[MOUSELOOK] Nrm:F12 Alt:clear
[MOUSELOOK_ENGAGE] Nrm:clear Alt:clear
[AUTOPRIM] Nrm:Q Alt:clear
[CONSIDER] Nrm:A Alt:clear
[DUCK] Nrm:C Alt:clear
[HAIL] Nrm:H Alt:clear
[INVENTORY] Nrm:I Alt:clear
[TELL] Nrm:clear Alt:clear
[USE] Nrm:U Alt:clear
[PITCHUP] Nrm:Num_9 Alt:Page_Up
[PITCHDOWN] Nrm:Num_3 Alt:Page_Down
[CENTERVIEW] Nrm:Num_5 Alt:Home
[ZOOMIN] Nrm:Num_7 Alt:Insert
[ZOOMOUT] Nrm:Num_1 Alt:Delete
[TOGGLECAM] Nrm:F9 Alt:clear
[FULLSCREEN] Nrm:F10 Alt:clear
[TARGETME] Nrm:F1 Alt:clear
[PARTY1] Nrm:F2 Alt:clear
[PARTY2] Nrm:F3 Alt:clear
[PARTY3] Nrm:F4 Alt:clear
[PARTY4] Nrm:F5 Alt:clear
[PARTY5] Nrm:F6 Alt:clear
[TARGETPC] Nrm:F7 Alt:clear
[CYCLEPCTARGETS] Nrm:clear Alt:clear
[TARGETNPC] Nrm:F8 Alt:clear
[CYCLENPCTARGETS] Nrm:Tab Alt:clear
[TARGETCORPSE] Nrm:clear Alt:clear
[CYCLECORPSETARGETS] Nrm:clear Alt:clear
[NETSTAT] Nrm:F11 Alt:clear
[HOT1_1] Nrm:1 Alt:clear
[HOT1_2] Nrm:2 Alt:clear
[HOT1_3] Nrm:3 Alt:clear
[HOT1_4] Nrm:4 Alt:clear
[HOT1_5] Nrm:5 Alt:clear
[HOT1_6] Nrm:6 Alt:clear
[HOT1_7] Nrm:7 Alt:clear
[HOT1_8] Nrm:8 Alt:clear
[HOT1_9] Nrm:9 Alt:clear
[HOT1_10] Nrm:0 Alt:clear
[HOT1_11] Nrm:- Alt:clear
[HOT1_12] Nrm:= Alt:clear
[HOT2_1] Nrm:clear Alt:clear
[HOT2_2] Nrm:clear Alt:clear
[HOT2_3] Nrm:clear Alt:clear
[HOT2_4] Nrm:clear Alt:clear
[HOT2_5] Nrm:clear Alt:clear
[HOT2_6] Nrm:clear Alt:clear
[HOT2_7] Nrm:clear Alt:clear
[HOT2_8] Nrm:clear Alt:clear
[HOT2_9] Nrm:clear Alt:clear
[HOT2_10] Nrm:clear Alt:clear
[HOT2_11] Nrm:clear Alt:clear
[HOT2_12] Nrm:clear Alt:clear
[HOT3_1] Nrm:clear Alt:clear
[HOT3_2] Nrm:clear Alt:clear
[HOT3_3] Nrm:clear Alt:clear
[HOT3_4] Nrm:clear Alt:clear
[HOT3_5] Nrm:clear Alt:clear
[HOT3_6] Nrm:clear Alt:clear
[HOT3_7] Nrm:clear Alt:clear
[HOT3_8] Nrm:clear Alt:clear
[HOT3_9] Nrm:clear Alt:clear
[HOT3_10] Nrm:clear Alt:clear
[HOT3_11] Nrm:clear Alt:clear
[HOT3_12] Nrm:clear Alt:clear
[HOT4_1] Nrm:clear Alt:clear
[HOT4_2] Nrm:clear Alt:clear
[HOT4_3] Nrm:clear Alt:clear
[HOT4_4] Nrm:clear Alt:clear
[HOT4_5] Nrm:clear Alt:clear
[HOT4_6] Nrm:clear Alt:clear
[HOT4_7] Nrm:clear Alt:clear
[HOT4_8] Nrm:clear Alt:clear
[HOT4_9] Nrm:clear Alt:clear
[HOT4_10] Nrm:clear Alt:clear
[HOT4_11] Nrm:clear Alt:clear
[HOT4_12] Nrm:clear Alt:clear
[HOT5_1] Nrm:clear Alt:clear
[HOT5_2] Nrm:clear Alt:clear
[HOT5_3] Nrm:clear Alt:clear
[HOT5_4] Nrm:clear Alt:clear
[HOT5_5] Nrm:clear Alt:clear
[HOT5_6] Nrm:clear Alt:clear
[HOT5_7] Nrm:clear Alt:clear
[HOT5_8] Nrm:clear Alt:clear
[HOT5_9] Nrm:clear Alt:clear
[HOT5_10] Nrm:clear Alt:clear
[HOT5_11] Nrm:clear Alt:clear
[HOT5_12] Nrm:clear Alt:clear
[HOT6_1] Nrm:clear Alt:clear
[HOT6_2] Nrm:clear Alt:clear
[HOT6_3] Nrm:clear Alt:clear
[HOT6_4] Nrm:clear Alt:clear
[HOT6_5] Nrm:clear Alt:clear
[HOT6_6] Nrm:clear Alt:clear
[HOT6_7] Nrm:clear Alt:clear
[HOT6_8] Nrm:clear Alt:clear
[HOT6_9] Nrm:clear Alt:clear
[HOT6_10] Nrm:clear Alt:clear
[HOT6_11] Nrm:clear Alt:clear
[HOT6_12] Nrm:clear Alt:clear
[HOT7_1] Nrm:clear Alt:clear
[HOT7_2] Nrm:clear Alt:clear
[HOT7_3] Nrm:clear Alt:clear
[HOT7_4] Nrm:clear Alt:clear
[HOT7_5] Nrm:clear Alt:clear
[HOT7_6] Nrm:clear Alt:clear
[HOT7_7] Nrm:clear Alt:clear
[HOT7_8] Nrm:clear Alt:clear
[HOT7_9] Nrm:clear Alt:clear
[HOT7_10] Nrm:clear Alt:clear
[HOT7_11] Nrm:clear Alt:clear
[HOT7_12] Nrm:clear Alt:clear
[HOT8_1] Nrm:clear Alt:clear
[HOT8_2] Nrm:clear Alt:clear
[HOT8_3] Nrm:clear Alt:clear
[HOT8_4] Nrm:clear Alt:clear
[HOT8_5] Nrm:clear Alt:clear
[HOT8_6] Nrm:clear Alt:clear
[HOT8_7] Nrm:clear Alt:clear
[HOT8_8] Nrm:clear Alt:clear
[HOT8_9] Nrm:clear Alt:clear
[HOT8_10] Nrm:clear Alt:clear
[HOT8_11] Nrm:clear Alt:clear
[HOT8_12] Nrm:clear Alt:clear
[HOT9_1] Nrm:clear Alt:clear
[HOT9_2] Nrm:clear Alt:clear
[HOT9_3] Nrm:clear Alt:clear
[HOT9_4] Nrm:clear Alt:clear
[HOT9_5] Nrm:clear Alt:clear
[HOT9_6] Nrm:clear Alt:clear
[HOT9_7] Nrm:clear Alt:clear
[HOT9_8] Nrm:clear Alt:clear
[HOT9_9] Nrm:clear Alt:clear
[HOT9_10] Nrm:clear Alt:clear
[HOT9_11] Nrm:clear Alt:clear
[HOT9_12] Nrm:clear Alt:clear
[HOT10_1] Nrm:clear Alt:clear
[HOT10_2] Nrm:clear Alt:clear
[HOT10_3] Nrm:clear Alt:clear
[HOT10_4] Nrm:clear Alt:clear
[HOT10_5] Nrm:clear Alt:clear
[HOT10_6] Nrm:clear Alt:clear
[HOT10_7] Nrm:clear Alt:clear
[HOT10_8] Nrm:clear Alt:clear
[HOT10_9] Nrm:clear Alt:clear
[HOT10_10] Nrm:clear Alt:clear
[HOT10_11] Nrm:clear Alt:clear
[HOT10_12] Nrm:clear Alt:clear
[HOTPAGE1_1] Nrm:shift+1 Alt:clear
[HOTPAGE1_2] Nrm:shift+2 Alt:clear
[HOTPAGE1_3] Nrm:shift+3 Alt:clear
[HOTPAGE1_4] Nrm:shift+4 Alt:clear
[HOTPAGE1_5] Nrm:shift+5 Alt:clear
[HOTPAGE1_6] Nrm:shift+6 Alt:clear
[HOTPAGE1_7] Nrm:shift+7 Alt:clear
[HOTPAGE1_8] Nrm:shift+8 Alt:clear
[HOTPAGE1_9] Nrm:shift+9 Alt:clear
[HOTPAGE1_10] Nrm:shift+0 Alt:clear
[HOTPAGE2_1] Nrm:clear Alt:clear
[HOTPAGE2_2] Nrm:clear Alt:clear
[HOTPAGE2_3] Nrm:clear Alt:clear
[HOTPAGE2_4] Nrm:clear Alt:clear
[HOTPAGE2_5] Nrm:clear Alt:clear
[HOTPAGE2_6] Nrm:clear Alt:clear
[HOTPAGE2_7] Nrm:clear Alt:clear
[HOTPAGE2_8] Nrm:clear Alt:clear
[HOTPAGE2_9] Nrm:clear Alt:clear
[HOTPAGE2_10] Nrm:clear Alt:clear
[HOTPAGE3_1] Nrm:clear Alt:clear
[HOTPAGE3_2] Nrm:clear Alt:clear
[HOTPAGE3_3] Nrm:clear Alt:clear
[HOTPAGE3_4] Nrm:clear Alt:clear
[HOTPAGE3_5] Nrm:clear Alt:clear
[HOTPAGE3_6] Nrm:clear Alt:clear
[HOTPAGE3_7] Nrm:clear Alt:clear
[HOTPAGE3_8] Nrm:clear Alt:clear
[HOTPAGE3_9] Nrm:clear Alt:clear
[HOTPAGE3_10] Nrm:clear Alt:clear
[HOTPAGE4_1] Nrm:clear Alt:clear
[HOTPAGE4_2] Nrm:clear Alt:clear
[HOTPAGE4_3] Nrm:clear Alt:clear
[HOTPAGE4_4] Nrm:clear Alt:clear
[HOTPAGE4_5] Nrm:clear Alt:clear
[HOTPAGE4_6] Nrm:clear Alt:clear
[HOTPAGE4_7] Nrm:clear Alt:clear
[HOTPAGE4_8] Nrm:clear Alt:clear
[HOTPAGE4_9] Nrm:clear Alt:clear
[HOTPAGE4_10] Nrm:clear Alt:clear
[HOTPAGE5_1] Nrm:clear Alt:clear
[HOTPAGE5_2] Nrm:clear Alt:clear
[HOTPAGE5_3] Nrm:clear Alt:clear
[HOTPAGE5_4] Nrm:clear Alt:clear
[HOTPAGE5_5] Nrm:clear Alt:clear
[HOTPAGE5_6] Nrm:clear Alt:clear
[HOTPAGE5_7] Nrm:clear Alt:clear
[HOTPAGE5_8] Nrm:clear Alt:clear
[HOTPAGE5_9] Nrm:clear Alt:clear
[HOTPAGE5_10] Nrm:clear Alt:clear
[HOTPAGE6_1] Nrm:clear Alt:clear
[HOTPAGE6_2] Nrm:clear Alt:clear
[HOTPAGE6_3] Nrm:clear Alt:clear
[HOTPAGE6_4] Nrm:clear Alt:clear
[HOTPAGE6_5] Nrm:clear Alt:clear
[HOTPAGE6_6] Nrm:clear Alt:clear
[HOTPAGE6_7] Nrm:clear Alt:clear
[HOTPAGE6_8] Nrm:clear Alt:clear
[HOTPAGE6_9] Nrm:clear Alt:clear
[HOTPAGE6_10] Nrm:clear Alt:clear
[HOTPAGE7_1] Nrm:clear Alt:clear
[HOTPAGE7_2] Nrm:clear Alt:clear
[HOTPAGE7_3] Nrm:clear Alt:clear
[HOTPAGE7_4] Nrm:clear Alt:clear
[HOTPAGE7_5] Nrm:clear Alt:clear
[HOTPAGE7_6] Nrm:clear Alt:clear
[HOTPAGE7_7] Nrm:clear Alt:clear
[HOTPAGE7_8] Nrm:clear Alt:clear
[HOTPAGE7_9] Nrm:clear Alt:clear
[HOTPAGE7_10] Nrm:clear Alt:clear
[HOTPAGE8_1] Nrm:clear Alt:clear
[HOTPAGE8_2] Nrm:clear Alt:clear
[HOTPAGE8_3] Nrm:clear Alt:clear
[HOTPAGE8_4] Nrm:clear Alt:clear
[HOTPAGE8_5] Nrm:clear Alt:clear
[HOTPAGE8_6] Nrm:clear Alt:clear
[HOTPAGE8_7] Nrm:clear Alt:clear
[HOTPAGE8_8] Nrm:clear Alt:clear
[HOTPAGE8_9] Nrm:clear Alt:clear
[HOTPAGE8_10] Nrm:clear Alt:clear
[HOTPAGE9_1] Nrm:clear Alt:clear
[HOTPAGE9_2] Nrm:clear Alt:clear
[HOTPAGE9_3] Nrm:clear Alt:clear
[HOTPAGE9_4] Nrm:clear Alt:clear
[HOTPAGE9_5] Nrm:clear Alt:clear
[HOTPAGE9_6] Nrm:clear Alt:clear
[HOTPAGE9_7] Nrm:clear Alt:clear
[HOTPAGE9_8] Nrm:clear Alt:clear
[HOTPAGE9_9] Nrm:clear Alt:clear
[HOTPAGE9_10] Nrm:clear Alt:clear
[HOTPAGE10_1] Nrm:clear Alt:clear
[HOTPAGE10_2] Nrm:clear Alt:clear
[HOTPAGE10_3] Nrm:clear Alt:clear
[HOTPAGE10_4] Nrm:clear Alt:clear
[HOTPAGE10_5] Nrm:clear Alt:clear
[HOTPAGE10_6] Nrm:clear Alt:clear
[HOTPAGE10_7] Nrm:clear Alt:clear
[HOTPAGE10_8] Nrm:clear Alt:clear
[HOTPAGE10_9] Nrm:clear Alt:clear
[HOTPAGE10_10] Nrm:clear Alt:clear
[CAST1] Nrm:alt+1 Alt:clear
[CAST2] Nrm:alt+2 Alt:clear
[CAST3] Nrm:alt+3 Alt:clear
[CAST4] Nrm:alt+4 Alt:clear
[CAST5] Nrm:alt+5 Alt:clear
[CAST6] Nrm:alt+6 Alt:clear
[CAST7] Nrm:alt+7 Alt:clear
[CAST8] Nrm:alt+8 Alt:clear
[CAST9] Nrm:alt+9 Alt:clear
[CAST10] Nrm:alt+0 Alt:clear
[CAST11] Nrm:alt+- Alt:clear
[CAST12] Nrm:alt+= Alt:clear
[REPLY] Nrm:T Alt:clear
[CYCLEREPLY] Nrm:Tab Alt:clear
[CYCLEREPLY_BACK] Nrm:shift+Tab Alt:clear
[BACKDROP] Nrm:clear Alt:clear
[TOGGLETARGET] Nrm:clear Alt:clear
[SPELLBOOK] Nrm:ctrl+B Alt:clear
[ABILITIES] Nrm:ctrl+A Alt:clear
[COMBAT] Nrm:ctrl+C Alt:clear
[SOCIALS] Nrm:ctrl+O Alt:clear
[MAIN] Nrm:ctrl+M Alt:clear
[WHO] Nrm:ctrl+W Alt:clear
[INVITE_FOLLOW] Nrm:ctrl+I Alt:clear
[DISBAND] Nrm:ctrl+D Alt:clear
[CAMP] Nrm:ctrl+X Alt:clear
[SIT_STAND] Nrm:ctrl+S Alt:clear
[RUN_WALK] Nrm:ctrl+R Alt:clear
[CLIP_IN] Nrm:shift+- Alt:clear
[CLIP_OUT] Nrm:shift+= Alt:clear
[VOICE_ON] Nrm:Num_Plus Alt:clear
[SCREENCAP] Nrm:Num_Minus Alt:clear
[HISTORY_UP] Nrm:shift+Num_8 Alt:shift+Up
[HISTORY_DOWN] Nrm:shift+Num_2 Alt:shift+Down
[PAGEUP] Nrm:shift+Num_9 Alt:shift+Page_Up
[PAGEDOWN] Nrm:shift+Num_3 Alt:shift+Page_Down
[CMDMODE_SAY] Nrm:clear Alt:clear
[CMDMODE_EMOTE] Nrm:shift+; Alt:clear
[LOCK_WINDOWS] Nrm:clear Alt:clear
[TOGGLE_PLAYERWIN] Nrm:alt+Y Alt:clear
[TOGGLE_PARTYWIN] Nrm:alt+P Alt:clear
[TOGGLE_TARGETWIN] Nrm:alt+T Alt:clear
[TOGGLE_SPELLSWIN] Nrm:alt+S Alt:clear
[TOGGLE_BUFFWIN] Nrm:alt+B Alt:clear
[TOGGLE_HOTBOX1WIN] Nrm:alt+H Alt:clear
[TOGGLE_HOTBOX2WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX3WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX4WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX5WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX6WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX7WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX8WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX9WIN] Nrm:clear Alt:clear
[TOGGLE_HOTBOX10WIN] Nrm:clear Alt:clear
[TOGGLE_CHATWIN] Nrm:clear Alt:clear
[TOGGLE_MAILWIN] Nrm:ctrl+E Alt:clear
[TOGGLE_MAILCOMPWIN] Nrm:ctrl+N Alt:clear
[TOGGLE_MAINMENUWIN] Nrm:alt+M Alt:clear
[TOGGLE_ALTADVWIN] Nrm:V Alt:clear
[TOGGLE_BAZAARWIN] Nrm:alt+I Alt:clear
[RTARGET] Nrm:ctrl+T Alt:clear
[TOGGLE_FRIENDSWIN] Nrm:alt+F Alt:clear
[TOGGLE_PETINFOWIN] Nrm:alt+F1 Alt:clear
[TOGGLE_OPTIONSWIN] Nrm:alt+O Alt:clear
[TOGGLE_HELPWIN] Nrm:clear Alt:clear
[TOGGLE_SELECTORWIN] Nrm:alt+W Alt:clear
[TOGGLE_VIDEOMODEWIN] Nrm:clear Alt:clear
[TOGGLE_BAZAARSEARCHWIN] Nrm:alt+A Alt:clear
[TOGGLE_COMPASSWIN] Nrm:alt+D Alt:clear
[TOGGLE_RAIDWIN] Nrm:alt+R Alt:clear
[TOGGLE_MUSICPLAYERWIN] Nrm:alt+K Alt:clear
[FORWARD_CAM] Nrm:alt+Num_8 Alt:alt+Up
[BACK_CAM] Nrm:alt+Num_2 Alt:alt+Down
[RIGHT_CAM] Nrm:alt+Num_6 Alt:alt+Right
[LEFT_CAM] Nrm:alt+Num_4 Alt:alt+Left
[PITCHUP_CAM] Nrm:alt+Num_9 Alt:alt+Page_Up
[PITCHDOWN_CAM] Nrm:alt+Num_3 Alt:alt+Page_Down
[TOGGLE_JOURNAL] Nrm:alt+J Alt:clear
[TOGGLE_SDBUFFWIN] Nrm:alt+E Alt:clear
[RELEASE_MOUSE_CURSOR] Nrm:shift+alt+R Alt:clear
[TOGGLE_STORYWIN] Nrm:alt+N Alt:clear
[TOGGLE_MAPWIN] Nrm:Backspace Alt:M
[TOGGLE_GUILDMGMTWIN] Nrm:alt+G Alt:clear
[TOGGLE_FELLOWSHIPWIN] Nrm:shift+ctrl+F Alt:clear
[TOGGLE_LFGROUPWIN] Nrm:clear Alt:clear
[TOGGLE_LFGUILDWIN] Nrm:clear Alt:clear
[TOGGLETWOTARGETS] Nrm:clear Alt:clear
[TOGGLE_CONTEXTMENUS] Nrm:clear Alt:clear
[FIRST_PERSON_CAMERA] Nrm:clear Alt:clear
[OVERHEAD_CAMERA] Nrm:clear Alt:clear
[CHASE_CAMERA] Nrm:clear Alt:clear
[USER1_CAMERA] Nrm:clear Alt:clear
[USER2_CAMERA] Nrm:clear Alt:clear
[TETHER_CAMERA] Nrm:clear Alt:clear
[TOGGLE_ADVREQUESTWIN] Nrm:alt+V Alt:clear
[CLOSE_TOP_WINDOW] Nrm:Esc Alt:clear
[CLEAR_TARGET] Nrm:Esc Alt:clear
[CMD_TOGGLE_FIND_WINDOW] Nrm:ctrl+F Alt:clear
[TOGGLE_LEADERSHIPWIN] Nrm:clear Alt:clear
[TOGGLE_TRIBUTEBENEFITWIN] Nrm:alt+U Alt:clear
[CMD_OPENING_ATTACK1] Nrm:ctrl+1 Alt:clear
[CMD_OPENING_ATTACK2] Nrm:ctrl+2 Alt:clear
[CMD_OPENING_ATTACK3] Nrm:ctrl+3 Alt:clear
[CMD_OPENING_ATTACK4] Nrm:ctrl+4 Alt:clear
[CMD_OPENING_ATTACK5] Nrm:ctrl+5 Alt:clear
[CMD_OPENING_ATTACK6] Nrm:ctrl+6 Alt:clear
[CMD_OPENING_ATTACK7] Nrm:ctrl+7 Alt:clear
[CMD_OPENING_ATTACK8] Nrm:ctrl+8 Alt:clear
[CMD_TOGGLE_COMBAT_ABILITY_WIN] Nrm:alt+C Alt:clear
[CMD_TOGGLE_DYNAMIC_ZONE_WIN] Nrm:alt+Z Alt:clear
[CMD_TOGGLE_PVP_LEADERBOARD] Nrm:ctrl+P Alt:clear
[CMD_TOGGLETASKWIN] Nrm:alt+Q Alt:clear
[CMD_TOGGLE_TICKET_WND] Nrm:P Alt:clear
[CMD_STOP_CAST] Nrm:shift+S Alt:clear
[CMD_TOGGLEVOICEWIN] Nrm:clear Alt:clear
[CMD_TOGGLE_TITLE_WND] Nrm:shift+T Alt:clear
[POTION_SLOT_1] Nrm:clear Alt:clear
[POTION_SLOT_2] Nrm:clear Alt:clear
[POTION_SLOT_3] Nrm:clear Alt:clear
[POTION_SLOT_4] Nrm:clear Alt:clear
[TOGGLE_POTION_BELT] Nrm:shift+P Alt:clear
[TOGGLE_BANDOLIER] Nrm:B Alt:clear
[OPEN_INV_BAGS] Nrm:clear Alt:clear
[CLOSE_INV_BAGS] Nrm:clear Alt:clear
[TOGGLE_INV_BAGS] Nrm:shift+B Alt:clear
[TOGGLE_SKILLS_WND] Nrm:clear Alt:clear
[OPEN_ETN_HELP] Nrm:clear Alt:clear
[CMD_TOGGLE_BLOCKEDBUFFWIN] Nrm:clear Alt:clear
[CMD_TOGGLE_AUDIO_TRIGGER_WINDOW] Nrm:clear Alt:clear
[CMD_CLIPBOARD_PASTE] Nrm:ctrl+V Alt:clear
[CMD_OPEN_EQPLAYERS] Nrm:clear Alt:clear
[CMD_TOGGLE_AURAWND] Nrm:shift+A Alt:clear
[CMD_TOGGLE_BLOCKEDPETBUFFWIN] Nrm:clear Alt:clear
[CMD_TOGGLE_REWARD_SELECTION_WIN] Nrm:clear Alt:clear
[CMD_TOGGLE_CLAIM_WIN] Nrm:shift+C Alt:clear
[CMD_TOGGLE_VOICE_BAR] Nrm:clear Alt:clear
[CMD_TOGGLE_AS_LIST] Nrm:clear Alt:clear
[CMD_PUSH_TO_TALK] Nrm:ctrl+Tab Alt:clear
[CMD_PUSH_TO_TALK_SAY] Nrm:clear Alt:clear
[CMD_PUSH_TO_TALK_GROUP] Nrm:clear Alt:clear
[CMD_PUSH_TO_TALK_RAID] Nrm:clear Alt:clear
[CMD_PUSH_TO_TALK_GUILD] Nrm:clear Alt:clear
[CMD_MERCENARIES] Nrm:clear Alt:clear
[CMD_MARKETPLACE] Nrm:clear Alt:clear
[CMD_WELCOMESCREEN] Nrm:clear Alt:clear
[CMD_EXTENDED_TARGET_WINDOW] Nrm:ctrl+alt+T Alt:clear
[CMD_ACHIEVEMENT_WINDOW] Nrm:clear Alt:clear
[TARGET_XTARGET_1] Nrm:clear Alt:clear
[TARGET_XTARGET_2] Nrm:clear Alt:clear
[TARGET_XTARGET_3] Nrm:clear Alt:clear
[TARGET_XTARGET_4] Nrm:clear Alt:clear
[TARGET_XTARGET_5] Nrm:clear Alt:clear
[TARGET_XTARGET_6] Nrm:clear Alt:clear
[TARGET_XTARGET_7] Nrm:clear Alt:clear
[TARGET_XTARGET_8] Nrm:clear Alt:clear
[TARGET_XTARGET_9] Nrm:clear Alt:clear
[TARGET_XTARGET_10] Nrm:clear Alt:clear
[TARGET_XTARGET_11] Nrm:clear Alt:clear
[TARGET_XTARGET_12] Nrm:clear Alt:clear
[TARGET_XTARGET_13] Nrm:clear Alt:clear
[TARGET_XTARGET_14] Nrm:clear Alt:clear
[TARGET_XTARGET_15] Nrm:clear Alt:clear
[TARGET_XTARGET_16] Nrm:clear Alt:clear
[TARGET_XTARGET_17] Nrm:clear Alt:clear
[TARGET_XTARGET_18] Nrm:clear Alt:clear
[TARGET_XTARGET_19] Nrm:clear Alt:clear
[TARGET_XTARGET_20] Nrm:clear Alt:clear
[ADD_XTARGET] Nrm:clear Alt:clear
[REMOVE_XTARGET] Nrm:clear Alt:clear
[CYCLE_XTARGET] Nrm:clear Alt:clear
[REMOVE_XTARGET_BY_SLOT] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_ITEMS_WINDOW] Nrm:shift+I Alt:clear
[CMD_REAL_ESTATE_MANAGE_WINDOW] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_TROPHIES_WINDOW] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_PLOT_SEARCH_WINDOW] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_HELP_WINDOW] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_TOGGLE_MODE] Nrm:shift+Z Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_SET_MODE_COLLISION] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_SET_MODE_WALL] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_SET_MODE_CURSOR] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_SET_MODE_FREE] Nrm:clear Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_RESET_ITEM_MOUSE_X_ROTATION] Nrm:shift+Q Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_RESET_ITEM_MOUSE_Y_ROTATION] Nrm:shift+W Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_RESET_ITEM_WHEEL_ROTATION] Nrm:shift+E Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_RESET_ITEM_SIZE] Nrm:shift+R Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_ROTATE_ITEM_MOUSE_X_ROTATION_90_DEGREES] Nrm:shift+D Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_ROTATE_ITEM_MOUSE_Y_ROTATION_90_DEGREES] Nrm:shift+F Alt:clear
[CMD_REAL_ESTATE_ITEM_PLACEMENT_ROTATE_ITEM_WHEEL_ROTATION_90_DEGREES] Nrm:shift+G Alt:clear
[CMD_REAL_ESTATE_LEAVE] Nrm:clear Alt:clear
[CMD_VOTE_RESULTS] Nrm:shift+V Alt:clear
[CMD_TOGGLE_TCG] Nrm:clear Alt:clear
[CMD_MOVE_DOWN] Nrm:D Alt:clear
[CMD_STOP_ACTION] Nrm:clear Alt:clear
[POTION_SLOT_5] Nrm:clear Alt:clear
[CMD_TOGGLE_ALARM] Nrm:clear Alt:clear
[CMD_TOGGLE_BANK_BAGS] Nrm:clear Alt:clear
[TOGGLE_ZONE_GUIDE_WINDOW] Nrm:clear Alt:clear
[TOGGLE_ZONE_PATH_WINDOW] Nrm:clear Alt:clear
[CMD_MARKETPLACE_SILVER] Nrm:clear Alt:clear
[CMD_MARKETPLACE_GOLD] Nrm:clear Alt:clear
[CMD_HISTORIC_ALERTS] Nrm:shift+H Alt:clear
[CMD_SOCIAL_SHARE] Nrm:shift+ctrl+S Alt:clear
[CMD_TOGGLE_AGGRO] Nrm:clear Alt:clear
[CMD_LOCK_AGGRO] Nrm:clear Alt:clear
[CMD_TOGGLE_BARTER_SEARCH] Nrm:clear Alt:clear
[CMD_OPEN_URL] Nrm:clear Alt:clear
[CMD_TOGGLE_TARGETOFTARGETWIN] Nrm:ctrl+U Alt:clear
[CMD_RAID_DELEGATE_MAIN_ASSIST] Nrm:clear Alt:clear
[CMD_INSPECT_BUFFS] Nrm:clear Alt:clear
[CMD_GROUP_DELEGATE_MARK_NPC] Nrm:clear Alt:clear
[CMD_RAID_DELEGATE_MARK_NPC] Nrm:clear Alt:clear
[CMD_GROUP_MARK_NPC_1] Nrm:clear Alt:clear
[CMD_GROUP_MARK_NPC_2] Nrm:clear Alt:clear
[CMD_GROUP_MARK_NPC_3] Nrm:clear Alt:clear
[CMD_RAID_MARK_NPC_1] Nrm:clear Alt:clear
[CMD_RAID_MARK_NPC_2] Nrm:clear Alt:clear
[CMD_RAID_MARK_NPC_3] Nrm:clear Alt:clear
[CMD_FIND_PC_GROUP_RAID] Nrm:clear Alt:clear
[CMD_TOGGLE_KEYRINGS] Nrm:clear Alt:clear
[CMD_GROUP_DELEGATE_MASTER_LOOTER] Nrm:clear Alt:clear
[CMD_RAID_DELEGATE_MASTER_LOOTER] Nrm:clear Alt:clear
[CMD_TOGGLE_ADVANCED_LOOT_WIN] Nrm:clear Alt:clear
[CMD_TOGGLE_PICKZONE_WIN] Nrm:clear Alt:clear
[CMD_TOGGLE_TASK_OVERLAY_WIN] Nrm:clear Alt:clear
[TOGGLE_FPS] Nrm:F Alt:clear
[TOGGLE_AVATAR] Nrm:Z Alt:clear
[TOGGLE_PETITION] Nrm:G Alt:clear
[TOGGLE_MEMINFO] Nrm:clear Alt:clear
[FLY_UP] Nrm:clear Alt:clear
[FLY_DOWN] Nrm:clear Alt:clear
[ADD_ROUTE] Nrm:clear Alt:clear
[LAY_PPOINT] Nrm:clear Alt:clear
[LAY_LINK] Nrm:clear Alt:clear
[CONFIRM_YES] Nrm:clear Alt:clear
[CONFIRM_NO] Nrm:clear Alt:clear
[TARGET_PREV_NPC] Nrm:clear Alt:clear
[TARGET_NEXT_NPC] Nrm:clear Alt:clear
[ROTATE_STATS] Nrm:ctrl+alt+F Alt:clear
[TOGGLE_NPC_TUNE] Nrm:alt+X Alt:clear
[TOGGLEQAMARKER] Nrm:clear Alt:clear
--------------
End EQ Binds
```
