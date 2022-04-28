# Editing Existing Macros

kharmakazy requested a macro that could loot any corpse. A macro like this already exists, so instead of inventing the wheel let's just change a current macro so it does what we need.

The macro in question is called Wait4Rez.mac by FaNTuM. His macro is for when you die, it'll consent group, raid, and guild. It will then wait for a rez box, auto-accept it, wait till you finish zoning, summon your corpse, then loot all the items. One particular reason I like this macro is that its clean and efficient, and it works. Without further babble, here's FaNTuM's macro - unedited:

`|** Wait4rez.mac by FaNTuM`  
`This will automatically accept rez, then loot your corpse for you, leaving`  
`the specified number of items on it. Usage:`&lt;/mac wait4rez 0&gt;`where 0`  
`is the number of items to leave on corpse, 0 loots all items.`  
`03/30/2005 **|`

`| --------------`  
`| -- Main Sub --`  
`| --------------`  
`Sub Main`  
`/declare t int outer 0`  
`/declare loottotal int outer`  
`/declare lootslot int outer`  
`/declare lootleft int outer 1`

`/if (!${Defined[Param0]}) {`  
`/echo Defaulting to leaving ${lootleft} item/s on corpse`  
`} else {`  
`/varset lootleft ${Param0}`  
`}`  
`/echo Wait4rez.mac activated. Now consenting guild, raid, and group.`  
`| --------------`  
`| -- Consents --`  
`| --------------`  
`/consent guild`  
`/delay 30`  
`/consent raid`  
`/delay 30`  
`/consent group`  
`/echo Awaiting rez: will auto-accept, then loot leaving ${lootleft} item/s on corpse`  
`| ---------------------`  
`| -- Auto-accept Rez --`  
`| ---------------------`  
`:waitforrez`  
`/if (!${Window[ConfirmationDialogBox].Open}) {`  
`/delay 1s ${Window[ConfirmationDialogBox].Open}`  
`/goto :waitforrez`  
`}`  
`/if (${Window[ConfirmationDialogBox].Open}) /notify ConfirmationDialogBox Yes_Button leftmouseup`  
`| ----------------------------------------------`  
`| -- Wait until fully zoned in before looting --`  
`| ----------------------------------------------`  
`:zonein`  
`/delay 5`  
`/target mycorpse`  
`/delay 5 ${Target.CleanName.Equal[${Me}'s corpse]}`  
`/if (${Target.CleanName.NotEqual[${Me}'s corpse]}) /goto :zonein`  
`/if (${Target.CleanName.Equal[${Me}'s corpse]}) {`  
`/delay 3s`  
`/call Loot`  
`} else {`  
`/goto :zonein`  
`}`  
`/end`

`| -----------------------`  
`| -- Pull corpse close --`  
`| -----------------------`  
`Sub Loot`  
`:corpsepull`  
`/target mycorpse`  
`/delay 5 ${Target.CleanName.Equal[${Me}'s corpse]}`  
`/if (${Target.CleanName.NotEqual[${Me}'s corpse]}) {`  
`/echo No corpse in this zone`  
`/return`  
`}`  
`/delay 3s`  
`/corpse`  
`/delay 1s ${Target.Distance}<20`  
`/if (${Target.Distance}>20) {`  
`/echo Corpse is too far away`  
`/return`  
`}`  
`| ---------------------`  
`| -- Open the corpse --`  
`| ---------------------`  
`/if (${Target.CleanName.Equal[${Me}'s corpse]}) {`  
`/loot`  
`} else {`  
`/echo where did my corpse go?`  
`/return`  
`}`  
`/delay 5s ${Me.State.Equal[BIND]}`  
`/if (${Me.State.NotEqual[BIND]}) /goto :corpsepull`  
`/varset loottotal 0`  
`| -----------------`  
`| -- Count items --`  
`| -----------------`  
`/delay 3s`  
`:LootLag`  
`/if (${loottotal}!=${Corpse.Items}) {`  
`/varset loottotal ${Corpse.Items}`  
`/delay 2s`  
`/goto :LootLag`  
`}`  
`/if (${loottotal}<=${lootleft}) {`  
`/echo Looting aborted. Error in number of items to be left on corpse.`  
`/notify LootWnd DoneButton leftmouseup`  
`/return`  
`}`  
`/varset loottotal ${Math.Calc[${Corpse.Items}-${lootleft}]}`  
`| ---------------------`  
`| -- Loot the corpse --`  
`| ---------------------`  
`/echo Looting all but ${lootleft} item(s)`  
`/for lootslot 1 to ${loottotal}`  
`:LootItem`  
`/itemnotify loot${lootslot} rightmouseup`  
`/delay 5 !${Corpse.Item[${lootslot}].ID}`  
`/if (!${Corpse.Item[${lootslot}].ID}) {`  
`/next lootslot`  
`} else {`  
`/goto :LootItem`  
`}`  
`| -----------------`  
`| -- Doublecheck --`  
`| -----------------`  
`/if (${Math.Calc[${Corpse.Items}-${lootleft}]}>0) /goto :LootLag`  
`/notify LootWnd DoneButton leftmouseup`  
`/echo Done looting. ${lootleft} Item(s) left on your corpse.`  
`/return`

