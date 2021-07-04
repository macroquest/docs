# Bard

# Beastlord

# Berserker

# Cleric

# Druid

# Enchanter

# Magician

# Monk

# Necromancer

# Paladin

# Ranger

# Rogue

# Shadow Knight

# Shaman

# Warrior

# Wizard

## Level 75

`[Settings]`  
`DoMelee=FALSE`  
`DoHeals=TRUE`  
`DoBuffs=FALSE`  
`DoDebuffs=FALSE`  
`DoEvents=FALSE`  
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
`MountCast=Tahka's Horse Saddle|Item`  
`MasterList=${NetBots.Client}`  
`TankName=${Group.MainTank.Name}`  
`PullerName=${Group.Puller.Name}`  
`Radius=75`  
`ZRadius=100`  
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
`PetShrink=TRUE`  
`PetShrinkSpell=`  
`GoMNuke=`  
  
`[Melee]`  
`OffTank=FALSE`  
`ACLeash=50`  
`ACAssistPct=95`  
`ACManaPct=101`  
`ACAnnounce=`  
`ACMeleeCmd=/melee plugin=1`  
`ACBefore=`  
`ACAfter=`  
`ACPetEnrage=TRUE`  
  
`[AdvHeal]`  
`AHCount=0`  
`AHNewFormat=1`  
`AHCheckTime=2`  
`AHHealOOBC=FALSE`  
`AHHealMode=0|0|12`  
`AHInterruptLevel=2`  
`AHClassPriority=enc,wiz,mag,nec,clr,dru,shm,pal,shd,war,bst,rng,ber,rog,brd,mnk`  
`AHAllowDismount=TRUE`  
  
`[AdvDebuff]`  
`ADCount=12`  
`ADNewFormat=1`  
`ADMobMax=20`  
`ADCheckTime=0`  
`ADAggroOnly=0`  
`ADHold=0|1|1|   1=on 0=off|Debuff spell #|Time to wait for debuff|`  
  
`[AD1]`  
`Gem=Alt`  
`Spell=Silent Casting`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=SilentCast`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=3`  
`TarBegHP=100`  
`TarEndHP=50`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=TRUE`  
`[AD2]`  
`Gem=Alt`  
`Spell=Arcane Whisper`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=AAHateReduc`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=3`  
`TarBegHP=95`  
`TarEndHP=25`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.PctAggro}>95) /return TRUE`  
`[AD3]`  
`Gem=Alt`  
`Spell=Mind Crash`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=MindCrash|AAConcussion`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=20`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.PctAggro}>85) /return TRUE`  
`[AD4]`  
`Gem=1`  
`Spell=Claw of Selay`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Nuke1|IceLure`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=10`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.PctAggro}<85 && !{Me.Song[Concussive Chill].ID} && !{Me.Song[Concussive Magic].ID} && !{Me.Song[Concussive Flames].ID}) /return TRUE`  
`[AD5]`  
`Gem=7`  
`Spell=Concussive Burst`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=`  
`Announce=/bc`  
`SpellMinMana=5`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=96`  
`TarEndHP=20`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if (!{Me.Song[Concussive Chill].ID} && !{Me.Song[Concussive Magic].ID} && !{Me.Song[Concussive Flames].ID}) /return TRUE`  
`[AD6]`  
`Gem=2`  
`Spell=Icefall Avalanche`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Nuke2|IceNuke`  
`Announce=/bc`  
`SpellMinMana=5`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=20`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.Song[Concussive Chill].ID}) /return TRUE`  
`[AD7]`  
`Gem=3`  
`Spell=Rolling Lightning`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Nuke3|MagicNuke`  
`Announce=/bc`  
`SpellMinMana=5`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=20`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.Song[concussive Magic].ID}) /return TRUE`  
`[AD8]`  
`Gem=4`  
`Spell=Ethereal Conflagration`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Nuke4|FireNuke`  
`Announce=/bc`  
`SpellMinMana=5`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=20`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.Song[Concussive Flames].ID}) /return TRUE`  
`[AD9]`  
`Gem=Alt`  
`Spell=Force of Will`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=AANuke`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=5`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.PctAggro}<85) /return TRUE`  
`[AD10]`  
`Gem=Alt`  
`Spell=Banestrike`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=60`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=95`  
`TarEndHP=15`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=/if ({Me.PctAggro}<85) /return TRUE`  
`[AD11]`  
`Gem=5`  
`Spell=Telakisz`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Stun`  
`Announce=/bc`  
`SpellMinMana=5`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=1`  
`TarBegHP=15`  
`TarEndHP=0`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=TRUE`  
`[AD12]`  
`Gem=Alt`  
`Spell=Call of Xuzl`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=swarm2`  
`Announce=/bc`  
`SpellMinMana=0`  
`SpellRecast=0`  
`SpellCastonResist=`  
`SpellDelay=0`  
`TarCnt=1`  
`TarType=3`  
`TarBegHP=95`  
`TarEndHP=75`  
`IfSpellImmune=`  
`UseHoTT=0`  
`PreCondition=TRUE`  
  
