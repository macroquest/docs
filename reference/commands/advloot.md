---
tags:
    - command
---
# /advloot

## Syntax

```eqcommand
/advloot {personal | shared} {set | <"item name"> | <#index> } <window option> [ <quantity> ]
```

## Description

Extends EverQuest's `/advloot` command to allow control of the advloot window, including item-specific control.


### Personal Loot Window

**Options:**

* `item`, `name`, `loot`, `leave`, `an`, `ag`, `never`

### Shared Loot Window

**Options:**

* `item`, `name`, `status`, `action`, `manage`, `autoroll`, `nd`, `gd`, `no`, `an`, `ag`, `nv`

**Window Commands:**

* `giveto <name> [<quantity>]` - Give to player (must be in group/raid)
* `leave` - Leaves the item on the corpse (Note: to unlock the corpse from timer, ALL items related to that corpse must be looted or left on it)
* `set <option>` - Option from the "Set all to:" combo box. Can be a player name or any of the other names that exist in that combo box

## Examples

| Command | Description |
|---------|-------------|
| `/advloot shared 2 leave` | Leave second item on corpse |
| `/advloot shared "spiderling silk" leave` | Leave first matching silk on corpse |
| `/advloot personal 3 ag` | Set third item to Always Greed |
| `/advloot shared 1 giveto brainiac 10` | Give 10 of first item to brainiac |




