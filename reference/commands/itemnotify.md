---
tags:
    - command
---
# /itemnotify

## Syntax

**/itemnotify [** _slotname_ **|** _#_ **|** **in** _bag_ _slot#_ **|** _itemname_ **]** _notification_

## Description

Simulates inventory interactions. Similar to [/click](click.md) without the mouse click.

## Parameters

* _slotname_ - any one of the equipment [Slot Names](../../reference/general/slot-names.md).
* _#_ - any slot number.
* **in** _bag_ _slot#_ - can be pack1-pack8 or bank1-bank24, followed by a slot number.
    - *Not supported: sharedbank, trade slots*
* _itemname_ - first match in inventory
* _notification_ can be any one of the following:

| Notification        | Action                              |
|---------------------|-------------------------------------|
| leftmouseup         | Left click (press + release)        |
| leftmouseheld       | Left mouse hold                     |
| leftmouseheldup     | Release after left hold             |
| rightmouseup        | Right click (press + release)       |
| rightmouseheld      | Right mouse hold                    |
| rightmouseheldup    | Release after right hold  

## Examples

Exchange the item in slot1 of pack8 with the item in your main hand:

```text
 /itemnotify in pack8 1 leftmouseup
 /itemnotify mainhand leftmouseup
 /itemnotify in pack8 1 leftmouseup
```

Right-click your Shrunken Goblin Skull Earring:

```text
 /itemnotify "Shrunken Goblin Skull Earring" rightmouseup
```
