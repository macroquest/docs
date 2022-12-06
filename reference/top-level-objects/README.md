# Top-Level Objects

A "Top-Level Object" is any kind of object that you can start with when trying to find a property.

TLOs are called Top-Level Objects because nothing comes before them. A TLO is not a member of any object, it is itself an accessor to objects.

!!! Note

    A TLO provides access to _instances_ of datatypes.

    See Also: [DataType Reference](../data-types/)


The data that a TLO gives you may depend on the parameters that are provided. Most TLOs don't take any parameters (like **Me**). However, some TLOs return different data dependent on what is provided to them.
This is explained in the documentation by using the term **Forms**. A TLO with multiple **Forms** may return different datatypes depending on what is passed in.

### Examples

#### Me

**[Me](tlo-me)** is a Top Level Object that returns a [_character_](../data-types/datatype-character). **Me** has access to the members of the _character_ datatype, but **Me** is not the _character_ datatype. You will notice that the _character_ datatype inherits the _spawn_ datatype, which means the TLO **Me** will have access to both the _character_ and _spawn_ members.

#### Int

The datatype named [_int_](../data-types/datatype-int) and the Top Level Object named [**Int**](tlo-int) are not the same thing. 

The TLO is used to parse integer strings. the int datatype represents a numeric value.

## See Also

A [Beginners Guide to TLOs and MQ2DataVars](../../macros/beginners-guide-datatypes) may be useful for understanding how TLOs work.

## TLO List

See sidebar for full list.
