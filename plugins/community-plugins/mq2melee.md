# MQ2Melee

## Description

**MQ2Melee**, written by s0rCieR, is designed to provide intelligent use of SHORT TIME REUSE MELEE ABILITIES and PET HANDLING during combat, depending on current combat conditions. It was developed to replace melee-oriented functions typically used in macros.

* MQ2Melee 7.09 Updated by Maskoi 02/17/2016 \[can be found

  here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=19600](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=19600)\), in the VIP Plugin Forum.

* 6.0 Updated by Teichou 12/02/2012 for RoF, \[can be found

  here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=18581](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=18581)\)

* 5.0 and so on can be found here [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=18040)
* Previous versions can be found [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12779).

### History

The inspiration for MQ2Melee was [MQ2AutoSkills](https://macroquest2.com/phpBB3/viewtopic.php?t=9079) and [MQ2ThrowIt](https://macroquest2.com/phpBB3/viewtopic.php?t=11295). All credit for the concepts should go to Cr4zyb4rd and Bushdaka, authors of those plugins.

### Donations

s0rcier is the author. Teichou and Maskoi is the current maintainer.

If you want to give them money, look them up.

### Special Thanks

* Thumbs up and many thanks to the BETA Tester Team: A\_Druid\_00, Dark2phoenix, DigitalMocking, Lacky, Moeymoejoe,

  Outlander and Warauinu.

* Thanks to those plugin authors Busdaka, Cr4zyb4rd, Outlander, pms and Wassup for providing inspiration and help.
* And finally thanks to Dark2phoenix and Wasted for updating and maintaining this wiki page.

### Prerequisites

1. You must have 1 point trained in any trainable Combat Ability you would like to use
2. You must have purchased the Alternate Ability you would like to use
3. You must have trained the Combat Discipline you would like to use
4. You meet any prerequisites for the use of the ability \(i.e. can't slam from a mount, can't bash without a shield or

   a two handed weapon and the AA ability, can't backstab without being behind target with a piercing weapon, etc\)

5. MQ2MoveUtils:v11 plugin is needed to use /stick parameters \[Can be found

   here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=15909](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=15909)\).

6. [MQ2Cast](mq2cast.md) is required to cast spells, activate Alternate Abilities or click items. \[Can be found

   here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=17517](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=17517)\).

7. [MQ2Exchange](mq2exchange.md) is required to find and swap items if using MQ2Cast to click items. \[Can be

   found here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=16436](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=16436)\).

8. MQ2BagWindow is required for finding and swapping items. \[Can be found

   here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=17035](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=17035)\).

9. moveitems.h is required for swapping items and compiling. \[Can be found

   here\]\([https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=17047](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=17047)\).

## Features

* Auto use abilities according to user settings and game conditions.
* Auto-equip defined items for bashing, backstabbing or ranged attack.
* Built in user conditions to restrain the use of certain abilities.
* **CHAT MONITORING:**
  * Auto-stand on Failed/Broken Feign Death.
  * Monitoring of "Begin to Cast" messages for automatic Bash/Slam/Kick or casting of defined stuns.
  * Automatic turning on/off of Attack on Enrage/Infuriate.
* **MELEE:**
  * Auto-equipping of weapon set\(s\) prior to engaging \(aggro/non-aggro sets\).
  * Auto-use of defined combat or other abilities.
  * User-configurable /stick arguments.
* **MELEE \(AGGRO MODE\):**
  * Auto Taunt when you loose aggro on target.
  * Configurable spells to cast to gain/maintain aggro.
* **MELEE \(NON AGGRO MODE\):**
  * Back off/Feign/Evade fight if your health goes below a point.
  * Auto Resume fight if your health goes back above a point.
* **RANGED:**
  * Toggle between Melee/Ranged mode according to Target distance.
  * Swap In/Out defined ranged items \(bow/throwing\).
  * Auto refill ammunition slot when less than 80 in a stack.
  * Built-in /throwit command you could use to pull \(see below for explanation\).
  * Auto-Sleep mode while auto-fire is on.
  * Configurable automatic facing of target.
* **PET HANDLING:**
  * Issue /pet back and /pet hold after each mobs dies.
  * Configure pet to wait to assist till mobs within range.
  * Configure pet to wait for a specified time before assisting.
  * Pet mend if its life goes below a certain point.
  * Option to automatically re-engage target when no longer mezzed.
  * Backup pet on enrage/infuriate events and re-engaging of target.
  * Auto /pet hold if you manually hit back button or do /pet back.
* **USER DEFINED CONDITIONS:**
  * Allows for conditional use of various abilities/disciplines.
  * Allows for customized actions based on conditional statements.
* **TOP-LEVEL OBJECTS:**
  * Provides MQ2Data information for better macro integration and HUD designs.
  * Can be used with custom user-defined conditions.

## Supported Abilities

### Combat Abilities

* See MQ2Melee\#Supported AA's, Combat Abilities, Skills & Spells by

  Class

### Alternate Advancement Abilities

* See MQ2Melee\#Supported AA's, Combat Abilities, Skills & Spells by

  Class

### Melee Disciplines

