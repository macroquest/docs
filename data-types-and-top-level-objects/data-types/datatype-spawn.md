# DataType:spawn

## Description

This is the type used for spawns.

This type inherits no other types.

## Members

<table>
  <thead>
    <tr>
      <th style="text-align:left"><b>Type</b>
      </th>
      <th style="text-align:left"><b>Member</b>
      </th>
      <th style="text-align:left"><b>Description</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AARank</b>
      </td>
      <td style="text-align:left">AA rank number</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AFK</b>
      </td>
      <td style="text-align:left">AFK?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Aggressive</b>
      </td>
      <td style="text-align:left">returns TRUE or FALSE if a mob is aggressive or not</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Animation</b>
      </td>
      <td style="text-align:left">Current animation ID. See <a href="../../general-information/animations.md">Animations</a> for
        a list of animations.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Anonymous</b>
      </td>
      <td style="text-align:left">Anonymous</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Assist</b>
      </td>
      <td style="text-align:left">Current Raid or Group assist target?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Binding</b>
      </td>
      <td style="text-align:left">Binding wounds?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-body.md"><em>body</em></a>
      </td>
      <td style="text-align:left"><b>Body</b>
      </td>
      <td style="text-align:left">Body type</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Buyer</b>
      </td>
      <td style="text-align:left">Is a buyer? (ie. Buyer in the bazaar)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-cachedbuff.md"><em>CachedBuff</em></a>
      </td>
      <td style="text-align:left"><b>CachedBuff</b>
      </td>
      <td style="text-align:left">Caches buff information cast on others, refer to <a href="https://github.com/macroquest/docs/tree/108032b0f20c28068c91a07957f88d1e87a0bb61/data-types/[[DataType:CachedBuff/README.md">[[DataType:CachedBuff</a> for
        additional information</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>CanSplashLand</b>
      </td>
      <td style="text-align:left">TRUE/FALSE on if a splash spell can land...NOTE! This check is ONLY for
        line of sight to the targetindicator (red/green circle)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>Casting</b>
      </td>
      <td style="text-align:left">Spell, if currently casting (only accurate on yourself, not NPCs or other
        group members)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-class.md"><em>class</em></a>
      </td>
      <td style="text-align:left"><b>Class</b>
      </td>
      <td style="text-align:left">Class</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>CleanName</b>
      </td>
      <td style="text-align:left">The &quot;cleaned up&quot; name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>ConColor</b>
      </td>
      <td style="text-align:left">GREY, GREEN, LIGHT BLUE, BLUE, WHITE, YELLOW, RED</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentEndurance</b>
      </td>
      <td style="text-align:left">Current Endurance points (only updates when target/group)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentHPs</b>
      </td>
      <td style="text-align:left">Current hit points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentMana</b>
      </td>
      <td style="text-align:left">Current Mana points (only updates when target/group)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Dead</b>
      </td>
      <td style="text-align:left">Dead?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-deity.md"><em>deity</em></a>
      </td>
      <td style="text-align:left"><b>Deity</b>
      </td>
      <td style="text-align:left">Deity</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>DisplayName</b>
      </td>
      <td style="text-align:left">Name displayed in game (same as EQ&apos;s %T)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Distance</b>
      </td>
      <td style="text-align:left">Distance from player in (x,y)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Distance3D</b>
      </td>
      <td style="text-align:left">Distance from player in (x,y,z) in 3D</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistanceN</b>
      </td>
      <td style="text-align:left">Distance from player in Y plane (North/South)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistancePredict</b>
      </td>
      <td style="text-align:left">Estimated distance in (x,y), taking into account the spawn&apos;s movement
        speed but not the player&apos;s</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistanceU</b>
      </td>
      <td style="text-align:left">Distance from player in Z plane (Up/Down)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistanceW</b>
      </td>
      <td style="text-align:left">Distance from player in X plane (East/West)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistanceX</b>
      </td>
      <td style="text-align:left">Distance from player in X plane</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistanceY</b>
      </td>
      <td style="text-align:left">Distance from player in Y plane</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>DistanceZ</b>
      </td>
      <td style="text-align:left">Distance from player in Z plane</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-action.md"><em>action</em></a>
      </td>
      <td style="text-align:left"><b>DoAssist</b>
      </td>
      <td style="text-align:left">assists the spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-action.md"><em>action</em></a>
      </td>
      <td style="text-align:left"><b>DoFace</b>
      </td>
      <td style="text-align:left">Faces target</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-action.md"><em>action</em></a>
      </td>
      <td style="text-align:left"><b>DoTarget</b>
      </td>
      <td style="text-align:left">targets spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Ducking</b>
      </td>
      <td style="text-align:left">Ducking?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Equipment</b>
      </td>
      <td style="text-align:left">returns a inttype, it takes numbers 0-8 or names: head chest arms wrists
        hands legs feet primary offhand</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>EQLoc</b>
      </td>
      <td style="text-align:left">Location using EQ format</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>FeetWet</b>
      </td>
      <td style="text-align:left">Feet wet/swimming?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Feigning</b>
      </td>
      <td style="text-align:left">Feigning?</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Following</b>
      </td>
      <td style="text-align:left">The spawn a player is following using /follow on - also returns your pet&apos;s
        target via ${Me.Pet.Following}</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Fleeing</b>
      </td>
      <td style="text-align:left">Is your target moving away from you?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Gender</b>
      </td>
      <td style="text-align:left">Gender</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>GM</b>
      </td>
      <td style="text-align:left">GM or Guide?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>GroupLeader</b>
      </td>
      <td style="text-align:left">Group leader?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Guild</b>
      </td>
      <td style="text-align:left">Guild name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>GuildStatus **</b>
      </td>
      <td style="text-align:left">Guild status (Leader, Officer, Member) <b>NOTE</b> GuildStatus is no longer
        present in BETA/TEST/LIVE versions and only available in UF and ROF EMU
        builds.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-heading.md"><em>heading</em></a>
      </td>
      <td style="text-align:left"><b>Heading</b>
      </td>
      <td style="text-align:left">Heading in this direction</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-heading.md"><em>heading</em></a>
      </td>
      <td style="text-align:left"><b>HeadingTo</b>
      </td>
      <td style="text-align:left">Heading player must travel in to reach this spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-heading.md"><em>heading</em></a>
      </td>
      <td style="text-align:left"><b>HeadingToLoc[</b>y<b>,</b>x<b>]</b>
      </td>
      <td style="text-align:left">Heading to the coordinates y,x from the spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Height</b>
      </td>
      <td style="text-align:left">Height</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Holding</b>
      </td>
      <td style="text-align:left">Represents what the pc/npc is holding</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Hovering</b>
      </td>
      <td style="text-align:left">Hovering?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ID</b>
      </td>
      <td style="text-align:left">Spawn ID</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Invis[ANY|0]</b>
      </td>
      <td style="text-align:left">
        <p>Gives TRUE/FALSE returns. Options are:</p>
        <ul>
          <li>ANY or 0 - ${Me.Invis[ANY]} or ${Me.Invis[0]} or ${Me.Invis}</li>
          <li>NORMAL or 1 - ${Me.Invis[NORMAL]} or just ${Me.Invis[1]}</li>
          <li>UNDEAD or 2 - ${Me.Invis[UNDEAD]} or just ${Me.Invis[2]}</li>
          <li>ANIMAL or 3 - ${Me.Invis[ANIMAL]} or just ${Me.Invis[3]}</li>
          <li>SOS or 4 - ${Me.Invis[SOS]} or just ${Me.Invis[4]} returns true IF you
            are a ROG AND in fact hidden AND have a skill of at least 100 in HIDE AND
            have the AA for SoS</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Invited</b>
      </td>
      <td style="text-align:left">Invited to group?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Level</b>
      </td>
      <td style="text-align:left">Level</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-action.md"><em>action</em></a>
      </td>
      <td style="text-align:left"><b>DoLeftClick</b>
      </td>
      <td style="text-align:left">left clicks the spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Levitating</b>
      </td>
      <td style="text-align:left">Levitating?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>LFG</b>
      </td>
      <td style="text-align:left">LFG?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Light</b>
      </td>
      <td style="text-align:left">Name of the light class this spawn has</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>LineOfSight</b>
      </td>
      <td style="text-align:left">Returns TRUE if spawn is in LoS</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Linkdead</b>
      </td>
      <td style="text-align:left">Linkdead?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Loc</b>
      </td>
      <td style="text-align:left">Loc of the spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>LocYX</b>
      </td>
      <td style="text-align:left">LocYX of the spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Look</b>
      </td>
      <td style="text-align:left">Looking this angle</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Mark</b>
      </td>
      <td style="text-align:left">Current Raid or Group marked npc mark number (raid first)</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Master</b>
      </td>
      <td style="text-align:left">Master, if it is charmed or a pet</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxEndurance</b>
      </td>
      <td style="text-align:left">Maximum Endurance points (only updates when target/group)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxHPs</b>
      </td>
      <td style="text-align:left">Maximum hit points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxMana</b>
      </td>
      <td style="text-align:left">Maximum Mana points (only updates when target/group)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>MaxRange</b>
      </td>
      <td style="text-align:left">The max distance from this spawn for it to hit you</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>MaxRangeTo</b>
      </td>
      <td style="text-align:left">The Max distance from this spawn for you to hit it</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Mount</b>
      </td>
      <td style="text-align:left">Mount</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Moving</b>
      </td>
      <td style="text-align:left">Moving?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>MQLoc</b>
      </td>
      <td style="text-align:left">Location using MQ format</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Name</b>
      </td>
      <td style="text-align:left">Name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Named</b>
      </td>
      <td style="text-align:left">Is this a &quot;named&quot; spawn (ie. does it&apos;s name not start with
        an &quot;a&quot; or an &quot;an&quot;)</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>NearestSpawn[</b>search<b>]</b>
      </td>
      <td style="text-align:left">Find the nearest spawn matching this <a href="../../general-information/spawn-search.md">Spawn Search</a>,
        to this spawn (most efficient on yourself)</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>NearestSpawn[</b>#<b>,</b>search<b>]</b>
      </td>
      <td style="text-align:left">Find the #th nearest spawn matching this <a href="../../general-information/spawn-search.md">Spawn Search</a>,
        to this spawn (most efficient on yourself)</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Next</b>
      </td>
      <td style="text-align:left">Next spawn in the list</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Owner</b>
      </td>
      <td style="text-align:left">Owner, if mercenary</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Prev</b>
      </td>
      <td style="text-align:left">Previous spawn in the list</td>
    </tr>
    <tr>
      <td style="text-align:left"><em>spawn</em>
      </td>
      <td style="text-align:left"><b>Pet</b>
      </td>
      <td style="text-align:left">Pet</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctHPs</b>
      </td>
      <td style="text-align:left">Percent hit points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PlayerState</b>
      </td>
      <td style="text-align:left">returns a mask as an inttype which has the following meaning: 0=Idle 1=Open
        2=WeaponSheathed 4=Aggressive 8=ForcedAggressive 0x10=InstrumentEquipped
        0x20=Stunned 0x40=PrimaryWeaponEquipped 0x80=SecondaryWeaponEquipped</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Primary</b>
      </td>
      <td style="text-align:left">Item ID of anything that may be in the Primary slot</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-race.md"><em>race</em></a>
      </td>
      <td style="text-align:left"><b>Race</b>
      </td>
      <td style="text-align:left">Race</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-action.md"><em>action</em></a>
      </td>
      <td style="text-align:left"><b>DoRightClick</b>
      </td>
      <td style="text-align:left">Right clicks the spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Roleplaying</b>
      </td>
      <td style="text-align:left">Roleplaying?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Secondary</b>
      </td>
      <td style="text-align:left">Item ID of anything that may be in the Secondary slot</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Sitting</b>
      </td>
      <td style="text-align:left">Sitting?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Sneaking</b>
      </td>
      <td style="text-align:left">Sneaking?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Speed</b>
      </td>
      <td style="text-align:left">Speed moving</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Standing</b>
      </td>
      <td style="text-align:left">Standing?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>StandState</b>
      </td>
      <td style="text-align:left">StandState</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>State</b>
      </td>
      <td style="text-align:left">STAND, SIT, DUCK, BIND, FEIGN, DEAD, STUN, HOVER, MOUNT, UNKNOWN</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Stunned</b>
      </td>
      <td style="text-align:left">Stunned?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Stuck</b>
      </td>
      <td style="text-align:left">Stuck?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Suffix</b>
      </td>
      <td style="text-align:left">Suffix attached to name, eg. of</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Surname</b>
      </td>
      <td style="text-align:left">Last name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Title</b>
      </td>
      <td style="text-align:left">Prefix/Title before name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Trader</b>
      </td>
      <td style="text-align:left">Trader?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Type</b>
      </td>
      <td style="text-align:left">PC, NPC, Untargetable, Mount, Pet, Corpse, Chest, Trigger, Trap, Timer,
        Item, Mercenary, Aura, Object, Banner, Campfire, Flyer</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Underwater</b>
      </td>
      <td style="text-align:left">Underwater?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>X</b>
      </td>
      <td style="text-align:left">X coordinate</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Y</b>
      </td>
      <td style="text-align:left">Y coordinate</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Z</b>
      </td>
      <td style="text-align:left">Z coordinate</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>N</b>
      </td>
      <td style="text-align:left">X, the Northward-positive coordinate</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>W</b>
      </td>
      <td style="text-align:left">Y, the Westward-positive coordinate</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>U</b>
      </td>
      <td style="text-align:left">Z, the Upward-positive coordinate</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>E</b>
      </td>
      <td style="text-align:left">Shortcut for -X (makes Eastward positive)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>S</b>
      </td>
      <td style="text-align:left">Shortcut for -Y (makes Southward positive)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>D</b>
      </td>
      <td style="text-align:left">Shortcut for -Z (makes Downward positive)</td>
    </tr>
    <tr>
      <td style="text-align:left">&apos;<b>&apos;</b><a href="datatype-string.md"><b>string</b></a>
      </td>
      <td style="text-align:left"><b>To String</b>
      </td>
      <td style="text-align:left">Same as <b>Name</b>
      </td>
    </tr>
  </tbody>
</table>

### All members as of 9/22/20

* AARank
* AATitle
* ActorDef
* Address
* AFK
* Aggressive
* Animation
* Anonymous
* Assist
* AssistName
* bAlwaysShowAura
* bBetaBuffed
* BearingToTarget
* Binding
* Blind
* Body
* bShowHelm
* bStationary
* bTempPet
* Buyer
* bWaitingForPort
* CachedBuff
* CachedBuffCount
* CanSplashLand
* Casting
* CeilingHeightAtCurrLocation
* Class
* CleanName
* CollisionCounter
* CombatSkillTicks
* ConColor
* ContractorID
* CorpseDragCount
* CurrentEndurance
* CurrentHPs
* CurrentMana
* D
* Dead
* Deity
* DisplayName
* Distance
* Distance3D
* DistanceN
* DistancePredict
* DistanceU
* DistanceW
* DistanceX
* DistanceY
* DistanceZ
* DraggingPlayer
* DragNames
* Ducking
* E
* EQLoc
* Equipment
* FD
* FeetWet
* Feigning
* Fleeing
* FloorZ
* Following
* Gender
* GM
* GMRank
* GroupLeader
* Guild
* GuildStatus
* Heading
* HeadingTo
* HeadingToLoc
* Height
* Holding
* HoldingAnimation
* Hovering
* ID
* InPvPArea
* Invis
* Invited
* Inviter
* IsBerserk
* IsPassenger
* IsSummoned
* LastCastNum
* LastCastTime
* Levitating
* LFG
* Light
* LineOfSight
* Linkdead
* Loc
* LocYX
* LocYXZ
* Look
* Mark
* Master
* MaxEndurance
* MaxHPs
* MaxMana
* MaxRange
* MaxRangeTo
* MercID
* Mount
* Moving
* MQLoc
* N
* Named
* NearestSpawn
* Next
* Owner
* PctEndurance
* PctHPs
* PctMana
* Pet
* PlayerState
* Prev
* Primary
* pTouchingSwitch
* Race
* Roleplaying
* S
* Secondary
* SeeInvis
* Sitting
* Sneaking
* SpawnStatus
* Speed
* Standing
* StandState
* State
* Stuck
* Stunned
* Suffix
* Surname
* Targetable
* TargetOfTarget
* TimeBeenDead
* Title
* Trader
* Type
* U
* Underwater
* W
* WarCry
* X
* Y
* Z

### Usage

|  |  |
| :--- | :--- |
| **Example** | **Output** |
| '''${Pet.Equipment\[primary\].ID} | ID number of the pet's primary weapon |
| '''${Group.Member\[mymagesname\].Pet.Equipment\[primary\].ID} | ID number of the group member's pet's primary weapon |
|  |  |

## See Also

* [Animations](../../general-information/animations.md)
* [Data Types](./)
* [DataType:character](datatype-character.md)
* [Spawn Search](../../general-information/spawn-search.md)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Me](../top-level-objects/tlo-me.md)

