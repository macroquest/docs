## Description

## Commands

-   *'<span style="color:red">/event</span> \[ <span style="color:blue">*load*</span> \|
    <span style="color:blue">*delete*</span>*name*\| <span style="color:blue">*settrigger*</span>*nametrigger text*\|
    <span style="color:blue">*setcommand*</span>*namecommand text*\| <span style="color:blue">*list''</span> \]

### Variables

    EventArg1 these are set acording to last event triggered and correspond to #1# .. #9#
    EventArg2 these are not cleared so you can have one event use #9# and once set it will stay set until another #9# is encountered.
    EventArg3
    EventArg4
    EventArg5
    EventArg6
    EventArg7
    EventArg8
    EventArg9

### INI file

MQ2Events_CharacterName.ini

Format:

    [eventname]
    trigger=trigger text
    command=command to execute when triggered

## Examples

### INI Entries

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

## See Also

-   [Plugins](../documentation/macroquest2-plugins.md)


