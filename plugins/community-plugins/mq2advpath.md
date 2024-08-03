---
tags:
   - plugin
---

# MQ2AdvPath

## Description

This plugin allows you to record and playback player movement.

## Commands

### **`/play`**

```text
/play [pathName|off] [stop] [pause|unpause] [loop|noloop] [normal|reverse] [smart|nosmart] [flee|noflee] [door|nodoor] [fast|slow]
[eval|noeval] [zone|nozone] [list] [listcustom] [show] [help] [setflag1]-[setflag9] y/n [resetflags]
The /play command will execute each command on the line. The commands that should be used single, or at the end of a line:
[off] [list] [listcustom] [show] [help]

setflag1-setflag9 can be used anywhere in the line and uses the following format:
/play setflag1 n pathname or /play pathname setflag n (n can be any single alpha character)
AdvPath flags can be accessed using ${AdvPath.Flag1} - ${AdvPath.Flag9}
/play resetflags resets all flags(1-9) to 'y'
```

### **`/record`**

```text
/record
/record save <PathName> ##
/record Checkpoint <checkpointname>
/record help
## is the distance between checkpoints to force checkpoints to be writen to the path file
```

### **`/afollow`**

```text
/afollow [on|off] [pause|unpause] [slow|fast] [intercept]
/afollow spawn # [slow|fast] - default=fast
/afollow help
```

## Top-Level Object

### `AdvPath`

## Members

### {{ renderMember(type='bool', name='Active') }}

:   Plugin loaded and ready

### {{ renderMember(type='int', name='State') }}

:   FollowState, 0 = off, 1 = Following, 2 = Playing, 3 = Recording

### {{ renderMember(type='int', name='Waypoints') }}

:   Total Number of Waypoints

### {{ renderMember(type='int', name='NextWaypoint') }}

:   Number of NextWaypoint

### {{ renderMember(type='string', name='Y', params='Waypoint Name|#') }}

:   Y Location of Waypoint

### {{ renderMember(type='string', name='X', params='Waypoint Name|#') }}

:   X Location of Waypoint

### {{ renderMember(type='string', name='Z', params='Waypoint Name|#') }}

:   Z Location of Waypoint

### {{ renderMember(type='spawn', name='Monitor') }}

:   Spawn you're Following

### {{ renderMember(type='int', name='Idle') }}

:   Idle time when following and not moving

### {{ renderMember(type='float', name='Length') }}

:   Estimated length of the follow PathName

### {{ renderMember(type='bool', name='Following') }}

:   Following Spawn

### {{ renderMember(type='bool', name='Playing') }}

:   Playing path

### {{ renderMember(type='bool', name='Recording') }}

:   Recording path

### {{ renderMember(type='int', name='Status') }}

:   Status 0 = off , 1 = on , 2 = Paused

### {{ renderMember(type='bool', name='Paused') }}

:   Paused

## INI

```ini
[settings.server.ToonName]
AutoStopFollow=0
AutoStopPath=0
UseStuckLogic=1
```

```text
AutoStopFollow=0/1/2 - how it works now/pause/turns off
AutoStopPath=0/1/2 - how it works now/pause/turns off
UseStuckLogic= 0/1 = off/on
```

[int]: datatype-int.md
[bool]: datatype-bool.md
[spawn]: datatype-spawn
[float]: datatype-float.md
[string]: datatype-string.md
