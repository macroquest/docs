---
tags:
   - command
---
# /mapclick

## Syntax

```eqcommand
/mapclick [left] {list|<key[+key[...]]> {clear|<command>}}
```

## Description

Define custom commands to execute when clicking on an in-game map object while holding down a specific key combination.

## Options
* `left` - Left-click (default is right-click)
* `list` - List the current mapclicks that have been defined.
* *`key`* can be one or more of the following (multiple keys must be specified with +):
    - ctrl
    - lalt
    - alt (same as lalt)
    - ralt
    - shift

## Default Mapclicks

| Mapclick | Command | Description |
| :--- | :--- | :--- |
| **ctrl** | /maphide id %i | Hides that spawn from the map |
| **lalt** | /highlight id %i | Highlights the clicked spawn |

## Example

```text
/mapclick lalt+shift /mycommand %i
```

When holding down the left alt, shift and then right-clicking a spawn on the map, "/mycommand %i" will be executed.
