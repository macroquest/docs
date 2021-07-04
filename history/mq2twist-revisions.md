\_\_FORCETOC\_\_

## MQ2Twist Revision History

### htw 10-13-09

`     Added flag in SetGameState() to prevent INI init on zone`

### htw 10-12-09

`     Corrected item swap in index, added a few more info lines if debug mode is on`

### htw 10-10-09

`     Corrected max check for items on song rotation`

### htw 09-22-09

See changes below

`     Changed click/aa entries to STL, added class (a couple members for future direction), a few other changes`

### dewey2461 09-19-09

Updated to let you twist AA abilities and define clicky/AA songs from inside the game

### 12-23-08

`     Updated array lengths to add more clicky slots`

### MinosDis 05-01-08

Updated to fix /twist once

### Simkin 12-17-07

Updated for Secrets of Faydwer 10 Songs

`     Support  items Secrets of Faydwer 10 Songs`

### 10-05-04

`     Support "swap in and click" items`

### 09-15-04

`     Support extra spell slot from Omens of War AA`

### 09-01-04

`     Command: /twist quiet to toggle some of the spam on/off`  
`     Various code fixes/speedups`

### 08-29-04

`     Moved LONGSONG_ADJUST into INI file and made /twist adjust command to set it on`  
`     the fly`

### 08-25-04

`     Changed output for /twist once to be slightly less misleading`  
`     Reset click/song timers every time they're called with /twist hold or /twist once;`  
`     if the user's specifying that song, they obviously want to cast it anyway.`  
`     Removed the variable MissedNote as close inspection revealed the only place it was`  
`     checked for was the line that set it. /boggle`  
`     Minor code tweaks, cleanups, formatting changes, etc`

### Pheph 08-24-04

cleaning up use of MQ2Data

`     Modified it to use only one TLO, as I found it somewhat messy having 4 different ones.`  
`     All the functionality of the old TLO's are now members of ${Twist}`  
`     ${Twising} is now ${Twist.Twisting}, or just ${Twist}`  
`     ${TwistCurrent} is now ${Twist.Current}`  
`     ${TwistNext} is now ${Twist.Next}`  
`     ${TwistList} is now ${Twist.List}`

### 08-23-04

`    Reset_ItemClick_Timers was being called far too often.  Now the only time we reset`  
`    is if a new list of songs are specified.  "/twist ${TwistList}" is a useful alias`  
`    if you for some reason want the old behavior.`  
`    Sing or /twist hold now resets the cast/item timer for that song only, rather than`  
`    the entire list.`  
`    Command: /twist reset calls Reset_ItemClick_Timers without interfering with the`  
`    state of the current twists.`

### 08-22-04

`    Command: /twist once [songlist] will cycle through the songs entered once, then`  
`    revert to the old twist, starting with the song that was interrupted.`  
`    Removed command "/twist on", it was making the string compare for "once" annoying,`  
`    and I didn't think it was worth the effort for a redundant command.`  
`    /twist delay with no argument now returns the delay without resetting it.  Values`  
`    less than 30 now give a warning...maybe they're not bards or have some other`  
`    reason for using a low value.`

### Cr4zyb4rd 08-19-04

taking over janitorial duties

`     Minor revamp of item notification.  Removed ITEMNOTIFY define and kludged in some`  
`     changes from Virtuoso65 to get casting by item name working.  /cast is no longer`  
`     used.`  
`     Added INI file support for above change.  File now uses distinct entries for item`  
`     names and slots.  *Quotes not required for multi-word item names in INI.*`  
`     Fixed the MQ2Data value TwistCurrent to display the current song as-advertised, and`  
`     added a new value TwistNext with the old behavior of showing the next song in the`  
`     queue. (Useful in scripting)`  
`     Removed a few DebugSpews that were mega-spamming my debugger output.`  
`     CastTime of -1 in the INI file now causes the default delay to be used.`

