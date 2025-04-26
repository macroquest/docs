---
tags:
   - command
---
# /mapnames

## Syntax

```eqcommand
/mapnames {target | normal} <option> | reset 
```

## Description

Controls how spawn names are displayed on the map, from minimal information to a very log name with ID#, class, race, level, etc. With no arguments, /mapnames will display the current settings for _target_ and _normal_ (both are set to %N by default).

## Options
*   **target**: Changes the naming scheme of your target only.
*   **normal**: Changes the naming scheme of all spawns except for your target.

!!! note
    It is important to note that names **are not** updated continually (except for your target if the target map filter is on).

* You may use the following _options_ to customize the display string:

| Option | Description                     |
| :----- | :------------------------------ |
| %n     | Default unique name (a_coyote34) |
| %N     | Cleaned up name (a coyote)      |
| %h     | Current HP percentage           |
| %i     | Spawn ID                        |
| %x     | X coordinate                    |
| %y     | Y coordinate                    |
| %z     | Z coordinate                    |
| %R     | Full race name (eg. Dwarf)      |
| %r     | 3-letter race code (eg. DWF)    |
| %C     | Class full name (eg. Shaman)    |
| %c     | 3-letter class code (eg. SHM)   |
| %l     | Level                           |
| %%     | Literal "%" sign                |

## Examples

```text
/mapnames normal [%l %R %C] %N - %h%%
```

Will display all spawns in the following format:

```text
[40 Human Banker] Banker Tawler - 100%
[70 Wood Elf Ranger] BillyBob - 100%
```
