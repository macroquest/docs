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
/// member | string Account
Account name associated with the profile
///

/// member | string Character
Character name from the profile
///

/// member | string Server
Server name from the profile
///

/// member | string Profile
Profile group name (if part of a profile group)
///

/// member | string HotKey
Hotkey assigned to the profile (if any)
///

/// member | class Class
Character's class as shortname, also provides access to class type members.
///

/// member | int Level
Character's level
///

/// member | string CustomCharacterIni
Custom client INI file path if specified in the profile
///

/// member | string ToString
Returns formatted profile info as "Profile: Character (Server)"
///
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
