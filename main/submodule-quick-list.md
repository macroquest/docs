# Plugin Submodule Quick List

A quick list of plugins that have been migrated and how to add them.  Once they're all added, you can `git submodule update --init --recursive`to get their depdendencies.
You can quickly update your plugins with:  `git pull --recurse-submodules` or `git submodule foreach "git pull || :"`.  Both of these require having checked out the correct
branch first.

The solution file with all of these in it is here: [MacroQuestCustom.sln](../uploads/MacroQuestCustom.sln) (place this file in the src folder beside MacroQuest.sln)

```bash
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AASpend.git plugins/MQ2AASpend
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AdvPath.git plugins/MQ2AdvPath
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoAccept.git plugins/MQ2AutoAccept
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoCamp.git plugins/MQ2AutoCamp
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoClaim.git plugins/MQ2AutoClaim
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoForage.git plugins/MQ2AutoForage
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoGroup.git plugins/MQ2AutoGroup
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoLoot.git plugins/MQ2AutoLoot
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoLootSort.git plugins/MQ2AutoLootSort
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2AutoSize.git plugins/MQ2AutoSize
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Bandolier.git plugins/MQ2Bandolier
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2BardSwap.git plugins/MQ2BardSwap
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Boxr.git plugins/MQ2Boxr
git submodule add -b master -f https://github.com/brainiac/MQ2Camera.git plugins/MQ2Camera
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Cast.git plugins/MQ2Cast
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Clipboard.git plugins/MQ2Clipboard
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Collections.git plugins/MQ2Collections
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2CPULoad.git plugins/MQ2CPULoad
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Cursor.git plugins/MQ2Cursor
git submodule add -b master -f https://github.com/dannuic/MQ2Dan.git plugins/MQ2Dan
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Debuffs.git plugins/MQ2Debuffs
git submodule add -b master -f https://gitlab.com/alynel/MQ2Discord.git plugins/MQ2Discord
git submodule add -b master -f https://github.com/projecteon/MQ2DotNet.git plugins/MQ2DotNet
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2DPSAdv.git plugins/MQ2DPSAdv
git submodule add -b master -f https://github.com/brainiac/MQ2EasyFind.git plugins/MQ2EasyFind
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2EQBC.git plugins/MQ2EQBC
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Events.git plugins/MQ2Events
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Exchange.git plugins/MQ2Exchange
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2FarmTest.git plugins/MQ2FarmTest
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2FeedMe.git plugins/MQ2FeedMe
git submodule add -b master -f https://gitlab.com/MMOBugs/MQ2GMCheck.git plugins/MQ2GMCheck
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2GroupInfo.git plugins/MQ2GroupInfo
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2HeadShot.git plugins/MQ2HeadShot
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2HUDMove.git plugins/MQ2HUDMove
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Ice.git plugins/MQ2Ice
git submodule add -b main -f https://gitlab.com/Ortster/MQItemColor.git plugins/MQItemColor
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2ItemScore.git plugins/MQ2ItemScore
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2KillTracker.git plugins/MQ2KillTracker
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2KissTemplate.git plugins/MQ2KissTemplate
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2LinkDB.git plugins/MQ2LinkDB
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Log.git plugins/MQ2Log
git submodule add -b master -f https://github.com/jessebevil/MQ2LootManager.git plugins/MQ2LootManager
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Medley.git plugins/MQ2Medley
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Melee.git plugins/MQ2Melee
git submodule add -b main -f https://github.com/wired420/MQ2MeshManager.git plugins/MQ2MeshManager
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2MoveUtils.git plugins/MQ2MoveUtils
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2MyButtons.git plugins/MQ2MyButtons
git submodule add -b master -f https://github.com/brainiac/MQ2Nav.git plugins/MQ2Nav
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2NetBots.git plugins/MQ2NetBots
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Notepad.git plugins/MQ2Notepad
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2OTD.git plugins/MQ2OTD
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Paranoid.git plugins/MQ2Paranoid
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2PlatTracker.git plugins/MQ2PlatTracker
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2PluginManager.git plugins/MQ2PluginManager
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2PortalSetter.git plugins/MQ2PortalSetter
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Posse.git plugins/MQ2Posse
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2RaidUtils.git plugins/MQ2RaidUtils
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Rand.git plugins/MQ2Rand
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2React.git plugins/MQ2React
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2RelayTells.git plugins/MQ2RelayTells
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Relocate.git plugins/MQ2Relocate
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Rewards.git plugins/MQ2Rewards
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Rez.git plugins/MQ2Rez
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Say.git plugins/MQ2Say
git submodule add -b master -f https://gitlab.com/Knightly1/MQ2ShellCmd.git plugins/MQ2ShellCmd
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2SpawnMaster.git plugins/MQ2SpawnMaster
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Spawns.git plugins/MQ2Spawns
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2SpawnSort.git plugins/MQ2SpawnSort
git submodule add -b master -f https://gitlab.com/Knightly1/MQ2SQLite.git plugins/MQ2SQLite
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Status.git plugins/MQ2Status
git submodule add -b master -f https://github.com/MMOBugs/MQ2Targets.git plugins/MQ2Targets
git submodule add -b main -f https://github.com/Knightly1/MQTextToSpeech.git plugins/MQTextToSpeech
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2ToolTip.git plugins/MQ2ToolTip
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Tracking.git plugins/MQ2Tracking
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2TributeManager.git plugins/MQ2TributeManager
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2TSTrophy.git plugins/MQ2TSTrophy
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Twist.git plugins/MQ2Twist
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2Vendors.git plugins/MQ2Vendors
git submodule add -b master -f https://github.com/MMOBugs/MQ2WinTitle.git plugins/MQ2WinTitle
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2WorstHurt.git plugins/MQ2WorstHurt
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2XAssist.git plugins/MQ2XAssist
git submodule add -b master -f https://gitlab.com/redguides/plugins/MQ2XPTracker.git plugins/MQ2XPTracker
# Emu only
git submodule add -b main -f https://github.com/Knightly1/MQMountClassicModels.git plugins/MQMountClassicModels
```