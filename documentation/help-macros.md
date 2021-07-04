# Help Macros

## General Macro Help

* First off, do you have the latest copy of your macro?  

  If you found your macro on the forums, check back to the first post and see if it has been updated since you last

  downloaded it. If you are unsure, or the macro writer has not included a version number, then it's easiest to just

  recopy the code from the forums into your macro and then save it and try again.

* Have you read all the documentation regarding the macro:
  1. The first post on the forum normally has some text indicating how to run the macro, what it does, what its

     dependencies are, etc.

  2. Secondly, read all the pages in the thread about the macro. Yes, this may take you a while if its an old or

     established macro, but it's very likely someone else has had the same problem and the question has been

     answered.

  3. Check the wiki page, if your macro has one. Often they are checked and modified more frequently than the macro

     thread/first post.
* Do you have all the pre-requisites for the macro, other snippets \(.inc files\) and plugins required?
* If there are pre-requisite plugins or snippets, are they configured correctly? You will most likely need to check

  the forum posts for the snippet/plugin in question too \(yes, more reading :\).

### INI file maintenance

To remove a keyname \(\[Section\]\) and all of it's valuenames and values, from an ini file:

```text
/ini "Myfile.ini" "KeynameToRemove"
```

To remove a valuename \(and all of it's values\) from an ini file:

```text
/ini "Myfile.ini" "Keyname" "ValuenameToRemove"
```

## Macro Problems

### Couldn't open macro file: xxx.mac

* Make sure you saved the macro into the Release\Macros directory.
* Make sure the macro has a .mac extension.
  * If you cannot see an extension on the macro file, you may have your file extensions turned off. In Explorer, go

    to Tools - Folder Options - View tab and untick the option _"Hide extensions for known file types"_. Then rename

    the file and change the extension to .mac.

### Due to complete misuse of the String Top-Level Object, it has been removed.

* A while back, macro writers were incorrectly using the ${String} TLO in their macros. In order to

  prevent people from using this TLO incorrectly, thus slowing down their macros, and in an attempt to teach people to

  create their macros properly and efficiently from the get-go, the ${String} TLO was removed.

* Finding this error when running a macro generally means you have an old copy of a macro. Most macros have been

  updated to not use the ${String} TLO and therefore the first place you should be looking is \*\*in the forum thread

  where you obtained your macro\*\*.

* Fixing the error is easy when you know what to look for, but a bit more tricky in a complicated macro or if you're

  not a macro maker yourself. Here's a simple example that should help explain it. The code:

`/if (${String[${Me.Gem[1]}].NotEqual[Complete Healing]}) /memspell 1 "Complete Healing"`

* What this does is check if the spell name of the spell in the first slot is "Complete Healing" \*\(the /if statement

  inside the brackets\)_. If it is not, then mem "Complete Healing" in slot 1_ \(the /memspell bit after the brackets\)\*.

* If we look in the manual, we see the following entry for the Gem reference type \(part of the

  [_character_](../data-types-and-top-level-objects/data-types/datatype-character.md) reference type\):

{\| border="1" cellpadding="2" cellspacing="0"

\|[_spell_](../data-types-and-top-level-objects/data-types/datatype-spell.md) **Gem\[**\#**\]** \|The name of the spell in this slot\# \|}

* The part we're interested here is the first word _spell_ which tells you what the return type of Gem\[\#\] will be.

  In this case it will return a type "spell".

* Equal or NotEqual can only be used to compare two strings \(which is why people would convert the result of

  ${Me.Gem\[1\]} _\("spell"\)_ to a string by using the ${String} TLO\). While this may look fine logically, it's not the

  way MQ2 Data Types were designed to be used, and its more work for your PC to convert the result of the _spell_ to a

  string.

* The way you're supposed to use the Data Types is to add more members to the end of the TLO until you get the result

  you're looking for. In the above example, if we look at the reference type for [_spell_](../data-types-and-top-level-objects/data-types/datatype-spell.md),

  we see the following:

{\| border="1" cellpadding="2" cellspacing="0"

\|[_string_](../data-types-and-top-level-objects/data-types/datatype-string.md) **Name** \|Name \|}

* This shows us that we can use the .Name reference type to get a string value as a result, which can then be compared

  \(using .Equal or .NotEqual\). So now we have a piece of code like the following:

`${Me.Gem[1].Name}`

* That will output a string value which contains the name of the spell in gem slot 1. The code:

`${Me.Gem[1].Name.NotEqual[Complete Healing]}`

* Will give us a TRUE/FALSE result if you echo the above statement.
* So instead of wrapping ${Me.Gem\[1\]} in a ${String\[\]} TLO, we've removed the need to convert the "spell" result

  to a "string" result, by adding .Name to the end of the TLO, thereby making it return a string value.

* The above changes can be incorporated into the initial faulty line, like this:

`/if (${Me.Gem[1].Name.NotEqual[Complete Healing]}) /memspell 1 "Complete Healing"`

* We've now removed the ${String\[\]} part, and still have a perfectly functioning \(and faster\) macro.

### This macro I downloaded doesn't do X \(fill in as appropriate\)

* If you have followed all the advice in the General Macro Help section, and you are still having problems, you may

  want to post your problem to the macro thread itself.

* Follow the instructions in Help Forums but make sure to reply to the main macro post, and

  do not post a new thread in any of the other Help forums.

* If you have a feature request for your macro, post the request in the main macro thread and the macro writer may

  oblige you and add your requested feature. Or failing that, dive right in and modify the macro for your own use.

  \*Remember, many new macros are born when someone modifies an existing macro to do something more/different, and then

  after enough changes, it becomes a new macro in its own right.\*

### Macros From Other Sites Not Working Properly

If you download a macro from a site that doesn't update their macros, first search the MQ2 forums to see if there is a similar problem discussed in any threads. If that doesn't help, read the Help Forums. Post to the thread that relates to the macro in question if one exists before starting a new thread. Make sure to follow all the rules discussed before posting in the Help section of the Message Boards.

### The Macro does not report if it's running or not

* You may: add _/echo macro\_name\_here is running_ to the Sub Main section of the actual .mac file
* Issue _/echo ${Macro}_ to see the name of the macro currently running
* If that doesn't help, read the Help Forums and then post on the boards, making sure to

  follow all the rules.

