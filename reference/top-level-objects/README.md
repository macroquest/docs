
# Top-Level Objects

<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-Achievement">Achievement</a>
          </li>
          <li><a href="tlo-AdvLoot">AdvLoot</a>
          </li>
          <li><a href="tlo-Alert">Alert</a>
          </li>
          <li><a href="tlo-Alias">Alias</a>
          </li>
          <li><a href="tlo-AltAbility">AltAbility</a>
          </li>
          <li><a href="tlo-Bool">Bool</a>
          </li>
          <li><a href="tlo-Corpse">Corpse</a>
          </li>
          <li><a href="tlo-Defined">Defined</a>
          </li>
          <li><a href="tlo-DisplayItem">DisplayItem</a>
          </li>
          <li><a href="tlo-DoorTarget">DoorTarget</a>
          </li>
          <li><a href="tlo-DynamicZone">DynamicZone</a>
          </li>
          <li><a href="tlo-EverQuest">EverQuest</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-Familiar">Familiar</a>
          </li>
          <li><a href="tlo-FindItem">FindItem</a>
          </li>
          <li><a href="tlo-FindItemBank">FindItemBank</a>
          </li>
          <li><a href="tlo-FindItemBankCount">FindItemBankCount</a>
          </li>
          <li><a href="tlo-FindItemCount">FindItemCount</a>
          </li>
          <li><a href="tlo-Float">Float</a>
          </li>
          <li><a href="tlo-FrameLimiter">FrameLimiter</a>
          </li>
          <li><a href="tlo-Friends">Friends</a>
          </li>
          <li><a href="tlo-GameTime">GameTime</a>
          </li>
          <li><a href="tlo-Ground">Ground</a>
          </li>
          <li><a href="tlo-GroundItemCount">GroundItemCount</a>
          </li>
          <li><a href="tlo-Group">Group</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-Heading">Heading</a>
          </li>
          <li><a href="tlo-If">If</a>
          </li>
          <li><a href="tlo-Illusion">Illusion</a>
          </li>
          <li><a href="tlo-Ini">Ini</a>
          </li>
          <li><a href="tlo-Int">Int</a>
          </li>
          <li><a href="tlo-ItemTarget">ItemTarget</a>
          </li>
          <li><a href="tlo-LastSpawn">LastSpawn</a>
          </li>
          <li><a href="tlo-LineOfSight">LineOfSight</a>
          </li>
          <li><a href="tlo-Macro">Macro</a>
          </li>
          <li><a href="tlo-MacroQuest">MacroQuest</a>
          </li>
          <li><a href="tlo-Math">Math</a>
          </li>
          <li><a href="tlo-Me">Me</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-Mercenary">Mercenary</a>
          </li>
          <li><a href="tlo-Mount">Mount</a>
          </li>
          <li><a href="tlo-NearestSpawn">NearestSpawn</a>
          </li>
          <li><a href="tlo-Pet">Pet</a>
          </li>
          <li><a href="tlo-Plugin">Plugin</a>
          </li>
          <li><a href="tlo-Raid">Raid</a>
          </li>
          <li><a href="tlo-Range">Range</a>
          </li>
          <li><a href="tlo-Select">Select</a>
          </li>
          <li><a href="tlo-SelectedItem">SelectedItem</a>
          </li>
          <li><a href="tlo-Skill">Skill</a>
          </li>
          <li><a href="tlo-Spawn">Spawn</a>
          </li>
          <li><a href="tlo-SpawnCount">SpawnCount</a>
          </li>
        </ul>
      </th>
      <th style="text-align:Up">
        <ul>
          <li><a href="tlo-Spell">Spell</a>
          </li>
          <li><a href="tlo-Switch">Switch</a>
          </li>
          <li><a href="tlo-Target">Target</a>
          </li>
          <li><a href="tlo-Task">Task</a>
          </li>
          <li><a href="tlo-Time">Time</a>
          </li>
          <li><a href="tlo-Type">Type</a>
          </li>
          <li><a href="tlo-Window">Window</a>
          </li>
          <li><a href="tlo-Zone">Zone</a>
          </li>
        </ul>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>


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

A [Beginners Guide to TLOs and MQ2DataVars](../../macros/beginners-guide-datatypes.md) may be useful for understanding how TLOs work.
