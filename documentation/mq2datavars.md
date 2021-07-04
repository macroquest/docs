**MQ2Data was designed so that accessing information could be done utilizing a uniform system. User variables are
treated as MQ2Data [Top-Level Objects](../top-level-objects/top-level-objects.md).**

## Variable Basics

1.  The default *scope* is local.
2.  The default *type* is string.
3.  The default *value* is nothing (empty string or 0).

### Scopes

-   **global**

Variables of global scope ALWAYS exist until they are deleted or macroquest ends

-   **outer**

Variables of outer scope exist while a macro is running

-   **local** (default)

Variables of local scope only exist while within a macro function or "Sub"

### Types

Variables can be declared as any of the types in [Data Types](../data-types/data-types.md). The default type is
[string](../data-types/datatype-string.md).

### Names

Only the following characters are allowed in the name of a variable: \[a-z\]\[A-Z\]\[0-9\]\_

Name lookup is case insensitive.

## Manipulating Variables

### Declaring

Variables are declared (initially defined) in the following format:

    /declare varname|varname[array extents] [type] [local|global|outer] [defaultvalue]

The parameters must be given in order, but any after *varname* may be skipped to use the default.

**Some Examples**

1.  This creates an int variable named MyVar that exists while the macro is running:

<!-- -->

    /declare MyVar int outer

<li>

This creates a string variable named MyVar that exists within the Sub it was created in:

</li>

    /declare MyVar local

<li>

This creates a timer named MyTime that is set to 3000 at creation and exists while the macro is running:

</li>

    /declare MyTimer timer outer 3000

</ol>

### Arrays

To create an array, attach square brackets to the end of the variable name and place in it the number of elements per
dimension.

**Array Examples**

1.  This creates a single-dimension local array of int with 10 elements (1-10) all 0:

<!-- -->

    /declare MyArray[10] int

<li>

This creates a 2-dimensional 10x10 elements(1-10,1-10) int array of scope outer with all values of 5:

</li>

    /declare MyArray[10,10] int outer 5

<li>

This creates a 3-dimensional array with 4x5x6 elements (1-4,1-5, 1-6) with UNDEFINED-ARRAY-ELEMENT in each location:

</li>

    /declare MyArray[4,5,6] string outer UNDEFINED-ARRAY-ELEMENT

There is no limit to the number of dimensions or the number of elements in each dimension, but use your own good
judgement.

</ol>

**Note:** You cannot make an array of timers.

### Deleting Variables

[/deletevar](../commands/deletevar.md) is used to delete variables. Examples:

1.  Deletes the variable varname. Using \* global will delete all global variables:

<!-- -->

    /deletevar varname [*|global]

<li>

Sets a variable directly to a new value. Keep in mind that the type itself may reject this value depending on what you
give it.

</li>

    /varset varname [newvalue]

To clear the value of the variable, you may omit the new value.

</ol>

### Setting/Changing Variables

[/varset](../macro-commands/varset.md) is used to set or change a variable. Examples:

1.  This concatenates (joins one to the other) "stuff" to the end a string variable:

<!-- -->

    /varset MyString ${MyString}stuff

<li>

This inserts stuff at the front of ${MyString}:

</li>

    /varset MyString stuff${MyString}

<li>

This sets MyInt to 123:

</li>

    /varset MyInt 123

<li>

This sets MyTimer to 123 seconds:

</li>

    /varset MyTimer 123s

<li>

This sets MyFloat to 1.23:

</li>

    /varset MyFloat 1.23

<li>

This sets array element n to 123:

</li>

    /varset MyIntArray[n] 123

</ol>

### Setting Variables to Results of Calculations

You can use [/varcalc](../macro-commands/varcalc.md) to set a variable directly to the numeric result of a calculation. Keep in
mind that the type itself may reject this value depending on what you give it. ***This will NOT work on strings!***

**Examples:**

     /varcalc MyInt 1+2*2+1 
     /varcalc MyInt 1+(2*2)+1 
     /varcalc NumBuffSlots ${Me.FreeBuffSlots}+${Me.CountBuffs}

### Setting Variables to the Result of MQ2Data Strings

    /vardata varname newMQ2Datavalue

Sets a variable directly to the end result of a MQ2Data string. To use this, do NOT put ${} around the outer data to
parse.

*This is most useful for when you want to keep the result of something instead of trying to make the variable accept a
string with /varset.*

**For Example:**

    /vardata MyFloat Math.Calc[${Me.X}+${Me.Y}]

## Parsing

It is important to note that parsing of variables is performed from the inside to the outside, so any ${} inside your
MQ2Data statement gets evaluated before continuing.

**Example**

`${MyString${MyVar}}`

The parser first evaluates ${MyVar}. If MyVar's value is 1, this gives us ${MyString1}. ${MyString1} is then evaluated,
giving the value of whatever MyString1 is. ${${MyString}} will get the value of a MQ2Data query stored in MyString. This
could be Me.Buff\[1\], or a variable name, or anything that is valid inside ${}. There is no limit to this recursion.

${${${${${${${${${${MyString}}}}}}}}}} will evaluate inside to outside until there is nothing left to evaluate.

This is also true for arrays: ${MyArray\[${MyInt}\]} has no problems.


