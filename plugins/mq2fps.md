## Description

[MQ2FPS](https://macroquest2.com/phpBB3/viewtopic.php?t=8346) (VIP only) is a plugin that changes the
frames per second of the Everquest screen when it is in focus and when it is in the background.

**Commands**

-   /fps
-   /render
-   /maxfps

**<span style="color:red">/fps</span> \[<span style="color:blue">on</span>\|<span style="color:blue">off</span>\]**  
**<span style="color:red">/fps</span> \[<span style="color:blue">x</span>\|<span style="color:blue">y</span>\]**  
**<span style="color:red">/fps</span> <span style="color:blue">mode</span>
\[<span style="color:blue">absolute</span>\|<span style="color:blue">calculate</span>\]**

-   On/Off enables or disables the FPS display.
-   Use *x* and *y* to control the location of the FPS display on the screen.
-   With *mode* you can change the FPS limiter mode to the one specified (absolute or calculate) or toggle between the
    two if no mode is specified.

**<span style="color:red">/render</span> \[<span style="color:blue">bg</span>\|<span style="color:blue">fg</span>\]
#\|\~#**

This sets the foreground or background rendering rate (ie. how many frames will be drawn). Setting the rendering rate
does not slow down the game at all. The client still responds to the mouse and keyboard the same, the UI is still drawn,
but the world itself is not drawn as often.

-   With *#*, [MQ2FPS](mq2fps.md) will drawn 1 out of # frames.
-   The use of *\~#* will cause [MQ2FPS](mq2fps.md) to draw #-1 out of # frames.

**Example**  

     /render bg 3              Draws 1 out of 3 frames
     /render bg ~3             Draws 2 out of 3 frames

**<span style="color:red">/maxfps</span> \[ <span style="color:blue">bg</span> \| <span style="color:blue">fg</span> \]
\[ # \]**  
Sets the foreground or background framerate.

**Example**  

     /maxfps fg 30            Sets foreground framerate to 30 FPS
     /maxfps bg 5             Sets background framerate to 5 FPS

## Top-Level Objects

*[fps](../data-types/mq2fps-datatype-fps.md)* **[FPS](../top-level-objects/tlo-fps.md)**

## Data types

*[fps](../data-types/mq2fps-datatype-fps.md)* **fps**

## Examples

`/maxfps fg 25`  
`/maxfps bg 25`  
`/fps on`  
`/fps mode absolute`  
`/fps 10,25`  
`/render fg 1`  
`/render bg 75`

## Sample INI File

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

## See Also

-   [Data Types](../data-types/data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Plugins](../documentation/macroquest2-plugins.md)


