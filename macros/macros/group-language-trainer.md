# Group Language Trainer

This macro was originally published in the Macro Depot 3.0 Forum, and has been successfully used to max out languages.

The speed at which languages are learned is dependent on either intelligence or wisdom, depending on class. The higher the stat, the quicker it goes up. A typical character will max all languages in about 3 passes.

**Instructions**

Paste this code into a file called lang.mac in your **\macros** directory.

In game, create a social with 5 lines of text, and place this in hotbutton 1. It doesn't matter what it says, as this macro will only end up spamming numbers anyway. While spamming, group members can either turn off group text in options, or can use /ignore \[spammer\] during the "lesson".

`|/////////////////////////////////////////////////////////////////////////////`  
`| Lang.mac`  
`|`  
`| /macro lang`  
`| Cycles through all your available languages`  
`| Target yourself to end`  
`|`  
`| Written by shuttle`  
`| Converted by bob_the_builder 4/22/04`  
`| Updated by loadingpleasewait 9/11/04`  
`|`  
`| Usage: /mac Lang`  
`|`  
`| NOTE: You must have spam text set to a social on hotbutton 1 as any other`  
`| way it does not actually speak the set languages.`  
`|`  
`|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\`

`#event LangHelp "Type /language help for a list"`

`|SetDeclares`  
`/declare LangNum outer`  
`/declare MinLangNum outer`  
`/declare MaxLangNum outer`

`|SetVars`  
`/varset MinLangNum 2`  
`/varset MaxLangNum 25`

`:MainLoop`  
`/if (${Target.ID}) /goto :end`

`|GroupChat`  
`/notify HotButtonWnd HB_Button1 leftmouseup`  
`/delay 2s`  
`|IncreaseLanguage`  
`/lang ${LangNum}`  
`/varcalc LangNum ${LangNum}+1`  
`/if (${LangNum}>${MaxLangNum}) /varset LangNum ${MinLangNum}`  
`/doevents`  
`/goto :MainLoop`

`:end`  
`/endmacro`

`Sub event_LangHelp`  
`/varset LangNum ${MinLangNum}`  
`/return`

