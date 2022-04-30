# TLO:AltAbility

!!! danger
    The AltAbility TLO should not be used except for when experimenting  with data. If you've already purchased the AA, use `Me.AltAbility`, which is tailored to your character and is much faster.

## Forms

| **Type** | **Form** | **Description** |
| :--- | :--- | :--- |
| [_altability_](../data-types/datatype-altability.md) **AltAbility**[ _Number_ ] | Look up an AltAbility by its altability id |
| [_altability_](../data-types/datatype-altability.md) **AltAbility**[ _Name_ ] | Look up an AltAbility by its name |


## Example Usage

=== "MQScript"

    ```
    | Prints the pre-requisite AA ability needed to train Combat Stability
    /echo ${AltAbility[Combat Stability].RequiresAbility}
    ```

=== "Lua"

    ```lua
    -- Prints the pre-requisite AA ability needed to train Combat Stability
    print(mq.TLO.AltAbility('Combat Stability').RequiresAbility())
    ```
