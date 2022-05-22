---
tags:
    - tlo
---

# `Target`

Object used to get information about your current target.

## Forms

[_spawn_](../data-types/datatype-spawn.md) **Target**

:   Returns the spawn object for the current target.


!!! warning "Note"

    These examples are not specific to target but work on any spawn type.

!!! note

    To display the target's unique name as sent by EQ use `${Target}` or `${Target.Name}`

    This will return `a_commander01` on a living mob or `a_commander's_corpse0` on a dead mob.

    To display the target's clean name (also similar to %t on living mobs) use
    `${Target.CleanName}` or `${Target.DisplayName}`

    This will return `a commander` on a living mob or `a commander's corpse` on a dead mob.

    To display the name as used by '%t' on a corpse use the `${Target.DisplayName}`

    This will return `a commander` when the corpse is targetted.

!!! example

    To display the spell ID of the snare debuff use ${Target.Snared.ID}

    ```
    /echo ${Target.Snared.ID}
    ```

    Example of using new Slowed target datatype

    ```
    /echo ${Target.Slowed.Name} will fade in ${Target.Slowed.Duration.TotalSeconds}s
    ```

    returns "Tepid Deeds will fade in 114s"

    Example of using new Mezzed target datatype

    ```
    /echo ${Target} will break mezz in ${Target.Mezzed.Duration.TotalSeconds}s`
    ```

    returns "a\_pyre\_beetle48 will break mezz in 66s"

