## Description

This include is ment to help automate defensive measures for various classes.

There is no INI file to go with this, this is simply my version of what each class ought to be doing as each line of
defense goes down.

Currently set up for use with AA, disc's, and BP clicks up to level 105. Currently set up for SK,Pal, and War.

You can find the latest version [posted here](https://macroquest2.com/phpBB3/viewtopic.php?f=49&t=19817)

## Requirements

Spell_Routines.inc

## Usage

Pretty much runs itself, you just need to make a call do it when you want it to engage defensive measures.

Someplace in your main loop/combat loop put some sort of call, for example:

` /if (${Target.Named} || ${Me.XTarget}>2 || ${Me.PctHPs}<60) && ${Target.Distance}<75) /call Defense`

This is set up to work with RaidDruid.mac, so it utilizes a ${ChatChannel} to make announcements if "ReportDefense" is
true/on.

If Defense.inc finds no "ReportDefense" variable, it will make one and default it to FALSE If Defense.inc finds no
"ChatChannel" variable, it will make one and default it to Echo


