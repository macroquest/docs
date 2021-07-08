# /mqcopylayout

## Syntax

**/mqcopylayout \| opt:** **\(not specifying a res, will default to "Windowed"\)\|** **nohot** **\|** **noload** **\|** **nosoc** **\|** **none \]**

## Description

Uses MQ2 to copy a UI layout.

## Examples

`/mqcopylayout eqmule test`

Will Copy the layout from UI\_eqmule\_test.ini setting including hotbuttons loadouts and socials to your UI. Ok, so the default behaviour is to copy everything. Now if you wish to exclude stuff:

`/mqcopylayout eqmule test nohot`

Will Copy the layout from UI\_eqmule\_test.ini setting including loadouts and socials to your UI but NOT hotbuttons.

`/mqcopylayout eqmule test nohot noload`

Will Copy the layout from UI\_eqmule\_test.ini setting including socials to your UI but NOT hotbuttons and NOT loadouts.

`/mqcopylayout eqmule test nohot noload nosoc`

Will Copy the layout from UI\_eqmule\_test.ini setting excluding hotbuttons loadouts and socials to your UI.

`/mqcopylayout eqmule test none`

Will Copy the layout from UI\_eqmule\_test.ini setting excluding hotbuttons loadouts and socials to your UI.

```/mqcopylayout eqmule test ``res:1600x900```

Will Copy the layout from UI\_eqmule\_test.ini setting including hotbuttons loadouts and socials to your 1600x900 UI \(if that resolution actually exist in your UI ini\).

