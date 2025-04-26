---
tags:
   - plugin
---
# CustomBinds

Custom commands that are executed when key combinations are pressed.

You may specify a command for when the key is pressed (down), and another for when it is released (up).

## Commands

{{ embedCommand('plugins/core-plugins/custombinds/custombind.md') }}

## Examples

```
/custombind add crylaugh
/custombind set crylaugh-down /cry
/custombind set crylaugh-up /laugh
/bind crylaugh shift+f
```
