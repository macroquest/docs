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

Links to pages (See sidebar for full list)

| | | | | |
| -- | -- | -- | -- | -- |
| [Achievement](tlo-achievement)  | [Familiar](tlo-familiar)                   | [Heading](tlo-heading)         | [Mercenary](tlo-mercenary)       | [Spell](tlo-spell)   |
| [AdvLoot](tlo-advloot)          | [FindItem](tlo-finditem)                   | [If](tlo-if)                   | [Mount](tlo-mount)               | [Switch](tlo-switch) |
| [Alert](tlo-alert)              | [FindItemBank](tlo-finditembank)           | [Illusion](tlo-illusion)       | [NearestSpawn](tlo-nearestspawn) | [Target](tlo-target) |
| [Alias](tlo-alias)              | [FindItemBankCount](tlo-finditembankcount) | [Ini](tlo-ini)                 | [Pet](tlo-pet)                   | [Task](tlo-task)     |
| [AltAbility](tlo-altability)    | [FindItemCount](tlo-finditemcount)         | [Int](tlo-int)                 | [Plugin](tlo-plugin)             | [Time](tlo-time)     |
| [Bool](tlo-bool)                | [Float](tlo-float)                         | [ItemTarget](tlo-itemtarget)   | [Raid](tlo-raid)                 | [Type](tlo-type)     |
| [Corpse](tlo-corpse)            | [FrameLimiter](tlo-framelimiter)           | [LastSpawn](tlo-lastspawn)     | [Range](tlo-range)               | [Window](tlo-window) |
| [Defined](tlo-defined)          | [Friends](tlo-friends)                     | [LineOfSight](tlo-lineofsight) | [Select](tlo-select)             | [Zone](tlo-zone)     |
| [DisplayItem](tlo-displayitem)  | [GameTime](tlo-gametime)                   | [Macro](tlo-macro)             | [SelectedItem](tlo-selecteditem) |                      |
| [DoorTarget](tlo-doortarget)    | [Ground](tlo-ground)                       | [MacroQuest](tlo-macroquest)   | [Skill](tlo-skill)               |                      |
| [DynamicZone](tlo-dynamiczone)  | [GroundItemCount](tlo-grounditemcount)     | [Math](tlo-math)               | [Spawn](tlo-spawn)               |                      |
| [EverQuest](tlo-everquest)      | [Group](tlo-group)                         | [Me](tlo-me)                   | [SpawnCount](tlo-spawncount)     |                      |
