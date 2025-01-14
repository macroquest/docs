# Spawn Search

All [Top-Level Objects](../top-level-objects/), [Data Types](../data-types/) and [Commands](../commands/) that support searching for spawns can take the following options:

| Parameter | Description |
| :--- | :--- |
| _**Anything Else**_ | Anything not matched below is considered a **name** |
| **=** | Exact name |
| _#_ | Any number is considered the minimum level |
| **alert** _#_ | Spawns on your alert list _#_ |
| **any** | All types |
| **aura** | Auras |
| **banker** | NPC bankers |
| **banner** | Banners |
| **body** _bodytype_ | Spawns with the specified [_bodytype_](..general/body-types.md) |
| **campfire** | Campfires |
| **chest** | Chests |
| **class** _classname_ | Spawns with this class name (long name) |
| **corpse** | Corpses |
| **dps** | Returns Wizards, Rangers, Berserkers and Rogues |
| **fellowship** | Characters in your fellowship |
| **flyer** | Flying monsters |
| **gm** | GMs and Guides who have chosen to be visible |
| **group** | Group members |
| **guild** | Returns spawns in your own guild |
| **guildname** _name_ | Returns spawns with the specified guild name, if blank, returns players with any guild name.  |
| **healer** | Returns Druids, Clerics and Shaman |
| **id** _#_ | Spawn with ID _#_ |
| **knight** | Returns Paladins and Shadow Knights |
| **lfg** | All spawns Looking For Group |
| **light** _lightsource_ | Spawns with the specified _lightsource_ |
| **loc** _#x_ _#y_ [_#z_] | Spawn at the specified loc, z is optional (defaults to your Z). Must be used with radius |
| **los** | Spawns in Line of Sight |
| **mercenary** | Mercenaries |
| **merchant** | NPC Merchants |
| **mount** | Mounts |
| **named** | "Named" spawns (spawns whose names start with a \#, or whose name does not start with "a" or "an") |
| **nearalert** _#_ | Spawns near alert list _#_ |
| **next** | Next spawn matching the search criteria (when using [/mqtarget](../commands/mqtarget.md)) |
| **noalert** _#_ | Spawns not on alert list _#_ |
| **nogroup** | Characters that aren't in your group |
| **noguild** | Spawns with no guild tag |
| **nopcnear** _#_ | Spawns with no players within specified radius (defaults to 200) |
| **nopet** | Not a pet |
| **notid** _#_ | Spawns not matching ID _#_ |
| **notnearalert** _#_ | Spawns not near alert list _#_ |
| **npc** | Non-Player Characters |
| **npccorpse** | Non-Player Characters Corpses |
| **npcpet** | Pets Owned by Non-Player Characters |
| **object** | Objects |
| **pc** | Player Characters (default) |
| **pccorpse** | Player corpses |
| **pcpet** | Pets Owned by Player Characters |
| **pet** | Pets |
| **playerstate** _#_ | Spawns that match the PlayerState int |
| **prev** | Previous spawn matching the search criteria (when using [/mqtarget](../commands/mqtarget.md))|
| **race** _racename_ | Spawns with the race _racename_ |
| **radius** _#_ | Within the radius _#_ |
| **raid** | Characters who are in your raid |
| **range** _low#_ _high#_ | Within the level range _low#_ and _high#_ |
| **slower** | Returns Shamans, Enchanters, Beastlords, and Bards |
| **tank** | Returns Paladins, Shadow Knights and Warriors |
| **targetable** | Spawns that can be targeted |
| **timer** | Timer spawns |
| **trader** | Characters who are in trader mode |
| **trap** | Traps |
| **tribute** | Tribute Masters |
| **trigger** | Triggers |
| **untargetable** | Untargettable spawns |
| **xtarhater** | Spawn on my xtarget list that hates me |
| **zradius** _#_ | Spawns within the specified Z-Axis radius |

## See also

- [Spawn (Top-Level Object)](../top-level-objects/tlo-spawn.md)
- [spawn (DataType)](../data-types/datatype-spawn.md)
- [/who](../commands/who.md)
- [/alert](../commands/alert.md)
- [/mqtarget](../commands/mqtarget.md)
- [NearestSpawn (Top-Level Object)](../top-level-objects/tlo-nearestspawn.md)