* See MQ2Melee\#Supported AA's, Combat Abilities, Skills & Spells by

  Class

### Detected Disciplines

The following Disciplines are detected to promote some combat abilities:

* Ashenhand Discipline, Assassin Discipline\(3\), Silentfist Discipline, and Thunderkick Discipline.

### Skills

* See MQ2Melee\#Supported AA's, Combat Abilities, Skills & Spells by

  Class

### Spell Handling

* Provoke can be configured to cast any AA, disc or spell. It will auto-detect if you lose aggro, and then attempt to

  use any of the defined spells to regain it.

  * To determine the proper Spell ID for any Discipline, Alternate Ability or Spell to be used with the provoke/stun

    commands use one of the following commands:

    * For Disciplines use: **/echo ${Me.CombatAbility\[${Me.CombatAbility\[\]}\].ID}**, replacing

      with the name of the Discipline.

    * For AAs, use **/aa info** . The first number \(before the AA name\) is the Spell ID.
    * For Spells, use **/echo ${Spell\[\].ID}**, replacing  with the spell name.

  * Alternatively, you can look on [Lucy](http://lucy.allakhazam.com/) for the discipline/spell/AA and get the ID

    from there.

  * Some common discipline IDs are listed below:
    * Ancient Chaos Cry \[id=5016\]
    * Bazu Bellow \[id=6173\]
    * Bellow \[id=4681\]
    * Bellow of the Mastruq \[id=5015\]
    * Berate \[id=4682\]
    * Incite \[id=4697\]
    * Mock \[id=8467\]
    * Provoke \[id=4608\]
    * Crippling Strike \[id=468\]

* Stuns can also be configured to cast any AA, disc or spells when MQ2Melee detects that your target begins to cast a

  spell.

* Provoke and Stun have built-in values, but they can always be overwritten using the command line \(eg. \*\*/melee

  provoke0=5015**\) or by editing the** _**provoke0**_ **setting in the INI file and then typing** /melee reload\*\* in game.

## Commands

* All options below are listed with on/off as the arguments used to enable/disable the option, however **true** or

  **1** can be used in place of **on**, and **false** or **0** can be used in place of **off**.

  * Example: **/melee on aggro=on taunt=on kick=1 bash=0 intimidation=false disarm=true**

* **/melee** by itself will list all abilities and settings that are available to you. Some settings are dependant on

  others being active, so may not show up until you enable the prerequisite option.

* To find the relevant Item IDs for the various options, you can use the following command:
  * **/echo ${FindItem\[=\].ID}**, replacing with the name of the item you are looking for \(no need

    to use quotes\). Eg. /echo ${FindItem\[=Blade of Carnage\].ID} results in "25210".

### /melee \[options\]

* **\[on\|off\]**

  _Turns plugin On/Off._

* **aggro**=\[on\|off\]

  \*Plugin tries to keep aggro on target using all enabled aggro abilities/disciplines until aggro is regained, or

  either you or the target dies.\*

* **aggropri**=\[Item ID\]

  _Item ID for primary weapon to be used in aggro mode._

* **aggrosec**=\[Item ID\]

  _Item ID for secondary weapon to be used in aggro mode._

* **arrow**=\[Item ID\]

  _Item ID of ammunition to use for ranged/throwing attacks._

* **backoff**=\[0-100\]

  \*Turns attack off if your life percentage goes below the designated value. Will never back off due to low health if

  aggro=on.\*

* **bash**=\[on\|off\]

  _Will try to bash target if you have a shield equipped or have have a 2-handed weapon and the 2 Hand Bash AA._

* **battleleap**=\[on\|off\]

  _Whether or not to use Battle Leap AA \(Default=0/off\)_

* **begging**=\[on\|off\]

  _Will turn attack off and beg target and turn back on._

* **bow**=\[Item ID\]

  _Item ID for ranged weapon._

* **disarm**=\[on\|off\]

  _Will try to disarm target if target is wielding a weapon._

* **downflag0-19**=\[on\|off\]

**downflag0**=\[on\|off\]  
_Whether or not to use defined DownShit0 from ini. After enabling this option, you must edit the INI file with your relevant DownShit command and then issue **/melee load** to enable it._

* **enrage**=\[on\|off\]

  \*Turns attack off and issues /pet hold \(/pet back if hold not available\) if target enrages and you are facing it.

  Automatically re-engages when enrage ends or if you are behind the target.\*

* **facing**=\[on\|off\]

  _Whether or not to face target \(checked every 2 seconds and only in ranged mode\)._

* **falls**=\[on\|off\]

  _\(Monk only\) Auto-feign to reduce aggro?._

* **holyflag0-19**=\[on\|off\]

**holyflag0**=\[on\|off\]  
_Whether or not to use defined HolyShit0 from ini. After enabling this option, you must edit the INI file with your relevant HolyShit command and then issue **/melee load** to enable it._

* **infuriate**=\[on\|off\]

  \*Turns attack off and issues /pet hold \(/pet back if hold not available\) if target infuriates and you are facing it.

  Re-engages when infuriate ends or if you are behind the target.\*

* **intimidation**=\[on\|off\]

  _Will use intimidation if available._

* **jolt**=\[0-100\]

  _Jolt every \# of hits \(0=off\)._

* **kick**=\[on\|off\]

  _Will use kick if available._

* **melee**=\[on\|off\]

  _Turn Melee Mode On/Off._

* **meleepri**=\[Item ID\]

  _Item ID for primary weapon to be used in non-aggro mode._

* **meleesec**=\[Item ID\]

  _Item ID for secondary weapon to be used in non-aggro mode_

* **mend**=\[0-100\]

  _Mend wounds if your life percentage goes below the designated value._

* **petassist**=\[on\|off\]

  \*Will send pet attack on engage and backoff on enrage/infuriate if those options are enabled. The plugin will also

  use /pet hold if you have that AA.\*

* **petdelay**=\[0-30\]

  _Will not engage pet until \[x\] seconds has passed._

* **petmend**=\[0-100\]

  \*Cast "Mend Companion" or "Replenish Companion" if pet is at or below given health % \(will cast higher of the two if

  you have both\).\*

* **petrange**=\[0-150\]

  _Will not engage pet until mob is within \[x\] range of your pet._

* **pickpocket**=\[on\|off\]

  _Turn off attack & try to pickpocket if not in aggro mode._

* **plugin**=\[on\|off\]

  _Turn plugin on/off._

* **poker**=\[Item ID\]

  _Item ID for backstabbing weapon. Will be swapped in before backstabbing if necessary._

* **pothealfast**=\[0-100\]

  _Use fast heal potion when my HP falls below \[X\]% \(default=30\)._

* **pothealover**=\[0-100\]

  _Use heal over time potion when my HP falls below \[X\]% \(default=60\)._

* **provoke0**=\[Disc/AA/Spell ID \#\]

  _ID of the Disc/AA/Spell to use for provoking \(0=off\)._

* **provoke1**=\[Disc/AA/Spell ID \#\]

  _ID of the Disc/AA/Spell to use for provoking \(0=off\)._

* **provokeend**=\[0-100\]

  _Stop trying to provoke when target's health falls below \[X\]% \(default=15\)._

* **provokemax**=\[0-100\]

  _Number of times you will try provoking aa/disc/spells to regain aggro \(default=1\)._

* **provokeonce**=\[on\|off\]

  _Only use provoke once to attempt to gain aggro._

* **range**=\[0-250\]

  _Enables ranged attacks when target is at or beyond this range._ Note that 0 disables ranged attacks completely.

* **resume**=\[0-100\]

  _Stand up and turn back attack on if your life percentage goes above this value. Used with /melee feigndeath=on._

* **shield**=\[Item ID\]

  _Item ID of shield to use for bashing_

* **slam**=\[on\|off\]

  _Will slam as often as possible._

* **sneak**=\[on\|off\]

  _Will try to sneak if not in combat._

* **standup**=\[on\|off\]

  _Will stand you on a failed FD._

* **stickdelay**=\[0-100\]

  _Wait \[X\] seconds before sticking to target._

* **stickmode**=\[0\|1\|2\]

  _If 1, it will use the \*stickcmd_ as defined in the INI file, if 0, it will use the default stick command, if 2,

  it will turn off sticking\*

* **stickrange**=\[0+\]

  _Enables sticking when target is at set distance away \(0=no sticking\)._

* **stun0**=\[Disc/AA/Spell ID \#\]

  _ID of the Disc/AA/Spell to use for stunning \(0=off\)._

* **stun1**=\[Disc/AA/Spell ID \#\]

  _ID of the Disc/AA/Spell to use for stunning \(0=off\)._

* **stunning**=\[0-100\]

  _Cast defined Stun spell\(s\) if target at or below \[X\]% and/or if detected that target is casting a spell._

* **taunt**=\[on\|off\]

  \*Will push taunt button if aggro=on and you're not the target's target. Without a TauntIF statement, this will cause

  your toon to chain taunt. If you do not wish for that, use a TauntIF command \(see below\).\*

* **throwstone**=\[0-100\]

  _Will use throw stone disc when ready and target in range._ Note: Will not use in aggro/provoke mode if provoke has

  not been used yet.

### Supported AA's, Combat Abilities, Skills & Spells by Class

#### Bard

**AA's**

* Selo's Kick

**selos**=0\|1 \[off\|on\]

* Boastful Bellow

**boastful**=0\|1 \[off\|on\]

#### Beastlord

**AA's**

* Bite of the Asp

**asp**=0\|1 \[off\|on\]

* Chameleon Strike

**cstrike**=0\|1 \[off\|on\]

* Gorilla Smash

**gorillasmash**=0\|1 \[off\|on\]

* Feral Swipe

**feralswipe**=0\|1 \[off\|on\]

* Playing Possum

**feigndeath**=\[0-100\] Attempt to feign death when life is below \[X\]%. 0=Off

* Raven's Claw

**ravens**=0\|1 \[off\|on\]

**Combat Ability**

* Bestial Vivisection, Bestial Rending, Bestial Evulsing

**bvivi**=\[0-100\] Use ability when endurance above \[X\]%. 0=Off

* Rake, Foray, Harrow, Rush, Barrage, Pummel

**rake**=\[0-100\] Use ability when endurance above \[X\]%. 0=Off

* Flurry of Claws, Tumult of Claws, Clamor of Claws

**fclaw**=\[0-100\] Use ability when endurance above \[X\]%. 0=Off

#### Berserker

**Combat Ability**

* Shared Bloodlust, Shared Brutality, Shared Savagery, Shared Viciousness

**bloodlust**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Leg Strike, Leg Cut, Leg Slice, Crippling Strike, Tendon Cleave, Tendon Sever, Tendon Shear, Tendon Lacerate, Tendon

  Slash, Tendon Gash

**cripple**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Cry Havoc

**cryhavoc**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Diversive Strike, Distracting Strike, Confusing Strike, Baffling Strike, Jarring Strike, Jarring Smash, Jarring

  Clash, Jarring Slam, Jarring Blow, Jarring Crush

**jolt**=0-100\] Jolt every \# of hits \(0=off\).

* Overpowering Frenzy, Overwhelming Frenzy, Vanquishing Frenzy

**opfrenzy**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Rage Volley, Destroyer's Volley, Giant Slayer's Volley, Annihilator's Volley, Decimator's Volley, Eradicator's

  Volley, Savage Volley, Brutal Volley

**ragevolley**=\[0-100\] Will use best ragevolley discipline that is available, ready and endurance above \[X\]% \(0=off\).

* Axe of Rallos, Axe of Graster

**rallos**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Slap in the Face, Kick in the Teeth, Punch in the Throat

**slapface**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Head Strike, Head Pummel, Head Crush, Mind Strike, Temple Blow, Temple Strike, Temple Bash, Temple Chop, Temple

  Smash, Temple Crush

**stun1**=\[Disc/AA/Spell ID \#\] ID of the Disc/AA/Spell to use for stunning \(0=off\).

* Vigorous Axe Throw, Energetic Axe Throw, Brutal Axe Throw

**vigaxe**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

#### Monk

**AA**

* Eye Gouge

**eyegouge**=0\|1 \[off\|on\]

**Combat Ability**

* Cloud of Fists

**cloud**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\)

* Feign Death, Imitate Death

**feign**=\[0-100\] Attempt to feign death when life is below \[X\]%. 0=Off

* Fists of Wu

**fistofwu**\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Leopard Claw, Dragon Fang, Clawstriker Flurry, Wheel Of Fists, Whorl Of Fists, Six-Step Pattern, Eight-Step Pattern

**leopardclaw**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Drunken Monkey

**monkey**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\)

* Calanin's Synergy, Dreamwalker's Synergy, Veilwalker's Synergy, Shadewalker's Synergy

**synergy**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Vigorous Shuriken

**vigshuriken**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

**Skills**

* Dragon Punch, Tail Rake \(Iksar\)

**dragonpunch**=0\|1 \[off\|on\] Will use if available.

* Eagle Strike

**eaglestrike**=0\|1 \[off\|on\] Will use if available.

* Flying Kick

**flyingkick**=0\|1 \[off\|on\] Will use if available.

* Mend

**mend**=0-100 \[off\|on\] Mend wounds if your life percentage goes below the designated value.

* Round Kick

**roundkick**=0\|1 \[off\|on\] Will use if available.

* Tiger Claw

**tigerclaw**=0\|1 \[off\|on\] Will use if available.

#### Paladin

**AA**

* Divine Stun, Hand of Disruption, Force of Disruption

**provoke0**=id ID of the Disc/AA/Spell to use for stunning \(0=off\).

**stun0**=id ID of the Disc/AA/Spell to use for stunning \(0=off\).

* Lay Hands

**layhand**=\[0-100\] Lay Hands on myself when my HP % falls below \[X\].

**Combat Ability**

* Righteous Indignation, Righteous Vexation, Righteous Umbrage

**rightind**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Withstand, Defy, Renounce, Reprove, Repel

**withstand**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

**Spells**

* Challenge for Honor, Trial for Honor, Charge for Honor, Confrontation for Honor, Provocation for Honor, Demand for

  Honor, Reverent Force

**challengefor**=0\|1 \[off\|on\] Activate aggro spells.

* Stun, Holy Might, Force of Akera, Force of Akilae, Ancient Force of Chaos, Force of Piety, Ancient Force of Jeron,

  Sacred Force, Force of Prexus. Solemn Force, Force of Timorous, Devout Force, Force of the Crying Seas, Earnest

  Force, Force of Marr, Force of the Iceclad

**provoke1**=id ID of the Disc/AA/Spell to use for stunning \(0=off\).

**stun1**=id ID of the Disc/AA/Spell to use for stunning \(0=off\).

* Steely Stance, Stubborn Stance, Stoic Stance, Steadfast Stance

**steely**=0\|1 \[off\|on\] Activate defensive spells.

#### Ranger

**AA**

* Ferocious Kick

**ferociouskick**=0\|1 0=OFF/1=ON

**Combat Ability**

* Jolting Snapkicks, Jolting Frontkicks, Jolting Hook Kicks, Jolting Crescent Kicks, Jolting Heel Kicks

**jltkicks**=\[0-100\] endurance

* Storm of Blades, Focused Storm of Blades

**stormblades**=0\|1 0=OFF/1=ON

**Spells**

* Jolt, Cinderjolt

**jolt**=0-100\] Jolt every \# of hits \(0=off\).

#### Rogue

**Combos**

* Assassinate

**assassinate**=0\|1 \[off\|on\] Activate the assassinate skill \(ie. Sneak, Hide, move behind target, activate Strike disc, backstab\).

**Combat Ability**

* Assault, Battery, Onslaught, Incursion

**assault**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Bleed, Wound, Lacerate, Gash

**bleed**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Jugular Slash, Jugular Slice, Jugular Sever, Jugular Gash, Jugular Lacerate

**jugular**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\)

* Pinpoint Vulnerability, Pinpoint Weaknesses, Pinpoint Vitals, Pinpoint Flaws, Pinpoint Liabilities, Pinpoint

  Deficiencies

**pinpoint**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\)

