# MQ2FPS

{% hint style="warning" %}
This plugin is deprecated and no longer available for MacroQuest. Framelimiting functionality is now part of **main**.
{% endhint %}

### Description

[MQ2FPS](https://macroquest2.com/phpBB3/viewtopic.php?t=8346) \(VIP only\) is a plugin that changes the frames per second of the Everquest screen when it is in focus and when it is in the background.

**Commands**

* /fps
* /render
* /maxfps

**/fps \[on\|off\]**  
**/fps \[x\|y\]**  
**/fps mode \[absolute\|calculate\]**

* On/Off enables or disables the FPS display.
* Use _x_ and _y_ to control the location of the FPS display on the screen.
* With _mode_ you can change the FPS limiter mode to the one specified \(absolute or calculate\) or toggle between the

  two if no mode is specified.

\*\*/render \[bg\|fg\]

## \|~\#\*\*

This sets the foreground or background rendering rate \(ie. how many frames will be drawn\). Setting the rendering rate does not slow down the game at all. The client still responds to the mouse and keyboard the same, the UI is still drawn, but the world itself is not drawn as often.

* With _\#_, [MQ2FPS](./) will drawn 1 out of \# frames.
* The use of _~\#_ will cause [MQ2FPS](./) to draw \#-1 out of \# frames.

**Example**

```text
 /render bg 3              Draws 1 out of 3 frames
 /render bg ~3             Draws 2 out of 3 frames
```

**/maxfps \[ bg \| fg \] \[ \# \]**  
Sets the foreground or background framerate.

**Example**

```text
 /maxfps fg 30            Sets foreground framerate to 30 FPS
 /maxfps bg 5             Sets background framerate to 5 FPS
```

### Top-Level Objects

[_fps_]() [**FPS**](tlo-fps.md)

### Data types

[_fps_]() **fps**

### Examples

`/maxfps fg 25`  
`/maxfps bg 25`  
`/fps on`  
`/fps mode absolute`  
`/fps 10,25`  
`/render fg 1`  
`/render bg 75`

### Sample INI File

`ForegroundMaxFPS=25`  
`BackgroundMaxFPS=25`  
`Indicator=1`  
`Mode=1`  
`IndicatorX=10`  
`IndicatorY=25`  
`[Rendering]`  
`FGRate=1`  
`ReverseFGRate=0`  
`BGRate=75`  
`ReverseBGRate=0`

### See Also

* [Data Types](../../../data-types-and-top-level-objects/data-types/)
* [Top-Level Objects](../../../data-types-and-top-level-objects/top-level-objects/)
* [Plugins](../../../documentation/macroquest2-plugins.md)

