# MQ2DataVars

**MQ2Data was designed so that accessing information could be done utilizing a uniform system. User variables are treated as MQ2Data** [**Top-Level Objects**](../reference/top-level-objects/README.md)**.**

## Variable Basics

1. Default _scope_ is local
2. Default _type_ is string
3. Default _value_ is nothing (empty string or 0)

### Scopes

* **global**

Variables of global scope ALWAYS exist until they are deleted or MacroQuest ends

* **outer**

Variables of outer scope exist while a macro is running

* **local** (default)

Variables of local scope only exist while within a macro function or "Sub"

### Types

Variables can be declared as any of the types in [Data Types](../reference/data-types/README.md). The default type is string.

### Names

Only the following characters are allowed in the name of a variable: [a-z\]\[A-Z\]\[0-9]\_

Name lookup is case insensitive.

## Manipulating Variables

### Declaring

Variables are declared (initially defined) in the following format:

```text
/declare varname|varname[array extents] [type] [local|global|outer] [defaultvalue]
```

The parameters must be given in order, but any after _varname_ may be skipped to use the default.

**Some Examples**

1. This creates an int variable named MyVar that exists while the macro is running:

```text
/declare MyVar int outer
```

This creates a string variable named MyVar that exists within the Sub it was created in:

```text
/declare MyVar local
```

This creates a timer named MyTime that is set to 3000 at creation and exists while the macro is running:

```text
/declare MyTimer timer outer 3000
```

### Arrays

To create an array, attach square brackets to the end of the variable name and place in it the number of elements per dimension.

**Array Examples**

1. This creates a single-dimension local array of int with 10 elements (1-10) all 0:

```text
/declare MyArray[10] int
```

This creates a 2-dimensional 10x10 elements(1-10,1-10) int array of scope outer with all values of 5:

```text
/declare MyArray[10,10] int outer 5
```

This creates a 3-dimensional array with 4x5x6 elements (1-4,1-5, 1-6) with UNDEFINED-ARRAY-ELEMENT in each location:

```text
/declare MyArray[4,5,6] string outer UNDEFINED-ARRAY-ELEMENT
```

There is no limit to the number of dimensions or the number of elements in each dimension but use your own good judgment.

**Note:** You cannot make an array of timers.

### Deleting Variables

[/deletevar](../reference/commands/deletevar.md) is used to delete variables. Examples:

1. Deletes the variable varname. Using \* global will delete all global variables:

```text
/deletevar varname [* global]
```

Sets a variable directly to a new value. Keep in mind that the type itself may reject this value depending on what you give it.

```text
/varset varname [newvalue]
```

To clear the value of the variable, you may omit the new value.

### Setting/Changing Variables

[/varset](../reference/commands/varset.md) is used to set or change a variable. Examples:

1. This concatenates (joins one to the other) "stuff" to the end a string variable:

```text
/varset MyString ${MyString}stuff
```

This inserts stuff at the front of ${MyString}:

```text
/varset MyString stuff${MyString}
```

This sets MyInt to 123:

```text
/varset MyInt 123
```

This sets MyTimer to 123 seconds:

```text
/varset MyTimer 123s
```

This sets MyFloat to 1.23:

```text
/varset MyFloat 1.23
```

This sets array element n to 123:

```text
/varset MyIntArray[n] 123
```

### Setting Variables to Results of Calculations

You can use [/varcalc](../reference/commands/varcalc.md) to set a variable directly to the numeric result of a calculation. Keep in mind that the type itself may reject this value depending on what you give it. _**This will NOT work on strings!**_

**Examples:**

```text
 /varcalc MyInt 1+2*2+1
 /varcalc MyInt 1+(2*2)+1
 /varcalc NumBuffSlots ${Me.FreeBuffSlots}+${Me.CountBuffs}
```

### Setting Variables to the Result of MQ2Data Strings

```text
/vardata varname newMQ2Datavalue
```

Sets a variable directly to the end result of a MQ2Data string. To use this, do NOT put ${} around the outer data to parse.

_This is most useful for when you want to keep the result of something instead of trying to make the variable accept a string with /varset._

**For Example:**

```text
/vardata MyFloat Math.Calc[${Me.X}+${Me.Y}]
```

## Parsing

It is important to note that parsing of variables is performed from the inside to the outside, so any ${} inside your MQ2Data statement gets evaluated before continuing.

**Example**

`${MyString${MyVar}}`

The parser first evaluates ${MyVar}. If MyVar's value is 1, this gives us ${MyString1}. ${MyString1} is then evaluated, giving the value of whatever MyString1 is. ${${MyString}} will get the value of a MQ2Data query stored in MyString. This could be Me.Buff[1], or a variable name, or anything that is valid inside ${}. There is no limit to this recursion.

`${${${${${${${${${${MyString}}}}}}}}}}` will evaluate inside to outside until there is nothing left to evaluate.

This is also true for arrays: `${MyArray[${MyInt}]}` has no problems.

