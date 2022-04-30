# MQ2Events

## Description

## Commands

* _'/event \[_ load\*&lt;/span&gt; \|

  _deletename_\| _settriggernametrigger text_\|

  _setcommandnamecommand text_\| \*list'' \]

### Variables

```text
EventArg1 these are set acording to last event triggered and correspond to #1# .. #9#
EventArg2 these are not cleared so you can have one event use #9# and once set it will stay set until another #9# is encountered.
EventArg3
EventArg4
EventArg5
EventArg6
EventArg7
EventArg8
EventArg9
```

### INI file

MQ2Events\_CharacterName.ini

Format:

```text
[eventname]
trigger=trigger text
command=command to execute when triggered
```

## Examples

### INI Entries

```text
[enrage]
trigger=|${Target.DisplayName}| has become ENRAGED#2#
command=/attack off

[relaytell]
trigger=#1# tells you, #2#
command=/tell relaytargetname ${EventArg1} told me, '${EventArg2.Mid[2,${Math.Calc[${EventArg2.Length}-2]}]}'

[group]
trigger=#1#To join the group, click on the 'FOLLOW' option, or 'DISBAND' to cancel.#2#
command=/timed ${Math.Calc[3+${Math.Rand[4]}].Int}s /keypress ctrl+i

[raid]
trigger=#1#To join the raid click the accept button in the raid window or type /raidaccept.#2#
command=/timed ${Math.Calc[3+${Math.Rand[4]}].Int}s /raidaccept
```
