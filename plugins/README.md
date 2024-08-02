# Plugins

## Introduction

Plugins extend the functionality of MQ, usually at a lower level than macros do. For example, a macro may help you do automatically mez mobs within a certain range, or auto-attack mob within a certain range. A plugin may control lower level functions like casting the mez spell for you (ie. making sure you have the right target, auto-recasting if you fizzle, etc\) or control movement to your intended victim and activating attack \(ie. moving you to melee range, turning on attack, automatically backstabbing, turning off attack on enrage, etc).

The functionality of plugins and macros often overlap, and in the above example its completely possible to do all the above using just a macro with no plugins.

Plugins are written in C++ whereas macros use MQ2's internal scripting language. The internal scripting language is a lot easier to use and manipulate than C++, which is why you'll find a lot more macros than plugins on the MQ2 message boards.

## Finding Plugins

Plugins can be found in the following forum:

[MQ2::Development::Plugins](https://macroquest.org/phpBB3/viewforum.php?f=31) (VIP Only)

ImaNoob posted a very helpful thread [here.](https://macroquest.org/phpBB3/viewtopic.php?f=31&t=6310) (VIP Only) Titled appropriately "The Complete Idiots Guide to MQ2 and plugins"

## Compiling Plugins

_Say you've seen an interesting looking plugin on the forums and you'd like to try it out, how exactly do you go about doing it?_

* Open up a command prompt (Windows key + R, type "cmd" without quotation marks, press enter) and navigate to your MQ2

  source directory (eg. `cd \mq2-latest`).

* Type "`mkplugin`". Use the name of the plugin from the forum post (eg. "`mkplugin MQ2Melee`").
* This will create the directory under your MQ2 source root and add a few files in there. Go to this directory in

  Explorer and open the .cpp file (eg. MQ2Melee.cpp) in your favourite text editor \(notepad will work

  just fine\). If you don't have any file extensions on your files (ie. none of them end with .cpp), then in Explorer

  go to Tools - Folder Options - View tab and untick "Hide file extensions for known file types".

* **Replace** the contents of this file with the code copied from the forum post. This code will generally start with

  a header indicating the name of the plugin, author, and maybe a brief description of the function of the plugin. An

  example of the first few lines of the MQ2Melee plugin are below:

```c++
//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//
// MQ2Melee.cpp |
// Author: s0rCieR |
// Version: 3.000 |
// Date: 20060213 |yes it should be
//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//
// #define aabug when alt abilities broken!
// #define cabug when combat abilities broken!
//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//

#include <mq/Plugin.h>

PreSetup("MQ2Melee");
PLUGIN_VERSION(3.000);
```

* Some plugins require additional files to be included as well (eg. .ccp, .h or .inc). Just create these files in the

  plugin directory with the names as given in the forum post. \*\*Make sure to save them as plain text documents with

  the correct extension (ie. do not save them with .txt extension) otherwise the plugin will not find them.\*\*

* After you've got the plugin created and all the files copied, open up the main MacroQuest2 project and add your

  newly created project:

  * In VS 6, Go to Projects-&gt;Insert Projects into workspace, then select .dsp (eg. MQ2Melee.dsp).
  * In VS .NET, go to File-&gt;Add Project-&gt;Existing project, and select the .vcproj \(eg.

    MQ2Melee.vcproj\).

  * In VS 2005 **AND NEWER**, go to File-&gt;Add-&gt;Existing project, and select the .vcproj \(or .vcxproj in

    newer versions of VS} (eg. MQ2Melee.vcproj or MQ2Melee.vcxproj).

* Compile the plugin:
  * In VS 2005 and newer, click on the plugin name in the Solution Explorer window, then click Build-&gt;Build

    .

## Using Plugins

MQ2 plugins are modular and can be loaded and unloaded on demand.

See [/plugin](../reference/commands/plugin.md) for information on loading and unloading plugins.

* If you need help with the plugin, you can most often find it within the main forum post or within the Wiki entry for

  that plugin. Some plugins have a built in help which can often be accessed in-game by typing the name of the

  plugin's slash command(s\) followed by help, or just the slash command\(s\) by itself. _\(more examples?)_

  * For example, in the MQ2MoveUtils plugin, the plugin adds the /moveto and /makecamp slash commands. Typing

    "`/moveto help`" and "`/makecamp help`" will bring up a list of current options for that part of the

    MQ2MoveUtils plugin.

## Plugins included with MacroQuest2

* [MQ2Bzsrch](../plugins/core-plugins/mq2bzsrch/) -- a bazaar search plug-in
* [MQ2Chat](../plugins/core-plugins/mq2chat.md) -- Directs MQ2 output to the regular chat window
* [MQ2ChatWnd](../plugins/core-plugins/mq2chatwnd/) -- Directs MQ2 output to a special chat window (safer)
* [MQ2CustomBinds](../plugins/core-plugins/mq2custombinds/) -- Allows you to specify custom commands to execute on a key combination
* [MQ2EQBugFix](../plugins/core-plugins/mq2eqbugfix.md) -- Currently nothing, but reserved for fixing bugs in EQ itself
* [MQ2EQIM](../plugins/discontinued/mq2eqim/) -- EQIM
* [MQ2HUD](../plugins/core-plugins/mq2hud/) -- Provides additional functionality to the HUD included with MQ2
* [MQ2IRC](../plugins/discontinued/mq2irc/) -- IRC plugin
* [MQ2ItemDisplay](../plugins/core-plugins/mq2itemdisplay/) -- Add extra data to item windows
* [MQ2Labels](../plugins/core-plugins/mq2labels.md) -- allows custom UI labels
* [MQ2Map](../plugins/core-plugins/mq2map/) -- enhanced map
* [MQ2Telnet](../plugins/discontinued/mq2telnet/) -- act as a telnet server for macro output

## List of Plugins with wiki pages

<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <ul>
          <li><a href="../plugins/community-plugins/mq2aapurchase/">MQ2AAPurchase</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2advpath/">MQ2AdvPath</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2autoforage/">MQ2AutoForage</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2autogroup/">MQ2AutoGroup</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2autologin/">MQ2AutoLogin</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2autosize/">MQ2AutoSize</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2autoskills/">MQ2AutoSkills</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2bandolier/">MQ2Bandolier</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2bufftool/">MQ2BuffTool</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2cast/">MQ2Cast</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2chat/">MQ2Chat</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2chatevents/">MQ2ChatEvents</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2chatwnd/">MQ2ChatWnd</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2clip/">MQ2Clip</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2cursor/">MQ2Cursor</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2custombinds/">MQ2CustomBinds</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2debuffs/">MQ2Debuffs</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2dps/">MQ2DPS</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2dpsadv/">MQ2DPSAdv</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="../plugins/community-plugins/mq2eqbc/">MQ2EQBC</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2eqbugfix/">MQ2EQBugFix</a>
          </li>
          <li><a href="../plugins/discontinued/mq2eqim/">MQ2EQIM</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2events/">MQ2Events</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2exchange/">MQ2Exchange</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2eqbc/">MQ2EQBC</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2fakelink/">MQ2FakeLink</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2feedme/">MQ2FeedMe</a>
          </li>
          <li><a href="../plugins/discontinued/mq2fps/">MQ2FPS</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2gmcheck/">MQ2GMCheck</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2hud/">MQ2HUD</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2hudmove/">MQ2HUDMove</a>
          </li>
          <li><a href="../plugins/discontinued/mq2irc/">MQ2IRC</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2itemdisplay/">MQ2ItemDisplay</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2labels/">MQ2Labels</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2linkdb/">MQ2Linkdb</a>
          </li>
          <li><a href="../plugins/core-plugins/mq2map/">MQ2Map</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2melee/">MQ2Melee</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2medley/">MQ2Medley</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2melee/">MQ2Melee</a>
          </li>
        </ul>
      </th>
      <th style="text-align:left">
        <ul>
          <li><a href="../plugins/community-plugins/mq2missing/">MQ2Missing</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2moveutils/">MQ2MoveUtils</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2moveutils/mq2moveutils-v11-faq/">MQ2MoveUtils:v11</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2netbots/">MQ2NetBots</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2netheal/">MQ2NetHeal</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2pq/">MQ2PQ</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2relaytells/">MQ2RelayTells</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2rez/">MQ2Rez</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2sound/">MQ2Sound</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2spawn/">MQ2Spawn</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2spawnmaster/">MQ2SpawnMaster</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2targets/">MQ2Targets</a>
          </li>
          <li><a href="../plugins/discontinued/mq2telnet/">MQ2Telnet</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2timestamp/">MQ2Timestamp</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2tracking/">MQ2Tracking</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2twist/">MQ2Twist</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2vendors/">MQ2Vendors</a>
          </li>
          <li><a href="../plugins/discontinued/mq2web/">MQ2Web</a>
          </li>
          <li><a href="../plugins/community-plugins/mq2xptracker/">MQ2XPTracker</a>
          </li>
        </ul>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

## Troubleshooting

See [General Help](./general-help.md) for troubleshooting plugin problems.

## Writing Your Own Plugins

See [Developing Plugins](./developing/) for further information.

### Unloading a plugin from within a plugin

Because call UnloadMQ2Plugin(name\) from within a plugin will crash, you must use a macro command to unload the plugin. DoCommand\(NULL, "/timed 20 /plugin unload"); will queue the macro command to unload after two seconds.

