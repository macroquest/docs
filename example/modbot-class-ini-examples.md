# Cleric

## Cleric Mid Lvl 50's

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPull=FALSE`  
`DoPet=FALSE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=`  
`MasterList=`  
`TankName=`  
`ExcludeList=a dusty box|a bitten victim|a hollow tree|`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Unswerving Hammer of Faith|gem7`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=mainhand`  
`DoAura=FALSE`  
`AuraCast=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=70`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/if (!{Me.Pet.ID} && {ACMATarget} && {Spawn[{ACMATarget}].Type.Equal[NPC]} && {Spawn[{ACMATarget}].Distance3D}<={ACLeash} && {Me.PctMana}>50) /call MBScript SumHam`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=5`  
`AHCheckTime=2`  
`AHHealOOBC=FALSE`  
  
`AHGem1=8`  
`AHSpell1=Divine Barrier`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=10`  
`AHSpellAlias1=da`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc hp15 clr`  
  
`AHGem2=3`  
`AHSpell2=Superior Healing`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=fastheal`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc pet group hp60 war30 shd30 pal30 rng mnk rog brd bst ber shm clr dru wiz mag enc nec `  
  
`AHGem3=6`  
`AHSpell3=Word of Healing`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=grpheal`  
`AHAnnounce3=/bc`  
`AHTarCnt3=3`  
`AHClass3=pc hp85 all group`  
  
`AHGem4=5`  
`AHSpell4=Complete Healing`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=ch`  
`AHAnnounce4=/bc`  
`AHTarCnt4=1`  
`AHClass4=pc group hp50 war shd pal`  
  
`AHGem5=4`  
`AHSpell5=Celestial Healing`  
`AHSpellFoci5=`  
`AHDurMod5=0`  
`AHSpellMinMana5=0`  
`AHSpellAlias5=hot`  
`AHAnnounce5=/bc`  
`AHTarCnt5=1`  
`AHClass5=pc group hp80 war shd pal rng mnk rog brd bst ber shm30 clr dru wiz mag enc nec70`  
  
`[AdvDebuff]`  
`ADCount=2`  
`ADMobMax=18`  
`ADCheckTime=2`  
  
`ADGem1=1`  
`ADSpell1=Retribution`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=dd`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=70`  
`ADSpellRecast1=2`  
`ADSpellDelay1=5`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=80`  
`ADTarEndHP1=0`  
`ADSpellCastonResist1=`  
  
`ADGem2=2`  
`ADSpell2=Force`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=stun`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=70`  
`ADSpellRecast2=3`  
`ADSpellDelay2=5`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=20`  
`ADTarEndHP2=2`  
`ADSpellCastonResist2=`  
  
`[AdvBuff]`  
`ABCount=2`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=7`  
`ABSpell1=Armor of Protection`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=buffshp`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=20`  
`ABTarCnt1=1`  
`ABTarType1=self`  
  
`ABGem2=7`  
`ABSpell2=Blessing of Temperance`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=buffghp`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=60`  
`ABTarCnt2=4`  
`ABTarType2=self grp`  
  
`[AdvEvent]`  
`AECount=0`  
`AECheckTime=8`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APBefore=`  
`APAfter=`  
`APMobMax=1`  
`APScript=AdvPull`  
  
`[AdvCure]`  
`AQCount=0`  
`AQCheckTime=8`  
  
`[Script-SumHam]`  
`Commands=2 `  
`C1=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5 `  
`C2=/if (!{Me.Pet.ID}) /multiline ; /casting ''{PetCast}'' -maxtries|2;/delay 3s`

## Level 65

These settings are currently working on the Progression servers as of 7/2/2012.

    [Settings]
    DoMelee=FALSE
    DoHeals=TRUE
    DoBuffs=FALSE
    DoDebuffs=FALSE
    DoEvents=FALSE
    DoCures=FALSE
    DoPull=FALSE
    DoPet=FALSE
    DoSit=TRUE
    DoLoot=FALSE
    DoFW=FALSE
    DoForage=FALSE
    ForageIni=forage.ini
    DoAfk=FALSE
    DoMount=FALSE
    MountCast=Brown Rope Bridle|Item
    MasterList=${NetBots.Client}
    TankName=${Group.MainTank.Name}
    Radius=90
    SitAggroRadiusCheck=75
    AfkMessage=Not now, thanks
    DeathSlot=FALSE
    NetworkINI=
    TraderName=
    FollowDistance=21
    FollowStick=21 hold uw
    PetCast=
    PetAggro=FALSE
    PetAssist=0
    PetFoci=
    PetShrink=TRUE
    PetShrinkSpell=
    [Melee]
    OffTank=FALSE
    ACLeash=50
    ACAssistPct=95
    ACManaPct=101
    ACAnnounce=
    ACMeleeCmd=/melee plugin=1
    ACBefore=
    ACAfter=
    [AdvHeal]
    AHCount=6
    AHCheckTime=2
    AHHealOOBC=FALSE
    AHHealMode=0|0|12
    AHInterruptLevel=2
    AHClassPriority=enc,clr,wiz,mag,nec,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk
    AHAllowDismount=TRUE

    AHGem1=3
    AHSpell1=Divine Barrier
    AHSpellFoci1=
    AHDurMod1=0
    AHSpellMinMana1=0
    AHSpellAlias1=db
    AHAnnounce1=/bc
    AHTarCnt1=1
    AHClass1=self hp40
    AHPreCondition1=TRUE

    AHGem2=alt
    AHSpell2=Divine Arbitration
    AHSpellFoci2=
    AHDurMod2=0
    AHSpellMinMana2=0
    AHSpellAlias2=divarb
    AHAnnounce2=/bc
    AHTarCnt2=1
    AHClass2=pc group hp35 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec
    AHPreCondition2=TRUE

    AHGem3=1
    AHSpell3=Ethereal Light
    AHSpellFoci3=
    AHDurMod3=0
    AHSpellMinMana3=0
    AHSpellAlias3=fast
    AHAnnounce3=/bc
    AHTarCnt3=1
    AHClass3=pc hp70 war30 mag enc cle wiz shm60 brd shd pal rng bst ber
    AHPreCondition3=TRUE

    AHGem4=2
    AHSpell4=Complete Heal
    AHSpellFoci4=
    AHDurMod4=0
    AHSpellMinMana4=0
    AHSpellAlias4=ch
    AHAnnounce4=/bc
    AHTarCnt4=1
    AHClass4=pc hp75 war pal shd
    AHPreCondition4=TRUE

    AHGem5=4
    AHSpell5=Supernal Elixir
    AHSpellFoci5=
    AHDurMod5=50
    AHSpellMinMana5=0
    AHSpellAlias5=hot
    AHAnnounce5=/bc
    AHTarCnt5=0
    AHClass5= hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec
    AHPreCondition5=TRUE

    AHGem6=alt
    AHSpell6=Celestial Regeneration
    AHSpellFoci6=
    AHDurMod6=0
    AHSpellMinMana6=0
    AHSpellAlias6=cregen
    AHAnnounce6=
    AHTarCnt6=3
    AHClass6=pc group hp80 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec
    AHPreCondition6=TRUE


    AHGem7=
    AHSpell7=
    AHSpellFoci7=
    AHDurMod7=0
    AHSpellMinMana7=0
    AHSpellAlias7=
    AHAnnounce7=
    AHTarCnt7=0
    AHClass7=pc pet group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec tnt mypet self
    AHPreCondition7=TRUE
    AHGem8=
    AHSpell8=
    AHSpellFoci8=
    AHDurMod8=0
    AHSpellMinMana8=0
    AHSpellAlias8=
    AHAnnounce8=
    AHTarCnt8=0
    AHClass8=pc pet group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec tnt mypet self
    AHPreCondition8=TRUE


    [AdvDebuff]
    ADCount=2
    ADMobMax=50
    ADCheckTime=6
    ADAggroOnly=0
    ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|

    ADGem1=4
    ADSpell1=Condemnation
    ADSpellFoci1= 
    ADDurMod1=0
    ADSpellAlias1=nuke
    ADAnnounce1=
    ADSpellMinMana1=70
    ADSpellRecast1=3 
    ADSpellDelay1=3
    ADTarCnt1=1
    ADTarType1=1 
    ADTarBegHP1=93
    ADTarEndHP1=20
    ADSpellCastonResist1=
    ADIfSpellImmune1=
    ADUseHoTT1=0
    ADPreCondition1=TRUE

    ADGem2=5
    ADSpell2=Mark of Karn
    ADSpellFoci2= 
    ADDurMod2=0
    ADSpellAlias2=rds
    ADAnnounce2=
    ADSpellMinMana2=70
    ADSpellRecast2=3 
    ADSpellDelay2=3
    ADTarCnt2=0 
    ADTarType2=1 
    ADTarBegHP2=99
    ADTarEndHP2=80
    ADSpellCastonResist2=
    ADIfSpellImmune2=
    ADUseHoTT2=0
    ADPreCondition2=TRUE
    [AdvBuff]
    ABCount=6
    ABMobMax=18
    ABCheckTime=8

    ABGem1=8
    ABSpell1=Hand of Virtue
    ABSpellFoci1=
    ABDurMod1=0
    ABSpellAlias1=hov
    ABAnnounce1=/bc
    ABSpellMinMana1=0
    ABTarCnt1=1
    ABTarType1=self grp
    ABRecast1=TRUE
    ABSpellIcon1=
    ABPreCondition1=TRUE

    ABGem2=7
    ABSpell2=Virtue
    ABSpellFoci2=
    ABDurMod2=0
    ABSpellAlias2=virt
    ABAnnounce2=/bc
    ABSpellMinMana2=0
    ABTarCnt2=0
    ABTarType2=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self
    ABRecast2=TRUE
    ABSpellIcon2=
    ABPreCondition2=TRUE

    ABGem3=6
    ABSpell3=Armor of the Zealot
    ABSpellFoci3=
    ABDurMod3=0
    ABSpellAlias3=shielding
    ABAnnounce3=/bc
    ABSpellMinMana3=0
    ABTarCnt3=1
    ABTarType3=self
    ABRecast3=TRUE
    ABSpellIcon3=
    ABPreCondition3=TRUE

    ABGem4=item
    ABSpell4=Breastplate of Vengeful Fury
    ABSpellFoci4=
    ABDurMod4=50
    ABSpellAlias4=spellhaste
    ABAnnounce4=
    ABSpellMinMana4=0
    ABTarCnt4=1
    ABTarType4=clr dru wiz mag enc shm nec shd pal bst rng
    ABRecast4=TRUE
    ABSpellIcon4=Blessing of Reverence
    ABPreCondition4=TRUE

    ABGem5=script 
    ABSpell5=rezgroup
    ABSpellFoci5= 
    ABDurMod5=0 
    ABSpellAlias5=rezspell
    ABAnnounce5= 
    ABSpellMinMana5=20 
    ABTarCnt5=1 
    ABTarType5=self 
    ABRecast5=FALSE
    ABSpellIcon5=
    ABPreCondition5=TRUE

    ABGem6=7
    ABSpell6=Reviviscence
    ABSpellFoci6= 
    ABDurMod6=0 
    ABSpellAlias6=rez 
    ABAnnounce6= 
    ABSpellMinMana6=20 
    ABTarCnt6=0 
    ABTarType6=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec
    ABRecast6=FALSE
    ABSpellIcon6=
    ABPreCondition6=TRUE

    [AdvEvent]
    AECustom1=
    AECustom2=
    AECustom3=
    AECount=0
    [AdvPull]
    APCheckTime=0
    APRadius=40
    APMobMax=1
    APScript=
    APPath=
    APRetPath=
    APBefore=
    APAfter=
    APAnnounce=
    APRetries=1
    [AdvCure]
    AQCount=0
    [Script-rezgroup] 
    Commands=8 
    C1=/if ({RezChkTimer}) /return 
    C2=/if (!{Defined[RezChkTimer]}) /declare RezChkTimer timer outer 80
    C3=/if (!{SpawnCount[corpse radius 80 group]}) /return 
    C4=/target id {Spawn[corpse group].ID} 
    C5=/delay 2s {Target.Type.Equal[corpse]} 
    C6=/corpse 
    C7=/call CastCall {Me.CleanName} ''cast rezspell {Spawn[corpse group].ID}''  C8=/varset RezChkTimer 80

## Level 78

Feel free to expand on it) Keep in mind the double apostraphy is missing in scripts.

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=FALSE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=TRUE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Small Black Drum|item`  
`DoAura=TRUE`  
`AuraCast=Aura of the Zealot|gem9`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=Emelia Daeren|Guardian Rhorin|`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Unflinching Hammer of Zeal|gem8`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`ForageIni=forage.ini`  
`PetShrinkSpell=`  
`SummonFood=Abundant Food|gem9`  
`SummonDrink=Abundant Drink|gem9`  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=30`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/if (!{Me.Pet.ID} && {ACMATarget} && {Spawn[{ACMATarget}].Type.Equal[NPC]} && {Spawn[{ACMATarget}].Distance3D}<={ACLeash} && {Me.PctMana}>50) /call MBScript SumHam`  
`ACAfter=`  
`[AdvHeal]`  
`AHCount=9`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
  
`AHGem1=5`  
`AHSpell1=Divine Custody Rk. II`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=barrier`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc hp20 clr self`  
  
`AHGem2=alt`  
`AHSpell2=Divine Arbitration`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=divarb`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc group hp35 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem3=3`  
`AHSpell3=Sacred Remedy Rk. II`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=remedy`  
`AHAnnounce3=/gsay`  
`AHTarCnt3=1`  
`AHClass3=pc group hp40 enc`  
  
`AHGem4=4`  
`AHSpell4=Word of Vivification`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=grpheal`  
`AHAnnounce4=/bc`  
`AHTarCnt4=3`  
`AHClass4=pc group hp80 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem5=alt`  
`AHSpell5=Celestial Regeneration`  
`AHSpellFoci5=`  
`AHDurMod5=0`  
`AHSpellMinMana5=0`  
`AHSpellAlias5=cregen`  
`AHAnnounce5=`  
`AHTarCnt5=2`  
`AHClass5=pc group hp90 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem6=1`  
`AHSpell6=Pious Light`  
`AHSpellFoci6=`  
`AHDurMod6=0`  
`AHSpellMinMana6=0`  
`AHSpellAlias6=fast`  
`AHAnnounce6=/bc`  
`AHTarCnt6=1`  
`AHClass6=pc pet hp60 war shd pal rng mnk rog brd bst ber shm45 clr dru wiz mag enc nec`  
  
`AHGem7=2`  
`AHSpell7=Complete Heal`  
`AHSpellFoci7=`  
`AHDurMod7=0`  
`AHSpellMinMana7=0`  
`AHSpellAlias7=CH`  
`AHAnnounce7=/bc CH inc for << %t  >>`  
`AHTarCnt7=1`  
`AHClass7=pc hp85 war shd pal rng85 mnk rog brd bst ber`  
  
`AHHealMode=1|6|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
  
`AHGem8=alt`  
`AHSpell8=Radiant Cure`  
`AHSpellFoci8=`  
`AHDurMod8=0`  
`AHSpellMinMana8=0`  
`AHSpellAlias8=rc3`  
`AHAnnounce8=`  
`AHTarCnt8=0`  
`AHClass8=pc group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem9=`  
`AHSpell9=`  
`AHSpellFoci9=`  
`AHDurMod9=0`  
`AHSpellMinMana9=0`  
`AHSpellAlias9=`  
`AHAnnounce9=`  
`AHTarCnt9=0`  
`AHClass9=pc pet group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec tnt mypet self`  
`AHAllowDismount=TRUE`  
  
`[AdvDebuff]`  
`ADCount=1`  
`ADMobMax=20`  
`ADCheckTime=2`  
  
`ADGem1=7`  
`ADSpell1=Shock of Wonder`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=stun`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellDelay1=20`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=40`  
`ADTarEndHP1=0`  
`ADSpellCastonResist1=`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
`ADIfSpellImmune1=`  
  
`[AdvBuff]`  
`ABCount=15`  
`ABMobMax=16`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=9`  
`ABSpell1=Armor of the Sacred`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=selfHP`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=self`  
`ABRecast1=FALSE`  
  
`ABGem2=9`  
`ABSpell2=Virtue`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=virt|virtue|`  
`ABAnnounce2=`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=self`  
`ABRecast2=TRUE`  
  
`ABGem3=6`  
`ABSpell3=Yaulp IX`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=yaulpspell`  
`ABAnnounce3=`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self cbt`  
`ABRecast3=FALSE`  
  
`ABGem4=9`  
`ABSpell4=Temerity`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=tens|tems|`  
`ABAnnounce4=`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast4=FALSE`  
  
  
`ABGem5=9`  
`ABSpell5=Symbol of Elushar`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=elu|symbol|elushar|`  
`ABAnnounce5=`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=dru grp`  
`ABRecast5=FALSE`  
  
`ABGem6=9`  
`ABSpell6=Symbol of Kazad`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=kazad`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast6=TRUE`  
  
`ABGem7=9`  
`ABSpell7=Conviction`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=conv|conviction|`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast7=FALSE`  
  
`ABGem8=script`  
`ABSpell8=weapon`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=weapon`  
`ABAnnounce8=`  
`ABSpellMinMana8=0`  
`ABTarCnt8=1`  
`ABTarType8=self cbt idle`  
`ABRecast8=FALSE`  
  
`ABGem9=9`  
`ABSpell9=Aura of Purpose`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=spellhaste`  
`ABAnnounce9=`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=self`  
  
`ABGem10=script `  
`ABSpell10=rezgroup`  
`ABSpellFoci10= `  
`ABDurMod10=0 `  
`ABSpellAlias10=rezspell`  
`ABAnnounce10= `  
`ABSpellMinMana10=0 `  
`ABTarCnt10=1 `  
`ABTarType10=self `  
`ABRecast10=FALSE`  
  
`ABGem11=item `  
`ABSpell11=Water Sprinkler of Nem Ankh`  
`ABSpellFoci11= `  
`ABDurMod11=0 `  
`ABSpellAlias11=rez `  
`ABAnnounce11= `  
`ABSpellMinMana11=0 `  
`ABTarCnt11=0 `  
`ABTarType11=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`ABRecast11=FALSE`  
  
`ABGem12=9`  
`ABSpell12=Hand of Tenacity`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=grptens`  
`ABAnnounce12=`  
`ABSpellMinMana12=0`  
`ABTarCnt12=0`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
  
`ABGem13=9`  
`ABSpell13=Rallied Aegis of Vie Rk. II`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=vie`  
`ABAnnounce13=`  
`ABSpellMinMana13=10`  
`ABTarCnt13=1`  
`ABTarType13=tank cbt idle`  
`ABRecast13=FALSE`  
  
`ABGem14=9`  
`ABSpell14=Sun Cloak`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=invisu`  
`ABAnnounce14=`  
`ABSpellMinMana14=0`  
`ABTarCnt14=0`  
`ABTarType14=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast14=FALSE`  
  
`ABGem15=`  
`ABSpell15=`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=`  
`ABAnnounce15=`  
`ABSpellMinMana15=0`  
`ABTarCnt15=0`  
`ABTarType15=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast15=FALSE`  
  
`[AdvEvent]`  
`AECount=0`  
`AECheckTime=8`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=1`  
`AQCheckTime=8`  
`AQGem1=alt`  
`AQSpell1=Radiant Cure`  
`AQSpellCntr1=0`  
`AQSpellFoci1=`  
`AQSpellCureType1=Poisoned Diseased Cursed All`  
`AQSpellMinMana1=0`  
`AQSpellRecast1=0`  
`AQTarCnt1=1`  
`AQTarType1=cbt`  
`AQSpellAlias1=rc`  
`AQAnnounce1=`  
  
`[Script-SumHam]`  
`Commands=3`  
`C1=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5`  
`C2=/if ({Me.AltAbilityReady[Celestial Hammer]}) /casting ''Celestial Hammer|alt''`  
`C3=/if (!{Me.Pet.ID}) /casting ''{PetCast}'' -maxtries|2`  
  
`[Script-rezgroup] `  
`Commands=8 `  
`C1=/if ({RezChkTimer}) /return `  
`C2=/if (!{Defined[RezChkTimer]}) /declare RezChkTimer timer outer 80`  
`C3=/if (!{SpawnCount[corpse radius 50 group]}) /return `  
`C4=/target id {Spawn[corpse group].ID} `  
`C5=/delay 2s {Target.Type.Equal[corpse]} `  
`C6=/corpse `  
`C7=/call CastCall {Me.CleanName} ''cast rezspell {Spawn[corpse group].ID}''  C8=/varset RezChkTimer 80`  
  
`[Script-weapon]`  
`Commands=3`  
`C1=/if ({InvSlot[mainhand].Item.ID}) /return`  
`C2=/casting ''Hammer of Reproach|gem9''`  
`C3=/autoinventory`

## Level 85

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=FALSE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=TRUE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Bridle of the Corrupted Sokokar|item`  
`DoAura=TRUE`  
`AuraCast=Aura of the Pious||gem9`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Unwavering Hammer of Zeal|gem8`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`PetShrinkSpell=`  
`SummonFood=Abundant Food|gem9`  
`SummonDrink=Abundant Drink|gem9`  
`NetworkINI=`  
`GoMNuke=Alias of debuff for GoM `  
`GoRMNuke=`  
`GoERMNuke=`  
`GoAERMNuke=`  
`TraderName=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=30`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/if (!{Me.Pet.ID} && {ACMATarget} && {Spawn[{ACMATarget}].Type.Equal[NPC]} && {Spawn[{ACMATarget}].Distance3D}<={ACLeash} && {Me.PctMana}>50) /call MBScript SumHam`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=8`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
`AHHealMode=1|6|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`AHGem1=5`  
`AHSpell1=Divine Eminence`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=barrier`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc hp15 clr self`  
`AHPreCondition1=TRUE`  
  
`AHGem2=alt`  
`AHSpell2=Divine Arbitration`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=divarb`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc group hp35 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition2=TRUE`  
  
`AHGem3=3`  
`AHSpell3=Devout Remedy Rk. II`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=remedy`  
`AHAnnounce3=/bc`  
`AHTarCnt3=1`  
`AHClass3=pc group hp40 enc`  
`AHPreCondition3=TRUE`  
  
`AHGem4=4`  
`AHSpell4=Word of Recovery`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=grpheal`  
`AHAnnounce4=/bc`  
`AHTarCnt4=3`  
`AHClass4=pc group hp80 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition4=TRUE`  
  
`AHGem5=alt`  
`AHSpell5=Celestial Regeneration`  
`AHSpellFoci5=`  
`AHDurMod5=0`  
`AHSpellMinMana5=0`  
`AHSpellAlias5=cregen`  
`AHAnnounce5=/bc`  
`AHTarCnt5=2`  
`AHClass5=pc group hp90 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition5=TRUE`  
  
`AHGem6=1`  
`AHSpell6=Devout Light`  
`AHSpellFoci6=`  
`AHDurMod6=0`  
`AHSpellMinMana6=0`  
`AHSpellAlias6=fast`  
`AHAnnounce6=/bc`  
`AHTarCnt6=1`  
`AHClass6=pc pet hp60 war shd pal rng mnk rog brd bst ber shm45 clr dru wiz mag enc nec`  
`AHPreCondition6=TRUE`  
  
`AHGem7=2`  
`AHSpell7=Complete Heal`  
`AHSpellFoci7=`  
`AHDurMod7=0`  
`AHSpellMinMana7=0`  
`AHSpellAlias7=CH`  
`AHAnnounce7=/bc CH inc for << %t  >>`  
`AHTarCnt7=1`  
`AHClass7=pc hp85 war shd pal rng85 mnk rog brd bst ber`  
`AHPreCondition7=TRUE`  
  
`AHGem8=alt`  
`AHSpell8=Radiant Cure`  
`AHSpellFoci8=`  
`AHDurMod8=0`  
`AHSpellMinMana8=0`  
`AHSpellAlias8=rc9`  
`AHAnnounce8=`  
`AHTarCnt8=0`  
`AHClass8=pc group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition8=TRUE`  
  
`[AdvDebuff]`  
`ADCount=1`  
`ADMobMax=100`  
`ADCheckTime=2`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=7`  
`ADSpell1=Mark of the Unsullied`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=revds`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellDelay1=300`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=95`  
`ADTarEndHP1=0`  
`ADSpellCastonResist1=`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
  
`[AdvBuff]`  
`ABCount=15`  
`ABMobMax=16`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=9`  
`ABSpell1=Armor of the Devout`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=selfHP`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=self`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
  
`ABGem2=9`  
`ABSpell2=Virtue`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=virt|virtue|`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=self`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
  
`ABGem3=6`  
`ABSpell3=Yaulp X`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=yaulpspell`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self cbt`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
  
`ABGem4=9`  
`ABSpell4=Gallantry`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=gall`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=0`  
`ABTarType4=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
  
`ABGem5=9`  
`ABSpell5=Symbol of Elushar`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=elu|symbol|elushar|`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=dru grp`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
  
`ABGem6=9`  
`ABSpell6=Symbol of Kaerra Rk. II`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=kazad`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
  
`ABGem7=9`  
`ABSpell7=Conviction`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=conv|conviction|`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
  
`ABGem8=script`  
`ABSpell8=weapon`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=weapon`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=0`  
`ABTarCnt8=1`  
`ABTarType8=self cbt idle`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
  
`ABGem9=9`  
`ABSpell9=Aura of Loyalty`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=spellhaste`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
  
`ABGem10=script `  
`ABSpell10=rezgroup`  
`ABSpellFoci10= `  
`ABDurMod10=0 `  
`ABSpellAlias10=rezspell`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=0 `  
`ABTarCnt10=1 `  
`ABTarType10=self `  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
  
`ABGem11=alt `  
`ABSpell11=Blessing of Resurrection`  
`ABSpellFoci11= `  
`ABDurMod11=0 `  
`ABSpellAlias11=rez `  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0 `  
`ABTarCnt11=0 `  
`ABTarType11=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
  
`ABGem12=9`  
`ABSpell12=Hand of Gallantry`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=grpgall`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=1`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
  
`ABGem13=9`  
`ABSpell13=Rallied Palladium of Vie`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=vie`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=10`  
`ABTarCnt13=1`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
  
`ABGem14=9`  
`ABSpell14=Distract the Departed`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=invisu`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=0`  
`ABTarType14=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
  
`ABGem15=item`  
`ABSpell15=Ornate Runed Totem Staff`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=mana`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=1`  
`ABTarType15=self`  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
  
`[AdvEvent]`  
`AECount=0`  
`AECheckTime=8`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=1`  
`AQCheckTime=8`  
  
`AQGem1=alt`  
`AQSpell1=Radiant Cure`  
`AQSpellCntr1=0`  
`AQSpellFoci1=`  
`AQSpellCureType1=Poisoned Diseased Cursed All`  
`AQSpellMinMana1=0`  
`AQSpellRecast1=0`  
`AQTarCnt1=1`  
`AQTarType1=cbt`  
`AQSpellAlias1=rc`  
`AQAnnounce1=/bc`  
  
`[Script-SumHam]`  
`Commands=3`  
`C1=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5`  
`C2=/if ({Me.AltAbilityReady[Celestial Hammer]}) /casting ''Celestial Hammer|alt''`  
`C3=/if (!{Me.Pet.ID}) /casting ''{PetCast}'' -maxtries|2`  
  
`[Script-rezgroup] `  
`Commands=8 `  
`C1=/if ({RezChkTimer}) /return `  
`C2=/if (!{Defined[RezChkTimer]}) /declare RezChkTimer timer outer 80`  
`C3=/if (!{SpawnCount[corpse radius 50 group]}) /return `  
`C4=/target id {Spawn[corpse group].ID} `  
`C5=/delay 2s {Target.Type.Equal[corpse]} `  
`C6=/corpse `  
`C7=/call CastCall {Me.CleanName} ''cast rezspell {Spawn[corpse group].ID}''`  
`C8=/varset RezChkTimer 80`  
  
`[Script-weapon]`  
`Commands=3`  
`C1=/if ({InvSlot[mainhand].Item.ID}) /return`  
`C2=/casting ''Hammer of Reproach|gem9''`  
`C3=/autoinventory`

## Level 100

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=TRUE`  
`DoPull=FALSE`  
`DoPet=FALSE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Bridle of the Corrupted Sokokar|item`  
`MasterList=${NetBots.Client} `  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`PetShrink=FALSE`  
`PetShrinkSpell=`  
`GoMNuke=Alias of debuff for GoM `  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=100`  
`ACAssistPct=98`  
`ACManaPct=30`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=11`  
`AHCheckTime=1`  
`AHHealOOBC=TRUE`  
`AHHealMode=1|6|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`AHGem1=alt`  
`AHSpell1=Bestow Divine Aura`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=barrier`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc hp15 clr self`  
`AHPreCondition1=TRUE`  
  
`AHGem2=alt`  
`AHSpell2=Divine Arbitration`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=divarb`  
`AHAnnounce2=/bc`  
`AHTarCnt2=0`  
`AHClass2=pc group hp35 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition2=TRUE`  
  
`AHGem3=1`  
`AHSpell3=Fifteenth Emblem`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=fast`  
`AHAnnounce3=/bc`  
`AHTarCnt3=1`  
`AHClass3=pc group hp45 war shd pal`  
`AHPreCondition3=TRUE`  
  
`AHGem4=2`  
`AHSpell4=Graceful Remedy`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=remedy`  
`AHAnnounce4=/bc`  
`AHTarCnt4=1`  
`AHClass4=pc group hp60 war shd pal brd`  
`AHPreCondition4=TRUE`  
  
`AHGem5=6`  
`AHSpell5=Word of Renewal`  
`AHSpellFoci5=`  
`AHDurMod5=0`  
`AHSpellMinMana5=0`  
`AHSpellAlias5=grpheal`  
`AHAnnounce5=/bc`  
`AHTarCnt5=3`  
`AHClass5=pc group hp80 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition5=TRUE`  
  
`AHGem6=7`  
`AHSpell6=Elixir of the Acquittal`  
`AHSpellFoci6=`  
`AHDurMod6=0`  
`AHSpellMinMana6=0`  
`AHSpellAlias6=grpregen`  
`AHAnnounce6=/bc`  
`AHTarCnt6=3`  
`AHClass6=pc group hp95 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition6=TRUE`  
  
`AHGem7=3`  
`AHSpell7=Reverent Light`  
`AHSpellFoci7=`  
`AHDurMod7=0`  
`AHSpellMinMana7=0`  
`AHSpellAlias7=heal`  
`AHAnnounce7=/bc`  
`AHTarCnt7=1`  
`AHClass7=pc hp90 war shd pal rng85 mnk rog brd bst ber`  
`AHPreCondition7=TRUE`  
  
`AHGem8=8`  
`AHSpell8=Virtuous Intervention`  
`AHSpellFoci8=`  
`AHDurMod8=0`  
`AHSpellMinMana8=0`  
`AHSpellAlias8=inter`  
`AHAnnounce8=/bc`  
`AHTarCnt8=1`  
`AHClass8=pc group hp80 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition8=TRUE`  
  
`AHGem9=5`  
`AHSpell9=Promised Reformation`  
`AHSpellFoci9=`  
`AHDurMod9=0`  
`AHSpellMinMana9=0`  
`AHSpellAlias9=promise`  
`AHAnnounce9=/bc`  
`AHTarCnt9=1`  
`AHClass9=pc hp95 war shd pal rng85 mnk rog brd bst ber`  
`AHPreCondition9=PR`  
  
`AHGem10=4`  
`AHSpell10=Reverent Elixir`  
`AHSpellFoci10=`  
`AHDurMod10=0`  
`AHSpellMinMana10=0`  
`AHSpellAlias10=elixir`  
`AHAnnounce10=/bc`  
`AHTarCnt10=1`  
`AHClass10=hp95 war shd pal rng85 mnk rog brd bst ber`  
`AHPreCondition10=TRUE`  
  
`AHGem11=alt`  
`AHSpell11=Radiant Cure`  
`AHSpellFoci11=`  
`AHDurMod11=0`  
`AHSpellMinMana11=0`  
`AHSpellAlias11=rc9`  
`AHAnnounce11=/bc`  
`AHTarCnt11=0`  
`AHClass11=pc pet group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec tnt mypet self`  
`AHPreCondition11=TRUE`  
  
`[AdvDebuff]`  
`ADCount=2`  
`ADMobMax=100`  
`ADCheckTime=2`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=10`  
`ADSpell1=Olsif's Retort`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=rds`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellCastonResist1=`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=98`  
`ADTarEndHP1=90`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=9`  
`ADSpell2=Virtuous Contravention`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=contra`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=0`  
`ADSpellCastonResist2=`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=98`  
`ADTarEndHP2=0`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`[AdvBuff]`  
`ABCount=31`  
`ABMobMax=100`  
`ABCheckTime=8`  
  
`ABGem1=12`  
`ABSpell1=Virtue`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=virt|virtue|`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=0`  
`ABTarType1=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
`ABPreCondition1=TRUE`  
  
`ABGem2=12`  
`ABSpell2=Conviction`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=conv|conviction|`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=12`  
`ABSpell3=Tenacity`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=ten|tenacity`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=0`  
`ABTarType3=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=12`  
`ABSpell4=Gallantry`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=gal|gallantry`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=0`  
`ABTarType4=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=12`  
`ABSpell5=Reliance`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=reli`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=0`  
`ABTarType5=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=12`  
`ABSpell6=Unified Hand of Certitude`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=gcred`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=3`  
`ABTarType6=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast6=FALSE`  
`ABSpellIcon6=Certitude`  
`ABPreCondition6=TRUE`  
  
`ABGem7=12`  
`ABSpell7=Unified Certitude`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=cred`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=1`  
`ABTarType7=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast7=FALSE`  
`ABSpellIcon7=Certitude`  
`ABPreCondition7=TRUE`  
  
`ABGem8=12`  
`ABSpell8=Rallied Bastion of Vie`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=gvie`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=0`  
`ABTarCnt8=3`  
`ABTarType8=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=12`  
`ABSpell9=Bastion of Vie`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=vie`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec grp pet`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=12`  
`ABSpell10=Symbol of Ealdun`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=eal|symbol|ealdun|`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=0`  
`ABTarCnt10=1`  
`ABTarType10=dru grp`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=11`  
`ABSpell11=Armor of the Reverent`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=selfHP`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=1`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=item`  
`ABSpell12=Cloak of Soothing`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=spikes`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=1`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=item`  
`ABSpell13=Arctender's Signet of Station`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=geo`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=0`  
`ABTarCnt13=0`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Tuankod's Earring of Hope`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=might`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=1`  
`ABTarType14=self`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`ABGem15=item`  
`ABSpell15=Face of Dread`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=end`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=1`  
`ABTarType15=self`  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
`ABPreCondition15=TRUE`  
  
`ABGem16=item`  
`ABSpell16=Brilliant Band of Arcane Knowledge`  
`ABSpellFoci16=`  
`ABDurMod16=0`  
`ABSpellAlias16=past`  
`ABAnnounce16=/bc`  
`ABSpellMinMana16=0`  
`ABTarCnt16=1`  
`ABTarType16=self`  
`ABRecast16=FALSE`  
`ABSpellIcon16=`  
`ABPreCondition16=TRUE`  
  
`ABGem17=item`  
`ABSpell17=Radiating Loop of Regeneration`  
`ABSpellFoci17=`  
`ABDurMod17=0`  
`ABSpellAlias17=def`  
`ABAnnounce17=/bc`  
`ABSpellMinMana17=0`  
`ABTarCnt17=0`  
`ABTarType17=self`  
`ABRecast17=FALSE`  
`ABSpellIcon17=`  
`ABPreCondition17=TRUE`  
  
`ABGem18=item`  
`ABSpell18=Bloodclaw Hide Spaulders`  
`ABSpellFoci18=`  
`ABDurMod18=0`  
`ABSpellAlias18=dodge`  
`ABAnnounce18=/bc`  
`ABSpellMinMana18=0`  
`ABTarCnt18=1`  
`ABTarType18=self`  
`ABRecast18=FALSE`  
`ABSpellIcon18=`  
`ABPreCondition18=TRUE`  
  
`ABGem19=item`  
`ABSpell19=Kelkos' Beaded Girdle`  
`ABSpellFoci19=`  
`ABDurMod19=0`  
`ABSpellAlias19=mind`  
`ABAnnounce19=/bc`  
`ABSpellMinMana19=0`  
`ABTarCnt19=1`  
`ABTarType19=self`  
`ABRecast19=FALSE`  
`ABSpellIcon19=`  
`ABPreCondition19=TRUE`  
  
`ABGem20=item`  
`ABSpell20=Holy Scepter of the Sky`  
`ABSpellFoci20=`  
`ABDurMod20=0`  
`ABSpellAlias20=ward`  
`ABAnnounce20=/bc`  
`ABSpellMinMana20=0`  
`ABTarCnt20=1`  
`ABTarType20=self`  
`ABRecast20=FALSE`  
`ABSpellIcon20=`  
`ABPreCondition20=TRUE`  
  
`ABGem21=11`  
`ABSpell21=Yaulp XIII`  
`ABSpellFoci21=`  
`ABDurMod21=0`  
`ABSpellAlias21=yaulpspell`  
`ABAnnounce21=/bc`  
`ABSpellMinMana21=0`  
`ABTarCnt21=0`  
`ABTarType21=self cbt`  
`ABRecast21=FALSE`  
`ABSpellIcon21=`  
`ABPreCondition21=TRUE`  
  
`ABGem22=12`  
`ABSpell22=Distract the Departed`  
`ABSpellFoci22=`  
`ABDurMod22=0`  
`ABSpellAlias22=invisu`  
`ABAnnounce22=/bc`  
`ABSpellMinMana22=0`  
`ABTarCnt22=0`  
`ABTarType22=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast22=FALSE`  
`ABSpellIcon22=`  
`ABPreCondition22=TRUE`  
  
`ABGem23=script`  
`ABSpell23=weapon`  
`ABSpellFoci23=`  
`ABDurMod23=0`  
`ABSpellAlias23=weapon`  
`ABAnnounce23=/bc`  
`ABSpellMinMana23=0`  
`ABTarCnt23=0`  
`ABTarType23=self cbt idle`  
`ABRecast23=FALSE`  
`ABSpellIcon23=`  
`ABPreCondition23=TRUE`  
  
`ABGem24=script`  
`ABSpell24=rezgroup`  
`ABSpellFoci24=`  
`ABDurMod24=0`  
`ABSpellAlias24=rezspell`  
`ABAnnounce24=/bc`  
`ABSpellMinMana24=0`  
`ABTarCnt24=0`  
`ABTarType24=self`  
`ABRecast24=FALSE`  
`ABSpellIcon24=`  
`ABPreCondition24=TRUE`  
  
`ABGem25=alt`  
`ABSpell25=Blessing of Resurrection`  
`ABSpellFoci25=`  
`ABDurMod25=0`  
`ABSpellAlias25=rez`  
`ABAnnounce25=/bc`  
`ABSpellMinMana25=0`  
`ABTarCnt25=0`  
`ABTarType25=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`ABRecast25=FALSE`  
`ABSpellIcon25=`  
`ABPreCondition25=TRUE`  
  
`ABGem26=12`  
`ABSpell26=Shining Bastion`  
`ABSpellFoci26=`  
`ABDurMod26=0`  
`ABSpellAlias26=def`  
`ABAnnounce26=/bc`  
`ABSpellMinMana26=10`  
`ABTarCnt26=1`  
`ABTarType26=tank idle cbt`  
`ABRecast26=FALSE`  
`ABSpellIcon26=`  
`ABPreCondition26=TRUE`  
  
`ABGem27=11`  
`ABSpell27=Aura of the Reverent`  
`ABSpellFoci27=`  
`ABDurMod27=0`  
`ABSpellAlias27=aura1`  
`ABAnnounce27=/bc`  
`ABSpellMinMana27=10`  
`ABTarCnt27=1`  
`ABTarType27=self aura`  
`ABRecast27=FALSE`  
`ABSpellIcon27=`  
`ABPreCondition27=TRUE`  
  
`ABGem28=11`  
`ABSpell28=Aura of Divinity`  
`ABSpellFoci28=`  
`ABDurMod28=0`  
`ABSpellAlias28=aura2`  
`ABAnnounce28=/bc`  
`ABSpellMinMana28=10`  
`ABTarCnt28=1`  
`ABTarType28=self aura`  
`ABRecast28=FALSE`  
`ABSpellIcon28=`  
`ABPreCondition28=TRUE`  
  
`ABGem29=11`  
`ABSpell29=Hand of Graceful Infusion`  
`ABSpellFoci29=`  
`ABDurMod29=0`  
`ABSpellAlias29=proc`  
`ABAnnounce29=/bc`  
`ABSpellMinMana29=10`  
`ABTarCnt29=1`  
`ABTarType29=tank cbt`  
`ABRecast29=FALSE`  
`ABSpellIcon29=`  
`ABPreCondition29=TRUE`  
  
`ABGem30=item`  
`ABSpell30=Ring of the Ancients`  
`ABSpellFoci30=`  
`ABDurMod30=0`  
`ABSpellAlias30=shrink`  
`ABAnnounce30=/bc`  
`ABSpellMinMana30=10`  
`ABTarCnt30=0`  
`ABTarType30=self`  
`ABRecast30=FALSE`  
`ABSpellIcon30=`  
`ABPreCondition30=TRUE`  
  
`ABGem31=item`  
`ABSpell31=Polymorph Wand: Dark Bellikos`  
`ABSpellFoci31=`  
`ABDurMod31=0`  
`ABSpellAlias31=illusion`  
`ABAnnounce31=/bc`  
`ABSpellMinMana31=0`  
`ABTarCnt31=0`  
`ABTarType31=self`  
`ABRecast31=FALSE`  
`ABSpellIcon31=`  
`ABPreCondition31=TRUE`  
  
`[AdvEvent]`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=1`  
`AQCheckTime=8`  
  
`AQGem1=alt`  
`AQSpell1=Radiant Cure`  
`AQSpellCntr1=0`  
`AQSpellFoci1=`  
`AQSpellCureType1=Poisoned Diseased Cursed All`  
`AQSpellMinMana1=0`  
`AQSpellRecast1=0`  
`AQTarCnt1=1`  
`AQTarType1=grp cbt idle `  
`AQSpellAlias1=rc`  
`AQAnnounce1=/bc`  
  
`[Script-SumHam]`  
`Commands=3`  
`C1=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5`  
`C2=/if ({Me.AltAbilityReady[Celestial Hammer]}) /casting ''Celestial Hammer|alt''`  
`C3=/if (!{Me.Pet.ID}) /casting ''{PetCast}'' -maxtries|2`  
  
`[Script-rezgroup] `  
`Commands=8 `  
`C1=/if ({RezChkTimer}) /return `  
`C2=/if (!{Defined[RezChkTimer]}) /declare RezChkTimer timer outer 80`  
`C3=/if (!{SpawnCount[corpse radius 50 group]}) /return `  
`C4=/target id {Spawn[corpse group].ID} `  
`C5=/delay 2s {Target.Type.Equal[corpse]} `  
`C6=/corpse `  
`C7=/call CastCall {Me.CleanName} ''cast rez {Spawn[corpse group].ID}''`  
`C8=/varset RezChkTimer 80`  
  
`[Script-weapon]`  
`Commands=3`  
`C1=/if ({InvSlot[mainhand].Item.ID}) /return`  
`C2=/casting ''Hammer of Reproach|gem10''`  
`C3=/autoinventory`  
  
`[Script-PR]`  
`Commands=0`  
`C1=/return`

# Paladin

## Low 50's

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=FALSE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=TRUE`  
`DoPet=FALSE`  
`DoSit=FALSE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=`  
`TankName=`  
`ExcludeList=a bitten victim|a hollow tree|`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`DoMount=FALSE`  
`MountCast=`  
`DoPull=FALSE`  
`DoCures=FALSE`  
`DeathSlot=mainhand`  
`DoAura=FALSE`  
`AuraCast=`  
  
  
`[Melee]`  
`OffTank=TRUE`  
`ACLeash=50`  
`ACAssistPct=99`  
`ACManaPct=0`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee load`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=2`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
  
`AHGem1=5`  
`AHSpell1=Greater Healing`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=60`  
`AHSpellAlias1=heal`  
`AHAnnounce1=`  
`AHTarCnt1=1`  
`AHClass1=group pc hp30 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem2=8`  
`AHSpell2=Wave of Life`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=40`  
`AHSpellAlias2=grpheal`  
`AHAnnounce2=/bc `  
`AHTarCnt2=3`  
`AHClass2=group pc hp80 all`  
  
`[AdvDebuff]`  
`ADCount=0`  
`ADMobMax=10`  
`ADCheckTime=2`  
  
`ADGem1=2`  
`ADSpell1=Cease`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=pull`  
`ADAnnounce1=`  
`ADSpellMinMana1=40`  
`ADSpellRecast1=0`  
`ADSpellDelay1=0`  
`ADTarCnt1=0`  
`ADTarType1=0`  
`ADTarBegHP1=0`  
`ADTarEndHP1=0`  
  
`[AdvBuff]`  
`ABCount=6`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=7`  
`ABSpell1=Instrument of Nife`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=buffproc`  
`ABAnnounce1=`  
`ABSpellMinMana1=40`  
`ABTarCnt1=1`  
`ABTarType1=self`  
  
`ABGem2=7`  
`ABSpell2=Brell's Steadfast Aegis`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=buffhp`  
`ABAnnounce2=`  
`ABSpellMinMana2=0`  
`ABTarCnt2=3`  
`ABTarType2=self grp`  
  
`ABGem3=7`  
`ABSpell3=Symbol of Pinzarn`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=buffsym`  
`ABAnnounce3=`  
`ABSpellMinMana3=40`  
`ABTarCnt3=0`  
`ABTarType3=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec grp`  
  
`ABGem4=7`  
`ABSpell4=Armor of Faith`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=buffsym`  
`ABAnnounce4=`  
`ABSpellMinMana4=40`  
`ABTarCnt4=0`  
`ABTarType4=war shd pal rng mnk rog brd bst ber clr grp`  
  
`ABGem5=7`  
`ABSpell5=Valor of Marr`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=selfhaste`  
`ABAnnounce5=`  
`ABSpellMinMana5=40`  
`ABTarCnt5=0`  
`ABTarType5=self grp`  
  
`ABGem6=6`  
`ABSpell6=Yaulp II`  
`ABSpellFoci6=`  
`ABDurMod6=95`  
`ABSpellAlias6=yaulp`  
`ABAnnounce6=`  
`ABSpellMinMana6=40`  
`ABTarCnt6=1`  
`ABTarType6=self cbt`  
  
`[AdvEvent]`  
`AECount=0`  
`AECheckTime=0`  
  
`[AdvCure]`  
`AQCount=0`  
`AQCheckTime=0`  
  
`AQGem2=7`  
`AQSpell2=Counteract Poison`  
`AQSpellCntr2=8`  
`AQSpellFoci2=`  
`AQSpellCureType2=Poisoned`  
`AQSpellMinMana2=0`  
`AQSpellRecast2=5`  
`AQTarCnt2=1`  
`AQTarType2=self grp testing only`  
`AQSpellAlias2=curep`  
`AQAnnounce2=/bc`  
  
`AQGem1=7`  
`AQSpell1=Cure Disease`  
`AQSpellCntr1=8`  
`AQSpellFoci1=`  
`AQSpellCureType1=Diseased`  
`AQSpellMinMana1=0`  
`AQSpellRecast1=5`  
`AQTarCnt1=1`  
`AQTarType1=self bla`  
`AQSpellAlias1=cured`  
`AQAnnounce1=/bc`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APBefore=`  
`APAfter=`  
`APMobMax=1`  
`APScript=Pull`

# Beastlord

## Late lvl 40's

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPet=TRUE`  
`DoSit=FALSE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=`  
`TankName=`  
`ExcludeList=a hollow tree|            `  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`AfkMessage=Not now, thanks`  
  
`PetCast=Spirit of Keshuval|gem8 -invis`  
`PetAggro=FALSE`  
`PetAssist=1`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACMobStick=6 !front`  
`ACLeash=50`  
`ACAssistPct=98`  
`ACManaPct=50`  
`ACParams=/melee plugin=1 petassist=on petdelay=1 petrange=200 feigndeath=30 enrage=on infuriate=on`  
`ACAnnounce=/bc`  
  
`[AdvHeal]`  
`AHCount=2`  
`AHCheckTime=1`  
  
`AHGem1=6`  
`AHSpell1=Keshuval's Rejuvenation`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellAlias1=petheal`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pet hp75 all`  
  
`AHGem2=5`  
`AHSpell2=Light Healing`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellAlias2=small heal`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=group pc hp30 clr dru wiz mag enc nec`  
  
`[AdvDebuff]`  
`ADCount=2`  
`ADMobMax=10`  
`ADCheckTime=2`  
  
`ADGem1=4`  
`ADSpell1=Drowsy`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=slow`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=30`  
`ADSpellRecast1=0`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=11`  
`ADTarBegHP1=100`  
`ADTarEndHP1=25`  
  
`ADGem2=2`  
`ADSpell2=Tainted Breath`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=psndot`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=60`  
`ADSpellRecast2=0`  
`ADSpellDelay2=20`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=95`  
`ADTarEndHP2=75`  
  
`ADGem3=3`  
`ADSpell3=Sicken`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=dsedot`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=60`  
`ADSpellRecast3=0`  
`ADSpellDelay3=20`  
`ADTarCnt3=0`  
`ADTarType3=1`  
`ADTarBegHP3=99`  
`ADTarEndHP3=90`  
  
`ADGem4=1`  
`ADSpell4=Blast of Frost`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=colddd`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=40`  
`ADSpellRecast4=0`  
`ADSpellDelay4=10`  
`ADTarCnt4=0`  
`ADTarType4=1`  
`ADTarBegHP4=90`  
`ADTarEndHP4=40`  
  
`[AdvBuff]`  
`ABCount=4`  
`ABMobMax=12`  
`ABCheckTime=8`  
  
`ABGem1=7`  
`ABSpell1=Strengthen`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=str`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=40`  
`ABTarCnt1=1`  
`ABTarType1=war shd pal rng mnk rog brd bst nec pet grp`  
  
`ABGem2=7`  
`ABSpell2=Spirit of Bear`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=sta`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=40`  
`ABTarCnt2=1`  
`ABTarType2=war shd pal rng mnk rog brd bst ber nec clr dru wiz enc grp`  
  
`ABGem3=7`  
`ABSpell3=Inner Fire`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=`  
`ABAnnounce3=`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
  
`ABGem4=7`  
`ABSpell4=Spirit of the Blizzard`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=petbuff`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=30`  
`ABTarCnt4=1`  
`ABTarType4=mypet`  
  
`[AdvEvent]`  
`AECount=0`

# Shadowknight

## Level 69

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=TRUE `  
`DoBuffs=FALSE `  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoCures=FALSE `  
`DoPull=TRUE `  
`DoPet=TRUE `  
`DoSit=FALSE `  
`DoLoot=TRUE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`DoAfk=FALSE `  
`DoMount=FALSE `  
`MountCast= `  
`DoAura=FALSE `  
`AuraCast= `  
`MasterList=MastersGalore `  
`TankName=Me `  
`ExcludeList= `  
`Radius=100 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Not now, thanks `  
`DeathSlot= `  
`FollowDistance=20 `  
`FollowStick=20 hold uw `  
`PetCast=Son of Decay|gem4 `  
`PetAggro=FALSE `  
`PetAssist=0 `  
`PetFoci=`  
  
`[Melee] `  
`OffTank=TRUE `  
`ACLeash=50 `  
`ACAssistPct=100 `  
`ACManaPct=70 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 `  
`ACBefore= `  
`ACAfter= `  
`[AdvHeal] `  
`AHCount=0 `  
  
`[AdvDebuff] `  
`ADCount=5 `  
`ADMobMax=10 `  
`ADCheckTime=2 `  
  
`ADGem1=6 `  
`ADSpell1=Theft of Pain `  
`ADSpellFoci1= `  
`ADDurMod1=0 `  
`ADSpellAlias1=acdebuff `  
`ADAnnounce1= `  
`ADSpellMinMana1=10 `  
`ADSpellRecast1=0 `  
`ADSpellCastonResist1= `  
`ADSpellDelay1=0 `  
`ADTarCnt1=1 `  
`ADTarType1=1 `  
`ADTarBegHP1=100 `  
`ADTarEndHP1=100 `  
  
`ADGem2=2 `  
`ADSpell2=Festering Darkness `  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2=snare `  
`ADAnnounce2= `  
`ADSpellMinMana2=10 `  
`ADSpellRecast2=0 `  
`ADSpellCastonResist2= `  
`ADSpellDelay2=0 `  
`ADTarCnt2=1 `  
`ADTarType2=1 `  
`ADTarBegHP2=100 `  
`ADTarEndHP2=0 `  
  
`ADGem3=1 `  
`ADSpell3=Inruku's Bite `  
`ADSpellFoci3= `  
`ADDurMod3=0 `  
`ADSpellAlias3=bite `  
`ADAnnounce3= `  
`ADSpellMinMana3=10 `  
`ADSpellRecast3=0 `  
`ADSpellCastonResist3= `  
`ADSpellDelay3=0 `  
`ADTarCnt3=1 `  
`ADTarType3=1 `  
`ADTarBegHP3=100 `  
`ADTarEndHP3=5 `  
  
`ADGem4=5 `  
`ADSpell4=Aura of Hate `  
`ADSpellFoci4= `  
`ADDurMod4=0 `  
`ADSpellAlias4=atkdebuff `  
`ADAnnounce4= `  
`ADSpellMinMana4=10 `  
`ADSpellRecast4=0 `  
`ADSpellCastonResist4= `  
`ADSpellDelay4=0 `  
`ADTarCnt4=1 `  
`ADTarType4=1 `  
`ADTarBegHP4=95 `  
`ADTarEndHP4=10 `  
  
`ADGem5=3 `  
`ADSpell5=Bond of Inruku `  
`ADSpellFoci5= `  
`ADDurMod5=0 `  
`ADSpellAlias5=bond `  
`ADAnnounce5= `  
`ADSpellMinMana5=10 `  
`ADSpellRecast5=0 `  
`ADSpellCastonResist5= `  
`ADSpellDelay5=0 `  
`ADTarCnt5=1 `  
`ADTarType5=1 `  
`ADTarBegHP5=90 `  
`ADTarEndHP5=10 `  
  
  
`[AdvBuff] `  
`ABCount=4 `  
`ABMobMax=12 `  
`ABCheckTime=8 `  
`ABProactive=TRUE `  
  
`ABGem1=4 `  
`ABSpell1=Cloak of Luclin `  
`ABSpellFoci1= `  
`ABDurMod1=0 `  
`ABSpellAlias1=selfbuff `  
`ABAnnounce1= `  
`ABSpellMinMana1=10 `  
`ABTarCnt1=1 `  
`ABTarType1=self `  
  
`ABGem2=4 `  
`ABSpell2=Shroud of Discord `  
`ABSpellFoci2= `  
`ABDurMod2=0 `  
`ABSpellAlias2=proc `  
`ABAnnounce2= `  
`ABSpellMinMana2=10 `  
`ABTarCnt2=1 `  
`ABTarType2=self `  
  
`ABGem3=7 `  
`ABSpell3=Voice of Thule `  
`ABSpellFoci3= `  
`ABDurMod3=0 `  
`ABSpellAlias3=hatemod `  
`ABAnnounce3= `  
`ABSpellMinMana3=10 `  
`ABTarCnt3=1 `  
`ABTarType3=self `  
  
`ABGem4=4 `  
`ABSpell4=Rune of Decay `  
`ABSpellFoci4= `  
`ABDurMod4=0 `  
`ABSpellAlias4=petbuff `  
`ABAnnounce4= `  
`ABSpellMinMana4=10 `  
`ABTarCnt4=1 `  
`ABTarType4=mypet `  
  
`[AdvEvent] `  
`AECount=0 `  
`[AdvPull] `  
`APCheckTimer=0 `  
`APRadius=100 `  
`APMobMax=1 `  
`APScript=AdvPull `  
`APBefore= `  
`APAfter= `  
`[AdvCure] `  
`AQCount=0`

## Level 85

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=FALSE `  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoCures=FALSE `  
`DoPull=FALSE `  
`DoPet=FALSE `  
`DoSit=TRUE `  
`DoLoot=FALSE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`ForageIni=forage.ini `  
`DoAfk=FALSE `  
`DoMount=FALSE `  
`MountCast= `  
`DoAura=FALSE `  
`AuraCast= `  
`MasterList=${NetBots.Client} `  
`TankName=`  
`Radius=100 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Not now, thanks `  
`DeathSlot=FALSE `  
`NetworkINI= `  
`FollowDistance=20 `  
`FollowStick=20 hold uw `  
`PetCast= `  
`PetAggro=FALSE `  
`PetAssist=0 `  
`PetFoci= `  
`PetShrinkSpell= `  
`TraderName=`  
  
`[Melee] `  
`OffTank=FALSE`  
`ACLeash=50 `  
`ACAssistPct=200`  
`ACManaPct=40 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 taunt=1 stickrange=125 `  
`ACBefore= `  
`ACAfter=/stick 12 `  
  
`[AdvHeal] `  
`AHCount=0 `  
  
`[AdvDebuff] `  
`ADCount=4 `  
`ADMobMax=100`  
`ADCheckTime=2 `  
`ADAggroOnly=0 `  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff| `  
  
`ADGem1=6`  
`ADSpell1=Torrent of Fatigue `  
`ADSpellFoci1= `  
`ADDurMod1=0 `  
`ADSpellAlias1=strdebuff`  
`ADAnnounce1=/bc `  
`ADSpellMinMana1=10 `  
`ADSpellRecast1=0 `  
`ADSpellCastonResist1= `  
`ADSpellDelay1=0 `  
`ADTarCnt1=1 `  
`ADTarType1=1 `  
`ADTarBegHP1=100 `  
`ADTarEndHP1=40 `  
`ADIfSpellImmune1= `  
`ADUseHoTT1=0 `  
`ADPreCondition1=TRUE`  
  
`ADGem2=alt`  
`ADSpell2=Encroaching Darkness `  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2=snare `  
`ADAnnounce2=/bc `  
`ADSpellMinMana2=10 `  
`ADSpellRecast2=0 `  
`ADSpellCastonResist2= `  
`ADSpellDelay2=0 `  
`ADTarCnt2=1 `  
`ADTarType2=1 `  
`ADTarBegHP2=70 `  
`ADTarEndHP2=0 `  
`ADIfSpellImmune2= `  
`ADUseHoTT2=0 `  
`ADPreCondition2=TRUE`  
  
`ADGem3=7`  
`ADSpell3=Torrent of Pain `  
`ADSpellFoci3= `  
`ADDurMod3=0 `  
`ADSpellAlias3=acdebuff`  
`ADAnnounce3=/bc `  
`ADSpellMinMana3=10 `  
`ADSpellRecast3=0 `  
`ADSpellCastonResist3= `  
`ADSpellDelay3=0 `  
`ADTarCnt3=1 `  
`ADTarType3=1 `  
`ADTarBegHP3=95 `  
`ADTarEndHP3=30 `  
`ADIfSpellImmune3= `  
`ADUseHoTT3=0 `  
`ADPreCondition3=TRUE`  
  
`ADGem4=9`  
`ADSpell4=Bond of Laarthik`  
`ADSpellFoci4= `  
`ADDurMod4=0 `  
`ADSpellAlias4=bond `  
`ADAnnounce4=/bc `  
`ADSpellMinMana4=10 `  
`ADSpellRecast4=0 `  
`ADSpellCastonResist4= `  
`ADSpellDelay4=0 `  
`ADTarCnt4=1 `  
`ADTarTpe4=1 `  
`ADTarBegHP4=90 `  
`ADTarEndHP4=10 `  
`ADIfSpellImmune4= `  
`ADUseHoTT4=0 `  
`ADTarType4=0 `  
`ADPreCondition4=TRUE`  
  
`ADGem5=8`  
`ADSpell5=Torrent of Hate`  
`ADSpellFoci5= `  
`ADDurMod5=0 `  
`ADSpellAlias5=atkdebuff`  
`ADAnnounce5=/bc `  
`ADSpellMinMana5=10 `  
`ADSpellRecast5=0 `  
`ADSpellCastonResist5= `  
`ADSpellDelay5=0 `  
`ADTarCnt5=1 `  
`ADTarTpe5=1 `  
`ADTarBegHP5=90 `  
`ADTarEndHP5=10 `  
`ADIfSpellImmune5= `  
`ADUseHoTT5=0 `  
`ADTarType5=0 `  
`ADPreCondition5=TRUE`  
  
`[AdvBuff] `  
`ABCount=3`  
`ABMobMax=12 `  
`ABCheckTime=8 `  
`ABProactive=TRUE `  
  
`ABGem1=alt`  
`ABSpell1=Voice of Thule `  
`ABSpellFoci1= `  
`ABDurMod1=0 `  
`ABSpellAlias1=hatemod `  
`ABAnnounce1=/bc `  
`ABSpellMinMana1=10 `  
`ABTarType1=self `  
`ABTarCnt1=1`  
`ABTarType1=self`  
`ABRecast1=TRUE `  
`ABSpellIcon1=`  
  
`ABGem2=10`  
`ABSpell2=Drape of Korafax`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=drape`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=1`  
`ABTarType2=self`  
`ABRecast2=TRUE`  
`ABSpellIcon2=`  
  
`ABGem3=10`  
`ABSpell3=Shroud of the Blightborn`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=shroud`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=TRUE`  
`ABSpellIcon3=`  
  
`[AdvEvent] `  
`AECount=0 `  
  
`[AdvPull] `  
`APCheckTime=30 `  
`APRadius=100 `  
`APMobMax=15 `  
`APScript=Pull `  
`APPath= `  
`APRetPath= `  
`APRetPath1= `  
`APBefore= `  
`APAfter= `  
`APAnnounce=/bc Incoming -[ %t ]- `  
`APRetries=1 `  
  
`[AdvCure] `  
`AQCount=0`  
`AQCheckTime=8 `  
  
`[Script-Pull] `  
`Commands=1 `  
`C1=/echo Going to kill mobs `  
  
`[Script-PullCamp] `  
`Commands=5 `  
`C1=/docommand {If[{DoPull},/varset DoPull FALSE,/varset DoPull TRUE]} `  
`C2=/docommand {If[{DoPull},/varset DoMelee TRUE,/varset DoMelee FALSE]} `  
`C3=/docommand {If[{DoPull},/varset ACAssistPct 100,/varset ACAssistPct 95]} `  
`C4=/docommand {If[{DoPull},/mb makecamp,/mb follow]} `  
`C5=/echo DoPull-{DoPull} DoMelee-{DoMelee}`

## Level 100

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=FALSE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=FALSE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Abyssal Steed|alt`  
`MasterList=${NetBots.Client} `  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Minion of Grelleth|Gem12`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`PetShrink=TRUE`  
`PetShrinkSpell=Ring of the Ancients|item`  
`GoMNuke=Alias of debuff for GoM `  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=200`  
`ACManaPct=40`  
`ACAnnounce=`  
`ACMeleeCmd=/melee plugin=1 taunt=1 stickrange=125 provoke0=34687 challengefor=1 steely=1`  
`ACBefore=`  
`ACAfter=/stick 12 `  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=10`  
`ADMobMax=20`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=1`  
`ADSpell1=Repugnance`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=burst`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellCastonResist1=`  
`ADSpellDelay1=0`  
`ADTarCnt1=3`  
`ADTarType1=1`  
`ADTarBegHP1=99`  
`ADTarEndHP1=0`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=2`  
`ADSpell2=Terror of Poira`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=terror`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=0`  
`ADSpellCastonResist2=`  
`ADSpellDelay2=0`  
`ADTarCnt2=0`  
`ADTarType2=1`  
`ADTarBegHP2=99`  
`ADTarEndHP2=0`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=3`  
`ADSpell3=Demand for Power`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=power`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=0`  
`ADTarType3=1`  
`ADTarBegHP3=99`  
`ADTarEndHP3=0`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=4`  
`ADSpell4=Touch of Falsin`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=touch`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=99`  
`ADTarEndHP4=0`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=5`  
`ADSpell5=Bond of Ralstok`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=bond`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=99`  
`ADTarEndHP5=0`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=6`  
`ADSpell6=Ralstok's Bite`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=bite`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=99`  
`ADTarEndHP6=0`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=7`  
`ADSpell7=Blood of Ralstok`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=blood`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=1`  
`ADTarType7=1`  
`ADTarBegHP7=99`  
`ADTarEndHP7=0`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`ADGem8=8`  
`ADSpell8=Smoldering Darkness`  
`ADSpellFoci8=`  
`ADDurMod8=0`  
`ADSpellAlias8=snare`  
`ADAnnounce8=/bc`  
`ADSpellMinMana8=0`  
`ADSpellRecast8=0`  
`ADSpellCastonResist8=`  
`ADSpellDelay8=0`  
`ADTarCnt8=1`  
`ADTarType8=1`  
`ADTarBegHP8=99`  
`ADTarEndHP8=0`  
`ADIfSpellImmune8=`  
`ADUseHoTT8=0`  
`ADPreCondition8=TRUE`  
  
`ADGem9=9`  
`ADSpell9=Spear of Grelleth`  
`ADSpellFoci9=`  
`ADDurMod9=0`  
`ADSpellAlias9=spear`  
`ADAnnounce9=`  
`ADSpellMinMana9=0`  
`ADSpellRecast9=0`  
`ADSpellCastonResist9=`  
`ADSpellDelay9=0`  
`ADTarCnt9=1`  
`ADTarType9=1`  
`ADTarBegHP9=99`  
`ADTarEndHP9=0`  
`ADIfSpellImmune9=`  
`ADUseHoTT9=0`  
`ADPreCondition9=TRUE`  
  
`ADGem10=10`  
`ADSpell10=Dire Stricture`  
`ADSpellFoci10=`  
`ADDurMod10=0`  
`ADSpellAlias10=dire`  
`ADAnnounce10=`  
`ADSpellMinMana10=0`  
`ADSpellRecast10=0`  
`ADSpellCastonResist10=`  
`ADSpellDelay10=0`  
`ADTarCnt10=1`  
`ADTarType10=1`  
`ADTarBegHP10=99`  
`ADTarEndHP10=0`  
`ADIfSpellImmune10=`  
`ADUseHoTT10=0`  
`ADPreCondition10=TRUE`  
  
`[AdvBuff]`  
`ABCount=19`  
`ABMobMax=18`  
`ABCheckTime=8`  
  
`ABGem1=alt`  
`ABSpell1=Voice of Thule`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=hatemod`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=self`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
`ABPreCondition1=TRUE`  
  
`ABGem2=11`  
`ABSpell2=Drape of the Fallen`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=drape`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=1`  
`ABTarType2=self`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=11`  
`ABSpell3=Shroud of the Darksworn`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=shroud`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=11`  
`ABSpell4=Call of Gloomhaze`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=atk`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=11`  
`ABSpell5=Grelleth's Horror`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=proc1`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=self`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=12`  
`ABSpell6=Gift of Falsin`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=pethaste`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=1`  
`ABTarType6=mypet cbt idle`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=item`  
`ABSpell7=Stolen Traveler's Cloak`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=spikes`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=1`  
`ABTarType7=self`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=item`  
`ABSpell8=Archon Insignia Hoop`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=breath`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=0`  
`ABTarCnt8=1`  
`ABTarType8=self`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=item`  
`ABSpell9=Azure Stud of the Breeze`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=might`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=item`  
`ABSpell10=Face of Dread`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=end`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=0`  
`ABTarCnt10=1`  
`ABTarType10=self`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=item`  
`ABSpell11=Signet of Blood`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=def`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=0`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=item`  
`ABSpell12=Intricate Band of Petrified Wood`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=ihaste`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=1`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=item`  
`ABSpell13=Glowing Spaulders of Torture`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=dodge`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=0`  
`ABTarCnt13=1`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Wavecrasher's Raw-Hide Belt`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=mind`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=1`  
`ABTarType14=self`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`ABGem15=item`  
`ABSpell15=Erilon Soldier Bow`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=ward`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=1`  
`ABTarType15=self`  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
`ABPreCondition15=TRUE`  
  
`ABGem16=item`  
`ABSpell16=Ring of the Ancients`  
`ABSpellFoci16=`  
`ABDurMod16=0`  
`ABSpellAlias16=shrink`  
`ABAnnounce16=/bc`  
`ABSpellMinMana16=0`  
`ABTarCnt16=0`  
`ABTarType16=self`  
`ABRecast16=FALSE`  
`ABSpellIcon16=`  
`ABPreCondition16=TRUE`  
  
`ABGem17=11`  
`ABSpell17=Zombie Skin`  
`ABSpellFoci17=`  
`ABDurMod17=0`  
`ABSpellAlias17=selfds`  
`ABAnnounce17=/bc`  
`ABSpellMinMana17=0`  
`ABTarCnt17=1`  
`ABTarType17=self`  
`ABRecast17=FALSE`  
`ABSpellIcon17=`  
`ABPreCondition17=TRUE`  
  
`ABGem18=11`  
`ABSpell18=Grelleth's Skin`  
`ABSpellFoci18=`  
`ABDurMod18=0`  
`ABSpellAlias18=proc2`  
`ABAnnounce18=/bc`  
`ABSpellMinMana18=0`  
`ABTarCnt18=0`  
`ABTarType18=self`  
`ABRecast18=FALSE`  
`ABSpellIcon18=`  
`ABPreCondition18=TRUE`  
  
`ABGem19=item`  
`ABSpell19=Polymorph Wand: Dark Minotaur`  
`ABSpellFoci19=`  
`ABDurMod19=0`  
`ABSpellAlias19=illusion`  
`ABAnnounce19=/bc`  
`ABSpellMinMana19=0`  
`ABTarCnt19=0`  
`ABTarType19=self`  
`ABRecast19=FALSE`  
`ABSpellIcon19=`  
`ABPreCondition19=TRUE`  
  
`[AdvEvent]`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTime=30`  
`APRadius=100`  
`APMobMax=15`  
`APScript=Pull`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=/bc Incoming -[ %t ]- `  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-Pull] `  
`Commands=1 `  
`C1=/echo Going to kill mobs `  
  
`[Script-PullCamp] `  
`Commands=5 `  
`C1=/docommand {If[{DoPull},/varset DoPull FALSE,/varset DoPull TRUE]} `  
`C2=/docommand {If[{DoPull},/varset DoMelee TRUE,/varset DoMelee FALSE]} `  
`C3=/docommand {If[{DoPull},/varset ACAssistPct 100,/varset ACAssistPct 95]} `  
`C4=/docommand {If[{DoPull},/mb makecamp,/mb follow]} `  
`C5=/echo DoPull-{DoPull} DoMelee-{DoMelee}`

# Shaman

## Level 65

These settings are currently working on the Progression servers as of 7/2/2012.

    [Settings]
    DoMelee=FALSE
    DoHeals=TRUE
    DoBuffs=FALSE
    DoDebuffs=FALSE
    DoEvents=FALSE
    DoCures=FALSE
    DoPull=FALSE
    DoPet=TRUE
    DoSit=TRUE
    DoLoot=FALSE
    DoFW=FALSE
    DoForage=FALSE
    ForageIni=forage.ini
    DoAfk=FALSE
    DoMount=FALSE
    MountCast=Brown Rope Bridle|Item
    MasterList=${NetBots.Client}
    TankName=${Group.MainTank.Name}
    Radius=90
    SitAggroRadiusCheck=75
    AfkMessage=Not now, thanks
    DeathSlot=FALSE
    NetworkINI=
    TraderName=
    FollowDistance=20
    FollowStick=20 hold uw
    PetCast=
    PetAggro=FALSE
    PetAssist=97
    PetFoci=
    PetShrink=TRUE
    PetShrinkSpell=Tiny Companion
    [Melee]
    OffTank=FALSE
    ACLeash=50
    ACAssistPct=95
    ACManaPct=101
    ACAnnounce=
    ACMeleeCmd=/melee plugin=1
    ACBefore=
    ACAfter=
    [AdvHeal]
    AHCount=2
    AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk
    AHAllowDismount=False
    AHCheckTime=2
    AHHealOOBC=FALSE
    AHHealMode=0|0|12
    AHInterruptLevel=2

    AHGem1=7
    AHSpell1=Tnarg's Mending
    AHSpellFoci1=
    AHDurMod1=0
    AHSpellMinMana1=0
    AHSpellAlias1=tnarg
    AHAnnounce1=/bc
    AHTarCnt1=1
    AHClass1=pc hp50 war cle brd shm60 enc mag shd rng
    AHPreCondition1=TRUE

    AHGem2=8
    AHSpell2=Quiescence
    AHSpellFoci2=
    AHDurMod2=150
    AHSpellMinMana2=0
    AHSpellAlias2=qui
    AHAnnounce2=/bc
    AHTarCnt2=0
    AHClass2=pc pet hp50 war shd pal rng mnk rog brd bst ber shm60 clr70 dru wiz mag enc nec 
    AHPreCondition2=TRUE

    [AdvDebuff]
    ADCount=6
    ADMobMax=20
    ADCheckTime=2
    ADAggroOnly=0
    ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|

    ADGem1=1
    ADSpell1=Turgur's Insects
    ADSpellFoci1= 
    ADDurMod1=0
    ADSpellAlias1=slow 
    ADAnnounce1=
    ADSpellMinMana1=5
    ADSpellRecast1=3 
    ADSpellDelay1=3
    ADTarCnt1=1 
    ADTarType1=1 
    ADTarBegHP1=97
    ADTarEndHP1=50
    ADSpellCastonResist1=
    ADIfSpellImmune1=
    ADUseHoTT1=0
    ADPreCondition1=TRUE

    ADGem2=4
    ADSpell2=Cripple
    ADSpellFoci2= 
    ADDurMod2=0
    ADSpellAlias2=cripple
    ADAnnounce2=
    ADSpellMinMana2=30
    ADSpellRecast2=3 
    ADSpellDelay2=3
    ADTarCnt2=0 
    ADTarType2=1 
    ADTarBegHP2=95
    ADTarEndHP2=40
    ADSpellCastonResist2=
    ADIfSpellImmune2=
    ADUseHoTT2=0
    ADPreCondition2=TRUE

    ADGem3=5
    ADSpell3=Malos
    ADSpellFoci3= 
    ADDurMod3=0
    ADSpellAlias3=malo 
    ADAnnounce3=
    ADSpellMinMana3=0
    ADSpellRecast3=3 
    ADSpellDelay3=0
    ADTarCnt3=0
    ADTarType3=11 
    ADTarBegHP3=99
    ADTarEndHP3=0
    ADSpellCastonResist3=
    ADIfSpellImmune3=
    ADUseHoTT3=0
    ADPreCondition3=TRUE

    ADGem4=2
    ADSpell4=Velium Strike
    ADSpellFoci4= 
    ADDurMod4=0
    ADSpellAlias4=nuke
    ADAnnounce4=
    ADSpellMinMana4=30
    ADSpellRecast4=3
    ADSpellDelay4=0
    ADTarCnt4=1
    ADTarType4=1 
    ADTarBegHP4=70
    ADTarEndHP4=0
    ADSpellCastonResist4=
    ADIfSpellImmune4=
    ADUseHoTT4=0
    ADPreCondition4=TRUE

    ADGem5=4
    ADSpell5=Cloud of Grummus
    ADSpellFoci5= 
    ADDurMod5=0
    ADSpellAlias5=dslow 
    ADAnnounce5=
    ADSpellMinMana5=0
    ADSpellRecast5=10 
    ADSpellDelay5=0
    ADTarCnt5=0 
    ADTarType5=1 
    ADTarBegHP5=100
    ADTarEndHP5=0
    ADSpellCastonResist5=
    ADIfSpellImmune5=disdebuff
    ADUseHoTT5=0
    ADPreCondition5=TRUE

    ADGem6=5
    ADSpell6=Malicious Decay
    ADSpellFoci6= 
    ADDurMod6=0
    ADSpellAlias6=disdebuff
    ADAnnounce6=
    ADSpellMinMana6=0
    ADSpellRecast6=10 
    ADSpellDelay6=0
    ADTarCnt6=0 
    ADTarType6=1 
    ADTarBegHP6=100
    ADTarEndHP6=0
    ADSpellCastonResist6=
    ADIfSpellImmune6=
    ADUseHoTT6=0
    ADPreCondition6=TRUE

    [AdvBuff]
    ABCount=9
    ABMobMax=18
    ABCheckTime=8

    ABGem1=3
    ABSpell1=Spirit of the Puma
    ABSpellFoci1=
    ABDurMod1=150
    ABSpellAlias1=puma
    ABAnnounce1=
    ABSpellMinMana1=20
    ABTarCnt1=1
    ABTarType1=pc war rng brd rog mnk bst cbt
    ABRecast1=FALSE
    ABSpellIcon1=
    ABPreCondition1=TRUE

    ABGem2=5
    ABSpell2=Focus of the Seventh
    ABSpellFoci2=
    ABDurMod2=150
    ABSpellAlias2=gfocus
    ABAnnounce2=/bc
    ABSpellMinMana2=0
    ABTarCnt2=1
    ABTarType2=self grp
    ABRecast2=FALSE
    ABSpellIcon2=
    ABPreCondition2=TRUE

    ABGem3=4
    ABSpell3=Spirit of Bih`Li
    ABSpellFoci3=
    ABDurMod3=150
    ABSpellAlias3=sow
    ABAnnounce3=
    ABSpellMinMana3=0
    ABTarCnt3=1
    ABTarType3=self grp
    ABRecast3=FALSE
    ABSpellIcon3=
    ABPreCondition3=TRUE

    ABGem4=5
    ABSpell4=Talisman of the Brute
    ABSpellFoci4=
    ABDurMod4=150
    ABSpellAlias4=stam
    ABAnnounce4=/bc
    ABSpellMinMana4=0
    ABTarCnt4=1
    ABTarType4=self grp
    ABRecast4=FALSE
    ABSpellIcon4=
    ABPreCondition4=TRUE

    ABGem5=item
    ABSpell5=Distillate of Spirituality IX
    ABSpellFoci5=
    ABDurMod5=0
    ABSpellAlias5=potspir
    ABAnnounce5=
    ABSpellMinMana5=0
    ABTarCnt5=0
    ABTarType5=self
    ABRecast5=FALSE
    ABSpellIcon5=Elixir of Spiritualism IX
    ABPreCondition5=TRUE

    ABGem6=item
    ABSpell6=Scaled Avatar's Hauberk
    ABSpellFoci6=
    ABDurMod6=150
    ABSpellAlias6=swift
    ABAnnounce6=
    ABSpellMinMana6=0
    ABTarCnt6=1
    ABTarType6=tank mypet
    ABRecast6=FALSE
    ABSpellIcon6=Swift Like The Wind
    ABPreCondition6=TRUE

    ABGem7=item
    ABSpell7=Scaled Avatar's Hauberk
    ABSpellFoci7=
    ABDurMod7=150
    ABSpellAlias7=pswift
    ABAnnounce7=
    ABSpellMinMana7=0
    ABTarCnt7=1
    ABTarType7=pet
    ABRecast7=FALSE
    ABSpellIcon7=Swift Like The Wind
    ABPreCondition7=TRUE

    ABGem8=7
    ABSpell8=Focus of Soul
    ABSpellFoci8=
    ABDurMod8=150
    ABSpellAlias8=focus
    ABAnnounce8=/bc
    ABSpellMinMana8=0
    ABTarCnt8=0
    ABTarType8=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self
    ABRecast8=TRUE
    ABSpellIcon8=
    ABPreCondition8=TRUE

    ABGem9=6
    ABSpell9=True Spirit
    ABSpellFoci9=
    ABDurMod9=0
    ABSpellAlias9=pet
    ABAnnounce9=/bc
    ABSpellMinMana9=10
    ABTarCnt9=1
    ABTarType9=petspell
    ABRecast9=FALSE
    ABSpellIcon9=
    ABPreCondition9=TRUE


    [AdvEvent]
    AECustom1=
    AECustom2=
    AECustom3=
    AECount=2

    AEGem1=script
    AESpell1=FCanni
    AESpellFoci1= 
    AEDurMod1=0 
    AEDelay1=0
    AEEventMinMana1=1
    AEEventMinHP1=80
    AEMinMana1=1 
    AEMaxMana1=80
    AEMinHP1=80
    AEMaxHP1=100 
    AETarType1=self
    AESpellAlias1=canni5script
    AEAnnounce1=/bc
    AETarCnt1=1

    AEGem2=alt
    AESpell2=Cannibalization
    AESpellFoci2=
    AEDurMod2=0
    AEDelay2=0
    AEEventMinMana2=1
    AEEventMinHP2=75
    AEMinMana2=1
    AEMaxMana2=80
    AEMinHP2=73
    AEMaxHP2=100
    AETarType2=self
    AESpellAlias2=canni5
    AEAnnounce2=/bc
    AETarCnt2=0
    AECheckTime=8


    [AdvPull]
    APCheckTime=0
    APRadius=40
    APMobMax=1
    APScript=
    APPath=
    APRetPath=
    APBefore=
    APAfter=
    APAnnounce=
    APRetries=1
    [AdvCure]
    AQCount=0

    [Script-FCanni] 
    Commands=3
    C1=/if ({Me.PctHPs}<80 && !{Me.Song[Quiescence].ID} && !{Me.Casting.ID} && {Me.AltAbilityReady[Cannibalization]} && !{NetHeal[{Me.CleanName}].hot}) /multiline ; /target myself;/delay 2;/call MQ2Cast ''Quiescence'' gem8 3s CastCheck -targetid|{Me.ID};/netheal hot {Math.Calc[{Spell[Quiescence].Duration.TotalSeconds}*100]} {Me.CleanName}
    C2=/if (({Me.PctHPs}<80 && {NetHeal[{Me.CleanName}].hot} || {Me.PctHPs}>80) && {Cast.Ready[Cannibalization]}) /multiline ; /call MQ2Cast ''Cannibalization'' alt 3s CastCheck
    C3=/if ({Me.Casting.ID}=={Spell[Cannibalization].ID}) /delay 3s !{Me.Casting.ID}

## Level 78

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Collapsable Roboboar|item`  
`DoAura=FALSE`  
`AuraCast=`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Vegu's Faithful|gem9|sm`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`PetShrinkSpell=Tiny Companion|gem9`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=98`  
`ACManaPct=10`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
`[AdvHeal]`  
`AHCount=5`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
  
`AHGem1=7`  
`AHSpell1=Ahnkaul's Mending`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=heal`  
`AHAnnounce1=`  
`AHTarCnt1=1`  
`AHClass1=pc pet hp45 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem2=alt`  
`AHSpell2=Call of the Ancients`  
`AHSpellFoci2=`  
`AHDurMod2=15`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=grpsong`  
`AHAnnounce2=`  
`AHTarCnt2=3`  
`AHClass2=pc hp75 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem3=alt`  
`AHSpell3=Ancestral Aid`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=aid`  
`AHAnnounce3=`  
`AHTarCnt3=3`  
`AHClass3=pc group hp86 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`AHGem4=6`  
`AHSpell4=Halcyon Zephyr`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=`  
`AHAnnounce4=`  
`AHTarCnt4=1`  
`AHClass4=pc pet hp90 war shd pal rng mnk rog brd bst ber shm65 clr dru wiz mag enc nec `  
`AHAllowDismount=TRUE`  
`AHGem5=`  
`AHSpell5=`  
`AHSpellFoci5=`  
`AHDurMod5=0`  
`AHSpellMinMana5=0`  
`AHSpellAlias5=`  
`AHAnnounce5=`  
`AHTarCnt5=0`  
`AHClass5=pc pet group hp0 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec tnt mypet self`  
  
`[AdvDebuff]`  
`ADCount=7`  
`ADMobMax=20`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
  
`ADGem1=alt`  
`ADSpell1=Turgur's Swarm`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=slow`  
`ADAnnounce1=/bc Slowed << %t >> with [ %s ]`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellCastonResist1=malis`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=11`  
`ADTarBegHP1=200`  
`ADTarEndHP1=20`  
  
`ADGem2=alt`  
`ADSpell2=Turgur's Swarm`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=addslow`  
`ADAnnounce2=/bc Slowed %t with %s`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=2`  
`ADSpellCastonResist2=malis`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=2`  
`ADTarBegHP2=105`  
`ADTarEndHP2=20`  
  
`ADGem3=script`  
`ADSpell3=panthbuff`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=panther`  
`ADAnnounce3=`  
`ADSpellMinMana3=20`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=95`  
`ADTarEndHP3=20`  
  
`ADGem4=4`  
`ADSpell4=Juju`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=dot`  
`ADAnnounce4=`  
`ADSpellMinMana4=20`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=95`  
`ADTarEndHP4=20`  
  
`ADGem5=10`  
`ADSpell5=Vengeance of Ahnkaul`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=dot2`  
`ADAnnounce5=`  
`ADSpellMinMana5=15`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=0`  
`ADTarType5=1`  
`ADTarBegHP5=96`  
`ADTarEndHP5=20`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem6=3`  
`ADSpell6=Malis`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=malis`  
`ADAnnounce6=`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=0`  
`ADTarType6=0`  
`ADTarBegHP6=100`  
`ADTarEndHP6=0`  
  
`ADGem7=alt`  
`ADSpell7=Spirit Call`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=pups`  
`ADAnnounce7=`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=0`  
`ADTarType7=1`  
`ADTarBegHP7=97`  
`ADTarEndHP7=60`  
  
`ADIfSpellImmune1=`  
`ADIfSpellImmune2=`  
`ADIfSpellImmune3=`  
`ADIfSpellImmune4=`  
`ADIfSpellImmune5=`  
`ADIfSpellImmune6=`  
`ADIfSpellImmune7=`  
  
`[AdvBuff]`  
`ABCount=25`  
`ABMobMax=20`  
`ABCheckTime=0`  
`ABProactive=TRUE`  
  
`ABGem1=8`  
`ABSpell1=Talisman of the Panther`  
`ABSpellFoci1=`  
`ABDurMod1=120`  
`ABSpellAlias1=panther`  
`ABAnnounce1=`  
`ABSpellMinMana1=30`  
`ABTarCnt1=0`  
`ABTarType1=self cbt`  
`ABRecast1=FALSE`  
  
`ABGem2=5`  
`ABSpell2=champion`  
`ABSpellFoci2=`  
`ABDurMod2=50`  
`ABSpellAlias2=champ`  
`ABAnnounce2=`  
`ABSpellMinMana2=30`  
`ABTarCnt2=1`  
`ABTarType2=self cbt`  
`ABRecast2=FALSE`  
  
`ABGem3=9`  
`ABSpell3=Talisman of the Wrulan`  
`ABSpellFoci3=`  
`ABDurMod3=30`  
`ABSpellAlias3=grpwrulan`  
`ABAnnounce3=`  
`ABSpellMinMana3=10`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=FALSE`  
  
`ABGem4=9`  
`ABSpell4=Talisman of the Diaku`  
`ABSpellFoci4=`  
`ABDurMod4=30`  
`ABSpellAlias4=grpdiaku`  
`ABAnnounce4=`  
`ABSpellMinMana4=10`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=FALSE`  
  
`ABGem5=9`  
`ABSpell5=Preternatural Foresight`  
`ABSpellFoci5=`  
`ABDurMod5=30`  
`ABSpellAlias5=fore`  
`ABAnnounce5=`  
`ABSpellMinMana5=10`  
`ABTarCnt5=1`  
`ABTarType5=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast5=FALSE`  
  
`ABGem6=9`  
`ABSpell6=Strength of the Diaku`  
`ABSpellFoci6=`  
`ABDurMod6=30`  
`ABSpellAlias6=diaku`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=war shd pal clr rng mnk rog brd bst ber pet mypet`  
`ABRecast6=FALSE`  
  
`ABGem7=9`  
`ABSpell7=Spirit of Wolf`  
`ABSpellFoci7=`  
`ABDurMod7=30`  
`ABSpellAlias7=sow`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=self`  
`ABRecast7=TRUE`  
  
`ABGem8=9`  
`ABSpell8=Talisman of Vehemence`  
`ABSpellFoci8=`  
`ABDurMod8=30`  
`ABSpellAlias8=grpfort|grpsta|`  
`ABAnnounce8=`  
`ABSpellMinMana8=10`  
`ABTarCnt8=1`  
`ABTarType8=self`  
`ABRecast8=FALSE`  
  
`ABGem9=9`  
`` ABSpell9=Spirit of Bih`Li ``  
`ABSpellFoci9=`  
`ABDurMod9=30`  
`ABSpellAlias9=grpsow`  
`ABAnnounce9=`  
`ABSpellMinMana9=0`  
`ABTarCnt9=0`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
  
`ABGem10=9`  
`ABSpell10=Talisman of the Tribunal`  
`ABSpellFoci10=`  
`ABDurMod10=30`  
`ABSpellAlias10=tot`  
`ABAnnounce10=`  
`ABSpellMinMana10=80`  
`ABTarCnt10=1`  
`ABTarType10=self`  
`ABRecast10=FALSE`  
  
`ABGem11=9`  
`ABSpell11=Talisman of Wunshi`  
`ABSpellFoci11=`  
`ABDurMod11=30`  
`ABSpellAlias11=grpwunshi`  
`ABAnnounce11=`  
`ABSpellMinMana11=11`  
`ABTarCnt11=0`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
  
`ABGem12=9`  
`ABSpell12=Wunshi's Focusing`  
`ABSpellFoci12=`  
`ABDurMod12=30`  
`ABSpellAlias12=wunshi`  
`ABAnnounce12=`  
`ABSpellMinMana12=10`  
`ABTarCnt12=0`  
`ABTarType12=mypet`  
`ABRecast12=TRUE`  
  
`ABGem13=9`  
`ABSpell13=Spirit of Perseverance`  
`ABSpellFoci13=`  
`ABDurMod13=30`  
`ABSpellAlias13=regen`  
`ABAnnounce13=`  
`ABSpellMinMana13=10`  
`ABTarCnt13=0`  
`ABTarType13=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast13=TRUE`  
  
`ABGem14=9`  
`ABSpell14=Focus of Soul`  
`ABSpellFoci14=`  
`ABDurMod14=30`  
`ABSpellAlias14=focus`  
`ABAnnounce14=`  
`ABSpellMinMana14=0`  
`ABTarCnt14=0`  
`ABTarType14=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast14=TRUE`  
  
`ABGem15=9`  
`ABSpell15=Endurance of the Boar`  
`ABSpellFoci15=`  
`ABDurMod15=30`  
`ABSpellAlias15=boar`  
`ABAnnounce15=`  
`ABSpellMinMana15=0`  
`ABTarCnt15=0`  
`ABTarType15=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast15=TRUE`  
  
`ABGem16=9`  
`ABSpell16=Spirit of Fortitude`  
`ABSpellFoci16=`  
`ABDurMod16=30`  
`ABSpellAlias16=fort`  
`ABAnnounce16=`  
`ABSpellMinMana16=0`  
`ABTarCnt16=0`  
`ABTarType16=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast16=TRUE`  
  
`ABGem17=9`  
`ABSpell17=Spirit of Might`  
`ABSpellFoci17=`  
`ABDurMod17=30`  
`ABSpellAlias17=might`  
`ABAnnounce17=`  
`ABSpellMinMana17=0`  
`ABTarCnt17=0`  
`ABTarType17=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast17=TRUE`  
  
`ABGem18=9`  
`ABSpell18=Agility of the Wrulan`  
`ABSpellFoci18=`  
`ABDurMod18=30`  
`ABSpellAlias18=wrulan`  
`ABAnnounce18=`  
`ABSpellMinMana18=0`  
`ABTarCnt18=0`  
`ABTarType18=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast18=TRUE`  
  
`ABGem19=9`  
`ABSpell19=Spirit of Sense`  
`ABSpellFoci19=`  
`ABDurMod19=30`  
`ABSpellAlias19=sense`  
`ABAnnounce19=`  
`ABSpellMinMana19=0`  
`ABTarCnt19=0`  
`ABTarType19=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast19=TRUE`  
  
`ABGem20=9`  
`ABSpell20=Bloodworg Focusing`  
`ABSpellFoci20=`  
`ABDurMod20=30`  
`ABSpellAlias20=dire|Bloodworg|worg|`  
`ABAnnounce20=`  
`ABSpellMinMana20=5`  
`ABTarCnt20=1`  
`ABTarType20=war shd pal rng mnk rog brd bst ber shm dru wiz mag enc nec mypet pet cbt idle`  
`ABRecast20=FALSE`  
  
`ABGem21=10`  
`ABSpell21=Lassitude`  
`ABSpellFoci21=`  
`ABDurMod21=1250`  
`ABSpellAlias21=lassitude`  
`ABAnnounce21=`  
`ABSpellMinMana21=20`  
`ABTarCnt21=1`  
`ABTarType21=war shd pal rng grp`  
`ABRecast21=FALSE`  
  
`ABGem22=9`  
`ABSpell22=Talisman of the Stoic One`  
`ABSpellFoci22=`  
`ABDurMod22=0`  
`ABSpellAlias22=grpregen`  
`ABAnnounce22=`  
`ABSpellMinMana22=0`  
`ABTarCnt22=1`  
`ABTarType22=self`  
`ABRecast22=FALSE`  
  
`ABGem23=9`  
`ABSpell23=Tiny Terror`  
`ABSpellFoci23=`  
`ABDurMod23=0`  
`ABSpellAlias23=shrink`  
`ABAnnounce23=`  
`ABSpellMinMana23=0`  
`ABTarCnt23=0`  
`ABTarType23=self`  
`ABRecast23=FALSE`  
  
`ABGem24=10`  
`ABSpell24=Levitation`  
`ABSpellFoci24=`  
`ABDurMod24=0`  
`ABSpellAlias24=levi`  
`ABAnnounce24=`  
`ABSpellMinMana24=0`  
`ABTarCnt24=0`  
`ABTarType24=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec grp cbt idle`  
`ABRecast24=TRUE`  
  
`ABGem25=`  
`ABSpell25=`  
`ABSpellFoci25=`  
`ABDurMod25=0`  
`ABSpellAlias25=`  
`ABAnnounce25=`  
`ABSpellMinMana25=0`  
`ABTarCnt25=0`  
`ABTarType25=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast25=FALSE`  
  
  
  
`[AdvEvent]`  
`AECount=3`  
`AECheckTime=0`  
  
`AEGem1=1`  
`AESpell1=Ancestral Hearkening`  
`AESpellFoci1= `  
`AEDurMod1=0 `  
`AEDelay1=0 `  
`AEEventMinMana1=1 `  
`AEEventMinHP1=60`  
`AEMinMana1=1 `  
`AEMaxMana1=85`  
`AEMinHP1=60`  
`AEMaxHP1=100 `  
`AETarType1=self cbt idle`  
`AESpellAlias1=canni `  
`AEAnnounce1=/bc`  
`AETarCnt1=1`  
  
`AEGem2=script`  
`AESpell2=FCanni`  
`AESpellFoci2= `  
`AEDurMod2=0 `  
`AEDelay2=0`  
`AEEventMinMana2=1`  
`AEEventMinHP2=80`  
`AEMinMana2=1 `  
`AEMaxMana2=80`  
`AEMinHP2=80`  
`AEMaxHP2=100 `  
`AETarType2=self`  
`AESpellAlias2=canni5script`  
`AEAnnounce2=`  
`AETarCnt2=1`  
  
`AEGem3=alt`  
`AESpell3=Cannibalization`  
`AESpellFoci3=`  
`AEDurMod3=0`  
`AEDelay3=0`  
`AEEventMinMana3=1`  
`AEEventMinHP3=75`  
`AEMinMana3=1`  
`AEMaxMana3=80`  
`AEMinHP3=73`  
`AEMaxHP3=100`  
`AETarType3=self`  
`AESpellAlias3=canni5`  
`AEAnnounce3=`  
`AETarCnt3=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
`[AdvCure]`  
`AQCount=0`  
  
  
`[Script-Canni] `  
`Commands=3`  
`C1=/if (!{Me.Gem[Ancestral Hearkening]}) /memorize ''Ancestral Hearkening|gem1''`  
`C2=/if ({Cast.Ready} && !{Cast.Ready[Ancestral Hearkening|gem1]}) /delay 1s {Cast.Ready[Ancestral Hearkening|gem1]}`  
`C3=/if (({Me.CombatState.NotEqual[Resting]} || {Me.Mount.ID}) && !{Me.Moving} && {Cast.Ready[Ancestral Hearkening|gem1]}) /multiline ; /echo casting;/call MQ2Cast ''Ancestral Hearkening'' gem1 3s AHHealCheck`  
  
`[Script-panthbuff] `  
`Commands=5`  
`C1=/if ({Me.Buff[Talisman of the Panther].ID} || {Me.PctMana}<30) /return`  
`C2=/if (!{Me.Gem[Talisman of the Panther]}) /memorize ''Talisman of the Panther|gem8''`  
`C3=/if ({Me.Casting.ID}) /delay {Math.Calc[({Cast.Timing}/100)+1]}s {Cast.Ready}`  
`C4=/if ({Cast.Ready} && !{Cast.Ready[Talisman of the Panther]}) /return`  
`C5=/call Mq2Cast ''Talisman of the Panther'' gem8 4s CastCheck`  
  
`[Script-FCanni] `  
`Commands=3`  
`C1=/if ({Me.PctHPs}<80 && !{Me.Song[Halcyon Zephyr].ID} && !{Me.Casting.ID} && {Me.AltAbilityReady[Cannibalization]} && !{NetHeal[{Me.CleanName}].hot}) /multiline ; /target myself;/delay 2;/call MQ2Cast ''Halcyon Zephyr'' gem7 3s CastCheck -targetid|{Me.ID};/netheal hot {Math.Calc[{Spell[Halcyon Zephyr].Duration.TotalSeconds}*100]} {Me.CleanName}`  
`C2=/if (({Me.PctHPs}<80 && {NetHeal[{Me.CleanName}].hot} || {Me.PctHPs}>80) && {Cast.Ready[Cannibalization]}) /multiline ; /call MQ2Cast ''Cannibalization'' alt 3s CastCheck`  
`C3=/if ({Me.Casting.ID}=={Spell[Cannibalization].ID}) /delay 3s !{Me.Casting.ID}`

## Level 85

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=`  
`DoAura=FALSE`  
`AuraCast=`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Aina's Faithful|gem10|smii`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`PetShrinkSpell=Tiny Companion|gem10`  
`NetworkINI=`  
`TraderName=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=10`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/pet qattack`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=4`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHAllowDismount=TRUE`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
  
`AHGem1=7`  
`AHSpell1=Dannal's Mending`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=heal`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc pet hp45 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition1=TRUE`  
  
`AHGem2=alt`  
`AHSpell2=Call of the Ancients`  
`AHSpellFoci2=`  
`AHDurMod2=15`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=grpsong`  
`AHAnnounce2=/bc`  
`AHTarCnt2=3`  
`AHClass2=pc hp75 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition2=TRUE`  
  
`AHGem3=alt`  
`AHSpell3=Ancestral Aid`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=aid`  
`AHAnnounce3=/bc`  
`AHTarCnt3=3`  
`AHClass3=pc group hp86 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition3=TRUE`  
  
`AHGem4=6`  
`AHSpell4=Halcyon Whisper`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=`  
`AHAnnounce4=/bc`  
`AHTarCnt4=1`  
`AHClass4=pc pet hp90 war shd pal rng mnk rog brd bst ber shm65 clr dru wiz mag enc nec `  
`AHPreCondition4=TRUE`  
  
`[AdvDebuff]`  
`ADCount=6`  
`ADMobMax=100`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=alt`  
`ADSpell1=Turgur's Swarm`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=slow`  
`ADAnnounce1=/bc Slowed << %t >> with [ %s ]`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellCastonResist1=malis`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=11`  
`ADTarBegHP1=200`  
`ADTarEndHP1=20`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=alt`  
`ADSpell2=Turgur's Swarm`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=addslow`  
`ADAnnounce2=/bc Slowed %t with %s`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=2`  
`ADSpellCastonResist2=malis`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=2`  
`ADTarBegHP2=200`  
`ADTarEndHP2=20`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=8 `  
`ADSpell3=Talisman of the Panther`  
`ADSpellFoci3=/bc`  
`ADDurMod3=0`  
`ADSpellAlias3=panther`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=20`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=95`  
`ADTarEndHP3=20`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=4`  
`ADSpell4=Mojo`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=dot`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=20`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=95`  
`ADTarEndHP4=20`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=10`  
`ADSpell5=BLood of Jaled'Dar`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=dot2`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=15`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=95`  
`ADTarEndHP5=20`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=3`  
`ADSpell6=Malosenea Rk. II`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=malis`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=100`  
`ADTarEndHP6=0`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=alt`  
`ADSpell7=Spirit Call`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=pups`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=0`  
`ADTarType7=1`  
`ADTarBegHP7=97`  
`ADTarEndHP7=60`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`[AdvBuff]`  
`ABCount=25`  
`ABMobMax=20`  
`ABCheckTime=0`  
`ABProactive=TRUE`  
  
`ABGem1=8`  
`ABSpell1=Talisman of the Cougar`  
`ABSpellFoci1=`  
`ABDurMod1=120`  
`ABSpellAlias1=cougar`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=30`  
`ABTarCnt1=0`  
`ABTarType1=self cbt`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
  
`ABGem2=5`  
`ABSpell2=Champion`  
`ABSpellFoci2=`  
`ABDurMod2=50`  
`ABSpellAlias2=champ`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=30`  
`ABTarCnt2=1`  
`ABTarType2=self cbt`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
  
`ABGem3=9`  
`ABSpell3=Talisman of the Wrulan`  
`ABSpellFoci3=`  
`ABDurMod3=30`  
`ABSpellAlias3=grpwrulan`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=10`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
  
`ABGem4=9`  
`ABSpell4=Talisman of the Diaku`  
`ABSpellFoci4=`  
`ABDurMod4=30`  
`ABSpellAlias4=grpdiaku`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=10`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
  
`ABGem5=9`  
`ABSpell5=Talisman of Unity`  
`ABSpellFoci5=`  
`ABDurMod5=30`  
`ABSpellAlias5=grpunity`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=10`  
`ABTarCnt5=1`  
`ABTarType5=self`  
`ABRecast5=FALSE`  
`ABSpellIcon5=Mammoth's Strength`  
  
`ABGem6=9`  
`ABSpell6=Strength of the Diaku`  
`ABSpellFoci6=`  
`ABDurMod6=30`  
`ABSpellAlias6=diaku`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=war shd pal clr rng mnk rog brd bst ber pet mypet`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
  
`ABGem7=9`  
`ABSpell7=Spirit of Wolf`  
`ABSpellFoci7=`  
`ABDurMod7=30`  
`ABSpellAlias7=sow`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=self`  
`ABRecast7=TRUE`  
`ABSpellIcon7=`  
  
`ABGem8=9`  
`ABSpell8=Talisman of Vehemence`  
`ABSpellFoci8=`  
`ABDurMod8=30`  
`ABSpellAlias8=grpfort|grpsta|`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=10`  
`ABTarCnt8=0`  
`ABTarType8=self`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
  
`ABGem9=9`  
`` ABSpell9=Spirit of Bih`Li ``  
`ABSpellFoci9=`  
`ABDurMod9=30`  
`ABSpellAlias9=grpsow`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=0`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
  
`ABGem10=9`  
`ABSpell10=Talisman of the Tribunal`  
`ABSpellFoci10=`  
`ABDurMod10=30`  
`ABSpellAlias10=tot`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=80`  
`ABTarCnt10=0`  
`ABTarType10=self`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
  
`ABGem11=9`  
`ABSpell11=Talisman of the Bloodworg`  
`ABSpellFoci11=`  
`ABDurMod11=30`  
`ABSpellAlias11=grpworg`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=11`  
`ABTarCnt11=0`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
  
`ABGem12=9`  
`ABSpell12=Bloodworg Focusing Rk. II`  
`ABSpellFoci12=`  
`ABDurMod12=30`  
`ABSpellAlias12=dire|Bloodworg|worg|`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=5`  
`ABTarCnt12=0`  
`ABTarType12=war shd pal rng mnk rog brd bst ber shm dru wiz mag enc nec mypet pet cbt idle`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
  
`ABGem13=9`  
`ABSpell13=Spirit of the Resolute`  
`ABSpellFoci13=`  
`ABDurMod13=30`  
`ABSpellAlias13=regen`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=10`  
`ABTarCnt13=0`  
`ABTarType13=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast13=TRUE`  
`ABSpellIcon13=`  
  
`ABGem14=9`  
`ABSpell14=Focus of Soul`  
`ABSpellFoci14=`  
`ABDurMod14=30`  
`ABSpellAlias14=focus`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=0`  
`ABTarType14=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast14=TRUE`  
`ABSpellIcon14=`  
  
`ABGem15=9`  
`ABSpell15=Endurance of the Boar`  
`ABSpellFoci15=`  
`ABDurMod15=30`  
`ABSpellAlias15=boar`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=0`  
`ABTarType15=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast15=TRUE`  
`ABSpellIcon15=`  
  
`ABGem16=9`  
`ABSpell16=Unity of the Spirits`  
`ABSpellFoci16=`  
`ABDurMod16=30`  
`ABSpellAlias16=unity`  
`ABAnnounce16=/bc`  
`ABSpellMinMana16=0`  
`ABTarCnt16=0`  
`ABTarType16=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast16=TRUE`  
`ABSpellIcon16=`  
  
`ABGem17=9`  
`ABSpell17=Spirit of Might`  
`ABSpellFoci17=`  
`ABDurMod17=30`  
`ABSpellAlias17=might`  
`ABAnnounce17=/bc`  
`ABSpellMinMana17=0`  
`ABTarCnt17=0`  
`ABTarType17=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast17=TRUE`  
`ABSpellIcon17=`  
  
`ABGem18=9`  
`ABSpell18=Agility of the Wrulan`  
`ABSpellFoci18=`  
`ABDurMod18=30`  
`ABSpellAlias18=wrulan`  
`ABAnnounce18=/bc`  
`ABSpellMinMana18=0`  
`ABTarCnt18=0`  
`ABTarType18=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast18=TRUE`  
`ABSpellIcon18=`  
  
`ABGem19=9`  
`ABSpell19=Spirit of Sense`  
`ABSpellFoci19=`  
`ABDurMod19=30`  
`ABSpellAlias19=sense`  
`ABAnnounce19=/bc`  
`ABSpellMinMana19=0`  
`ABTarCnt19=0`  
`ABTarType19=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast19=TRUE`  
`ABSpellIcon19=`  
  
`ABGem20=10`  
`ABSpell20=Lassitude`  
`ABSpellFoci20=`  
`ABDurMod20=1250`  
`ABSpellAlias20=lassitude`  
`ABAnnounce20=/bc`  
`ABSpellMinMana20=20`  
`ABTarCnt20=0`  
`ABTarType20=war shd pal rng grp`  
`ABRecast20=FALSE`  
`ABSpellIcon20=`  
  
`ABGem21=9`  
`ABSpell21=Talisman of the Resolute`  
`ABSpellFoci21=`  
`ABDurMod21=0`  
`ABSpellAlias21=grpregen`  
`ABAnnounce21=/bc`  
`ABSpellMinMana21=0`  
`ABTarCnt21=1`  
`ABTarType21=self`  
`ABRecast21=FALSE`  
`ABSpellIcon21=`  
  
`ABGem22=9`  
`ABSpell22=Tiny Terror`  
`ABSpellFoci22=`  
`ABDurMod22=0`  
`ABSpellAlias22=shrink`  
`ABAnnounce22=/bc`  
`ABSpellMinMana22=0`  
`ABTarCnt22=0`  
`ABTarType22=self`  
`ABRecast22=FALSE`  
`ABSpellIcon22=`  
  
`ABGem23=10`  
`ABSpell23=Swift Like the Wind`  
`ABSpellFoci23=`  
`ABDurMod23=0`  
`ABSpellAlias23=haste`  
`ABAnnounce23=/bc`  
`ABSpellMinMana23=0`  
`ABTarCnt23=1`  
`ABTarType23=war shd pal rng mnk rog brd bst ber shm pet mypet cbt idle`  
`ABRecast23=TRUE`  
`ABSpellIcon23=`  
  
`ABGem24=script`  
`ABSpell24=summfavor`  
`ABSpellFoci24=`  
`ABDurMod24=0`  
`ABSpellAlias24=`  
`ABAnnounce24=/bc`  
`ABSpellMinMana24=20`  
`ABTarCnt24=1`  
`ABTarType24=self`  
`ABRecast24=FALSE`  
`ABSpellIcon24=`  
  
`ABGem25=item`  
`ABSpell25=Wishka's Favor Trinket`  
`ABSpellFoci25=`  
`ABDurMod25=0`  
`ABSpellAlias25=favor`  
`ABAnnounce25=/bc`  
`ABSpellMinMana25=20`  
`ABTarCnt25=4`  
`ABTarType25=self`  
`ABRecast25=FALSE`  
`ABSpellIcon25=`  
  
`[AdvEvent]`  
`AECount=3`  
`AECheckTime=0`  
  
`AEGem1=1`  
`AESpell1=Ancestral Obligation`  
`AESpellFoci1= `  
`AEDurMod1=0 `  
`AEDelay1=0 `  
`AEEventMinMana1=1 `  
`AEEventMinHP1=60`  
`AEMinMana1=1 `  
`AEMaxMana1=85`  
`AEMinHP1=60`  
`AEMaxHP1=100 `  
`AETarType1=self cbt idle`  
`AESpellAlias1=canni `  
`AEAnnounce1=/bc`  
`AETarCnt1=1`  
  
`AEGem2=script`  
`AESpell2=FCanni`  
`AESpellFoci2= `  
`AEDurMod2=0 `  
`AEDelay2=0`  
`AEEventMinMana2=1`  
`AEEventMinHP2=80`  
`AEMinMana2=1 `  
`AEMaxMana2=80`  
`AEMinHP2=80`  
`AEMaxHP2=100 `  
`AETarType2=self`  
`AESpellAlias2=canni5script`  
`AEAnnounce2=/bc`  
`AETarCnt2=1`  
  
`AEGem3=alt`  
`AESpell3=Cannibalization`  
`AESpellFoci3=`  
`AEDurMod3=0`  
`AEDelay3=0`  
`AEEventMinMana3=1`  
`AEEventMinHP3=75`  
`AEMinMana3=1`  
`AEMaxMana3=80`  
`AEMinHP3=73`  
`AEMaxHP3=100`  
`AETarType3=self`  
`AESpellAlias3=canni5`  
`AEAnnounce3=/bc`  
`AETarCnt3=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-FCanni] `  
`Commands=3`  
`C1=/if ({Me.PctHPs}<80 && !{Me.Song[Halcyon Whisper].ID} && !{Me.Casting.ID} && {Me.AltAbilityReady[Cannibalization]} && !{NetHeal[{Me.CleanName}].hot}) /multiline ; /target myself;/delay 2;/call MQ2Cast ''Halcyon Whisper'' gem6 3s CastCheck -targetid|{Me.ID};/netheal hot {Math.Calc[{Spell[Halcyon Whisper].Duration.TotalSeconds}*100]} {Me.CleanName}`  
`C2=/if (({Me.PctHPs}<80 && {NetHeal[{Me.CleanName}].hot} || {Me.PctHPs}>80) && {Cast.Ready[Cannibalization]}) /multiline ; /call MQ2Cast ''Cannibalization'' alt 3s CastCheck`  
`C3=/if ({Me.Casting.ID}=={Spell[Cannibalization].ID}) /delay 3s !{Me.Casting.ID}`  
  
`[Script-summfavor]`  
`Commands=3`  
`C1=/if (!{FindItemCount[Wishka's Favor Trinket]}) /casting ''Wishka's Favor|gem9''`  
`C2=/if (!{FindItemCount[Wishka's Favor Trinket]}) /delay 1s {Me.Casting.ID}`  
`C3=/if (!{FindItemCount[Wishka's Favor Trinket]}) /delay 7s !{Me.Casting.ID}`  

## Level 100

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=TRUE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Ornate Barding|item`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`Radius=75`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Kriegas' Faithful|gem12|smii`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`PetShrink=TRUE`  
`PetShrinkSpell=Ring of the Ancients|item`  
`GoMNuke=Alias of debuff for GoM `  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=98`  
`ACManaPct=10`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/pet qattack`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=5`  
`AHCheckTime=4`  
`AHHealOOBC=FALSE`  
`AHHealMode=1|1|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`AHGem1=8`  
`AHSpell1=Blezon's Mending`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=heal`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc pet group hp45 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition1=TRUE`  
  
`AHGem2=alt`  
`AHSpell2=Call of the Ancients`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=grpsong`  
`AHAnnounce2=/bc`  
`AHTarCnt2=3`  
`AHClass2=ppc pet group hp75 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition2=TRUE`  
  
`AHGem3=alt`  
`AHSpell3=Ancestral Aid`  
`AHSpellFoci3=`  
`AHDurMod3=0`  
`AHSpellMinMana3=0`  
`AHSpellAlias3=aid`  
`AHAnnounce3=/bc`  
`AHTarCnt3=3`  
`AHClass3=pc pet group hp86 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition3=TRUE`  
  
`AHGem4=7`  
`AHSpell4=Halcyon Shear`  
`AHSpellFoci4=`  
`AHDurMod4=0`  
`AHSpellMinMana4=0`  
`AHSpellAlias4=halcyon`  
`AHAnnounce4=/bc`  
`AHTarCnt4=1`  
`AHClass4=pc pet group hp90 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition4=TRUE`  
  
`AHGem5=9`  
`AHSpell5=Antecessor's Intervention`  
`AHSpellFoci5=`  
`AHDurMod5=0`  
`AHSpellMinMana5=0`  
`AHSpellAlias5=grpheal`  
`AHAnnounce5=/bc`  
`AHTarCnt5=3`  
`AHClass5=pc pet group hp86 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHPreCondition5=TRUE`  
  
`[AdvDebuff]`  
`ADCount=7`  
`ADMobMax=100`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=2`  
`ADSpell1=Crippling Counterbias`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=slow`  
`ADAnnounce1=/bc Slowed << %t >> with [ %s ]`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellCastonResist1=slow`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=11`  
`ADTarBegHP1=200`  
`ADTarEndHP1=20`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=alt`  
`ADSpell2=Turgur's Swarm`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=addslow`  
`ADAnnounce2=/bc Slowed %t with %s`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=1`  
`ADSpellCastonResist2=addslow`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=12`  
`ADTarBegHP2=200`  
`ADTarEndHP2=20`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=3`  
`ADSpell3=Falhotep's Malosenia`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=malo`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=0`  
`ADTarType3=1`  
`ADTarBegHP3=100`  
`ADTarEndHP3=0`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=4`  
`ADSpell4=Nectar of Anguish`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=poisondot`  
`ADAnnounce5=/bc`  
`ADSpellMinMana4=15`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=98`  
`ADTarEndHP4=20`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=5`  
`ADSpell5=Vilefeaster's Pandemic`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=diseasedot`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=15`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=98`  
`ADTarEndHP5=20`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=6`  
`ADSpell6=Enalam's Curse`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=cursedot`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=15`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=98`  
`ADTarEndHP6=20`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=alt`  
`ADSpell7=Spirit Call`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=pups`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=0`  
`ADTarType7=1`  
`ADTarBegHP7=98`  
`ADTarEndHP7=60`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
`ADAnnounce4=`  
  
`[AdvBuff]`  
`ABCount=22`  
`ABMobMax=100`  
`ABCheckTime=8`  
  
`ABGem1=12`  
`ABSpell1=Talisman of the Courageous`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=gunity`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=10`  
`ABTarCnt1=3`  
`ABTarType1=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast1=FALSE`  
`ABSpellIcon1=Insistent Focusing`  
`ABPreCondition1=TRUE`  
  
`ABGem2=12`  
`ABSpell2=Unity of the Courageous`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=unity`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=10`  
`ABTarCnt2=1`  
`ABTarType2=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast2=FALSE`  
`ABSpellIcon2=Insistent Focusing`  
`ABPreCondition2=TRUE`  
  
`ABGem3=12`  
`ABSpell3=Talisman of the Steadfast`  
`ABSpellFoci3=grpregen`  
`ABDurMod3=0`  
`ABSpellAlias3=grpregen`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=10`  
`ABTarCnt3=3`  
`ABTarType3=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=12`  
`ABSpell4=Spirit of the Indomitable`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=regen`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=10`  
`ABTarCnt4=1`  
`ABTarType4=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=12`  
`ABSpell5=Talisman of the Wrulan`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=grpwrulan`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=10`  
`ABTarCnt5=3`  
`ABTarType5=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=12`  
`ABSpell6=Talisman of the Diaku`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=grpdiaku`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=10`  
`ABTarCnt6=3`  
`ABTarType6=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec mypet pet`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=12`  
`ABSpell7=Swift Like the Wind`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=haste`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=10`  
`ABTarCnt7=1`  
`ABTarType7=war shd pal rng mnk rog brd bst ber shm cbt idle`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=10`  
`ABSpell8=Fatigue`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=Fatigue`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=10`  
`ABTarCnt8=1`  
`ABTarType8=war shd pal rng grp cbt`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=script`  
`ABSpell9=summfavor`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=summfavor`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=20`  
`ABTarCnt9=1`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=11`  
`ABSpell10=Rampant Growth`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=growth`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=20`  
`ABTarCnt10=1`  
`ABTarType10=tank idle cbt`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=item`  
`ABSpell11=Perorate Cloak of the Word Lord`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=spikes`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=1`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=item`  
`ABSpell12=Double Hoop of Tegleth`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=geo`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=0`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=item`  
`ABSpell13=Earring of Soothing Melodies`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=petshrink`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=0`  
`ABTarCnt13=0`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Face of Dread`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=end`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=1`  
`ABTarType14=self`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`ABGem15=item`  
`ABSpell15=Brilliant Band of Arcane Knowledge`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=past1`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=0`  
`ABTarType15=self`  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
`ABPreCondition15=TRUE`  
  
`ABGem16=item`  
`ABSpell16=Signet of the Record Master`  
`ABSpellFoci16=`  
`ABDurMod16=0`  
`ABSpellAlias16=past2`  
`ABAnnounce16=/bc`  
`ABSpellMinMana16=0`  
`ABTarCnt16=1`  
`ABTarType16=self`  
`ABRecast16=FALSE`  
`ABSpellIcon16=`  
`ABPreCondition16=TRUE`  
  
`ABGem17=item`  
`ABSpell17=Featherweight Drape of Harmony`  
`ABSpellFoci17=`  
`ABDurMod17=0`  
`ABSpellAlias17=dodge`  
`ABAnnounce17=/bc`  
`ABSpellMinMana17=0`  
`ABTarCnt17=1`  
`ABTarType17=self`  
`ABRecast17=FALSE`  
`ABSpellIcon17=`  
`ABPreCondition17=TRUE`  
  
`ABGem18=item`  
`ABSpell18=Burning Belt of Endless Shadow`  
`ABSpellFoci18=`  
`ABDurMod18=0`  
`ABSpellAlias18=mind`  
`ABAnnounce18=/bc`  
`ABSpellMinMana18=0`  
`ABTarCnt18=1`  
`ABTarType18=self`  
`ABRecast18=FALSE`  
`ABSpellIcon18=`  
`ABPreCondition18=TRUE`  
  
`ABGem19=item`  
`ABSpell19=Ancient Alaran Manuscript`  
`ABSpellFoci19=`  
`ABDurMod19=0`  
`ABSpellAlias19=ward`  
`ABAnnounce19=/bc`  
`ABSpellMinMana19=0`  
`ABTarCnt19=1`  
`ABTarType19=self`  
`ABRecast19=FALSE`  
`ABSpellIcon19=`  
`ABPreCondition19=TRUE`  
  
`ABGem20=item`  
`ABSpell20=Ring of the Ancients`  
`ABSpellFoci20=`  
`ABDurMod20=0`  
`ABSpellAlias20=shrink`  
`ABAnnounce20=/bc`  
`ABSpellMinMana20=0`  
`ABTarCnt20=0`  
`ABTarType20=self`  
`ABRecast20=FALSE`  
`ABSpellIcon20=`  
`ABPreCondition20=TRUE`  
  
`ABGem21=12`  
`ABSpell21=Spirit Bolstering`  
`ABSpellFoci21=`  
`ABDurMod21=0`  
`ABSpellAlias21=pethaste`  
`ABAnnounce21=/bc`  
`ABSpellMinMana21=0`  
`ABTarCnt21=0`  
`ABTarType21=pet mypet cbt idle`  
`ABRecast21=FALSE`  
`ABSpellIcon21=`  
`ABPreCondition21=TRUE`  
  
`ABGem22=item`  
`ABSpell22=Polymorph Wand: Forest Fairy`  
`ABSpellFoci22=`  
`ABDurMod22=0`  
`ABSpellAlias22=illusion`  
`ABAnnounce22=/bc`  
`ABSpellMinMana22=0`  
`ABTarCnt22=0`  
`ABTarType22=self`  
`ABRecast22=FALSE`  
`ABSpellIcon22=`  
`ABPreCondition22=TRUE`  
  
`[AdvEvent]`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECount=3`  
`AECheckTime=8`  
  
`AEGem1=1`  
`AESpell1=Ancestral Arrangement`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=1`  
`AEEventMinHP1=60`  
`AEMinMana1=1`  
`AEMaxMana1=85`  
`AEMinHP1=60`  
`AEMaxHP1=100`  
`AETarType1=self cbt idle`  
`AESpellAlias1=canni`  
`AEAnnounce1=/bc`  
`AETarCnt1=1`  
  
`AEGem2=script`  
`AESpell2=FCanni`  
`AESpellFoci2=`  
`AEDurMod2=0`  
`AEDelay2=0`  
`AEEventMinMana2=1`  
`AEEventMinHP2=80`  
`AEMinMana2=1`  
`AEMaxMana2=80`  
`AEMinHP2=80`  
`AEMaxHP2=100`  
`AETarType2=self`  
`AESpellAlias2=canniscript`  
`AEAnnounce2=/bc`  
`AETarCnt2=1`  
  
`AEGem3=alt`  
`AESpell3=Cannibalization`  
`AESpellFoci3=`  
`AEDurMod3=0`  
`AEDelay3=0`  
`AEEventMinMana3=1`  
`AEEventMinHP3=75`  
`AEMinMana3=1`  
`AEMaxMana3=80`  
`AEMinHP3=73`  
`AEMaxHP3=100`  
`AETarType3=self`  
`AESpellAlias3=canni`  
`AEAnnounce3=/bc`  
`AETarCnt3=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-FCanni] `  
`Commands=3`  
`C1=/if ({Me.PctHPs}<80 && !{Me.Song[Halcyon Shear].ID} && !{Me.Casting.ID} && {Me.AltAbilityReady[Cannibalization]} && !{NetHeal[{Me.CleanName}].hot}) /multiline ; /target myself;/delay 2;/call MQ2Cast ''Halcyon Shear'' gem6 3s CastCheck -targetid|{Me.ID};/netheal hot {Math.Calc[{Spell[Halcyon Shear].Duration.TotalSeconds}*100]} {Me.CleanName}`  
`C2=/if (({Me.PctHPs}<80 && {Me.Song[Halcyon Shear].ID} && {Cast.Ready[Cannibalization]} || {Me.PctHPs}>80) && {Cast.Ready[Cannibalization]}) /multiline ; /call MQ2Cast ''Cannibalization'' alt 3s CastCheck`  
`C3=/if ({Me.Casting.ID}=={Spell[Cannibalization].ID}) /delay 3s !{Me.Casting.ID}`  
  
`[Script-summfavor]`  
`Commands=3`  
`C1=/if (!{FindItemCount[Wishka's Favor Trinket]}) /casting ''Wishka's Favor|gem10''`  
`C2=/if (!{FindItemCount[Wishka's Favor Trinket]}) /delay 1s {Me.Casting.ID}`  
`C3=/if (!{FindItemCount[Wishka's Favor Trinket]}) /delay 7s !{Me.Casting.ID}`

# Druid

## Level 75

No frills. Exodus in AHSpell1 might need turned off for a script

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=FALSE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoPet=FALSE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Tan Rope Bridle|item`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=Apprentice Mage Sarcrynn|a scrykin neophyte|an initiate of Relic|Grand Historian Rygua|Natvil|Jurrock|`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now thanks`  
`FollowDistance=12`  
`FollowStick=12 hold uw`  
`PetCast=`  
`PetAggro=FALSE`  
`PetAssist=0`  
`DoPull=FALSE`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=`  
`DoAura=TRUE`  
`AuraCast=Aura of the Grove|gem9`  
`ForageIni=forage.ini`  
`PetShrinkSpell=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=101`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=2`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
` `  
`AHGem1=alt`  
`AHSpell1=Exodus`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=exodus`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc group hp10 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHHealMode=0|0|12`  
  
`AHGem2=5`  
`AHSpell2=Pure Life`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=fast`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc hp70 war50 shd50 pal50 rng50 mnk50 rog50 brd50 bst50 ber50 shm45 clr65 dru wiz mag enc nec`  
  
`[AdvDebuff]`  
`ADCount=6`  
`ADMobMax=20`  
`ADCheckTime=2`  
  
`ADGem1=1`  
`ADSpell1=Swarm of Fireants`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=dot`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=45`  
`ADSpellRecast1=0`  
`ADSpellDelay1=10`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=90`  
`ADTarEndHP1=30`  
  
`ADGem2=2`  
`ADSpell2=Nature's Blazing Wrath`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=fdot`  
`ADAnnounce2=`  
`ADSpellMinMana2=50`  
`ADSpellRecast2=0`  
`ADSpellDelay2=5`  
`ADTarCnt2=0`  
`ADTarType2=1`  
`ADTarBegHP2=85`  
`ADTarEndHP2=50`  
  
`ADGem3=3`  
`ADSpell3=Equinox Burn`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=fnuke`  
`ADAnnounce3=`  
`ADSpellMinMana3=40`  
`ADSpellRecast3=0`  
`ADSpellDelay3=30`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=80`  
`ADTarEndHP3=20`  
  
`ADGem4=4`  
`ADSpell4=Rime Crystals Rk. II`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=cnuke`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=50`  
`ADSpellRecast4=0`  
`ADSpellDelay4=30`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=70`  
`ADTarEndHP4=15`  
`ADSpellCastonResist1=`  
`ADSpellCastonResist2=`  
`ADSpellCastonResist3=`  
`ADAggroOnly=0`  
`ADSpellCastonResist4=`  
  
`ADGem5=7`  
`ADSpell5=Ensnare`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=snare`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=3`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=65`  
`ADTarEndHP5=5`  
  
`ADGem6=9`  
`ADSpell6=Nature's Serenity`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=paci`  
`ADAnnounce6=`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=0`  
`ADTarType6=0`  
`ADTarBegHP6=0`  
`ADTarEndHP6=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
`ADIfSpellImmune1=`  
`ADIfSpellImmune2=`  
`ADIfSpellImmune3=`  
`ADIfSpellImmune4=`  
`ADIfSpellImmune5=`  
`ADIfSpellImmune6=`  
  
`[AdvBuff]`  
`ABCount=12`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=8`  
`ABSpell1=Direwild Skin`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=skin`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=self`  
  
`ABGem2=8`  
`ABSpell2=Oaken Vigor`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=regen`  
`ABAnnounce2=`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec grp`  
  
`ABGem3=8`  
`ABSpell3=Flight of Eagles`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=foe`  
`ABAnnounce3=`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
  
`ABGem4=8`  
`ABSpell4=Superior Camoflage`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=invis`  
`ABAnnounce4=`  
`ABSpellMinMana4=0`  
`ABTarCnt4=0`  
`ABTarType4=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec grp`  
  
`ABGem5=7`  
`ABSpell5=Legacy of Viridiflora`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=selfthorns`  
`ABAnnounce5=`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=self`  
  
`ABGem6=8`  
`ABSpell6=Mask of the Wild`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=selfMR`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
`ABTarCnt6=1`  
`ABTarType6=self`  
  
`ABGem7=7`  
`ABSpell7=Legacy of Viridiflora`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=grpthorns`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
`ABTarCnt7=1`  
`ABTarType7=self cbt`  
  
`ABGem8=9`  
`ABSpell8=Viridicoat`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=thorns`  
`ABAnnounce8=`  
`ABSpellMinMana8=0`  
`ABTarCnt8=0`  
`ABTarType8=self cbt`  
  
`ABGem9=9`  
`ABSpell9=Spirit of Eagle`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=soe`  
`ABAnnounce9=`  
`ABSpellMinMana9=0`  
`ABTarCnt9=0`  
`ABTarType9=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec cbt idle`  
  
`ABGem10=alt`  
`ABSpell10=Shared Camouflage`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=grpinvis`  
`ABAnnounce10=`  
`ABSpellMinMana10=0`  
`ABTarCnt10=0`  
`ABTarType10=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`ABGem11=9`  
`ABSpell11=Spirit of Wolf`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=sow`  
`ABAnnounce11=`  
`ABSpellMinMana11=0`  
`ABTarCnt11=0`  
`ABTarType11=war shd pal rng mnk rog brd bst ber shm clr wiz mag enc nec`  
  
`ABGem12=`  
`ABSpell12=`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=`  
`ABAnnounce12=`  
`ABSpellMinMana12=0`  
`ABTarCnt12=0`  
`ABTarType12=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast1=TRUE`  
`ABRecast2=FALSE`  
`ABRecast3=FALSE`  
`ABRecast4=FALSE`  
`ABRecast5=FALSE`  
`ABRecast6=FALSE`  
`ABRecast7=FALSE`  
`ABRecast8=FALSE`  
`ABRecast9=TRUE`  
`ABRecast10=FALSE`  
`ABRecast11=FALSE`  
`ABRecast12=FALSE`  
  
`[AdvEvent]`  
`AECount=0`  
`AECheckTime=8`  
`AEGem1=alt`  
`AESpell1=Exodus`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=0`  
`AEEventMinHP1=3`  
`AEMinMana1=1`  
`AEMaxMana1=100`  
`AEMinHP1=1`  
`AEMaxHP1=10`  
`AETarType1=self`  
`AESpellAlias1=`  
`AEAnnounce1=`  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=1`  
`AQCheckTime=8`  
  
`AQGem1=alt`  
`AQSpell1=Radiant Cure`  
`AQSpellCntr1=15`  
`AQSpellFoci1=`  
`AQSpellCureType1=Poisoned Diseased Cursed all`  
`AQSpellMinMana1=0`  
`AQSpellRecast1=0`  
`AQTarCnt1=1`  
`AQTarType1=cbt idle`  
`AQSpellAlias1=RC`  
`AQAnnounce1=/bc`

# Ranger

## Level 70

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=TRUE`  
`DoEvents=FALSE`  
`DoPet=FALSE`  
`DoSit=false`  
`DoLoot=false`  
`DoFW=FALSE`  
`DoForage=False`  
`DoAfk=FALSE`  
`MasterList=The List Is Long`  
`TankName=Joebob`  
`ExcludeList=a skeletal worker|a confused mutation|a hatchling|         `  
`Radius=100`  
`SitAggroRadiusCheck=50`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`AfkMessage=Not now, thanks`  
`DoMount=FALSE`  
`MountCast=`  
`DoPull=FALSE`  
`DoCures=FALSE`  
`DoAura=FALSE`  
`AuraCast=`  
`DeathSlot=chest`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=200`  
`ACAssistPct=99`  
`ACManaPct=70`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1 melee=40 enrage=1 infuriate=1 range=200 standup=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=1`  
`AHCheckTime=2`  
`AHGem1=8`  
`AHSpell1=Sylvan Water`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc group hp30 war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
`AHSpellAlias1=smallheal`  
`AHHealOOBC=FALSE`  
`AHSpellMinMana1=0`  
`AHHealMode=0|0|12`  
  
`[AdvDebuff]`  
`ADCount=3`  
`ADCheckTime=2`  
`ADMobMax=10`  
  
`ADGem1=4`  
`ADSpell1=Earthen Shackles`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=11`  
`ADTarBegHP1=80`  
`ADTarEndHP1=0`  
`ADSpellAlias1=Snare`  
`ADAnnounce1=/bc`  
`ADSpellCastonResist1=`  
  
`ADGem2=1`  
`ADSpell2=Scorched Earth`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellMinMana2=50`  
`ADSpellRecast2=5`  
`ADSpellDelay2=30`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=75`  
`ADTarEndHP2=45`  
`ADSpellAlias2=DD Fire`  
`ADAnnounce2=/bc`  
`ADSpellCastonResist2=`  
  
`ADGem3=2`  
`ADSpell3=Frost Wind`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellMinMana3=60`  
`ADSpellRecast3=5`  
`ADSpellDelay3=30`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=75`  
`ADTarEndHP3=45`  
`ADSpellAlias3=DD Ice`  
`ADAnnounce3=/bc`  
`ADSpellCastonResist3=`  
`ADAggroOnly=0`  
  
`[AdvBuff]`  
`ABCount=7`  
`ABMobMax=12`  
`ABCheckTime=10`  
`ABProactive=TRUE`  
  
`ABGem1=9`  
`ABSpell1=Spirit of Eagle`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=soe`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=60`  
`ABTarCnt1=0`  
`ABTarType1=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self grp`  
  
`ABGem2=9`  
`ABSpell2=Ward of the Hunter`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=SelfDS`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=65`  
`ABTarCnt2=1`  
`ABTarType2=self`  
  
`ABGem3=9`  
`ABSpell3=Eagle Eye`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=SelfBowBuff`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=30`  
`ABTarCnt3=1`  
`ABTarType3=self`  
  
`ABGem4=9`  
`ABSpell4=Howl of the Predator`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=HoP|Predator`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=65`  
`ABTarCnt4=1`  
`ABTarType4=war shd pal mnk rog brd bst ber grp`  
  
`ABGem5=9`  
`ABSpell5=Gaurd of the Earth`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=Gote`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=40`  
`ABTarCnt5=1`  
`ABTarType5=war shd pal mnk rog brd bst ber grp`  
  
`ABGem6=9`  
`ABSpell6=Mask of the Stalker`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=Mask`  
`ABAnnounce6=/bc`  
`ABSpellMinMana5=40`  
`ABTarCnt6=1`  
`ABTarType6=self`  
`ABSpell6=`  
`ABDurMod6=0`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
  
`ABGem7=9`  
`ABSpell7=Strength of the hunter`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=hp`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=40`  
`ABTarCnt7=1`  
`ABTarType7=self grp`  
`ABSpell7=`  
`ABDurMod7=0`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
  
`[AdvEvent]`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
  
`[AdvCure]`  
`AQCount=0`

# Necromancer

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=TRUE`  
`DoDebuffs=FALSE`  
`DoEvents=TRUE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=`  
`TankName=`  
`ExcludeList=a dusty barrel|a dark coffin|a bitten victim|a hollow tree|                                                `  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`AfkMessage=Not now, thank`  
  
`remPetCast=charm 8 1`  
`PetCast=Invoke Death|gem8`  
`PetFoci=`  
  
`PetAggro=FALSE`  
`PetAssist=1`  
`DoMount=FALSE`  
`MountCast=`  
`DoPull=FALSE`  
`DoCures=FALSE`  
`DeathSlot=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=99`  
`ACManaPct=101`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=3`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
  
`AHGem1=5`  
`AHSpell1=Feign Death`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellAlias1=fd`  
`AHSpellMinMana1=5`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc hp30 nec`  
  
`AHGem2=Script`  
`AHSpell2=convertoff`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellAlias2=convertoff`  
`AHSpellMinMana2=0`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc hp40 nec`  
  
`AHGem3=2`  
`AHSpell3=Drain Soul`  
`AHSpellFoci3=`  
`AHDurMod3=7`  
`AHSpellAlias3=tap`  
`AHSpellMinMana3=60`  
`AHAnnounce3=/bc`  
`AHTarCnt3=1`  
`AHClass3=pc hp85 nec tnt`  
  
`[AdvDebuff]`  
`ADCount=3`  
`ADMobMax=10`  
`ADCheckTime=0`  
  
`ADGem1=8`  
`ADSpell1=Beguile Undead`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=charmpet`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=75`  
`ADSpellRecast1=8`  
`ADSpellDelay1=10`  
`ADTarCnt1=0`  
`ADTarType1=10`  
`ADTarBegHP1=100`  
`ADTarEndHP1=1`  
`ADSpellCastonResist1=`  
  
`ADGem2=1`  
`ADSpell2=Dooming Darkness`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=snare`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=20`  
`ADSpellRecast2=1`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=90`  
`ADTarEndHP2=1`  
`ADSpellCastonResist2=`  
  
`ADGem3=3`  
`ADSpell3=Torbas' Poison Blast`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=psndd`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=60`  
`ADSpellRecast3=1`  
`ADSpellDelay3=8`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=85`  
`ADTarEndHP3=40`  
`ADSpellCastonResist3=`  
  
`ADGem4=`  
`ADSpell4=`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=`  
`ADAnnounce4=`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellDelay4=0`  
`ADTarCnt4=0`  
`ADTarType4=0`  
`ADTarBegHP4=0`  
`ADTarEndHP4=0`  
`ADSpellCastonResist4=`  
  
`[AdvBuff]`  
`ABCount=2`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=7`  
`ABSpell1=Arch Shielding`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=20`  
`ABTarCnt1=1`  
`ABTarType1=self`  
  
`ABGem2=7`  
`ABSpell2=Augment Death`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=pethaste`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=50`  
`ABTarCnt2=1`  
`ABTarType2=mypet`  
  
`ABGem3=7`  
`ABSpell3=Endure Cold`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=rcold`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
  
`[AdvEvent]`  
`AECount=3`  
`AECheckTime=2`  
  
`AEGem1=6`  
`AESpell1=Lich`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=1`  
`AEEventMinHP1=40`  
`AEMinMana1=1`  
`AEMaxMana1=90`  
`AEMinHP1=40`  
`AEMaxHP1=100`  
`AETarType1=self`  
`AESpellAlias1=convert`  
`AEAnnounce1=/bc`  
  
`AEGem2=8`  
`AESpell2=Rapacious Subvention`  
`AESpellFoci2=`  
`AEDurMod2=0`  
`AEDelay2=0`  
`AEEventMinMana2=30`  
`AEEventMinHP2=50`  
`AEMinMana2=1`  
`AEMaxMana2=30`  
`AEMinHP2=50`  
`AEMaxHP2=100`  
`AETarType2=clr enc`  
`AESpellAlias2=manafeed`  
`AEAnnounce2=/bc`  
  
`AEGem3=Script`  
`AESpell3=convertoff`  
`AESpellFoci3=`  
`AEDurMod3=0`  
`AEDelay3=0`  
`AEEventMinMana3=1`  
`AEEventMinHP3=1`  
`AEMinMana3=1`  
`AEMaxMana3=100`  
`AEMinHP3=1`  
`AEMaxHP3=35`  
`AETarType3=self`  
`AESpellAlias3=convertoff`  
`AEAnnounce3=/bc`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
  
`[Script-manacheck] `  
`Commands=2`  
`C1=/if ({AEMaxMana[2]}==90) /multiline ; /varset AEMaxMana[2] 30;/return`  
`C2=/varset AEMaxMana[2] 90`  
  
`[Script-convertoff]`  
`Commands=2`  
`C1=/if (!{Me.Buff[Lich].ID}) /return`  
`C2=/if ({Me.Buff[Lich].ID}) /notify BuffWindow Buff{Math.Calc[{Me.Buff[Lich].ID}-1].Int} leftmouseup`

# Enchanter

## Mid lvl 50's

To use charming set tarcnt=1 for charm spell (Cajoling Whispers in this INI) and unremark the "remPetCast" line and
remark "PetCast" to remPetCast

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=`  
`MasterList=`  
`TankName=`  
`ExcludeList=a dusty box|a dark coffin|a bitten victim|a hollow tree|`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
  
`` PetCast=Kintaz`s Animation|gem7 ``  
  
`remPetCast=charm 4 4 "an ethereal banshee,a young bat"`  
  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=mainhand`  
`DoAura=FALSE`  
`AuraCast=`  
  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=98`  
`ACManaPct=70`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=5`  
`ADMobMax=18`  
`ADCheckTime=0`  
  
`ADGem1=4`  
`ADSpell1=Cajoling Whispers`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=charm`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=2`  
`ADSpellDelay1=0`  
`ADTarCnt1=0`  
`ADTarType1=10`  
`ADTarBegHP1=200`  
`ADTarEndHP1=30`  
`ADSpellCastonResist1=tash`  
  
`ADGem2=6`  
`ADSpell2=Entrance`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=mez`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=3`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=12`  
`ADTarBegHP2=200`  
`ADTarEndHP2=90`  
`ADSpellCastonResist2=tash`  
  
`ADGem3=5`  
`ADSpell3=Shiftless Deeds`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=slow`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=40`  
`ADSpellRecast3=2`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=11`  
`ADTarBegHP3=200`  
`ADTarEndHP3=70`  
`ADSpellCastonResist3=tash`  
  
`ADGem4=2`  
`ADSpell4=Tashani`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=tash`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=40`  
`ADSpellRecast4=3`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=200`  
`ADTarEndHP4=50`  
`ADSpellCastonResist4=`  
  
`ADGem5=3`  
`ADSpell5=Dementia`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=dd`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=80`  
`ADSpellRecast5=2`  
`ADSpellDelay5=20`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=80`  
`ADTarEndHP5=20`  
`ADSpellCastonResist5=`  
  
`[AdvBuff]`  
`ABCount=5`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=7`  
`ABSpell1=Arch Shielding`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=buffshp`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=40`  
`ABTarCnt1=1`  
`ABTarType1=self`  
  
`ABGem2=8`  
`ABSpell2=Aanya's Quickening`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=haste`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=40`  
`ABTarCnt2=1`  
`ABTarType2=war shd pal rng mnk rog brd bst ber grp`  
  
`ABGem3=7`  
`ABSpell3=Boon of the Clear Mind`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=mana`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=40`  
`ABTarCnt3=3`  
`ABTarType3=self grp`  
  
`ABGem4=7`  
`ABSpell4=Intellectual Superiority`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=bufffiz`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=40`  
`ABTarCnt4=1`  
`ABTarType4=shd pal rng brd bst ber shm clr dru wiz mag enc nec grp`  
  
`ABGem5=7`  
`ABSpell5=Brilliance`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=buffbrain`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=40`  
`ABTarCnt5=0`  
`ABTarType5=shd pal rng brd bst ber shm clr dru wiz mag enc nec grp`  
  
`[AdvEvent]`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APBefore=`  
`APAfter=`  
`APMobMax=1`  
`APScript=AdvPull`  
  
`[AdvCure]`  
`AQCount=0`

## Level 65

These settings are currently working on the Progression servers as of 7/2/2012.

    [Settings]
    DoMelee=FALSE
    DoHeals=TRUE
    DoBuffs=FALSE
    DoDebuffs=FALSE
    DoEvents=FALSE
    DoCures=FALSE
    DoPull=FALSE
    DoPet=TRUE
    DoSit=TRUE
    DoLoot=FALSE
    DoFW=FALSE
    DoForage=FALSE
    ForageIni=forage.ini
    DoAfk=FALSE
    DoMount=FALSE
    MountCast=Brown Rope Bridle|Item
    MasterList=${NetBots.Client}
    TankName=${Group.MainTank.Name}
    Radius=90
    SitAggroRadiusCheck=75
    AfkMessage=Not now, thanks
    DeathSlot=FALSE
    NetworkINI=
    TraderName=
    FollowDistance=17
    FollowStick=20 hold uw
    PetCast=
    PetAggro=FALSE
    PetAssist=98
    PetFoci=
    PetShrink=FALSE
    PetShrinkSpell=
    [Melee]
    OffTank=FALSE
    ACLeash=50
    ACAssistPct=95
    ACManaPct=101
    ACAnnounce=
    ACMeleeCmd=/melee plugin=1
    ACBefore=
    ACAfter=

    [AdvHeal]
    AHCount=1
    AHCheckTime=2
    AHHealOOBC=FALSE
    AHHealMode=0|0|12
    AHInterruptLevel=2
    AHClassPriority=enc,clr,wiz,mag,nec,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk
    AHAllowDismount=FALSE

    AHGem1=alt
    AHSpell1=Eldritch Rune
    AHSpellFoci1=
    AHDurMod1=0
    AHSpellMinMana1=0
    AHSpellAlias1=aarune
    AHAnnounce1=/bc
    AHTarCnt1=1
    AHClass1=self hp85
    AHPreCondition1=TRUE
    [AdvDebuff]
    ADCount=8
    ADMobMax=20
    ADCheckTime=2
    ADAggroOnly=0
    ADHold=1|2|6|   1=on 0=off|Debuff spell #|Time to wait for debuff|

    ADGem1=1
    ADSpell1=Color Slant
    ADSpellFoci1=
    ADDurMod1=0
    ADSpellAlias1=aestun
    ADAnnounce1=/bc
    ADSpellMinMana1=0
    ADSpellRecast1=3
    ADSpellDelay1=15
    ADTarCnt1=0
    ADTarType1=12
    ADTarBegHP1=200
    ADTarEndHP1=1
    ADSpellCastonResist1=
    ADIfSpellImmune1=
    ADUseHoTT1=0
    ADPreCondition1=TRUE

    ADGem2=8
    ADSpell2=Bliss
    ADSpellFoci2=
    ADDurMod2=0
    ADSpellAlias2=mez
    ADAnnounce2=/bc
    ADSpellMinMana2=0
    ADSpellRecast2=3
    ADSpellDelay2=0
    ADTarCnt2=1
    ADTarType2=12
    ADTarBegHP2=200
    ADTarEndHP2=70
    ADSpellCastonResist2=tash
    ADIfSpellImmune2=
    ADUseHoTT2=0
    ADPreCondition2=TRUE

    ADGem3=2
    ADSpell3=Howl of Tashan
    ADSpellFoci3=
    ADDurMod3=0
    ADSpellAlias3=tash
    ADAnnounce3=
    ADSpellMinMana3=0
    ADSpellRecast3=20
    ADSpellDelay3=0
    ADTarCnt3=1
    ADTarType3=11
    ADTarBegHP3=98
    ADTarEndHP3=60
    ADSpellCastonResist3=
    ADIfSpellImmune3=
    ADUseHoTT3=0
    ADPreCondition3=TRUE

    ADGem4=3
    ADSpell4=Tepid Deeds
    ADSpellFoci4=
    ADDurMod4=0
    ADSpellAlias4=slow
    ADAnnounce4=
    ADSpellMinMana4=0
    ADSpellRecast4=3
    ADSpellDelay4=0
    ADTarCnt4=0
    ADTarType4=1
    ADTarBegHP4=98
    ADTarEndHP4=60
    ADSpellCastonResist4=
    ADIfSpellImmune4=
    ADUseHoTT4=0
    ADPreCondition4=TRUE

    ADGem5=4
    ADSpell5=Insanity
    ADSpellFoci5=
    ADDurMod5=0
    ADSpellAlias5=nuke
    ADAnnounce5=
    ADSpellMinMana5=40
    ADSpellRecast5=1
    ADSpellDelay5=14
    ADTarCnt5=1
    ADTarType5=1
    ADTarBegHP5=90
    ADTarEndHP5=0
    ADSpellCastonResist5=
    ADIfSpellImmune5=
    ADUseHoTT5=0
    ADPreCondition5=TRUE

    ADGem6=1
    ADSpell6=Cripple
    ADSpellFoci6=
    ADDurMod6=0
    ADSpellAlias6=cripple
    ADAnnounce6=/bc
    ADSpellMinMana6=100
    ADSpellRecast6=1
    ADSpellDelay6=0
    ADTarCnt6=0
    ADTarType6=1
    ADTarBegHP6=99
    ADTarEndHP6=0
    ADSpellCastonResist6=
    ADIfSpellImmune6=
    ADUseHoTT6=0
    ADPreCondition6=TRUE

    ADGem7=5
    ADSpell7=Color Shift
    ADSpellFoci7=
    ADDurMod7=0
    ADSpellAlias7=ae2
    ADAnnounce7=/bc
    ADSpellMinMana7=100
    ADSpellRecast7=1
    ADSpellDelay7=0
    ADTarCnt7=0
    ADTarType7=1
    ADTarBegHP7=100
    ADTarEndHP7=0
    ADSpellCastonResist7=
    ADIfSpellImmune7=
    ADUseHoTT7=0
    ADPreCondition7=TRUE

    ADGem8=6
    ADSpell8=Color Flux
    ADSpellFoci8=
    ADDurMod8=0
    ADSpellAlias8=ae3
    ADAnnounce8=/bc
    ADSpellMinMana8=100
    ADSpellRecast8=1
    ADSpellDelay8=0
    ADTarCnt8=0
    ADTarType8=1
    ADTarBegHP8=100
    ADTarEndHP8=0
    ADSpellCastonResist8=
    ADIfSpellImmune8=
    ADUseHoTT8=0
    ADPreCondition8=TRUE

    [AdvBuff]
    ABCount=7
    ABMobMax=18
    ABCheckTime=8

    ABGem1=7
    ABSpell1=Voice of Quellious
    ABSpellFoci1=
    ABDurMod1=0
    ABSpellAlias1=kei
    ABAnnounce1=/bc
    ABSpellMinMana1=0
    ABTarCnt1=1
    ABTarType1=self grp
    ABRecast1=FALSE
    ABSpellIcon1=
    ABPreCondition1=TRUE

    ABGem2=7
    ABSpell2=Vallon's Quickening
    ABSpellFoci2=
    ABDurMod2=0
    ABSpellAlias2=haste
    ABAnnounce2=/bc
    ABSpellMinMana2=0
    ABTarCnt2=1
    ABTarType2=tank grp
    ABRecast2=FALSE
    ABSpellIcon2=
    ABPreCondition2=TRUE

    ABGem3=5
    ABSpell3=Arcane Rune
    ABSpellFoci3=
    ABDurMod3=0
    ABSpellAlias3=rune
    ABAnnounce3=
    ABSpellMinMana3=0
    ABTarCnt3=1
    ABTarType3=self
    ABRecast3=FALSE
    ABSpellIcon3=
    ABPreCondition3=TRUE

    ABGem4=7
    ABSpell4=Guard of Druzzil
    ABSpellFoci4=
    ABDurMod4=0
    ABSpellAlias4=grm
    ABAnnounce4=
    ABSpellMinMana4=0
    ABTarCnt4=1
    ABTarType4=self grp
    ABRecast4=FALSE
    ABSpellIcon4=
    ABPreCondition4=TRUE

    ABGem5=7
    ABSpell5=Shield of the Magi
    ABSpellFoci5=
    ABDurMod5=0
    ABSpellAlias5=shielding
    ABAnnounce5=
    ABSpellMinMana5=0
    ABTarCnt5=1
    ABTarType5=self
    ABRecast5=FALSE
    ABSpellIcon5=
    ABPreCondition5=TRUE

    ABGem6=6
    ABSpell6=Night's Dark Terror
    ABSpellFoci6=
    ABDurMod6=0
    ABSpellAlias6=crow
    ABAnnounce6=
    ABSpellMinMana6=0
    ABTarCnt6=1
    ABTarType6=tank cbt
    ABRecast6=FALSE
    ABSpellIcon6=
    ABPreCondition6=TRUE

    ABGem7=6
    ABSpell7=Aeldorb's Animation
    ABSpellFoci7=
    ABDurMod7=0
    ABSpellAlias7=pet
    ABAnnounce7=/bc
    ABSpellMinMana7=10
    ABTarCnt7=0
    ABTarType7=petspell
    ABRecast7=FALSE
    ABSpellIcon7=
    ABPreCondition7=TRUE

    [AdvEvent]
    AECustom1=
    AECustom2=
    AECustom3=
    AECount=0
    [AdvPull]
    APCheckTime=0
    APRadius=40
    APMobMax=1
    APScript=
    APPath=
    APRetPath=
    APBefore=
    APAfter=
    APAnnounce=
    APRetries=1
    [AdvCure]
    AQCount=0

## Level 78

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=FALSE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=`  
`Radius=100`  
`SitAggroRadiusCheck=50`  
`FollowDistance=12`  
`FollowStick=12 hold uw`  
`AfkMessage=Not now  thanks`  
`PetCast=Ellowind's Animation|gem9|sm`  
`PetAggro=FALSE`  
`PetAssist=1`  
`DoMount=FALSE`  
`MountCast=Small White Drum|item`  
`DoPull=FALSE`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=`  
`DoAura=TRUE`  
`AuraCast=Learner's Aura|gem9`  
`ForageIni=forage.ini`  
`PetShrinkSpell=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=75`  
`ACAssistPct=98`  
`ACManaPct=20`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
`[AdvHeal]`  
`AHCount=0`  
`[AdvDebuff]`  
`ADCount=6`  
`ADCheckTime=0`  
`ADMobMax=20`  
  
`ADGem1=8`  
`ADSpell1=Mystify`  
`ADSpellFoci1=`  
`ADDurMod1=15`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=5`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=12`  
`ADTarBegHP1=200`  
`ADTarEndHP1=60`  
`ADSpellAlias1=mez `  
`ADAnnounce1=/bc [+r+]Mezzed[+x+] <<[+y+] %t [+x+]>>  with[+g+] %s [+x+]`  
  
`ADGem2=1`  
`ADSpell2=Din of Tashan`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellMinMana2=40`  
`ADSpellRecast2=0`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=11`  
`ADTarBegHP2=96`  
`ADTarEndHP2=25`  
`ADSpellAlias2=tash`  
`ADAnnounce2=/bc`  
  
`ADGem3=3`  
`ADSpell3=Multichromatic Assault`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellMinMana3=60`  
`ADSpellRecast3=0`  
`ADSpellDelay3=10`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=70`  
`ADTarEndHP3=20`  
`ADSpellAlias3=dd `  
`ADAnnounce3=/bc`  
  
`ADGem4=3`  
`ADSpell4=Strangling Air`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellMinMana4=50`  
`ADSpellRecast4=0`  
`ADSpellDelay4=0`  
`ADTarCnt4=0`  
`ADTarType4=1`  
`ADTarBegHP4=93`  
`ADTarEndHP4=50`  
`ADSpellAlias4=dot `  
`ADAnnounce4=/bc`  
  
`ADGem5=2`  
`ADSpell5=Desolate Deeds`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellMinMana5=25`  
`ADSpellRecast5=0`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=11`  
`ADTarBegHP5=95`  
`ADTarEndHP5=40`  
`ADSpellAlias5=slow`  
`ADAnnounce5=/bc`  
  
`ADGem6=7`  
`ADSpell6=Fractured Consciousness Rk. II`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=cripple`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=20`  
`ADSpellRecast6=0`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=90`  
`ADTarEndHP6=20`  
`ADSpellCastonResist1=`  
`ADSpellCastonResist2=`  
`ADSpellCastonResist3=`  
`ADSpellCastonResist4=`  
`ADSpellCastonResist5=`  
`ADSpellCastonResist6=`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
`ADIfSpellImmune1=`  
`ADIfSpellImmune2=`  
`ADIfSpellImmune3=`  
`ADIfSpellImmune4=`  
`ADIfSpellImmune5=`  
`ADIfSpellImmune6=`  
  
`[AdvBuff]`  
`ABCount=12`  
`ABMobMax=18`  
`ABCheckTime=1`  
`ABProactive=TRUE`  
  
`ABGem1=5`  
`ABSpell1=Speed of Erradien`  
`ABSpellFoci1=`  
`ABDurMod1=40`  
`ABSpellAlias1=haste`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=10`  
`ABTarCnt1=1`  
`ABTarType1=war pal shd mnk brd bst rng rog clr pet grp`  
  
`ABGem2=4`  
`ABSpell2=Voice of Quellious`  
`ABSpellFoci2=`  
`ABDurMod2=40`  
`ABSpellAlias2=VoQ`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=10`  
`ABTarCnt2=0`  
`ABTarType2=self`  
  
`ABGem3=4`  
`ABSpell3=Overwhelming Splendor`  
`ABSpellFoci3=`  
`ABDurMod3=40`  
`ABSpellAlias3=charisma|cha`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=70`  
`ABTarCnt3=1`  
`ABTarType3=self`  
  
`ABGem4=6`  
`ABSpell4=Draconic Rune`  
`ABSpellFoci4=`  
`ABDurMod4=40`  
`ABSpellAlias4=AR`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=20`  
`ABTarCnt4=1`  
`ABTarType4=self cbt idle`  
  
  
`ABGem5=4`  
`ABSpell5=Voice of Intuition Rk. II`  
`ABSpellFoci5=`  
`ABDurMod5=40`  
`ABSpellAlias5=grpc6|grpc7|`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=0`  
`ABTarType5=self`  
  
`ABGem6=4`  
`ABSpell6=Guard of Druzzil`  
`ABSpellFoci6=`  
`ABDurMod6=40`  
`ABSpellAlias6=resists|Resists|GoD|`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
`ABTarCnt6=1`  
`ABTarType6=self`  
  
`ABGem7=9`  
`ABSpell7=Levitation`  
`ABSpellFoci7=`  
`ABDurMod7=40`  
`ABSpellAlias7=levi`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec cbt idle`  
`ABRecast7=TRUE`  
  
`ABGem8=9`  
`ABSpell8=Cloud of Indifference`  
`ABSpellFoci8=`  
`ABDurMod8=40`  
`ABSpellAlias8=invis`  
`ABAnnounce8=`  
`ABSpellMinMana8=0`  
`ABTarCnt8=0`  
`ABTarType8=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
  
`ABGem9=9`  
`ABSpell9=Seer's Cognizance`  
`ABSpellFoci9=`  
`ABDurMod9=40`  
`ABSpellAlias9=c6|c7`  
`ABAnnounce9=`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=shd pal rng bst bst shm clr dru wiz mag enc grp`  
`ABRecast1=FALSE`  
`ABRecast2=FALSE`  
`ABRecast3=FALSE`  
`ABRecast4=FALSE`  
`ABRecast5=FALSE`  
`ABRecast6=FALSE`  
  
`ABRecast8=FALSE`  
`ABRecast9=FALSE`  
  
`ABGem10=9`  
`ABSpell10=Ward of Bewilderment`  
`ABSpellFoci10=`  
`ABDurMod10=50`  
`ABSpellAlias10=ward`  
`ABAnnounce10=`  
`ABSpellMinMana10=0`  
`ABTarCnt10=1`  
`ABTarType10=self`  
`ABRecast10=FALSE`  
  
`ABGem11=9`  
`ABSpell11=Speed of Vallon`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=lowhaste|vallon|`  
`ABAnnounce11=`  
`ABSpellMinMana11=0`  
`ABTarCnt11=0`  
`ABTarType11=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast11=TRUE`  
  
`ABGem12=`  
`ABSpell12=`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=`  
`ABAnnounce12=`  
`ABSpellMinMana12=0`  
`ABTarCnt12=0`  
`ABTarType12=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast12=FALSE`  
  
`[AdvEvent]`  
`AECount=1`  
`AECheckTime=8`  
  
`AEGem1=alt`  
`AESpell1=Gather Mana`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=0`  
`AEEventMinHP1=50`  
`AEMinMana1=0`  
`AEMaxMana1=5`  
`AEMinHP1=0`  
`AEMaxHP1=100`  
`AETarType1=self`  
`AESpellAlias1=gather`  
`AEAnnounce1=`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
`[AdvCure]`  
`AQCount=0`  
`[Script-SumHam]`  
`Commands=0`  
`C1=NULL`  
`[Script-AdvPull]`  
`Commands=0`  
`C1=NULL`

## Level 85

Setup to cast aoe mez first then single mez

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=FALSE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=`  
`Radius=100`  
`SitAggroRadiusCheck=55`  
`AfkMessage=Dinner...`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Yozan's Animation|gem10`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=FALSE`  
`DoAura=FALSE`  
`AuraCast=Beguiler's Aura|gem7`  
`MountCast=Bridle of the Viridian Cragslither|item`  
`ForageIni=forage.ini`  
`PetShrinkSpell=`  
`NetworkINI=`  
`remPetCast=charm 4 4 "a rat,a young bat"`  
`TraderName=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=110`  
`ACAssistPct=96`  
`ACManaPct=101`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee pettaunt=0`  
`ACBefore=/pet hold`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=2`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
`AHHealMode=1|2|12`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
`AHInterruptLevel=2`  
  
`AHGem1=alt`  
`AHSpell1=Doppelganger`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=dop`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc group hp90 enc self tnt`  
  
`AHGem2=alt`  
`AHSpell2=Eldritch Rune`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=erune`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc group hp80 enc self`  
  
`[AdvDebuff]`  
`ADCount=9`  
`ADMobMax=50`  
`ADCheckTime=1`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=10`  
`ADSpell1=Docility`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=mez`  
`ADAnnounce1=/bc [+r+]Group Mez[+x+] <<[+y+] %t [+x+]>>  with[+g+] %s [+x+]`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellDelay1=0`  
`ADTarCnt1=3`  
`ADTarType1=12`  
`ADTarBegHP1=200`  
`ADTarEndHP1=70`  
`ADSpellCastonResist1=tash`  
`ADHold=0|1|6|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
  
`ADGem2=9`  
`ADSpell2=Befuddle`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=mez`  
`ADAnnounce2=/bc [+r+]Mezzed[+x+] <<[+y+] %t [+x+]>>  with[+g+] %s [+x+]`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=5`  
`ADSpellDelay2=0`  
`ADTarCnt2=2`  
`ADTarType2=12`  
`ADTarBegHP2=200`  
`ADTarEndHP2=70`  
`ADSpellCastonResist2=tash`  
`ADHold=0|1|6|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
  
`ADGem3=3`  
`ADSpell3=Desolate Deeds`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=slow`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=20`  
`ADSpellRecast3=3`  
`ADSpellCastonResist3=tash`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=11`  
`ADTarBegHP3=200`  
`ADTarEndHP3=70`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
  
`ADGem4=2`  
`ADSpell4=Bark of Tashan`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=tash`  
`ADAnnounce4=/bc Tash`  
`ADSpellMinMana4=20`  
`ADSpellRecast4=0`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=11`  
`ADTarBegHP4=200`  
`ADTarEndHP4=50`  
`ADSpellCastonResist4=`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
  
`ADGem5=4`  
`ADSpell5=Fragmented Consciousness`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=dd`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=60`  
`ADSpellRecast5=1`  
`ADSpellDelay5=20`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=75`  
`ADTarEndHP5=30`  
`ADSpellCastonResist5=tash`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
  
`ADGem6=7`  
`ADSpell6=Mind Twist`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=mdot`  
`ADAnnounce6=/bc Mind Twist`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=1`  
`ADSpellDelay6=100`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=90`  
`ADTarEndHP6=10`  
`ADSpellCastonResist6=`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
  
`ADGem7=6`  
`ADSpell7=The Downward Spiral`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=stun`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=10`  
`ADSpellRecast7=1`  
`ADSpellDelay7=0`  
`ADTarCnt7=1`  
`ADTarType7=1`  
`ADTarBegHP7=20`  
`ADTarEndHP7=1`  
`ADSpellCastonResist7=`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
  
`ADGem8=5`  
`ADSpell8=Polychaotic Assault`  
`ADSpellFoci8=`  
`ADDurMod8=0`  
`ADSpellAlias8=pa`  
`ADAnnounce8=/bc`  
`ADSpellMinMana8=70`  
`ADSpellRecast8=0`  
`ADSpellDelay8=0`  
`ADTarCnt8=1`  
`ADTarType8=11`  
`ADTarBegHP8=60`  
`ADTarEndHP8=25`  
`ADSpellCastonResist8=`  
`ADIfSpellImmune8=`  
`ADUseHoTT8=0`  
  
`ADGem9=item`  
`ADSpell9=Staff of Eternal Eloquence`  
`ADSpellFoci9=`  
`ADDurMod9=0`  
`ADSpellAlias9=epic`  
`ADAnnounce9=/bc`  
`ADSpellMinMana9=0`  
`ADSpellRecast9=0`  
`ADSpellDelay9=0`  
`ADTarCnt9=1`  
`ADTarType9=1`  
`ADTarBegHP9=200`  
`ADTarEndHP9=1`  
`ADSpellCastonResist9=`  
`ADIfSpellImmune9=`  
`ADUseHoTT9=0`  
  
`[AdvBuff]`  
`ABCount=9`  
`ABMobMax=50`  
`ABCheckTime=1`  
`ABProactive=TRUE`  
  
`ABGem1=1`  
`ABSpell1=Pearlescent Rune`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=rune`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=20`  
`ABTarCnt1=1`  
`ABRecast1=TRUE`  
`ABTarType1=self cbt idle`  
`ABSpellIcon1=`  
  
`ABGem2=8`  
`ABSpell2=Guard of Druzzil`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=god`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=40`  
`ABTarCnt2=3`  
`ABRecast2=TRUE`  
`ABTarType2=self grp cbt idle`  
`ABSpellIcon2=`  
  
`ABGem3=8`  
`ABSpell3=Voice of Prescience`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=mana`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=40`  
`ABTarCnt3=3`  
`ABRecast3=TRUE`  
`ABTarType3=self grp cbt idle`  
`ABSpellIcon3=`  
  
`ABGem4=8`  
`ABSpell4=Shield of the Void`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=svoid`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=6`  
`ABTarCnt4=1`  
`ABRecast4=TRUE`  
`ABTarType4=self cbt idle`  
`ABSpellIcon4=`  
  
`ABGem5=8`  
`ABSpell5=Hastening of Erradien`  
`ABSpellFoci5=`  
`ABDurMod5=15`  
`ABSpellAlias5=haste`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=30`  
`ABTarCnt5=3`  
`ABRecast5=TRUE`  
`ABTarType5=war shd pal rng mnk rog brd bst ber shm clr self mypet grp pet cbt idle`  
`ABSpellIcon5=`  
  
`ABGem6=item`  
`ABSpell6=Loop of Loyality`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=def`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=5`  
`ABTarCnt6=1`  
`ABRecast6=TRUE`  
`ABTarType6=self idle`  
`ABSpellIcon6=`  
  
`ABGem7=item`  
`ABSpell7=Fang of The Fallen God`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=ffg`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=5`  
`ABTarCnt7=1`  
`ABRecast7=TRUE`  
`ABTarType7=self idle`  
`ABSpellIcon7=`  
  
`ABGem8=item`  
`ABSpell8=Veil of Draconic Study`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=Vds`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=5`  
`ABTarCnt8=1`  
`ABRecast8=TRUE`  
`ABTarType8=self idle`  
`ABSpellIcon8=`  
  
`ABGem9=item`  
`ABSpell9=Amice of Black Dawn`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=Vds`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABRecast9=TRUE`  
`ABTarType9=self idle`  
`ABSpellIcon9=`  
  
`[AdvEvent]`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APBefore=`  
`APAfter=`  
`APMobMax=1`  
`APScript=AdvPull`  
`APAgroRadius=55`  
`APAggroRadius=55`  
`APPath=`  
`APCheckTime=0`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-Defense]`  
`Commands=0`  
`C1=/return`

## Level 90

Thanks to Olain for this submission! (Posted 8/24/11)

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Verdant Hedgerow Leaf`  
`MasterList=${NetBots.Client}`  
`TankName=${Group.MainTank.Name}`  
`Radius=50`  
`SitAggroRadiusCheck=35`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Novak's Animation Rk. II|gem2`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`PetShrink=FALSE`  
`PetShrinkSpell=`  
`DoAura=TRUE`  
`AuraCast=Learner's Aura Rk. II|gem2`  
`GoMNuke=Alias of debuff for GoM `  
`GoRMNuke=`  
`GoERMNuke=`  
`GoAERMNuke=`  
`GoDERMNuke= `  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=70`  
`ACAnnounce=`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/pet qattack`  
`ACAfter= `  
  
`[AdvHeal]`  
`AHCount=2`  
`AHCheckTime=0`  
`AHHealOOBC=FALSE`  
`AHHealMode=1|2|12`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
`AHInterruptLevel=2 `  
  
`AHGem1=alt`  
`AHSpell1=Doppelganger`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=dop`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc group hp90 enc self tnt`  
  
`AHGem2=alt`  
`AHSpell2=Veil of Mindshadow`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=0`  
`AHSpellAlias2=erune`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=pc group hp80 enc self tnt`  
`AHPreCondition1=TRUE`  
`AHPreCondition2=TRUE `  
  
`[AdvDebuff]`  
`ADCount=7`  
`ADMobMax=50`  
`ADCheckTime=1`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff| `  
  
`ADGem1=9`  
`ADSpell1=Serenity Rk. II`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=aemez`  
`ADAnnounce1=/bc [+r+]Group Mez[+x+] <<[+y+] %t [+x+]>>  with[+g+] %s [+x+]`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=1`  
`ADSpellDelay1=0`  
`ADTarCnt1=3`  
`ADTarType1=12`  
`ADTarBegHP1=100`  
`ADTarEndHP1=70`  
`ADSpellCastonResist1=tash`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=8`  
`ADSpell2=Baffle Rk. II`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=mez`  
`ADAnnounce2=/bc [+r+]Mezzed[+x+] <<[+y+] %t [+x+]>>  with[+g+] %s [+x+]`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=5`  
`ADSpellDelay2=0`  
`ADTarCnt2=2`  
`ADTarType2=12`  
`ADTarBegHP2=100`  
`ADTarEndHP2=70`  
`ADSpellCastonResist2=tash`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=7`  
`ADSpell3=Curtailing Helix Rk. II`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=slow`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=20`  
`ADSpellRecast3=5`  
`ADSpellCastonResist3=tash`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=10`  
`ADTarBegHP3=200`  
`ADTarEndHP3=10`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=6`  
`ADSpell4=Clamor of Tashan Rk. II`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=tash`  
`ADAnnounce4=/bc Tash`  
`ADSpellMinMana4=20`  
`ADSpellRecast4=0`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=200`  
`ADTarEndHP4=50`  
`ADSpellCastonResist4=`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE `  
  
`ADGem5=3`  
`ADSpell5=Baffling Constriction Rk. II`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=dot`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=30`  
`ADSpellRecast5=1`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=90`  
`ADTarEndHP5=10`  
`ADSpellCastonResist5=tash`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=5`  
`ADSpell6=Spectral Assault Rk. II`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=dd1`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=30`  
`ADSpellRecast6=5`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=90`  
`ADTarEndHP6=10`  
`ADSpellCastonResist6=`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=4`  
`ADSpell7=Mindblade Rk. II`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=dd2`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=30`  
`ADSpellRecast7=5`  
`ADSpellDelay7=0`  
`ADTarCnt7=1`  
`ADTarType7=1`  
`ADTarBegHP7=90`  
`ADTarEndHP7=10`  
`ADSpellCastonResist7=`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`[AdvBuff]`  
`ABCount=8`  
`ABMobMax=50`  
`ABCheckTime=1`  
`ABProactive=TRUE`  
  
`ABGem1=1`  
`ABSpell1=Spectral Unity Rk. II`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=rune`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=20`  
`ABTarCnt1=1`  
`ABRecast1=TRUE`  
`ABTarType1=self cbt idle`  
`ABSpellIcon1=Polyspectral Rune Rk. II`  
`ABPreCondition1=TRUE`  
  
`ABGem2=2`  
`ABSpell2=Hastening of Novak Rk. II`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=haste`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=30`  
`ABTarCnt2=1`  
`ABRecast2=FALSE`  
`ABTarType2=war shd pal rng mnk rog brd bst ber mypet pet grp cbt idle`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=2`  
`ABSpell3=Voice of Forethought Rk. II`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=clarity`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=40`  
`ABTarCnt3=3`  
`ABRecast3=TRUE`  
`ABTarType3=pal rng self clr grp idle`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=2`  
`ABSpell4=Shield of Dreams Rk. II`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=svoid`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=6`  
`ABTarCnt4=1`  
`ABRecast4=TRUE`  
`ABTarType4=self idle`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=2`  
`ABSpell5=Baffler's Aura Rk. II`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=regenaura`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=6`  
`ABTarCnt5=1`  
`ABRecast5=TRUE`  
`ABTarType5=self aura idle`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=2`  
`ABSpell6=Learner's Aura Rk. II`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=`  
`ABAnnounce6=`  
`ABSpellMinMana6=10`  
`ABTarCnt6=1`  
`ABTarType6=self aura idle`  
`ABRecast6=TRUE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=2`  
`ABSpell7=Manastorm Rk. II`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=storm`  
`ABAnnounce7=`  
`ABSpellMinMana7=50`  
`ABTarCnt7=2`  
`ABTarType7=self rng grp idle`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=2`  
`ABSpell8=Ward of Bafflement Rk. II`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=selfstun`  
`ABAnnounce8=`  
`ABSpellMinMana8=20`  
`ABTarCnt8=1`  
`ABTarType8=self idle`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`[AdvEvent]`  
`AECount=1`  
`AECheckTime=8`  
  
`AEGem1=alt`  
`AESpell1=Mana Draw`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=0`  
`AEEventMinHP1=50`  
`AEMinMana1=0`  
`AEMaxMana1=5`  
`AEMinHP1=0`  
`AEMaxHP1=100`  
`AETarType1=self`  
`AESpellAlias1=gather`  
`AEAnnounce1=`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AETarCnt1=1`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`

# Bard

## Mid lvl 50's

I'm using a custom BardCombatGems being set via a script. To not use a custom BardCombatGems, make these adjustments to
the complete INI below this:

`[AdvDebuff]`  
`ADCount=6`  
`ADMobMax=18`  
`ADCheckTime=0`  
`ADAgroOnly=FALSE`  
  
`ADGem1=script`  
`ADSpell1=CombatGems`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=CombatGems`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellDelay1=999`  
`ADTarCnt1=0`  
`ADTarType1=1`  
`ADTarBegHP1=100`  
`ADTarEndHP1=0`  
`ADSpellCastonResist1=`  
  
`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=FALSE`  
`DoBuffs=TRUE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPet=FALSE`  
`DoSit=FALSE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=`  
`TankName=`  
`ExcludeList=a dusty box|a bitten victim|a hollow tree|`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=`  
`PetAggro=FALSE`  
`PetAssist=0`  
`DoMount=FALSE`  
`MountCast=`  
`DoPull=FALSE`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=mainhand`  
`DoAura=FALSE`  
`AuraCast=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=99`  
`ACManaPct=1`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1 melee=200 enrage=1 infuriate=1 range=0 standup=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=1`  
`ADMobMax=18`  
`ADCheckTime=0`  
`ADAgroOnly=FALSE`  
  
`ADGem1=script`  
`ADSpell1=CombatGems`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=CombatGems`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellDelay1=999`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=100`  
`ADTarEndHP1=0`  
`ADSpellCastonResist1=`  
  
`ADGem2=5`  
`ADSpell2=Psalm of Mystic Shielding`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=ds`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=0`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=100`  
`ADTarEndHP2=0`  
`ADSpellCastonResist2=`  
  
`ADGem3=3`  
`` ADSpell3=Tuyen`s Chant of Flame ``  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=firedot`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=2`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=99`  
`ADTarEndHP3=0`  
`ADSpellCastonResist3=`  
  
`ADGem4=2`  
`` ADSpell4=Tuyen`s Chant of Disease ``  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=dsedot`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=2`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=99`  
`ADTarEndHP4=0`  
`ADSpellCastonResist4=`  
  
`ADGem5=4`  
`` ADSpell5=Vilia`s Chorus of Celerity ``  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=haste`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=0`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=100`  
`ADTarEndHP5=0`  
`ADSpellCastonResist5=`  
  
`ADGem6=1`  
`` ADSpell6=Tuyen`s Chant of Frost ``  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=colddot`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=2`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=99`  
`ADTarEndHP6=0`  
`ADSpellCastonResist6=`  
  
`ADGem7=`  
`ADSpell7=`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=`  
`ADAnnounce7=`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=0`  
`ADTarType7=0`  
`ADTarBegHP7=0`  
`ADTarEndHP7=0`  
  
`[AdvBuff]`  
`ABCount=3`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=6`  
`ABSpell1=Hymn of Restoration`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=regen`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=brd`  
  
`ABGem2=7`  
`ABSpell2=Cassindra's Chorus of Clarity`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=mana`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=1`  
`ABTarType2=brd`  
  
`ABGem3=8`  
`` ABSpell3=Selo`s Accelerating Chorus ``  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=selo`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=brd`  
  
`[AdvEvent]`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APBefore=`  
`APAfter=`  
`APMobMax=1`  
`APScript=`  
`APAgroRadius=40`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-CombatGems]`  
`Commands=2`  
`C1=/if ({ACMATarget}!={Target.ID}) /multiline ; /target id {ACMATarget};/delay 5`  
`C2=/if ({BardCombatGems.NotEqual[1 2 4 5 4 5 3 7]}) /multiline ; /twist off;/varset BardCombatGems 1 2 4 5 4 5 3 7;/delay 5`  
  
`[Script-reqadv]`  
`Commands=9`  
`C1=/varset Timer 10m`  
`C2=/equipset drums`  
`C3=/call mbwayplay ldon b t c`  
`C4=/mqp`  
`C5=/varset Timer 10m`  
`C6=/call mbwayplay Wayfarer b t c`  
`C7=/mb follow {FollowName}`  
`C8=/equipset combat`  
`C9=/timed 200 /bct all //mb buffup`

## Mid Level 60's

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=FALSE `  
`DoBuffs=TRUE `  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoPet=FALSE `  
`DoSit=FALSE `  
`DoLoot=FALSE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`DoAfk=FALSE `  
`MasterList=bob,john,jane `  
`TankName=bob `  
`ExcludeList=a dusty box|a bitten victim|a hollow tree| `  
`Radius=150 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Not now, thanks `  
`FollowDistance=20 `  
`FollowStick=20 hold uw `  
`PetCast= `  
`PetAggro=FALSE `  
`PetAssist=0 `  
`DoMount=FALSE `  
`MountCast= `  
`DoPull=FALSE `  
`PetFoci= `  
`DoCures=FALSE `  
`DeathSlot=mainhand `  
`DoAura=FALSE `  
`AuraCast= `  
`ForageIni=forage.ini `  
`PetShrinkSpell= `  
  
`[Melee] `  
`OffTank=FALSE `  
`ACLeash=50 `  
`ACAssistPct=98 `  
`ACManaPct=1 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 melee=200 enrage=1 infuriate=1 range=0 standup=1 `  
`ACBefore= `  
`ACAfter= `  
  
`[AdvHeal] `  
`AHCount=0 `  
  
`[AdvDebuff] `  
`ADCount=7 `  
`ADMobMax=18 `  
`ADCheckTime=0 `  
`ADAggroOnly=0 `  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff| `  
  
`ADGem1=4 `  
`ADSpell1=Dreams of Thule `  
`ADSpellFoci1= `  
`ADDurMod1=0 `  
`ADSpellAlias1=mez `  
`ADAnnounce1=/bc `  
`ADSpellMinMana1=0 `  
`ADSpellRecast1=0 `  
`ADSpellDelay1=0 `  
`ADTarCnt1=1 `  
`ADTarType1=12 `  
`ADTarBegHP1=100 `  
`ADTarEndHP1=0 `  
`ADSpellCastonResist1= `  
  
`ADGem2=5 `  
`ADSpell2=Warsong of Zek `  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2=ADHaste `  
`ADAnnounce2=/bc `  
`ADSpellMinMana2=0 `  
`ADSpellRecast2=0 `  
`ADSpellDelay2=0 `  
`ADTarCnt2=1 `  
`ADTarType2=1 `  
`ADTarBegHP2=100 `  
`ADTarEndHP2=0 `  
`ADSpellCastonResist2= `  
` `  
`ADGem3=1 `  
`ADSpell3=Tuyen's Chant of Venom `  
`ADSpellFoci3= `  
`ADDurMod3=0 `  
`ADSpellAlias3=pdot `  
`ADAnnounce3=/bc `  
`ADSpellMinMana3=0 `  
`ADSpellRecast3=0 `  
`ADSpellDelay3=0 `  
`ADTarCnt3=1 `  
`ADTarType3=1 `  
`ADTarBegHP3=100 `  
`ADTarEndHP3=0 `  
`ADSpellCastonResist3= `  
  
`ADGem4=2 `  
`ADSpell4=Tuyen's Chant of Frost `  
`ADSpellFoci4= `  
`ADDurMod4=0 `  
`ADSpellAlias4=ddot `  
`ADAnnounce4=/bc `  
`ADSpellMinMana4=0 `  
`ADSpellRecast4=0 `  
`ADSpellCastonResist4= `  
`ADSpellDelay4=0 `  
`ADTarCnt4=1 `  
`ADTarType4=1 `  
`ADTarBegHP4=100 `  
`ADTarEndHP4=0 `  
  
`ADGem5=6 `  
`ADSpell5=Psalm of Veeshan `  
`ADSpellFoci5= `  
`ADDurMod5=0 `  
`ADSpellAlias5=adresbuff `  
`ADAnnounce5=/bc `  
`ADSpellMinMana5=0 `  
`ADSpellRecast5=0 `  
`ADSpellCastonResist5= `  
`ADSpellDelay5=0 `  
`ADTarCnt5=1 `  
`ADTarType5=1 `  
`ADTarBegHP5=100 `  
`ADTarEndHP5=0 `  
  
`ADGem6=9 `  
`ADSpell6=Selo's Consonant Chain `  
`ADSpellFoci6= `  
`ADDurMod6=0 `  
`ADSpellAlias6=snare `  
`ADAnnounce6=/bc `  
`ADSpellMinMana6=0 `  
`ADSpellRecast6=0 `  
`ADSpellCastonResist6= `  
`ADSpellDelay6=0 `  
`ADTarCnt6=0 `  
`ADTarType6=1 `  
`ADTarBegHP6=100 `  
`ADTarEndHP6=0 `  
  
`ADGem7=9 `  
`ADSpell7=Cassindra's Insipid Ditty `  
`ADSpellFoci7= `  
`ADDurMod7=0 `  
`ADSpellAlias7=manadrain `  
`ADAnnounce7=/bc `  
`ADSpellMinMana7=0 `  
`ADSpellRecast7=0 `  
`ADSpellCastonResist7= `  
`ADSpellDelay7=0 `  
`ADTarCnt7=0 `  
`ADTarType7=1 `  
`ADTarBegHP7=100 `  
`ADTarEndHP7=0 `  
  
`[AdvBuff] `  
`ABCount=5 `  
`ABMobMax=12 `  
`ABCheckTime=8 `  
`ABProactive=TRUE `  
  
`ABGem1=5 `  
`ABSpell1=Warsong of Zek `  
`ABSpellFoci1= `  
`ABDurMod1=0 `  
`ABSpellAlias1=haste `  
`ABAnnounce1=/bc `  
`ABSpellMinMana1=0 `  
`ABTarCnt1=1 `  
`ABTarType1=brd  `  
`ABRecast1=FALSE  `  
  
`ABGem2=6 `  
`ABSpell2=Psalm of Veeshan `  
`ABSpellFoci2= `  
`ABDurMod2=0 `  
`ABSpellAlias2=resbuff `  
`ABAnnounce2=/bc `  
`ABSpellMinMana2=0 `  
`ABTarCnt2=1 `  
`ABTarType2=brd `  
`ABRecast2=FALSE `  
  
`ABGem3=7 `  
`ABSpell3=Wind of Marr `  
`ABSpellFoci3= `  
`ABDurMod3=0 `  
`ABSpellAlias3=reg `  
`ABAnnounce3=/bc `  
`ABSpellMinMana3=0 `  
`ABTarCnt3=1 `  
`ABTarType3=brd `  
`ABRecast3=FALSE `  
  
`ABGem4=8 `  
`ABSpell4=Selo's Accelerating Chorus `  
`ABSpellFoci4= `  
`ABDurMod4=0 `  
`ABSpellAlias4=selo `  
`ABAnnounce4=/bc `  
`ABSpellMinMana4=0 `  
`ABTarCnt4=1 `  
`ABTarType4=brd `  
`ABRecast4=FALSE  `  
  
`ABGem5=item `  
`ABSpell5=Singing Steel Boots `  
`ABSpellFoci5= `  
`ABDurMod5=0 `  
`ABSpellAlias5=lev `  
`ABAnnounce5=/bc `  
`ABSpellMinMana5=0 `  
`ABTarCnt5=0 `  
`ABTarType5=brd `  
`ABRecast5=FALSE `  
  
`[AdvCure] `  
`AQCount=0  `  
  
`[AdvEvent] `  
`AECount=0 `  
  
`[AdvPull] `  
`APBefore= `  
`APAfter= `  
`APMobMax=4 `  
`APScript=Pull `  
`APPath=PullPoNa `  
`APCheckTime=30 `  
`APRadius=149 `  
`APAnnounce= `  
`APRetPath= `  
  
`[Script-reqadv] `  
`Commands=11 `  
`C1=/varset Timer 10m `  
`C2=/equipset drums `  
`C3=/call CastCall {Me.CleanName} `*`cast`` ``selo`*` `  
`C4=/call mbwayplay LFldonGF b t c `  
`C5=/mqp `  
`C6=/mb follow {FollowName} `  
`C7=/varset Timer 10m `  
`C8=/call mbwayplay BBGFWayfarer b t c `  
`C9=/equipset melee  `  
`C10=/makeleader {FollowName}  `  
`C11=/timed 200 /bcaa //mb buffup  `  
  
`[Script-FHalls] `  
`Commands=10 `  
`C1=/varset Timer 10m `  
`C2=/equipset drums `  
`C3=/call mbwayplay fhalls b `  
`C4=/tar Eldros Danmor `  
`C5=/delay 2s `  
`C6=/say interested in visiting `  
`C7=/delay 1s `  
`C8=/bcaa //keypress esc `  
`C9=/call mbwayplay fhalls e `  
`C10=/equipset melee `  
  
`[Script-reqadvnro] `  
`Commands=9 `  
`C1=/varset Timer 10m `  
`C2=/equipset drums `  
`C3=/call mbwayplay NRoLDoN b `  
`C4=/mqp `  
`C5=/varset Timer 10m `  
`C6=/call mbwayplay NRoLDoN e `  
`C7=/mb follow {TankName} `  
`C8=/equipset combat `  
`C9=/timed 50 /bct all //mb buffup`

## Level 85

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=FALSE `  
`DoBuffs=TRUE `  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoPet=FALSE `  
`DoSit=FALSE `  
`DoLoot=FALSE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`DoAfk=FALSE `  
`MasterList=${NetBots.Client}`  
`TankName= `  
`Radius=75 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Not now, thanks `  
`FollowDistance=20 `  
`FollowStick=20 hold uw `  
`PetCast= `  
`PetAggro=FALSE `  
`PetAssist=0 `  
`DoMount=FALSE `  
`MountCast= `  
`DoPull=FALSE `  
`PetFoci= `  
`DoCures=FALSE `  
`DeathSlot=FALSE `  
`DoAura=FALSE `  
`AuraCast= `  
`ForageIni=forage.ini `  
`PetShrinkSpell= `  
`NetworkINI=`  
`TraderName=`  
  
`[Melee] `  
`OffTank=FALSE `  
`ACLeash=50 `  
`ACAssistPct=95`  
`ACManaPct=1 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 melee=200 enrage=1 infuriate=1 range=0 standup=1 `  
`ACBefore= `  
`ACAfter= `  
  
`[AdvHeal] `  
`AHCount=0 `  
  
`[AdvDebuff] `  
`ADCount=9 `  
`ADMobMax=18 `  
`ADCheckTime=0 `  
`ADAggroOnly=0 `  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff| `  
  
`ADGem1=6`  
`ADSpell1=Command of Queen Veneneu`  
`ADSpellFoci1= `  
`ADDurMod1=0 `  
`ADSpellAlias1=mez `  
`ADAnnounce1=/bc `  
`ADSpellMinMana1=0 `  
`ADSpellRecast1=0 `  
`ADSpellDelay1=0 `  
`ADTarCnt1=1 `  
`ADTarType1=12 `  
`ADTarBegHP1=100 `  
`ADTarEndHP1=0 `  
`ADSpellCastonResist1= `  
`ADIfSpellImmune1= `  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=1`  
`ADSpell2=War March of Brekt`  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2= ADHaste `  
`ADAnnounce2=/bc `  
`ADSpellMinMana2=0 `  
`ADSpellRecast2=0 `  
`ADSpellDelay2=0 `  
`ADTarCnt2=1 `  
`ADTarType2=1 `  
`ADTarBegHP2=100 `  
`ADTarEndHP2=0 `  
`ADSpellCastonResist2= `  
`ADIfSpellImmune2= `  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=3`  
`ADSpell3=Dirge of the Darkvine Rk. II`  
`ADSpellFoci3= `  
`ADDurMod3=0 `  
`ADSpellAlias3= ADprotect`  
`ADAnnounce3=/bc `  
`ADSpellMinMana3=0 `  
`ADSpellRecast3=0 `  
`ADSpellCastonResist3= `  
`ADSpellDelay3=0 `  
`ADTarCnt3=1 `  
`ADTarType3=1 `  
`ADTarBegHP3=100 `  
`ADTarEndHP3=0 `  
`ADIfSpellImmune3= `  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=4`  
`ADSpell4=Talendor's Aria`  
`ADSpellFoci4= `  
`ADDurMod4=0 `  
`ADSpellAlias4=spellbuff `  
`ADAnnounce4=/bc `  
`ADSpellMinMana4=0 `  
`ADSpellRecast4=0 `  
`ADSpellCastonResist4= `  
`ADSpellDelay4=0 `  
`ADTarCnt4=1 `  
`ADTarType4=1 `  
`ADTarBegHP4=100 `  
`ADTarEndHP4=0 `  
`ADIfSpellImmune4= `  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=10`  
`ADSpell5=Talendor's Chant of Flame`  
`ADSpellFoci5= `  
`ADDurMod5=0 `  
`ADSpellAlias5=fdot `  
`ADAnnounce5=/bc `  
`ADSpellMinMana5=0 `  
`ADSpellRecast5=0 `  
`ADSpellDelay5=0 `  
`ADTarCnt5=1 `  
`ADTarType5=1 `  
`ADTarBegHP5=100 `  
`ADTarEndHP5=0 `  
`ADSpellCastonResist5= `  
`ADIfSpellImmune5= `  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=2`  
`ADSpell6=Katta's Song of Sword Dancing`  
`ADSpellFoci6= `  
`ADDurMod6=0 `  
`ADSpellAlias6= ADdexbuff`  
`ADAnnounce6=/bc `  
`ADSpellMinMana6=0 `  
`ADSpellRecast6=0 `  
`ADSpellCastonResist6= `  
`ADSpellDelay6=0 `  
`ADTarCnt6=1`  
`ADTarType6=1 `  
`ADTarBegHP6=100 `  
`ADTarEndHP6=0 `  
`ADIfSpellImmune6= `  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=8`  
`ADSpell7=Selo's Consonant Chain `  
`ADSpellFoci7= `  
`ADDurMod7=0 `  
`ADSpellAlias7=snare `  
`ADAnnounce7=/bc `  
`ADSpellMinMana7=0 `  
`ADSpellRecast7=0 `  
`ADSpellCastonResist7= `  
`ADSpellDelay7=0 `  
`ADTarCnt7=1`  
`ADTarType7=1 `  
`ADTarBegHP7=100 `  
`ADTarEndHP7=0 `  
`ADIfSpellImmune7= `  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`ADGem8=8`  
`ADSpell8=Selo's Consonant Chain `  
`ADSpellFoci8= `  
`ADDurMod8=0 `  
`ADSpellAlias8=slow `  
`ADAnnounce8=/bc `  
`ADSpellMinMana8=0 `  
`ADSpellRecast8=0 `  
`ADSpellCastonResist8= `  
`ADSpellDelay8=0 `  
`ADTarCnt8=0 `  
`ADTarType8=1 `  
`ADTarBegHP8=100 `  
`ADTarEndHP8=0 `  
`ADIfSpellImmune8= `  
`ADUseHoTT8=0`  
`ADPreCondition8=TRUE`  
  
`ADGem9=7`  
`ADSpell9=Cassindra's Insipid Ditty `  
`ADSpellFoci9= `  
`ADDurMod9=0 `  
`ADSpellAlias9=man ADrain `  
`ADAnnounce9=/bc `  
`ADSpellMinMana9=0 `  
`ADSpellRecast9=0 `  
`ADSpellCastonResist9= `  
`ADSpellDelay9=0 `  
`ADTarCnt9=0 `  
`ADTarType9=1 `  
`ADTarBegHP9=100 `  
`ADTarEndHP9=0 `  
`ADIfSpellImmune9= `  
`ADUseHoTT9=0`  
`ADPreCondition9=TRUE`  
  
`[AdvBuff] `  
`ABCount=6 `  
`ABMobMax=12 `  
`ABCheckTime=8 `  
`ABProactive=TRUE `  
  
`ABGem1=1`  
`ABSpell1=War March of Brekt`  
`ABSpellFoci1= `  
`ABDurMod1=0 `  
`ABSpellAlias1=haste `  
`ABAnnounce1=/bc `  
`ABSpellMinMana1=0 `  
`ABTarCnt1=1 `  
`ABTarType1=brd cbt idle `  
`ABRecast1=FALSE `  
`ABSpellIcon1=`  
  
`ABGem2=3`  
`ABSpell2=Dirge of the Darkvine Rk. II`  
`ABSpellFoci2= `  
`ABDurMod2=0 `  
`ABSpellAlias2=protect`  
`ABAnnounce2=/bc `  
`ABSpellMinMana2=0 `  
`ABTarCnt2=1 `  
`ABTarType2=brd `  
`ABRecast2=FALSE `  
`ABSpellIcon2=`  
  
`ABGem3=7 `  
`ABSpell3=Cantata of Rodcet`  
`ABSpellFoci3= `  
`ABDurMod3=0 `  
`ABSpellAlias3=reg `  
`ABAnnounce3=/bc `  
`ABSpellMinMana3=0 `  
`ABTarCnt3=1 `  
`ABTarType3=brd `  
`ABRecast3=FALSE `  
`ABSpellIcon3=`  
  
`ABGem4=6`  
`ABSpell4=Selo's Accelerating Chorus `  
`ABSpellFoci4= `  
`ABDurMod4=0 `  
`ABSpellAlias4=selo `  
`ABAnnounce4=/bc `  
`ABSpellMinMana4=0 `  
`ABTarCnt4=0`  
`ABTarType4=brd `  
`ABRecast4=FALSE `  
`ABSpellIcon4=`  
  
`ABGem5=item `  
`ABSpell5=Singing Steel Boots `  
`ABSpellFoci5= `  
`ABDurMod5=0 `  
`ABSpellAlias5=lev `  
`ABAnnounce5=/bc `  
`ABSpellMinMana5=0 `  
`ABTarCnt5=0 `  
`ABTarType5=brd `  
`ABRecast5=FALSE `  
`ABSpellIcon5=`  
  
`ABGem6=item `  
`ABSpell6=Stonewall Pauldrons `  
`ABSpellFoci6= `  
`ABDurMod6=0 `  
`ABSpellAlias6=selfac `  
`ABAnnounce6=/bc `  
`ABSpellMinMana6=0 `  
`ABTarCnt6=1 `  
`ABTarType6=self `  
`ABRecast6=FALSE `  
`ABSpellIcon6=`  
  
`[AdvCure] `  
`AQCount=0 `  
  
`[AdvEvent] `  
`AECount=0 `  
  
`[AdvPull] `  
`APBefore= `  
`APAfter= `  
`APMobMax=4 `  
`APScript= `  
`APPath= `  
`APCheckTime=30 `  
`APRadius=149 `  
`APAnnounce= `  
`APRetPath= `  
`APRetries=1`

## Level 85 b

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=FALSE`  
`DoBuffs=TRUE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPet=FALSE`  
`DoSit=FALSE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=`  
`PetAggro=FALSE`  
`PetAssist=0`  
`DoMount=FALSE`  
`MountCast=`  
`DoPull=FALSE`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=FALSE`  
`ForageIni=forage.ini`  
`PetShrinkSpell=`  
`NetworkINI=t:\mb_network.ini`  
`TraderName=`  
`PetShrink=TRUE`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=98`  
`ACManaPct=1`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1 melee=200 enrage=1 infuriate=1 range=0 standup=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=1`  
`AHCheckTime=2`  
`AHHealOOBC=FALSE`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`AHGem1=alt`  
`AHSpell1=Shield of Notes`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=0`  
`AHSpellAlias1=sheal`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=pc hp70 brd self`  
`AHPreCondition1=TRUE`  
  
`[ADvDebuff]`  
`ADCount=19`  
`ADMobMax=12`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=4`  
`ADSpell1=Serenity of Oceangreen`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=bmez`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellDelay1=0`  
`ADTarCnt1=0`  
`ADTarType1=12`  
`ADTarBegHP1=100`  
`ADTarEndHP1=0`  
`ADSpellCastonResist1=`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=FALSE`  
`ADPreCondition1=TRUE`  
  
`ADGem2=5`  
`ADSpell2=Aria of the Artist`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2= ADhaste`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=0`  
`ADSpellDelay2=0`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=100`  
`ADTarEndHP2=0`  
`ADSpellCastonResist2=`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=FALSE`  
`ADPreCondition2=TRUE`  
  
`ADGem3=6`  
`ADSpell3a=Psalm of Veeshan`  
`ADSpell3=War March of Meldrath`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3= ADresbuff`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=100`  
`ADTarEndHP3=0`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=FALSE`  
`ADPreCondition3=TRUE`  
  
`ADGem4=1`  
`ADSpell4=Tjudawos' Chant of Flame`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=fdot`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=0`  
`ADTarType4=1`  
`ADTarBegHP4=100`  
`ADTarEndHP4=0`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=FALSE`  
`ADPreCondition4=TRUE`  
  
`ADGem5=2`  
`ADSpell5=Zeixshi-Kar's Chant of Frost`  
`ADSpell5a=Psalm of Veeshan`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=cdot`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=0`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=100`  
`ADTarEndHP5=0`  
`ADSpellCastonResist5=`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=FALSE`  
`ADPreCondition5=TRUE`  
  
`ADGem6=1`  
`ADSpell6=Severilous' Chant of Poison`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=pdot`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=100`  
`ADTarEndHP6=0`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=FALSE`  
`ADPreCondition6=TRUE`  
  
`ADGem7=8`  
`ADSpell7=Dirge of Metala`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=bsnare`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=0`  
`ADTarType7=1`  
`ADTarBegHP7=100`  
`ADTarEndHP7=0`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=FALSE`  
`ADPreCondition7=TRUE`  
  
`ADGem8=3`  
`ADSpell8=Requiem of Time`  
`ADSpellFoci8=`  
`ADDurMod8=0`  
`ADSpellAlias8=bslow`  
`ADAnnounce8=/bc`  
`ADSpellMinMana8=0`  
`ADSpellRecast8=0`  
`ADSpellCastonResist8=`  
`ADSpellDelay8=0`  
`ADTarCnt8=0`  
`ADTarType8=1`  
`ADTarBegHP8=100`  
`ADTarEndHP8=0`  
`ADIfSpellImmune8=`  
`ADUseHoTT8=FALSE`  
`ADPreCondition8=TRUE`  
  
`ADGem9=3`  
`ADSpell9=Zuriki's Song of Shenanigans`  
`ADSpellFoci9=`  
`ADDurMod9=0`  
`ADSpellAlias9=baeslow`  
`ADAnnounce9=/bc`  
`ADSpellMinMana9=0`  
`ADSpellRecast9=0`  
`ADSpellCastonResist9=`  
`ADSpellDelay9=0`  
`ADTarCnt9=0`  
`ADTarType9=1`  
`ADTarBegHP9=100`  
`ADTarEndHP9=0`  
`ADIfSpellImmune9=`  
`ADUseHoTT9=FALSE`  
`ADPreCondition9=TRUE`  
  
`ADGem10=3`  
`ADSpell10=Bellow of Chaos`  
`ADSpellFoci10=`  
`ADDurMod10=0`  
`ADSpellAlias10=dd`  
`ADAnnounce10=/bc`  
`ADSpellMinMana10=0`  
`ADSpellRecast10=0`  
`ADSpellCastonResist10=`  
`ADSpellDelay10=0`  
`ADTarCnt10=0`  
`ADTarType10=1`  
`ADTarBegHP10=100`  
`ADTarEndHP10=0`  
`ADIfSpellImmune10=`  
`ADUseHoTT10=FALSE`  
`ADPreCondition10=TRUE`  
  
`ADGem11=alt`  
`ADSpell11=Boastful Bellow`  
`ADSpellFoci11=`  
`ADDurMod11=0`  
`ADSpellAlias11= ADd`  
`ADAnnounce11=/bc`  
`ADSpellMinMana11=0`  
`ADSpellRecast11=0`  
`ADSpellCastonResist11=`  
`ADSpellDelay11=0`  
`ADTarCnt11=1`  
`ADTarType11=1`  
`ADTarBegHP11=95`  
`ADTarEndHP11=0`  
`ADIfSpellImmune11=`  
`ADUseHoTT11=FALSE`  
`ADPreCondition11=TRUE`  
  
`ADGem12=alt`  
`ADSpell12=F ADing Memories`  
`ADSpellFoci12=`  
`ADDurMod12=0`  
`ADSpellAlias12=f ADe`  
`ADAnnounce12=/bc`  
`ADSpellMinMana12=0`  
`ADSpellRecast12=0`  
`ADSpellCastonResist12=`  
`ADSpellDelay12=0`  
`ADTarCnt12=0`  
`ADTarType12=1`  
`ADTarBegHP12=90`  
`ADTarEndHP12=0`  
`ADIfSpellImmune12=`  
`ADUseHoTT12=FALSE`  
`ADPreCondition12=TRUE`  
  
`ADGem13=alt`  
`ADSpell13=Dance of Bl ADes`  
`ADSpellFoci13=`  
`ADDurMod13=0`  
`ADSpellAlias13=dbl ADes`  
`ADAnnounce13=/bc`  
`ADSpellMinMana13=0`  
`ADSpellRecast13=0`  
`ADSpellCastonResist13=`  
`ADSpellDelay13=0`  
`ADTarCnt13=1`  
`ADTarType13=1`  
`ADTarBegHP13=95`  
`ADTarEndHP13=0`  
`ADIfSpellImmune13=`  
`ADUseHoTT13=FALSE`  
`ADPreCondition13=TRUE`  
  
`ADGem14=alt`  
`ADSpell14=Song of Stone`  
`ADSpellFoci14=`  
`ADDurMod14=0`  
`ADSpellAlias14=pets`  
`ADAnnounce14=/bc`  
`ADSpellMinMana14=0`  
`ADSpellRecast14=0`  
`ADSpellCastonResist14=`  
`ADSpellDelay14=0`  
`ADTarCnt14=1`  
`ADTarType14=1`  
`ADTarBegHP14=95`  
`ADTarEndHP14=0`  
`ADIfSpellImmune14=`  
`ADUseHoTT14=FALSE`  
`ADPreCondition14=TRUE`  
  
`ADGem15=alt`  
`ADSpell15=Cacophony`  
`ADSpellFoci15=`  
`ADDurMod15=0`  
`ADSpellAlias15=idot`  
`ADAnnounce15=/bc`  
`ADSpellMinMana15=0`  
`ADSpellRecast15=0`  
`ADSpellCastonResist15=`  
`ADSpellDelay15=0`  
`ADTarCnt15=1`  
`ADTarType15=1`  
`ADTarBegHP15=95`  
`ADTarEndHP15=0`  
`ADIfSpellImmune15=`  
`ADUseHoTT15=FALSE`  
`ADPreCondition15=TRUE`  
  
`ADGem16=alt`  
`ADSpell16=Funeral Dirge`  
`ADSpellFoci16=`  
`ADDurMod16=0`  
`ADSpellAlias16=fdirge`  
`ADAnnounce16=/bc`  
`ADSpellMinMana16=0`  
`ADSpellRecast16=0`  
`ADSpellCastonResist16=`  
`ADSpellDelay16=0`  
`ADTarCnt16=1`  
`ADTarType16=1`  
`ADTarBegHP16=95`  
`ADTarEndHP16=0`  
`ADIfSpellImmune16=`  
`ADUseHoTT16=FALSE`  
`ADPreCondition16=TRUE`  
  
`ADGem17=alt`  
`ADSpell17=Fierce Eye`  
`ADSpellFoci17=`  
`ADDurMod17=0`  
`ADSpellAlias17=fierce`  
`ADAnnounce17=/bc`  
`ADSpellMinMana17=0`  
`ADSpellRecast17=0`  
`ADSpellCastonResist17=`  
`ADSpellDelay17=0`  
`ADTarCnt17=1`  
`ADTarType17=1`  
`ADTarBegHP17=80`  
`ADTarEndHP17=0`  
`ADIfSpellImmune17=`  
`ADUseHoTT17=FALSE`  
`ADPreCondition17=TRUE`  
  
`ADGem18=alt`  
`ADSpell18=Dirge of the Sleepwalker`  
`ADSpellFoci18=`  
`ADDurMod18=0`  
`ADSpellAlias18=dirgesleep`  
`ADAnnounce18=/bc`  
`ADSpellMinMana18=0`  
`ADSpellRecast18=0`  
`ADSpellCastonResist18=`  
`ADSpellDelay18=0`  
`ADTarCnt18=0`  
`ADTarType18=1`  
`ADTarBegHP18=99`  
`ADTarEndHP18=0`  
`ADIfSpellImmune18=`  
`ADUseHoTT18=FALSE`  
`ADPreCondition18=TRUE`  
  
`ADGem19=alt`  
`ADSpell19=Quick Time`  
`ADSpellFoci19=`  
`ADDurMod19=0`  
`ADSpellAlias19=haste3`  
`ADAnnounce19=/bc`  
`ADSpellMinMana19=0`  
`ADSpellRecast19=0`  
`ADSpellCastonResist19=`  
`ADSpellDelay19=0`  
`ADTarCnt19=1`  
`ADTarType19=1`  
`ADTarBegHP19=99`  
`ADTarEndHP19=0`  
`ADIfSpellImmune19=`  
`ADUseHoTT19=FALSE`  
`ADPreCondition19=TRUE`  
  
`[AdvBuff]`  
`ABCount=16`  
`ABMobMax=18`  
`ABCheckTime=5`  
`ABProactive=TRUE`  
  
`ABGem1=6`  
`ABSpell1=War March of Meldrath`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=bhaste`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=0`  
`ABTarType1=brd cbt idle`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
`ABPreCondition1=TRUE`  
  
`ABGem2=6`  
`ABSpell2=Psalm of Veeshan`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=resbuff`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=brd`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=7`  
`ABSpell3=Cantata of Restoration`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=reg`  
`ABAnnounce3=`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=brd`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=Alt`  
`ABSpell4=Selo's Sonata`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=selo`  
`ABAnnounce4=`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=brd cbt idle`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=item`  
`ABSpell5=Singing Steel Boots`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=lev`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=0`  
`ABTarType5=brd`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=item`  
`ABSpell6=Thicker Leather Apron`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=selfac`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=1`  
`ABTarType6=self`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=8`  
`ABSpell7=Selo's Song of Travel`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=tselo`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=brd`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=8`  
`ABSpell8=Song of Highsun`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=hisun`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=0`  
`ABTarCnt8=0`  
`ABTarType8=brd`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=8`  
`ABSpell9=Luvwen's Aria of Serenity`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=bcalm`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=0`  
`ABTarType9=brd`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=8`  
`ABSpell10=Shauri's Sonorous Clouding`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=invis`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=0`  
`ABTarCnt10=0`  
`ABTarType10=brd`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=item`  
`ABSpell11=Corrigible Chain of Dogmatic Embrace`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=selfrune`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=1`  
`ABTarType11=self brd `  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=10`  
`ABSpell12=Aura of Insight`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=aura`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=1`  
`ABTarType12=aura self brd `  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=item`  
`ABSpell13=Darkened Mask of Deception`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=illde`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=0`  
`ABTarCnt13=0`  
`ABTarType13=self brd `  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Assassin's Earpiece`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=selfregen`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=1`  
`ABTarType14=self brd `  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`ABGem15=item`  
`ABSpell15=Flowing Black Silk Sash`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=overhaste`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=1`  
`ABTarType15=self brd `  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
`ABPreCondition15=TRUE`  
  
`ABGem16=item`  
`ABSpell16=Crown of the Froglok Kings`  
`ABSpellFoci16=`  
`ABDurMod16=0`  
`ABSpellAlias16=selfres`  
`ABAnnounce16=/bc`  
`ABSpellMinMana16=0`  
`ABTarCnt16=1`  
`ABTarType16=self brd `  
`ABRecast16=FALSE`  
`ABSpellIcon16=`  
`ABPreCondition16=TRUE`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[AdvEvent]`  
`AECount=0`  
`AECustom1=Greater Bloodmoon Healing`  
`AECustom2=`  
`AECustom3=`  
  
`[AdvPull]`  
`APBefore=`  
`APAfter=`  
`APMobMax=4`  
`APScript=Pull`  
`APPath=`  
`APCheckTime=30`  
`APRadius=149`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[Script-AECustomEvent1]`  
`Commands=1`  
`C1=/mb cast bmez `  
  
`[Script-Pull]`  
`Commands=1`  
`C1=/call CastCall {Me.CleanName} `*`cast`` ``pull`` ``{Target.ID}`*  
  
`[Script-Defense]`  
`Commands=0`  
`C1=/return`

## Level 89

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=FALSE `  
`DoBuffs=TRUE `  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoPet=FALSE `  
`DoSit=FALSE `  
`DoLoot=FALSE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`DoAfk=FALSE `  
`MasterList=${NetBots.Client}`  
`TankName=TankName`  
`Radius=75 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Not now, thanks `  
`FollowDistance=20 `  
`FollowStick=20 hold uw `  
`PetAggro=FALSE `  
`PetAssist=0 `  
`DoMount=FALSE `  
`DoPull=FALSE `  
`DoCures=FALSE `  
`DeathSlot=FALSE `  
`DoAura=TRUE`  
`AuraCast=Aura of Renewal|gem4`  
`ForageIni=forage.ini `  
`PetShrink=TRUE`  
  
`[Melee] `  
`OffTank=FALSE `  
`ACLeash=50 `  
`ACAssistPct=98`  
`ACManaPct=1 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 melee=200 enrage=1 infuriate=1 range=0 standup=1 `  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff] `  
`ADCount=9`  
`ADMobMax=18 `  
`ADCheckTime=0 `  
`ADAggroOnly=1`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff| `  
  
`ADGem1=9`  
`ADSpell1=Wave of Slumber`  
`ADDurMod1=0`  
`ADSpellAlias1=AEMez`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellDelay1=0`  
`ADTarCnt1=3`  
`ADTarType1=12`  
`ADTarBegHP1=200`  
`ADTarEndHP1=0`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=8`  
`ADSpell2=Slumber of Sionachie`  
`ADDurMod2=0`  
`ADSpellAlias2=Mez`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=0`  
`ADSpellDelay2=0`  
`ADTarCnt2=2`  
`ADTarType2=12`  
`ADTarBegHP2=200`  
`ADTarEndHP2=0`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=7`  
`ADSpell3=Largo's Assonant Binding`  
`ADDurMod3=0`  
`ADSpellAlias3=Snare`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=0`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=98`  
`ADTarEndHP3=0`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=1`  
`ADSpell4=War March of Dagda`  
`ADDurMod4=0`  
`ADSpellAlias4=ADHaste`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=98`  
`ADTarEndHP4=0`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=2`  
`ADSpell5=Dirge of Dreams`  
`ADDurMod5=0`  
`ADSpellAlias5=ADProtect`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=0`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=98`  
`ADTarEndHP5=0`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=5`  
`ADSpell6=Aria of the Composer`  
`ADDurMod6=0`  
`ADSpellAlias6=NukeBuff`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=98`  
`ADTarEndHP6=0`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=6`  
`ADSpell7=Pulse of Renewal`  
`ADDurMod7=0`  
`ADSpellAlias7=HealBuff`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellDelay7=0`  
`ADTarCnt7=1`  
`ADTarType7=1`  
`ADTarBegHP7=98`  
`ADTarEndHP7=0`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`ADGem8=3`  
`ADSpell8=Noira's Song of Suffering`  
`ADDurMod8=0`  
`ADSpellAlias8=WeapProc`  
`ADAnnounce8=/bc`  
`ADSpellMinMana8=0`  
`ADSpellRecast8=0`  
`ADSpellDelay8=0`  
`ADTarCnt8=1`  
`ADTarType8=1`  
`ADTarBegHP8=98`  
`ADTarEndHP8=0`  
`ADUseHoTT8=0`  
`ADPreCondition8=TRUE`  
  
`ADGem9=10`  
`ADSpell9=Shiverback's Chant of Disease`  
`ADDurMod9=0`  
`ADSpellAlias9=DOT`  
`ADAnnounce9=/bc`  
`ADSpellMinMana9=0`  
`ADSpellRecast9=0`  
`ADSpellDelay9=0`  
`ADTarCnt9=1`  
`ADTarType9=1`  
`ADTarBegHP9=98`  
`ADTarEndHP9=0`  
`ADUseHoTT9=0`  
`ADPreCondition9=TRUE`  
  
`[AdvBuff] `  
`ABCount=6`  
`ABMobMax=12 `  
`ABCheckTime=8 `  
`ABProactive=TRUE`  
  
`ABGem1=1`  
`ABSpell1=War March of Dagda`  
`ABDurMod1=0`  
`ABSpellAlias1=Haste`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=brd cbt idle`  
`ABRecast1=FALSE`  
`ABPreCondition1=TRUE`  
  
`ABGem2=2`  
`ABSpell2=Dirge of Dreams`  
`ABDurMod2=0`  
`ABSpellAlias2=Protect`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=1`  
`ABTarType2=brd`  
`ABRecast2=FALSE`  
`ABPreCondition2=TRUE`  
  
`ABGem3=4`  
`ABSpell3=Chorus of Renewal`  
`ABDurMod3=0`  
`ABSpellAlias3=Regen`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=brd`  
`ABRecast3=FALSE`  
`ABPreCondition3=TRUE`  
  
`ABGem4=item`  
`ABSpell4=Paragon's Ear Stud of the Combatant`  
`ABDurMod4=0`  
`ABSpellAlias4=might`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=TRUE`  
`ABPreCondition4=TRUE`  
  
`ABGem5=item`  
`ABSpell5=Paragon's Earring of the Combatant`  
`ABDurMod5=0`  
`ABSpellAlias5=puff`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=self`  
`ABRecast5=TRUE`  
`ABPreCondition5=TRUE`  
  
`ABGem6=item`  
`ABSpell6=Band of Woven Straw`  
`ABDurMod6=0`  
`ABSpellAlias6=form`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=1`  
`ABTarType6=self`  
`ABRecast6=TRUE`  
`ABPreCondition6=TRUE`  
  
`[AdvCure] `  
`AQCount=0 `  
  
`[AdvEvent] `  
`AECount=0`  
  
`[AdvPull] `  
`APMobMax=4 `  
`APCheckTime=30 `  
`APRadius=149 `  
`APRetries=1`

## Level 100

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=TRUE`  
`DoPull=FALSE`  
`DoPet=FALSE`  
`DoSit=FALSE`  
`DoLoot=TRUE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`PetShrink=FALSE`  
`PetShrinkSpell=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=98`  
`ACManaPct=1`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1 melee=200 enrage=1 infuriate=1 range=0 standup=1 `  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=9`  
`ADMobMax=20`  
`ADCheckTime=0`  
`ADAggroOnly=1`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=9`  
`ADSpell1=Wave of Quietude`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=AEMez`  
`ADAnnounce1=/bc`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=0`  
`ADSpellCastonResist1=`  
`ADSpellDelay1=0`  
`ADTarCnt1=3`  
`ADTarType1=12`  
`ADTarBegHP1=200`  
`ADTarEndHP1=0`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=8`  
`ADSpell2=Slumber of Motlak`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=Mez`  
`ADAnnounce2=/bc`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=0`  
`ADSpellCastonResist2=`  
`ADSpellDelay2=0`  
`ADTarCnt2=2`  
`ADTarType2=12`  
`ADTarBegHP2=200`  
`ADTarEndHP2=0`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=7`  
`ADSpell3=Corpseflower's Assonant Binding`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=snare`  
`ADAnnounce3=/bc`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=98`  
`ADTarEndHP3=0`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=1`  
`ADSpell4=War March of Protan`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=ADHaste`  
`ADAnnounce4=/bc`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=98`  
`ADTarEndHP4=0`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=2`  
`ADSpell5=Dirge of Dreams`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=ADProtect`  
`ADAnnounce5=/bc`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=98`  
`ADTarEndHP5=0`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=5`  
`ADSpell6=Aria of Va'Ker`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=NukeBuff`  
`ADAnnounce6=/bc`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=98`  
`ADTarEndHP6=0`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=6`  
`ADSpell7=Pulse of Salarra`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=HealBuff`  
`ADAnnounce7=/bc`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=1`  
`ADTarType7=1`  
`ADTarBegHP7=98`  
`ADTarEndHP7=0`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`ADGem8=3`  
`ADSpell8=Kaficus' Spiteful Lyric`  
`ADSpellFoci8=`  
`ADDurMod8=0`  
`ADSpellAlias8=WeapProc`  
`ADAnnounce8=/bc`  
`ADSpellMinMana8=0`  
`ADSpellRecast8=0`  
`ADSpellCastonResist8=`  
`ADSpellDelay8=0`  
`ADTarCnt8=1`  
`ADTarType8=1`  
`ADTarBegHP8=98`  
`ADTarEndHP8=0`  
`ADIfSpellImmune8=`  
`ADUseHoTT8=0`  
`ADPreCondition8=TRUE`  
  
`ADGem9=10`  
`ADSpell9=Gosik's Chant of Flame`  
`ADSpellFoci9=`  
`ADDurMod9=0`  
`ADSpellAlias9=DOT`  
`ADAnnounce9=/bc`  
`ADSpellMinMana9=0`  
`ADSpellRecast9=0`  
`ADSpellCastonResist9=`  
`ADSpellDelay9=0`  
`ADTarCnt9=1`  
`ADTarType9=1`  
`ADTarBegHP9=98`  
`ADTarEndHP9=0`  
`ADIfSpellImmune9=`  
`ADUseHoTT9=0`  
`ADPreCondition9=TRUE`  
  
`[AdvBuff]`  
`ABCount=15`  
`ABMobMax=18`  
`ABCheckTime=8`  
  
`ABGem1=4`  
`ABSpell1=Aura of Salarra`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=self aura`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=aura`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
`ABPreCondition1=TRUE`  
  
`ABGem2=1`  
`ABSpell2=War March of Protan`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=Haste`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=1`  
`ABTarType2=brd cbt idle`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=2`  
`ABSpell3=Dirge of Dreams`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=Protect`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=brd cbt idle`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=6`  
`ABSpell4=Pulse of Salarra`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=Regen`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=brd cbt idle`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=item`  
`ABSpell5=Guggles' Mangy Hide`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=spikes`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=self`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=item`  
`ABSpell6=Archon Insignia Hoop`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=breath`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=self`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=item`  
`ABSpell7=Azure Stud of the Breeze`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=might`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=1`  
`ABTarType7=self`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=item`  
`ABSpell8=Face of Dread`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=end`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=0`  
`ABTarCnt8=1`  
`ABTarType8=self`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=item`  
`ABSpell9=Mindlock's Seal of Memories`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=past`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=item`  
`ABSpell10=Moonstone Band of the Dark`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=ihaste`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=0`  
`ABTarCnt10=1`  
`ABTarType10=self`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=item`  
`ABSpell11=Glowing Spaulders of Torture`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=dodge`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=1`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=item`  
`ABSpell12=Wavecrasher's Raw-Hide Belt`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=mind`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=1`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=item`  
`` ABSpell13=Il`Valrikar's Verdant Orb of Life ``  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=ward`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=0`  
`ABTarCnt13=1`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Ring of the Ancients`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=shrink`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=0`  
`ABTarType14=self`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`ABGem15=item`  
`ABSpell15=Polymorph Wand: Siren Sorceress`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=illusion`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=0`  
`ABTarType15=self`  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
`ABPreCondition15=TRUE`  
  
`[AdvEvent]`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=4`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`

# Rogue

## Mid Level Rogue

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=FALSE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPet=FALSE`  
`DoSit=FALSE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`MasterList=`  
`TankName=`  
`ExcludeList=a dusty barrel|a dark coffin|a bitten victim|a hollow tree|                                                       `  
`Radius=50`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=`  
`PetAggro=FALSE`  
`DoMount=FALSE`  
`MountCast=`  
`DoPull=FALSE`  
`DoCures=FALSE`  
`DeathSlot=chest`  
`DoAura=FALSE`  
`AuraCast=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=99`  
`ACManaPct=0`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1 pickpocket=0 melee=200 range=0 stickrange=200 resume=20 disarm=1 evade=0 facing=1 hide=0 sneak=0 backstab=50 enrage=1`  
`ACBefore=/if ({ACMATarget} && {Spawn[{ACMATarget}].Distance3D}<={ACLeash} && {Me.CombatAbilityReady[Sneak Attack]} && {Me.Invis} && {Me.Sneaking} && {Me.PctEndurance}>40 && !{Me.Moving}) /call mbscript SneakAttack`  
`ACAfter=/if (!{ADMobCount} && {DoLoot} && {LootMobs}) /call LootMobs`  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=0`  
`ADMobMax=18`  
`ADCheckTime=0`  
  
`[AdvBuff]`  
`ABCount=2`  
`ABMobMax=12`  
`ABCheckTime=2s`  
`ABProactive=TRUE`  
  
`ABGem1=script`  
`ABSpell1=HideSneak`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=hidesneak`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=self cbt idle`  
  
`ABGem2=item`  
`ABSpell2=Mrylokar's Helm`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=uv`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=0`  
`ABTarCnt2=1`  
`ABTarType2=self`  
  
`[AdvEvent]`  
`AECount=0`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APMobMax=1`  
`APScript=Pull`  
`APBefore=`  
`APAfter=`  
`APRangedMod=0`  
  
`[Script-makecamp]`  
`Commands=5`  
`C1=/bc Trying to find a sweet spot /evilgrin`  
`C2=/multiline ; /delay 7;/stick off;/tar {TankName}`  
`C3=/multiline ; /delay 2s;/stick 3 behindonce`  
`C4=/multiline ; /delay 12;/stick off;/keypress back hold`  
`C5=/multiline ; /keypress back;/varset FollowFlag 0;/makecamp on;/varset MakeCampX {Me.X};/varset MakeCampY {Me.Y};/varset CampStatus 1;/if (!{DoLoot}) /mb doloot on`  
  
`[Script-lfsell]`  
`Commands=3`  
`C1=/varset Timer 10m`  
`C2=/call mbwayplay ldon b f`  
`C3=/mb follow {FollowName}`  
  
`[Script-lfpull]`  
`Commands=2`  
`C1=/varset Timer 3m`  
`C2=/call mbwayplay lfpull b`  
  
`[Script-HideSneak]`  
`Commands=4`  
`C1=/if ({FollowFlag} && {Me.Sneaking}) /doability sneak`  
`C2=/if (!{FollowFlag} && !{ACState} && !{ACMATarget} && !{MiscCheckTimer}<10 && {Select[{MakeCamp},on]} && {Me.AbilityReady[Hide]} && !{Me.Moving} && !{Melee.Combat}) /multiline ; /doability Hide;/delay 5`  
`C3=/if (!{FollowFlag} && !{ACState} && !{ACMATarget} && !{MiscCheckTimer}<10 && {Select[{MakeCamp},on]} && {Me.AbilityReady[Sneak]} && !{Me.AbilityReady[Hide]} && !{Me.Moving} && !{Melee.Combat} && {Me.Invis}) /multiline ; /doability Sneak;/delay 5`  
`C4=/if ({ACState} && {ACMATarget}=={Target.ID} && !{Me.Moving} && {Me.AbilityReady[Backstab]} && !{ACMobProb}) /varset ACMobProb 1`  
  
`[Script-SneakAttack]`  
`Commands=11`  
`C1=/if ({Melee.Enable}) /melee plugin=0`  
`C2=/if (!{Melee.Enable} && {Timer}<5) /multiline ; /melee plugin=1;/return`  
`C3=/if ({Me.CombatAbilityReady[Sneak Attack]}) /keypress 8`  
`C4=/if (!{Me.Moving} && !{Stick.MoveBehind} && {Stick.Distance}<={Math.Calc[{Spawn[{ACMATarget}].MaxRangeTo}]}) /stick {Math.Calc[{Spawn[{ACMATarget}].MaxRangeTo}-2]} hold behind id {ACMATarget}`  
`C5=/if ({Target.ID}!={ACMATarget}) /multiline ; /target id {ACMATarget};/delay 5`  
`C6=/if ({Melee.BackAngle}>60 || {Melee.BackAngle}<-60) /goto :Top`  
`C7=/if ({Target.Distance3D}>={Spawn[{ACMATarget}].MaxRangeTo}-2) /stick {Math.Calc[{Spawn[{ACMATarget}].MaxRangeTo}-5]} hold behind id {ACMATarget}`  
`C8=/if ({Target.Distance3D}>={Spawn[{ACMATarget}].MaxRangeTo}-3) /goto :Top`  
`C9=/delay 5`  
`C10=/if ({Me.AbilityReady[Backstab]}) /doability backstab`  
`C11=/melee plugin=1`  
  
`[Script-Pull]`  
`Commands=1`  
`C1=/if ({Target.ID}) /doability ''Throw Stone''`

## Level 85 Rogue

Courtesy of Bartab. Posted 4/18/09.

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=TRUE `  
`DoBuffs=FALSE `  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoCures=FALSE `  
`DoPull=FALSE `  
`DoPet=FALSE `  
`DoSit=FALSE `  
`DoLoot=FALSE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`ForageIni=forage.ini `  
`DoAfk=TRUE `  
`DoMount=FALSE `  
`MountCast= `  
`MasterList=${NetBots.Client} `  
`TankName= `  
`Radius=200 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Esquire for hire with total rapid fire. Supplier to any Tom Dick Jerry Maguire. You chose the right man to get the plan executed. I get the situation happening before you shoot it `  
`DeathSlot=FALSE `  
`FollowDistance=20 `  
`FollowStick=20 hold uw `  
`NetworkINI=MBini/MB_network.ini `  
`TraderName= `  
  
`[Melee] `  
`OffTank=FALSE `  
`ACLeash=100 `  
`ACAssistPct=97 `  
`ACManaPct=70 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 `  
`ACBefore= `  
`ACAfter= `  
  
`[AdvHeal] `  
`AHCount=0 `  
  
`[AdvDebuff] `  
`ADCount=2 `  
`ADMobMax=100 `  
`ADCheckTime=0 `  
`ADAggroOnly=0 `  
`ADHold=0|1|1|`  
  
`ADGem1=alt `  
`ADSpell1=Ligament Slice `  
`ADSpellFoci1= `  
`ADDurMod1=0 `  
`ADSpellAlias1=deb `  
`ADAnnounce1=/bc `  
`ADSpellMinMana1=0 `  
`ADSpellRecast1=0 `  
`ADSpellCastonResist1= `  
`ADSpellDelay1=0 `  
`ADTarCnt1=0 `  
`ADTarType1=1 `  
`ADTarBegHP1=95 `  
`ADTarEndHP1=85 `  
`ADIfSpellImmune1= `  
`ADUseHoTT1=0 `  
`ADPreCondition1=TRUE`  
  
`ADGem2=potionbelt`  
`ADSpell2=Mugger's Sap `  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2=sapkt `  
`ADAnnounce2=/bc `  
`ADSpellMinMana2=0 `  
`ADSpellRecast2=0 `  
`ADSpellCastonResist2= `  
`ADSpellDelay2=0 `  
`ADTarCnt2=1 `  
`ADTarType2=1 `  
`ADTarBegHP2=95 `  
`ADTarEndHP2=0 `  
`ADIfSpellImmune2= `  
`ADUseHoTT2=0 `  
`ADPreCondition2=/if ({Target.Body.Name.Equal[Humanoid]}) /return TRUE`  
  
`[AdvBuff] `  
`ABCount=14 `  
`ABMobMax=12 `  
`ABCheckTime=8 `  
`ABProactive=TRUE`  
  
`ABGem1=item`  
`ABSpell1=Nightshade, Blade of Entropy `  
`ABSpellFoci1= `  
`ABDurMod1=0 `  
`ABSpellAlias1=epic `  
`ABAnnounce1=/bc `  
`ABSpellMinMana1=0 `  
`ABTarCnt1=1 `  
`ABTarType1=cbt `  
`ABRecast1=FALSE `  
`ABSpellIcon1=`  
  
`ABGem2=item`  
`ABSpell2=Hanvar's Hoop `  
`ABSpellFoci2= `  
`ABDurMod2=0 `  
`ABSpellAlias2= `  
`ABAnnounce2= `  
`ABSpellMinMana2=0 `  
`ABTarCnt2=1 `  
`ABTarType2=self `  
`ABRecast2=FALSE `  
`ABSpellIcon2= `  
  
`ABGem3=item `  
`ABSpell3=Desiccated Halfling Mask `  
`ABSpellFoci3= `  
`ABDurMod3=0 `  
`ABSpellAlias3=illuHFL `  
`ABAnnounce3= `  
`ABSpellMinMana3=0 `  
`ABTarCnt3=0 `  
`ABTarType3=self `  
`ABRecast3=FALSE `  
`ABSpellIcon3=`  
  
`ABGem4=item `  
`ABSpell4=Guise of the Hunter `  
`ABSpellFoci4= `  
`ABDurMod4=0 `  
`ABSpellAlias4=illuVAH `  
`ABAnnounce4= `  
`ABSpellMinMana4=0 `  
`ABTarCnt4=0 `  
`ABTarType4=self `  
`ABRecast4=FALSE `  
`ABSpellIcon4=`  
  
`ABGem5=item `  
`ABSpell5=Flayed Barbarian Hide Mask `  
`ABSpellFoci5= `  
`ABDurMod5=0 `  
`ABSpellAlias5=illuBAR `  
`ABAnnounce5= `  
`ABSpellMinMana5=0 `  
`ABTarCnt5=0 `  
`ABTarType5=self `  
`ABRecast5=FALSE `  
`ABSpellIcon5=`  
  
`ABGem6=item `  
`ABSpell6=Mask of Obtenebration `  
`ABSpellFoci6= `  
`ABDurMod6=0 `  
`ABSpellAlias6=illuERU `  
`ABAnnounce6= `  
`ABSpellMinMana6=0 `  
`ABTarCnt6=0 `  
`ABTarType6=self `  
`ABRecast6=FALSE `  
`ABSpellIcon6=`  
  
`ABGem7=item `  
`ABSpell7=Mask of Deception `  
`ABSpellFoci7= `  
`ABDurMod7=0 `  
`ABSpellAlias7=illuDEF `  
`ABAnnounce7= `  
`ABSpellMinMana7=0 `  
`ABTarCnt7=0 `  
`ABTarType7=self `  
`ABRecast7=FALSE `  
`ABSpellIcon7=`  
  
`ABGem8=item `  
`ABSpell8=Burnoose of the Halfbreed `  
`ABSpellFoci8= `  
`ABDurMod8=0 `  
`ABSpellAlias8=illuHEF `  
`ABAnnounce8= `  
`ABSpellMinMana8=0 `  
`ABTarCnt8=0 `  
`ABTarType8=self `  
`ABRecast8=FALSE `  
`ABSpellIcon8=`  
  
`ABGem9=item`  
`ABSpell9=Iksar Hide Mask `  
`ABSpellFoci9= `  
`ABDurMod9=0 `  
`ABSpellAlias9=illuIKS `  
`ABAnnounce9= `  
`ABSpellMinMana9=0 `  
`ABTarCnt9=0 `  
`ABTarType9=self `  
`ABRecast9=FALSE `  
`ABSpellIcon9=`  
  
`ABGem10=item `  
`ABSpell10=Direwolf Totem of Battle `  
`ABSpellFoci10= `  
`ABDurMod10=0 `  
`ABSpellAlias10=atkbuff `  
`ABAnnounce10=/bc `  
`ABSpellMinMana10=0 `  
`ABTarCnt10=0 `  
`ABTarType10=self `  
`ABRecast10=FALSE `  
`ABSpellIcon10=`  
  
`ABGem11=item`  
`ABSpell11=Girdle of Solusek Ro `  
`ABSpellFoci11= `  
`ABDurMod11=0 `  
`ABSpellAlias11=ovhaste `  
`ABAnnounce11= `  
`ABSpellMinMana11=0 `  
`ABTarCnt11=1 `  
`ABTarType11=self `  
`ABRecast11=FALSE `  
`ABSpellIcon11=`  
  
`ABGem12=item `  
`ABSpell12=Dragonscar Facemask `  
`ABSpellFoci12= `  
`ABDurMod12=0 `  
`ABSpellAlias12=endu `  
`ABAnnounce12= `  
`ABSpellMinMana12=0 `  
`ABTarCnt12=1 `  
`ABTarType12=self `  
`ABRecast12=FALSE `  
`ABSpellIcon12=`  
  
`ABGem13=item `  
`ABSpell13=Silvered Earstud of the Sanguine `  
`ABSpellFoci13= `  
`ABDurMod13=0 `  
`ABSpellAlias13=ovatk `  
`ABAnnounce13= `  
`ABSpellMinMana13=0 `  
`ABTarCnt13=1 `  
`ABTarType13=self `  
`ABRecast13=FALSE `  
`ABSpellIcon13=`  
  
`ABGem14=script `  
`ABSpell14=summugger `  
`ABSpellFoci14= `  
`ABDurMod14=0 `  
`ABSpellAlias14=summugger `  
`ABAnnounce14= `  
`ABSpellMinMana14=20 `  
`ABTarCnt14=1 `  
`ABTarType14=self `  
`ABRecast14=FALSE `  
`ABSpellIcon14=`  
  
`[AdvEvent] `  
`AECount=0 `  
`AECustom1=41485616.00340526 `  
`AECustom2=188739616.00489387 `  
`AECustom3=988488616.00710173 `  
  
`[AdvPull] `  
`APCheckTime=20 `  
`APRadius=10 `  
`APMobMax=40 `  
`APScript=pull `  
`APPath=sketch `  
`APBefore= `  
`APAfter= `  
`APAnnounce=/bc `  
`APRetPath= `  
`APRetries=1 `  
  
`[AdvCure] `  
`AQCount=0 `  
  
`[Script-illu] `  
`Commands=8 `  
`C1=/if (!{Defined[CntBuff]}) /multiline ; /declare CntBuff int local ; /varset CntBuff 1 `  
`C2=/if (!{Defined[ClickedOff]}) /multiline ; /declare ClickedOff bool local ; /varset ClickedOff FALSE `  
`C3=/if (!{Defined[IlluCasted]}) /multiline ; /declare IlluCasted bool local ; /varset IlluCasted FALSE `  
`C4=/if ({CntBuff}>10 || {ClickedOff}) /multiline ; /varset IlluCasted TRUE ; /call CastCall {Me.CleanName} `*`cast`` ``{Param1}`*` `  
`C5=/if ({Me.Buff[{CntBuff}].Name.Find[Illusion]}==1) /multiline ; /notify BuffWindow Buff{Math.Calc[{CntBuff}-1].Int} leftmouseup ; /varset ClickedOff TRUE `  
`C6=/varcalc CntBuff {CntBuff}+1 `  
`C7=/if ({IlluCasted}) /return `  
`C8=/goto :Top`  
  
`[Script-pull] `  
`Commands=3 `  
`C1=/echo pull BEGIN `  
`C2=/ranged `  
`C3=/echo pull END `  
  
`[Script-summugger] `  
`Commands=3 `  
`C1=/if (!{FindItemCount[Mugger's Sap]}) /disc Procure Sap Rk. II `  
`C2=/if (!{FindItemCount[Mugger's Sap]}==0) /delay 1s {Me.Casting.ID} `  
`C3=/if (!{FindItemCount[Mugger's Sap]}==0) /delay 7s !{Me.Casting.ID}`

# Magician

## Level 65

These settings are currently working on the Progression servers as of 7/2/2012.

    [Settings]
    DoMelee=FALSE
    DoHeals=TRUE
    DoBuffs=FALSE
    DoDebuffs=FALSE
    DoEvents=FALSE
    DoCures=FALSE
    DoPull=FALSE
    DoPet=TRUE
    DoSit=TRUE
    DoLoot=FALSE
    DoFW=FALSE
    DoForage=FALSE
    ForageIni=forage.ini
    DoAfk=FALSE
    DoMount=FALSE
    MountCast=Brown Rope Bridle|Item
    MasterList=${NetBots.Client},Kukoc
    TankName=${Group.MainTank.Name}
    Radius=90
    SitAggroRadiusCheck=75
    AfkMessage=Not now, thanks
    DeathSlot=FALSE
    NetworkINI=
    TraderName=
    FollowDistance=20
    FollowStick=20 hold uw
    PetAggro=FALSE
    PetAssist=1
    PetFoci=
    PetShrink=FALSE
    PetShrinkSpell=
    [Melee]
    OffTank=FALSE
    ACLeash=70
    ACAssistPct=97
    ACManaPct=101
    ACAnnounce=
    ACMeleeCmd=/melee plugin=1
    ACBefore=
    ACAfter=
    [AdvHeal]
    AHCount=0
    [AdvDebuff]
    ADCount=2
    ADMobMax=50
    ADCheckTime=2
    ADAggroOnly=0
    ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|

    ADGem1=alt
    ADSpell1=Frenzied Burnout
    ADSpellFoci1=
    ADDurMod1=0
    ADSpellAlias1=burn
    ADAnnounce1=
    ADSpellMinMana1=0 
    ADSpellRecast1=3 
    ADSpellDelay1=3
    ADTarCnt1=3 
    ADTarType1=1 
    ADTarBegHP1=100
    ADTarEndHP1=70
    ADSpellCastonResist1=
    ADIfSpellImmune1=
    ADUseHoTT1=0
    ADPreCondition1=TRUE

    ADGem2=2
    ADSpell2=Black Steel
    ADSpellFoci2= 
    ADDurMod2=0
    ADSpellAlias2=nuke 
    ADAnnounce2=
    ADSpellMinMana2=00 
    ADSpellRecast2=3 
    ADSpellDelay2=3
    ADTarCnt2=1 
    ADTarType2=1 
    ADTarBegHP2=96
    ADTarEndHP2=10
    ADSpellCastonResist2=
    ADIfSpellImmune2=
    ADUseHoTT2=0
    ADPreCondition2=TRUE

    [AdvBuff]
    ABCount=5
    ABMobMax=18
    ABCheckTime=8

    ABGem1=7
    ABSpell1=Burnout IV
    ABSpellFoci1=
    ABDurMod1=0
    ABSpellAlias1=pethaste
    ABAnnounce1=/bc
    ABSpellMinMana1=0
    ABTarCnt1=1
    ABTarType1=mypet
    ABRecast1=FALSE
    ABSpellIcon1=
    ABPreCondition1=TRUE

    ABGem2=6
    ABSpell2=Flameshield of Ro
    ABSpellFoci2=
    ABDurMod2=0
    ABSpellAlias2=ds
    ABAnnounce2=/bc
    ABSpellMinMana2=0
    ABTarCnt2=1
    ABTarType2=tank
    ABRecast2=FALSE
    ABSpellIcon2=
    ABPreCondition2=TRUE

    ABGem3=5
    ABSpell3=Xegony's Phantasmal Guard
    ABSpellFoci3=
    ABDurMod3=0
    ABSpellAlias3=selfhp
    ABAnnounce3=/bc
    ABSpellMinMana3=0
    ABTarCnt3=1
    ABTarType3=self
    ABRecast3=FALSE
    ABSpellIcon3=
    ABPreCondition3=TRUE

    ABGem4=alt
    ABSpell4=Elemental Form: Water
    ABSpellFoci4=
    ABDurMod4=0
    ABSpellAlias4=water
    ABAnnounce4=/bc
    ABSpellMinMana4=0
    ABTarCnt4=0
    ABTarType4=self
    ABRecast4=FALSE
    ABSpellIcon4=
    ABPreCondition4=TRUE

    ABGem5=6
    ABSpell5=Ward of Xegony
    ABSpellFoci5=
    ABDurMod5=0
    ABSpellAlias5=pet
    ABAnnounce5=/bc
    ABSpellMinMana5=10
    ABTarCnt5=1
    ABTarType5=petspell
    ABRecast5=FALSE
    ABSpellIcon5=
    ABPreCondition5=TRUE

    [AdvEvent]
    AECustom1=
    AECustom2=
    AECustom3=
    AECount=0
    [AdvPull]
    APCheckTime=0
    APRadius=40
    APMobMax=1
    APScript=
    APPath=
    APRetPath=
    APBefore=
    APAfter=
    APAnnounce=
    APRetries=1
    [AdvCure]
    AQCount=0

## Level 75

Target the pet you want to give weapons to, and "/mb script PetKit" to summon and give weapons. No target defaults to
your own pet. Spells may need updated.

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Small White Drum|item`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now thanks`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Essence of Air|gem8`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=`  
`DoAura=FALSE`  
`Cast= |gem8`  
`AuraCast=`  
`ForageIni=forage.ini`  
`PetShrinkSpell=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=5`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=1`  
`AHCheckTime=2`  
`AHHealOOBC=FALSE`  
  
`AHGem1=7`  
`AHSpell1=Renewal of Aenda`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=10`  
`AHSpellAlias1=petheal`  
`AHAnnounce1=`  
`AHTarCnt1=1`  
`AHClass1=hp60 mypet`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`[AdvDebuff]`  
`ADCount=6`  
`ADMobMax=20`  
`ADCheckTime=2`  
  
`ADGem1=1`  
`ADSpell1=Mala`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=debmala`  
`ADAnnounce1=`  
`ADSpellMinMana1=10`  
`ADSpellRecast1=0`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=97`  
`ADTarEndHP1=20`  
  
`ADGem2=item`  
`ADSpell2=Summoned: Elemental Ice Sliver`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=sliver`  
`ADAnnounce2=`  
`ADSpellMinMana2=10`  
`ADSpellRecast2=0`  
`ADSpellDelay2=20`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=95`  
`ADTarEndHP2=20`  
  
`ADGem3=4`  
`ADSpell3=Blade Strike`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=mnuke`  
`ADAnnounce3=`  
`ADSpellMinMana3=10`  
`ADSpellRecast3=0`  
`ADSpellDelay3=5`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=90`  
`ADTarEndHP3=40`  
  
`ADGem4=2`  
`ADSpell4=Scalding Sands`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=fire2`  
`ADAnnounce4=`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellDelay4=15`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=90`  
`ADTarEndHP4=20`  
`ADSpellCastonResist1=`  
`ADSpellCastonResist2=`  
`ADSpellCastonResist3=`  
`ADSpellCastonResist4=`  
  
`ADAggroOnly=0`  
  
`ADGem5=2`  
`ADSpell5=Black Steel`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=magic2`  
`ADAnnounce5=`  
`ADSpellMinMana5=10`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=10`  
`ADTarCnt5=0`  
`ADTarType5=1`  
`ADTarBegHP5=92`  
`ADTarEndHP5=25`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem6=3`  
`ADSpell6=Bolt of Molten Slag Rk. II`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=fire`  
`ADAnnounce6=`  
`ADSpellMinMana6=0`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=91`  
`ADTarEndHP6=10`  
`ADIfSpellImmune1=`  
`ADIfSpellImmune2=`  
`ADIfSpellImmune3=`  
`ADIfSpellImmune4=`  
`ADIfSpellImmune5=`  
`ADIfSpellImmune6=`  
  
`[AdvBuff]`  
`ABCount=9`  
`ABMobMax=16`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=script`  
`ABSpell1=haste`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=pethaste`  
`ABAnnounce1=`  
`ABSpellMinMana1=10`  
`ABTarCnt1=1`  
`ABTarType1=mypet cbt idle`  
  
`ABGem2=6`  
`ABSpell2=Fireskin`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=ds`  
`ABAnnounce2=`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=mypet`  
  
`ABGem3=8`  
`ABSpell3=Phantom Shield`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=manabuff`  
`ABAnnounce3=`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
  
`ABGem4=8`  
`ABSpell4=Summon Dagger of the Deep`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=petwep`  
`ABAnnounce4=`  
`ABSpellMinMana4=0`  
`ABTarCnt4=0`  
`ABTarType4=self`  
  
`ABGem5=8`  
`ABSpell5=Summon Muzzle of Mowcha`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=petmask`  
`ABAnnounce5=`  
`ABSpellMinMana5=0`  
`ABTarCnt5=0`  
`ABTarType5=self`  
  
`ABGem6=script`  
`ABSpell6=PetKit`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=petkit`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=self`  
  
`ABGem7=8`  
`ABSpell7=Summon Crystal Belt`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=petbelt`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=self`  
`ABRecast1=FALSE`  
`ABRecast2=FALSE`  
`ABRecast3=FALSE`  
`ABRecast4=FALSE`  
`ABRecast5=FALSE`  
`ABRecast6=FALSE`  
`ABRecast7=FALSE`  
  
`ABGem8=script`  
`ABSpell8=summparadox`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=`  
`ABAnnounce8=`  
`ABSpellMinMana8=0`  
`ABTarCnt8=1`  
`ABTarType8=self cbt idle`  
  
`ABRecast8=FALSE`  
`ABGem9=`  
`ABSpell9=`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=`  
`ABAnnounce9=`  
`ABSpellMinMana9=0`  
`ABTarCnt9=0`  
`ABTarType9=tank war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self mypet grp pet cbt idle`  
`ABRecast9=FALSE`  
  
`[AdvEvent]`  
`AECount=1`  
`AECheckTime=8`  
  
`AEGem1=script`  
`AESpell1=Draw`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=45`  
`AEEventMinMana1=10`  
`AEEventMinHP1=50`  
`AEMinMana1=10`  
`AEMaxMana1=93`  
`AEMinHP1=40`  
`AEMaxHP1=100`  
`AETarType1=self`  
`AESpellAlias1=draw`  
`AEAnnounce1=`  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-PetKit] `  
`Commands=14`  
`C1=/if (!{Defined[PKPetName]}) /declare PKPetName string outer`  
`C2=/if ({Target.ID}!={Me.Pet.ID} && {Spawn[{Target.ID}].Type.Equal[pet]}) /varset PKPetName {Target.CleanName}`  
`C3=/if ({PKPetName.Length}<4 && {Me.Pet.ID}) /varset PKPetName {Me.Pet.CleanName} `  
`C4=/if ({PKPetName.Length}<4) /return `  
`C5=/varset Timer 10m`  
`C6=/call CastCall {Me.CleanName} ''cast petmask''`  
`C7=/multiline ; /delay 1s;/autoinventory`  
`C8=/multiline ; /autoinventory;/call CastCall {Me.CleanName} ''cast petwep''`  
`C9=/multiline ; /delay 1s;/autoinventory`  
`C10=/multiline ; /autoinventory;/call CastCall {Me.CleanName} ''cast petwep''`  
`C11=/multiline ; /delay 1s;/autoinventory`  
`C12=/multiline ; /autoinventory;/call CastCall {Me.CleanName} ''cast petbelt'' `  
`C13=/multiline ; /delay 1s;/autoinventory`  
`C14=/call GiveCheck {PKPetName} ''Summoned: Crystal Belt|Summoned: Dagger of the Deep|Summoned: Dagger of the Deep|Summoned: Muzzle of Mowcha'' `  
`[Script-Draw]`  
`Commands=3`  
`C1=/if ({Select[{Me.CombatState},Resting,Active]} || {Me.State.Equal[Sit]} || !{Me.Pet.ID}) /return`  
`C2=/if (!{Me.Gem[Elemental Draw]}) /memorize ''Elemental Draw|gem6'' `  
`C3=/if ({Me.Pet.ID} && {Me.Pet.PctHPs}>80 && !{Select[{Me.CombatState},Resting,Active]} && {Cast.Ready[Elemental Draw]}) /casting ''Elemental Draw|gem6''`  
  
`[Script-haste]`  
`Commands=3`  
`C1=/if (!{Me.PetBuff[Elemental Fury]}) /casting ''Elemental Fury|gem5'' `  
`C2=/delay 1s {Me.Casting.ID}`  
`C3=/delay 5s !{Me.Casting.ID}`  
  
`[Script-summparadox]`  
`Commands=3`  
`C1=/if (!{FindItemCount[Summoned: Elemental Ice Sliver]}) /casting ''Summon Wintry Paradox|gem8''`  
`C2=/if (!{FindItemCount[Summoned: Elemental Ice Sliver]}) /delay 1s {Me.Casting.ID}`  
`C3=/if (!{FindItemCount[Summoned: Elemental Ice Sliver]}) /delay 7s !{Me.Casting.ID}`

## Level 85

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=`  
`DoAura=FALSE`  
`AuraCast=`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Aspect of Earth|Gem10|smii`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`PetShrinkSpell=Kraxz' Earring of Command|ear`  
`GoMNuke=Alias of debuff for GoM `  
`GoRMNuke=`  
`GoERMNuke=`  
`GoAERMNuke=`  
`TraderName=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=70`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/pet qattack`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=1`  
`AHCheckTime=2`  
`AHHealOOBC=FALSE`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`AHGem1=7`  
`AHSpell1=Renewal of Cadwin`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=10`  
`AHSpellAlias1=petheal`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=hp60 mypet`  
`AHPreCondition1=TRUE`  
  
`[AdvDebuff]`  
`ADCount=3`  
`ADMobMax=100`  
`ADCheckTime=2`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=1`  
`ADSpell1=Shock of Discordant Steel`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=steel`  
`ADAnnounce1=/bc [+y+]`  
`ADSpellMinMana1=0`  
`ADSpellRecast1=3`  
`ADSpellCastonResist1=`  
`ADSpellDelay1=15`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=95`  
`ADTarEndHP1=20`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=2`  
`ADSpell2=Torrid Sands`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=sands`  
`ADAnnounce2=/bc [+y+]`  
`ADSpellMinMana2=0`  
`ADSpellRecast2=3`  
`ADSpellCastonResist2=`  
`ADSpellDelay2=10`  
`ADTarCnt2=1`  
`ADTarType2=1`  
`ADTarBegHP2=95`  
`ADTarEndHP2=20`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=item`  
`ADSpell3=Summoned: Elemental Ice Sliver`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=sliver`  
`ADAnnounce3=/bc [+y+]`  
`ADSpellMinMana3=10`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=20`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=95`  
`ADTarEndHP3=20`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`[AdvBuff]`  
`ABCount=3`  
`ABMobMax=18`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=6`  
`ABSpell1=Burnout VIII`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=pethaste`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=10`  
`ABTarCnt1=1`  
`ABTarType1=mypet cbt idle`  
`ABRecast1=TRUE`  
`ABSpellIcon1=`  
  
`ABGem2=8`  
`ABSpell2=Circle of Brimstoneskin`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=skin`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=20`  
`ABTarCnt2=4`  
`ABTarType2=self grp`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
  
`ABGem3=script`  
`ABSpell3=summparadox`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=20`  
`ABTarCnt3=4`  
`ABTarType3=self cbt idle`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
  
`[AdvEvent]`  
`AECount=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-haste]`  
`Commands=3`  
`C1=/if (!{Me.PetBuff[Elemental Fury]}) /casting ''Elemental Fury|gem5''`  
`C2=/delay 1s {Me.Casting.ID}`  
`C3=/delay 5s !{Me.Casting.ID}`  
  
`[Script-summparadox]`  
`Commands=3`  
`C1=/if (!{FindItemCount[Summoned: Elemental Ice Sliver]}) /casting ''Summon Wintry Paradox|gem8''`  
`C2=/if (!{FindItemCount[Summoned: Elemental Ice Sliver]}) /delay 1s {Me.Casting.ID}`  
`C3=/if (!{FindItemCount[Summoned: Elemental Ice Sliver]}) /delay 7s !{Me.Casting.ID}`

## Level 100

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=TRUE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=TRUE`  
`DoPull=FALSE`  
`DoPet=FALSE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Ornate Barding|item`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Shard of Water|Gem11|smii`  
`PetAggro=FALSE`  
`PetAssist=1`  
`PetFoci=`  
`PetShrink=TRUE`  
`PetShrinkSpell=Ring of the Ancients|item`  
`GoMNuke=spear`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=100`  
`ACAssistPct=98`  
`ACManaPct=70`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=/pet qattack`  
`ACAfter=`  
  
`[AdvHeal]`  
`AHCount=2`  
`AHCheckTime=4`  
`AHHealOOBC=FALSE`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`AHGem1=6`  
`AHSpell1=Renewal of Hererra`  
`AHSpellFoci1=`  
`AHDurMod1=0`  
`AHSpellMinMana1=10`  
`AHSpellAlias1=petheal`  
`AHAnnounce1=/bc`  
`AHTarCnt1=1`  
`AHClass1=hp60 mypet`  
`AHPreCondition1=TRUE`  
  
`AHGem2=7`  
`AHSpell2=Promised Amelioration`  
`AHSpellFoci2=`  
`AHDurMod2=0`  
`AHSpellMinMana2=10`  
`AHSpellAlias2=petpr`  
`AHAnnounce2=/bc`  
`AHTarCnt2=1`  
`AHClass2=hp40 mypet`  
`AHPreCondition2=PR`  
  
`[AdvDebuff]`  
`ADCount=8`  
`ADMobMax=100`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=5`  
`ADSpell1=Blistersteel Malosenia`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=malo`  
`ADAnnounce1=/bc [+y+]`  
`ADSpellMinMana1=10`  
`ADSpellRecast1=3`  
`ADSpellCastonResist1=`  
`ADSpellDelay1=0`  
`ADTarCnt1=1`  
`ADTarType1=1`  
`ADTarBegHP1=98`  
`ADTarEndHP1=0`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=9`  
`ADSpell2=Broiling Sands`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=sands`  
`ADAnnounce2=/bc [+y+]`  
`ADSpellMinMana2=10`  
`ADSpellRecast2=0`  
`ADSpellCastonResist2=`  
`ADSpellDelay2=0`  
`ADTarCnt2=0`  
`ADTarType2=1`  
`ADTarBegHP2=97`  
`ADTarEndHP2=0`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=2`  
`ADSpell3=Fickle Magma`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=magma`  
`ADAnnounce3=/bc [+y+]`  
`ADSpellMinMana3=10`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=97`  
`ADTarEndHP3=0`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=3`  
`ADSpell4=Bolt of Molten Magma`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=bolt`  
`ADAnnounce4=/bc [+y+]`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=1`  
`ADTarType4=1`  
`ADTarBegHP4=97`  
`ADTarEndHP4=0`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=4`  
`ADSpell5=Blast of Sand`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=sand`  
`ADAnnounce5=/bc [+y+]`  
`ADSpellMinMana5=10`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=97`  
`ADTarEndHP5=0`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=1`  
`ADSpell6=Spear of Blistersteel`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=spear`  
`ADAnnounce6=/bc [+y+]`  
`ADSpellMinMana6=10`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=1`  
`ADTarType6=1`  
`ADTarBegHP6=97`  
`ADTarEndHP6=0`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`ADGem7=script`  
`ADSpell7=setNormalOrder`  
`ADSpellFoci7=`  
`ADDurMod7=0`  
`ADSpellAlias7=setNormalOrder`  
`ADAnnounce7=`  
`ADSpellMinMana7=0`  
`ADSpellRecast7=0`  
`ADSpellCastonResist7=`  
`ADSpellDelay7=0`  
`ADTarCnt7=0`  
`ADTarType7=1`  
`ADTarBegHP7=97`  
`ADTarEndHP7=0`  
`ADIfSpellImmune7=`  
`ADUseHoTT7=0`  
`ADPreCondition7=TRUE`  
  
`ADGem8=item`  
`ADSpell8=Summoned: Icebound Sliver`  
`ADSpellFoci8=`  
`ADDurMod8=0`  
`ADSpellAlias8=icebound`  
`ADAnnounce8=/bc [+y+]`  
`ADSpellMinMana8=10`  
`ADSpellRecast8=0`  
`ADSpellCastonResist8=`  
`ADSpellDelay8=0`  
`ADTarCnt8=1`  
`ADTarType8=1`  
`ADTarBegHP8=98`  
`ADTarEndHP8=0`  
`ADIfSpellImmune8=`  
`ADUseHoTT8=0`  
`ADPreCondition8=TRUE`  
  
`[AdvBuff]`  
`ABCount=23`  
`ABMobMax=100`  
`ABCheckTime=8`  
  
`ABGem1=12`  
`ABSpell1=Burnout XI`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=pethaste`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=10`  
`ABTarCnt1=1`  
`ABTarType1=mypet cbt idle`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
`ABPreCondition1=TRUE`  
  
`ABGem2=11`  
`ABSpell2=Circle of Flameskin`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=skin`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=10`  
`ABTarCnt2=1`  
`ABTarType2=self grp brd shd pal war pet`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=12`  
`ABSpell3=Shield of the Dauntless`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=shield`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=10`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=12`  
`ABSpell4=Phantasmal Guardian`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=guard`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=10`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=item`  
`ABSpell5=Staff of Elemental Essence`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=epic`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=mypet cbt idle`  
`ABRecast5=FALSE`  
`ABSpellIcon5=Elemental Conjunction`  
`ABPreCondition5=TRUE`  
  
`ABGem6=script`  
`ABSpell6=PetKit`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=petkit`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=self cbt idle`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=11`  
`ABSpell7=Iceflame Eminence`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=petward`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=10`  
`ABTarCnt7=0`  
`ABTarType7=mypet cbt idle`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=script`  
`ABSpell8=summparadox`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=summparadox`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=10`  
`ABTarCnt8=3`  
`ABTarType8=self cbt idle`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=11`  
`ABSpell9=Magmatic Veil`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=veil`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=10`  
`ABTarCnt9=3`  
`ABTarType9=tank cbt`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=8`  
`ABSpell10=Surge of Arcanum`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=surge`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=10`  
`ABTarCnt10=3`  
`ABTarType10=tank cbt`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=item`  
`ABSpell11=Perorate Cloak of the Word Lord`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=spikes`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=1`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=item`  
`ABSpell12=Double Hoop of Tegleth`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=geo`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=0`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=item`  
`ABSpell13=Earring of Soothing Melodies`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=petshrink`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=0`  
`ABTarCnt13=0`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Face of Dread`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=end`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=0`  
`ABTarCnt14=1`  
`ABTarType14=self`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`ABGem15=item`  
`ABSpell15=Brilliant Band of Arcane Knowledge`  
`ABSpellFoci15=`  
`ABDurMod15=0`  
`ABSpellAlias15=past1`  
`ABAnnounce15=/bc`  
`ABSpellMinMana15=0`  
`ABTarCnt15=0`  
`ABTarType15=self`  
`ABRecast15=FALSE`  
`ABSpellIcon15=`  
`ABPreCondition15=TRUE`  
  
`ABGem16=item`  
`ABSpell16=Bixie Mage Band`  
`ABSpellFoci16=`  
`ABDurMod16=0`  
`ABSpellAlias16=past2`  
`ABAnnounce16=/bc`  
`ABSpellMinMana16=0`  
`ABTarCnt16=1`  
`ABTarType16=self`  
`ABRecast16=FALSE`  
`ABSpellIcon16=`  
`ABPreCondition16=TRUE`  
  
`ABGem17=item`  
`ABSpell17=Featherweight Drape of Harmony`  
`ABSpellFoci17=`  
`ABDurMod17=0`  
`ABSpellAlias17=dodge`  
`ABAnnounce17=/bc`  
`ABSpellMinMana17=0`  
`ABTarCnt17=1`  
`ABTarType17=self`  
`ABRecast17=FALSE`  
`ABSpellIcon17=`  
`ABPreCondition17=TRUE`  
  
`ABGem18=item`  
`ABSpell18=Burning Belt of Endless Shadow`  
`ABSpellFoci18=`  
`ABDurMod18=0`  
`ABSpellAlias18=mind`  
`ABAnnounce18=/bc`  
`ABSpellMinMana18=0`  
`ABTarCnt18=1`  
`ABTarType18=self`  
`ABRecast18=FALSE`  
`ABSpellIcon18=`  
`ABPreCondition18=TRUE`  
  
`ABGem19=item`  
`ABSpell19=Compendium of Antonican Creatures`  
`ABSpellFoci19=`  
`ABDurMod19=0`  
`ABSpellAlias19=ward`  
`ABAnnounce19=/bc`  
`ABSpellMinMana19=0`  
`ABTarCnt19=1`  
`ABTarType19=self`  
`ABRecast19=FALSE`  
`ABSpellIcon19=`  
`ABPreCondition19=TRUE`  
  
`ABGem20=item`  
`ABSpell20=Ring of the Ancients`  
`ABSpellFoci20=`  
`ABDurMod20=0`  
`ABSpellAlias20=shrink`  
`ABAnnounce20=/bc`  
`ABSpellMinMana20=0`  
`ABTarCnt20=0`  
`ABTarType20=self`  
`ABRecast20=FALSE`  
`ABSpellIcon20=`  
`ABPreCondition20=TRUE`  
  
`ABGem21=12`  
`ABSpell21=Rathe's Strength`  
`ABSpellFoci21=`  
`ABDurMod21=0`  
`ABSpellAlias21=petaura`  
`ABAnnounce21=/bc`  
`ABSpellMinMana21=0`  
`ABTarCnt21=1`  
`ABTarType21=mypet aura`  
`ABRecast21=FALSE`  
`ABSpellIcon21=`  
`ABPreCondition21=TRUE`  
  
`ABGem22=12`  
`ABSpell22=Arcane Distillect`  
`ABSpellFoci22=`  
`ABDurMod22=0`  
`ABSpellAlias22=aura`  
`ABAnnounce22=/bc`  
`ABSpellMinMana22=0`  
`ABTarCnt22=0`  
`ABTarType22=self aura`  
`ABRecast22=FALSE`  
`ABSpellIcon22=`  
`ABPreCondition22=TRUE`  
  
`ABGem23=item`  
`ABSpell23=Polymorph Wand: Blood Red Bellikos`  
`ABSpellFoci23=`  
`ABDurMod23=0`  
`ABSpellAlias23=illusion`  
`ABAnnounce23=/bc`  
`ABSpellMinMana23=0`  
`ABTarCnt23=0`  
`ABTarType23=self`  
`ABRecast23=FALSE`  
`ABSpellIcon23=`  
`ABPreCondition23=TRUE`  
  
`[AdvEvent]`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECount=13`  
`AECheckTime=8`  
  
`AEGem1=11`  
`AESpell1=Shard of Water`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=0`  
`AEEventMinHP1=0`  
`AEMinMana1=0`  
`AEMaxMana1=0`  
`AEMinHP1=0`  
`AEMaxHP1=0`  
`AETarType1=self cbt idle`  
`AESpellAlias1=pet`  
`AEAnnounce1=/bc`  
`AETarCnt1=0`  
  
`AEGem2=11`  
`AESpell2=Grant Frightforged Armaments`  
`AESpellFoci2=`  
`AEDurMod2=0`  
`AEDelay2=0`  
`AEEventMinMana2=0`  
`AEEventMinHP2=0`  
`AEMinMana2=0`  
`AEMaxMana2=0`  
`AEMinHP2=0`  
`AEMaxHP2=0`  
`AETarType2=self cbt idle`  
`AESpellAlias2=petweap`  
`AEAnnounce2=/bc`  
`AETarCnt2=0`  
  
`AEGem3=11`  
`AESpell3=Grant Frightforged Plate`  
`AESpellFoci3=`  
`AEDurMod3=0`  
`AEDelay3=0`  
`AEEventMinMana3=0`  
`AEEventMinHP3=0`  
`AEMinMana3=0`  
`AEMaxMana3=0`  
`AEMinHP3=0`  
`AEMaxHP3=0`  
`AETarType3=self cbt idle`  
`AESpellAlias3=petarmor`  
`AEAnnounce3=/bc`  
`AETarCnt3=0`  
  
`AEGem4=11`  
`AESpell4=Grant Nint's Heirlooms`  
`AESpellFoci4=`  
`AEDurMod4=0`  
`AEDelay4=0`  
`AEEventMinMana4=0`  
`AEEventMinHP4=0`  
`AEMinMana4=0`  
`AEMaxMana4=0`  
`AEMinHP4=0`  
`AEMaxHP4=0`  
`AETarType4=self cbt idle`  
`AESpellAlias4=petfocus`  
`AEAnnounce4=/bc`  
`AETarCnt4=0`  
  
`AEGem5=11`  
`AESpell5=Grant Visor of Gobeker`  
`AESpellFoci5=`  
`AEDurMod5=0`  
`AEDelay5=0`  
`AEEventMinMana5=0`  
`AEEventMinHP5=0`  
`AEMinMana5=0`  
`AEMaxMana5=0`  
`AEMinHP5=0`  
`AEMaxHP5=0`  
`AETarType5=self cbt idle`  
`AESpellAlias5=visor`  
`AEAnnounce5=/bc`  
`AETarCnt5=0`  
  
`AEGem6=item`  
`AESpell6=Folded Pack of Frightforged Plate`  
`AESpellFoci6=`  
`AEDurMod6=0`  
`AEDelay6=0`  
`AEEventMinMana6=0`  
`AEEventMinHP6=0`  
`AEMinMana6=0`  
`AEMaxMana6=0`  
`AEMinHP6=0`  
`AEMaxHP6=0`  
`AETarType6=self cbt idle`  
`AESpellAlias6=armorbag`  
`AEAnnounce6=/bc`  
`AETarCnt6=0`  
  
`AEGem7=item`  
`AESpell7=Folded Pack of Frightforged Armaments`  
`AESpellFoci7=`  
`AEDurMod7=0`  
`AEDelay7=0`  
`AEEventMinMana7=0`  
`AEEventMinHP7=0`  
`AEMinMana7=0`  
`AEMaxMana7=0`  
`AEMinHP7=0`  
`AEMaxHP7=0`  
`AETarType7=self cbt idle`  
`AESpellAlias7=weapbag`  
`AEAnnounce7=/bc`  
`AETarCnt7=0`  
  
`AEGem8=item`  
`AESpell8=Folded Pack of Nint's Heirlooms`  
`AESpellFoci8=`  
`AEDurMod8=0`  
`AEDelay8=0`  
`AEEventMinMana8=0`  
`AEEventMinHP8=0`  
`AEMinMana8=0`  
`AEMaxMana8=0`  
`AEMinHP8=0`  
`AEMaxHP8=0`  
`AETarType8=self cbt idle`  
`AESpellAlias8=focusbag`  
`AEAnnounce8=/bc`  
`AETarCnt8=0`  
  
`AEGem9=11`  
`AESpell9=Grant Icebound Paradox`  
`AESpellFoci9=`  
`AEDurMod9=0`  
`AEDelay9=0`  
`AEEventMinMana9=0`  
`AEEventMinHP9=0`  
`AEMinMana9=0`  
`AEMaxMana9=0`  
`AEMinHP9=0`  
`AEMaxHP9=0`  
`AETarType9=self cbt idle`  
`AESpellAlias9=paradox`  
`AEAnnounce9=/bc`  
`AETarCnt9=0`  
  
`AEGem10=script`  
`AESpell10=Harvest`  
`AESpellFoci10=`  
`AEDurMod10=0`  
`AEDelay10=0`  
`AEEventMinMana10=1`  
`AEEventMinHP10=35`  
`AEMinMana10=1`  
`AEMaxMana10=30`  
`AEMinHP10=30`  
`AEMaxHP10=100`  
`AETarType10=self`  
`AESpellAlias10=`  
`AEAnnounce10=/bc`  
`AETarCnt10=0`  
  
`AEGem11=11`  
`AESpell11=Grant Quiver of Kalkek`  
`AESpellFoci11=`  
`AEDurMod11=0`  
`AEDelay11=0`  
`AEEventMinMana11=0`  
`AEEventMinHP11=0`  
`AEMinMana11=0`  
`AEMaxMana11=0`  
`AEMinHP11=0`  
`AEMaxHP11=0`  
`AETarType11=war pal rng shd rog`  
`AESpellAlias11=quiver`  
`AEAnnounce11=/bc`  
`AETarCnt11=0`  
  
`AEGem12=alt`  
`AESpell12=Call of the Hero`  
`AESpellFoci12=`  
`AEDurMod12=0`  
`AEDelay12=0`  
`AEEventMinMana12=0`  
`AEEventMinHP12=0`  
`AEMinMana12=0`  
`AEMaxMana12=0`  
`AEMinHP12=0`  
`AEMaxHP12=0`  
`AETarType12=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self tnt`  
`AESpellAlias12=coth`  
`AEAnnounce12=/bc`  
`AETarCnt12=0`  
  
`AEGem13=11`  
`AESpell13=Gift of Daybreak`  
`AESpellFoci13=`  
`AEDurMod13=0`  
`AEDelay13=0`  
`AEEventMinMana13=0`  
`AEEventMinHP13=0`  
`AEMinMana13=0`  
`AEMaxMana13=0`  
`AEMinHP13=0`  
`AEMaxHP13=0`  
`AETarType13=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec self tnt`  
`AESpellAlias13=feedme`  
`AEAnnounce13=/bc`  
`AETarCnt13=0`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-summparadox]`  
`Commands=1`  
`C1=/if (!{FindItemCount[Summoned: Icebound Sliver]}) /call CastCall {Me.CleanName} ''cast paradox''`  
  
`[Script-Harvest] `  
`Commands=6`  
`C1=/if (!{Me.Gem[Gather Magnitude]}) /memorize ''Gather Magnitude|gem10''`  
`C2=/if ({Me.Casting.ID}) /delay 5s {Cast.Ready} `  
`C3=/if (!{Cast.Ready[Gather Magnitude]}) /return `  
`C4=/if ({Cast.Ready[Gather Magnitude]}) /call MQ2Cast ''Gather Magnitude'' gem10 6s `  
`C5=/varset Timer 20s `  
`C6=/delay 15s !{Me.Buff[Gather Magnitude].ID}`  
  
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
`C5=/if (!{Me.Pet.ID}) /call CastCall {Me.CleanName} ''cast pet''`  
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
`C22=/if ({{EmptySlot.Equal[false]}) /bc no empty slots, sorry no pet kit right now.`  
`C23=/if ({{EmptySlot.Equal[false]}) /return 0`  
`; Allow for more than 30 seconds by setting the timer to 10 minutes`  
`C24=/varset Timer 10m`  
`; summon the pet armor`  
`C25=/bc giving pet armor`  
`C26=/call CastCall {Me.CleanName} ''cast petarmor''`  
`C27=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; unfold the armorbag`  
`C28=/call CastCall {Me.CleanName} ''cast armorbag''`  
`C29=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand armor to pet`  
`; adjust the armor below to match those summoned in the bag`  
`C30=/call GiveCheck {PKPetName} ''Frightforged Plate Helm|Frightforged Plate Breastplate|Frightforged Plate Bracers|Summoned: Frightforged Belt''`  
`C31=/call GiveCheck {PKPetName} ''Frightforged Plate Vambraces|Frightforged Plate Gauntlets|Frightforged Plate Greaves|Frightforged Plate Boots''`  
`; delete the Phantom Satchel`  
`; **DANGER** if you are using any Phantom Satchels to store items this could be disastrous`  
`C32=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C33=/delay 5`  
`C34=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`C35=/echo destroyed Phantom Satchel`  
`C36=/delay 1s`  
`;summon the pet weapons`  
`C37=/echo giving pet weapons`  
`C38=/call CastCall {Me.CleanName} ''cast petweap''`  
`C39=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; unfold the weapbag`  
`C40=/call CastCall {Me.CleanName} ''cast weapbag''`  
`C41=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand weapon to pet`  
`; adjust the weapons below to match those summoned in the bag`  
`C42=/call GiveCheck {PKPetName} ''Summoned: Frightforged Iceblade|Summoned: Frightforged Iceblade''`  
`; delete the Pouch of Quellious`  
`; **DANGER** if you are using any Pouch of Quellious' to store items this could be disastrous`  
`C43=/nomodkey /itemnotify {FindItem[Pouch of Quellious].InvSlot} leftmouseup`  
`C44=/delay 5`  
`C45=/if ({Cursor.Name.Equal[Pouch of Quellious]}) /destroy`  
`C46=/echo destroyed Pouch of Quellious`  
`C47=/delay 1s`  
`; summon pet focus items`  
`C48=/bc giving pet focus items`  
`C49=/call CastCall {Me.CleanName} ''cast petfocus''`  
`C50=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; unfold the focusbag`  
`C51=/call CastCall {Me.CleanName} ''cast focusbag''`  
`C52=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand focus items to pet`  
`; adjust the focus items below to match those summoned in the bag`  
`C53=/call GiveCheck {PKPetName} ''Nint's Linked Bracelet|Nint's Jade Bracelet|Nint's Ridged Earhoop|Nint's Gold Ring''`  
`C54=/call GiveCheck {PKPetName} ''Nint's Woven Shawl|Nint's Satin Choker''`  
`; delete the Phantom Satchel`  
`; **DANGER** if you are using any Phantom Satchels to store items this could be disastrous`  
`C55=/nomodkey /itemnotify {FindItem[Phantom Satchel].InvSlot} leftmouseup`  
`C56=/delay 5`  
`C57=/if ({Cursor.Name.Equal[Phantom Satchel]}) /destroy`  
`C58=/echo destroyed Phantom Satchel`  
`C59=/delay 1s`  
`; summon the visor`  
`C60=/echo giving pet visor`  
`C61=/call CastCall {Me.CleanName} ''cast visor''`  
`C62=/multiline ; /delay 1s ; /autoinventory ; /delay 1s`  
`; hand the visor to pet`  
`; adjust the below to match summoned visor`  
`C63=/call GiveCheck {PKPetName} ''Summoned: Visor of Gobeker''`  
`C64=/bc pet {PKPetName} ready for battle!`  
  
`[Script-PR]`  
`Commands=0`  
`C1=/return`  
  
`[Script-setNormalOrder] `  
`Commands=13 `  
`C1=/if (!{Defined[nextCast]}) /declare nextCast int outer 0; `  
`C2=/if (!{Defined[CastOne]}) /declare CastOne int outer 0; `  
`C3=/if (!{Defined[CastTwo]}) /declare CastTwo int outer 0; `  
`C4=/if (!{Defined[CastThree]}) /declare CastThree int outer 0; `  
`C5=/if (!{Defined[CastFour]}) /declare CastFour int outer 0; `  
`C6=/multiline ; /varset ADTarCnt[2] 0 ; /varset ADTarCnt[3] 0 ; /varset ADTarCnt[4] 0 ; /varset ADTarCnt[5] 0 ; /varset ADTarCnt[6] 0 `  
`C7=/if ({nextCast}==0) /multiline ; /varset nextCast 1 ; /varcalc CastOne {CastOne}+1 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return `  
`C8=/if ({nextCast}==1) /multiline ; /varset nextCast 3 ; /varcalc CastThree {CastThree}+1 ; /varset ADTarCnt[4] 1 ; /echo 4 ; /return `  
`C9=/if ({nextCast}==3 && {CastOne}<=1) /multiline ; /varset nextCast 1 ; /varcalc CastOne {CastOne}+1 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return `  
`C10=/if ({nextCast}==3 && {CastOne}>1) /multiline ; /varset nextCast 2 ; /varcalc CastTwo {CastTwo}+1 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return `  
`C11=/if ({nextCast}==2 && {Me.Song[Aria of the Composer].ID}) /multiline ; /varset nextCast 4 ; /varcalc CastFour {CastFour}+1 ; /varset ADTarCnt[5] 1 ; /echo 5 ; /return `  
`C12=/if ({nextCast}==2) /multiline ; /varset nextCast 3 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset ADTarCnt[4] 1 ; /echo 4 ; /return `  
`C13=/if ({nextCast}==4) /multiline ; /varset nextCast 2 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset CastFour 0 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return`

# Wizard

## Level 80

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=FALSE`  
`DoBuffs=FALSE`  
`DoDebuffs=TRUE`  
`DoEvents=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Small Black Drum|item`  
`MasterList=${NetBots.Client}`  
`TankName=`  
`ExcludeList=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now thanks`  
`FollowDistance=20`  
`FollowStick=12 hold uw`  
`PetCast=Loyal Familiar|alt -invis`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`DoCures=FALSE`  
`DeathSlot=`  
`DoAura=FALSE`  
`AuraCast=`  
`PetShrinkSpell=`  
`ForageIni=forage.ini`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=100`  
`ACAssistPct=95`  
`ACManaPct=20`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=12`  
`ADMobMax=20`  
`ADCheckTime=2`  
  
`ADGem1=1`  
`ADSpell1=Concussive Blast Rk. II`  
`ADSpellFoci1= `  
`ADDurMod1=30`  
`ADSpellAlias1=concblast `  
`ADAnnounce1=`  
`ADSpellMinMana1=15 `  
`ADSpellRecast1=3 `  
`ADSpellDelay1=30`  
`ADTarCnt1=1 `  
`ADTarType1=1 `  
`ADTarBegHP1=98 `  
`ADTarEndHP1=10`  
`ADSpellCastonResist1=`  
  
`ADGem2=script`  
`ADSpell2=concrecourse`  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2=concrecourse`  
`ADAnnounce2=`  
`ADSpellMinMana2=15 `  
`ADSpellRecast2=3 `  
`ADSpellDelay2=0 `  
`ADTarCnt2=1 `  
`ADTarType2=1 `  
`ADTarBegHP2=97 `  
`ADTarEndHP2=10 `  
`ADSpellCastonResist2=`  
  
`ADGem3=10`  
`ADSpell3=Atol's Spectral Shackles`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=snare`  
`ADAnnounce3=/bc [+g+]snared [+x+]`  
`ADSpellMinMana3=0`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=1`  
`ADTarType3=1`  
`ADTarBegHP3=40`  
`ADTarEndHP3=0`  
  
`ADGem4=7`  
`ADSpell4=Telekara`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=stun`  
`ADAnnounce4=`  
`ADSpellMinMana4=0`  
`ADSpellRecast4=1`  
`ADSpellDelay4=1`  
`ADTarCnt4=0`  
`ADTarType4=1`  
`ADTarBegHP4=25`  
`ADTarEndHP4=10`  
`ADSpellCastonResist4=`  
  
`ADGem5=3`  
`ADSpell5=Claw of Selig`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=icelure`  
`ADAnnounce5=`  
`ADSpellMinMana5=0`  
`ADSpellRecast5=1`  
`ADSpellDelay5=100`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=90`  
`ADTarEndHP5=10`  
`ADSpellCastonResist5=`  
`ADAggroOnly=0`  
  
`ADGem6=4`  
`ADSpell6=Ethereal Incineration`  
`ADSpellFoci6= `  
`AdDurMod6=0 `  
`ADSpellAlias6=firedd `  
`ADAnnounce6=`  
`ADspellMinMana6=0 `  
`ADSpellRecast6=3 `  
`ADSpellCastonResist6= `  
`ADSpellDelay6=0 `  
`ADTarCnt6=1 `  
`ADTarType6=1 `  
`ADTarBegHP6=95 `  
`ADTarEndHP6=10 `  
  
`ADGem7=9`  
`ADSpell7=Glacial Collapse`  
`ADSpellFoci7= `  
`AdDurMod7=0 `  
`ADSpellAlias7=icedd `  
`ADAnnounce7=`  
`ADspellMinMana7=0 `  
`ADSpellRecast7=3 `  
`ADSpellCastonResist7= `  
`ADSpellDelay7=0 `  
`ADTarCnt7=1 `  
`ADTarType7=1 `  
`ADTarBegHP7=95 `  
`ADTarEndHP7=10 `  
  
`ADGem8=8 `  
`ADSpell8=Rolling Lightning`  
`ADSpellFoci8= `  
`AdDurMod8=0 `  
`ADSpellAlias8=magicdd `  
`ADAnnounce8=`  
`ADspellMinMana8=0 `  
`ADSpellRecast8=3 `  
`ADSpellCastonResist8= `  
`ADSpellDelay8=0 `  
`ADTarCnt8=1 `  
`ADTarType8=1 `  
`ADTarBegHP8=95`  
`ADTarEndHP8=0`  
  
`ADGem9=2`  
`ADSpell9=Leap of Arclight`  
`ADSpellFoci9=`  
`ADDurMod9=0`  
`ADSpellAlias9=magiclure`  
`ADAnnounce9=`  
`ADSpellMinMana9=0`  
`ADSpellRecast9=0`  
`ADSpellCastonResist9=`  
`ADSpellDelay9=10`  
`ADTarCnt9=1`  
`ADTarType9=1`  
`ADTarBegHP9=95`  
`ADTarEndHP9=10`  
  
`ADGem10=5`  
`ADSpell10=Pyrolure`  
`ADSpellFoci10=`  
`ADDurMod10=0`  
`ADSpellAlias10=firelure`  
`ADAnnounce10=`  
`ADSpellMinMana10=0`  
`ADSpellRecast10=0`  
`ADSpellCastonResist10=`  
`ADSpellDelay10=10`  
`ADTarCnt10=1`  
`ADTarType10=1`  
`ADTarBegHP10=95`  
`ADTarEndHP10=10`  
  
`ADGem11=7`  
`ADSpell11=Lure of Isaz`  
`ADSpellFoci11=`  
`ADDurMod11=0`  
`ADSpellAlias11=coldlure2`  
`ADAnnounce11=`  
`ADSpellMinMana11=5`  
`ADSpellRecast11=0`  
`ADSpellCastonResist11=`  
`ADSpellDelay11=10`  
`ADTarCnt11=1`  
`ADTarType11=1`  
`ADTarBegHP11=95`  
`ADTarEndHP11=20`  
  
`ADGem12=item `  
`ADSpell12=Scepter of Incantations `  
`ADSpellFoci12= `  
`ADDurMod12=0 `  
`ADSpellAlias12=staff `  
`ADAnnounce12=/bc `  
`ADAnnounce12= `  
`ADSpellMinMana12=15 `  
`ADSpellRecast12=3 `  
`ADSpellDelay12=0 `  
`ADTarCnt12=1`  
`ADTarType12=1 `  
`ADTarBegHP12=95 `  
`ADTarEndHP12=10 `  
`ADSpellCastonResist12=`  
  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
`ADIfSpellImmune1=`  
`ADIfSpellImmune2=`  
`ADIfSpellImmune3=`  
`ADIfSpellImmune4=`  
`ADIfSpellImmune5=`  
`ADIfSpellImmune6=`  
`ADIfSpellImmune7=`  
`ADIfSpellImmune8=`  
`ADIfSpellImmune9=`  
`ADIfSpellImmune10=`  
`ADIfSpellImmune11=`  
`ADIfSpellImmune12=`  
  
`[AdvBuff]`  
`ABCount=9`  
`ABMobMax=12`  
`ABCheckTime=8`  
`ABProactive=TRUE`  
  
`ABGem1=5`  
`ABSpell1=Scales of the Crystalwing Rk. II`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=`  
`ABAnnounce1=`  
`ABSpellMinMana1=0`  
`ABTarCnt1=1`  
`ABTarType1=self`  
  
`ABGem2=5`  
`ABSpell2=levitation`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=levi`  
`ABAnnounce2=`  
`ABSpellMinMana2=0`  
`ABTarCnt2=0`  
`ABTarType2=war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec grp`  
  
`ABGem3=item`  
`ABSpell3=Fellowship Registration Insignia`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=site`  
`ABAnnounce3=`  
`ABSpellMinMana3=0`  
`ABTarCnt3=0`  
`ABTarType3=self`  
`ABRecast1=FALSE`  
`ABRecast2=FALSE`  
`ABRecast3=FALSE`  
  
`ABGem4=9`  
`ABSpell4=Katta Castrum Portal`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=Kattaport`  
`ABAnnounce4=`  
`ABSpellMinMana4=0`  
`ABTarCnt4=0`  
`ABTarType4=self`  
`ABRecast4=FALSE`  
  
`ABGem5=9`  
`ABSpell5=Knowledge Portal`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=pokport`  
`ABAnnounce5=`  
`ABSpellMinMana5=0`  
`ABTarCnt5=0`  
`ABTarType5=self`  
`ABRecast5=FALSE`  
  
`ABGem6=9`  
`ABSpell6=Alter Plane: Hate`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=hateport`  
`ABAnnounce6=`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=self`  
`ABRecast6=FALSE`  
  
`ABGem7=9`  
`ABSpell7=Alter Plane: Sky`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=skyport`  
`ABAnnounce7=`  
`ABSpellMinMana7=0`  
`ABTarCnt7=0`  
`ABTarType7=self`  
`ABRecast7=FALSE`  
  
`ABGem8=9`  
`ABSpell8=Phase March`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=groupinvis`  
`ABAnnounce8=`  
`ABSpellMinMana8=0`  
`ABTarCnt8=0`  
`ABTarType8=self`  
`ABRecast8=FALSE`  
  
`ABGem9=9`  
`ABSpell9=Dragonscale Hills Portal`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=dsport`  
`ABAnnounce9=`  
`ABSpellMinMana9=0`  
`ABTarCnt9=0`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
  
`[AdvEvent]`  
`AECount=3`  
`AECheckTime=8`  
  
`AEGem1=alt`  
`AESpell1=Harvest of Druzzil`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=1`  
`AEEventMinHP1=35`  
`AEMinMana1=1`  
`AEMaxMana1=80`  
`AEMinHP1=30`  
`AEMaxHP1=100`  
`AETarType1=self`  
`AESpellAlias1=`  
`AEAnnounce1=`  
  
`AEGem2=script`  
`AESpell2=Harvest`  
`AESpellFoci2=`  
`AEDurMod2=0`  
`AEDelay2=0`  
`AEEventMinMana2=1`  
`AEEventMinHP2=35`  
`AEMinMana2=1`  
`AEMaxMana2=30`  
`AEMinHP2=30`  
`AEMaxHP2=100`  
`AETarType2=self`  
`AESpellAlias2=`  
`AEAnnounce2=`  
  
`AEGem3=Script `  
`AESpell3=Pet `  
`AESpellFoci3= `  
`AEDurMod3=0 `  
`AEDelay3=0 `  
`AEEventMinMana3=0 `  
`AEEventMinHP3=1 `  
`AEMinMana3=1 `  
`AEMaxMana3=100 `  
`AEMinHP3=1 `  
`AEMaxHP3=100 `  
`AETarType3=self `  
`AESpellAlias3=Pet `  
`AEAnnounce3=/bc `  
  
`[AdvPull]`  
`APCheckTimer=0`  
`APRadius=100`  
`APSpell=`  
`APRangedMod=0`  
`APMobMax=1`  
`APScript=AdvPull`  
`APBefore=`  
`APAfter=`  
`APCheckTime=0`  
`APPath=`  
`APAnnounce=`  
`APRetPath=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-Harvest]`  
`Commands=3`  
`C1=/if (!${Me.Gem[Patient Harvest Rk. II]}) /memorize ''Patient Harvest Rk. II|gem10''`  
`C2=/if ({Cast.Ready[Patient Harvest Rk. II]}) /multiline ; /casting ''Patient Harvest Rk. II|gem10''`  
`C3=/delay 10s`  
  
`[Script-concrecourse] `  
`Commands=6`  
`C1=/multiline ; /declare totalsongs int local 0;/if (!{Defined[DoFire]}) /declare DoFire bool outer TRUE;/if (!{Defined[DoMagic]}) /declare DoMagic bool outer TRUE;/if (!{Defined[DoCold]}) /declare DoCold bool outer TRUE`  
`C2=/docommand {If[!{Me.Song[Concussive Flames].ID}&&{DoFire},/varset ADTarCnt[6] 0,/multiline ; /varset ADTarCnt[6] 1;/varset totalsongs {totalsongs}+1]}`  
`C3=/docommand {If[!{Me.Song[Concussive Chill].ID}&&{DoCold},/varset ADTarCnt[7] 0,/multiline ; /varset ADTarCnt[7] 1;/varset totalsongs {totalsongs}+1]}`  
`C4=/docommand {If[!{Me.Song[Concussive Magic].ID}&&{DoMagic},/varset ADTarCnt[8] 0,/varset ADTarCnt[8] 1;/varset totalsongs {totalsongs}+1]}`  
`C5=/docommand {If[{totalsongs}<1,/multiline ; /varset ADTarCnt[5] 1;/varset ADTarCnt[9] 1;/varset ADTarCnt[10] 1,/multiline ; /varset ADTarCnt[5] 0;/varset ADTarCnt[9] 0;/varset ADTarCnt[10] 0]}`  
`C6=/call MBScript setnukes`  
  
`[Script-Pet] `  
`Commands=2 `  
`C1=/multiline ; /if ({Me.AltAbilityReady[52]} && !{Me.Buff[Improved Familiar].ID} && !{Me.Casting.ID} && !{Me.Moving}) /alt activate 52`  
`C2=/if ({Me.Pet.ID}) /pet get lost `  
  
`[Script-setnukes]`  
`Commands=4`  
`C1=/multiline ; /if (!{Defined[DoFire]}) /declare DoFire bool outer TRUE;/if (!{Defined[DoMagic]}) /declare DoMagic bool outer TRUE;/if (!{Defined[DoCold]}) /declare DoCold bool outer TRUE`  
`C2=/if (!{DoFire}) /multiline ; /varset ADTarCnt[6] 0;/varset ADTarCnt[10] 0`  
`C3=/if (!{DoMagic}) /multiline ; /varset ADTarCnt[4] 0;/varset ADTarCnt[8] 0;/varset ADTarCnt[9] 0`  
`C4=/if (!{DoCold}) /multiline ; /varset ADTarCnt[5] 0;/varset ADTarCnt[7] 0;/varset ADTarCnt[11] 0`

## Level 85

`[Settings] `  
`DoMelee=FALSE `  
`DoHeals=FALSE `  
`DoBuffs=FALSE `  
`DoDebuffs=FALSE `  
`DoEvents=FALSE `  
`DoCures=FALSE `  
`DoPull=FALSE `  
`DoPet=TRUE `  
`DoSit=TRUE `  
`DoLoot=FALSE `  
`DoFW=FALSE `  
`DoForage=FALSE `  
`ForageIni=forage.ini `  
`DoAfk=FALSE `  
`DoMount=FALSE `  
`MountCast=Tan Chain Bridle|item`  
`DoAura=FALSE `  
`AuraCast= `  
`MasterList=${NetBots.Client} `  
`TankName=`  
`Radius=100 `  
`SitAggroRadiusCheck=75 `  
`AfkMessage=Not now, thanks `  
`DeathSlot=FALSE `  
`FollowDistance=20 `  
`FollowStick=12 hold uw `  
`PetCast=Improved Familiar|alt -invis`  
`PetAggro=FALSE `  
`PetAssist=0 `  
`PetFoci= `  
`PetShrinkSpell= `  
`GoMNuke=ec`  
`GoRMNuke=ec`  
`GoERMNuke=ec`  
`GoAERMNuke=ec`  
`NetworkINI=MB_network.ini`  
`TraderName=`  
  
`[Melee] `  
`OffTank=FALSE `  
`ACLeash=100 `  
`ACAssistPct=95 `  
`ACManaPct=101 `  
`ACAnnounce=/bc `  
`ACMeleeCmd=/melee plugin=1 `  
`ACBefore= `  
`ACAfter=/multiline ; /varset nextCast 0;/varset CastOne 0;/varset CastTwo 0;/varset CastThree 0;/varset CastFour 0 `  
  
`[AdvHeal] `  
`AHCount=0 `  
  
`[AdvDebuff] `  
`ADCount=6 `  
`ADMobMax=100`  
`ADCheckTime=1`  
`ADAggroOnly=0 `  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff| `  
  
`ADGem1=4`  
`ADSpell1=Chaos Combustion`  
`ADSpellFoci1= `  
`ADDurMod1=0 `  
`ADSpellAlias1=cc `  
`ADAnnounce1=/bc [+m+] `  
`ADSpellMinMana1=10 `  
`ADSpellReCastOne=0 `  
`ADSpellCastonResist1= `  
`ADSpellDelay1=0 `  
`ADTarCnt1=0 `  
`ADTarType1=1 `  
`ADTarBegHP1=95`  
`ADTarEndHP1=10 `  
`ADIfSpellImmune1= `  
`ADSpellRecast1=0 `  
`ADUseHoTT1=0 `  
`ADPreCondition1=TRUE`  
  
`ADGem2=1`  
`ADSpell2=Flashblaze Rk. II`  
`ADSpellFoci2= `  
`ADDurMod2=0 `  
`ADSpellAlias2=fb`  
`ADAnnounce2=/bc [+m+] `  
`ADSpellMinMana2=10 `  
`ADSpellReCastTwo=0 `  
`ADSpellCastonResist2= `  
`ADSpellDelay2=0 `  
`ADTarCnt2=0 `  
`ADTarType2=1 `  
`ADTarBegHP2=95`  
`ADTarEndHP2=10 `  
`ADIfSpellImmune2= `  
`ADSpellRecast2=0 `  
`ADUseHoTT2=0 `  
`ADPreCondition2=TRUE`  
  
`ADGem3=5`  
`ADSpell3=Wildmagic Blast Rk. III`  
`ADSpellFoci3= `  
`ADDurMod3=0 `  
`ADSpellAlias3=wmb3`  
`ADAnnounce3=/bc [+m+] `  
`ADSpellMinMana3=10 `  
`ADSpellReCastThree=0 `  
`ADSpellCastonResist3= `  
`ADSpellDelay3=0 `  
`ADTarCnt3=0 `  
`ADTarType3=1 `  
`ADTarBegHP3=95`  
`ADTarEndHP3=10 `  
`ADIfSpellImmune3= `  
`ADSpellRecast3=0 `  
`ADUseHoTT3=0 `  
`ADPreCondition3=TRUE`  
  
`ADGem4=2`  
`ADSpell4=Klixcxyk's Fire`  
`ADSpellFoci4= `  
`ADDurMod4=0 `  
`ADSpellAlias4=kf `  
`ADAnnounce4=/bc [+m+] `  
`ADSpellMinMana4=10 `  
`ADSpellReCastFour=0 `  
`ADSpellCastonResist4= `  
`ADSpellDelay4=0 `  
`ADTarCnt4=0 `  
`ADTarType4=1 `  
`ADTarBegHP4=95`  
`ADTarEndHP4=10 `  
`ADIfSpellImmune4= `  
`ADSpellRecast4=0 `  
`ADUseHoTT4=0 `  
`ADPreCondition4=TRUE`  
  
`ADGem5=3`  
`ADSpell5=Ethereal Combustion`  
`ADSpellFoci5= `  
`ADDurMod5=0 `  
`ADSpellAlias5=ec`  
`ADAnnounce5=/bc [+m+] `  
`ADSpellMinMana5=10 `  
`ADSpellRecast5=0 `  
`ADSpellCastonResist5= `  
`ADSpellDelay5=0 `  
`ADTarCnt5=0 `  
`ADTarType5=1 `  
`ADTarBegHP5=95`  
`ADTarEndHP5=10 `  
`ADIfSpellImmune5= `  
`ADUseHoTT5=0 `  
`ADPreCondition5=TRUE`  
  
`ADGem6=script `  
`ADSpell6=setNormalOrder `  
`ADSpellFoci6= `  
`ADDurMod6=0 `  
`ADSpellAlias6=setNormalOrder `  
`ADAnnounce6=`  
`ADSpellMinMana6=10 `  
`ADSpellRecast6=0 `  
`ADSpellCastonResist6= `  
`ADSpellDelay6=0 `  
`ADTarCnt6=1 `  
`ADTarType6=1 `  
`ADTarBegHP6=95`  
`ADTarEndHP6=10 `  
`ADIfSpellImmune6= `  
`ADUseHoTT6=0 `  
`ADPreCondition6=TRUE`  
  
`[AdvBuff] `  
`ABCount=6`  
`ABMobMax=18 `  
`ABCheckTime=8 `  
`ABProactive=TRUE `  
  
`ABGem1=6`  
`ABSpell1=Shield of the Void Rk. II`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=Shield`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=20`  
`ABTarCnt1=0`  
`ABTarType1=self`  
`ABRecast1=TRUE`  
`ABSpellIcon1=`  
  
`ABGem2=7`  
`ABSpell2=Squamae of the Crystalwing`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=Rune`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=20`  
`ABTarCnt2=1`  
`ABTarType2=self`  
`ABRecast2=TRUE`  
`ABSpellIcon2=`  
  
`ABGem3=alt`  
`ABSpell3=Pyromancy`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=mancy`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=1`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=TRUE`  
`ABSpellIcon3=`  
  
`ABGem4=item`  
`ABSpell4=Bloodseeker's Veil`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=form`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=TRUE`  
`ABSpellIcon4=`  
  
`ABGem5=item`  
`ABSpell5=Staff of Phenomenal Power`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=epic`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=1`  
`ABTarType5=cbt`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
  
`ABGem6=script`  
`ABSpell6=Evacuate`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=evac`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=20`  
`ABTarCnt6=0`  
`ABTarType6=self`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
  
`[AdvEvent] `  
`AECount=2 `  
`AECheckTime=8 `  
  
`AEGem1=alt `  
`AESpell1=Harvest of Druzzil `  
`AESpellFoci1= `  
`AEDurMod1=0 `  
`AEDelay1=0 `  
`AEEventMinMana1=1 `  
`AEEventMinHP1=35 `  
`AEMinMana1=1 `  
`AEMaxMana1=80 `  
`AEMinHP1=30 `  
`AEMaxHP1=100 `  
`AETarType1=self `  
`AESpellAlias1= `  
`AEAnnounce1=/bc `  
`AETarCnt1=1 `  
  
`AEGem2=script `  
`AESpell2=Harvest `  
`AESpellFoci2= `  
`AEDurMod2=0 `  
`AEDelay2=0 `  
`AEEventMinMana2=1 `  
`AEEventMinHP2=35 `  
`AEMinMana2=1 `  
`AEMaxMana2=30 `  
`AEMinHP2=30 `  
`AEMaxHP2=100 `  
`AETarType2=self `  
`AESpellAlias2= `  
`AEAnnounce2=/bc `  
`AETarCnt2=1 `  
  
`[AdvPull] `  
`APCheckTime=0 `  
`APRadius=40 `  
`APMobMax=1 `  
`APScript= `  
`APPath= `  
`APRetPath= `  
`APBefore= `  
`APAfter= `  
`APAnnounce= `  
`APRetries=1`  
  
`[AdvCure] `  
`AQCount=0 `  
  
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
`C11=/if ({nextCast}==2 && {Me.Song[Flashflames Singe].ID}) /multiline ; /varset nextCast 4 ; /varcalc CastFour {CastFour}+1 ; /varset ADTarCnt[4] 1 ; /echo 4 ; /return `  
`C12=/if ({nextCast}==2) /multiline ; /varset nextCast 3 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return `  
`C13=/if ({nextCast}==4) /multiline ; /varset nextCast 2 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset CastFour 0 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return `  
  
`[Script-Harvest] `  
`Commands=6`  
`C1=/if (!{Me.Gem[Serene Harvest]}) /memorize ''Serene Harvest|gem8''`  
`C2=/if ({Me.Casting.ID}) /delay 5s {Cast.Ready} `  
`C3=/if (!{Cast.Ready[Serene Harvest]}) /return `  
`C4=/if ({Cast.Ready[Serene Harvest]}) /call MQ2Cast ''Serene Harvest'' gem8 6s `  
`C5=/varset Timer 20s `  
`C6=/delay 15s !{Me.Buff[Serene Harvest].ID}`  
  
`[Script-Evacuate] `  
`Commands=4`  
`C1=/if (!{Me.Gem[Evacuate]}) /memorize ''Evacuate|gem9'' `  
`C2=/if ({Me.Casting.ID}) /delay 5s {Cast.Ready} `  
`C3=/if ({Cast.Ready[Exodus]}) /call MQ2Cast ''Exodus'' alt 6s `  
`C4=/if ({Cast.Ready[Evacuate]}) /call MQ2Cast ''Evacuate'' gem9 6s`

## Level 100

`[Settings]`  
`DoMelee=TRUE`  
`DoHeals=FALSE`  
`DoBuffs=TRUE`  
`DoDebuffs=TRUE`  
`DoEvents=TRUE`  
`DoCures=FALSE`  
`DoPull=FALSE`  
`DoPet=TRUE`  
`DoSit=TRUE`  
`DoLoot=FALSE`  
`DoFW=FALSE`  
`DoForage=FALSE`  
`ForageIni=forage.ini`  
`DoAfk=FALSE`  
`DoMount=FALSE`  
`MountCast=Tan Chain Bridle|item`  
`MasterList=${NetBots.Client} `  
`TankName=`  
`Radius=100`  
`SitAggroRadiusCheck=75`  
`AfkMessage=Not now, thanks`  
`DeathSlot=FALSE`  
`NetworkINI=`  
`TraderName=`  
`FollowDistance=20`  
`FollowStick=20 hold uw`  
`PetCast=Kerafyrm's Prismatic Familiar|alt -invis`  
`PetAggro=FALSE`  
`PetAssist=0`  
`PetFoci=`  
`PetShrink=FALSE`  
`PetShrinkSpell=`  
`GoMNuke=weave`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=100`  
`ACAssistPct=98`  
`ACManaPct=101`  
`ACAnnounce=/bc`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=/multiline ; /varset nextCast 0;/varset CastOne 0;/varset CastTwo 0;/varset CastThree 0;/varset CastFour 0 `  
  
`[AdvHeal]`  
`AHCount=0`  
  
`[AdvDebuff]`  
`ADCount=6`  
`ADMobMax=100`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`ADGem1=4`  
`ADSpell1=Claw of the Flamewing`  
`ADSpellFoci1=`  
`ADDurMod1=0`  
`ADSpellAlias1=Claw`  
`ADAnnounce1=/bc [+m+]`  
`ADSpellMinMana1=10`  
`ADSpellRecast1=0`  
`ADSpellCastonResist1=`  
`ADSpellDelay1=0`  
`ADTarCnt1=0`  
`ADTarType1=1`  
`ADTarBegHP1=98`  
`ADTarEndHP1=0`  
`ADIfSpellImmune1=`  
`ADUseHoTT1=0`  
`ADPreCondition1=TRUE`  
  
`ADGem2=1`  
`ADSpell2=Incandescent Vortex`  
`ADSpellFoci2=`  
`ADDurMod2=0`  
`ADSpellAlias2=thrice`  
`ADAnnounce2=/bc [+m+]`  
`ADSpellMinMana2=10`  
`ADSpellRecast2=0`  
`ADSpellCastonResist2=`  
`ADSpellDelay2=0`  
`ADTarCnt2=0`  
`ADTarType2=1`  
`ADTarBegHP2=98`  
`ADTarEndHP2=0`  
`ADIfSpellImmune2=`  
`ADUseHoTT2=0`  
`ADPreCondition2=TRUE`  
  
`ADGem3=2`  
`ADSpell3=Gosik's Fire`  
`ADSpellFoci3=`  
`ADDurMod3=0`  
`ADSpellAlias3=fire`  
`ADAnnounce3=/bc [+m+]`  
`ADSpellMinMana3=10`  
`ADSpellRecast3=0`  
`ADSpellCastonResist3=`  
`ADSpellDelay3=0`  
`ADTarCnt3=0`  
`ADTarType3=1`  
`ADTarBegHP3=98`  
`ADTarEndHP3=0`  
`ADIfSpellImmune3=`  
`ADUseHoTT3=0`  
`ADPreCondition3=TRUE`  
  
`ADGem4=6`  
`ADSpell4=Ethereal Incandescence`  
`ADSpellFoci4=`  
`ADDurMod4=0`  
`ADSpellAlias4=eth`  
`ADAnnounce4=/bc [+m+]`  
`ADSpellMinMana4=10`  
`ADSpellRecast4=0`  
`ADSpellCastonResist4=`  
`ADSpellDelay4=0`  
`ADTarCnt4=0`  
`ADTarType4=1`  
`ADTarBegHP4=98`  
`ADTarEndHP4=0`  
`ADIfSpellImmune4=`  
`ADUseHoTT4=0`  
`ADPreCondition4=TRUE`  
  
`ADGem5=script`  
`ADSpell5=setNormalOrder`  
`ADSpellFoci5=`  
`ADDurMod5=0`  
`ADSpellAlias5=setNormalOrder`  
`ADAnnounce5=`  
`ADSpellMinMana5=10`  
`ADSpellRecast5=0`  
`ADSpellCastonResist5=`  
`ADSpellDelay5=0`  
`ADTarCnt5=1`  
`ADTarType5=1`  
`ADTarBegHP5=98`  
`ADTarEndHP5=0`  
`ADIfSpellImmune5=`  
`ADUseHoTT5=0`  
`ADPreCondition5=TRUE`  
  
`ADGem6=5`  
`ADSpell6=Ethereal Weave`  
`ADSpellFoci6=`  
`ADDurMod6=0`  
`ADSpellAlias6=weave`  
`ADAnnounce6=`  
`ADSpellMinMana6=10`  
`ADSpellRecast6=0`  
`ADSpellCastonResist6=`  
`ADSpellDelay6=0`  
`ADTarCnt6=0`  
`ADTarType6=1`  
`ADTarBegHP6=98`  
`ADTarEndHP6=0`  
`ADIfSpellImmune6=`  
`ADUseHoTT6=0`  
`ADPreCondition6=TRUE`  
  
`[AdvBuff]`  
`ABCount=14`  
`ABMobMax=100`  
`ABCheckTime=8`  
  
`ABGem1=8`  
`ABSpell1=Shield of the Dauntless`  
`ABSpellFoci1=`  
`ABDurMod1=0`  
`ABSpellAlias1=shield`  
`ABAnnounce1=/bc`  
`ABSpellMinMana1=10`  
`ABTarCnt1=1`  
`ABTarType1=self`  
`ABRecast1=FALSE`  
`ABSpellIcon1=`  
`ABPreCondition1=TRUE`  
  
`ABGem2=10`  
`ABSpell2=Armor of the Stonescale`  
`ABSpellFoci2=`  
`ABDurMod2=0`  
`ABSpellAlias2=rune`  
`ABAnnounce2=/bc`  
`ABSpellMinMana2=10`  
`ABTarCnt2=1`  
`ABTarType2=self`  
`ABRecast2=FALSE`  
`ABSpellIcon2=`  
`ABPreCondition2=TRUE`  
  
`ABGem3=alt`  
`ABSpell3=Pyromancy`  
`ABSpellFoci3=`  
`ABDurMod3=0`  
`ABSpellAlias3=mancy`  
`ABAnnounce3=/bc`  
`ABSpellMinMana3=0`  
`ABTarCnt3=1`  
`ABTarType3=self`  
`ABRecast3=FALSE`  
`ABSpellIcon3=`  
`ABPreCondition3=TRUE`  
  
`ABGem4=item`  
`ABSpell4=Roon's Tunic`  
`ABSpellFoci4=`  
`ABDurMod4=0`  
`ABSpellAlias4=spikes`  
`ABAnnounce4=/bc`  
`ABSpellMinMana4=0`  
`ABTarCnt4=1`  
`ABTarType4=self`  
`ABRecast4=FALSE`  
`ABSpellIcon4=`  
`ABPreCondition4=TRUE`  
  
`ABGem5=item`  
`ABSpell5=Double Hoop of Tegleth`  
`ABSpellFoci5=`  
`ABDurMod5=0`  
`ABSpellAlias5=geo1`  
`ABAnnounce5=/bc`  
`ABSpellMinMana5=0`  
`ABTarCnt5=0`  
`ABTarType5=self`  
`ABRecast5=FALSE`  
`ABSpellIcon5=`  
`ABPreCondition5=TRUE`  
  
`ABGem6=item`  
`ABSpell6=The Depthkeeper's Ever-Glaring Eye`  
`ABSpellFoci6=`  
`ABDurMod6=0`  
`ABSpellAlias6=geo2`  
`ABAnnounce6=/bc`  
`ABSpellMinMana6=0`  
`ABTarCnt6=0`  
`ABTarType6=self`  
`ABRecast6=FALSE`  
`ABSpellIcon6=`  
`ABPreCondition6=TRUE`  
  
`ABGem7=item`  
`ABSpell7=Face of Dread`  
`ABSpellFoci7=`  
`ABDurMod7=0`  
`ABSpellAlias7=end`  
`ABAnnounce7=/bc`  
`ABSpellMinMana7=0`  
`ABTarCnt7=1`  
`ABTarType7=self`  
`ABRecast7=FALSE`  
`ABSpellIcon7=`  
`ABPreCondition7=TRUE`  
  
`ABGem8=item`  
`ABSpell8=Brilliant Band of Arcane Knowledge`  
`ABSpellFoci8=`  
`ABDurMod8=0`  
`ABSpellAlias8=past1`  
`ABAnnounce8=/bc`  
`ABSpellMinMana8=0`  
`ABTarCnt8=0`  
`ABTarType8=self`  
`ABRecast8=FALSE`  
`ABSpellIcon8=`  
`ABPreCondition8=TRUE`  
  
`ABGem9=item`  
`ABSpell9=Bixie Mage Band`  
`ABSpellFoci9=`  
`ABDurMod9=0`  
`ABSpellAlias9=past2`  
`ABAnnounce9=/bc`  
`ABSpellMinMana9=0`  
`ABTarCnt9=1`  
`ABTarType9=self`  
`ABRecast9=FALSE`  
`ABSpellIcon9=`  
`ABPreCondition9=TRUE`  
  
`ABGem10=item`  
`ABSpell10=Featherweight Drape of Harmony`  
`ABSpellFoci10=`  
`ABDurMod10=0`  
`ABSpellAlias10=dodge`  
`ABAnnounce10=/bc`  
`ABSpellMinMana10=0`  
`ABTarCnt10=1`  
`ABTarType10=self`  
`ABRecast10=FALSE`  
`ABSpellIcon10=`  
`ABPreCondition10=TRUE`  
  
`ABGem11=item`  
`ABSpell11=Burning Belt of Endless Shadow`  
`ABSpellFoci11=`  
`ABDurMod11=0`  
`ABSpellAlias11=mind`  
`ABAnnounce11=/bc`  
`ABSpellMinMana11=0`  
`ABTarCnt11=1`  
`ABTarType11=self`  
`ABRecast11=FALSE`  
`ABSpellIcon11=`  
`ABPreCondition11=TRUE`  
  
`ABGem12=item`  
`ABSpell12=Compendium of Antonican Creatures`  
`ABSpellFoci12=`  
`ABDurMod12=0`  
`ABSpellAlias12=ward`  
`ABAnnounce12=/bc`  
`ABSpellMinMana12=0`  
`ABTarCnt12=1`  
`ABTarType12=self`  
`ABRecast12=FALSE`  
`ABSpellIcon12=`  
`ABPreCondition12=TRUE`  
  
`ABGem13=script`  
`ABSpell13=Evacuate`  
`ABSpellFoci13=`  
`ABDurMod13=0`  
`ABSpellAlias13=evac`  
`ABAnnounce13=/bc`  
`ABSpellMinMana13=10`  
`ABTarCnt13=0`  
`ABTarType13=self`  
`ABRecast13=FALSE`  
`ABSpellIcon13=`  
`ABPreCondition13=TRUE`  
  
`ABGem14=item`  
`ABSpell14=Ring of the Ancients`  
`ABSpellFoci14=`  
`ABDurMod14=0`  
`ABSpellAlias14=shrink`  
`ABAnnounce14=/bc`  
`ABSpellMinMana14=10`  
`ABTarCnt14=0`  
`ABTarType14=self`  
`ABRecast14=FALSE`  
`ABSpellIcon14=`  
`ABPreCondition14=TRUE`  
  
`[AdvEvent]`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECount=2`  
`AECheckTime=8`  
  
`AEGem1=alt`  
`AESpell1=Harvest of Druzzil`  
`AESpellFoci1=`  
`AEDurMod1=0`  
`AEDelay1=0`  
`AEEventMinMana1=1`  
`AEEventMinHP1=35`  
`AEMinMana1=1`  
`AEMaxMana1=80`  
`AEMinHP1=30`  
`AEMaxHP1=100`  
`AETarType1=self`  
`AESpellAlias1=druz`  
`AEAnnounce1=/bc`  
`AETarCnt1=1`  
  
`AEGem2=script`  
`AESpell2=Harvest`  
`AESpellFoci2=`  
`AEDurMod2=0`  
`AEDelay2=0`  
`AEEventMinMana2=1`  
`AEEventMinHP2=35`  
`AEMinMana2=1`  
`AEMaxMana2=30`  
`AEMinHP2=30`  
`AEMaxHP2=100`  
`AETarType2=self`  
`AESpellAlias2=harv`  
`AEAnnounce2=/bc`  
`AETarCnt2=1`  
  
`[AdvPull]`  
`APCheckTime=0`  
`APRadius=40`  
`APMobMax=1`  
`APScript=`  
`APPath=`  
`APRetPath=`  
`APBefore=`  
`APAfter=`  
`APAnnounce=`  
`APRetries=1`  
  
`[AdvCure]`  
`AQCount=0`  
  
`[Script-setNormalOrder] `  
`Commands=13 `  
`C1=/if (!{Defined[nextCast]}) /declare nextCast int outer 0; `  
`C2=/if (!{Defined[CastOne]}) /declare CastOne int outer 0; `  
`C3=/if (!{Defined[CastTwo]}) /declare CastTwo int outer 0; `  
`C4=/if (!{Defined[CastThree]}) /declare CastThree int outer 0; `  
`C5=/if (!{Defined[CastFour]}) /declare CastFour int outer 0; `  
`C6=/multiline ; /varset ADTarCnt[1] 0 ; /varset ADTarCnt[2] 0 ; /varset ADTarCnt[3] 0 ; /varset ADTarCnt[4] 0`  
`C7=/if ({nextCast}==0) /multiline ; /varset nextCast 1 ; /varcalc CastOne {CastOne}+1 ; /varset ADTarCnt[1] 1 ; /echo 1 ; /return `  
`C8=/if ({nextCast}==1) /multiline ; /varset nextCast 3 ; /varcalc CastThree {CastThree}+1 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return `  
`C9=/if ({nextCast}==3 && {CastOne}<=1) /multiline ; /varset nextCast 1 ; /varcalc CastOne {CastOne}+1 ; /varset ADTarCnt[1] 1 ; /echo 1 ; /return `  
`C10=/if ({nextCast}==3 && {CastOne}>1) /multiline ; /varset nextCast 2 ; /varcalc CastTwo {CastTwo}+1 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return `  
`C11=/if ({nextCast}==2 && {Me.Song[Aria of Va'Ker].ID}) /multiline ; /varset nextCast 4 ; /varcalc CastFour {CastFour}+1 ; /varset ADTarCnt[4] 1 ; /echo 4 ; /return `  
`C12=/if ({nextCast}==2) /multiline ; /varset nextCast 3 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset ADTarCnt[3] 1 ; /echo 3 ; /return `  
`C13=/if ({nextCast}==4) /multiline ; /varset nextCast 2 ; /varset CastOne 0 ; /varset CastTwo 0 ; /varset CastThree 0 ; /varset CastFour 0 ; /varset ADTarCnt[2] 1 ; /echo 2 ; /return `  
  
`[Script-Harvest] `  
`Commands=6`  
`C1=/if (!{Me.Gem[Placid Harvest]}) /memorize ''Placid Harvest|gem7''`  
`C2=/if ({Me.Casting.ID}) /delay 5s {Cast.Ready} `  
`C3=/if (!{Cast.Ready[Placid Harvest]}) /return `  
`C4=/if ({Cast.Ready[Placid Harvest]}) /call MQ2Cast ''Placid Harvest'' gem7 6s `  
`C5=/varset Timer 20s `  
`C6=/delay 15s !{Me.Buff[Placid Harvest].ID}`  
  
`[Script-Evacuate] `  
`Commands=4`  
`C1=/if (!{Me.Gem[Evacuate]}) /memorize ''Evacuate|gem12'' `  
`C2=/if ({Me.Casting.ID}) /delay 5s {Cast.Ready} `  
`C3=/if ({Cast.Ready[Exodus]}) /call MQ2Cast ''Exodus'' alt 6s `  
`C4=/if ({Cast.Ready[Evacuate]}) /call MQ2Cast ''Evacuate'' gem12 6s`

No Monk Scripts Available please add

# Warrior

## Level 80

With 2.0 Bazu Bellow set up on hotkey 1

` [Settings] `  
` DoMelee=TRUE `  
` DoHeals=TRUE`  
` DoBuffs=FALSE`  
` DoDebuffs=FALSE`  
` DoEvents=FALSE`  
` DoCures=FALSE`  
` DoPull=TRUE`  
` DoPet=FALSE`  
` DoSit=FALSE`  
` DoLoot=FALSE`  
` DoFW=FALSE`  
` DoForage=FALSE`  
` DoAfk=FALSE`  
` DoMount=FALSE`  
` MountCast=`  
` DoAura=TRUE`  
` AuraCast=Champion's Aura|disc`  
` MasterList=`  
` TankName=`  
` ExcludeList=`  
` Radius=100`  
` SitAggroRadiusCheck=75`  
` AfkMessage=Not now, thanks`  
` DeathSlot=`  
` FollowDistance=20`  
` FollowStick=20 hold uw`  
` ForageIni=forage.ini`  
  
` [Melee]`  
` OffTank=FALSE`  
` ACLeash=50`  
` ACAssistPct=100`  
` ACManaPct=10`  
` ACAnnounce=/bc`  
` ACMeleeCmd=/melee plugin=1 aggro=1`  
` ACBefore=`  
` ACAfter=`  
  
` [AdvHeal]`  
` AHCount=0`  
  
` [AdvDebuff]`  
` ADCount=0`  
` ADMobMax=25`  
` ADCheckTime=2`  
` ADAggroOnly=0`  
` ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
` [AdvBuff]`  
` ABCount=3`  
` ABMobMax=25`  
` ABCheckTime=1`  
` ABProactive=TRUE`  
  
` ABGem1=item`  
` ABSpell1=Cobalt Bracer`  
` ABSpellFoci1=`  
` ABDurMod1=0`  
` ABSpellAlias1=shrink`  
` ABAnnounce1=/bc`  
` ABSpellMinMana1=0`  
` ABTarCnt1=0`  
` ABTarType1=self war shd pal rng mnk rog brd bst ber shm clr dru wiz mag enc nec`  
` ABRecast1=FALSE`  
  
` ABGem2=item`  
` ABSpell2=Kreljnok's Sword of Eternal Power`  
` ABSpellFoci2=`  
` ABDurMod2=0`  
` ABSpellAlias2=epic`  
` ABAnnounce2=/bc`  
` ABSpellMinMana2=0`  
` ABTarCnt2=1`  
` ABTarType2=self cbt`  
` ABRecast2=FALSE`  
  
` ABGem3=item`  
` ABSpell3=Girdle of Intense Durability`  
` ABSpellFoci3=`  
` ABDurMod3=0`  
` ABSpellAlias3=ds`  
` ABAnnounce3=/bc`  
` ABSpellMinMana3=0`  
` ABTarCnt3=1`  
` ABTarType3=self`  
` ABRecast3=FALSE`  
  
` [AdvEvent]`  
` AECount=0`  
  
` [AdvPull]`  
` APCheckTime=0`  
` APRadius=60`  
` APMobMax=20`  
` APScript=Pull`  
` APPath=`  
` APBefore=`  
` APAfter=`  
` APAnnounce=/gsay Incoming -[ %t ]-`  
` APRetPath=`  
  
` [AdvCure]`  
` AQCount=0`  
  
` [Script-Pull]`  
` Commands=3`  
` C1=/if ({Me.AbilityReady[Taunt]}) /doability Taunt`  
` C2=/delay 5`  
` C3=/if ({Me.CombatAbilityReady[Bazu Bellow]}) /keypress 1`

## Level 85

Setup as Puller and Main Tank (Requires you setup a waypoint file using MBWayrec)

` [Settings] `  
` DoMelee=TRUE`  
` DoHeals=FALSE`  
` DoBuffs=TRUE`  
` DoDebuffs=TRUE`  
` DoEvents=FALSE`  
` DoCures=FALSE`  
` DoPull=True`  
` DoPet=TRUE`  
` DoSit=TRUE`  
` DoLoot=FALSE`  
` DoFW=FALSE`  
` DoForage=FALSE`  
` DoAfk=FALSE`  
` DoMount=FALSE`  
` MountCast=`  
` DoAura=TRUE`  
` AuraCast=Myrmidon's Aura|disc`  
` MasterList=${NetBots.Client}`  
` TankName=${Me.CleanName}`  
` Radius=185`  
` SitAggroRadiusCheck=55`  
` AfkMessage=Not now, thanks`  
` DeathSlot=FALSE`  
` FollowDistance=20`  
` FollowStick=20 hold uw`  
` PetCast=`  
` PetAggro=False`  
` PetAssist=0`  
` ForageIni=forage.ini`  
` NetworkINI=`  
` TraderName=`  
  
` [Melee] `  
` OffTank=FALSE`  
` ACLeash=35`  
` ACAssistPct=110`  
` ACManaPct=70`  
` ACAnnounce=`  
` ACMeleeCmd=/melee plugin=1 taunt=1 stickrange=125 facing=1`  
` ACBefore`  
` ACAnnounce=`  
` ACBefore=`  
` ACAfter=/stick 12`  
  
` [AdvHeal]`  
` AHCount=0`  
  
` [AdvDebuff]`  
` ADCount=1`  
` ADMobMax=50`  
` ADCheckTime=2`  
` ADAggroOnly=0`  
` ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
` ADGem1=alt`  
` ADSpell1=Area Taunt`  
` ADSpellFoci1=`  
` ADDurMod1=0`  
` ADSpellAlias1=AT`  
` ADAnnounce1=/bc Taunting All Area`  
` ADSpellMinMana1=0`  
` ADSpellRecast1=0`  
` ADSpellDelay1=0`  
` ADTarCnt1=2`  
` ADTarType1=11`  
` ADTarBegHP1=98`  
` ADTarEndHP1=5`  
` ADSpellCastonResist1=`  
` ADIfSpellImmune1=`  
` ADUseHoTT1=FALSE`  
  
` [AdvBuff]`  
` ABCount=5`  
` ABMobMax=50`  
` ABCheckTime=8`  
` ABProactive=TRUE`  
  
` ABGem1=item`  
` ABSpell1=Greasy Steam-Pauldrons`  
` ABSpellFoci1=`  
` ABDurMod1=0`  
` ABSpellAlias1=pauld`  
` ABAnnounce1=/bc`  
` ABSpellMinMana1=0`  
` ABTarCnt1=1`  
` ABTarType1=self`  
` ABRecast1=FALSE`  
` ABSpellIcon1=`  
  
` ABGem2=item`  
` ABSpell2=Earstud of a Mother's Love`  
` ABSpellFoci2=`  
` ABDurMod2=0`  
` ABSpellAlias2=Might`  
` ABAnnounce2=/bc`  
` ABSpellMinMana2=0`  
` ABTarCnt2=1`  
` ABTarType2=self`  
` ABRecast2=FALSE`  
` ABSpellIcon2=`  
  
` ABGem3=item`  
` ABSpell3=Kizrak's Gauntlets of Battle`  
` ABSpellFoci3=`  
` ABDurMod3=0`  
` ABSpellAlias3=haste`  
` ABAnnounce3=/bc [+g+]`  
` ABSpellMinMana3=0`  
` ABTarCnt3=1`  
` ABTarType3=self`  
` ABRecast3=FALSE`  
` ABSpellIcon3=`  
  
` ABGem4=item`  
` ABSpell4=Familiar of the Hooded Scrykin`  
` ABSpellFoci4=`  
` ABDurMod4=0`  
` ABSpellAlias4=pet`  
` ABAnnounce4=/bc`  
` ABSpellMinMana4=0`  
` ABTarCnt4=1`  
` ABTarType4=self idle`  
` ABRecast4=FALSE`  
` ABSpellIcon4=`  
  
` ABGem5=script`  
` ABSpell5=StoneCheck`  
` ABSpellFoci5=`  
` ABDurMod5=0`  
` ABSpellAlias5=StoneCheck`  
` ABAnnounce5=/bc >> MAKING PULL ITEMS <<`  
` ABSpellMinMana5=0`  
` ABTarCnt5=1`  
` ABTarType5=self`  
` ABRecast5=FALSE`  
` ABSpellIcon5=`  
  
` [AdvEvent]`  
` AECount=0`  
  
` [AdvPull]`  
` APRadius=35`  
` APSpell=`  
` APRangedMod=0`  
` APMobMax=4`  
` APScript=Pull`  
` APBefore=/if (({Spawn[group cleric].ID} && {Spawn[group cleric].CurrentMana}<50 || {Me.PctHPs}<85 || {Me.PctEndurance}<40 || !{Spawn[group cleric].ID} && {Spawn[group shaman].ID} && {Spawn[group shaman].CurrentMana}<30) && {Math.Distance[{Me.Y},{Me.X}:{MakeCampY},{MakeCampX}]}<40 && (!{Spawn[{APTargetID}].ID} || {ACMATarget})) /docommand ${If[${Me.PctHPs}<85,/multiline ; /delay 10s;/echo Waiting for heal,/multiline ; /makecamp return;/varset APCheckTimer 45s;/keypress centerview;/delay 10s;/return]}`  
` APAfter=`  
` APCheckTime=10`  
` APPath=PathFileName`  
` APAnnounce=/gsay Incoming -[ %t ]-`  
` APMobMax=1 `  
` APRetPath=`  
` APRetries=2`  
  
` [AdvCure] `  
` AQCount=0`  
  
` [Script-Pull]`  
` Commands=6`  
` C1=/equipset 2hPull`  
` C2=/if ({Target.Distance3D}>30) /ranged`  
` C3=/if ({Target.Distance3D}<=30) /doability Sneer`  
` C4=/delay 3s {Me.CombatState.Equal[combat]}`  
` C5=/call MBMoveTo {MakeCampY} {MakeCampX}`  
` C6=/equipset 2hFight`  
` [Script-StoneCheck]`  
` Commands=3`  
` C1=/if ({FindItemCount[=Dreadstone]}>=500) /return`  
` C2=/casting "pouch of curses|item"`  
` C3=/delay 6s`  
` [Script-BarbCheck]`  
` Commands=4`  
` C1=/if ({FindItemCount[=Hunter's Barbs]}>=60 || !{FindItemCount[=Purified Crystal]}) /return`  
` C2=/casting "bloody ancille's pouch|item"`  
` C3=/delay 6s`  
` C4=/call ClearCursor`  
` [Script-OffHeal]`  
` Commands=4`  
` C1=/if ({ADMobCount}) /return`  
` C2=/if ({Me.PctHPs}<80) /bc cast hot`  
` C3=/varset ABTarCnt[5] 0`  
` C4=/timed 300 /varset ABTarCnt[5] 1`  
` [Script-Defense]`  
` Commands=0`  
` C1=/return`


