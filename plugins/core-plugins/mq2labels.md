# MQ2Labels

## Description

This plugin allows you to use MQ2Data within your EQ UI.

* It provides a number of EQTypes that can be used exactly as you use the built-in EQTypes.
* If there is not a suitable EQType for your use, you can use ToolTips to display custom information.

## MQ2 EQTypes

* **1000:** ${Me.CurrentMana}
* **1001:** ${Me.MaxMana}
* **1002:** ${Me.State}
* **1003:** ${Me.Speed}
* **1004:** ${Me.Heading}
* **1005:** ${Me.X}
* **1006:** ${Me.Y}
* **1007:** ${Me.Z}
* **1008:** ${Me.Dar}
* **1009:** ${Me.Cash}
* **1010:** ${Me.CashBank}
* **1011:** ${Me.Platinum\)
* **1012:** ${Me.PlatinumShared}
* **1013:** ${Me.Gold}
* **1014:** ${Me.SilverBank}
* **1015:** ${Me.CopperBank}

\* **2000:** ${Target.Level}

* **2001:** ${Target.Class}
* **2002:** ${Target.Race}
* **2003:** ${Target.Distance}
* **2004:** _none_
* **2005:** ${Target.State}
* **2006:** ${Target.X}
* **2007:** ${Target.Y}
* **2008:** ${Target.Z}
* **2009:** ${Target.Heading}
* **2010:** ${Target.Speed}
* **2011:** ${Target.ID}

\* **3000:** ${Zone}

* **3001:** _none_
* **3002:** ${Me.Bound}
* **3003:** ${Time.Time24}
* **3004:** ${Time.Hour}
* **3005:** ${Time.Minute}
* **3006:** ${Time.Second}
* **3007:** ${Time.Date}
* **3008:** ${Time.Year}
* **3009:** ${Time.Month}
* **3010:** ${Time.Day}
* **3011:** ${If\[${Spawn\[gm\].ID},TRUE,FALSE\]}
* **3012:** ${Me.FreeInventory}

### Example

TargetLevel2000 2true243322140255255 **0**truefalsetruefalse

## Using Tooltips

Tooltips can be used to add any information \(even information from plugins or macros\) that doesn't have a built-in EQType. You add the EQType of 9999 and then add the MQ2Data string that gives you your required information within the

tags.\`9999\`\`${variable}\`

### Example

Buff0Duration9999${Me.Buff1.Duration} 2true23315314255255 **255**truefalsefalse

### Note about ToolTipReference

There are certain characters that are used in XML Code that are reserved. If these characters are used in the tooltipreference they will cause errors and the UI will fail to load. The most notable of these characters is the "\&lt;" symbol. The "&gt;" symbol can still be used for comparisons. So In cases where you would use "\&lt;", rephase the statement to use "&gt;" instead. The "&" character also causes problems. In the case where you use a "&&" in your if statements use nested ifs to get around the problem.

#### Example

${If\[${Target.ID} && ${Target.Casting},${Target.CleanName} is casting.,\]}

would become

${If\[${Target.ID},${If\[${Target.Casting},${Target.CleanName} is casting.,\]},\]}

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)
* [Custom UIs](../../documentation/custom-uis.md)

