# Top-Level Objects

## Overview

A "Top-Level Object" is any kind of object that you can start with when trying to find a property.

* The TLO type is indicated by the italic text preceding the TLO name \(in bold\)
* The TLO has access to all of the members of its type
* The TLO name is static and cannot be changed

TLOs are called Top-Level Objects because nothing comes before them. A TLO is not a member of any object, it is itself an object. However, the TLO has access to all members and properties of its datatype, and any inherited members of its datatype.

### Example

[_character_](../data-types/datatype-character.md) **Me** is a Top Level Object of type [_character_](../data-types/datatype-character.md). **Me** has access to the members of the _character_ type, but **Me** is not the _character_ type. You will notice that the _character_ datatype inherits the _spawn_ datatype, which gives the **Me** TLO access to both the _character_ and _spawn_ members.

The immediate datatype named _int_ and the Top Level Object named **Int** are not the same thing.

A [Beginners Guide to TLOs and MQ2DataVars](../../documentation/beginners-guide-to-tlos-and-mq2datavars.md) may be useful for understanding how TLOs work.

## Built-in Top-Level Objects

<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-achievement.md">TLO:Achievement</a> &#x1F195;</li>
          <li><a href="tlo-advloot.md">TLO:AdvLoot</a>
          </li>
          <li><a href="tlo-alert.md">TLO:Alert</a>
          </li>
          <li><a href="tlo-alias.md">TLO:Alias</a>
          </li>
          <li><a href="tlo-altability.md">TLO:AltAbility</a>
          </li>
          <li><a href="tlo-bandolier.md">TLO:Bandolier</a>
          </li>
          <li><a href="tlo-bool.md">TLO:Bool</a>
          </li>
          <li><a href="tlo-corpse.md">TLO:Corpse</a>
          </li>
          <li><a href="tlo-cursor.md">TLO:Cursor</a>
          </li>
          <li><a href="tlo-defined.md">TLO:Defined</a>
          </li>
          <li><a href="tlo-displayitem.md">TLO:DisplayItem</a>
          </li>
          <li><a href="tlo-doortarget.md">TLO:DoorTarget</a>
          </li>
          <li><a href="tlo-dynamiczone.md">TLO:DynamicZone</a>
          </li>
          <li><a href="tlo-event.md">TLO:Event</a>
          </li>
          <li><a href="tlo-everquest.md">TLO:EverQuest</a>
          </li>
          <li><a href="tlo-familiar.md">TLO:Familiar</a>
          </li>
          <li><a href="tlo-finditem.md">TLO:FindItem</a>
          </li>
          <li><a href="tlo-finditembank.md">TLO:FindItemBank</a>
          </li>
          <li><a href="tlo-finditembankcount.md">TLO:FindItemBankCount</a>
          </li>
          <li><a href="tlo-finditemcount.md">TLO:FindItemCount</a>
          </li>
          <li><a href="tlo-float.md">TLO:Float</a>
          </li>
          <li><a href="../../plugins/discontinued-unsupported/mq2fps/tlo-fps.md">TLO:FPS</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-friends.md">TLO:Friends</a>
          </li>
          <li><a href="tlo-gametime.md">TLO:GameTime</a>
          </li>
          <li><a href="tlo-ground.md">TLO:Ground</a>
          </li>
          <li><a href="tlo-grounditemcount.md">TLO:GroundItemCount</a>
          </li>
          <li><a href="tlo-group.md">TLO:Group</a>
          </li>
          <li><a href="tlo-heading.md">TLO:Heading</a>
          </li>
          <li><a href="tlo-if.md">TLO:If</a>
          </li>
          <li><a href="tlo-illusion.md">TLO:Illusion</a>
          </li>
          <li><a href="tlo-ini.md">TLO:Ini</a>
          </li>
          <li><a href="tlo-int.md">TLO:Int</a>
          </li>
          <li><a href="tlo-itemtarget.md">TLO:ItemTarget</a>
          </li>
          <li><a href="tlo-lastspawn.md">TLO:LastSpawn</a>
          </li>
          <li><a href="tlo-lineofsight.md">TLO:LineOfSight</a>
          </li>
          <li><a href="tlo-macro.md">TLO:Macro</a>
          </li>
          <li><a href="tlo-macroquest.md">TLO:MacroQuest</a>
          </li>
          <li><a href="tlo-math.md">TLO:Math</a>
          </li>
          <li><a href="tlo-me.md">TLO:Me</a>
          </li>
          <li><a href="tlo-mercenary.md">TLO:Mercenary</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-merchant.md">TLO:Merchant</a>
          </li>
          <li><a href="tlo-mount.md">TLO:Mount</a>
          </li>
          <li><a href="tlo-nearestspawn.md">TLO:NearestSpawn</a>
          </li>
          <li><a href="tlo-pet.md">TLO:Pet</a>
          </li>
          <li><a href="tlo-plugin.md">TLO:Plugin</a>
          </li>
          <li><a href="tlo-raid.md">TLO:Raid</a>
          </li>
          <li><a href="tlo-range.md">TLO:Range</a>
          </li>
          <li><a href="tlo-select.md">TLO:Select</a>
          </li>
          <li><a href="tlo-selecteditem.md">TLO:SelectedItem</a>
          </li>
          <li><a href="tlo-skill.md">TLO:Skill</a>
          </li>
          <li><a href="tlo-spawn.md">TLO:Spawn</a>
          </li>
          <li><a href="tlo-spawncount.md">TLO:SpawnCount</a>
          </li>
          <li><a href="tlo-spell.md">TLO:Spell</a>
          </li>
          <li><a href="tlo-switch.md">TLO:Switch</a>
          </li>
          <li><a href="tlo-target.md">TLO:Target</a>
          </li>
          <li><a href="tlo-task.md">TLO:Task</a>
          </li>
          <li><a href="tlo-time.md">TLO:Time</a>
          </li>
          <li><a href="tlo-type.md">TLO:Type</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="tlo-window.md">TLO:Window</a>
          </li>
          <li><a href="tlo-zone.md">TLO:Zone</a>
          </li>
        </ul>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

