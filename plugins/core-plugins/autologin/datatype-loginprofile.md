---
tags:
    - datatype
---
# `LoginProfile`

<!--dt-desc-start-->
Datatype providing access to AutoLogin profile information.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='string', name='Account')}}

:   Account name associated with the profile

### {{ renderMember(type='string', name='Character')}}

:   Character name from the profile

### {{ renderMember(type='string', name='Server')}}

:   Server name from the profile

### {{ renderMember(type='string', name='Profile')}}

:   Profile group name (if part of a profile group)

### {{ renderMember(type='string', name='HotKey')}}

:   Hotkey assigned to the profile (if any)

### {{ renderMember(type='class', name='Class')}}

:   Character's class as shortname, also provides access to class type members.

### {{ renderMember(type='int', name='Level')}}

:   Character's level

### {{ renderMember(type='string', name='CustomCharacterIni')}}

:   Custom client INI file path if specified in the profile

### {{ renderMember(type='string', name='ToString') }}

:   Returns formatted profile info as "Profile: Character (Server)"
<!--dt-members-end-->

## Examples

```text
/echo ${AutoLogin.Profile.Account}  # Show account name
/echo ${AutoLogin.Profile.Level}    # Show character level
/echo ${AutoLogin.Profile}          # Show formatted profile info e.g. "MyProfile: MyCharacter (MyServer)"
/echo ${AutoLogin.Profile.Profile}  # Show profile name only
```
<!--dt-linkrefs-start-->
[string]: ../../../reference/data-types/datatype-string.md  
[int]: ../../../reference/data-types/datatype-int.md
[class]: ../../../reference/data-types/datatype-class.md
<!--dt-linkrefs-end-->