* Sneak Attack, Thief's Vengeance, Assassin Strike, Kyv Strike, Ancient Chaos Strike, Daggerfall, Razor Arc, Swift

  Blade, Dagger Lunge, Dagger Swipe, Daggerswipe, Daggerstrike, Daggerthrust

**strike**=0\|1 \[off\|on\] Use your best sneak attack disc

* Thief's Eye

**thiefeye**=\[0-100\] Uses ability if your endurance is over \[X\]%. \(0=off\).

* Vigorous Dagger-Throw, Vigorous Dagger-Strike, Energetic Dagger-Throw

**vigdagger**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

**Skills**

* Backstab

**backstab**=0\|1 \[off\|on\] Will try to back stab if you wielding a piercing weapon in your main hand and behind the target.

* Escape

**escape**=\[0-100\] Turn off Attack and use rogue escape skill if your life percentage goes below the designated value. Will never happen if aggro=on.

* Evade

**evade**=0\|1 \[off\|on\] Will attempt to evade in fight to drop some aggro each time hide skill available, strongly suggest that you set unhide=1 to authorize plugin to break invis and rejoin the fight.

* Hide

**hide**=0\|1 \[off\|on\] Will try to hide if you're not in a combat and not moving.

* Pickpocket

**pickpocket**=0\|1 \[off\|on\] Turn off attack & try to pickpocket if not in aggro mode.

