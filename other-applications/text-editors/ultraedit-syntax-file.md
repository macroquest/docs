# UltraEdit Syntax File

## Pre-requesites

* Windows 98, Windows Me, Windows 2000, Windows XP
* Ultraedit 11.10 or higher from [www.ultraedit.com](http://www.ultraedit.com)

## Installing the Highlighting Syntax Definition

1. Open your WORDFILE.TXT file. It is installed in the same directory as UltraEdit, usually C:\Program

   Files\UltraEdit\Wordfile.txt.

2. Copy/paste the section below into the bottom of the file.
3. Look for the next available section number to use. Section headings begin with /LXX"Language"

   where XX is a number from 1 to 20.

4. Change the section number of the code below to the next available number and it's ready to use!

## Install Highlighting Syntax for UltraEdit v15+

1. Simply copy/paste the section below into a NEW .uew file in the %appdata%\IDMComp\UltraEdit\wordfiles directory.
2. Open UltraEdit \(or close/reopen, new definitions are not available until UE is restarted.\)



Select: View &gt; View as \(Highlighting File Type\) &gt; \[whatever you named the file as from step 1 above.\]

## Highlighting Syntax Definition

```text
/L12"MacroQuest2" Line Comment Preceding Chars = [~*)|] Line Comment Num = 2|  Block Comment On = |* Block Comment Off = *| Escape Char = \ String Chars = " File Extensions = MAC INC
/Delimiters = .~ !@%^&*()+=|\[]{}:;"<>,    ?
/Function String = "%Sub[ ^t*]+^([a-zA-Z_0-9]+^)" 
/Indent Strings = "/for" "} else {" "{"
/Unindent Strings = "/next" "} else /" "} else {" "}"
/Open Brace Strings ="{" "(" "["
/Close Brace Strings ="}" ")" "]"
/Ignore Strings SOL = "|*" "*|" 
/Open Fold Strings = "sub"
/Close Fold Strings = "/return" 
/C1"Macroquest2 Commands"
// /aa /alert /alias /altkey
// /banklist /beep /bind
// /call /caption /captioncolor /cast /charinfo /cleanup /clearerrors /click /combine /ctrlkey /custombind
// /defaulthud /delay /destroy /docommand /doors /doortarget /dosocial /drop /dumpbinds /declare /deletevar /doevents
// /echo /endmacro
// /face /filter /for
// /goto
// /help /hud /highlight
// /identify /ini /itemnotify /items /itemtarget /if
// /keepkeys /keypress
// /loadcfg /loadspells /location /loginname /look /listmacros /loadhud
// /memspell /mouseto /mqfont /mqlog /mqpause /multiline /macro /mapclick /mapfilter /maphide /mapnames /mapshow
// /nomodkey /noparse /notify /next
// /plugin /popup
// /ranged /return
// /sellitem /setautorun /shiftkey /skills /spew /squelch /substitute /seterror
// /target /timed
// /unload /updateitems
// /varset /varcalc /vardata
// /where /who /whofilter /whotarget /windows /windowstate
// /stick /circle /moveto
bool
array
downto 
else
global 
int
local
main 
next
outer 
string
to timer   
/C2"EQ Commands"
// /anon /a /afk /assist /attack /auction /autojoin /autosplit
// /book /bug /b
// /camp /cast /channel /chatfontsize /consent /corpse
// /decline /disband /dismount /doability /duel /d /dynamiclights
// /em /exit
// /facepick /fastdrop /feedback /filter /follow /friend
// /gems /gsay /g /guild /guildsay /guildinvite /guildremove /guilddelete /guildstatus /guildleader /guildwar /guildpeace /guildmotd
// /help /hidecorpses /ignore /inspect /invite /invwinlabels
// /language /lfg /log /location /loc /loot /lootnodrop
// /mcicontrol /me /mousespeed /msg
// /note
// /ooc
// /pet /petition /played
// /quit
// /random /reply /report /resetwindows /reverb /reversesound /roleplay
// /serverfilter /shout /shownames /showspelleffects /sit /split /stopsong /surname
// /targetgroupbuff /tell /time /trackfilter /trackplayers /tracksort
// /usercolor
// /vrdelay
// /who /whotarget /wincolor /yell
/C3"EQ Emotes"
// /agree /amaze /apologize /applaud
// /bite /bleed /blink /blush /boggle /bonk /bored /bow /brb /burp /bye
// /cackle /calm /cheer /clap /comfort /congratulate /cough /cringe /cry /curious
// /dance /drool /duck
// /eye
// /fidget /flex
// /gasp /giggle /glare /grin /groan /grovel
// /happy /hungry
// /introduce
// /jk
// /kneel
// /lost
// /massage /moan /mourn
// /nod /nudge
// /panic /pat /peer /plead /point /ponder /purr /puzzle
// /raise /ready /roar /rofl
// /salute /shiver /shrug /sigh /smack /smirk /snarl /snicker /stare
// /tap /tease /thank /thirsty
// /veto
// /wave /welcome /whine /whistle
// /yawn
/C4"TLOs"
AltAbility
Bool
Corpse Cursor
Defined
FindItemBankCount FindItemBank FindItemCount FindItem Float Foreground FPS
GameTime Ground GroupLeaderName GroupLeader
Heading HUD
If Ini Int InvSlot Irc
LastSpawn
MacroQuest Macro MapSpawn Math MaxFPS Merchant Me
NearestSpawn
Param0 Param1 Param2 Param3 Param4 Param5 Param6 Param7 Param8 Param9 P0 P1 P2 P3 P4 P5 P6 P7 P8 P9 Plugin
Raid
Select SelectedItem Skill SpawnCount Spawn Spell Switch
Target Time Type
Window
Zone
/C5"Members"
A AAExp AAPoints AARank AARankRequired AATitle Abs Ability AbilityReady Accuracy AccuracyBonus Acos AERange AFK AltAbility AltAbilityReady AltAbilityTimer AltTimer AltTimerReady AGI AmIGroupLeader Animation Anonymous Arg Asin Assist Atan AttackBonus AttackSpeed AverageLevel AvoidanceBonus
B Base Basic Bank bazaaritem BGColor Binding Body Book Buddy Buddies Buff BuildDate BuyPrice
Calc CanCast CareerFavor Cash CashBank CastOnAnother CastOnYou Casting CastTime Centi CHA Child Channel Charges Children Class CleanName Checked ClericType Clock Combat CombatAbility CombatAbilityReady CombatAbilityTimer CombatEffectsBonus Compare CompareCS ConColor Container Connected Copper CopperBank Cos Cost Count CountBuffs CurrentFavor CurrentHPs CurrentMana CurrentWeight
D DamageShieldBonus Dar Date Day DayOfWeek Dec Deci DefaultX DefaultY DefaultZ Degrees DegreesCCW Description DEX Diety Dimensions Distance DistanceX DistanceY DistanceZ Distance3D DistancePredict DistanceW DistanceN DistanceU DMGBonus Done DoTShieldBonus DruidType Ducking Duration
E EffectType Enabled Endurance EnduranceBonus EnduranceRegen Error Exp
FeedWet Feigning Find FirstChild FizzleTime Float Foreground FreeBuffSlots FreeInventory
G GameState Gem Gender GM Gold GoldBank Group Gravity GroupAssistTarget Grouped GroupLeader GroupLeaderExp GroupLeaderPoints GroupList GroupMarkNPC GukEarned Guild GuildStatus
Heading HeadingTo HeadingToLoc Height Hex Highlighted Holding Hour Hours HPBonus HPRegen HPRegenBouns HScrollMax HScrollPos HscrollPct HUD Hunger
Int INT Inventory Invis Invited Items Item ItemID
Language LargestFreeInventory LastCommand LastTell LastSeen LDoNPoints LDoNTheme Leader Left Length Level Levitating LFG Light LineOfSight LinkDead List LoginName Look Looter Looters LootTypeLore Lower
Magic ManaBonus ManaRegen ManaRegenBonus Mark Markup Master MaxEndurance MaxRank Max MaxClip MaxHPs MaxMana MaxRange MaxRangeTo Member Members Mid Milli MinClip MinLevel Minute Minutes MirEarned MMEarned Mod Month Mount MouseX MouseY MouseOver Moving MQ2DataError MyCastTime
N Name NearestSpawn NecromancerType Next Nick Night NoDrop NoRent
Open
Pack Params Parent PctAAExp PctEndurance PctExp PctGroupLeader PctHPS PctMana PctRaidLeaderExp Pet PetBuff PetClass Platinum PlatinumBank PlatinumShared Port Precision Prev Price PureCaster PushBack
Quantity
R Race RaidAssistTarget RaidLeader RaidLeaderExp RaidLeaderPoints RaidMarkNPC Rand Range RangedReady Rank RecastTime RecastType RecoveryTime RequiresAbility RequiresAbilityPoints Return ReuseTime ResistAdj Reverse Right Roleplaying RujEarned Running RunTime
S ScreenID Second Seconds SecondsSinceMidnight SellPrice Server ShieldingBonus ShamanType ShortName Siblings Silver SilverBank Sin Sitting Size Skill SkillCapPre50 SkillCapPost50 SkyType Slot Spell Song Spawn Speed SpellReady SpellShieldBonus SpellType Sqrt STA Stack Stackable Standing StartingSkill State Status StatusID STR StrikeThroughBonus Stunned StunResistBonus Style Suffix Surname svCold svDisease svFire svMagic svPoison Swimming SyntaxError
TakEarned Tan TargetOfTarget Target TargetType Team Text Thirst Ticks Time TimeHMS Time12 Time24 Token Tooltip TotalLevels TotalMinutes TotalSeconds Trader Tribute Type
U Underwater Upper
Value VScrollMax VScrollPos VScrollPos VScrollPct
W WIS Weight WornSlots WornSlot
X
Y Year
Z
/C6"Pre-Processor"
#turbo
#define
#include
#event
#chat
Sub
** : Event_ 
/C7"Inventory Slots"
ammo arms
back
charm chest
face feet
hands head
leftear leftfinger leftwrist legs
mainhand
neck
offhand
ranged rightear rightfinger rightwrist
shoulder
waist
** bank bazaar enviro inspect loot merchant pack sharedbank trade
/C8"Operators"
.Equal
.NotEqual
.EqualCS
.NotEqualCS
.Not
*
+
-
=
//
%
&
>
<
=
!
<
>
~
\
^
$
|
{
}
```

## Using UltraEdit with the Syntax Highlighting

### What Highlighted Syntax Looks Like

A simple example of a highlighted macro:

```<font color="green">``\| _- EventTest.mac -`</font>` `<font color="green">` Demo for /doevents`</font>` `<font color="green">` Chat and YouSay are handled every loop`</font>` `<font color="green">` JudgesYou and Rude are only handled when YouSay`</font>` `<font color="green">` calls /doevents for all_ \|`</font>` ``` #turbo``  
```<font color="red">``\#chat`</font>` say``` #eventYouSay"You say, '#1#'"``  
```<font color="red">``\#event`</font>` JudgesYou `<font color="purple">`"\(\#1\#\) judges you amiably"`</font>` `<font color="red">`\#event`</font>` Rude `<font color="purple">`"\(\#1\#\) makes a rude gesture\#\*\#"`</font>` ``` Sub Main``  
```<font color="blue">``/declare`</font>` ConCheck `<font color="#0000ff">`int`</font>` `<font color="#0000ff">`outer`</font>` `<font color="#ff0000">`0`</font>` `<font color="red">`:Loop`</font>` `<font color="blue">`/doevents`</font>` `<font color="#0000ff">`/delay`</font>` `<font color="#ff0000">`2`</font>` `<font color="#0000ff">`/goto`</font>` `<font color="#ff0000">`:Loop`</font>` `<font color="#0000ff">`/return`</font>` ``` Sub Event_Chat``  
```<font color="#0000ff">``/echo`</font>` You got a `<font color="#ff0000">`${`</font><font color="#0000ff">`Param0`</font><font color="#ff0000">`}`</font>` from `<font color="#ff0000">`${`</font><font color="#0000ff">`Param1`</font><font color="#ff0000">`}:`</font>` `<font color="#ff0000">`${`</font><font color="#0000ff">`Param2`</font><font color="#ff0000">`}`</font>` `<font color="#0000ff">`/return`</font>` ``` Sub Event_YouSay(stringline,stringfirstword)``  
```<font color="#0000ff">``/echo`</font>` in YouxxxSay `<font color="#ff0000">`${`</font>`firstword`<font color="#ff0000">`}`</font>` `<font color="#ff0000">`${`</font>`firstword`<font color="#ff0000">`.NotEqual`</font>`\[Hail\]`<font color="#ff0000">`}`</font>` `<font color="#0000ff">`/if`</font>` \(`<font color="#ff0000">`${`</font>`firstword`<font color="#ff0000">`.NotEqual`</font>`\[Hail\]`<font color="#ff0000">`}`</font>`\) `<font color="#ff0000">`{`</font>` `<font color="#0000ff">`/varset`</font>` ConCheck `<font color="#ff0000">`0`</font>` `<font color="#0000ff">`/return`</font>` `<font color="#ff0000">`}`</font>` `<font color="#0000ff">`/echo`</font>` You con'd amiable `<font color="#ff0000">`${`</font>`ConCheck`<font color="#ff0000">`}`</font>` times since you last hailed.``` /return``  
`````  `<font color="#ff0000">`Sub Event\_JudgesYou`</font>`\(`<font color="#0000ff">`string`</font>` line, `<font color="#0000ff">`string`</font>` who\)``` /echoYou con'd amiable to${who}``  
```<font color="#0000ff">``/varcalc`</font>` ConCheck `<font color="#ff0000">`${`</font>`ConCheck}`<font color="#ff0000">`+1`</font>` `<font color="#0000ff">`/return`</font>` ``` Sub Event_Rude(stringline,stringwho)``  
```<font color="#0000ff">``/echo`</font>` `<font color="#ff0000">`${`</font>`who`<font color="#ff0000">`}`</font>` flipped someone off!``` /return``

You may want to change the default colors that UltraEdit chooses for the different categories. To do that navigate to: _Advanced → Configuration → Editor Display → Syntax Highlighting_ and you can change the colors to your own choosing.

### Indenting

Ultraedit will also perform automatic indenting for you. It will create an indent whenever it see you have an open "{" and will unindent whenever it see a closing "}". You can also manually reformat any section by highlighting it then choosing _Format → Indent Section_ from the UltraEdit Menu.

Note: There is currently one bug in how indenting works. It currently does not properly unindent /elseif statements. UltraEdit will also not bring the final "}" back to the beginning of the first if like it is supposed to.

Example 1: What UltraEdit Should do

`Sub ChatOut(string ChatTarget,string ChatText)`  
`/if (${ChatIn.Equal[tell]}) {`  
`/tell ${ChatInChannel} ${ChatText}`  
`} else /if (${ChatIn.Equal[Group]}) {`  
`/g ${ChatText}`  
`} else /if (${ChatIn.Equal[Raid]}) {`  
`/rs ${ChatText}`  
`} else /if (${ChatIn.Equal[Say]}) {`  
`/say ${ChatText}`  
`} else /if (${ChatIn.Equal[Channel]}) {`  
`/chat #${ChatInChannel} ${ChatText}`  
`} else /if (${ChatIn.Equal[IRC]}) {`  
`/irc ${ChatText}`  
`} else /if (${ChatIn.Equal[GUILD]}) {`  
`/gu ${ChatText}`  
`} else /if (${ChatIn.Equal[Auction]}) {`  
`/auc ${ChatText}`  
`} else {`  
`/e Incorrect Arguments: Chatin: ${ChatIn} ChatinChanel: ${ChatinChannel}`  
`/call ShowHelp`  
`}`  
`/return`

Example 2: What UltraEdit Does

`Sub ChatOut(string ChatTarget,string ChatText)`  
`/if (${ChatIn.Equal[tell]}) {`  
`/tell ${ChatInChannel} ${ChatText}`  
`} else /if (${ChatIn.Equal[Group]}) {`  
`/g ${ChatText}`  
`} else /if (${ChatIn.Equal[Raid]}) {`  
`/rs ${ChatText}`  
`} else /if (${ChatIn.Equal[Say]}) {`  
`/say ${ChatText}`  
`} else /if (${ChatIn.Equal[Channel]}) {`  
`/chat #${ChatInChannel} ${ChatText}`  
`} else /if (${ChatIn.Equal[IRC]}) {`  
`/irc ${ChatText}`  
`} else /if (${ChatIn.Equal[GUILD]}) {`  
`/gu ${ChatText}`  
`} else /if (${ChatIn.Equal[Auction]}) {`  
`/auc ${ChatText}`  
`} else {`  
`/e Incorrect Arguments: Chatin: ${ChatIn} ChatinChanel: ${ChatinChannel}`  
`/call ShowHelp`  
`}`  
`/return`