Now, first thing we can skim away is the consent section. Since we will be looting NPC corpses we have no need to consent. By a quick glance, there's only a few lines that deal with consenting:

`| --------------`  
`| -- Consents --`  
`| --------------`  
`/consent guild`  
`/delay 30`  
`/consent raid`  
`/delay 30`  
`/consent group`  
`/echo Awaiting rez: will auto-accept, then loot leaving ${lootleft} item/s on corpse`

Now, let's look at the waiting for rez section. Again, when we kill a NPC we won't be getting a rez box, so that section can be removed as well.

`| ---------------------`  
`| -- Auto-accept Rez --`  
`| ---------------------`  
`:waitforrez`  
`/if (!${Window[ConfirmationDialogBox].Open}) {`  
`/delay 1s ${Window[ConfirmationDialogBox].Open}`  
`/goto :waitforrez`  
`}`  
`/if (${Window[ConfirmationDialogBox].Open}) /notify ConfirmationDialogBox Yes_Button leftmouseup`

Looking at the code, the next thing it does is it waits until it's fully zoned before looting. I'd surely hope you were fully zoned before looting a NPC corpse you just killed, so there's another section we can axe.

`| ----------------------------------------------`  
`| -- Wait until fully zoned in before looting --`  
`| ----------------------------------------------`  
`:zonein`  
`/delay 5`  
`/target mycorpse`  
`/delay 5 ${Target.CleanName.Equal[${Me}'s corpse]}`  
`/if (${Target.CleanName.NotEqual[${Me}'s corpse]}) /goto :zonein`  
`/if (${Target.CleanName.Equal[${Me}'s corpse]}) {`  
`/delay 3s`  
`/call Loot`  
`} else {`  
`/goto :zonein`  
`}`  
`/end`

Here we go again - next section deals with using the built in command /corpse to summon the corpse. (In case it was moved since you had been rezzed.)

`| -----------------------`  
`| -- Pull corpse close --`  
`| -----------------------`  
`Sub Loot`  
`:corpsepull`  
`/target mycorpse`  
`/delay 5 ${Target.CleanName.Equal[${Me}'s corpse]}`  
`/if (${Target.CleanName.NotEqual[${Me}'s corpse]}) {`  
`/echo No corpse in this zone`  
`/return`  
`}`  
`/delay 3s`  
`/corpse`  
`/delay 1s ${Target.Distance}<20`  
`/if (${Target.Distance}>20) {`  
`/echo Corpse is too far away`  
`/return`  
`}`

Now the next section we run across our first spot where we will use something, and remove something from the same section. Before we do that though, we need to take a brief look into one of the most basic programming ideas, the IF-THEN statement.

