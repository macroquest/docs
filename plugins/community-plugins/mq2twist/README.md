# MQ2Twist

## General Details

### Description

MQ2Twist is a plugin for bards which allows them to "twist" a number of songs and/or items together very reliably. It takes care of missed notes and interrupts automatically, and can swap in items to cast too.

This plugin was developed by koad, CyberTech, Cr4zyb4rd and Pheph, and can be downloaded from [here](https://macroquest2.com/phpBB3/viewtopic.php?t=8895) _VIP ACCESS REQUIRED_ it was last edited by Cr4zyb4rd on Wed Jun 21, 2006.

Winnower is the last one to post an updated file but it is user modified and that was on Wed Jul 29, 2015 [here](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=8895&start=465),

**I am unable to find a current stable version. If you happen to find one please update this Wiki.** -\(Description updated by Valendar 6-15-16\)

### Development Notes

For the development history of this plugin see the article [MQ2Twist Revision History](mq2twist-revisions.md)

## Commands

* **/twist \# \# \# \# \#**

Twists the songs/items in the order specified \(up to 10 can be specified\).

Valid options are 1 thru NUM\_SPELL\_GEMS \(EQData.h\) for song gems, and 21 thru 29 for item clicks. These may be mixed in any order, and repeats are allowable. If a song is specified with a duration longer than standard \(eg. Selo's Accelerating Chorus\), that song will be twisted in based on it's duration. For example, riz+mana+selos

`would be a 2 song twist with selos pulsed every 2.5 min.`

* **/twist once \# \# \# \# \#**

Twists in songs once the order given, then reverts back to original twist

* **/twist hold \#**

Pause twisting and sing only the specified song

* **/twist stop/end/off**

Stop twisting, does not clear the twist queue

* **/twist or /twist start**

Resume the twist after using /twist hold or /twist stop

* **/twist reset**

Reset timers for item clicks and long duration songs

* **/twist clear**

Stop twist and clear song list

* **/twist delay \#**

Specify the delay to be used before starting a new song \(in 10ths of a second\). The minimum is 30, default is 33

* **/twist adjust \#**

How early to recast long duration songs \(in ticks\)

* **/twist reload**

Reload the INI file to update item clicks

* **/twist slots**

List the slots/items defined in the INI and their item numbers

* **/twist quiet**

Toggles songs listing and start/stop messages for one-shot twists

* **/sing**

Alias for /twist hold

* **/stoptwist**

Alias for /twist stop

## Top-Level Objects

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Twist}**  

  _Same as ${Twist.Twisting} \(see below\)_

* [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Twist.Twisting}**  

  Returns TRUE if currently twisting, FALSE if not and NULL if plugin not loaded.

* [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Twist.Current}**  

  Returns the current gem being sung, -1 for item or 0 if not twisting

* [_int_](../../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Twist.Next}**  

  Returns the next gem to be sung, -1 for item or 0 if not twisting

* [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) **${Twist.List}**  

  Returns the twist sequence in a format suitable for /twist.

## Examples

`/twist 1 Sing gem 1 forever`  
`/twist 1 2 3 Twist gems 1,2, and 3 forever`  
`/twist 1 2 3 10 Twist gems 1,2,3, and clicky 10, forever`  
`/twist hold 4 Sing gem 4 forever, until another singing-related /twist command is given`  
`/sing 4 Same as above`

/twist set 16 32 120 "Cassindra's Chorus of Clarity" AA

`Set Click_16 to CastTime=32, ReCastTime=120, Name="Cassindra's Chorus of Clarity", Slot=AA ; and save to INI`

## INI File

`[MQ2Twist]`  
`Delay=32 Delay between twists (in 10ths of a second). Lag & System dependant.`  
`Adjust=1 This defines how many ticks before the 'normal'`  
`recast time to cast a long song.`

Long songs are defined as songs greater than 3 ticks in length. If set to 1 tick, and a song lasts 10 ticks, the song will be recast at the 8 tick mark, instead of at the 9 tick mark as it normally would.

`[Click_21] through [Click_29]`  
`CastTime=30 Casting Time, -1 to use the normal song delay`  
`ReCastTime=0 How often to recast, 0 to twist normally.`  
`Name="Fife of Battle" Item name for /itemnotify`  
`Slot=neck Slot name for /itemnotify`

* Delay, CastTime and ReCastTime are specified in 10ths of a second \(so 10 = 1 second\)
* The INI file allows you to specify items by name \(with Name=\), or by inventory slot \(with

  Slot=\).

  * If both a Name and Slot are defined for an item, the plugin will attempt to swap the item into that slot using

    the /exchange command. After casting, it will replace the original item.

  * If only Name or Slot are specified, "[/itemnotify](../../../commands/slash-commands/itemnotify.md) _Slot_ rightmouseup" is used to

    perform item clicks.

### item click method

`MQ2Twist uses /itemnotify slotname rightmouseup to perform item clicks.`

`The INI file allows you to specify items by name (with name=itemname), or by`  
`inventory slot (with slot=slotname). If both a name and slot are defined for an`  
`item, the plugin will attempt to swap the item into that slot (via the /exchange`  
`command) and replace the original item when casting is complete.`  
`````  The example INI file below contains examples of the types of usage.\`

### ini file example

```text
            [MQ2Twist]
            Delay=31
            Quiet=0

            ;Shadowsong cloak
            [Click_21]
            CastTime=30
            ReCastTime=350
            Name=Shadowsong Cloak
            Slot=DISABLED

            ;girdle of living thorns (current belt will be swapped out)
            [Click_22]
            CastTime=0
            ReCastTime=11600
            Name=Girdle of Living Thorns
            Slot=waist

            ;nature's melody
            [Click_23]
            CastTime=-1
            ReCastTime=135
            Name=DISABLED
            Slot=mainhand

            ;lute of the flowing waters
            [Click_24]
            CastTime=0
            ReCastTime=0
            Name=Lute of the Flowing Waters
            Slot=DISABLED

            ;lute of the flowing waters
            [Click_25]
            CastTime=32
            ReCastTime=120
            Name=Cassindra's Chorus of Clarity
            Slot=AA

         [Click_26] ... [Click_30]
            CastTime=33
            ReCastTime=0
            Name=DISABLED
            Slot=DISABLED
```

## See Also

* [Top-Level Objects](../../../data-types-and-top-level-objects/top-level-objects/)
* [Plugins](../../../documentation/macroquest2-plugins.md)

