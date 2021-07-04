# MQ2AdvPath

## Description

This plugin allows you to record and playback player movement.

## Commands

* /afollow \[on\|off\] \[nodoor\|\*door\]
* /afollow \[pause\|unpause\]
* /afollow spawn \# \[nodoor\|\*door\]
* /afollow \[nodoor\|\*door\]
* /play \[PathName\|off\] \[reverse\|\*normal\] \[loop\|\*noloop\] \[smart\] \[pause\|\*unpause\] \[nodoor\|\*door\]
* /record 
* /record save 
* /record checkpoint 

## TLOs

* ${AdvPath.Active} Plugin Loaded and ready
* ${AdvPath.State} // FollowState, 0 = off, 1 = Following, 2 = Playing, 3 = Recording
* ${AdvPath.Waypoints} // Total Number of Waypoints
* ${AdvPath.NextWaypoint} // Number of NextWaypoint
* ${AdvPath.Y\[Check Point Name OR Waypoint number\]} LOC
* ${AdvPath.X\[Check Point Name OR Waypoint number\]} LOC
* ${AdvPath.Z\[Check Point Name OR Waypoint number\]} LOC
* ${AdvPath.Monitor} // Spawn your following
* ${AdvPath.Idle} // Idel time when following and not moving
* ${AdvPath.Length} // Estimated length off the follow path
* ${AdvPath.Following} // BOOL Following spawn ?
* ${AdvPath.Playing} // BOOL Playing ?
* ${AdvPath.Recording} // BOOL Recording?
* ${AdvPath.Status} // INT Status 0 = off , 1 = on , 2 = paused?
* ${AdvPath.Paused} // BOOL Paused?
* ${AdvPath.WaitingWarp} // BOOL Wating if warp take action ?

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