In plain english, an IF-THEN statement reads just like this: if A is true, then do B. Now, we can add a little to it, and add ELSE. IF-THEN-ELSE would read in plain english like this: if A is true, then B, otherwise(else) do C.

Now, each programming language is different, but the basic way MacroQuest evaluates this is something similar to this:

`/if (A) {`  
`B`  
`} else {`  
`C`  
`}`

If this does not make sense to you, re-read it a few times. This is a very basic concept, don't make it harder than it is.

Back on track, let's look at the next section of the Wait4Rez macro:

`| ---------------------`  
`| -- Open the corpse --`  
`| ---------------------`  
`/if (${Target.CleanName.Equal[${Me}'s corpse]}) {`  
`/loot`  
`} else {`  
`/echo where did my corpse go?`  
`/return`  
`}`  
`/delay 5s ${Me.State.Equal[BIND]}`  
`/if (${Me.State.NotEqual[BIND]}) /goto :corpsepull`  
`/varset loottotal 0`

Now I am NOT a coder. I learned one type of code and as soon as I got proficient, everything changed. Ever since then I haven't really done much of anything with code. Using common sense, however, we can read most of this section. Here's the section again, the bolded is plain english of what I think it means.

`| ---------------------`  
`| -- Open the corpse --`  
`| ---------------------`  
`/if (${Target.CleanName.Equal[${Me}'s corpse]}) {`**```/if`` ``(My`` ``Target's`` ``Name`` ``is`` ``Equal`` ``to`` ``Myname's`` ``corpse)`` ``{```**  
`/loot`**```Use`` ``the`` ``EQ`` ``command`` ``/loot```**  
`} else {`**`Otherwise`**  
`/echo where did my corpse go?`**```Put`` ``this`` ``text`` ``in`` ``the`` ``MQ2`` ``Window```**  
`/return`**```End`` ``macro```**  
`}`  
`/delay 5s ${Me.State.Equal[BIND]}`  
`/if (${Me.State.NotEqual[BIND]}) /goto :corpsepull`  
`/varset loottotal 0`

Some of that IF-THEN-ELSE statement will not be needed for our macro. We will need the /loot part, but the rest of it can be canned. Also in that section is a delay of some sort - 5s (assuming 5 seconds) and then a statement that sorta looks like it's asking if we are binding wound. Then it has another IF-THEN statement that looks like IF you aren't in the bind wound position THEN goto :corpsepull. We removed corpsepull already, so it looks like we can get rid of the statement in whole. The /varset was put in there for a reason, and I'm not entirely sure why yet - so I'm going to leave it in.

So now, we have this:

`|** Wait4rez.mac by FaNTuM`  
`This will automatically accept rez, then loot your corpse for you, leaving`  
`the specified number of items on it. Usage:`&lt;/mac wait4rez 0&gt;`where 0`  
`is the number of items to leave on corpse, 0 loots all items.`  
`03/30/2005 **|`  
````` \| --------------```\| -- Main Sub --````` \| --------------```Sub Main``  
`/declare t int outer 0`  
`/declare loottotal int outer`  
`/declare lootslot int outer`  
`/declare lootleft int outer 1`

