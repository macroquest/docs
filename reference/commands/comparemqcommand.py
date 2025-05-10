import os
import re

# Get list of existing command files (excluding index.md)
command_files = [f for f in os.listdir() if f.endswith(".md") and f != "index.md"]

# Extract command names from C++ array
cpp_commands = """
	// Add MQ commands...
	struct { const char* szCommand; MQCommandHandler pFunc; bool Parse; bool InGame; } NewCommands[] = {
		{ "/aa",                AltAbility,                 true,  true  },
#if HAS_ADVANCED_LOOT
		{ "/advloot",           AdvLootCmd,                 true,  true  },
#endif
		{ "/alert",             Alert,                      true,  true  },
		{ "/alias",             Alias,                      false, false },
		{ "/altkey",            DoAltCmd,                   false, false },
		{ "/assist",            AssistCmd,                  true,  true  },
		{ "/banklist",          BankList,                   true,  true  },
		{ "/beep",              MacroBeep,                  true,  false },
		{ "/bind",              MQ2KeyBindCommand,          true,  false },
		{ "/break",             Break,                      true,  false },
		{ "/buyitem",           BuyItem,                    true,  true  },
		{ "/cachedbuffs",       CachedBuffsCommand,         true,  true  },
		{ "/call",              Call,                       true,  false },
		{ "/cast",              Cast,                       true,  true  },
		{ "/cecho",             EchoClean,                  true,  false },
		{ "/char",              CharInfo,                   true,  true  },
		{ "/cleanup",           Cleanup,                    true,  false },
		{ "/clearerrors",       ClearErrorsCmd,             true,  false },
		{ "/click",             Click,                      true,  false },
		{ "/combine",           CombineCmd,                 true,  true  },
		{ "/continue",          Continue,                   true,  false },
#if HAS_ITEM_CONVERT_BUTTON
		{ "/convertitem",       ConvertItemCmd,             true,  true  },
#endif
		{ "/ctrlkey",           DoCtrlCmd,                  false, false },
		{ "/declare",           DeclareVar,                 true,  false },
		{ "/delay",             Delay,                      false, false }, // do not parse
		{ "/deletevar",         DeleteVarCmd,               true,  false },
		{ "/destroy",           EQDestroyHeldItemOrMoney,   true,  true  },
		{ "/doability",         DoAbility,                  true,  true  },
		{ "/docommand",         DoCommandCmd,               true,  false },
		{ "/doevents",          DoEvents,                   true,  false },
		{ "/doors",             Doors,                      true,  true  },
		{ "/doortarget",        DoorTarget,                 true,  true  },
		{ "/dosocial",          DoSocial,                   true,  true  },
		{ "/drop",              DropCmd,                    true,  true  },
		{ "/dumpbinds",         DumpBindsCommand,           true,  false },
		{ "/dumpstack",         DumpStack,                  true,  false },
		{ "/echo",              Echo,                       true,  false },
		{ "/endmacro",          EndMacro,                   true,  false },
		{ "/engine",            EngineCommand,              true,  false },
		{ "/exec",              Exec,                       true,  false },
		{ "/executelink",       ExecuteLinkCommand,         true,  true  },
		{ "/face",              Face,                       true,  true  },
		{ "/filter",            Filter,                     true,  false },
		{ "/for",               For,                        true,  false },
		{ "/foreground",        ForeGroundCmd,              true,  false },
		{ "/getwintitle",       GetWinTitle,                true,  false },
		{ "/goto",              Goto,                       true,  false },
		{ "/help",              Help,                       true,  false },
		{ "/hotbutton",         DoHotButton,                true,  true  },
		{ "/hud",               HudCmd,                     true,  false },
		{ "/identify",          Identify,                   true,  true  },
		{ "/if",                MacroIfCmd,                 true,  false },
		{ "/ini",               IniOutput,                  true,  false },
		{ "/insertaug",         InsertAugCmd,               true,  true  },
		{ "/invoke",            InvokeCmd,                  true,  false },
		{ "/items",             Items,                      true,  true  },
		{ "/itemtarget",        ItemTarget,                 true,  true  },
		{ "/keepkeys",          KeepKeys,                   true,  false },
		{ "/keypress",          DoMappable,                 true,  false },
		{ "/listmacros",        ListMacros,                 true,  false },
		{ "/loadcfg",           LoadCfgCommand,             true,  false },
		{ "/loadspells",        LoadSpells,                 true,  true  },
		{ "/location",          Location,                   true,  true  },
		{ "/loginname",         DisplayLoginName,           true,  false },
		{ "/look",              Look,                       true,  true  },
		{ "/lootall",           LootAll,                    true,  false },
		{ "/macro",             Macro,                      true,  false },
		{ "/makemevisible",     MakeMeVisible,              false, true  },
		{ "/memspell",          MemSpell,                   true,  true  },
		{ "/mercswitch",        MercSwitchCmd,              true,  true  },
		{ "/mouseto",           MouseTo,                    true,  false },
		{ "/mqcopylayout",      MQCopyLayout,               true,  false },
		{ "/mqlistmodules",     ListModulesCommand,         false, false },
		{ "/mqlistprocesses",   ListProcessesCommand,       false, false },
		{ "/mqlog",             MacroLog,                   true,  false },
		{ "/mqpause",           MacroPause,                 true,  false },
		{ "/mqtarget",          Target,                     true,  true  },
		{ "/msgbox",            MQMsgBox,                   true,  false },
		{ "/multiline",         MultilineCommand,           false, false },
		{ "/next",              Next,                       true,  false },
		{ "/nomodkey",          NoModKeyCmd,                false, false },
		{ "/noparse",           NoParseCmd,                 false, false },
		{ "/pet",               PetCmd,                     true,  true  },
		{ "/pickzone",          PickZoneCmd,                true,  true  },
		{ "/popcustom",         PopupTextCustom,            true,  true  },
		{ "/popup",             PopupText,                  true,  true  },
		{ "/popupecho",         PopupTextEcho,              true,  true  },
		{ "/profile",           ProfileCmd,                 true,  false },
		{ "/quit",              QuitCmd,                    true,  false },
		{ "/ranged",            RangedCmd,                  true,  true  },
		{ "/reloadui",          ReloadUICmd,                true,  true  },
		{ "/removeaug",         RemoveAugCmd,               true,  true  },
		{ "/removeaura",        RemoveAura,                 true,  true  },
		{ "/removebuff",        RemoveBuff,                 true,  true  },
		{ "/removelev",         RemoveLevCmd,               true,  false },
		{ "/removepetbuff",     RemovePetBuff,              true,  true  },
		{ "/return",            Return,                     true,  false },
		{ "/screenmode",        ScreenModeCmd,              true,  false },
		{ "/selectitem",        SelectItem,                 true,  true  },
		{ "/sellitem",          SellItem,                   true,  true  },
		{ "/setautorun",        SetAutoRun,                 false, true  },
		{ "/seterror",          SetError,                   true,  false },
		{ "/setprio",           SetProcessPriority,         true,  false },
		{ "/setwintitle",       SetWinTitle,                true,  false },
		{ "/shiftkey",          DoShiftCmd,                 false, false },
		{ "/skills",            Skills,                     true,  true  },
		{ "/spellslotinfo",     SpellSlotInfo,              true,  true  },
		{ "/spewfile",          DebugSpewFile,              true,  false },
		{ "/squelch",           SquelchCommand,             true,  false },
		{ "/target",            Target,                     true,  true  },  // TODO:  Deprecate /target in favor of /mqtarget so that /target is the actual EQ Command. See #298
		{ "/taskquit",          TaskQuitCmd,                true,  true  },
		{ "/timed",             DoTimedCmd,                 false, false },
		{ "/unload",            Unload,                     true,  false },
		{ "/useitem",           UseItemCmd,                 true,  true  },
		{ "/usercamera",        UserCameraCmd,              true,  false },
		{ "/varcalc",           VarCalcCmd,                 true,  false },
		{ "/vardata",           VarDataCmd,                 true,  false },
		{ "/varset",            VarSetCmd,                  true,  false },
		{ "/where",             Where,                      true,  true  },
		{ "/while",             MacroWhileCmd,              true,  false },
		{ "/who",               SuperWho,                   true,  true  },
		{ "/whofilter",         SWhoFilter,                 true,  true  },
		{ "/whotarget",         SuperWhoTarget,             true,  true  },
		{ "/windowstate",       WindowState,                true,  false },
""".splitlines()

# Extract command names using regex
command_names = []
pattern = re.compile(r'\{\s+"(/[^"]+)"')
for line in cpp_commands:
    match = pattern.search(line)
    if match:
        command = match.group(1).lstrip('/')  # Remove leading slash
        command_names.append(command)

# Compare files vs commands
existing_docs = []
missing_docs = []
extra_docs = []

# Check which commands have documentation
for cmd in command_names:
    if f"{cmd}.md" in command_files:
        existing_docs.append(cmd)
    else:
        missing_docs.append(cmd)

# Check for extra documentation files
for f in command_files:
    base = f[:-3]  # Remove .md extension
    if base not in command_names:
        extra_docs.append(f)

# Print results
print("Commands with documentation:")
print("\n".join(existing_docs))

print("\nCommands missing documentation:")
print("\n".join(missing_docs))

print("\nExtra documentation files (not in command list):")
print("\n".join(extra_docs))