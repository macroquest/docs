## Syntax

**<span style="color:red">/custombind</span> \[ <span style="color:blue">list</span> \| \[
<span style="color:blue">add</span>\|<span style="color:blue">delete</span>\|<span style="color:blue">set</span>\|<span style="color:blue">clear</span>
*bindname*\[<span style="color:blue">-down</span>\|<span style="color:blue">-up</span>\] \] \[*command* \]**

## Description

This command is used to add, delete, list or change custom key bindings. See also [/bind](bind.md) and
[/dumpbinds](dumpbinds.md).

|                                              |                                                                                                              |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **/custombind list**                         | Lists all your custom bind names and commands (the key combinations must be set using /bind)                 |
| **/custombind add *bindname***               | Add a new bind called *bindname* ready for use.                                                              |
| **/custombind delete *bindname***            | Remove the custom bind *bindname*.                                                                           |
| **/custombind clear name\[-down\|-up\]**     | This will clear a specific command for a custom bind. If -up or -down is not specified it defaults to -down. |
| **/custombind set *bindname*\[-down\|-up\]** | Will set a specific command for a custom bind. This too defaults to -down if not specified.                  |

## Example

**NOTE: MQ2's very first bind command is "RANGED" so you do not need to do this, it is just listed here as an example**

        /custombind add mybind
        /custombind set mybind /ranged
        /bind mybind n

This binds the /ranged command to the n key.

Example of using down and up

    /custombind add echotest
    /custombind set echotest-down /echo n key is down!
    /custombind set echotest-up /echo n key is up!
    /bind echotest n

[Return to Slash Commands](slash-commands.md)


