# Top-Level Objects

A "Top-Level Object" is any kind of object that you can start with when trying to find a property.

* The TLO type is indicated by the italic text preceding the TLO name (in bold)
* The TLO has access to all of the members of its type
* The TLO name is static and cannot be changed

TLOs are called Top-Level Objects because nothing comes before them. A TLO is not a member of any object, it is itself an object. However, the TLO has access to all members and properties of its datatype, and any inherited members of its datatype.

### Example

**[Me](tlo-me.md)** is a Top Level Object of type [_character_](../data-types/datatype-character.md). **Me** has access to the members of the _character_ type, but **Me** is not the _character_ type. You will notice that the _character_ datatype inherits the _spawn_ datatype, which means the TLO **Me** will have access to both the _character_ and _spawn_ members.

``` mermaid
classDiagram
  Me *-- character
  character <|-- spawn
  class Me {
     Int Level
     String Loc
  }
  class character {
    Int Level
  }
  class spawn {
    String Loc
  }
```

The immediate datatype named _int_ and the Top Level Object named **Int** are not the same thing.

A [Beginners Guide to TLOs and MQ2DataVars](../../documentation/beginners-guide-to-tlos-and-datavars.md) may be useful for understanding how TLOs work.