* Sense Traps

**sensetraps**=\[on\|off\]  
_Will try to sense traps if not in combat._

* Sneak

**sneak**=0\|1 \[off\|on\] Will try to sneak if not in combat.

#### Shadow Knight

**AA**

* Death Peace

**feign1**=\[0-100\] Attempt to feign death when life is below \[X\]%. 0=Off

* Harm Touch

**harmtouch**=0\|1 \[off\|on\] Use Harm Touch ability when ready.

**Combat Ability**

* Withstand, Defy, Renounce, Reprove, Repel

**withstand**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Gouging Blade, Gashing Blade, Lacerating Blade

**gblade**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

**Spells**

* Feign Death, Comatose, Death Peace, Last Breath, Rigor Mortis, Last Grasp, Final Breath, Last Breath, Final Gasp,

  Terminal Breath

**feign0**=\[0-100\] Attempt to feign death when life is below \[X\]%. 0=Off

* Terror of Death, Terror of Terris, Terror of Thule, Terror of Discord, Terror of Vergalid, Terror of Soulbleeder,

  Terror of Jelvalak, Terror of Rerekalen, Terror of Poira, Terror of Narus

**provoke1**=\[Disc/AA/Spell ID \#\] ID of the Disc/AA/Spell to use for provoking \(0=off\).

* Challenge for Power, Trial for Power, Charge for Power, Confrontation for Power, Provocation for Power, Demand for

  Power, Impose for Power

**challengefor**=0\|1 \[off\|on\] Activate aggro spells.

* Steely Stance, Stubborn Stance, Stoic Stance, Steadfast Stance, Staunch Stance

**steely**=0\|1 \[off\|on\] Activate defensive spells.

#### Warrior

**AA**

* Call of Challenge

**callchallenge**=0\|1 \[off\|on\] Use Alt Ability when ready.

* Gut Punch

**gutpunch**=0\|1 \[off\|on\] Use Alt Ability when ready.

* Knee Strike

**kneestrike**=0\|1 \[off\|on\] Use Alt Ability when ready.

**Combat Ability**

* Bracing Defense, Staunch Defense, Stalwart Defense, Steadfast Defense

**defense**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Commanding Voice

**commanding**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Field Armorer, Field Outfitter, Field Defender, Field Guardian

**fieldarm**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Opportunistic Strike, Strategic Strike, Vital Strike, Vital Strike

**opportunisticstrike**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

* Provoke, Belllow, Berate, Incite, Bellow of the Mastrug, Ancient Chaos Cry, Bazu Bellow, Scowl, Sneer, Jeer, Bazu

  Bluster, Bazu Roar, Scoff, Krondal's Roar, Ridicule

**provoke1**=\[Disc/AA/Spell ID \#\] ID of the Disc/AA/Spell to use for provoking \(0=off\).

* Throat Jab

**throatjab**=\[0-100\] Use ability when endurance above \[X\]% \(0=off\).

## Top-Level Objects

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee}**

  Same as ${Melee.Enable} \(see below\).

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.AggroMode}**

  TRUE/FALSE if the plugin is operating in Aggro-mode or not.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Melee.Ammunition}**

  Count of defined ammunition or current equipped ammunition.

