---
tags:
   - command
---
# /mapclick

## Syntax

**/mapclick \[ list \|** _**keycombo**_ **\| clear \]** _**command**_

## Description

Allows you to define custom _commands_ to execute when right-clicking with a certain key combination on the in-game map.

* List will show you the current mapclicks that have been defined.
* _Keycombo_ can be one or more of the following \(multiple keys must be specified with +\):
  * ctrl
  * lalt
  * ralt
  * shift
* The default mapclicks are the following:

|  |  |  |
| :--- | :--- | :--- |
| **ctrl** | /maphide id %i | Hides that spawn from the map |
| **lalt** | /highlight id %i | Highlights the clicked spawn |

## Example

```text
/mapclick lalt+shift /mycommand %i
```

When holding down the left alt, shift and then right-clicking a spawn on the map, "/mycommand %i" will be executed.
