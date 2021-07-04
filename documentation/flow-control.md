# Flow Control

MQ2 provides a few ways to control the execution of your macro.

* If/else decisions
* While loops
* For loops
* Goto jumps

## If/else decisions

* If statement blocks are the most common form of flow control in MQ2.
* The syntax for an _/if_ statement can be found [here](../commands/macro-commands/if.md).
* The simplest statements are one-liners like the following:

  ```text
  /if (${Me.Sitting}) /stand
  ```

  This will stand you up if you're sitting.

\*One-line [/if](../commands/macro-commands/if.md) statements do not require curly braces \( {} \)

* If you wish to execute more than one command, you must wrap your set of commands in braces:

```text
/if (${Me.Sitting}) {
  /stand
  /echo I'm standing now!
}
```

\*If statements can also match multiple conditions for fine-grained control:

```text
/if (${Me.Standing} && !${Me.Combat} && !${Me.Casting.ID}) {
  /sit
  /echo Medding now
}
```

The above example will only be matched if you're currently standing **and** you're not in combat **and** you're not casting. Any of the [Operators](operators.md) can be used to "fine-tune" the matching of any conditions. Also, brackets can be used to group certain sets of statements together.

```text
/if ( (${Me.Sitting} && !${Window[SpellBookWnd].Open}) || ${Me.Standing} ) /call Cast "Complete Healing" 10s
```

This will only cast the spell if:

* I'm sitting **and** the spellbook window is not open

**OR**

* I'm standing.

You will also need the curly braces any time you're using _else_ or _else if_ statements. An example:

```text
/if (${Me.Sitting}) {
  /stand
  /echo I'm standing now!
} else {
  /echo I'm already standing
}
```

Else blocks are extremely useful for catching "everything else" that is not matched by the [/if](../commands/macro-commands/if.md) statement.

You can go one further and add some further matching with additional /if statments, like the following:

```text
/declare random int local ${Math.Rand[10]}
/if (${random}<=3) {
  /echo The number is less than or equal to 3
} else /if (${random}<=5) {
  /echo The number is less than or equal to 5
} else /if (${random}<=8) {
  /echo The number is less than or equal to 8
} else {
  /echo The number is 9 or higher
}
```

You can also nest /if statements within other /if statements, to make your matching and macro flow very powerful.

## While loops

Similar to for loops, while loops can be used to execute a series of commands as long as a certain set of conditions are or are not true.

```text
/while (${Me.PctHPs}<100 || ${Me.PctMana}<100) {
 /if (${Me.Standing}) {
  /echo Sitting because I am standing.
   /sit
 }
 /echo Resting until my hitpoints (${Me.PctHPs}%) and mana (${Me.PctMana}%) are at 100%.
 /delay 6s
}
```

You can end a /while loop immediately with /break or try the next iteration with /continue

## See also /while

* [/while](../commands/macro-commands/while.md)
* [/break](../commands/macro-commands/break.md)
* [/continue](../commands/macro-commands/continue.md)

## For loops

For loops are used when you want to perform the same set of commands on a list of items. With a /for loop, you define a starting number, an end number and \(if necessary\) a number to increment by. The loop will perform the set of commands with the starting number, then will increment it \(by 1 as a default, unless you specify the number\) and will then re-run all the commands with the next number. It will continue to do that until it reaches the end number, at which time it will exit.

Take this example, which will give a list of all your buff slots:

```text
/declare x int local
/for x 1 to 15
 /echo Buff ${x} is ${Me.Buff[${x}]}
/next x
```

The problem with this example is that you'll get a couple of NULLs if you have no buffs in those slots, so we can further refine the loop to make use of an [/if](../commands/macro-commands/if.md) statement as well, like this:

```text
/declare x int local
/for x 1 to 15
 /if (${Me.Buff[${x}].ID}) /echo Buff ${x} is ${Me.Buff[${x}]}
/next x
```

This will have a look and see if the buff in slot ${x} has an ID \(remember that /if statements only deal with numbers\) and if the number is positive \(ie. not 0\), then it will echo the buff name.

You could easily list the buffs in reverse order by using "downto" instead of "to" in the /for loop.

```text
/declare x int local
/for x 15 downto 1
 /if (${Me.Buff[${x}].ID}) /echo Buff ${x} is ${Me.Buff[${x}]}
/next x
```

You can end a /for loop immediately with /break or try the next iteration with /continue.

## See also /for

* [/for](../commands/macro-commands/for.md)
* [/break](../commands/macro-commands/break.md)
* [/continue](../commands/macro-commands/continue.md)

## Goto jumps

As with most programming and scripting languages, the use of the "goto" function is frowned upon \(generally because it's slow and there are better ways of achieving the same result\). In MQ2 it's not much different, and since MQ2 originally didn't include any type of "while" function, many older macros still include goto statements.

First off, you need a marker to denote where the [/goto](../commands/macro-commands/goto.md) function should move to. A marker is created in the following format:

```text
:marker
```

To utilize that marker with a [/goto](../commands/macro-commands/goto.md) statment, do something like the following:

```text
Sub Main
  /echo start here

  :marker
  /echo just passed the marker
  /goto :marker
/return
```

In the above example, your MQ2 chat window would be filled with "just passed the marker" echoed constantly until you ended the macro. We've created an infinite loop above, which is the most common use of /goto. A conditional /goto \(ie. a /goto after an /if statment\) is the closest you can get to a "while" function. Take the following example:

```text
Sub Main
  /declare num int local 1
  :marker
  /echo Number is ${num}
  /varcalc ${num} ${num}+1
  /if (${num}<=5) /goto :marker
/return
```

This would output:

```text
[MQ2] Number is 1
[MQ2] Number is 2
[MQ2] Number is 3
[MQ2] Number is 4
[MQ2] Number is 5
```

The macro echoes "${num}" and then increments it by one. If the total is less than or equal to 5, it loops back to the start. If the total is above 5, it won't loop back and will end naturally.

## :OnExit

Anything included after that label will be called whenever an /endmacro command is issued. To use this feature, the label must be at the end of your 'Sub Main' function and end with a /return. Please note that this is NOT required of macros, so no macros will have to be altered unless you wish to take advantage of this feature.

OnExit will not function upon a macro ending while paused.

example:

```text
Sub Main
/while (1) {
  /delay 5
}
/return
  :OnExit
  /echo Should run on exit. 
  /return
```