* [_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) **${Melee.BackAngle}**

  Angle representing heading difference with current target's back.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.BackStabbing}**

  TRUE/FALSE if **backstab** setting is on/off.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Melee.Casted}**

  Time \(in miliseconds\) elapsed since last detected spell casting \(60000 if none\).

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.Combat}**

  TRUE/FALSE if plugin enable and got valid kill target. Should replace ${Me.Combat} logic.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Melee.DiscID}**

  Spell ID of currently running discipline, 0 if none.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.Enable}**

  TRUE/FALSE if plugin on/off, NULL if not loaded.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.Engage}**

  TRUE if we have a valid kill target and it's okay to turn attack on, FALSE if not.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.Enrage}**

  Is kill target enraged?

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.GotAggro}**

  TRUE/FALSE if current target seems to be aggroed on you \(not perfect\).

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.Immobilize}**

  TRUE if you have been standing still for more then 250ms, FALSE if not.

* [_bool_](../../data-types-and-top-level-objects/data-types/datatype-bool.md) **${Melee.Infuriate}**

  TRUE if kill target is infuriated!

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Melee.MeleeMode}**

  Maximum distance to target to be considered in melee range.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Melee.RangeMode}**

  Minimum distance to target to be considered in archery range.

* [_string_]() **${Melee.Status}**

  Current plugin status, can be one or more of the following: ENGAGED, WAITING, MELEE, RANGE, ENRAGE, INFURIATE,

  BACKING, ESCAPING, FEIGNING, EVADING, FALLING, STEALING, BEGGING.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${Melee.Target}**

  SpawnID of current valid kill target, otherwise 0.

