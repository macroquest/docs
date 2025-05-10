---
tags:
    - datatype
---
# `xtarget`

<!--dt-desc-start-->
Contains the data related to your extended target list
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='int', name='ID') }}

:   ID of specified XTarget

### {{ renderMember(type='string', name='Name') }}

:   Name of specified XTarget

### {{ renderMember(type='int', name='PctAggro') }}

:   PctAggro of specified XTarget

### {{ renderMember(type='string', name='TargetType') }}

:   Extended target type. Will return one of the following:

    * Empty Target
    * Auto Hater
    * Specific PC
    * Specific NPC
    * Target's Target
    * Group Tank
    * Group Tank's Target
    * Group Assist
    * Group Assist Target
    * Group Puller
    * Group Puller Target
    * Group Mark 1
    * Group Mark 2
    * Group Mark 3
    * Raid Assist 1
    * Raid Assist 2
    * Raid Assist 3
    * Raid Assist 1 Target
    * Raid Assist 2 Target
    * Raid Assist 3 Target
    * Raid Mark 1
    * Raid Mark 2
    * Raid Mark 3
    * Pet Target
    * Mercenary Target

### [string][string] `To String`

:   Number of current extended targets

<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
