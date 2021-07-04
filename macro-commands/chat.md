## Description

<span style="color:red">#chat</span> <span style="color:blue">channelname</span>

This is a special type of #event which watches the specified channelname. Content from the channelname is accessed by
creating a Sub Event_Chat.

## Use

Valid channels are: auc, *chat*, guild, group, ooc, say, shout, and tell. (*chat* represents channels) Channel raid was
added with Oct 21, 2020 update

Only one channel may be used on the #chat line, however multiple lines may be added.

## Example

    #chat guild
    #chat group

    Sub Event_Chat(ChatChannel,ChatSender,ChatText)
      /echo ${ChatSender} told me ${ChatText} in ${ChatChannel}
    /return

This would trigger Event_Chat for both guild and group chat.

        /if (${ChatText.Find[send me to]} && ${DoPorts} && ${Select[${Me.Class.ShortName},DRU,WIZ]}) {
            /call SendUs ${ChatText.Arg[4]} ${Sender}
            /return
            }

This would watch for the key phrase "send me to" and then call the subroutine SendUs with the keyword following the
phrase.

Ex "/g send me to pok" would man the keyword was pok, and the subroutine would cast the appropriate spell to send you to
Plane of Knowledge.

        /if (${ChatText.Find[open door]} || ${ChatText.Find[click door]}) {
            /doortarget
            /delay 1s
            /face door
            /if (${DoorTarget.Distance}>20) {
                /click left door
                }
            }

In this instance the macro would watch for the key phrase "open door" or "click door" and, provide the door was with in
twenty feet, click on the door.

Also see here for information on #events and the #chat special event.

## See Also

-   [Pound_Commands](pound-commands.md)
-   [Macro_Reference](../documentation/macro-reference.md)


