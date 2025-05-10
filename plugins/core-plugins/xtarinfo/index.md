---
tags:
   - plugin
---
# XTarInfo

## Description
<!--desc-start-->
XTarInfo adds distance and other information to the Extended Target Window
<!--desc-end-->
## Commands

<a href="xtarinfo/">
{% 
  include-markdown "plugins/core-plugins/xtarinfo/xtarinfo.md"  
  start="<!--cmd-syntax-start-->" 
  end="<!--cmd-syntax-end-->" 
%}
</a>
:    {% include-markdown "plugins/core-plugins/xtarinfo/xtarinfo.md"
        start="<!--cmd-desc-start-->" 
        end="<!--cmd-desc-end-->" 
        trailing-newlines=false 
     %} {{ readMore('plugins/core-plugins/xtarinfo/xtarinfo.md') }}


## Settings

Example configuration:

```ini title="MQ2XTarInfo.ini"
[Default]
UsePerCharSettings=0

ShowDistance=1
DistanceLabelToolTip=XTarget Distance

[UI_default]
UseExtLayoutBox=0
ExtDistanceLoc=0,-20,70,0
; This label is used as a template for distance.
LabelBaseXT=Player_ManaLabel

[UI_Drakah]
; Custom settings built into plugin
ExtDistanceLoc=0,-20,80,0
; End Built-In Settings

[UI_Freq_SteelDragon]
; Custom settings built into plugin
ExtDistanceLoc=3,-10,70,28
LabelBaseXT=PW_ManaLabel
; End Built-In Settings

[UI_Melee]
; Custom settings built into plugin
ExtDistanceLoc=0,-20,90,0
; End Built-In Settings

[UI_RGInnerUI]
; Custom settings built into plugin
UseExtLayoutBox=1
; End Built-In Settings

[UI_sars]
; Custom settings built into plugin
UseExtLayoutBox=1
ExtDistanceLoc=0,12,30,-20
; End Built-In Settings

[UI_Simple_SticeGroup]
; Can use defaults

[UI_Sparxx]
; Custom settings built into plugin
ExtDistanceLoc=0,-10,80,0
; End Built-In Settings

[UI_zliz]
; Can use defaults
```