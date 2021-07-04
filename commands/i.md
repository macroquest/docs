## Syntax

**<span style="color:red">/i</span> <span style="color:blue">help</span>\|<span style="color:blue">nick</span>
*name*\|<span style="color:blue">join</span> *#channel*\|<span style="color:blue">part</span>
\[*#channel*\]\|<span style="color:blue">whois</span> *nickname*\|<span style="color:blue">msg</span> *nickname*
*text*\|<span style="color:blue">say</span> *text*\|<span style="color:blue">raw</span>
*command*\|<span style="color:blue">quit</span>\|<span style="color:blue">names</span>\|<span style="color:blue">x</span>**

## Description

This is the main IRC slash command and controls most things related to IRC communication. All the commands below must be
entered after you have connected with */iconnect*.

-   **help:** Show a list of commands that can be issued after /i.
-   **nick:** Change your nick to *name*.
-   **join:** Join the channel *#channel*. The channel must have a # in front of it.
-   **part:** Leave *#channel*. If no channel is given, it will leave the last-joined channel.
-   **whois:** Display information available on *nickname*.
-   **msg:** Send a directed message of "*text*" to *nickname*. This is the IRC equivalent of a tell.
-   **say:** Speak "*text*" in the current channel. This *text* will be visible to everyone in the channel.
-   **raw:** Send *command* to the server. This is useful for other IRC commands that are not available with /i (eg. "/i
    raw list" to list all channels on the server).
-   **quit:** Leave the server (same as the IRC command /quit).
-   **names:** List all nicknames on the current channel.
-   **x:** *Not sure*.

## See Also

-   [MQ2IRC](../plugins/mq2irc.md)
-   [/iconnect](iconnect.md)
-   [/istatus](istatus.md)

[Return to Slash Commands](slash-commands.md)


