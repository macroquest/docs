## Syntax

**<span style="color:red">/mapnames</span> \[<span style="color:blue">help</span>\] \[
<span style="color:blue">target</span>\|<span style="color:blue">normal</span> *options* \]**

## Description

Sets how spawn names will be displayed on the MQ2 map, for your target or all other spawns.  
\*This command takes a parameter specifying normal/target, and then an optional custom string.

-   With no arguments, /mapnames will display the current settings for *target* and *normal* (both are set to %N by
    default).
-   The plugin will replace the %l %r %c %N *options* with a piece of information.
-   Each option is **case sensitive** and exactly one character in length.
-   It is important to note that names **are not** updated continually (except for your target if the target map filter
    is on).
-   You may use the following *options* to customize the display string:

  
{\| border="1" cellpadding="2" cellspacing="0" \|**%n** \|The default unique "name" of the target, like "a_coyote34" \|-
\|**%N** \|The cleaned up name of the target, like "a coyote" \|- \|**%h***\|Current HP percentage \|- \|**%i*** \|Spawn
ID \|- \|**%x***\|X coordinate \|- \|**%y*** \|Y coordinate \|- \|**%z***\|Z coordinate \|- \|**%R*** \|Full race name
(eg. Dwarf) \|- \|**%r***\|3-letter race code (eg. DWF) \|- \|**%C*** \|Class full name (eg. Shaman) \|-
\|**%c***\|3-letter class code (eg. SHM) \|- \|**%l*** \|Level \|- \|**%%**'' \|"%" sign \|} **Note:** All other
characters will be displayed as normal.

## Examples

    /mapnames normal [%l %R %C] %N - %h%%

Will display all spawns in the following format:

    [40 Human Banker] Banker Tawler - 100%
    [70 Wood Elf Ranger] BillyBob - 100%

## See Also

-   [MQ2Map](../plugins/mq2map.md)

[Return to Slash Commands](slash-commands.md)