* [_float_](../../data-types-and-top-level-objects/data-types/datatype-float.md) **${Melee.ViewAngle}**

  Angle of view with current target.

Debugging TLOs:

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${meleemvb\[**idskill**\]}**

  1 if the skill is ready and target in range, 0 if not. Most combat and/or character kills that can use an ID are

  testable here. Examples of _idskills_ are: **idleopardclaw**, **idslam**, **idforage**, **idfrenzy**,

  **idtigerclaw**, **idescape**.

* [_int_](../../data-types-and-top-level-objects/data-types/datatype-int.md) **${meleemvi\[**variable**\]}**

  1/0 if the variable is set to on/off. This includes all variables that can be set on the command line.

* [_string_]() **${meleemvs\[**option**\]}**

  Evaluates _option_ based on the current conditions and target. _Options_ are all the INI options that contain

  command lines that need to be evaluated. Examples are: **bashif**, **beggingif**, **tauntif**, **holyshit0**,

  **holyshit1**, **downshit1**, **slamif**, etc. Echoing one of these options will show you how they evaluate.

## INI File

MQ2Melee saves most options for each character in the INI file called \_.ini. Most options in the INI file are set using the command line \(/melee _command=on\|off_\) and they are best set this way, and not by editing the INI file. Any options given this way are then saved to the INI file when you issue the command **/melee save**. Options that contain macro commands are set by editing the INI file and then loading the values with **/melee load**.

### "IF" Options

* The following "IF" options can be set in the INI file. They will then be evaluated before the relevant disc/skill is

  triggered.

* They all need to take the form of ${If\[_condition_,1,0\]} statements and must return an integer. Any return of 0 is

  considered FALSE, any other integer is considered TRUE.

Eg. ${If\[${Me.Combat},1,0\]} will always be evaluated correctly.

* Your defined _condition_ must not exceed 255 characters, or it will cause the plugin to crash.
* backstabif
* bashif
* beggingif
* callchallengeif
* challengeforif
* commandingif
* cryhavocif
* disarmif
* dragonpunchif
* eaglestrikeif
* evadeif
* fallsif
* feralswipeif
* fistofwuif
* flyingkickif
* forageif
* frenzyif
* harmtouchif
* pothealfastif
* pothealoverif
* hideif
* intimidationif
* joltif
* kickif
* layhandif
* leopardclawif
* mendif
* pickpocketif
* provokeif
* ragevolleyif
* rakeif
* roundkickif
* sensetrapif
* slamif
* sneakif
* strikeif
* stunningif
* tauntif
* thiefeyeif
* throwstoneif
* tigerclawif
* twistedshankif

### Other Options

* stickcmd

This command takes a list of options that should be passed to the /stick command. Eg. "hold 15"

* downshit0-downshit7

Each one of these takes a macro command that will be run when you are not in combat. Remember, you have to enable each option with **/melee downflag\#=on**.

* holyshit0-holyshit7

Each one of these takes a macro command that will be run at the beginning of combat. Remember, you have to enable each option with **/melee holyflag\#=on**.

### HolyShit and DownShit

MQ2Melee now supports up to 20 macro command lines of each that will be executed when one of the following conditions are true:

* Holyshit:

