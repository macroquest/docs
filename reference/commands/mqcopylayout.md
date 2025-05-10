---
tags:
    - command
---
# /mqcopylayout

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/mqcopylayout <charname> <server> [res:<W>x<H>] [nohot] [noload] [nosoc] [none]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Intelligent copying of EverQuest's UI layout. By default copies all options (hotbuttons, loadouts, socials) using the windowed resolution.
<!--cmd-desc-end-->
## Options


- _charname_ - Name of the character whose UI to copy
- _server_ - Server shortname where character exists
- **[res:**_W_**x**_H_**]** - Specific resolution to copy (if exists in UI INI)
- **nohot** - Exclude hotbuttons
- **noload** - Exclude loadouts
- **nosoc** - Exclude socials
- **none** - Exclude all options (equivalent to nohot+noload+nosoc)


## Examples

`/mqcopylayout bobby vox`

Copies everything including hotbuttons, loadouts, and socials using windowed resolution

`/mqcopylayout bobby vox nohot`

Copies layout excluding hotbuttons

`/mqcopylayout bobby vox nohot noload`

Copies layout excluding hotbuttons and loadouts

`/mqcopylayout bobby vox nohot noload nosoc`

Copies layout excluding hotbuttons, loadouts, and socials

`/mqcopylayout bobby vox none`

Same as above (excludes all options)

`/mqcopylayout bobby vox res:1600x900`

Copies layout for specific 1600x900 resolution (if exists)