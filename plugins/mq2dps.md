**MQ2Dps**

Display someone melee and non melee dmg (procs, casts, kicks, backstabs...) and DPS.

ex: Jarr total dmg: 5600 (345) in 10, DPS : 560 total (non melee) in TIME (seconds), DPS total/time

**All Damage Related Text MUST Be Allowed**

## Developers

Shire - 12-09-03 - Original Source

Not Sure on Others, Someone Else Will Need to Add Them

## Commands

-   **/dps <option> <value>**

:\***on\|off\|reset**

  
  
Activate dps parsing or not. reset parser

### Example

**/dps on**

  
Would Turn on the DPS Parsing

## Variables

-   ${Dps.Version}
-   ${Dps\[0\].Dps}
-   ${Dps\[0\].Name}
-   ${Dps.Me}
-   ${Dps.MyPet} (id start at value 0, plugin internal id, not ingame spawn id.)

## Changes

### 04/30/2004 v0.9.94

  
New param system ${Dps.Version} , ${Dps\[0\].Dps} , ${Dps\[0\].Name} , ${Dps.Me} , ${Dps.MyPet}

Replace 0 by the index.

Added options "focus", "/dps focus %target%", MAY CAUSE CTDs.

Added Window infos saved into INI. But not working now.

Added absolutedps\[true,false\], Timer used for calculating player's dps is the same."

'This release is mainly for the window to work with new params system.'

### 03/20/2004 v0.9.93

  
Fixed assasination.

Added Sorting by dps,melee,cast,total damage.

Fixed some compilation warning (CXStr())

Added options "petfollowowner", "/dps petfollowowner true", if True pet'stats will be grouped with pet's owner.

Extended window to display 8 char and player and player's pet dps.

### 12/13/2003 v0.9.92

  
Fixed Warder not being displayed under there owner.

Fixed event mob dead. (need a bit more work)

Mob name will appear red.

Added a window that show real time DPS (only 4 first).

Added some command and param: /dps on\|off\|reset\|showwindow)

$dps(id),$dpsname(id),$dpsversion

id start at value 0.

### 12/10/2003 v0.9.91

  
Fixed Mob total hp.

Pet's owner will always been displayed now even if they don't do any damages.

Changed the stats separator line to '----------------'

Changed \_\_time64_t data type to time_t (time.h) to make it VS 6 friendly. Let me know if it compiles now.

### 12/09/2003 v0.9.9

  
Released

## Screenshots

[Click Here For Screenshot(Not Working)](http://www.lamah.com/shire/mq2dps0_99.jpg)

## See Also