Commands will be executed when in combat, no casting going on and the cursor is free.

* Downshit:

Commands will be executed when not in combat, not casting and the cursor is free.

When setting these commands, you must be careful not to fall into an endless loop or create a spam war. Make sure that when your line finishes, it will set up something that will force it to be FALSE for a while!

These Commands are turned on and off by downflagx and holyflagx if your downshit or holyshit parses ANY macro variables, you MUST set these flags to 2 instead of 1

## INI File Examples

* Please Note: Use this section only for adding useful examples that can be included in the INI file, not for

  copy/pastes of the INI files themselves. Anyone can see what a default INI is by loading up the plugin, running

  **/melee on**, **/melee save** and then opening the INI file in Notepad.

`; Will just echo that the macro is paused (this is stupid btw, but its an example.)`  
`; SINCE WE USE A MACRO VARIABLE (ModVersion) WE NEED TO SET THE FLAG TO 2!`  
`downflag0=2`  
`downshit0=/if (${Macro.Paused}) /echo ${Macro} ${ModVersion} is PAUSED!`

`; Swapping an Avatar-proccing weapon when needed.`  
`; - The first line swaps your Ancient Prismatic Spear [id=29435] into your offhand if you don't already have it equipped and you don't have the Avatar buff`  
`; - The second line swaps your Orcish Bone Axe [id=82634] back into your offhand if it's not equipped and you have the Avatar buff already`  
`holyshit0=/if (${Me.Inventory[offhand].ID}==82634 && !${Me.Buff[avatar].ID} && ${Spell[avatar].Stacks} && (${Melee.AggroMode} && ${Melee.GotAggro})) /exchange 29435 offhand`  
`holyshit1=/if (${Me.Inventory[offhand].ID}==29435 && (${Me.Buff[avatar].ID} || !${Spell[avatar].Stacks} || (${Melee.AggroMode} && !${Melee.GotAggro}))) /exchange 82634 offhand`

`; Activating the Area Taunt AA when multiple mobs in range`  
`holyshit2=/if (${Melee.Combat} && ${SpawnCount[npc radius 50 zradius 10]}>1 && ${Me.AltAbilityReady[area taunt]} && ${Melee.AggroMode}) /alt activate 110`

`; Forage if you have a chest item (usually used to check if you awaiting a rez) and your cursor is free`  
`forageif=${If[${Me.Inventory[chest].ID} && !${Cursor.ID},1,0]}`

`;Swap in and click monk epic haste gloves [id=10652] (or monk ornate gloves [id=12623]) if needed`  
`holyshit0=/if (!${Me.Buff[Celestial Tranquility].ID} && ${Spell[Celestial Tranquility].Stacks} && ${Me.FreeBuffSlots}>=1) /casting 10652|hands`

`;For monks, toggle enrage detection if you have Master's Aura (makes you immune to enrage)`  
`holyshit2=/if (!${Me.Song[Master's Aura Effect].ID} && !${meleemvi[enrage]}) /melee enrage=1`  
`holyshit3=/if (${Me.Song[Master's Aura Effect].ID} && ${meleemvi[enrage]}) /melee enrage=0`

`; During downtime, check my clicky buffs and recast them if needed`  
`downshit0=/if (${Spell[Form of Defense I].Stacks} && !${Me.Buff[Form of Defense I].ID} && !${Me.Moving}) /casting "Shroud of the Fallen Defender"|back`  
`downshit1=/if (${Spell[Shield of the Arcane].Stacks} && !${Me.Buff[Shield of the Arcane].ID} && !${Me.Moving}) /casting "Kizrak's Chestplate of Battle"|chest`

`; Cast my clicky DS ring during combat if needed (it's insta-cast, so I can do so while in combat without affecting anything)`  
`holyshit4=/if (${Spell[Shield of the Eighth].Stacks} && !${Me.Buff[Shield of the Eighth].ID}) /casting "Velium Coldain Insignia Ring"|item`

`;Uses crippling strike to snare`  
`holyshit4=/if (${Target.CurrentHPs}<20 && ${Target.Speed}>50) /disc crippling strike`

`;During downtime, check my aura's and recast if needed`  
`downshit1=/if (!${Spell[${Me.Aura[1]}].ID} && !${Me.Moving} && !${Me.Invis} && ${Me.PctEndurance} > 4 && ${Me.Standing}) /disc Myrmidon's Aura`

`;Activate Respite on Warrior if Endurance is low and deactivate running defensive if needed`  
`downshit1=/if (${Me.PctEndurance}<25 && ${Me.CombatAbilityReady[Respite Rk. II]} && ${Me.CurrentEndurance}>100 && (${Zone.ID}!=344)) /disc Respite Rk. II`  
`downshit2=/if (${Window[CombatAbilityWnd].Child[CAW_CombatEffectLabel].Text.Equal[Staunch Defense Rk. II]} && ${Me.PctEndurance}<25) /notify CombatAbilityWnd CAW_CombatEffectButton leftmouseup`

