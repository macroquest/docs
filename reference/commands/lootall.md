---
tags:
    - ref
    - slash
---
# /lootall

## Syntax

**/lootall**

## Description

* **/lootall** allows you to loot everything on the corpse that is _not_ No Trade. You must manually loot those unless

  you have [/lootnodrop](../commands/eq/lootnodrop.md) set to never.

* Using **/lootall** will loot _everything_ on the corpse automatically unless there is more than one No Trade item on

  it. In this case, you will have to loot everything (including the item\(s\) that are not No Trade) manually.

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
