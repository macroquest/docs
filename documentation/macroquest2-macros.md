## Introduction

Macros are essentially scripts that run certain MQ2 commands when certain conditions are met.

As an example, say you want to create a macro that repeatedly casts a certain spell (eg. if you were trying to train up
your Divination skill). The macro could do something like this:

1.  Cast "True North" spell
2.  Check mana and if not enough mana to cast the above spell, sit down and rest until mana is full.
3.  If you have enough mana to cast the spell, then loop back to the beginning.

Macros can also be triggered off of things that happen in game. For example, you can create a macro that waits until
someone says "Heal Me" in group, and then casts a heal on that person.

A snippet is a portion of macro code that can be re-used in lots of different macros. One of the most popular snippets
of code is the spell_routines snippet, which casts a spell reliably (ie. deals with fizzles, target being out of range,
etc). This snippet can be included in many different macros so that all of them benefit from the increased
functionality.

Snippets help keep key pieces of code separate from the main macro, which makes it easier to update portions of big
macros.

**Please Note:** VIP macros and snippets are only available on the VIP forums.

## Finding Macros and Snippets

You can find Macros in the following Forums:

[MQ2::Macros::Macro Depot v3.0](https://macroquest2.com/phpBB3/viewforum.php?f=43)  
[VIP::Macros](https://macroquest2.com/phpBB3/viewforum.php?f=49) (VIP only)

Snippets can be found here:

[MQ2::Macros::Snippets](https://macroquest2.com/phpBB3/viewforum.php?f=45)  
[VIP::Macros](https://macroquest2.com/phpBB3/viewforum.php?f=49) (VIP only). *There's no specific
VIP snippet forum, so all of them are just located in the VIP macro forum.*

## Using Macros or Snippets that you have found

### Macros

Using a macro is simply a matter of copying and pasting the code from the forum into a text file and placing the
resulting file into the Release\\Macros directory.

**Macros with a .mac extension can be run without typing the ".mac". Macros with other extensions require you to type
the extension for the /macro command to work.**

In game, you can run the macro with the following command:

`/macro `<macro_name>

Sometimes macros have additional arguments that you can pass to them when starting. These need to be added to the end of
the /macro line, like so:

`/macro `<macro_name>` 1 2 3`

The main macro post and/or the comments at the top of the macro should tell you how the macro needs to be run.

### Snippets

Just like a macro, a snippet needs to be copied into a text file. Traditionally, snippets have a .inc file extension,
but there are no restrictions as to what the file is called.

To use a snippet, add a line like the following examples, to the top of your macro before the Main sub:

`#include spell_routines.inc`  
`#include wait4rez.inc`

## List of popular Macros and Snippets

<table>
<thead>
<tr class="header">
<th><p>List of non VIP Macros</p></th>
<th><p>List of Non-VIP Snippets/Includes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><a href="../macros/advanced-fishing.md">Advanced Fishing</a> Advanced Fishing macro (adv_fishing.mac)</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=9067">Language Macro</a></li>
<li><a href="../macros/necro-helper.md">Necro Helper</a> Necro Helper (necrohelper.mac)</li>
<li><a href="../macros/rogue-helper.md">Rogue Helper</a> Rogue Helper (RH.mac)</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=7751">Wait4rez.mac</a></li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=6816">YAFM - Yet Another Forage Macro</a></li>
<li><a href="http://www.macroquest2.com/wiki/index.php/Spell_Skill_Trainer">YAST - Yet Another Spell Trainer</a></li>
</ul></td>
<td><ul>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=8655">AdvPath.inc</a> (Pathing and Movement Snippet)</li>
<li><a href="../macros/defense.inc.md">Defense.inc</a> Include file for automating tank defensive measures</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=11022">NinjaLoot.inc</a> (Looting Snippet)</li>
<li><a href="../macros/ninjadvloot.inc.md">Ninjadvloot.inc</a></li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=8964">Skill_Routines.inc</a> (Skill Trainer)</li>
<li><a href="../macros/spell-routines.inc.md">Spell_Routines.inc</a></li>
<li><a href="../macros/wait4rez.inc.md">Wait4Rez.inc</a></li>
</ul></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------------------------------------------------------

<table>
<thead>
<tr class="header">
<th><p>List of VIP Macros</p></th>
<th><p>List of VIP Snippets/ Includes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=11139">Advbot.mac</a> - General purpose macro suitable for all classes</li>
<li><a href="Afcleric.mac_-_nils" title="wikilink">Afcleric.mac - nils</a> - <a href="nils">nils</a> - Cleric Macro</li>
<li><a href="../macros/autobot.mac.md">AutoBot.mac</a> - Very popular macro suitable for all classes</li>
<li><a href="../macros/autobot.mac-v4.28+.md">AutoBot.mac-V4.28+</a> - Another flavor of Raid Druid</li>
<li><a href="../macros/cleric.mac-nytemyst.md">Cleric.mac - nytemyst</a> - Cleric macro written by nytemyst</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=12002">Autoenc.mac</a> - Enchanter Macro</li>
<li><a href="../macros/drshmbot.md">dRShmbot.mac</a> - Shaman Macro</li>
<li><a href="Enchanter.mac_-_nils" title="wikilink">Enchanter.mac - nils</a> - <a href="nils">nils</a> Enchanter Macro</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=12472">Mage.mac</a> - Mage Macro</li>
<li><a href="../macros/modbot.md">ModBot</a> - Another macro suitable for all classes</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=11679">MyCleric.mac</a> - Cleric Macro</li>
<li><a href="Shaman.mac_-_nils" title="wikilink">Shaman.mac - nils</a> - <a href="nils">nils</a> Shaman Macro</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=12763">shambot.mac</a> - Shaman Macro</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=10690">Shaman Slow Macro</a></li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=11765">SimpleBeastlord.mac</a> - Beastlord Macro</li>
<li><a href="http://macroquest2.com/phpBB2/viewtopic.php?t=11766">SimpleWizard.mac</a> - Wizard Macro</li>
<li><a href="Ranger.mac_-_nils" title="wikilink">Ranger.mac - nils</a> - <a href="nils">nils</a> Ranger Macro with Auto Pull</li>
<li><a href="Warrior.mac_-_nils" title="wikilink">Warrior.mac - nils</a> - <a href="nils">nils</a> Warrior Macro</li>
</ul></td>
<td><ul>
<li><a href="../macros/spell-routines.inc.md">Spell_Routines.inc</a></li>
<li><a href="../macros/wait4rez.inc.md">Wait4Rez.inc</a></li>
<li><a href="../macros/quickbeg.inc.md">QuickBeg.inc</a> - Buff Begging snippet</li>
<li><a href="../macros/puller.inc.md">Puller.inc</a> - Include that can use pre-defined paths to pull</li>
<li><a href="GemOpt">GemOpt.inc</a> - Include that manages the usage and optimization of spell gems, as well as memorization</li>
</ul></td>
</tr>
</tbody>
</table>

## Creating your own Macros

Creating your own macro is a rewarding and fun experience, although there is a bit of a learning curve if you've never
scripted before.

See the [Macro Reference](macro-reference.md) for information on how to create your own macros.

## Troubleshooting

See [Help Macros](help-macros.md) for Help and Troubleshooting information.