`;Change cleric merc to reactive on named mobs, to balanced on non named mobs. Easily adjustable for DPS mercs`  
`holyshit1=/if (!${Target.Named} && ${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Stance.NotEqual[Balanced]} && ${Mercenary.Class.Name.Equal[Cleric]}) /stance balanced`  
`holyshit2=/if (${Target.Named} && ${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Stance.NotEqual[Reactive]} && ${Mercenary.Class.Name.Equal[Cleric]}) /stance reactive`

`;Pal/Sk check if target is undead and is not otherwise slowed, then use Helix of the Undying`  
`holyshit4=/if (${Target.Body.Name.Equal[Undead]} && ${Me.AltAbilityReady[2018]} && !${Bool[${Target.Slowed}]}) /alt activate 2018`  
`;Alernatively a slow weapon exchange using the Bandolier and mainhand check, if there is no enc/sham nearby to slow`  
`holyshit19=/if (!${Bool[${Target.Slowed}]} && ${Me.Inventory[mainhand].ID}!=133167 && !${SpawnCount[pc class shaman radius 50]} && !${SpawnCount[pc class enchanter radius 50]}) /Bandolier Activate Slow`  
`holyshit20=/if (${Bool[${Target.Slowed}]} && ${Me.Inventory[mainhand].ID}!=140616) /Bandolier Activate 1Hand`

`;Necro - utilize the aggro meter to FD off aggro when over a set percentage`  
`holyshit3=/if (${Me.PctAggro}>80 && ${Target.Distance}<15) /casting "Improved Death Peace" alt`

`;Sk centric but can be edited for use with any tank`  
`;first line checks if first damage mod disc is ready, the target is named , endurance is over needed amount, and there is no current disc running`  
`;second line does the same as first, but also check that first damage mod disc is unavailable`  
`;third line does same as second , except it also checks that the second damage mod disc is unavailable`  
`holyshit7=/if (${Me.CombatAbilityReady[${Spell[Unholy Guardian Discipline].RankName}]} && ${Target.Named} && ${Me.CurrentEndurance}>5300 && !${Melee.DiscID}) /disc ${Spell[Unholy Guardian Discipline].RankName}`  
`holyshit8=/if (${Me.CombatAbilityReady[${Spell[Doomscale Mantle].RankName}]} && !${Me.CombatAbilityReady[${Spell[Unholy Guardian Discipline].RankName}]} && ${Target.Named} && ${Me.CurrentEndurance}>7700 && !${Melee.DiscID}) /disc ${Spell[Doomscale Mantle].RankName}`  
`holyshit9=/if (${Me.CombatAbilityReady[${Spell[Grelleth's Carapace].RankName}]} && !${Me.CombatAbilityReady[${Spell[Doomscale Mantle].RankName}]} && !${Me.CombatAbilityReady[${Spell[Unholy Guardian Discipline].RankName}]} && ${Target.Named} && ${Me.CurrentEndurance}>2700 && !${Melee.DiscID}) /disc ${Spell[Grelleth's Carapace].RankName}`

## Optional Global INI File

MQ2Melee also has 3 global \(not character specific\) parameters that can be set in a second, optional INI file. MQ2Melee uses default values for these parameters unless it finds a file named MQ2Melee.ini that you created in the same directory. Here is an example of a MQ2Melee.ini file and a description of the parameters:

`[Settings]`  
`SpawnType=10`  
`MeleeKeys=z`  
`RangeKeys=x`

* **SpawnType**: 0 + all desired target type modifier: \(+1 PC\) \(+2 NPC\) \(+4 PC PET\) \(+8 NPC PET\) \(+16 PC CORPSE\) \(+32

  NPC CORPSE\) default is 10 \(0 for base + 2 for NPC and + 8 for NPC PET\).

* **MeleeKeys**: Melee Attack Key \(not same as eq please unless you like problems\) default is z.
* **RangeKeys**: Range Attack Key default is x.

## Troubleshooting/FAQ

* **I have made changes to my INI settings. How do I activate the new settings?**

If you have MQ2Melee loaded and use an editor to make changes to your INI file, use **/melee load** to reload your settings. Alternatively, you can unload and reload the plugin.

* **I keep having to making changes to my melee settings from the command line. How do I save the new settings?**

From the command line type **/melee save**.

* **I can't get the StickCmd to work**

With Version 4 of the MQ2Melee plugin there was a change to the StickCmd, wherein it no longer requires "/stick" in the parameters. The old format of "StickCmd=/Stick hold 10 moveback" thus becomes "StickCmd=hold 10 moveback". Also you will have to execute **/melee stickmode=1** to tell the plugin to use stick arguments from ini and not built-in default /stick behaviour.

* \*\*I get the message "Exchange: -1 slot can not be Found" or "Item "XYZ" is not found" for potion belt enabled items

  and using in downshit & holyshit command lines\*\*.

Use /potionbelt activate \# Where as \#=the potionbelt slot your item in \(example for Haste potion that is in slot 2 of the potionbelt\) downshit6=/if \(${Spell\[Elixir of Speed X\].Stacks} && !${Me.Buff\[Elixir of Speed X\].ID} && !${Me.Moving}\) /potionbelt activate 2

## See Also

* [Data Types](../../data-types-and-top-level-objects/data-types/)
* [Plugins](../../documentation/macroquest2-plugins.md)

