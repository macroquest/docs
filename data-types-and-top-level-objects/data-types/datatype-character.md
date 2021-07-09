# DataType:character

This data type contains all the information about _your_ character.

Inherits [_spawn_](datatype-spawn.md).

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
      <td style="text-align:left"><b>AAExp</b>
      </td>
      <td style="text-align:left">AA exp as a raw number out of 10,000 (10,000=100%)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AAPoints</b>
      </td>
      <td style="text-align:left">Unused AA points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AAPointsSpent</b>
      </td>
      <td style="text-align:left">The number of points you have spent on AA abilities</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AAPointsTotal</b>
      </td>
      <td style="text-align:left">The total number of AA points you have</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AAVitality</b>
      </td>
      <td style="text-align:left">The total number of AA Vitality you have</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Ability[</b>name<b>]</b>
        </td>
        <td style="text-align:left">Skill name assigned to this doability button</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Ability[</b>#<b>]</b>
      </td>
      <td style="text-align:left">The doability button number that the skill <em>name</em> is on</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AbilityReady[</b>#|name<b>]</b>
      </td>
      <td style="text-align:left">Ability with this <em>name</em> or on this button <em>#</em> ready?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AccuracyBonus</b>
      </td>
      <td style="text-align:left">Accuracy bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>ActiveDisc</b>
      </td>
      <td style="text-align:left">Returns a spell if melee discipline is active.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ActiveFavorCost</b>
      </td>
      <td style="text-align:left">If Tribute is active, how much it is costing you every 10 minutes. Returns
        NULL if tribute is inactive.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-altability.md"><em>altability</em></a>
      </td>
      <td style="text-align:left"><b>AltAbility[</b>#|name<b>]</b>
      </td>
      <td style="text-align:left">Returns the total number of points you have spent in ability # or <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AltAbilityReady[</b>#|name<b>]</b>
      </td>
      <td style="text-align:left">Alt ability <em>#</em> or <em>name</em> ready?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AltAbilityTimer[</b>#|name<b>]</b>
      </td>
      <td style="text-align:left">Alt ability reuse time remaining (in ticks) for ability <em>#</em> or <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AltTimerReady</b>
      </td>
      <td style="text-align:left">Alternate timer ready? (Bash/Slam/Frenzy/Backstab). <b>Note: ${AbilityReady} works fine with most of these.</b>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AGI</b>
      </td>
      <td style="text-align:left">Character Agility</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>AggroLock</b>
      </td>
      <td style="text-align:left">spawn info for aggro lock player</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AmIGroupLeader</b>
      </td>
      <td style="text-align:left">Am I the group leader?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AssistComplete</b>
      </td>
      <td style="text-align:left">returns true/false if the assist is complete</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AttackBonus</b>
      </td>
      <td style="text-align:left">Attack bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AttackSpeed</b>
      </td>
      <td style="text-align:left">Your Attack Speed. No haste spells/items = AttackSpeed of 100. A 41% haste
        item will result in an AttackSpeed of 141. This variable does not take
        into account spell or song haste.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Aura</b>
        </td>
        <td style="text-align:left">The aura effect name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>AutoFire</b>
      </td>
      <td style="text-align:left">Is Autofire on?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>AvoidanceBonus</b>
      </td>
      <td style="text-align:left">Avoidance bonus from gear/spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-item.md"><em>item</em></a>
      </td>
      <td style="text-align:left"><b>Bank[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Item in this bankslot #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>BardSongPlaying</b>
      </td>
      <td style="text-align:left">Is a bard song playing?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Book[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Slot in your spellbook assigned to spell <em>name</em>.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>Book[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Spell assigned to this slot # in your spellbook</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-buff.md"><em>buff</em></a>
      </td>
      <td style="text-align:left"><b>Buff[</b>name<b>]</b>
      </td>
      <td style="text-align:left">The buff with this name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-buff.md"><em>buff</em></a>
      </td>
      <td style="text-align:left"><b>Buff[</b>#<b>]</b>
      </td>
      <td style="text-align:left">The buff in this slot #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left">&apos;&apos;&apos;Buyer</td>
      <td style="text-align:left">if you are an active buyer</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left">&apos;&apos;&apos;CanMount</td>
      <td style="text-align:left">for some indoor zones that where not flagged as nomount and added bazaar,
        nexus to zones where its ok to mount.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CareerFavor</b>
      </td>
      <td style="text-align:left">Career favor/tribute</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Cash</b>
      </td>
      <td style="text-align:left">Total cash on your character, expressed in coppers (eg. if you are carrying
        100pp, <b>Cash</b> will return 100000)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CashBank</b>
      </td>
      <td style="text-align:left">Total cash in your bank, expressed in coppers</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CHA</b>
      </td>
      <td style="text-align:left">Character Charisma</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Chronobines</b>
      </td>
      <td style="text-align:left">Chronobines on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ClairvoyanceBonus</b>
      </td>
      <td style="text-align:left">Clairvoyance Bonus</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Combat</b>
      </td>
      <td style="text-align:left">In combat?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>CombatAbility[</b>#<b>]</b>
      </td>
      <td style="text-align:left">The name of Combat Ability # in your list (not the same as anyone else&apos;s
        list!)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CombatAbility[</b>name<b>]</b>
      </td>
      <td style="text-align:left">The number of Combat ability <em>name</em> in your list (not the same as
        anyone else&apos;s list!)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>CombatAbilityReady[</b>name|#]&apos;&apos;&apos;</td>
      <td style="text-align:left">Is this Combat Ability ready?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CombatAbilityTimer[</b>name|#<b>]</b>
      </td>
      <td style="text-align:left">The time remaining (in seconds) before the Combat Ability <em>name</em> is
        usable</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CombatEffectsBonus</b>
      </td>
      <td style="text-align:left">Combat Effects bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>CombatState</b>
        </td>
        <td style="text-align:left">Returns one of the following: COMBAT, DEBUFFED, COOLDOWN, ACTIVE, RESTING,
          UNKNOWN</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Copper</b>
      </td>
      <td style="text-align:left">Copper on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CopperBank</b>
      </td>
      <td style="text-align:left">Copper in bank</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>Corrupted</b>
      </td>
      <td style="text-align:left">Returns the name of the Corrupted debuff if you have one</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CountBuffs</b>
      </td>
      <td style="text-align:left">Number of buffs you have, not including short duration buffs</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CountersCurse</b>
      </td>
      <td style="text-align:left">Number of curse counters you have</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CountersDisease</b>
      </td>
      <td style="text-align:left">Number of disease counters you have</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CountersPoison</b>
      </td>
      <td style="text-align:left">Number of poison counters you have</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CountSongs</b>
      </td>
      <td style="text-align:left">Number of songs you have</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Counters</b>
      </td>
      <td style="text-align:left">Damage Absorption Counters Remaining</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentEndurance</b>
      </td>
      <td style="text-align:left">Current endurance</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentFavor</b>
      </td>
      <td style="text-align:left">Current favor/tribute</td>
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
      <td style="text-align:left">Current mana</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentWeight</b>
      </td>
      <td style="text-align:left">Current weight</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>Cursed</b>
      </td>
      <td style="text-align:left">Returns the name of the Curse debuff if you are effected by one</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>DamageShieldBonus</b>
      </td>
      <td style="text-align:left">Damage Shield bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>DamageShieldMitigationBonus</b>
      </td>
      <td style="text-align:left">Damage Shield Mitigation bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Dar</b>
      </td>
      <td style="text-align:left">Damage absorption remaining (eg. from Rune-type spells)</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Diseased</b>
        </td>
        <td style="text-align:left">Returns the name of any Disease spell</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>DEX</b>
      </td>
      <td style="text-align:left">Character Dexterity</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Dotted</b>
        </td>
        <td style="text-align:left">Returns name of first DoT on character.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>DoTShieldBonus</b>
      </td>
      <td style="text-align:left">DoT Shield bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Doubloons</b>
      </td>
      <td style="text-align:left">Doubloons on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-ticks.md"><em>ticks</em></a>
      </td>
      <td style="text-align:left"><b>Downtime</b>
      </td>
      <td style="text-align:left">Downtime (Ticks left til combat timer end)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Drunk</b>
      </td>
      <td style="text-align:left">Drunkenness level</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>EbonCrystals</b>
      </td>
      <td style="text-align:left">Number of Ebon Crystals on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>EnduranceBonus</b>
      </td>
      <td style="text-align:left">Endurance bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>EnduranceRegen</b>
      </td>
      <td style="text-align:left">Endurance regen from the last tick</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>EnduranceRegenBonus</b>
      </td>
      <td style="text-align:left">Endurance regen bonus</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Exp</b>
      </td>
      <td style="text-align:left">Experience (out of 10,000)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ExpansionFlags</b>
      </td>
      <td style="text-align:left">Returns a numeric number representing which expansions your toon is flagged
        for</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Faycites</b>
      </td>
      <td style="text-align:left">Faycites on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-fellowship.md"><em>fellowship</em></a>
      </td>
      <td style="text-align:left"><b>Fellowship</b>
      </td>
      <td style="text-align:left">Info about Fellowship</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>FreeBuffSlots</b>
      </td>
      <td style="text-align:left">Number of open buff slots (not counting the short duration buff slots)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>FreeInventory</b>
      </td>
      <td style="text-align:left">Number of free inventory spaces</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>FreeInventory[#]</b>
      </td>
      <td style="text-align:left">Number of free inventory spaces of at least # size (giant=4)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Gem[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Returns the slot # with the spell <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>Gem[</b>#<b>]</b>
      </td>
      <td style="text-align:left">The name of the spell in this slot #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-ticks.md"><em>ticks</em></a>
      </td>
      <td style="text-align:left"><b>GemTimer[</b>name|#<b>]</b>
      </td>
      <td style="text-align:left">The timer for the spell with this <em>name</em> or in this gem <em>#</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Gold</b>
      </td>
      <td style="text-align:left">Gold on character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GoldBank</b>
      </td>
      <td style="text-align:left">Gold in bank</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>GroupAssistTarget</b>
      </td>
      <td style="text-align:left">Current group assist target</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Grouped</b>
      </td>
      <td style="text-align:left">Grouped?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GroupLeaderExp</b>
      </td>
      <td style="text-align:left">Group leadership experience (out of 330)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GroupLeaderPoints</b>
      </td>
      <td style="text-align:left">Group leadership points</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>GroupList</b>
        </td>
        <td style="text-align:left">Returns a string of your group members (excluding you)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>GroupMarkNPC[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Current group marked NPC (1-3)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GroupSize</b>
      </td>
      <td style="text-align:left">Size of group</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GukEarned</b>
      </td>
      <td style="text-align:left">Total LDoN points earned in Deepest Guk</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>GuildID</b>
      </td>
      <td style="text-align:left">Returns the ID number of your guild</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>HaveExpansion[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Returns TRUE/FALSE if you have that expansion #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Haste</b>
      </td>
      <td style="text-align:left">Total Combined Haste (worn and spell) as shown in Inventory Window stats</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HealAmountBonus</b>
      </td>
      <td style="text-align:left">Total Heal Amount bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicAGIBonus</b>
      </td>
      <td style="text-align:left">Total Heroic Agility bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicCHABonus</b>
      </td>
      <td style="text-align:left">Total Heroic Charisma bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicDEXBonus</b>
      </td>
      <td style="text-align:left">Total Heroic Dexterity bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicINTBonus</b>
      </td>
      <td style="text-align:left">Total Heroic Intelligence bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicSTABonus</b>
      </td>
      <td style="text-align:left">Total Heroic Stamina bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicSTRBonus</b>
      </td>
      <td style="text-align:left">Total Heroic Strength bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HeroicWISBonus</b>
      </td>
      <td style="text-align:left">Total Heroic Wisdom bonus from gear</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HPBonus</b>
      </td>
      <td style="text-align:left">Hit point bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HPRegen</b>
      </td>
      <td style="text-align:left">Hit point regeneration from last tick</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>HPRegenBonus</b>
      </td>
      <td style="text-align:left">HP regen bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Hunger</b>
      </td>
      <td style="text-align:left">Hunger level</td>
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
      <td style="text-align:left"><b>InInstance</b>
      </td>
      <td style="text-align:left">Returns TRUE/FALSE if you are in an instance.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>INT</b>
      </td>
      <td style="text-align:left">Character Intelligence</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-item.md"><em>item</em></a>
      </td>
      <td style="text-align:left"><b>Inventory[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Item in this slot #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-item.md"><em>item</em></a>
      </td>
      <td style="text-align:left"><b>Inventory[</b>slotname<b>]</b>
      </td>
      <td style="text-align:left">Item in this <em>slotname</em> (inventory slots only). See <a href="../../general-information/slot-names.md">Slot Names</a> for
        a list of <em>slotnames</em>.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Invulnerable</b>
        </td>
        <td style="text-align:left">Returns the invulnerable spell name on you, can be used with spell data
          type ex. ${Me.Invulnerable.Spell.ID}</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>ItemReady[XXX]</b>
      </td>
      <td style="text-align:left">True/False on if the item is ready to cast.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LADelegateMA</b>
      </td>
      <td style="text-align:left">Level of Delegate MA of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LADelegateMarkNPC</b>
      </td>
      <td style="text-align:left">Level of Delegate Mark NPC of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAFindPathPC</b>
      </td>
      <td style="text-align:left">Level of Find Path PC of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAHealthEnhancement</b>
      </td>
      <td style="text-align:left">Level of Health Enhancement of the current group leader (not your own
        ability level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAHealthRegen</b>
      </td>
      <td style="text-align:left">Level of Health Regen of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAHoTT</b>
      </td>
      <td style="text-align:left">Level of HoTT of the current group leader (not your own ability level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAInspectBuffs</b>
      </td>
      <td style="text-align:left">Level of Inspect Buffs of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAManaEnhancement</b>
      </td>
      <td style="text-align:left">Level of Mana Enhancement of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAMarkNPC</b>
      </td>
      <td style="text-align:left">Level of Mark NPC of the current group leader (not your own ability level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LANPCHealth</b>
      </td>
      <td style="text-align:left">Level of NPC Health of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LAOffenseEnhancement</b>
      </td>
      <td style="text-align:left">Level of Offense Enhancement of the current group leader (not your own
        ability level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LASpellAwareness</b>
      </td>
      <td style="text-align:left">Level of Spell Awareness of the current group leader (not your own ability
        level)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Language[</b>language name<b>]</b>
      </td>
      <td style="text-align:left">The EQ language number of the specified language. See below for language/number
        table.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Language[</b>language number<b>]</b>
        </td>
        <td style="text-align:left">Returns the EQ language name of the <em>language number</em> specified.
          See below for language/number table.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LanguageSkill[</b>language<b>]</b>
      </td>
      <td style="text-align:left">Your skill in <em>language</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LargestFreeInventory</b>
      </td>
      <td style="text-align:left">Size of your largest free inventory space</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LargestFreeInventory</b>
      </td>
      <td style="text-align:left">Size of your largest free inventory space</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-timestamp.md"><em>timestamp</em></a>
      </td>
      <td style="text-align:left"><b>LastZoned</b>
      </td>
      <td style="text-align:left">Returns a timestamp of last time you zoned</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LDoNPoints</b>
      </td>
      <td style="text-align:left">Available LDoN points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Level</b>
      </td>
      <td style="text-align:left">Character Level</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ManaBonus</b>
      </td>
      <td style="text-align:left">Mana bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ManaRegen</b>
      </td>
      <td style="text-align:left">Mana regeneration from last tick</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ManaRegenBonus</b>
      </td>
      <td style="text-align:left">Mana regen bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxBuffSlots</b>
      </td>
      <td style="text-align:left">Max number of buffs you can have on you. /echo ${Me.MaxBuffSlots}</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxEndurance</b>
      </td>
      <td style="text-align:left">Max endurance</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxHPs</b>
      </td>
      <td style="text-align:left">Max hit points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxMana</b>
      </td>
      <td style="text-align:left">Max mana</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Mercenary</b>
        </td>
        <td style="text-align:left">The state of your Mercenary, ACTIVE, SUSPENDED, or UNKNOWN (If it&apos;s
          dead). Returns NULL if you do not have a Mercenary.</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>MercenaryStance</b>
        </td>
        <td style="text-align:left">Current active mercenary stance as a string, default is NULL.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MirEarned</b>
      </td>
      <td style="text-align:left">Total LDoN points earned in Miragul&apos;s</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MMEarned</b>
      </td>
      <td style="text-align:left">Total LDoN points earned in Mistmoore</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Moving</b>
      </td>
      <td style="text-align:left">Moving? (including strafe)</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Name</b>
        </td>
        <td style="text-align:left">First name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>NumGems</b>
      </td>
      <td style="text-align:left">Returns the amount of spell gems your toon has</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Orux</b>
      </td>
      <td style="text-align:left">Orux on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>PctAAExp</b>
      </td>
      <td style="text-align:left">AA exp as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctAAVitality</b>
      </td>
      <td style="text-align:left">Percentage of AA Vitality your toon has</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctAggro</b>
      </td>
      <td style="text-align:left">Your aggro percentage</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctEndurance</b>
      </td>
      <td style="text-align:left">Current endurance as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>PctExp</b>
      </td>
      <td style="text-align:left">Experience as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>PctGroupLeaderExp</b>
      </td>
      <td style="text-align:left">Group leadership exp as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctHPs</b>
      </td>
      <td style="text-align:left">Current HP as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctMana</b>
      </td>
      <td style="text-align:left">Current mana as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>PctRaidLeaderExp</b>
      </td>
      <td style="text-align:left">Raid leadership experience as a %</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PctVitality</b>
      </td>
      <td style="text-align:left">Percentage of Vitality the toon has</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spell.md"><em>spell</em></a>
      </td>
      <td style="text-align:left"><b>PetBuff[</b>#<b>]</b>
      </td>
      <td style="text-align:left">The spell in this PetBuff slot #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PetBuff[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Finds PetBuff slot with the spell <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Phosphenes</b>
      </td>
      <td style="text-align:left">Phosphenes on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Phosphites</b>
      </td>
      <td style="text-align:left">Phosphites on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Platinum</b>
      </td>
      <td style="text-align:left">Platinum on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PlatinumBank</b>
      </td>
      <td style="text-align:left">Platinum in bank</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>PlatinumShared</b>
      </td>
      <td style="text-align:left">Platinum in shared bank</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Poisoned</b>
        </td>
        <td style="text-align:left">Returns the name of any Poison spell</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>RadiantCrystals</b>
      </td>
      <td style="text-align:left">Number of Radiant Crystals on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>RaidAssistTarget[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Current raid assist target (1-3)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>RaidLeaderExp</b>
      </td>
      <td style="text-align:left">Raid leadership exp (out of 330)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>RaidLeaderPoints</b>
      </td>
      <td style="text-align:left">Raid leadership points</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>RaidMarkNPC[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Current raid marked NPC (1-3)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>RangedReady</b>
      </td>
      <td style="text-align:left">Ranged attack ready?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>RujEarned</b>
      </td>
      <td style="text-align:left">Total LDoN points earned in Rujarkian</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Running</b>
      </td>
      <td style="text-align:left">Do I have auto-run turned on?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SecondaryPctAggro</b>
      </td>
      <td style="text-align:left">Secondary Percentage aggro</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>SecondaryAggroPlayer</b>
      </td>
      <td style="text-align:left">spawninfo for secondary aggro player</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ShieldingBonus</b>
      </td>
      <td style="text-align:left">Shielding bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Shrouded</b>
      </td>
      <td style="text-align:left">Am I Shrouded?</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Silenced</b>
        </td>
        <td style="text-align:left">Returns the name of the Silence type effect on you</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Silver</b>
      </td>
      <td style="text-align:left">Silver on your character</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SilverBank</b>
      </td>
      <td style="text-align:left">Silver in bank</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Skill[</b>name|#<b>]</b>
      </td>
      <td style="text-align:left">Skill level of skill with this <em>name</em> or <em>ID #</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SkillCap[</b>name|#<b>]</b>
      </td>
      <td style="text-align:left">Skill cap of skill with this <em>name</em> or <em>ID #</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-buff.md"><em>buff</em></a>
      </td>
      <td style="text-align:left"><b>Song[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Finds song with this <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-buff.md"><em>buff</em></a>
      </td>
      <td style="text-align:left"><b>Song[</b>#<b>]</b>
      </td>
      <td style="text-align:left">The song in this slot #</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>Spawn</b>
      </td>
      <td style="text-align:left">The character&apos;s spawn</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>SpellInCooldown</b>
      </td>
      <td style="text-align:left">returns TRUE if you have a spell in cooldown and FALSE when not.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SpellDamageBonus</b>
      </td>
      <td style="text-align:left">Spell Damage bonus</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SpellRankCap</b>
      </td>
      <td style="text-align:left">your characters spell rank cap. if it returns: 1 = Rk. I spells 2 = Rk.
        II spells 3 = Rk. III spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>SpellReady[</b>name|#<b>]</b>
      </td>
      <td style="text-align:left">Gem with this spell <em>name</em> or in this gem <em>#</em> ready to cast?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SpellShieldBonus</b>
      </td>
      <td style="text-align:left">Spell Shield bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>STA</b>
      </td>
      <td style="text-align:left">Character Stamina</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>STR</b>
      </td>
      <td style="text-align:left">Character Strength</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>StrikeThroughBonus</b>
      </td>
      <td style="text-align:left">Strikethrough bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Stunned</b>
      </td>
      <td style="text-align:left">Am I stunned?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>StunResistBonus</b>
      </td>
      <td style="text-align:left">Stun Resist bonus from gear and spells</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Subscription</b>
        </td>
        <td style="text-align:left">Subscription type GOLD, FREE, (Silver?)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>SubscriptionDays</b>
      </td>
      <td style="text-align:left">Usage: <code>/echo I have ${Me.SubscriptionDays} left before my all access expires.</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Surname</b>
        </td>
        <td style="text-align:left">Last name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svChromatic</b>
      </td>
      <td style="text-align:left">Your character&apos;s lowest resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svCold</b>
      </td>
      <td style="text-align:left">Character Cold Resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svCorruption</b>
      </td>
      <td style="text-align:left">Character Corruption Resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svDisease</b>
      </td>
      <td style="text-align:left">Character Disease Resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svFire</b>
      </td>
      <td style="text-align:left">Character Fire Resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svMagic</b>
      </td>
      <td style="text-align:left">Character Magic Resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svPoison</b>
      </td>
      <td style="text-align:left">Character Poison Resist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>svPrismatic</b>
      </td>
      <td style="text-align:left">The average of your character&apos;s resists</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>TakEarned</b>
      </td>
      <td style="text-align:left">Total LDoN points earned in Takish</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-spawn.md"><em>spawn</em></a>
      </td>
      <td style="text-align:left"><b>TargetOfTarget</b>
      </td>
      <td style="text-align:left">Target of Target (will only work when group or raid Target of Target is
        active; if not, it will return NULL)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Thirst</b>
      </td>
      <td style="text-align:left">Thirst level</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Trader</b>
      </td>
      <td style="text-align:left">if you are an active Trader</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>TributeActive</b>
      </td>
      <td style="text-align:left">Tribute Active</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-ticks.md"><em>ticks</em></a>
      </td>
      <td style="text-align:left"><b>TributeTimer</b>
      </td>
      <td style="text-align:left">Tribute Timer</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>UseAdvancedLooting</b>
      </td>
      <td style="text-align:left">TRUE/FALSE if using advanced looting</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>WIS</b>
      </td>
      <td style="text-align:left">Character Wisdom</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>XTAggroCount[</b>N<b>]</b>
      </td>
      <td style="text-align:left">
        <p><code>XTAggroCount</code>
          <br /><code>XTAggroCount[100]</code>
        </p>
        <p>Returns the number of AUTO-HATER mobs on the extended target window where
          your aggro is less than the optional parameter N. N must be between 1-100
          inclusive or it will be set to 100 (the default value).</p>
        <p></p>
        <p>${Me.XTAggroCount} and ${Me.XTAggroCount[100]} are identical.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-xtarget.md"><em>xtarget</em></a>
      </td>
      <td style="text-align:left"><b>XTarget[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Extended target data for the specified XTarget #. <b>Note: Passing no index to this returns the number of current extended targets.</b>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Vitality</b>
      </td>
      <td style="text-align:left">Total amount of Vitality your toon has</td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>To String</b>
        </td>
        <td style="text-align:left">Same as <b>Name</b>
        </td>
    </tr>
  </tbody>
</table>

## Methods

| Name | Action |
| :--- | :--- |
| **Sit** | Causes toon to sit if not already |
| **Stand** | Causes toon to stand if not already |
| **StopCast** | Causes toon to stop casting |

## Language Table

<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <ul>
          <li>1 Common Tongue</li>
          <li>2 Barbarian</li>
          <li>3 Erudian</li>
          <li>4 Elvish</li>
          <li>5 Dark Elvish</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>6 Dwarvish</li>
          <li>7 Troll</li>
          <li>8 Ogre</li>
          <li>9 Gnomish</li>
          <li>10 Halfling</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>11 Thieves Cant</li>
          <li>12 Old Erudian</li>
          <li>13 Elder Elvish</li>
          <li>14 Froglok</li>
          <li>15 Goblin</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>16 Gnoll</li>
          <li>17 Combine Tongue</li>
          <li>17 Elder Teir&apos;Dal</li>
          <li>19 Lizardman</li>
          <li>20 Orcish</li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li>21 Faerie</li>
          <li>22 Dragon</li>
          <li>23 Elder Dragon</li>
          <li>24 Dark Speech</li>
          <li>25 Vah Shir</li>
        </ul>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

### Examples

`/assist Eqmule`  
`/delay 5s ${Me.AssistComplete}==TRUE`

The delay will last either 5s OR until the assist is complete

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Me](../top-level-objects/tlo-me.md)
* [spawn](datatype-spawn.md)
* [Slot Names](../../general-information/slot-names.md)

## Ref mq2-2010121\MQ2Main\MQ2DataTypes.h

Just putting this here because list above is incomplete and dont want to keep opening source...

```text
class MQ2CharacterType : public MQ2Type
{
public:
    enum CharacterMembers
    {
        CountSongs = 2,
        MaxBuffSlots = 3,
        Exp = 4,
        Spawn = 5,
        Dar = 6,
        AAExp = 7,
        AAPoints = 8,
        CurrentHPs = 10,
        MaxHPs = 11,
        HPRegen = 12,
        PctHPs = 13,
        CurrentMana = 14,
        MaxMana = 15,
        ManaRegen = 16,
        PctMana = 17,
        Buff = 18,
        Song = 19,
        Book = 20,
        Skill = 21,
        Ability = 22,
        Cash = 24,
        CashBank = 25,
        PlatinumShared = 26,
        Grouped = 27,
        HPBonus = 28,
        ManaBonus = 29,
        GukEarned = 30,
        MMEarned = 31,
        RujEarned = 32,
        TakEarned = 33,
        MirEarned = 34,
        LDoNPoints = 35,
        CurrentFavor = 36,
        CareerFavor = 37,
        Endurance = 38,
        Inventory = 39,
        Bank = 40,
        Combat = 42,
        FreeInventory = 43,
        Gem = 44,
        SpellReady = 45,
        Drunk = 50,
        STR = 51,
        STA = 52,
        CHA = 53,
        DEX = 54,
        INT = 55,
        AGI = 56,
        WIS = 57,
        svMagic = 58,
        svFire = 59,
        svCold = 60,
        svPoison = 61,
        svDisease = 62,
        Hunger = 63,
        Thirst = 64,
        BaseSTR = 65,
        BaseSTA = 66,
        BaseCHA = 67,
        BaseDEX = 68,
        BaseINT = 69,
        BaseAGI = 70,
        BaseWIS = 71,
        PracticePoints = 72,
        PctExp = 73,
        PctAAExp = 74,
        Moving = 75,
        AbilityReady = 76,
        PetBuff = 77,
        Platinum = 78,
        Gold = 79,
        Silver = 80,
        Copper = 81,
        PlatinumBank = 82,
        GoldBank = 83,
        SilverBank = 84,
        CopperBank = 85,
        Stunned = 88,
        RangedReady = 89,
        AltTimerReady = 90,
        MaxEndurance = 91,
        PctEndurance = 92,
        AltAbility = 93,
        AltAbilityReady = 94,
        AltAbilityTimer = 95,
        CombatAbility = 96,
        CombatAbilityTimer = 97,
        LargestFreeInventory = 98,
        TargetOfTarget = 99,
        RaidAssistTarget = 100,
        GroupAssistTarget = 101,
        RaidMarkNPC = 102,
        GroupMarkNPC = 103,
        CountBuffs = 104,
        LanguageSkill = 105,
        EnduranceBonus = 106,
        CombatEffectsBonus = 107,
        ShieldingBonus = 108,
        SpellShieldBonus = 109,
        AvoidanceBonus = 110,
        AccuracyBonus = 111,
        StunResistBonus = 112,
        StrikeThroughBonus = 113,
        AttackBonus = 114,
        HPRegenBonus = 115,
        ManaRegenBonus = 116,
        DamageShieldBonus = 117,
        DoTShieldBonus = 118,
        AttackSpeed = 119,
        GroupList = 120,
        AmIGroupLeader = 121,
        CurrentEndurance = 122,
        EnduranceRegen = 123,
        FreeBuffSlots = 124,
        CurrentWeight = 125,
        AAPointsSpent = 126,
        AAPointsTotal = 127,
        TributeActive = 128,
        CombatAbilityReady = 129,
        Running = 130,
        GroupSize = 131,
        TributeTimer = 132,
        RadiantCrystals = 133,
        EbonCrystals = 134,
        Shrouded = 135,
        AutoFire = 136,
        Language = 137,
        Aura = 138,
        LAMarkNPC = 139,
        LANPCHealth = 140,
        LADelegateMA = 141,
        LADelegateMarkNPC = 142,
        LAInspectBuffs = 143,
        LASpellAwareness = 144,
        LAOffenseEnhancement = 145,
        LAManaEnhancement = 146,
        LAHealthEnhancement = 147,
        LAHealthRegen = 148,
        LAFindPathPC = 149,
        LAHoTT = 150,
        ActiveFavorCost = 151,
        CombatState = 152,
        svCorruption = 153,
        svPrismatic = 154,
        svChromatic = 155,
        Doubloons = 156,
        Orux = 157,
        Phosphenes = 158,
        Phosphites = 159,
        Fellowship = 160,
        Downtime = 161,
        DamageShieldMitigationBonus = 162,
        HeroicSTRBonus = 163,
        HeroicINTBonus = 164,
        HeroicWISBonus = 165,
        HeroicAGIBonus = 166,
        HeroicDEXBonus = 167,
        HeroicSTABonus = 168,
        HeroicCHABonus = 169,
        HealAmountBonus = 170,
        SpellDamageBonus = 171,
        ClairvoyanceBonus = 172,
        EnduranceRegenBonus = 173,
        Counters = 174,
        Faycites = 175,
        Chronobines = 176,
        Mercenary = 177,
        XTarget = 178,
        Haste = 179,
        MercenaryStance = 180,
        SkillCap = 181,
        GemTimer = 182,
        HaveExpansion = 183,
        PctAggro = 184,
        SecondaryPctAggro = 185,
        SecondaryAggroPlayer = 186,
        AggroLock = 187,
        ZoneBound = 188,
        ZoneBoundX = 189,
        ZoneBoundY = 190,
        ZoneBoundZ = 191,
        PctMercAAExp = 192,
        MercAAExp = 193,
        Subscription = 194,
        AAPointsAssigned = 195,
        AltCurrency = 196,
        ActiveDisc = 197,
        Commemoratives = 198,
        Nobles = 199,
        Zoning = 200,
        InInstance = 201,
        Instance = 202,
        MercListInfo = 203,
        UseAdvancedLooting = 204,
        Fists = 205,
        EnergyCrystals = 206,
        PiecesofEight = 207,
        SpellInCooldown = 208,
        Slowed = 209,
        Rooted = 210,
        Mezzed = 211,
        Crippled = 212,
        Malod = 213,
        Tashed = 214,
        Snared = 215,
        Hasted = 216,
        Aego = 217,
        Skin = 218,
        Focus = 219,
        Regen = 220,
        Symbol = 221,
        Clarity = 222,
        Pred = 223,
        Strength = 224,
        Brells = 225,
        SV = 226,
        SE = 227,
        HybridHP = 228,
        Growth = 229,
        Shining = 230,
        Beneficial = 231,
        DSed = 232,
        RevDSed = 233,
        Charmed = 234,
        CursorPlatinum = 235,
        CursorGold = 236,
        CursorSilver = 237,
        CursorCopper = 238,
        Diseased = 239,
        Poisoned = 240,
        Cursed = 241,
        Corrupted = 242,
        Krono = 243,
        XTargetSlots = 244,
        AssistComplete = 245,
        ItemReady = 246,
        NumGems = 247,
        Vitality = 248,
        PctVitality = 249,
        AAVitality = 250,
        PctAAVitality = 251,
        GuildID = 252,
        ExpansionFlags = 253,
        SPA = 254,
        BoundLocation = 255,
        SkillBase = 256,
    };
    enum CharacterMethods
    {
        Stand,
        Sit,
        Dismount,
        StopCast,
    };
```

