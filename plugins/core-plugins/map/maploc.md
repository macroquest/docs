---
tags:
   - command
---
# /maploc

## Syntax

```eqcommand
/maploc <x> <y> [<z>] [options] | [options]
```

## Description

Places a big X on a location or target. Helpful when you're given a loc and want to see it on the map. It's as simple as `/maploc 1 2 3`

## Options

* **size `<10-200>`**  
  Determines size of the X.

* **width `<1-10>`**  
  Determines width of the X.

* **color `<r g b>`**  
  The color of the X.

* **radius `<distance>`**  
  The size of the circle radius around the X.

* **rcolor `<r> <g> <b>`**  
  The color of the radius.

* **`<yloc> <xloc> [<zloc>]`**  
  The location you'd like the X to appear. Z axis is optional.

* **target**  
  Rather than placing the X on a location, this will place it on a target.

* **label `<text>`**  
  Adds a label to the X. Must come at the end of syntax.

* **remove `[<index> | <loc>]`**  
  Removes all X's if no option is passed. Indexes may be found on the map, in the center of each X.

## Examples

* You find a loc on allakhazam, and decide to put a big red X on it:
```bash
/maploc -690 625 -153
```
* If you zoom in on the red X you just made, you can see its index number: 1. Now remove it,
```bash
/maploc remove 1
```
* Return the red X, and label the location with "treasure!"
```bash
/maploc -690 625 -153 label treasure!
```
* Make a very big orange X, with a 100 hot-pink radius ring around it, placed on your current target, labeled "wander"
```bash
/maploc size 200 width 8 radius 100 color 255 128 0 rcolor 255 51 255 target label wander
```