`[AdvBuff]`  
`ABCount=8`  
`ABNewFormat=1`  
`ABMobMax=18`  
`ABCheckTime=8`  
  
`[AB1]`  
`Gem=10`  
`Spell=Bulwark of the Crystalwing`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Shielding`  
`Announce=/bc`  
`SpellMinMana=10`  
`TarCnt=1`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
`[AB2]`  
`Gem=10`  
`Spell=Laminae of the Crystalwing`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Rune`  
`Announce=/bc`  
`SpellMinMana=10`  
`TarCnt=1`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
`[AB3]`  
`Gem=Alt`  
`Spell=E'ci's Icy Familiar`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=IceFamiliar`  
`Announce=/bc`  
`SpellMinMana=0`  
`TarCnt=1`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=E'ci's Icy Familiar III`  
`PreCondition=TRUE`  
`[AB4]`  
`Gem=Alt`  
`Spell=Cryomancy`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Cryomancy`  
`Announce=/bc`  
`SpellMinMana=0`  
`TarCnt=1`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
`[AB5]`  
`Gem=Alt`  
`Spell=Group Perfected Invisibility`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=GrpInvis|`  
`Announce=/bc`  
`SpellMinMana=0`  
`TarCnt=0`  
`TarType=Self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
`[AB6]`  
`Gem=Alt`  
`Spell=Teleport Bind`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=PortBind|`  
`Announce=`  
`SpellMinMana=0`  
`TarCnt=0`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
`[AB7]`  
`Gem=Alt`  
`Spell=Exodus`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=Exodus|Evac`  
`Announce=/bc`  
`SpellMinMana=0`  
`TarCnt=0`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
`[AB8]`  
`Gem=10`  
`Spell=Knowledge Portal`  
`SpellFoci=`  
`DurMod=0`  
`SpellAlias=PortPoK`  
`Announce=`  
`SpellMinMana=0`  
`TarCnt=0`  
`TarType=self`  
`Recast=FALSE`  
`SpellIcon=`  
`PreCondition=TRUE`  
  
`[AdvEvent]`  
`AECount=2`  
`AENewFormat=1`  
`AECustom1=`  
`AECustom2=`  
`AECustom3=`  
`AECheckTime=8`  
  
`[AE1]`  
`Gem=alt`  
`Spell=Harvest of Druzzil`  
`SpellFoci=`  
`DurMod=0`  
`Delay=0`  
`EventMinMana=1`  
`EventMinHP=50`  
`MinMana=1`  
`MaxMana=75`  
`MinHP=50`  
`MaxHP=100`  
`TarType=self`  
`SpellAlias=AAHarvest`  
`Announce=/bc`  
`TarCnt=1`  
`[AE2]`  
`Gem=8`  
`Spell=Tranquil Harvest`  
`SpellFoci=`  
`DurMod=0`  
`Delay=0`  
`EventMinMana=1`  
`EventMinHP=50`  
`MinMana=1`  
`MaxMana=65`  
`MinHP=50`  
`MaxHP=100`  
`TarType=self`  
`SpellAlias=Harvest`  
`Announce=/bc`  
`TarCnt=1`  
  
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
`AQNewFormat=1`


