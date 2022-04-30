# \#chat

## Description

\#chat channel

This is a special type of \#event which watches the specified channel. Content from the channel is accessed by creating a Sub Event\_Chat.

## Use

Valid channels are: auc, _chat_, guild, group, raid, ooc, say, shout, and tell. (_chat_ represents channels)

Only one channel may be used on the \#chat line, however multiple lines may be added.

## Example

```text
#chat guild
#chat group

Sub Event_Chat(Channel,Sender,Text)
  /echo ${Sender} told me ${Text} in ${Channel}
/return
```

This would trigger Event\_Chat for both guild and group chat.

```text
/if (${Text.Find[send me to]} && ${Select[${Me.Class.ShortName},DRU,WIZ]}) {
  /call SendUs ${Text.Arg[4]} ${Sender}
  /return
}
```

This would watch for the key phrase "send me to" and then call the subroutine SendUs with the keyword following the phrase.

Ex "/g send me to pok" would man the keyword was pok, and the subroutine would cast the appropriate spell to send you to Plane of Knowledge.

```text
/if (${Text.Find[open door]} || ${Text.Find[click door]}) {
  /doortarget
  /delay 1s
  /face door
  /if (${DoorTarget.Distance}>20) {
    /click left door
  }
}
```

In this instance the macro would watch for the key phrase "open door" or "click door" and, provide the door was with in twenty feet, click on the door.

Also see here for information on \#events and the \#chat special event.
