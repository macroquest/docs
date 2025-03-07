---
tags:
    - command
---
# /mqconsole

## Syntax

```eqcommand
/mqconsole [clear | toggle | show | hide]
```

## Description

Brings up an external MacroQuest console 

## Parameters

- **clear** - Clears the text in the console
- **toggle** - Toggles the window. Good to hotkey.
- **show** - Forces console to appear
- **hide** - Hides the console

## Configuration

INI settings in MacroQuest.ini,
```ini
[MacroQuest]
ShowMacroQuestConsole=1 # Show the console on startup
[Console]
PersistentCommandHistory=1 # Maintain command history between sessions
MaxBufferLines=5000 # Maximum lines kept in scrollback buffer
LocalEcho=1 # Show executed commands in console
```