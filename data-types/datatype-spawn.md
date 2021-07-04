## Description

This is the type used for spawns.

This type inherits no other types.

## Members

<table>
<tbody>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p><strong>Member</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>AARank</strong></p></td>
<td><p>AA rank number</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>AFK</strong></p></td>
<td><p>AFK?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Aggressive</strong></p></td>
<td><p>returns TRUE or FALSE if a mob is aggressive or not</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Animation</strong></p></td>
<td><p>Current animation ID. See <a href="../general-information/animations.md">Animations</a> for a list of animations.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Anonymous</strong></p></td>
<td><p>Anonymous</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Assist</strong></p></td>
<td><p>Current Raid or Group assist target?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Binding</strong></p></td>
<td><p>Binding wounds?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-body.md">body</a></em></p></td>
<td><p><strong>Body</strong></p></td>
<td><p>Body type</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Buyer</strong></p></td>
<td><p>Is a buyer? (ie. Buyer in the bazaar)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-cachedbuff.md">CachedBuff</a></em></p></td>
<td><p><strong>CachedBuff</strong></p></td>
<td><p>Caches buff information cast on others, refer to <a href="[[DataType:CachedBuff">[[DataType:CachedBuff</a> for additional information</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>CanSplashLand</strong></p></td>
<td><p>TRUE/FALSE on if a splash spell can land...NOTE! This check is ONLY for line of sight to the targetindicator (red/green circle)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-spell.md">spell</a></em></p></td>
<td><p><strong>Casting</strong></p></td>
<td><p>Spell, if currently casting (only accurate on yourself, not NPCs or other group members)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-class.md">class</a></em></p></td>
<td><p><strong>Class</strong></p></td>
<td><p>Class</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>CleanName</strong></p></td>
<td><p>The "cleaned up" name</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>ConColor</strong></p></td>
<td><p>GREY, GREEN, LIGHT BLUE, BLUE, WHITE, YELLOW, RED</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CurrentEndurance</strong></p></td>
<td><p>Current Endurance points (only updates when target/group)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CurrentHPs</strong></p></td>
<td><p>Current hit points</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CurrentMana</strong></p></td>
<td><p>Current Mana points (only updates when target/group)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Dead</strong></p></td>
<td><p>Dead?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-deity.md">deity</a></em></p></td>
<td><p><strong>Deity</strong></p></td>
<td><p>Deity</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>DisplayName</strong></p></td>
<td><p>Name displayed in game (same as EQ's %T)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Distance</strong></p></td>
<td><p>Distance from player in (x,y)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Distance3D</strong></p></td>
<td><p>Distance from player in (x,y,z) in 3D</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistanceN</strong></p></td>
<td><p>Distance from player in Y plane (North/South)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistancePredict</strong></p></td>
<td><p>Estimated distance in (x,y), taking into account the spawn's movement speed but not the player's</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistanceU</strong></p></td>
<td><p>Distance from player in Z plane (Up/Down)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistanceW</strong></p></td>
<td><p>Distance from player in X plane (East/West)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistanceX</strong></p></td>
<td><p>Distance from player in X plane</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistanceY</strong></p></td>
<td><p>Distance from player in Y plane</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>DistanceZ</strong></p></td>
<td><p>Distance from player in Z plane</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>DoAssist</strong></p></td>
<td><p>assists the spawn</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>DoFace</strong></p></td>
<td><p>Faces target</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>DoTarget</strong></p></td>
<td><p>targets spawn</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Ducking</strong></p></td>
<td><p>Ducking?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Equipment</strong></p></td>
<td><p>returns a inttype, it takes numbers 0-8 or names: head chest arms wrists hands legs feet primary offhand</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>EQLoc</strong></p></td>
<td><p>Location using EQ format</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>FeetWet</strong></p></td>
<td><p>Feet wet/swimming?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Feigning</strong></p></td>
<td><p>Feigning?</p></td>
</tr>
<tr class="even">
<td><p><em>spawn</em></p></td>
<td><p><strong>Following</strong></p></td>
<td><p>The spawn a player is following using /follow on - also returns your pet's target via ${Me.Pet.Following}</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Fleeing</strong></p></td>
<td><p>Is your target moving away from you?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Gender</strong></p></td>
<td><p>Gender</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>GM</strong></p></td>
<td><p>GM or Guide?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>GroupLeader</strong></p></td>
<td><p>Group leader?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Guild</strong></p></td>
<td><p>Guild name</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>GuildStatus **</strong></p></td>
<td><p>Guild status (Leader, Officer, Member) <strong>NOTE</strong> GuildStatus is no longer present in BETA/TEST/LIVE versions and only available in UF and ROF EMU builds.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-heading.md">heading</a></em></p></td>
<td><p><strong>Heading</strong></p></td>
<td><p>Heading in this direction</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-heading.md">heading</a></em></p></td>
<td><p><strong>HeadingTo</strong></p></td>
<td><p>Heading player must travel in to reach this spawn</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-heading.md">heading</a></em></p></td>
<td><p><strong>HeadingToLoc[</strong>y<strong>,</strong>x<strong>]</strong></p></td>
<td><p>Heading to the coordinates y,x from the spawn</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Height</strong></p></td>
<td><p>Height</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Holding</strong></p></td>
<td><p>Represents what the pc/npc is holding</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Hovering</strong></p></td>
<td><p>Hovering?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>ID</strong></p></td>
<td><p>Spawn ID</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Invis[ANY|0]</strong></p></td>
<td><p>Gives TRUE/FALSE returns. Options are:</p>
<ul>
<li>ANY or 0 - ${Me.Invis[ANY]} or ${Me.Invis[0]} or ${Me.Invis}</li>
<li>NORMAL or 1 - ${Me.Invis[NORMAL]} or just ${Me.Invis[1]}</li>
<li>UNDEAD or 2 - ${Me.Invis[UNDEAD]} or just ${Me.Invis[2]}</li>
<li>ANIMAL or 3 - ${Me.Invis[ANIMAL]} or just ${Me.Invis[3]}</li>
<li>SOS or 4 - ${Me.Invis[SOS]} or just ${Me.Invis[4]} returns true IF you are a ROG AND in fact hidden AND have a skill of at least 100 in HIDE AND have the AA for SoS</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Invited</strong></p></td>
<td><p>Invited to group?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Level</strong></p></td>
<td><p>Level</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>DoLeftClick</strong></p></td>
<td><p>left clicks the spawn</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Levitating</strong></p></td>
<td><p>Levitating?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>LFG</strong></p></td>
<td><p>LFG?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Light</strong></p></td>
<td><p>Name of the light class this spawn has</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>LineOfSight</strong></p></td>
<td><p>Returns TRUE if spawn is in LoS</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Linkdead</strong></p></td>
<td><p>Linkdead?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Loc</strong></p></td>
<td><p>Loc of the spawn</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>LocYX</strong></p></td>
<td><p>LocYX of the spawn</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Look</strong></p></td>
<td><p>Looking this angle</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Mark</strong></p></td>
<td><p>Current Raid or Group marked npc mark number (raid first)</p></td>
</tr>
<tr class="odd">
<td><p><em>spawn</em></p></td>
<td><p><strong>Master</strong></p></td>
<td><p>Master, if it is charmed or a pet</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>MaxEndurance</strong></p></td>
<td><p>Maximum Endurance points (only updates when target/group)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>MaxHPs</strong></p></td>
<td><p>Maximum hit points</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>MaxMana</strong></p></td>
<td><p>Maximum Mana points (only updates when target/group)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>MaxRange</strong></p></td>
<td><p>The max distance from this spawn for it to hit you</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>MaxRangeTo</strong></p></td>
<td><p>The Max distance from this spawn for you to hit it</p></td>
</tr>
<tr class="odd">
<td><p><em>spawn</em></p></td>
<td><p><strong>Mount</strong></p></td>
<td><p>Mount</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Moving</strong></p></td>
<td><p>Moving?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>MQLoc</strong></p></td>
<td><p>Location using MQ format</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Name</strong></p></td>
<td><p>Name</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Named</strong></p></td>
<td><p>Is this a "named" spawn (ie. does it's name not start with an "a" or an "an")</p></td>
</tr>
<tr class="even">
<td><p><em>spawn</em></p></td>
<td><p><strong>NearestSpawn[</strong>search<strong>]</strong></p></td>
<td><p>Find the nearest spawn matching this <a href="../general-information/spawn-search.md">Spawn Search</a>, to this spawn (most efficient on yourself)</p></td>
</tr>
<tr class="odd">
<td><p><em>spawn</em></p></td>
<td><p><strong>NearestSpawn[</strong>#<strong>,</strong>search<strong>]</strong></p></td>
<td><p>Find the #th nearest spawn matching this <a href="../general-information/spawn-search.md">Spawn Search</a>, to this spawn (most efficient on yourself)</p></td>
</tr>
<tr class="even">
<td><p><em>spawn</em></p></td>
<td><p><strong>Next</strong></p></td>
<td><p>Next spawn in the list</p></td>
</tr>
<tr class="odd">
<td><p><em>spawn</em></p></td>
<td><p><strong>Owner</strong></p></td>
<td><p>Owner, if mercenary</p></td>
</tr>
<tr class="even">
<td><p><em>spawn</em></p></td>
<td><p><strong>Prev</strong></p></td>
<td><p>Previous spawn in the list</p></td>
</tr>
<tr class="odd">
<td><p><em>spawn</em></p></td>
<td><p><strong>Pet</strong></p></td>
<td><p>Pet</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>PctHPs</strong></p></td>
<td><p>Percent hit points</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>PlayerState</strong></p></td>
<td><p>returns a mask as an inttype which has the following meaning: 0=Idle 1=Open 2=WeaponSheathed 4=Aggressive 8=ForcedAggressive 0x10=InstrumentEquipped 0x20=Stunned 0x40=PrimaryWeaponEquipped 0x80=SecondaryWeaponEquipped</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Primary</strong></p></td>
<td><p>Item ID of anything that may be in the Primary slot</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-race.md">race</a></em></p></td>
<td><p><strong>Race</strong></p></td>
<td><p>Race</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>DoRightClick</strong></p></td>
<td><p>Right clicks the spawn</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Roleplaying</strong></p></td>
<td><p>Roleplaying?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Secondary</strong></p></td>
<td><p>Item ID of anything that may be in the Secondary slot</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Sitting</strong></p></td>
<td><p>Sitting?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Sneaking</strong></p></td>
<td><p>Sneaking?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Speed</strong></p></td>
<td><p>Speed moving</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Standing</strong></p></td>
<td><p>Standing?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>StandState</strong></p></td>
<td><p>StandState</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>State</strong></p></td>
<td><p>STAND, SIT, DUCK, BIND, FEIGN, DEAD, STUN, HOVER, MOUNT, UNKNOWN</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Stunned</strong></p></td>
<td><p>Stunned?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Stuck</strong></p></td>
<td><p>Stuck?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Suffix</strong></p></td>
<td><p>Suffix attached to name, eg. of <servername></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Surname</strong></p></td>
<td><p>Last name</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Title</strong></p></td>
<td><p>Prefix/Title before name</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Trader</strong></p></td>
<td><p>Trader?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Type</strong></p></td>
<td><p>PC, NPC, Untargetable, Mount, Pet, Corpse, Chest, Trigger, Trap, Timer, Item, Mercenary, Aura, Object, Banner, Campfire, Flyer</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Underwater</strong></p></td>
<td><p>Underwater?</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>X</strong></p></td>
<td><p>X coordinate</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Y</strong></p></td>
<td><p>Y coordinate</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Z</strong></p></td>
<td><p>Z coordinate</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>N</strong></p></td>
<td><p>X, the Northward-positive coordinate</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>W</strong></p></td>
<td><p>Y, the Westward-positive coordinate</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>U</strong></p></td>
<td><p>Z, the Upward-positive coordinate</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>E</strong></p></td>
<td><p>Shortcut for -X (makes Eastward positive)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>S</strong></p></td>
<td><p>Shortcut for -Y (makes Southward positive)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>D</strong></p></td>
<td><p>Shortcut for -Z (makes Downward positive)</p></td>
</tr>
<tr class="even">
<td><p>'<strong>'<a href="datatype-string.md">string</a></strong></p></td>
<td><p><strong>To String</strong></p></td>
<td><p>Same as <strong>Name</strong></p></td>
</tr>
</tbody>
</table>

### All members as of 9/22/20

-   AARank
-   AATitle
-   ActorDef
-   Address
-   AFK
-   Aggressive
-   Animation
-   Anonymous
-   Assist
-   AssistName
-   bAlwaysShowAura
-   bBetaBuffed
-   BearingToTarget
-   Binding
-   Blind
-   Body
-   bShowHelm
-   bStationary
-   bTempPet
-   Buyer
-   bWaitingForPort
-   CachedBuff
-   CachedBuffCount
-   CanSplashLand
-   Casting
-   CeilingHeightAtCurrLocation
-   Class
-   CleanName
-   CollisionCounter
-   CombatSkillTicks
-   ConColor
-   ContractorID
-   CorpseDragCount
-   CurrentEndurance
-   CurrentHPs
-   CurrentMana
-   D
-   Dead
-   Deity
-   DisplayName
-   Distance
-   Distance3D
-   DistanceN
-   DistancePredict
-   DistanceU
-   DistanceW
-   DistanceX
-   DistanceY
-   DistanceZ
-   DraggingPlayer
-   DragNames
-   Ducking
-   E
-   EQLoc
-   Equipment
-   FD
-   FeetWet
-   Feigning
-   Fleeing
-   FloorZ
-   Following
-   Gender
-   GM
-   GMRank
-   GroupLeader
-   Guild
-   GuildStatus
-   Heading
-   HeadingTo
-   HeadingToLoc
-   Height
-   Holding
-   HoldingAnimation
-   Hovering
-   ID
-   InPvPArea
-   Invis
-   Invited
-   Inviter
-   IsBerserk
-   IsPassenger
-   IsSummoned
-   LastCastNum
-   LastCastTime
-   Levitating
-   LFG
-   Light
-   LineOfSight
-   Linkdead
-   Loc
-   LocYX
-   LocYXZ
-   Look
-   Mark
-   Master
-   MaxEndurance
-   MaxHPs
-   MaxMana
-   MaxRange
-   MaxRangeTo
-   MercID
-   Mount
-   Moving
-   MQLoc
-   N
-   Named
-   NearestSpawn
-   Next
-   Owner
-   PctEndurance
-   PctHPs
-   PctMana
-   Pet
-   PlayerState
-   Prev
-   Primary
-   pTouchingSwitch
-   Race
-   Roleplaying
-   S
-   Secondary
-   SeeInvis
-   Sitting
-   Sneaking
-   SpawnStatus
-   Speed
-   Standing
-   StandState
-   State
-   Stuck
-   Stunned
-   Suffix
-   Surname
-   Targetable
-   TargetOfTarget
-   TimeBeenDead
-   Title
-   Trader
-   Type
-   U
-   Underwater
-   W
-   WarCry
-   X
-   Y
-   Z

### Usage

|                                                               |                                                      |
|---------------------------------------------------------------|------------------------------------------------------|
| **Example**                                                   | **Output**                                           |
| '''${Pet.Equipment\[primary\].ID}                             | ID number of the pet's primary weapon                |
| '''${Group.Member\[mymagesname\].Pet.Equipment\[primary\].ID} | ID number of the group member's pet's primary weapon |
|                                                               |                                                      |

## See Also

-   [Animations](../general-information/animations.md)
-   [Data Types](data-types.md)
-   [DataType:character](datatype-character.md)
-   [Spawn Search](../general-information/spawn-search.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Me](../top-level-objects/tlo-me.md)


