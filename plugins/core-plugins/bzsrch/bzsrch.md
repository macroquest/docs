---
tags:
   - command
---
# /bzsrch

## Syntax

```eqcommand
/bzsrch [params] [name]
```

## Description

Searches the bazaar for items matching the specified criteria. Parameters mirror the bazaar window.

## Parameters

* **`trader`** *[parameter]* - Filter by trader name or index number
* **`race`** *[parameter]* - Filter by race (e.g. `human`, `"dark elf"`) or index
* **`class`** *[parameter]* - Filter by class (e.g. `warrior`, `"cleric"`) or index  
* **`stat`** *[parameter]* - Filter by primary stat (e.g. `strength`, `"heroic stamina"`) or index
* **`slot`** *[parameter]* - Filter by equipment slot (e.g. `chest`, `ammo`) or index
* **`type`** *[parameter]* - Filter by item type (e.g. `"1h slashing"`, `"2h blunt"`) or index
* **`prestige`** *[true|false]* - Filter prestige items
* **`augment`** *[true|false]* - Filter augmented items
* **`price`** *[low]* *[high]* - Price range filter
* **[name]** - Item name or partial name (use quotes for "multi word names")

## Examples

```text
/bzsrch class Bard "lute of the howler"
```
You can string together multiple parameters, like this:
```text
/bzsrch class "shadow knight" race Human stat "heroic stamina"
``` 