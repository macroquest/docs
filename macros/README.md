# Macro Reference

The use of macros is what really makes MacroQuest extremely powerful. Additional in-game functionality like [the map](../plugins/core-plugins/mq2map/), cross-zone targeting, enhanced [/who](../reference/commands/who.md), custom binds, [the HUD](../plugins/core-plugins/mq2hud/) and [plugins](../plugins/README.md) are useful, but macroing is what **Macro**Quest is all about.

See [Getting Started](getting-started.md) for some introductory information about macros. This page is concerned primarily with all the relevant information required to create your own macros.

## Macro Fundamentals

The MQ scripting language primarily involves the use of [Slash Commands](../reference/commands/README.md), [variables](variables.md), [Top-Level Objects](../reference/top-level-objects/) and some [Flow Control](flow-control.md) to help the macro along.

Accessing and manipulating data can be done with:

* [Variables](variables.md)
* [MQ2Data](mqdata.md)
    * [Top-Level Objects](../reference/top-level-objects/)
    * [Data Types](../reference/data-types/)
* [Slash Commands](../reference/commands/)

Things that can be added to the macro file:

* [Comments](comments.md)
* [Macro Directives](../reference/macro-directives/)
* [Custom Events](custom-events.md)

Controlling macro execution is done with:

* [Flow Control](flow-control.md)
* [Operators](operators.md)
* [Subroutines and Functions](subroutines.md)

## Include Files

An effective way to store subroutines which are used in multiple macros is by using include files. Include files hold code just like macros, but do not have a Main subroutine. To use an include file, add "\#include FileNameHere" in your macro. Include files can be any file type that works with plain text, such as .txt or .ini, but .inc is the most common file type.

## Macro Tips

* Sometimes you find a macro, and it's ALMOST what you need it for. In those cases, just edit the macro for your use.

  Take a look at this tutorial: [Editing Existing Macros](editing-existing-macros.md)

* Be patient and expect to fail a few times. If your macro involved killing stuff, expect to die a few times to

  perfect your macro.

* Remember to check your syntax. Most of the common problems people run into are becuase they haven't closed their

  {}'s, []'s and ()'s properly. If you have to, start at the end of the troublesome section and start matching up

  the {}'s, []'s and ()'s by hand. It can really help sometimes to just print the macro and start crossing them out.

* For people using Utraedit, here is an addition you can make to your [UltraEdit Syntax File](https://github.com/macroquest/docs/tree/abfc239f4d668ae116ab48141e49bbff82337715/other-applications/ultraedit-syntax-file.md)

  that will give you some syntax highlighting and reformatting.

