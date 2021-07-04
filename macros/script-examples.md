Following are examples of scripts that have been created by ModBot users over the years. Some work great, while others
work pretty well, but they all at the very least will give you some solid examples from which you can start to create
your own fantactis scripts (which you will, of course, post here as an example :)

## Heal Script Examples

### Intelligent use of Promised Renewal

------------------------------------------------------------------------------------------------------------------------

**Please note**: "PR" has been added as a precondition for heals, so this script is no longer needed (although it is
being left here as a good example). Please see the AdvHeal section of the ModBot wiki for information on using PR with
AHPreCondition.

------------------------------------------------------------------------------------------------------------------------

Unlike most other heal spells, Promised Renewal lands as a buff on the target that heals after it fades (\~18 seconds).
The challenge in the current incarnation of ModHeal is that Modheal calculates the mob's dps and along with your
target's time to live (ttl) without taking into account the PR buff - the end result is that it will often cast a big
(and mana expensive) fast heal on your target five seconds before the PR buff fades.

This script, created by Kroak, works to use PR correctly.

`[Script-CHCheck] `  
`Commands=9 `  
`C1=/declare vName string local {Spawn[{Param1}].Name} `  
`C2=/if ({NetBots[{vName}].ID} && !{NetBots[{vName}].Buff.Find[9755]} || !{Me.LAInspectBuffs} && !{NetBots[{vName}].ID} || {NetBots[{Spawn[{Param1}].Name}].Buff.Find[9755]} && {NetBots[{vName}].Duration[{NetBots[{vName}].Buff.Left[{NetBots[{vName}].Buff.Find[9755]}].Count[ ]}]}>2 && {Spawn[{Param1}].PctHPs}<55) /return TRUE `  
`C3=/if ({NetBots[{Spawn[{Param1}].Name}].Buff.Find[9755]} && ({NetBots[{vName}].Duration[{NetBots[{vName}].Buff.Left[{NetBots[{vName}].Buff.Find[9755]}].Count[ ]}]}<3 && {Param2}==13 || {NetBots[{vName}].Duration[{NetBots[{vName}].Buff.Left[{NetBots[{vName}].Buff.Find[9755]}].Count[ ]}]}<2 && {Param2}!=13)) /return FALSE `  
`C4=/if ({NetBots[{vName}].ID}) /return FALSE `  
`C5=/if ({Target.ID}!={Param1}) /target id {Param1} `  
`C6=/delay 2s {Target.ID}=={Param1} && {Target.Buff[1].ID} || {Me.TargetOfTarget.ID} `  
`C7=/if ({Target.BuffDuration[Promised Renewal]}<3) /return FALSE `  
`C8=/return TRUE`

Kroak notes the following about this script:

-   Parts of this I did in an attempt to be sure non-netbots toons are checked also, but Netbots toons are checked
    first, and the rest is untested, and I think turned off by line 4. There's a couple of reasons this isn't the
    perfect solution - Rk. II versions of the spell will require a change in the ID checked. I don't have Rk. II, so
    this just checks for buff id 9755. Also, the PctHps\<55 is a very important check. For harder fights you might want
    that a bit higher.

<!-- -->

-   The second line checks if you're attempting to cast CH and checks the duration of the buff against cast time of your
    heal.

<!-- -->

-   If you notice how long some of the lines are, you might guess why I'd like Netbots\[X\].Duration\[Y\] to take a
    spell name or ID instead of only listing by buff number.

<!-- -->

-   Anyways, my goal was to set this in my NetworkINI file, then AHPreCondition8=net-CHCheck on any toon that heals. It
    semi-works.

