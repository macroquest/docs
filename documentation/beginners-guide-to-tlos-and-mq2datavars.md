## Introduction

[Top-Level Objects](../top-level-objects/top-level-objects.md) (TLOs) are basically "built-in" global variables which contain
information from the EQ client.

## Usage

In order to use these built-in variables, you need to pick a Top-Level Object to start with, and then "build" the
variable by adding one or more [DataType](../data-types/data-types.md) members of that TLO. It's best understood with some
examples. **Note:** TLOs and members are all case sensitive, so enter them exactly as seen.

### Example 1: Mana Percentage

Say you want to display your current Mana Percentage in a [HUD](../plugins/mq2hud.md) or use it in a macro.

-   First off, you look through the [list of TLOs](../top-level-objects/top-level-objects.md) and pick one that best suits the
    information you're looking for. The [Me TLO](../top-level-objects/tlo-me.md) looks like a good bet.
-   Opening that page, you see that the Me TLO has access to the [*character*](../data-types/datatype-character.md) datatype
    and the [*spawn*](../data-types/datatype-spawn.md) datatype. The *character* datatype contains information about your own
    character, mostly things that only you will know (eg. how much mana you have, what spells you have loaded, etc).
    Since your character is also a spawn in the EQ world (ie. other people can see you and interact with you), you are
    also able to access the *spawn* datatype, which gives information that other characters in the same zone may know
    (eg. your location, your race, your class, etc).
-   Since we're looking for your Mana Percentage, this is something that only you can know, so choose the *character*
    datatype page.
-   This will display a list of all the members that are available to *character*. In the front of each datatype is an
    italic word, which is the datatype that the member belongs to. It may seem a bit confusing right now but should get
    easier as we progress to more complex examples.
-   Scroll down the list until you find a member that looks like it will give us what we need. The **PctMana** member
    looks good.
-   The *int* in front of **PctMana** shows that it is an integer. Since we're expecting a number, this seems correct.
-   Click on the *[int](../data-types/datatype-int.md)* link and you'll notice another table similar to the *character*
    datatype. This table has all the members of the *int* datatype. Note that the bottom line of the list is **To
    String**, which is the default for the datatype. The default for the *int* datatype is the number. Since we're just
    looking for the number, we can stop here.
-   So now we can "build" our variable. Remember, all variables start with a $-sign and are surrounded by braces { }. We
    start with our TLO:

`${Me`

-   Then we add a period to indicate that we want to include a member of **Me**:

`${Me.`

-   Now we add the first datatype, **PctMana**:

`${Me.PctMana`

-   Now **PctMana** is an *int* and the default for *int* is just the number, so we don't need to add any members of
    *int*. So we can close off the variable now:

`${Me.PctMana}`

-   To test this variable, you can echo it in the EQ client. So typing the following will echo your mana percentage to
    the MQ2 chat window:

`/echo ${Me.PctMana}`

### Example 2: Class ShortName

Next example deals with getting your class shortname (the 3-letter abbreviation of your class).

-   First, find the most likely TLO again. Again, the [Me TLO](../top-level-objects/tlo-me.md) looks best.
-   Next find the member you would like to select. To find the members of **Me**, go to
    [Character](../data-types/datatype-character.md)
-   Scrolling through the members of **Me**, **Class** looks like the best candidate.
-   The *class* datatype has a default of "Same as Name". Looking at the **Name** member, we can see that it is the
    "long name" of the class (eg. Enchanter). We're actually looking for the short name, so we need to find a member of
    *class* found here [Class](../data-types/datatype-class.md). Funny enough, **ShortName** looks like it will do the job.
-   **ShortName** is a *string* datatype and the default for this datatype (surprisingly) is the string, and since we're
    looking for a 3-letter string, this is perfect. So now we've found our end point, we can build the variable as
    before.
-   Start with the TLO:

`${Me`

-   Add the first member

`${Me.Class`

-   Since we need a member of **Class**, we add another period and the next member

`${Me.Class.ShortName`

-   We've now arrived at the end of our variable, so we "close" it here

`${Me.Class.ShortName}`

-   Again, to test, we echo the variable and see that the result is what we expect.

`/echo ${Me.Class.ShortName}`

### Example 3: Comparison using a string

For the next example, we will use the variable and compare it to a string in an if statement. Lets say we want to echo
something if we're a bard, and something else if we're not.

-   We'll be using the same **ShortName** example as above, but since we don't just want to echo the current short name,
    we have to go a step further.
-   Go back to the **ShortName** member and you'll see that it is a *string* datatype.
-   Under the *string* datatype, you'll see the **Equals** member. This is the one we'll be using. **Equals** is a
    *bool* datatype, which means that it doesn't have any members. It will return 1 if true and 0 if false, which is
    good enough for our test.
-   In the following example, I'll be using an /if statement. For the purposes of this example, you don't need to
    understand how they work, but they're the staple of MQ2, so it's a good idea to have a look at the [Flow
    Control](flow-control.md) page and familiarize yourself with /if and its friends.
-   Returning to the example though, lets build the variable. We'll start with where we left off in the previous
    example. Since we want to access a member of **ShortName**, we won't close it off:

`/if (${Me.Class.ShortName`

-   You'll notice that the **Equals** datatype has square brackets after it, which means that you need to enter
    something between the brackets. This can be another variable, or just a string. For this example, we're checking if
    we're a bard:

`/if (${Me.Class.ShortName.Equals[BRD]`

-   Remember that we're using **ShortName**, so we need to include the 3-letter abbreviation. Since this is the end of
    the variable (**Equals** is a *bool*), we can close it off:

`/if (${Me.Class.ShortName.Equals[BRD]}`

-   But this is actually an /if statement, and we need to close that off to, so lets make it echo something if we're a
    bard.

`/if (${Me.Class.ShortName.Equal[BRD]}) {`  
`  /echo Catch me if you can!`  
`}`

-   We'll flesh this out a bit more by echoing one thing if we're a bard and another if we're not:

`/if (${Me.Class.ShortName.Equal[BRD]}) {`  
`  /echo Catch me if you can!`  
`} else {`  
`  /echo Nerf bards!`  
`}`


