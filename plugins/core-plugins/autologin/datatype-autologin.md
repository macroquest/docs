---
tags:
    - datatype
---
# `AutoLogin`

<!--dt-desc-start-->
Datatype providing access to AutoLogin status and profile information.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='bool', name='Active')}}

:   True when actively performing automated login

### {{ renderMember(type='LoginProfile', name='Profile')}}

:   Displays autologin profile information, also provides access to current profile information ([LoginProfile] type)
<!--dt-members-end-->

## Examples

```text
/echo ${AutoLogin.Active}           # Check if autologin is running
/echo ${AutoLogin.Profile.Account}  # Show account name from profile
```
<!--dt-linkrefs-start-->
[bool]: ../../../reference/data-types/datatype-bool.md
[LoginProfile]: datatype-loginprofile.md
<!--dt-linkrefs-end-->
