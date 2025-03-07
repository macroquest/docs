---
tags:
    - command
---
# /cast

## Syntax

```eqcommand
/cast [ list | <"spellname"> | item <"itemname"> ] [ loc <x y z> ]
```

## Description

MacroQuest adds additional functionality to EverQuest's `/cast #` (gem number) command: cast by spell name, use items that have a "click" spell effect, and cast splash spells at a specific location.

## Options

- **list** - List of spells currently memorized and their gems
- **"spellname"** - Name or partial name of the spell to cast (case-insensitive). Quotes required for multi-word names.
- **item "itemname"** - Name of an item with an activated click effect. The item must be in your inventory.
- **loc x y z** - For splash-type spells only: Casts at specified coordinates (uses target's location if omitted)

## Examples

```text
/cast "Complete Healing"
/cast 1
/cast item "mana robe"
/cast list
/cast "Reforming Splash" loc 123 456 789
```

