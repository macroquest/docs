# Custom Events

## Basic Event Usage

The Custom Event system allows you to trigger [Subroutines](../documentation/subroutines.md) off of any text that reaches the EQ client. Basically any text that is displayed in an EQ chat window, or in the MQ2 chat window can be used. You are able to use parts of the text as parameters for your event subroutine. An example of an \#event is below:

```text
#event Invite           "BillyBob invites you to join a group."
```

This means that when the text "BillyBob invites you to join a group." appears on screen, the event will queue up. It's important to remember that the event will not trigger it's subroutine until you allow it to in your macro. You do so by adding "/doevents" or "/doevents Invite" at an appropriate point in your macro.

When your macro hits the [/doevents](../reference/commands/doevents.md) line, it will trigger any events that are queued up. At this point, the macro will look for the appropriately named subroutine, which in the above case is "Sub Event\_Invite". So to flesh out the example above, we should have the following macro:

```text
 #event Invite           "BillyBob invites you to join a group."
 Sub Main
   :mainloop
   /doevents
   /delay 0
   /goto :mainloop
 /return

 Sub Event_Invite
   /echo BillyBob invited me!
 /return
```

This will keep running /doevents and when it senses the \#event trigger text, it will /echo the text in the Event Sub.

## Using part of the \#event text as a variable

Now while the above example is pretty useful (eg. you can accept the invite in the Sub Event\_Invite), what if we want to accept invites from more than one person? We could create two separate events and have them each echo a different piece of text. Or we could use part of the event text as a variable and manipulate it in the [subroutine](../documentation/subroutines.md). You can do this by marking out the part of text you want to use as a variable. In the above example, we'll use the inviter's name:

```text
 #event Invite           "#1# invites you to join a group."
 Sub Main
   :mainloop
   /doevents
   /goto :mainloop
 /return

 Sub Event_Invite(Line,Inviter)
   /echo ${Inviter} invited me!
 /return
```

A few things to note about the above example:

1. Firstly, we use \#1\# to mark the first variable that we'd like passed to our Sub. If you want more than one variable

   to be passed, you can use \#2\# and greater to indicate other variables.

2. Secondly, the above Sub has two variables passed to it - ${Line} and ${Inviter}. 1. The \#event system will always pass the entire line of matched text to the subroutine as the first variable. Even

   if you don't wish to use the entire line of text, you need to define the variable. Using "Line" as the first

   variable is very common. However the first variable can be called whatever you'd like, especially if you'd like

   to use the line in your Sub!

   1. The next variable, Inviter, is the one we're interested in, and will match whatever's between the first set of \#

      symbols in the \#event line.

So when the text "PeggySue invites you to a group." appears in a chat window, the same event will trigger, and it will echo

```text
"PeggySue invited me!"
```

in the MQ2 chat window.

## Ignoring parts of the \#event text

You can also ignore certain parts of the trigger text by using \#\*\#. So the example:

```text
#event Invite           "#1# invites you to join #*#"
```

Would trigger when someone invited you to a group or a raid.

## Using variables in the \#event text

You can also have the \#event system parse variables at the time of the match too. In the following example:

```text
#event Follow "#*#follow |${Me.CleanName}|'"
```

When the text, apart from what is between the \| symbols, is matched, it then evaluates what's between the \| symbols and the event is triggered if the variable matches the text.

So if ${Me.CleanName} was "PeggySue", the following text would not be matched:

`BillyBob tells the raid, 'follow me'`

While the following text would be:

`BillyBob tells the raid, 'follow PeggySue'`

## \#chat Special event

The \#chat command is a special custom event. It will always pass the channel, sender and text to the Sub Event\_Chat subroutine. So your Sub Event\_Chat should look something like this:

`Sub Event_Chat(ChatChannel,ChatSender,ChatText)`  
`/echo ${ChatSender} told me ${ChatText} in ${ChatChannel}`  
`/return`

Variable names can be anything you choose.

## Timer Events

This is another special custom event. The name of the Timer and the Original Value it was set to, are passed to the subroutine as soon as the timer reaches 0. For example:

`Sub Event_Timer(Timer,OriginalValue)`  
`/echo ${Timer} reached 0, original value was ${OriginalValue}`  
`/return`

## Notes and Tips

1. Because the system lets you pick the parameter number of any portion of the message, some parameters may not get

   defined. It's up to you to make sure you define all the needed parameters, and to make sure they're defined as the

   correct type (string, int, bool, etc).

2. Pay particular attention to the syntax of your \#event line. It will only trigger if the text is _identical_, so best

   to check it against text in game or in your log file.

### If your death event no longer works

_Note: This should be fixed as of the 20060628 MQ2 release._

A common use for \#event in a lot of macros was for use when you died, something like this:

`#event Died "#*#You have entered#*#"`

Due to a few small bugs, this event did not always work. To work around this, you can do the following:

1. Declare an outer variable with the ID of your zone in the Main sub.
2. Somewhere in your main loop, add a check that calls the \#event if the zone is not the same.
3. Reset the outer variable within your event.

For example

```text
 #event Died       "#*#You have entered#*#"

 sub Main
   /declare zonecheck int outer ${Zone.ID}

   :main_loop
   /if (${zonecheck} != ${Zone.ID}) /call Event_Died
   /delay 0
   /goto :main_loop
 /return

 sub Event_Died
   /varset zonecheck ${Zone.ID}
   /sit
   /delay 10s
   /afk
   /endmacro
 /return
```

