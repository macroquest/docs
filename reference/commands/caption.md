---
tags:
    - command
---
# /caption

## Syntax

```eqcommand
/caption list | update <#> | MQCaptions [on|off] | reload | <type> <value> 
```

## Description

Customize spawn captions (names, titles, linkdead, etc.). You can also limit how many captions are processed to improve performance.

## Options

* **list** - List custom captions
* **reload** - Update captions from .ini
* **Update** - The number of nearest spawns which will have their caption updated each pass. The default is 35.
* **MQCaptions [on|off]** - Turns captions on or off
* The anon option has been deprecated, please use [/mqanon](mqanon.md) instead
* **_type_** _value_ - The spawn type and the value for its caption. Available types are:

  | Type       | Description                          |
  |------------|--------------------------------------|
  | Player1-6  | Player captions for /shownames 1-6   | 
  | Pet        | Pet captions                         | 
  | Merc       | Mercenary captions                  | 
  | NPC        | NPC captions                        | 
  | Corpse     | Corpse captions                     |

## Examples

Default captions can be overriden in the `[Captions]` section of your MacroQuest.ini file. 

```ini
[Captions]
# Player1 (basic), /shownames 1
Player1=${If[${NamingSpawn.Mark},${NamingSpawn.Mark} - ,]}${If[${NamingSpawn.Trader},Trader ,]}${If[${NamingSpawn.Invis},(${NamingSpawn.DisplayName}),${NamingSpawn.DisplayName}]}${If[${NamingSpawn.AFK}, AFK,]}${If[${NamingSpawn.Linkdead}, LD,]}${If[${NamingSpawn.LFG}, LFG,]}${If[${NamingSpawn.GroupLeader}, LDR,]}

# Player3 (with guild), /shownames 3
Player3=${If[${NamingSpawn.Mark},${NamingSpawn.Mark} - ,]}${If[${NamingSpawn.Trader},Trader ,]}${If[${NamingSpawn.Invis},(${NamingSpawn.DisplayName}),${NamingSpawn.DisplayName}]}${If[${NamingSpawn.Surname.Length}, ${NamingSpawn.Surname},]}${If[${NamingSpawn.AFK}, AFK,]}${If[${NamingSpawn.Linkdead}, LD,]}${If[${NamingSpawn.LFG}, LFG,]}${If[${NamingSpawn.GroupLeader}, LDR,]}${If[${NamingSpawn.Guild.Length},\n<${NamingSpawn.Guild}>,]}

# NPC
NPC=${If[${NamingSpawn.Mark},${NamingSpawn.Mark} - ,]}${If[${NamingSpawn.Assist},>> ,]}${NamingSpawn.DisplayName}${If[${NamingSpawn.Assist}, - ${NamingSpawn.PctHPs}%<<,]}${If[${NamingSpawn.Surname.Length},\n(${NamingSpawn.Surname}),]}

# Corpse
Corpse=${NamingSpawn.DisplayName}'s corpse
```

* NamingSpawn is an internal TLO, so it's not documented along with other TLOs since it will always return NULL outside of caption processing. It inherits all [spawn](../data-types/datatype-spawn.md) members. (e.g., DisplayName from `${NamingSpawn.DisplayName}` is a spawn member.)
* Use `\n` to add a new line when setting captions
* To set a caption in-game,
  ```text
  /caption Corpse ${NamingSpawn.DisplayName}'s corpse
  ```
* To revert to the default, you can delete the [Captions] section of your MacroQuest.ini file or clear the specific type with an empty value command like so,
  ```text
  /caption Corpse
  ```

## See Also

* [/captioncolor](captioncolor.md)
