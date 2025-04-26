---
tags:
   - plugin
---
# ChatWnd

An additional window that displays all output from MacroQuest. Anything you type into this window will avoid your character log.

## Commands

{{ embedCommand('plugins/core-plugins/chatwnd/mqchat.md') }}
{{ embedCommand('plugins/core-plugins/chatwnd/style.md') }}
{{ embedCommand('plugins/core-plugins/chatwnd/mqfont.md') }}
{{ embedCommand('plugins/core-plugins/chatwnd/mqmin.md') }}
{{ embedCommand('plugins/core-plugins/chatwnd/mqclear.md') }}
{{ embedCommand('plugins/core-plugins/chatwnd/setchattitle.md') }}

## Configuration

The easiest way to configure ChatWnd is to use [/mqchat ui](mqchat.md) to open the ChatWnd configuration window. Alternately you can configure the window by using the commands listed above, or editing the _MQ2ChatWnd.ini_ file directly.

```text
[Settings]
AutoScroll=on
NoCharSelect=off
SaveByChar=on
```

(*Explanation of these settings can be found in the [mqchat](mqchat.md) command reference.*)

## Key Binding

By default, the chat window has a key bind of `.` (period) and this is handy! Rather than selecting the window with your mouse, you can hit the period key `.` and MQ window will be selected, so you can type a command quickly. This can be modified in [MacroQuest.ini](../../../main/macroquest.ini.md) under `[Key Binds]` via the setting `MQ2CHAT_Nrm=.`
