---
tags:
   - command
---
# /custombind

## Syntax

**/custombind \[ list \| \[ add\|delete\|set\|clear** _**bindname**_**\[-down\|-up\] \] \[**_**command**_ **\]**

## Description

This command is used to add, delete, list or change custom key bindings. See [/bind](../../../reference/commands/bind.md) and [/dumpbinds](../../../reference/commands/dumpbinds.md).

|  |  |
| :--- | :--- |
| **/custombind list** | Lists all your custom bind names and commands \(the key combinations must be set using /bind\) |
| **/custombind add** _**bindname**_ | Add a new bind called _bindname_ ready for use. |
| **/custombind delete** _**bindname**_ | Remove the custom bind _bindname_. |
| **/custombind clear name\[-down\|-up\]** | This will clear a specific command for a custom bind. If -up or -down is not specified it defaults to -down. |
| **/custombind set** _**bindname**_**\[-down\|-up\]** | Will set a specific command for a custom bind. This too defaults to -down if not specified. |

## Example

!!! note

    MQ's very first bind command is "RANGED" so you do not need to do this, it is just listed here as an example.


```text
    /custombind add mybind
    /custombind set mybind /ranged
    /bind mybind n
```

This binds the /ranged command to the n key.

Example of using down and up

```text
/custombind add echotest
/custombind set echotest-down /echo n key is down!
/custombind set echotest-up /echo n key is up!
/bind echotest n
```