`/if (!${Defined[Param0]}) {`  
`/echo Defaulting to leaving ${lootleft} item/s on corpse`  
`} else {`  
`/varset lootleft ${Param0}`  
`}`  
`/echo Wait4rez.mac activated. Now consenting guild, raid, and group.`  
`/loot`  
`| -----------------`  
`| -- Count items --`  
`| -----------------`  
`/delay 3s`  
`:LootLag`  
`/if (${loottotal}!=${Corpse.Items}) {`  
`/varset loottotal ${Corpse.Items}`  
`/delay 2s`  
`/goto :LootLag`  
`}`  
`/if (${loottotal}<=${lootleft}) {`  
`/echo Looting aborted. Error in number of items to be left on corpse.`  
`/notify LootWnd DoneButton leftmouseup`  
`/return`  
`}`  
`/varset loottotal ${Math.Calc[${Corpse.Items}-${lootleft}]}`  
`| ---------------------`  
`| -- Loot the corpse --`  
`| ---------------------`  
`/echo Looting all but ${lootleft} item(s)`  
`/for lootslot 1 to ${loottotal}`  
`:LootItem`  
`/itemnotify loot${lootslot} rightmouseup`  
`/delay 5 !${Corpse.Item[${lootslot}].ID}`  
`/if (!${Corpse.Item[${lootslot}].ID}) {`  
`/next lootslot`  
`} else {`  
`/goto :LootItem`  
`}`  
`| -----------------`  
`| -- Doublecheck --`  
`| -----------------`  
`/if (${Math.Calc[${Corpse.Items}-${lootleft}]}>0) /goto :LootLag`  
`/notify LootWnd DoneButton leftmouseup`  
`/echo Done looting. ${lootleft} Item(s) left on your corpse.`  
`/return`

Looks like we're almost done. Now, let's change one thing that's been bothering me. FaNTuM's macro by default leaves 1 item on the corpse. If we're looting NPC's then we don't need to leave 1 item on the corpse at all. (Unless you are a Necro or you group with one often that is)

Scanning the code I see:

`/declare lootleft int outer 1`

Which I'm pretty sure is the variable that is the default of how many items to leave on the corpse. Let's try changing it to 0.

I also noticed, just by looking at the code logically, that we currently have no way of targeting our corpse. Keeping it simple, let's add in a /target corpse somewhere before it attempts to open a loot window.

Now, we can edit or remove the /echo statements - all /echo statements do it put text in your MQ2 Chat Window. I'm going to just delete them all - we can always add them in later if we decide we need to be told that we just looted something.

Looks good - Now I'll just edit the comments at the top to better reflect what this macro does and we're finished.

`|** Loot.mac by TheNewGuy`  
`20 July 2005`

`Make a hotkey:`  
`/mac loot.mac`

`When something dies, push that hotkey as you are standing over the`  
`corpse. This should loot everything.`

`This code based upon Wat4rez.mac by FaNTuM. Changed from Wait4rez.mac to`  
`loot.mac at the following URL:`

[`http://www.macroquest2.com/wiki/index.php/Editing_Existing_Macros`](https://macroquest2.com/wiki/index.php/Editing_Existing_Macros)

`**|`  
````` \| --------------```\| -- Main Sub --````` \| --------------```Sub Main``  
`/declare t int outer 0`  
`/declare loottotal int outer`  
`/declare lootslot int outer`  
`/declare lootleft int outer 0`  
`/if (!${Defined[Param0]}) {`  
`} else {`  
`/varset lootleft ${Param0}`  
`}`  
`/tar corpse`  
`/loot`  
`| -----------------`  
`| -- Count items --`  
`| -----------------`  
`/delay 3s`  
`:LootLag`  
`/if (${loottotal}!=${Corpse.Items}) {`  
`/varset loottotal ${Corpse.Items}`  
`/delay 2s`  
`/goto :LootLag`  
`}`  
`/if (${loottotal}<=${lootleft}) {`  
`/notify LootWnd DoneButton leftmouseup`  
`/return`  
`}`  
`/varset loottotal ${Math.Calc[${Corpse.Items}-${lootleft}]}`  
`| ---------------------`  
`| -- Loot the corpse --`  
`| ---------------------`  
`/for lootslot 1 to ${loottotal}`  
`:LootItem`  
`/itemnotify loot${lootslot} rightmouseup`  
`/delay 5 !${Corpse.Item[${lootslot}].ID}`  
`/if (!${Corpse.Item[${lootslot}].ID}) {`  
`/next lootslot`  
`} else {`  
`/goto :LootItem`  
`}`  
`| -----------------`  
`| -- Doublecheck --`  
`| -----------------`  
`/if (${Math.Calc[${Corpse.Items}-${lootleft}]}>0) /goto :LootLag`  
`/notify LootWnd DoneButton leftmouseup`  
`/return`

