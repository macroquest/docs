---
tags:
    - datatype
---
# `fellowship`

<!--dt-desc-start-->
Contains all the data about your fellowship
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='bool', name='Campfire') }}

:   TRUE if campfire is up, FALSE if not

### {{ renderMember(type='ticks', name='CampfireDuration') }}

:   Time left on current campfire

### {{ renderMember(type='float', name='CampfireX') }}

:   Campfire X location

### {{ renderMember(type='float', name='CampfireY') }}

:   Campfire Y location

### {{ renderMember(type='float', name='CampfireZ') }}

:   Campfire Z location

### {{ renderMember(type='zone', name='CampfireZone') }}

:   Zone information for the zone that contains your campfire

### {{ renderMember(type='bool', name='Exists') }}

:   Returns TRUE if a fellowship exists.

### {{ renderMember(type='int', name='ID') }}

:   Fellowship ID

### {{ renderMember(type='string', name='Leader') }}

:   Fellowship leader's name

### {{ renderMember(type='fellowshipmember', name='Member', params='name|#') }}

:   Member data by _name_ or _#_

### {{ renderMember(type='int', name='Members') }}

:   Number of members in the fellowship

### {{ renderMember(type='string', name='MotD') }}

:   Fellowship Message of the Day

### {{ renderMember(type='bool', name='Sharing', params='N') }}

:   Returns TRUE if exp sharing is enabled for the Nth member

### [string][string] `To String`

:   TRUE if currently in a fellowship, FALSE if not
<!--dt-members-end-->

## Changelog

* May 13, 2022: Added Exists
* December 3rd, 2020: Added Sharing
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[fellowshipmember]: datatype-fellowshipmember.md
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
[ticks]: datatype-ticks.md
[zone]: datatype-zone.md
<!--dt-linkrefs-end-->
