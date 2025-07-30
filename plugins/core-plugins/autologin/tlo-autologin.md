---
tags:
    - tlo
---
# `AutoLogin`

<!--tlo-desc-start-->
Returns "AutoLogin" string when plugin is loaded, provides access to AutoLogin functionality.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='AutoLogin', name='AutoLogin') }}

:   Returns "AutoLogin" string when plugin is loaded
<!--tlo-forms-end-->

## Associated DataTypes

## [AutoLogin](datatype-autologin.md)
{%
  include-markdown "plugins/core-plugins/autologin/datatype-autologin.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/autologin/datatype-autologin.md') }}

<h2>Members</h2>
{%
  include-markdown "plugins/core-plugins/autologin/datatype-autologin.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "plugins/core-plugins/autologin/datatype-autologin.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## [LoginProfile](datatype-loginprofile.md)
{%
  include-markdown "plugins/core-plugins/autologin/datatype-loginprofile.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/autologin/datatype-loginprofile.md') }}

<h2>Members</h2>
{%
  include-markdown "plugins/core-plugins/autologin/datatype-loginprofile.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "plugins/core-plugins/autologin/datatype-loginprofile.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Example

```text
/echo ${AutoLogin}          # Outputs "AutoLogin"
```
<!--tlo-linkrefs-start-->
[AutoLogin]: datatype-autologin.md
<!--tlo-linkrefs-end-->
