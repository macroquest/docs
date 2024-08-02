# MQ2AdvPath

## Description

This plugin allows you to record and playback player movement.

## Commands

`/afollow [on|off] [nodoor|door]`<br>
`/afollow [pause|unpause]`<br>
`/afollow spawn # [nodoor|door]`<br>
`/afollow [nodoor|door]`<br>
`/play [PathName|off] [reverse|normal] [loop|noloop] [smart] [pause|unpause] [nodoor|door]`<br>
`/record`<br>
`/record save`<br>
`/record checkpoint`<br>

## Top-Level Object: ${AdvPath}

| **Type**                                              | **Member Name**  | **Description**                                            |
| :---------------------------------------------------- | :--------------- | :--------------------------------------------------------- |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Active**       | Plugin loaded and ready |
| [_int_](../../reference/data-types/datatype-int.md) | **State**        | FollowState, 0 = off, 1 = Following, 2 = Playing, 3 = Recording |
| [_int_](../../reference/data-types/datatype-int.md) | **Waypoints**    | Total Number of Waypoints |
| [_int_](../../reference/data-types/datatype-int.md) | **NextWaypoint** | Number of NextWaypoint |
| [_string_](../../reference/data-types/datatype-string.md) | **Y[Check Point Name OR Waypoint number]** | LOC |
| [_string_](../../reference/data-types/datatype-string.md) | **X[Check Point Name OR Waypoint number]** | LOC |
| [_string_](../../reference/data-types/datatype-string.md) | **Z[Check Point Name OR Waypoint number]** | LOC |
| [_spawn_](../../reference/data-types/datatype-spawn.md) | **Monitor**      | Spawn you're following |
| [_int_](../../reference/data-types/datatype-int.md) | **Idle**         | Idle time when following and not moving |
| [_float_](../../reference/data-types/datatype-float.md) | **Length**       | Estimated length of the follow path |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Following**    | Following spawn |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Playing**      | Playing path |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Recording**    | Recording path |
| [_int_](../../reference/data-types/datatype-int.md) | **Status**       | Status 0 = off , 1 = on , 2 = paused |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Paused**       | Paused |
