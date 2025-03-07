---
tags:
    - command
---
# /lootall

## Syntax

```eqcommand
/lootall
```

## Description

Automatically loots all non-"No Trade" items from corpses. If EverQuest's `/lootnodrop` command is enabled, it will loot all items. Otherwise, single No Trade items leave others lootable, while multiple No Trade items disable auto-looting entirely, requiring manual collection of all items.

## Examples

* **Will loot everything**:

```text
Slot 1: Diamond
Slot 2: Jacinth
Slot 3: No Trade Item
```

* **Will** _not_ **loot everything**:

```text
Slot 1: Diamond
Slot 2: Jacinth
Slot 3: No Trade Item
Slot 4: No Trade Item
```
