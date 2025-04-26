---
tags:
   - plugin
---
# TargetInfo

## Description

Distance, line of sight and place-holder info directly on target. 

## Commands

{{ embedCommand('plugins/core-plugins/targetinfo/targetinfo.md') }}

## Settings

Example configuration:

```ini title="mq2targetinfo.ini"
[Default]
UsePerCharSettings=0
; Use unique settings for each character
ShowDistance=1
; Show distance to target
DistanceLabelToolTip=Target Distance
; Customize the tooltip text when you hover over target distance
ShowTargetInfo=1
; Show detailed target info
ShowPlaceholder=1
; Show placeholder/named information
ShowSight=1
; Toggle O/X based on line of sight


[UI_default]
Target_BuffWindow_TopOffset=76
dTopOffset=60
dBottomOffset=74
dLeftOffset=50

CanSeeTopOffset=47
CanSeeBottomOffset=61

TargetInfoWindowStyle=0
TargetInfoAnchoredToRight=0

; These two labels are used as templates for distance.
Label1=Player_ManaLabel
Label2=Player_FatigueLabel

TargetInfoLoc=34,48,0,40
TargetDistanceLoc=34,48,90,0
```
Settings for additional UIs are included in the default ini, but not shown here as they frequently change. 