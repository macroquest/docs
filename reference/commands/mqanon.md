---
tags:
    - command
---
# /mqanon

## Syntax

**/mqanon** [*command*] [*parameters*] [*strategy*]

## Description

Anonymization tool that filters words in-game, designed for streaming and recording. It handles both the active player and any party/raid/fellowship members. It does **not** grant full-fledged anonymization, but is a tool to help with the process of anonymizing words (names, guilds, etc) in-game. For more (especially for plugin authors), see the [Anonymize](../../main/features/anonymize.md) feature.

**Important Notes:**
- Login/character screens contain no anonymization, this command is in-game only. Any text at server select, character select, login, etc ***will not be filtered***. Please make any considerations necessary to prevent visibility of the client outside of actual in-game experiences.
- Requires `/caption MQCaptions on` for name sprite anonymization. See [/caption](caption.md).

## Command Reference
 - no arguments: toggle on/off state of anonymization
 - `asterisk <name>`
   - add a filter for `name` and replace it with asterisks
 - `class <name>`
   - add a filter for `name` and replace it with class information
 - `custom <name> <text>`
   - add a filter for `name` and replace it with custom `text`
 - `drop <name>`
   - remove the filter for `name`
 - `alias <name> <alternate>`
   - add an alternate for `name`
   - will use the same replacement strategy as `name`
 - `unalias [name] <alternate>`
   - remove an alternate from `name`
   - specifying the name is optional here
 - `me [asterisk|class|me|none]`
   - set self anonymization to strategy
   - if no argument is specified, will use the `me` strategy
 - `group <asterisk|class|none>`
   - set group anonymization to strategy
 - `fellowship <asterisk|class|none>`
   - set fellowship anonymization to strategy
 - `guild <asterisk|class|none>`
   - set guild anonymization to strategy
 - `raid <asterisk|class|none>`
   - set raid anonymization to strategy
 - `all <asterisk|class|none>`
   - set all anonymization strategies at once
 - `save`
   - save the current configuration
 - `load`
   - load the configuration from file (for use when editing the config externally)
 - `[command] -h` or `[command] --help`
   - display help
   - commands that take arguments also allow this switch

## Replacement Strategies
There are some pre-built strategies that are commonly used (as seen in the command reference):
 - asterisk
   - replaces the middle characters in the name with asterisks
   - `Myname` becomes `M****e`
 - class
   - replaces the name with `"[${Spawn[pc {0}].Level}] ${Spawn[pc {0}].Class}"`
   - example: `/mqanon class Bigtank` changes `Bigtank` to `[60] WAR`
   - note that this assumes a pc
 - me
    - replaces your name with `"[${Me.Level}] ${Me.Race} ${Me.Class}"`
    - example: `/mqanon me` changes your name to `[60] Barbarian Warrior`
 - custom
    - Full custom replacement with macro parsing  
    - Example: `/mqanon custom Littlewiz "[Little] ${Spawn[pc {Littlewiz}].Class}"` → replaces "Littlewiz" with "Little Wizard"

## Replacement Priority
Since the same character can exist in multiple groupings (guild/group/raid, etc) and each grouping can have a separate strategy, the priority is as follows:
1) Custom
2) Self
3) Group
4) Fellowship
5) Guild
6) Raid

## Configuration
Settings are stored in `Config/MQ2Anonymize.yaml`. Example configuration:
```yaml
enabled: true
group: asterisk
fellowship: none
guild: class
raid: none
self: me

replacers:
  - name: "Bigtank"
    strategy: "custom"
    target: "[${Spawn[pc {Bigtank}].Level}] ${Spawn[pc {Bigtank}].Class}] MT"
    alternates:
      - "TankAlt"
      - "OldTankName"
      
  - name: "Banker"
    strategy: "asterisk"
    alternates:
      - "Mule"
```