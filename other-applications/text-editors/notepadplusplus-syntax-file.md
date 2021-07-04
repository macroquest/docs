# Notepad++ Syntax File

## Pre-requesites

* Notepad++ version 3.6 or higher [notepad-plus.sourceforge.net](http://notepad-plus.sourceforge.net)

## Installation

User defined languages are stored in a file named **userDefineLang.xml**. If you do not have any extra languages defined, create a new file called userDefineLang.xml and add two lines

```<NotepadPlus>`` ````` &lt;/NotepadPlus&gt;

Note that newer versions of Notepad++ stores userDefineLang.xml in "%userprofile%\Application Data\Notepad++" \(Use Start &gt; Run, and copy/paste that path\). Windows 7 users will find the userDefineLang.xml under "%AppData%\Notepad++."

Alternately, create a new stub language with Notepad++ using the User Define Dialog... \(found under the Language menu\). Edit userDefineLang.xml and add the following in between the  delimiters

000000sub/return\( \) \[ \] { } + &lt; = &gt;/aa /alert /alias /altkey /press /zapvars /varadd /sendkey  
/banklist /beep /bind  
/call /caption /captioncolor /cast /charinfo /cleanup /clearerrors /click /combine /ctrlkey /custombind  
/defaulthud /delay /destroy /docommand /doors /doortarget /dosocial /drop /dumpbinds /declare /deletevar /doevents  
/echo /endmacro  
/face /filter /for  
/goto  
/help /hud /highlight  
/identify /ini /itemnotify /items /itemtarget  
/keepkeys /keypress  
/loadcfg /loadspells /location /loginname /look /listmacros /loadhud  
/memspell /mouseto /mqfont /mqlog /mqpause /multiline /macro /mapclick /mapfilter /maphide /mapnames /mapshow  
/nomodkey /noparse /notify /next  
/plugin /popup  
/ranged  
/sellitem /setautorun /shiftkey /skills /spew /squelch /substitute /seterror  
/target /timed  
/unload /updateitems  
/varset /varcalc /vardata  
/where /who /whofilter /whotarget /windows /windowstate  
/stick /circle /moveto/1 /2 /3 /4 /5 /6 /7 /8 /9 /10  
/a /addraidlooter /announce /adriver /adventure /anon /anonymous /afk /agree /alignment /alternateadv /amaze /assist /apologize /applaud /approval /attack /audiodebug /auction /autofire /autoinventory /autojoin /autosplit  
/b /bandolier /barter /bazaar /becomenpc /beta /betabuff /bite /bird /bleed /blink /blush /bodytint /boggle /bonk /book /bored /bounce /bow /brb /broadcast /bug /bugreport /burp /buyer /bye  
/cackle /chuckle /calm /camp /cast /changename /channel /chat /chatfontsize /cheer /claim /clearmarks /clap /clear /clearhits /combatmusic /comfort /con /congratulate /consider /consent /corpse /corpsedrag /corpsedrop /cough /cringe /cry /curious  
/d /dance /decline /delcorpse /deletepetition /deny /disband /disbelief /discipline /dismount /doability /dopropertinting /drool /duck /duel /dynamiclights /dzaddplayer /dzhelp /dzlisttimers /dzmakeleader /dzplayer /dzplayerlist /dzquit /dzremoveplayer /dzswapplayer  
/em /edit /emote /eye /exit /eqplayersupdate /eqplayersguildupdate  
/facepick /fastdrop /feedback /fidget /find /findpc /finger /filter /flex /flipoff /fontface /follow /friend /friends /frown /ftell /fullscreen  
/g /gasp /gems /gesture /getguildmotd /giggle /glare /gmarknpc /gmarkwaypoint /grin /groan /grovel /gsay /guide /guidehelp /guild /guildsay /guildinvite /guildremove /guilddelete /guildstatus /guildleader /guildwar /guildpeace /guildmotd  
/happy /hail /height /help /hidecorpse /hidecorpses /hideme /hitsmode /honor /hotbutton /hug /hungry  
/ignore /indicator /inspect /inspectbuffs /introduce /invite /inquire /invwinlabels  
/jk /join /kbroadcast  
/key /keys /kick /kill /kiss /kneel  
/language /lastname /laugh /leader /leave /leaveall /lfg /list /loadskin /log /location /loc /loot /lootnodrop /lost  
/makeleader /makeraidleader /marknpc /massage /map /mcicontrol /microphone /me /melody /memspellset /mixahead /moan /motd /mourn /movelog /mousespeed /mp3 /msg  
/name /netstats /nod /nudge /note  
/ooc /open /outputfile  
/panic /paperdoll /particledensity /pat /peer /pet /petition /played /plead /point /poke /ponder /popmail /potionbelt /praise /private /purr /puzzle  
/quit  
/raidaccept /raiddecline /raiddisband /raidinvite /raise /random /ready /removeraidlooter /reply /report /resetwindows /reveal /reverb /reversesound /rmarknpc /rmarkwaypoint /roar /rofl /roleplay /rude /rsay /rtarget  
/salute /safelock /safemove /savespellset /say /sdriver /searchcorpse /selfkill /send /serverfilter /servers /setloottype /setstartcity /shadows /shield /shiver /shrug /shout /showgrass /shownames /shownpcnames /showplayernames /showspelleffects /sigh /sit /smack /smile /smirk /snarl /snicker /split /stand /stare /stopcast /stopsong /stoptracking /system /summon /summoncorpse /surname  
/tap /targetgroupbuff /testbuffme /taskaddplayer /taskmakeleader /taskplayerlist /taskswapplayer /taskquit /taskremoveplayer /tasktimers /tease /tell /tgb /thank /thirsty /time /toggleinspect /toggletell /trade /trader /trackfilter /trackplayers /tracksort /ttell  
/url /usecolor /usercolor  
/veteranreward /veteranReward /veto /vgroup /viewpetition /viewpoint /viewport /voice /vplay /vraid /vrdelay /vtell  
/warn /wave /webupdate /welcome /whine /whistle /who /whotarget /wincolor /wordlist /www  
/yawn /yell  
/zoneAAW\_ArchetypePage AAW\_ClassPage AAW\_GeneralPage AAW\_Page4 AAW\_Page5 AAW\_Page6 AAWindow ActionsAbilitiesPage ActionsCombatPage ActionsMainPage ActionsSocialsPage ActionsWindow ActorParticlesPage AdventureLeaderboardWnd AdventureMerchantWnd AdventureRequestWnd AdventureStatsWnd AlarmWnd  
BZW\_BazaarSlotsWnd BazaarSearchWnd BazaarWnd BigBankWnd BodyTintWnd BookWindow BreathWindow BuffWindow BugReportWindow  
CJNPC\_Layout COMBW\_CombineArea COMBW\_ComponentArea COMBW\_ContainerArea COMBW\_FavoritesArea COMBW\_FlagsArea COMBW\_LeftSideArea COMBW\_RecipeListArea COMBW\_RightSideArea COMBW\_SearchArea CastSpellWnd CastingWindow ColorPickerWnd CombatAbilityWnd CombatSkillSelectWnd CompassWindow CursorAttachment  
DZLeaderSection DynamicZoneWnd  
EditLabelWnd EnvironmentParticlesPage  
FW\_FriendsPage FW\_IgnorePage FacePickWindow FeedbackWindow FileSelectionWnd FindLocationWnd FriendsWindow Friends\_TimerSlider0  
GGW\_GameView GT\_MemberPage GT\_NotePage GemsGameWnd GiveWnd GroupInfoPage GroupListPage GroupSearchFiltersWnd GroupSearchWnd GroupWindow GuildManagementWnd  
HelpWindow HotButtonWnd  
IW\_CharacterView InspectWnd InventoryWindow  
JournalCatWnd JournalNPCWnd  
KnowledgeBasePage  
LEW\_GroupPage LEW\_RaidPage LW\_LootInvWnd LargeDialogWindow LeadershipWindow LoadskinWnd LootWnd  
MVW\_MapRenderArea MW\_MerchantSlotsWnd MW\_SlotsWndThree MW\_SlotsWndTwo MapToolbarWnd MapViewWnd MerchantWnd MusicPlayerWnd  
NewTicketPage NoteWindow  
OpenTicketsPage OptionsChatPage OptionsColorPage OptionsDisplayPage OptionsGeneralPage OptionsKeyboardPage OptionsMousePage OptionsWindow  
PIW\_BuffWindow PetInfoWindow PlayerInfoPage PlayerListPage PlayerNotesWindow PlayerWindow PvPMerchantWnd PvPStatsWnd PvpLeaderboardWnd  
QuantityWnd  
RAID\_MemberPage RAID\_NotePage RaidOptionsWindow RaidWindow  
SelectorWindow ShortDurationBuffWindow SkillsSelectWindow SkillsWindow SocialEditWnd SpellBookWnd SpellParticlesPage StoryWnd SystemInfoDialogBox  
TBW\_LabelWnd TBW\_Layout TMW\_ActiveBenefitArea TMW\_BenefitMasterArea TMW\_DonateWnd TMW\_LabelWnd  
TMW\_Layout TargetOfTargetWindow TargetWindow TextEntryWnd TicketCommentWindow TicketWindow TipWindow TrackingWnd TradeWnd TradeskillWnd TrainWindow TRDW\_HisName TributeBenefitWnd TributeMasterWnd  
VideoModesWindow\#turbo \#define \#include \#event \#chat

## Using Notepad++ with the Syntax Highlighting

You will want to associate .mac \(and possible .inc\) files with Notepad++. This can be done inside the application and by associating the extensions with the OS.

From Menu

Settings &gt; Preferences &gt; File Association Tab

Click on customize in left side box

Type .mac in the middle box that appears then click the arrow until it shows up in registered ext in the right side box

Click close

### What Highlighted Syntax Looks Like

Sample lines showing sytax colors.

```<font color="blue">``\#event`</font>` CombineError "\#_\#There was no place to put that\#_\#"`````   
```<font color="green">``\| Sub DoCombine`</font>` ``` /varsetEndingVar 1``  
`````  `<font color="#3399FF">`/nomodkey /notify `</font><font color="#FF9966">`TradeskillWnd `</font>` CombineButton leftmouseup\`

`/if (${Cursor.ID}) {`

```<font color="#3399FF">``/timed `</font>`5 `<font color="#993300">`/autoinventory\`&lt;/font&gt;

