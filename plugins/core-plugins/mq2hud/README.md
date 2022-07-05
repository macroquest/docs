---
tags:
   - plugin
---
# MQ2HUD

## Description

This plugin provides a Heads Up Display for your EQ window, which can provide a large amount of information in a relatively small amount of space. The HUD acts as a transparent background layer, upon which any information can be displayed. Each element of the HUD gets parsed each time MQ2Data is displayed, so there is no need to reload the HUD after making changes to the .ini file, they are instantly available as soon as you save.

The HUD is customized by entries in the MQ2HUD.ini file. The .ini file allows any number of HUDs to be created and saved within. Loading a new HUD from the .ini file can be done with `/loadhud`. The entry names are not case-sensitive.

The default HUD entry is called \[Elements\] and can be loaded with the `/defaulthud` command.

You can toggle the display of the HUD by using F11.

## Commands

* [/hud](hud.md)
* [/loadhud](loadhud.md)
* [/defaulthud](defaulthud.md)
* [/classhud](classhud.md)
* [/zonehud](zonehud.md)

## Top-Level Objects

* [_string_]() **HUD**

Name of currently loaded HUD

## INI File Format

Entries in the MQ2HUD.ini file are in the following format:

`[Elements]`  
`TYPE,X,Y,RED,GREEN,BLUE,TEXT`

* **TYPE** can be a combination of the following \(just add the numbers\):
  * **1:** Display in non-fullscreen mode
  * **2:** Display in fullscreen mode \("F10 mode"\)
  * **4:** Based on cursor location
  * **8:** Display at charselect
  * **16:** Only parse if a macro IS running
* **X** and **Y** denote the location of the entry on the screen \(0,0 is the upper left of your screen\)
* **RED**, **GREEN** and **BLUE** are RGB values for the **TEXT** color \(255,255,255 is white; 0,0,0 is black\)
* **TEXT** is the MQ2Data you wish to display. As a tip, the [If](../../../reference/top-level-objects/tlo-if.md) TLO is very useful here.

## Examples

`[Elements]`  
`TargetInfo=3,5,35,255,255,255,${Target}`  
`GMIndicator=3,5,45,0,0,255,${Spawn[gm]}`  
`CursorItemName=7,-15,-15,255,255,255,${If[${Cursor.ID},${Cursor},]}`  
`ClickMeForFun=6,-25,-25,255,255,255,${If[!${Cursor.ID},click me,]}`  
`MacroName=19,5,70,255,255,255,${If[${Bool[${Macro}]}, Current Macro Running - ${Macro},]}`

In the above HUD, the _CursorItemName_ entry states that it will show the name of your cursor item in all modes. Using 6 as the **TYPE** will display the cursor in full-screen mode only.

`/loadhud bard`

This will load the \[bard\] section of the MQ2HUD.ini.

## Code Segments

This section contains code segments to help you customize your HUD. Please be sure to substitute the X, Y cords for the location you'd like to see them on your HUD.

`//AAXP`  
`AAXPText=3,X,Y,255,234,8,AAXP`  
`AAXP=3,X,Y,255,234,8,${Me.PctAAExp}`

`//AttackSpeed`  
`AttackSpeedText=3,X,Y,255,234,8,AttackSpeed :`  
`AttackSpeed=3,X,Y,255,234,8,${Me.AttackSpeed}`

`//Date`  
`Datetext=3,X,Y,255,234,8,Todays Date Is`  
`Date=3,X,Y,255,234,8,${Time.Date}`

`//Damage Absorb Left`  
`DamageShieldText=3,X,Y,255,234,8,Dmg Abs. Left`  
`DamageShield=3,X,Y,255,234,8,${Me.Dar}`

`//Vet AA's`  
`ThroneText=3,500,402,255,234,8,GL Port - - - -`  
`ThroneReadyText=3,610,402,0,255,0,${If[${Me.AltAbilityReady[Throne Of Heroes]},Ready,]}`  
`ThroneNotReady=3,610,402,255,0,0,${If[!${Me.AltAbilityReady[Throne Of Heroes]},${Me.AltAbilityTimer[Throne Of Heroes].TimeHMS},]}`

`//what macro is currently running`  
`Macro1=3,110,110,0,250,0,${If[${Macro.Name.NotEqual["NULL"]},${Macro.Name},]}`  
`Macro2=3,10,110,225,250,225,MACRO RUNNING =`

`//if the macro Raid Druid (Autobot) is currently paused`  
`RDPauseInd1=3,10,122,225,250,225,RD PAUSED =`  
`RDPauseInd2=3,85,122,225,0,0,${RDPause}`
