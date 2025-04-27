---
tags:
    - tlo
---
# `FrameLimiter`

The FrameLimiter TLO provides access to the [frame limiter](../../main/features/framelimiter.md) feature.

## Forms

### {{ renderMember(type='framelimiter', name='FrameLimiter') }}

:   The frame limiter object


## Associated DataTypes

{{ embedMQType('reference/data-types/datatype-framelimiter.md') }}

## Usage

Indicates that the frame limiter is enabled:

```
/echo ${FrameLimiter.Enabled}
```

[bool]: ../data-types/datatype-bool.md
[string]: ../data-types/datatype-string.md
[float]: ../data-types/datatype-float.md
[framelimiter]: ../data-types/datatype-framelimiter.md