[**Return to main ModBot Wiki**](https://macroquest2.com/wiki/index.php/ModBot)

## Disc and Item Examples

### Procure Sap Rogue Disc

Rogues get a disc Procure Sap that summons a potion called Mugger's Sap - this item goes in your potion belt, and once
right-clicked on a humanoid, can pickpocket an item on a separate loot table. Recast on potion belt item is
approximately 20 minutes.

`ABGem3=script `  
`ABSpell3=summugger `  
`ABSpellFoci3= `  
`ABDurMod3=0 `  
`ABSpellAlias3= `  
`ABAnnounce3= `  
`ABSpellMinMana3=20 `  
`ABTarCnt3=4 `  
`ABTarType3=self cbt idle `  
`ABRecast3=FALSE `  
`ABSpellIcon3= `  
  
`[Script-summugger] `  
`Commands=3 `  
`C1=/if (!{FindItemCount[Mugger's Sap]}) /disc Procure Sap Rk. II `  
`C2=/if (!{FindItemCount[Mugger's Sap]}==0) /delay 1s {Me.Casting.ID} `  
`C3=/if (!{FindItemCount[Mugger's Sap]}==0) /delay 7s !{Me.Casting.ID}`

[**Return to main ModBot Wiki**](https://macroquest2.com/wiki/index.php/ModBot)

## Nuking and Attack Examples

### Wizard Script for Setting Nuke Order

Thanks to Bartab for this one. Bartab explains how this script works as follows:

Basically my wizard has 5 nukes, I want him to cast it in the following order : 1 3 1 3 2 ----> 1 3 1 3 2 ----> .....  
\*knowing that when I cast 1 or 3 I can have a song in my song window, in that case I want to cast 4.

-   I also want to cast 5 if I get a GoM.
-   And if I cast 4 or 5 I always want to cast 2 just after.

`[Script-setNormalOrder] `  
`Commands=13 `  
`C1=/if (!{Defined[nextCast]}) /declare nextCast int outer 0; `  
`C2=/if (!{Defined[CastOne]}) /declare CastOne int outer 0; `  
`C3=/if (!{Defined[CastTwo]}) /declare CastTwo int outer 0; `  
`C4=/if (!{Defined[CastThree]}) /declare CastThree int outer 0; `  
`C5=/if (!{Defined[CastFour]}) /declare CastFour int outer 0; `  
`C6=/multiline ; /varset ADTarCnt[1] 0 ; /varset ADTarCnt[2] 0 ; /varset ADTarCnt[3] 0 ; /varset ADTarCnt[4] 0 ; /varset ADTarCnt[5] 0 `  
`C7=/if ({nextCast}==0) /multiline ; /varset nextCast 1 ; /varcalc CastOne {CastOne}+1 ; /varset ADTarCnt[1] 1 ; /echo 1 ; /return `  
`C8=/if ({nextCast}==1) /multiline ; /varset nextCast 3 ; /varcalc CastThree {CastThree}+1 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return `  
`C9=/if ({nextCast}==3 && {CastOne}<=1) /multiline ; /varset nextCast 1 ; /varcalc CastOne {CastOne}+1 ; /varset ADTarCnt[1] 1 ; /echo 1 ; /return `  
`C10=/if ({nextCast}==3 && {CastOne}>1) /multiline ; /varset nextCast 2 ; /varcalc CastTwo {CastTwo}+1 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return `  
`C11=/if ({nextCast}==2 && {Me.Song[Flashblaze Singe].ID}) /multiline ; /varset nextCast 4 ; /varcalc CastFour {CastFour}+1 ; /varset ADTarCnt[4] 1 ; /echo 4 ; /return `  
`C12=/if ({nextCast}==2) /multiline ; /varset nextCast 3 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return `  
`C13=/if ({nextCast}==4) /multiline ; /varset nextCast 2 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset CastFour 0 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return`

An important addition to this script is to reset all of the variables after a mob dies (otherwise the ordering will get
screwed up). This is best accomplished using the ACAfter setting in the INI:

`ACAfter=/multiline ; /varset nextCast 0;/varset CastOne 0;/varset CastTwo 0;/varset CastThree 0;/varset CastFour 0`

Note: Please see the Level 85 Wizard INI example found
[**here**](https://macroquest2.com/wiki/index.php/Modbot_Class_INI_Examples#Wizard.INI) to see the nukes that Bartab
is referring to (this will provide a bit of context for his desired casting order).

### Enchanter Script for Using Mana Reiterate

Thanks to Kzboray for posting his working script (with some help from Kroak :). Kzboray says that this script can also
be used for any other Enchanter damage buff!:

`ADGem4=script`  
`ADSpell4=ddbuff`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=manar`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=20`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=100`  
`ADTarEndHP4=20`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`

`[Script-ddbuff]`  
`Commands=5`  
`C1=/if ({Me.Buff[Mana Reiterate Rk. II].ID} || {Me.PctMana}<30) /return`  
`C2=/if (!{Me.Gem[Mana Reiterate Rk. II]}) /memorize `*`Mana`` ``Reiterate`` ``Rk.`` ``II|gem7`*  
`C3=/if ({Me.Casting.ID}) /delay {Math.Calc[({Cast.Timing}/100)+1]}s {Cast.Ready}`  
`C4=/if ({Cast.Ready} && !{Cast.Ready[Mana Reiterate Rk. II]} || {NetBots[WizName].Buff.Find[{Spell[Mana Reiterate Rk. II].ID}]}) /return`  
`C5=/call Mq2Cast `*`Mana`` ``Reiterate`` ``Rk.`` ``II`*` gem7 30s CastCheck -targetid|{Group.Member[{Group.Member[WizName]}].ID}`

Simply change WizName (2 places in the C4 and C5 lines) to the name of the toon you want to be buffed and your done.
Hope this helps someone else.

[**Return to main ModBot Wiki**](https://macroquest2.com/wiki/index.php/ModBot)

## Utility Scripts

### Creating Campfires and Getting to Them

Thanks to Toomanynames for this gem :). The first script will set up the campsite fire for you and the second script
will get you to the campsite (note that there are some class specific items in the second script (bard)).

`[Script-MakeSite] `  
`Commands=15 `  
`C1=/varset Timer 120s `  
`C2=/windowstate FellowshipWnd open `  
`C3=/nomodkey /notify FellowshipWnd FP_Subwindows tabselect 2 `  
`C4=/delay 1s `  
`C5=/nomodkey /notify FellowshipWnd FP_RefreshList leftmouseup `  
`C6=/delay 2s `  
`C7=/nomodkey /notify FellowshipWnd FP_CampsiteKitList listselect 1 `  
`C8=/delay 1s `  
`C9=/nomodkey /notify FellowshipWnd FP_CampsiteKitList leftmouse 1 `  
`C10=/delay 1s `  
`C11=/nomodkey /notify FellowshipWnd FP_CreateCampsite leftmouseup `  
`C12=/delay 2s `  
`C13=/windowstate FellowshipWnd close `  
`C14=/if ({NearestSpawn[any radius 30 zradius 30 fsp].ID}) /multiline ; /bc Campsite looks good;/return `  
`C15=/bc Not sure about the Campsite `

`[Script-ToSite] `  
`Commands=7 `  
`C1=/if ({NearestSpawn[any radius 30 zradius 30 fsp].ID}) /multiline ; /bc Looks like I'm at the campsite;/return `  
`C2=/if ({Select[{Me.Class},bard]}) /twist off `  
`C3=/if ({Me.Sneaking} || {Me.Invis}) /attack `  
`C4=/delay 10s !{Me.Casting.ID} `  
`C5=/casting ''Fellowship Registration Insignia|item''`  
`C6=/delay 5s {Me.Casting.ID} `  
`C7=/delay 10s !{Me.Casting.ID}`

### Magician Pet Kits

#### Example 1 from Banderas

Before using this, you need to make room so make sure you have only 7 bags and one slot free. Make certain that you have
the PetKit script entry before all other pet toy "buffs" in the AdvBuff section so that the bag goes to the free slot
(then you can have frigid paradox stuff and others below the petkit entry).

`ABGem10=script `  
`ABSpell10=PetKit `  
`ABSpellFoci10= `  
`ABDurMod10=0 `  
`ABSpellAlias10=petkit `  
`ABAnnounce10= `  
`ABSpellMinMana10=0 `  
`ABTarCnt10=1 `  
`ABTarType10=self `  
`ABRecast10=FALSE `

`[Script-PetKit] `  
`Commands=9 `  
`C1=/if (!{Defined[PKPetName]}) /declare PKPetName string outer `  
`C2=/if ({Target.ID}!={Me.Pet.ID} && {Spawn[{Target.ID}].Type.Equal[pet]}) /varset PKPetName {Target.CleanName} `  
`C3=/if ({PKPetName.Length}<4 && {Me.Pet.ID}) /varset PKPetName {Me.Pet.CleanName} `  
`C4=/if ({PKPetName.Length}<4) /return `  
`C5=/varset Timer 10m `  
`C6=/multiline ; /autoinventory;/call CastCall {Me.CleanName} `*`cast`` ``petwep`*` `  
`C7=/multiline ; /delay 5s;/autoinventory `  
`C8=/call GiveCheck {PKPetName} `*`Summoned:`` ``Tonfa`` ``of`` ``the`` ``North`` ``Wind|Summoned:`` ``Blazing`` ``Brand`*` `  
`C9=/varset ABTarCnt[10] 0 `

-   Modify C8 to chose the wep you like for pet.
-   C9 will make the script stop redoing it again and again, so if your pet dies, simply re-start the macro or make a
    hotkey to do only petkit ones as /varset ABTarCnt\[10\] 1

#### Example 2 from Lunason

Just for fun I did up a level 85 mage pet kit script. Works pretty well. I borrowed a lot of it and assembled it to my
own liking. Only uses 1 inventory slot to do all of it's work and cleans up after itself.

Theoretically it should give a pet kit to any pet it has targeted. That's untested.

`[Script-PetKit]`  
`Commands=51`  
`;need to check for empty inventory slot`  
`;/if (!${InvSlot[22 - 29].Item.ID})`  
`;this requires 4 events to be setup`  
`;event names`  
`;   pet`  
`;   petweap`  
`;   petarmor`  
`;   petfocus`  
`C1=/if (!{Defined[PKPetName]}) /declare PKPetName string outer`  
`C2=/varset PKPetName null`  
`;if we have a pet targeted we'll equip it`  
`C3=/if ({Spawn[{Target.ID}].Type.Equal[pet]}) /varset PKPetName {Target.CleanName}`  
`;if no pet targeted and we have a pet we'll equip it`  
`C4=/if ({Me.Pet.ID} && {PKPetName.Equal[null]}) /varset PKPetName {Me.Pet.CleanName}`  
`;if no pet targeted and no pet of our own make one`  
`C5=/if (!{Me.Pet.ID}) /call CastCall {Me.CleanName} `*`cast`` ``pet`*  
`C6=/if (!{Me.Pet.ID}) /delay 3s`  
`;if no pet defined yet set the var to the new pet`  
`C7=/if ({PKPetName.Equal[null]} && {Me.Pet.ID}) /varset PKPetName {Me.Pet.CleanName}`  
`;if still no pet let them know and exit`  
`C8=/if ({PKPetName.Equal[null]}) /bc Unable to find a pet to equip`  
`C9=/if ({PKPetName.Equal[null]}) /return`  
`;check for an empty inventory slot`  
`C10=/bc equipping {PKPetName}`  
`C11=/if (!{Defined[EmptySlot]}) /declare EmptySlot string outer false`  
`C12=/if (!${InvSlot[22].Item.ID}) /varset EmptySlot true`  
`C13=/if (!${InvSlot[23].Item.ID}) /varset EmptySlot true`  
`C14=/if (!${InvSlot[24].Item.ID}) /varset EmptySlot true`  
`C15=/if (!${InvSlot[25].Item.ID}) /varset EmptySlot true`  
`C16=/if (!${InvSlot[26].Item.ID}) /varset EmptySlot true`  
`C17=/if (!${InvSlot[27].Item.ID}) /varset EmptySlot true`  
`C18=/if (!${InvSlot[28].Item.ID}) /varset EmptySlot true`  
`C19=/if (!${InvSlot[29].Item.ID}) /varset EmptySlot true`  
`C20=/if (${EmptySlot.Equal[false]}) /echo no empty slots, sorry no pet kit right now.`  
`C21=/if (${EmptySlot.Equal[false]}) /return 0`  
`;Allow for more than 30 seconds by setting the timer to 10minutes`  
`C22=/varset Timer 10m`  
`;cast the pet armor`  
`C23=/bc giving pet armor`  
`C24=/call CastCall {Me.CleanName} `*`cast`` ``petarmor`*  
`C25=/multiline ; /delay 1s;/autoinventory`  
`C26=/call GiveCheck {PKPetName} `*`Prime`` ``Plate`` ``Helm|Prime`` ``Plate`` ``Breastplate|Prime`` ``Plate`` ``Bracers|Summoned:`` ``Prime`` ``Belt`*  
`C27=/call GiveCheck {PKPetName} `*`Prime`` ``Plate`` ``Vambraces|Prime`` ``Plate`` ``Gauntlets|Prime`` ``Plate`` ``Greaves|Prime`` ``Plate`` ``Boots`*  
`;delete the phanton sachel`  
`C28=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C29=/delay 5`  
`C30=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`;cast the pet weapons`  
`C31=/echo giving pet weapons`  
`C32=/multiline ; /autoinventory;/call CastCall {Me.CleanName} `*`cast`` ``petwep`*  
`C33=/multiline ; /delay 1s;/autoinventory`  
`C34=/call GiveCheck {PKPetName} `*`Summoned:`` ``Winterbane|Summoned:`` ``Winterbane`*  
`;delete the phanton sachel`  
`C35=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C36=/delay 5`  
`C37=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`C38=/echo destroyed phanton satchel`  
`C39=/delay 1s`  
`;cast pet focus items`  
`C40=/bc giving pet focus items`  
`C41=/call CastCall {Me.CleanName} `*`cast`` ``petfocus`*  
`C42=/multiline ; /delay 1s;/autoinventory`  
`C43=/call GiveCheck {PKPetName} `*`Zabella's`` ``Linked`` ``bracelet|Zabella's`` ``Jade`` ``Bracelet|Zabella's`` ``Ridged`` ``Earhoop|Zabella's`` ``Gold`` ``Ring`*  
`;delete the phanton sachel`  
`C44=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C45=/delay 5`  
`C46=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`;cast the muzzle`  
`C47=/echo giving pet muzzle`  
`C48=/call CastCall {Me.CleanName} `*`cast`` ``muzzle`*  
`C49=/delay 1s`  
`C50=/call GiveCheck {PKPetName} `*`Summoned:`` ``Muzzle`` ``of`` ``Mowcha`*  
`C51=/bc pet {PKPetname} ready for battle!`

#### Example 3 from three-p-o

Update of Lunason's script to work with 10 inventory slots and level 86+ spells. This will summon the folded packs and
unfold them for you prior to giving out the items.  
Also, I can confirm that the theoretical part about it giving the petkit to any targeted pet does work.

`[Script-PetKit]`  
`Commands=64`  
`; this requires 8 events to be setup with AETarType=self cbt idle`  
`; event names - description`  
`;  pet`  
`;  petweap  - this summons the folded pack - example spell Grant Frightforged Armaments`  
`;  weapbag  - this unfolds the pack        - example item  Folded Pack of Frightforged Plate`  
`;  petarmor - this summons the folded pack - example spell Grant Frightforged Plate`  
`;  armorbag - this unfolds the pack        - example item  Folded Pack of Frightforged Armaments`  
`;  petfocus - this summons the folded pack - example spell Grant Nint's Heirlooms`  
`;  focusbag - this unfolds the pack        - example item  Folded Pack of Nint's Heirlooms`  
`;  visor`  
`C1=/if (!{Defined[PKPetName]}) /declare PKPetName string outer`  
`C2=/varset PKPetName null`  
`; if we have a pet targeted we'll equip it`  
`C3=/if ({Spawn[{Target.ID}].Type.Equal[pet]}) /varset PKPetName {Target.CleanName}`  
`; if no pet targeted and we have a pet we'll equip it`  
`C4=/if ({PKPetName.Equal[null]} && {Me.Pet.ID}) /varset PKPetName {Me.Pet.CleanName}`  
`; if no pet targeted and no pet of our own make one`  
`C5=/if (!{Me.Pet.ID}) /call CastCall {Me.CleanName} `*`cast`` ``pet`*  
`C6=/if (!{Me.Pet.ID}) /delay 3s`  
`; if no pet defined yet set the var to the new pet`  
`C7=/if ({PKPetName.Equal[null]} && {Me.Pet.ID}) /varset PKPetName {Me.Pet.CleanName}`  
`; if still no pet let them know and exit`  
`C8=/if ({PKPetName.Equal[null]}) /bc Unable to find a pet to equip`  
`C9=/if ({PKPetName.Equal[null]}) /return`  
`; check for an empty inventory slot`  
`C10=/bc equipping {PKPetName}`  
`; need to check for empty inventory slot`  
`; /if (!${InvSlot[23 - 32].Item.ID}) - updated to check 10 slots`  
`C11=/if (!{Defined[EmptySlot]}) /declare EmptySlot string outer false`  
`C12=/if (!{InvSlot[23].Item.ID}) /varset EmptySlot true`  
`C13=/if (!{InvSlot[24].Item.ID}) /varset EmptySlot true`  
`C14=/if (!{InvSlot[25].Item.ID}) /varset EmptySlot true`  
`C15=/if (!{InvSlot[26].Item.ID}) /varset EmptySlot true`  
`C16=/if (!{InvSlot[27].Item.ID}) /varset EmptySlot true`  
`C17=/if (!{InvSlot[28].Item.ID}) /varset EmptySlot true`  
`C18=/if (!{InvSlot[29].Item.ID}) /varset EmptySlot true`  
`C19=/if (!{InvSlot[30].Item.ID}) /varset EmptySlot true`  
`C20=/if (!{InvSlot[31].Item.ID}) /varset EmptySlot true`  
`C21=/if (!{InvSlot[32].Item.ID}) /varset EmptySlot true`  
`C22=/if (${EmptySlot.Equal[false]}) /bc no empty slots, sorry no pet kit right now.`  
`C23=/if (${EmptySlot.Equal[false]}) /return 0`  
`; Allow for more than 30 seconds by setting the timer to 10 minutes`  
`C24=/varset Timer 10m`  
`; summon the pet armor`  
`C25=/bc giving pet armor`  
`C26=/call CastCall {Me.CleanName} `*`cast`` ``petarmor`*  
`C27=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; unfold the armorbag`  
`C28=/call CastCall {Me.CleanName} `*`cast`` ``armorbag`*  
`C29=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand armor to pet`  
`; adjust the armor below to match those summoned in the bag`  
`C30=/call GiveCheck {PKPetName} `*`Frightforged`` ``Plate`` ``Helm|Frightforged`` ``Plate`` ``Breastplate|Frightforged`` ``Plate`` ``Bracers|Summoned:`` ``Frightforged`` ``Belt`*  
`C31=/call GiveCheck {PKPetName} `*`Frightforged`` ``Plate`` ``Vambraces|Frightforged`` ``Plate`` ``Gauntlets|Frightforged`` ``Plate`` ``Greaves|Frightforged`` ``Plate`` ``Boots`*  
`; delete the Phantom Satchel`  
`; **DANGER** if you are using any Phantom Satchels to store items this could be disastrous`  
`C32=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C33=/delay 5`  
`C34=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`C35=/echo destroyed Phantom Satchel`  
`C36=/delay 1s`  
`;summon the pet weapons`  
`C37=/echo giving pet weapons`  
`C38=/call CastCall {Me.CleanName} `*`cast`` ``petweap`*  
`C39=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; unfold the weapbag`  
`C40=/call CastCall {Me.CleanName} `*`cast`` ``weapbag`*  
`C41=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand weapon to pet`  
`; adjust the weapons below to match those summoned in the bag`  
`C42=/call GiveCheck {PKPetName} `*`Summoned:`` ``Frightforged`` ``Iceblade|Summoned:`` ``Frightforged`` ``Iceblade`*  
`; delete the Pouch of Quellious`  
`; **DANGER** if you are using any Pouch of Quellious' to store items this could be disastrous`  
`C43=/nomodkey /itemnotify {FindItem[Pouch of Quellious].InvSlot} leftmouseup`  
`C44=/delay 5`  
`C45=/if ({Cursor.Name.Equal[Pouch of Quellious]}) /destroy`  
`C46=/echo destroyed Pouch of Quellious`  
`C47=/delay 1s`  
`; summon pet focus items`  
`C48=/bc giving pet focus items`  
`C49=/call CastCall {Me.CleanName} `*`cast`` ``petfocus`*  
`C50=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; unfold the focusbag`  
`C51=/call CastCall {Me.CleanName} `*`cast`` ``focusbag`*  
`C52=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand focus items to pet`  
`; adjust the focus items below to match those summoned in the bag`  
`C53=/call GiveCheck {PKPetName} `*`Nint's`` ``Linked`` ``Bracelet|Nint's`` ``Jade`` ``Bracelet|Nint's`` ``Ridged`` ``Earhoop|Nint's`` ``Gold`` ``Ring`*  
`C54=/call GiveCheck {PKPetName} `*`Nint's`` ``Woven`` ``Shawl|Nint's`` ``Satin`` ``Choker`*  
`; delete the Phantom Satchel`  
`; **DANGER** if you are using any Phantom Satchels to store items this could be disastrous`  
`C55=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C56=/delay 5`  
`C57=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`C58=/echo destroyed Phantom Satchel`  
`C59=/delay 1s`  
`; summon the visor`  
`C60=/echo giving pet visor`  
`C61=/call CastCall {Me.CleanName} `*`cast`` ``visor`*  
`C62=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand the visor to pet`  
`; adjust the below to match summoned visor`  
`C63=/call GiveCheck {PKPetName} `*`Summoned:`` ``Visor`` ``of`` ``Gobeker`*  
`C64=/bc pet {PKPetName} ready for battle!`

### Buying Items

A "buy" procedure was recently added to Modbot.inc. The syntax is: *Buy <item> <quantity> <vendor name>*

`[Script-BuyStuff]`  
`Commands=1`  
`C1=/call Buy ''water flask'' 75 yenny`

### Dropping group out of task

`[Script-droptask]`  
`Commands=6`  
`C1=/if (!{Defined[k]}) /declare k int local 1`  
`C2=/if (!{Group.Member[{k}].CleanName.Equal[{Me.CleanName}]}) /multiline ; /taskremove {Group.Member[{k}]};/delay 1s`  
`C3=/varset k {Math.Calc[{k}+1]}`  
`C4=/if ({k}<={Group.Members}) /varset a 1`  
`C5=/delay 6`  
`C6=/taskquit`

### Clearing your Bot's Target

Sometimes your bots remain fixated on a target (e.g. after you switch targets, kill a mob and decide to mez/blur the
rest (think Old Man McKenzie instances)). Here is a line that you can toss on a hot key that will clear the target from
all of your ModBot bots:

`/bcaa //multiline ; /varset ACMATarget 0;/target clear`


