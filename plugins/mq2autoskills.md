## Description

MQ2AutoSkills, developed by Cr4zyb4rd, is a plugin that attempts to use combat or other skills
whenever they're available (and the pre-requisite conditions are met). It also has the ability to turn off attack during
ENRAGE or Infuriate.

Currently supported skills are:

-   Backstab
-   Bash
-   Begging
-   Disarm
-   Dragon Punch
-   Eagle Strike
-   Flying Kick
-   Frenzy
-   Evade
-   Forage
-   Feign Death
-   Intimidation
-   Kick
-   Mend
-   Pick Pockets
-   Round Kick
-   Sense Traps
-   Slam
-   Taunt
-   Tiger Claw

The plugin can be downloaded from [here](https://macroquest2.com/phpBB3/viewtopic.php?t=9079).

'**'Note:** This plugin was developed many years ago and has been superceded by other more fully-featured plugins, the
most popular being [MQ2Melee](mq2melee.md).

## Commands

In order for MQ2AutoSkills to use any of your skills, you must have the skill mapped to an ability button.

-   **/autoskills help**

  
This lists all options

-   **/autoskills list**

  
List available skills and whether they are enabled

-   **/autoskills settings**

  
List settings/thresholds

-   **/autoskills backoff \[#\]**

  
%HP at which to not re-engage after FD/Evade

-   **/autoskills melee \[#\]**

  
Range to be considered "in melee range"

-   **/autoskills mendhp \[#\]**

  
%HP at which to use the mend ability

-   **/autoskills \[skill\]**

  
Toggle a skill on/off and update the INI

-   **/autoskills \[skill\] \[on\|off\]**

  
Enable/disable a skill

## Examples

-   For a Warrior, you could use something like the following

`/autoskills taunt`  
`/autoskills bash`  
`/autoskills melee 15`

-   For a Berserker , trying to optimize dps while watching cooldown timers

`/autoskills Frenzy`  
`/autoskills Volley`  
`/autoskills War Cry`

## Bugs

Trade/Vendor windows and possibly some other events may cause some skills to fire when not appropriate and spam you.

## See Also

-   [Plugins](../documentation/macroquest2-plugins.md)
-   [MQ2Melee](mq2melee.md)


