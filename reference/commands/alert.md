---
tags:
    - command
---
# /alert

## Syntax

**/alert { add | remove | clear | list }** _#list_ **[** _Spawn Search_ **]**

## Description

Used to manipulate alert lists which "watch" for spawns. Uses [Spawn Search](../general/spawn-search.md).

## Options

| Option | Description |
|--------|-------------|
| `add | remove` | Adds or removes spawn search item from alert list |
| `clear` | Clear all entries from the specified alert list |
| `list` | Display all entries in the specified alert list |

## Spawn Search

Any valid [Spawn Search](../general/spawn-search.md) parameter can be used. Common examples include:

| Parameter | Description | Example |
|-----------|-------------|----------|
| `pc|npc|corpse|any` | Basic spawn types | `npc` |
| `class <classname>` | Class name (use long name) | `class warrior` |
| `race <racename>` | Race name | `race troll` |
| `radius #` | Search radius around you | `radius 100` |
| `zradius #` | Vertical (Z-axis) radius | `zradius 50` |
| `range <lower> <upper>` | Level range to search | `range 30 35` |
| `name <name>` | Name to search for | `name Fippy` |
| `id #` | Specific spawn ID | `id 1234` |

## Examples

| Command | Description |
|---------|-------------|
| `/alert add 1 "Lady Vox"` | Adds Lady Vox to alert list 1 |
| `/alert add 1 npc class warrior radius 100` | Alerts on warrior NPCs within 100 radius |
| `/alert add 2 npc race iksar range 30 35` | Alerts on iksar NPCs between levels 30-35 |
| `/alert add 3 named radius 200` | Alerts on named mobs within 200 radius |
| `/alert clear 1` | Clears all members from alert list 1 |
| `/alert list 1` | Lists all members of alert list 1 |
| `/alert remove 1 id 1234` | Removes the entry in alert list 1 for spawn ID 1234 |

See [Spawn Search](../general/spawn-search.md) for a complete list of available search parameters.
