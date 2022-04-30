# MQ2Cursor

## Description

**MQ2Cursor** by s0rCieR is a plugin that tries to keep your cursor free of items. It was inspired by the plugins [MQ2FeedMe](mq2feedme.md) and MQ2AutoDestroy.

* It also tries to keep you above a certain hunger/thirst level \(so that you don't eat your stat food\).
* Additionally, it can be used to loot your own corpse.

MQ2Cursor can be found [here](https://macroquest.org/phpBB3/viewtopic.php?t=12368), in the VIP forums.

**Features:**

* Auto Keep item from list up to a certain quantity.
* Consume, Drop, or Destroy when quantity is reached.
* Auto Sleep with certain windows are open \(Spellbook, Casting, Bank, Give, Merchant, Trade, GuildTributemaster,

  TributeMaster, GuildBank, Inventory but not Loot window, Loot window but not Inventory\).

* Quiet/Silent Operating Mode and Global On/Off flags.
* Autoloot your corpse when loot Window Up.

All settings are saved to the INI file \_.ini.

## Commands

**/cursor on\|off\|auto**

Turn plugin On/Off or Toggle

**/cursor silent on\|off\|auto**

Turn Quiet Mode On/Off or Toggle

**/cursor feeding**

Turn Feeding Mode On/Off or Toggle

**/cursor dropping**

Turn Dropping Mode On/Off or Toggle

**/cursor load\|save**

Save/Load information from the INI file.

**/cursor rem\(ove\)\|del\(ete\) id**

Remove ID or \(Item on Cursor\).

**/cursor list \[partial name\]**

List items in the cursor list along with their status \(drop, protected, etc\). A partial name can be supplied to further narrow down the list, but please remember that the partial name is case sensitive.

**/cursor al\(l\(ways\)**

Always keep those \(Item On Cursor\).

**/cursor \# \[st\(acks\)\]**

Keep quantity \# \(Item On Cursor\).

**/cursor random \#**

Random humanish delay in ms 0=off.

**/keep**

Keep Item on Cursor \(and don't add it to the list\).

**/lootme on\|off\|auto**

Turn Plugin On/Off or Toggle.

**/lootme silent on\|off\|auto**

Turn Quiet Mode On/Off or Toggle.

## Examples

`/cursor 2 st`  
`/cursor rem 1685`  
`/cursor silent on`  
`/cursor list Water`
