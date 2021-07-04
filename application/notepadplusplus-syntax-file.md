## Notepad++ Syntax File

## Pre-requesites

-   Notepad++ version 3.6 or higher [notepad-plus.sourceforge.net](http://notepad-plus.sourceforge.net)

## Installation

User defined languages are stored in a file named **userDefineLang.xml**. If you do not have any extra languages
defined, create a new file called userDefineLang.xml and add two lines

` `<NotepadPlus>` `  
` `</NotepadPlus>

Note that newer versions of Notepad++ stores userDefineLang.xml in "%userprofile%\\Application Data\\Notepad++" (Use
Start \> Run, and copy/paste that path). Windows 7 users will find the userDefineLang.xml under "%AppData%\\Notepad++."

Alternately, create a new stub language with Notepad++ using the User Define Dialog... (found under the Language menu).
Edit userDefineLang.xml and add the following in between the <NotepadPlus> delimiters

    <nowiki>
        <UserLang name="MacroQuest" ext="mac" commentLine="|" commentStart="|**" commentEnd="**|">
            <Settings>
                <Global caseIgnored="yes" />
                <TreatAsSymbol comment="no" commentLine="no" />
                <Prefix words1="no" words2="no" words3="no" words4="no" />
            </Settings>
            <KeywordLists>
                <Keywords name="Delimiters">000000</Keywords>
                <Keywords name="Folder+">sub</Keywords>
                <Keywords name="Folder-">/return</Keywords>
                <Keywords name="Operators">( ) [ ] { } + &lt; = &gt;</Keywords>
                <Keywords name="Words1">/aa /alert /alias /altkey /press /zapvars /varadd /sendkey&#x0D;&#x0A;/banklist /beep /bind&#x0D;&#x0A;/call /caption /captioncolor /cast /charinfo /cleanup /clearerrors /click /combine /ctrlkey /custombind&#x0D;&#x0A;/defaulthud /delay /destroy /docommand /doors /doortarget /dosocial /drop /dumpbinds /declare /deletevar /doevents&#x0D;&#x0A;/echo /endmacro&#x0D;&#x0A;/face /filter /for&#x0D;&#x0A;/goto&#x0D;&#x0A;/help /hud /highlight&#x0D;&#x0A;/identify /ini /itemnotify /items /itemtarget&#x0D;&#x0A;/keepkeys /keypress&#x0D;&#x0A;/loadcfg /loadspells /location /loginname /look /listmacros /loadhud&#x0D;&#x0A;/memspell /mouseto /mqfont /mqlog /mqpause /multiline /macro /mapclick /mapfilter /maphide /mapnames /mapshow&#x0D;&#x0A;/nomodkey /noparse /notify /next&#x0D;&#x0A;/plugin /popup&#x0D;&#x0A;/ranged&#x0D;&#x0A;/sellitem /setautorun /shiftkey /skills /spew /squelch /substitute /seterror&#x0D;&#x0A;/target /timed&#x0D;&#x0A;/unload /updateitems&#x0D;&#x0A;/varset /varcalc /vardata&#x0D;&#x0A;/where /who /whofilter /whotarget /windows /windowstate&#x0D;&#x0A;/stick /circle /moveto</Keywords>
                <Keywords name="Words2">/1 /2 /3 /4 /5 /6 /7 /8 /9 /10&#x0D;&#x0A;/a /addraidlooter /announce /adriver /adventure /anon /anonymous /afk /agree /alignment /alternateadv /amaze /assist /apologize /applaud /approval /attack /audiodebug /auction /autofire /autoinventory /autojoin /autosplit&#x0D;&#x0A;/b /bandolier /barter /bazaar /becomenpc /beta /betabuff /bite /bird /bleed /blink /blush /bodytint /boggle /bonk /book /bored /bounce /bow /brb /broadcast /bug /bugreport /burp /buyer /bye&#x0D;&#x0A;/cackle /chuckle /calm /camp /cast /changename /channel /chat /chatfontsize /cheer /claim /clearmarks /clap /clear /clearhits /combatmusic /comfort /con /congratulate /consider /consent /corpse /corpsedrag /corpsedrop /cough /cringe /cry /curious&#x0D;&#x0A;/d /dance /decline /delcorpse /deletepetition /deny /disband /disbelief /discipline /dismount /doability /dopropertinting /drool /duck /duel /dynamiclights /dzaddplayer /dzhelp /dzlisttimers /dzmakeleader /dzplayer /dzplayerlist /dzquit /dzremoveplayer /dzswapplayer&#x0D;&#x0A;/em /edit /emote /eye /exit /eqplayersupdate /eqplayersguildupdate&#x0D;&#x0A;/facepick /fastdrop /feedback /fidget /find /findpc /finger /filter /flex /flipoff /fontface /follow /friend /friends /frown /ftell /fullscreen&#x0D;&#x0A;/g /gasp /gems /gesture /getguildmotd /giggle /glare /gmarknpc /gmarkwaypoint /grin /groan /grovel /gsay /guide /guidehelp /guild /guildsay /guildinvite /guildremove /guilddelete /guildstatus /guildleader /guildwar /guildpeace /guildmotd&#x0D;&#x0A;/happy /hail /height /help /hidecorpse /hidecorpses /hideme /hitsmode /honor /hotbutton /hug /hungry&#x0D;&#x0A;/ignore /indicator /inspect /inspectbuffs /introduce /invite /inquire /invwinlabels&#x0D;&#x0A;/jk /join /kbroadcast&#x0D;&#x0A;/key /keys /kick /kill /kiss /kneel&#x0D;&#x0A;/language /lastname /laugh /leader /leave /leaveall /lfg /list /loadskin /log /location /loc /loot /lootnodrop /lost&#x0D;&#x0A;/makeleader /makeraidleader /marknpc /massage /map /mcicontrol /microphone /me /melody /memspellset /mixahead /moan /motd /mourn /movelog /mousespeed /mp3 /msg&#x0D;&#x0A;/name /netstats /nod /nudge /note&#x0D;&#x0A;/ooc /open /outputfile&#x0D;&#x0A;/panic /paperdoll /particledensity /pat /peer /pet /petition /played /plead /point /poke /ponder /popmail /potionbelt /praise /private /purr /puzzle&#x0D;&#x0A;/quit&#x0D;&#x0A;/raidaccept /raiddecline /raiddisband /raidinvite /raise /random /ready /removeraidlooter /reply /report /resetwindows /reveal /reverb /reversesound /rmarknpc /rmarkwaypoint /roar /rofl /roleplay /rude /rsay /rtarget&#x0D;&#x0A;/salute /safelock /safemove /savespellset /say /sdriver /searchcorpse /selfkill /send /serverfilter /servers /setloottype /setstartcity /shadows /shield /shiver /shrug /shout /showgrass /shownames /shownpcnames /showplayernames /showspelleffects /sigh /sit /smack /smile /smirk /snarl /snicker /split /stand /stare /stopcast /stopsong /stoptracking /system /summon /summoncorpse /surname&#x0D;&#x0A;/tap /targetgroupbuff /testbuffme /taskaddplayer /taskmakeleader /taskplayerlist /taskswapplayer /taskquit /taskremoveplayer /tasktimers /tease /tell /tgb /thank /thirsty /time /toggleinspect /toggletell /trade /trader /trackfilter /trackplayers /tracksort /ttell&#x0D;&#x0A;/url /usecolor /usercolor&#x0D;&#x0A;/veteranreward /veteranReward /veto /vgroup /viewpetition /viewpoint /viewport /voice /vplay /vraid /vrdelay /vtell&#x0D;&#x0A;/warn /wave /webupdate /welcome /whine /whistle /who /whotarget /wincolor /wordlist /www&#x0D;&#x0A;/yawn /yell&#x0D;&#x0A;/zone</Keywords>
                <Keywords name="Words3">AAW_ArchetypePage AAW_ClassPage AAW_GeneralPage AAW_Page4 AAW_Page5 AAW_Page6 AAWindow ActionsAbilitiesPage ActionsCombatPage ActionsMainPage ActionsSocialsPage ActionsWindow ActorParticlesPage AdventureLeaderboardWnd AdventureMerchantWnd AdventureRequestWnd AdventureStatsWnd AlarmWnd&#x0D;&#x0A;BZW_BazaarSlotsWnd BazaarSearchWnd BazaarWnd BigBankWnd BodyTintWnd BookWindow BreathWindow BuffWindow BugReportWindow&#x0D;&#x0A;CJNPC_Layout COMBW_CombineArea COMBW_ComponentArea COMBW_ContainerArea COMBW_FavoritesArea COMBW_FlagsArea COMBW_LeftSideArea COMBW_RecipeListArea COMBW_RightSideArea COMBW_SearchArea CastSpellWnd CastingWindow ColorPickerWnd CombatAbilityWnd CombatSkillSelectWnd CompassWindow CursorAttachment&#x0D;&#x0A;DZLeaderSection DynamicZoneWnd&#x0D;&#x0A;EditLabelWnd EnvironmentParticlesPage&#x0D;&#x0A;FW_FriendsPage FW_IgnorePage FacePickWindow FeedbackWindow FileSelectionWnd FindLocationWnd FriendsWindow Friends_TimerSlider0&#x0D;&#x0A;GGW_GameView GT_MemberPage GT_NotePage GemsGameWnd GiveWnd GroupInfoPage GroupListPage GroupSearchFiltersWnd GroupSearchWnd GroupWindow GuildManagementWnd&#x0D;&#x0A;HelpWindow HotButtonWnd&#x0D;&#x0A;IW_CharacterView InspectWnd InventoryWindow&#x0D;&#x0A;JournalCatWnd JournalNPCWnd&#x0D;&#x0A;KnowledgeBasePage&#x0D;&#x0A;LEW_GroupPage LEW_RaidPage LW_LootInvWnd LargeDialogWindow LeadershipWindow LoadskinWnd LootWnd&#x0D;&#x0A;MVW_MapRenderArea MW_MerchantSlotsWnd MW_SlotsWndThree MW_SlotsWndTwo MapToolbarWnd MapViewWnd MerchantWnd MusicPlayerWnd&#x0D;&#x0A;NewTicketPage NoteWindow&#x0D;&#x0A;OpenTicketsPage OptionsChatPage OptionsColorPage OptionsDisplayPage OptionsGeneralPage OptionsKeyboardPage OptionsMousePage OptionsWindow&#x0D;&#x0A;PIW_BuffWindow PetInfoWindow PlayerInfoPage PlayerListPage PlayerNotesWindow PlayerWindow PvPMerchantWnd PvPStatsWnd PvpLeaderboardWnd&#x0D;&#x0A;QuantityWnd&#x0D;&#x0A;RAID_MemberPage RAID_NotePage RaidOptionsWindow RaidWindow&#x0D;&#x0A;SelectorWindow ShortDurationBuffWindow SkillsSelectWindow SkillsWindow SocialEditWnd SpellBookWnd SpellParticlesPage StoryWnd SystemInfoDialogBox&#x0D;&#x0A;TBW_LabelWnd TBW_Layout TMW_ActiveBenefitArea TMW_BenefitMasterArea TMW_DonateWnd TMW_LabelWnd&#x0D;&#x0A;TMW_Layout TargetOfTargetWindow TargetWindow TextEntryWnd TicketCommentWindow TicketWindow TipWindow TrackingWnd TradeWnd TradeskillWnd TrainWindow TRDW_HisName TributeBenefitWnd TributeMasterWnd&#x0D;&#x0A;VideoModesWindow</Keywords>
                <Keywords name="Words4">#turbo #define #include #event #chat</Keywords>
            </KeywordLists>
            <Styles>
                <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="FOLDEROPEN" styleID="12" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="FOLDERCLOSE" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="KEYWORD1" styleID="5" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="KEYWORD2" styleID="6" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="1" />
                <WordsStyle name="KEYWORD3" styleID="7" fgColor="FF8040" bgColor="FFFFFF" fontName="" fontStyle="1" />
                <WordsStyle name="KEYWORD4" styleID="8" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="COMMENT" styleID="1" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008040" bgColor="FFFFFF" fontName="" fontStyle="1" />
                <WordsStyle name="NUMBER" styleID="4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="OPERATOR" styleID="10" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="DELIMINER1" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="DELIMINER2" styleID="15" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
                <WordsStyle name="DELIMINER3" styleID="16" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" />
            </Styles>
        </UserLang>
    </nowiki>

## Using Notepad++ with the Syntax Highlighting

You will want to associate .mac (and possible .inc) files with Notepad++. This can be done inside the application and by
associating the extensions with the OS.

From Menu

Settings \> Preferences \> File Association Tab

Click on customize in left side box

Type .mac in the middle box that appears then click the arrow until it shows up in registered ext in the right side box

Click close

### What Highlighted Syntax Looks Like

Sample lines showing sytax colors.

` `<font color="blue">`#event`</font>` CombineError "#*#There was no place to put that#*#"`  
` `  
` `<font color="green">`| Sub DoCombine`</font>  
` `  
` `<font color="#3399FF">`/varset `</font>`EndingVar 1`  
` `  
` `<font color="#3399FF">`/nomodkey /notify `</font><font color="#FF9966">`TradeskillWnd `</font>` CombineButton leftmouseup`

` /if (${Cursor.ID}) { `  
  
` `<font color="#3399FF">`/timed `</font>`5 `<font color="#993300">`/autoinventory`</font>


