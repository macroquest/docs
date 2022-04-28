# MQ2Data

## MQ2Data Types

MQ2Data types are the means by which properties or methods ([Data Types](../data-types-and-top-level-objects/data-types/)\) of TLOs \([Top-Level Objects](../data-types-and-top-level-objects/top-level-objects/)) are accessed and used within macros. [Variables](mqdatavars.md) in MQ2 are treated as [Top-Level Objects](../data-types-and-top-level-objects/top-level-objects/).

The basic syntax for accessing this MQ2Data is:

`${TopLevelObject[index].Member[index].Member[index]}`

To access a property of a TLO you begin with the TLO type you want, then append successive type members or properties until you get the result you're looking for. The use of properties can become very complex (ie. extremely long), especially when using ${Math.Calc[]}.

**Note:** You absolutely MUST pay attention to the return types of each member and object. Make sure to always compare identical [Data Types](../data-types-and-top-level-objects/data-types/) when doing comparisons (eg. string to a string, or a numeric to a numeric). Using .Equal or .NotEqual to compare .Name to .ID will give errors. For example, ${Target.Name.Equal[${Me.ID}]} will not work. .Name returns a string, but .ID returns an int

Also be sure to look at the To String of each type.

**Example of building an MQ2Data string:**

* Suppose you want to display the distance to an NPC that you have targeted.
* First, check the page for [TLO:Target](../data-types-and-top-level-objects/top-level-objects/tlo-target.md). There you can see its forms listed as

  "[_spawn_](../data-types-and-top-level-objects/data-types/datatype-spawn.md) **Target**". This indicates that the Target TLO has access to all the

  [_spawn_](../data-types-and-top-level-objects/data-types/datatype-spawn.md) reference type members.

* Looking at the [_spawn_](../data-types-and-top-level-objects/data-types/datatype-spawn.md) reference type, you will find a list of the properties and

  members of spawn, to which **Target** has access to.

* Since you want to find the distance to the target, you would select one of the Distance members. For this example we

  will use:

[_float_](../data-types-and-top-level-objects/data-types/datatype-float.md) **Distance**

Distance from player in (x,y)

* So you append append .Distance to the TLO name to get: Target.Distance
* Once you have gotten to the information you want, you MUST enclose the entire string in ${ }, so the end result of

  the example would be:

`/echo Distance to target is: ${Target.Distance}`

* This returns the distance to your target in the float format \#\#\#.\#\#

**Note:** All TLOs and reference data types have access to immediate types, but ensure you use the appropriate members of the immediate types with reference types or TLOs. For example, if you wanted to convert the above float value Distance, to an int value, you could append one of the members of the float immediate type, to make it:

`/echo Distance to target is: ${Target.Distance.Int}`

## MQ2Data Members

Members can also be describd as Properties or things that are property (owned by, contained by, etc) of objects of a type.

For example, the **Desk** type of object might have a property called **Screws**. The **Screws** property itself might be represented like this:

[_int_](../data-types-and-top-level-objects/data-types/datatype-int.md) **Screws**

_int_ is a type of object which means WHOLE NUMBER while **Screws** is the name of the object

To demonstrate that an object named **Screws** is a member of the **Desk** type, we may also say:

[_int_](../data-types-and-top-level-objects/data-types/datatype-int.md) **Desk.Screws**

The return type is of the last member appended (ie. int).

## MQ2Data Inheritance

Inheritance is a way to get less specific about what "type" of object you are looking at. For example, say you have two types, like **desk** and **woodendesk**.

* All wooden desks are desks, but not all desks are wooden desks.
* So now we have

_woodendesk_ **ThisDesk**

* Remember that "desk" we said has a member called **Screws** of type _int_. "woodendesk" IS a desk, so it

  automatically gets a member called **Screws**.

* Therefore, "ThisDesk.Screws", even though it is a wooden desk and not just "desk", is valid.

