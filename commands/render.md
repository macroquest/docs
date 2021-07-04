## Syntax

**<span style="color:red">/render</span> \[<span style="color:blue">bg</span>\|<span style="color:blue">fg</span>\]
#\|\~#**

## Description

This sets the foreground or background rendering rate (ie. how many frames will be drawn). Setting the rendering rate
does not slow down the game at all. The client still responds to the mouse and keyboard the same, the UI is still drawn,
but the world itself is not drawn as often.

-   With *#*, [MQ2FPS](../plugins/mq2fps.md) will drawn 1 out of # frames.
-   The use of *\~#* will cause [MQ2FPS](../plugins/mq2fps.md) to draw #-1 out of # frames.

## Example

     /render bg 3              Draws 1 out of 3 frames
     /render bg ~3             Draws 2 out of 3 frames

## See Also

-   [MQ2FPS](../plugins/mq2fps.md)
-   [/fps](fps.md)
-   [/maxfps](maxfps.md)


