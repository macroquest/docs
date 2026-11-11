---
tags:
    - datatype
---
# `type`

<!--dt-desc-start-->
Contains information about data types
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int InheritedType
Type of inherited type, if applicable.

Ex: character inherits from spawn, so its inherited type will be spawn.
///

/// member | string Name
Type name
///

/// member | string Member[N]
Member name based on an internal ID number (based on 1 through _N_, not all values will be used)
///

/// member | int Member[name]
Member internal ID number based on _name_ (will be a number from 1 to N)
///

### [string][string] `(To String)`

:   Same as **Name**

<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
