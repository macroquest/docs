---
tags:
   - command
---
# /mqchat

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/mqchat [reset | ui | autoscroll {on|off} | NoCharSelect {on|off} | SaveByChar {on|off}]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Configure and manage mqchatwnd's settings.
<!--cmd-desc-end-->
## Options

- **reset**: Resets window and INI settings.
- **ui**: A UI to configure settings.
- **autoscroll {on|off}**: By default set to on, this automatically scrolls to the bottom of the chat window every time a new text line is displayed. If you set this option to off, the chat window will retain your current slider position rather than automatically scroll to the bottom.
- **NoCharSelect {on|off}**: By default set to off, this displays the chat window at the character select screen. If you set this option to on, the chat window will only display when you have entered or re-entered the world.
- **SaveByChar {on|off}**: By default set to on, this creates a new INI entry for every character that you log in so that each character uses its own window position and settings. If you set this option to off, a single [Default] section will be created and all characters will use the same window position and settings.