### 06-01-04

`     Added LONGSONG_ADJUST (default to 1 tick) to help with the timing of recasting long`  
`     songs, such as selo's.`  
`     Twisting is now paused when you sit (this would include camping).  This fixes`  
`     problems reported by Chyld989 (twisting across chars) and Kiniktoo (new autostand on`  
`     cast 'feature' in EQ makes twisting funky)`

### 05-19-04

`     Added workaround for incorrect duration assumption for durationtype=5 songs, such as`  
`     Cassindra's Chant of Clarity or Cassindra's Chorus of Clarity.`  
`     Added check of char state before casting a song. Actually added for 1.05`  
`        Checked states and resulting action are:`  
`           Feigned, or Ducking = /stand`  
`           Stunned = Delay`  
`           Dead - Stop twisting.`  
`        If you're a monk using this to click your epic, you'll want to disable the autostand on feign code =)`

### 05-05-04

`     Fixed CTD on song unmem or death, while twisting.  Oops`  
`     Removed circle functionality.  It's better suited for a plugin like the MQ2MoveUtils`  
`        plugin by tonio at `[`http://macroquest.sourceforge.net/phpBB2/viewtopic.php?t=6973`](http://macroquest.sourceforge.net/phpBB2/viewtopic.php?t=6973)

### 05-01-04

`     Fixed problem with using pchar before state->ingame causing CTD on eq load (thanks MTBR)`  
`     Fixed vc6 compile error w/ reset_itemclick_timers`  
`     Replaced various incantations of pChar and pSpawn with GetCharInfo()`  
`     Fixed /circle behavior w/ unspecified y/x`  
`     Fixed /circle on when already circling and you want to update loc`  
`     Added output of parsed circle parameters on start.`

### 04-25-04

`     Converted to MQ2Data`  
`        Top Level Objects:`  
`           bool   Twisting      (if NULL plugin is not loaded)`  
`           int      TwistCurrent`  
`           string   TwistList`  
`     Removed $Param synatax for above`  
`     Added check to make sure item twists specified are defined`  
`     Fixed error with twist parameter processing`  
`     Changed twist startup output to be more verbose`  
`     Command: /twist on added as alias for /twist start`  
`     INI File is now named per-character (MQ2Twist_Charname.ini)`  
`        * Be sure to rename existing ini files`  
`     Modified twist routine to take into account songs with`  
`        non-0 recast times or longer than 3 tick durations,`  
`        and only re-cast them after the appropriate delay.`  
`        This is for songs like Selos 2.5 min duration, etc.`  
`        * Note that this makes no attempt to recover if the song`  
`        effect is dispelled, your macro will need to take care`  
`        of that.`  
`     Added ability to compile-time change the method used for`  
`        clicking items.`

### 04-13-04

`     Changed /circle command to allow calling w/o specifying loc`  
`     Corrected a problem with multiple consecutive missed notes`  
`     Added handling of attempting to sing while stunned`  
`     Command: /twist slots, to list the slot to # associations`  
`     Command: /twist reload, to reload the ini file on the fly`  
`     Command: /twist end, /twist off as aliases for /twist stop`  
`     Command: /sing #, as an alias for /twist hold #`

`     Added support for item clickies.  Clickies are specified`  
`     as "gem" 10-19. For example, /twist 1 2 10 12`

`     Added INI file support for storing item clicky info`  
`     and default twist delay.`

### 04-11-04

`     Integrated the /circle code from Easar, runs in a circle.  type`  
`     /circle for help.`

### CyberTech 03-31-04

w/ code/ideas from Falco72 & Space-boy

### koad 03-24-04

Original plugin (http://macroquest.sourceforge.net/phpBB2/viewtopic.php?t=5962&start=2)

## See Also

-   [MQ2Twist](../plugins/mq2twist.md)
-   [MacroQuest2 Plugins](../documentation/macroquest2-plugins.md)


