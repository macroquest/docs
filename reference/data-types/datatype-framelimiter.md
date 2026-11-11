---
tags:
    - datatype
---
# `framelimiter`

<!--dt-desc-start-->
Data type to access frame limiter information.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | float BackgroundFPS
Value of the target background fps setting.
///

/// member | bool ClearScreen
Value of the clear screen when not rendering setting.
///

/// member | float CPU
Current CPU usage as %
///

/// member | bool Enabled
TRUE if the frame limiter feature is currently active.
///

/// member | float ForegroundFPS
Value of the target foreground fps setting.
///

/// member | float MinSimulationFPS
Value of the minimum simualtion rate setting.
///

/// member | float RenderFPS
Current graphics scene frame rate (visible fps).
///

/// member | bool SaveByChar
TRUE if settings for the frame limiter are being saved by character.
///

/// member | float SimulationFPS
Current simulation frame rate (game updates per second).
///

/// member | string Status
Either "Foreground" or "Background".
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
