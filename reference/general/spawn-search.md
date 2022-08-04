
# Spawn Search

All [Top-Level Objects](../top-level-objects/README.md) and [Data Types](../data-types/README.md) that support searching for spawns, can take the following options:

| Parameter | Description |
| :--- | :--- |
| **alert \#** | Any spawns on the alert list \# |     
| * alert Examples:| `/alert add 1 id ${Me.ID}` `/alert add 1 ${Me.Name}`|
| **aura** | Auras |
| **body** _bodytype_ | Spawns with the specified _bodytype_ |
| **chest** | Chests |
| **class** _classname_ | Spawns with this class name (long name) |
| **corpse** | Corpses |
| **dps** | Returns Wizards, Rangers and Rogues |
| **fellowship** | includes toons in your fellowship that is in zone |
| **gm** | GMs and Guides |
| **group** | Group members |
| **guildname** _name_ | Members of _name_ guild |
| **guildname** | Members of your own guild |
| **healer** | Returns Druids and Clerics |
| **id \#** | Spawn with ID \# |
| **invis** | Invisible spawns |
| **knight** | Returns Paladins and Shadow Knights |
| **lfg** | All spawns Looking For Group |
| **light** _lightsource_ | Spawns with the specified _lightsource_ |
| **loc \#x \#y [\#z]** | Spawn at the specified loc, Z is optional, if Z is not supplied it will use your current Z. (note: you must use radius with this keyword) |
| **los** | Spawns in Line of Sight (from your point of view) |
| **mercenary** | Spawn which is a mercenary |
| **merchant** | NPC Merchants |
| **name** | Spawn with this name |
| **named** | "Named" spawns (spawns whose names start with a \#, or whose name does not start with "a" or "an") |
| **nearalert \#** | Spawns close to alert list \# |
| **next** | Next spawn matching the search criteria |
| **noalert \#** | Spawns not on the alert list \# |
| **noguild** | Spawns with no guild tag |
| **notid \#** | Spawns not matching ID \# |
| **npc** | Non-Player Characters |
| **npccorpse** | Non-Player Characters Corpses |
| **npcpet** | Pets Owned by Non-Player Characters |
| **pc** | Player Characters (default) |
| **pccorpse** | Player corpses |
| **pcpet** | Pets Owned by Player Characters |
| **pet** | Pets |
| **prev** | Previous spawn matching the search criteria |
| **race** _racename_ | Spawns with the race _racename_ |
| **radius \#** | Within the radius \# |
| **range low\# high\#** | Within the level range \#(low\) and \#\(high) |
| **slower** | Returns Shamans, Enchanters and Beastlords |
| **tank** | Returns Paladins, Shadow Knights and Warriors |
| **targetable** | Spawns that can be targeted |
| **timer** | Timer spawns |
| **trap** | Traps |
| **tribute** | Tribute Masters |
| **trigger** | Triggers |
| **untargettable** | Untargettable spawns |
| **zradius \#** | Spawns within the specified Z-Axis radius |
| _**Anything Else**_ | Anything not matched above is considered a **name** |

* Complete list of searchables as of 30 march 2020

`"pc"`  
`"npc"`  
`"mount"`  
`"pet"`  
`"pcpet"`  
`"npcpet"`  
`"xtarhater"`  
`"nopet"`  
`"corpse"`  
`"npccorpse"`  
`"pccorpse"`  
`"trigger"`  
`"untargetable"`  
`"trap"`  
`"chest"`  
`"timer"`  
`"aura"`  
`"object"`  
`"banner"`  
`"campfire"`  
`"mercenary"`  
`"flyer"`  
`"any"`  
`"next"`  
`"prev"`  
`"lfg"`  
`"gm"`  
`"group"`  
`"fellowship"`  
`"nogroup"`  
`"raid"`  
`"noguild"`  
`"trader"`  
`"named"`  
`"merchant"`  
`"banker"`  
`"tribute"`  
`"knight"`  
`"tank"`  
`"healer"`  
`"dps"`  
`"slower"`  
`"los"`  
`"targetable"`  
````"range"`` ``MinLevel`` ``MaxLevel``````` "loc"`````KnownLocation``` `xLoc` `yLoc` ``````zLoc`````    
`````"id"`````` `bSpawnID` ``````SpawnID`````    
`"radius"`    
`````"body"`````` ```````BodyType``````````` "class"```"race"``  
`[[ "light"`  
`Light, Lights[Light] ]]`  
`"guild"`  
`"guildname"`  
`"alert"`  
`"noalert"`  
`"notnearalert"`  
`"nearalert"`  
`"zradius"`  
`"notid"`  
`"nopcnear"`  
`"playerstate"`

