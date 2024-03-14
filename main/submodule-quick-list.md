# Plugin repository Quick List

A quick list of plugins that have been migrated and how to add them.  Once they're all added, you may need to initialize submodules for any plugins which have any.

You can initialize submodules of any plugin which has them with:  
Using Git Bash:  `find ./plugins -maxdepth 1 -type d -exec git -C {} submodule update --init --recursive \;`  
Using PowerShell:  `Get-ChildItem -Directory -Force -Recurse *.git | ForEach-Object { cd $_.Parent.FullName; Write-Host $_.Parent.FullName; git submodule update --init --recursive }`  

You can quickly update your plugins with:  
Using Git Bash:  `find ./plugins -maxdepth 1 -type d -exec git -C {} pull \;`  
Using PowerShell:  `Get-ChildItem -Directory -Force -Recurse *.git | ForEach-Object { cd $_.Parent.FullName; Write-Host $_.Parent.FullName; git pull }`  

The solution file with all of these in it is here: [MacroQuestCustom.sln](../uploads/MacroQuestCustom.sln) (place this file in the src folder beside MacroQuest.sln)

```bash
git clone -b master https://github.com/RedGuides/MQ2AASpend.git plugins/MQ2AASpend
git clone -b master https://github.com/RedGuides/MQ2AdvPath.git plugins/MQ2AdvPath
git clone -b master https://github.com/RedGuides/MQ2AutoAccept.git plugins/MQ2AutoAccept
git clone -b master https://github.com/RedGuides/MQ2AutoCamp.git plugins/MQ2AutoCamp
git clone -b master https://github.com/RedGuides/MQ2AutoClaim.git plugins/MQ2AutoClaim
git clone -b master https://github.com/RedGuides/MQ2AutoForage.git plugins/MQ2AutoForage
git clone -b master https://github.com/RedGuides/MQ2AutoGroup.git plugins/MQ2AutoGroup
git clone -b master https://github.com/RedGuides/MQ2AutoLoot.git plugins/MQ2AutoLoot
git clone -b master https://github.com/RedGuides/MQ2AutoLootSort.git plugins/MQ2AutoLootSort
git clone -b master https://github.com/RedGuides/MQ2AutoSize.git plugins/MQ2AutoSize
git clone -b master https://github.com/RedGuides/MQ2Bandolier.git plugins/MQ2Bandolier
git clone -b master https://github.com/RedGuides/MQ2BardSwap.git plugins/MQ2BardSwap
git clone -b master https://github.com/RedGuides/MQ2Boxr.git plugins/MQ2Boxr
git clone -b master https://github.com/brainiac/MQ2Camera.git plugins/MQ2Camera
git clone -b master https://github.com/RedGuides/MQ2Cast.git plugins/MQ2Cast
git clone -b master https://github.com/RedGuides/MQ2Clipboard.git plugins/MQ2Clipboard
git clone -b master https://github.com/RedGuides/MQ2Collections.git plugins/MQ2Collections
git clone -b master https://github.com/RedGuides/MQ2CPULoad.git plugins/MQ2CPULoad
git clone -b master https://github.com/RedGuides/MQ2Cursor.git plugins/MQ2Cursor
git clone -b master https://github.com/dannuic/MQ2Dan.git plugins/MQ2Dan
git clone -b master https://github.com/RedGuides/MQ2Debuffs.git plugins/MQ2Debuffs
git clone -b master https://gitlab.com/alynel/MQ2Discord.git plugins/MQ2Discord
git clone -b master https://github.com/projecteon/MQ2DotNet.git plugins/MQ2DotNet
git clone -b master https://github.com/RedGuides/MQ2DPSAdv.git plugins/MQ2DPSAdv
git clone -b master https://github.com/brainiac/MQ2EasyFind.git plugins/MQ2EasyFind
git clone -b master https://github.com/RedGuides/MQ2EQBC.git plugins/MQ2EQBC
git clone -b master https://github.com/RedGuides/MQ2Events.git plugins/MQ2Events
git clone -b master https://github.com/RedGuides/MQ2Exchange.git plugins/MQ2Exchange
git clone -b master https://github.com/RedGuides/MQ2FarmTest.git plugins/MQ2FarmTest
git clone -b master https://github.com/RedGuides/MQ2FeedMe.git plugins/MQ2FeedMe
git clone -b master https://github.com/MMOBugs/MQ2GMCheck.git plugins/MQ2GMCheck
git clone -b master https://github.com/RedGuides/MQ2GroupInfo.git plugins/MQ2GroupInfo
git clone -b master https://github.com/RedGuides/MQ2HeadShot.git plugins/MQ2HeadShot
git clone -b master https://github.com/RedGuides/MQ2HUDMove.git plugins/MQ2HUDMove
git clone -b master https://github.com/RedGuides/MQ2Ice.git plugins/MQ2Ice
git clone -b main https://gitlab.com/Ortster/MQItemColor.git plugins/MQItemColor
git clone -b master https://github.com/RedGuides/MQ2ItemScore.git plugins/MQ2ItemScore
git clone -b master https://github.com/RedGuides/MQ2KillTracker.git plugins/MQ2KillTracker
git clone -b master https://github.com/RedGuides/MQ2KissTemplate.git plugins/MQ2KissTemplate
git clone -b master https://github.com/RedGuides/MQ2LinkDB.git plugins/MQ2LinkDB
git clone -b master https://github.com/RedGuides/MQ2Log.git plugins/MQ2Log
git clone -b master https://github.com/jessebevil/MQ2LootManager.git plugins/MQ2LootManager
git clone -b master https://github.com/RedGuides/MQ2Medley.git plugins/MQ2Medley
git clone -b master https://github.com/RedGuides/MQ2Melee.git plugins/MQ2Melee
git clone -b main https://github.com/wired420/MQ2MeshManager.git plugins/MQ2MeshManager
git clone -b master https://github.com/RedGuides/MQ2MoveUtils.git plugins/MQ2MoveUtils
git clone -b master https://github.com/RedGuides/MQ2MyButtons.git plugins/MQ2MyButtons
git clone -b master https://github.com/brainiac/MQ2Nav.git plugins/MQ2Nav
git clone -b master https://github.com/RedGuides/MQ2NetBots.git plugins/MQ2NetBots
git clone -b master https://github.com/RedGuides/MQ2Notepad.git plugins/MQ2Notepad
git clone -b master https://github.com/RedGuides/MQ2OTD.git plugins/MQ2OTD
git clone -b master https://github.com/RedGuides/MQ2Paranoid.git plugins/MQ2Paranoid
git clone -b master https://github.com/RedGuides/MQ2PlatTracker.git plugins/MQ2PlatTracker
git clone -b master https://github.com/RedGuides/MQ2PluginManager.git plugins/MQ2PluginManager
git clone -b master https://github.com/RedGuides/MQ2PortalSetter.git plugins/MQ2PortalSetter
git clone -b master https://github.com/RedGuides/MQ2Posse.git plugins/MQ2Posse
git clone -b master https://github.com/RedGuides/MQ2RaidUtils.git plugins/MQ2RaidUtils
git clone -b master https://github.com/RedGuides/MQ2Rand.git plugins/MQ2Rand
git clone -b master https://github.com/RedGuides/MQ2React.git plugins/MQ2React
git clone -b master https://github.com/RedGuides/MQ2RelayTells.git plugins/MQ2RelayTells
git clone -b master https://github.com/RedGuides/MQ2Relocate.git plugins/MQ2Relocate
git clone -b master https://github.com/RedGuides/MQ2Rewards.git plugins/MQ2Rewards
git clone -b master https://github.com/RedGuides/MQ2Rez.git plugins/MQ2Rez
git clone -b master https://github.com/RedGuides/MQ2Say.git plugins/MQ2Say
git clone -b master https://gitlab.com/Knightly1/MQ2ShellCmd.git plugins/MQ2ShellCmd
git clone -b master https://github.com/RedGuides/MQ2SpawnMaster.git plugins/MQ2SpawnMaster
git clone -b master https://github.com/RedGuides/MQ2Spawns.git plugins/MQ2Spawns
git clone -b master https://github.com/RedGuides/MQ2SpawnSort.git plugins/MQ2SpawnSort
git clone -b master https://gitlab.com/Knightly1/MQ2SQLite.git plugins/MQ2SQLite
git clone -b master https://github.com/RedGuides/MQ2Status.git plugins/MQ2Status
git clone -b master https://github.com/MMOBugs/MQ2Targets.git plugins/MQ2Targets
git clone -b main https://github.com/Knightly1/MQTextToSpeech.git plugins/MQTextToSpeech
git clone -b master https://github.com/RedGuides/MQ2ToolTip.git plugins/MQ2ToolTip
git clone -b master https://github.com/RedGuides/MQ2Tracking.git plugins/MQ2Tracking
git clone -b master https://github.com/RedGuides/MQ2TributeManager.git plugins/MQ2TributeManager
git clone -b master https://github.com/RedGuides/MQ2TSTrophy.git plugins/MQ2TSTrophy
git clone -b master https://github.com/RedGuides/MQ2Twist.git plugins/MQ2Twist
git clone -b master https://github.com/RedGuides/MQ2Vendors.git plugins/MQ2Vendors
git clone -b master https://github.com/MMOBugs/MQ2WinTitle.git plugins/MQ2WinTitle
git clone -b master https://github.com/RedGuides/MQ2WorstHurt.git plugins/MQ2WorstHurt
git clone -b master https://github.com/RedGuides/MQ2XAssist.git plugins/MQ2XAssist
git clone -b master https://github.com/RedGuides/MQ2XPTracker.git plugins/MQ2XPTracker
# Emu only
git clone -b main https://github.com/Knightly1/MQMountClassicModels.git plugins/MQMountClassicModels
# Update submodules of these submodules
git submodule update --init --recursive
```
