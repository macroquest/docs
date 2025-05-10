---
tags:
   - tlo
---
# `FrameLimiter`

<!--tlo-desc-start-->
The FrameLimiter TLO provides access to the [frame limiter](../../main/features/framelimiter.md) feature.
<!--tlo-desc-end-->

## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='framelimiter', name='FrameLimiter') }}

:   The frame limiter object
<!--tlo-forms-end-->

## Associated DataTypes

## [framelimiter](../data-types/datatype-framelimiter.md)
{%
  include-markdown "reference/data-types/datatype-framelimiter.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-framelimiter.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-framelimiter.md"
  start="<!--dt-members-start -->"
  end="<!--dt-members-end -->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-framelimiter.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%} 

## Usage

Indicates that the frame limiter is enabled:

```
/echo ${FrameLimiter.Enabled}
```

<!--tlo-linkrefs-start-->
[bool]: ../data-types/datatype-bool.md
[string]: ../data-types/datatype-string.md
[float]: ../data-types/datatype-float.md
[framelimiter]: ../data-types/datatype-framelimiter.md
<!--tlo-linkrefs-end-->