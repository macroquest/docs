# History Of MacroQuest

### MacroQuest

In 1999, a site called HackersQuest opened its doors with public forums. It is interesting to note that many popular projects \(black hat as well as white hat\) seem to have been born there, or at least been somehow associated. Of note: WyvernX \(also known as Admin\) of XUnleashed, Ratt of ShowEQ, just some dude of EQWindows, and Mapfiend of RPG-Toolbox were some of the first registered users at HackersQuest.

Plazmic first publicly announced what would be come MacroQuest in a post dated May 11th, 2002, the date he joined HackersQuest.

The post is below:

> _I'm currently working on a truely intelligent macro subsystem for EverQuest that can run while EQ is NOT the forground process._
>
> _I have a test character that has levelled from 1 to 5 in North Qeynos chasing snakes and other things around, runs back to the gate to rest when low on health, and head to the merchants when low on packspace._
>
> _Another character was running around Shadowhaven making and selling Pickled Gator meat for a small profit \(really not worth the time\)_
>
> _Would anyone be interested in this type of a macro program? I'm not sure fully what Xylobot offers, but I figure background macroing would be a hit nevertheless._

A poll attached to the post turned up 3 votes -- one for "I'd rather use Xylobot", one for "Running a macro in the background would be cool", and one for "Sign me up for the beta!".

A little bit less than a month later he posted again, this time with a link to a new site at [sourceforge](http://www.sourceforge.net). The project was called MacroQuest, and would later become the most successful and popular tool for automating EverQuest_._ This new utility was originally only available for Windows 2000 and XP users, but later adapted for Windows 98 and ME. It boasted new commands that could be used directly in EverQuest, with variables and a macro language -- and even came with some macros, including a fletching macro to make arrows.

**Note:** Credit for writing the above text goes to Feonix762.

### MacroQuest 2

Macroquest2 was developed from the existing MacroQuest project, initially by Lax. You may find the original post about MacroQuest2 replacing MacroQuest [here](https://macroquest2.com/phpBB3/viewtopic.php?t=4023).

The text of the post:

> _**Post subject: Nonbelievers of Lax soon to be disproven!**_
>
> _In the last 3 days I have been working hard to redefine the future of Macroquest. The people who have seen the work this far are pleased, and the time draws near to actually allow public beta testing. Please note that nothing in the current MQ will be changed, or broken. This will be an entirely new distribution, from the same place. For now the project is dubbed MQ2._
>
> _**So what is MQ2?**_
>
> _MQ2 is an EverQuest development platform, with some default functionality. The development platform is so good, in fact, that it is second only to having the current EQ source code. Gone are the days for inline assembly \(99% of it anyway\) in MQ. Now we have a much cleaner and easier method of stealing! What was previously 10 lines of inline assembly, is now 1 line that looks like pEverQuest-&gt;dsp\_chat\(Line,Color\);..._
>
> ''MQ2 is plugin-based. There is a main DLL, MQ2Main, which contains the API needed to create plugins that do pretty much anything. Plugins simply include a "MQ2Plugin.h" header file and instantly gain access to everything in MQ2Main, all of the data structures, etc. To add custom commands, you use AddCommand. To add custom ParseMacroParameters parms, like $char, you use AddParm. To add a detour, you use AddDetour. To execute code on every MQ pulse, you make copy the plugin template function OnPulse\(\). And so on. It's incredibly simple.
>
> _**"**Many people have great ideas like bazaar functionality.. .. and many have things they do not want to share, and don't want to have to diff in their changes every time they get a new source. Now, instead of the cumbersome "EQLib\_Custom.cpp", you simply make a plugin and it's independent._
>
> _**What sort of plugins...?**_
>
> _Several features of "old" Macroquest are removed from the main system. Namely: FPS Limiter, Chat \(including the windows\), Map labelling, UI Labels, Item display mods, Telnet. Plugins can handle all of these and more. In fact, most of the features just listed already have been developed in plugin form. A little more testing by developers and things will be ready._
>
> _**Can my plugin use another plugin as an API?**_
>
> _Sure. You probably shouldn't try to use things from plugins that arent designed to be API. Export things from the API plugin, and import them in the functional plugin, and make sure the functional plugin is using the .lib from the API plugin in addition to the others needed._
>
> _**What does this mean for us right NOW, not tomorrow when we can get this?**_
>
> _MQ2 is a couple days behind as far as new features and fixes implemented in the "old" macroquest CVS. Anything implemented since a few days ago will have to be re-done into MQ2. I'm working fast to keep this delta as small as possible._
>
> _**WHEN DOES BETA START**_
>
> _It should not be long before we have a zip for you to download for beta testing. Beta testing will last as long as it takes to get the plugins tested, which will not be long._
>
> _Once the default set of plugins is working, we can call it a "stable" release._

