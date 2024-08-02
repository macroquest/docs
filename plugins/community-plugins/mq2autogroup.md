# MQ2AutoGroup

## Description

Like it says this will autogroup, or auto accept raid invites from the names you have in your ini. Big thanks to Psycotic for the coding help. And to the other coders who's code i borrowed to try and put this thing together. Hopefully someone finds this plugin semi usefull.

You can find the latest version of MQ2AutoGroup [here](https://macroquest.org/phpBB3/viewtopic.php?f=50&t=13712&hilit=MQ2AutoGroup).

## Commands

`/autogroup [help | on | off \| guild | load | save | add | del | clear | list ]`<br>

* help = list of ingame options
* on = turn plugin on
* off = turn plugin off
* guild = toggles automatic guild/raid invite accept from your guild members
* load = loads options and names from ini file
* (any current unsaved names will be lost)
* save = updates .ini to match current options and names
* add = add a new character name (ex: /autogroup add bubbawar)
* del = delete a character name (ex: /autogroup del 15 , deletes name number 15)
* clear = clears all character names
* list = lists current character names

## INI Entries

`[Settings]`<br>
`AutoGroup=on`<br>
`[Names]`<br>
`Name0=bob`<br>
`Name1=fred`<br>
`Name2=harry`<br>
