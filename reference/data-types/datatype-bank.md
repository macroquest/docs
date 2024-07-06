---
tags:
    - datatype
---
# `bank`

This is the type for your bank (not including shared bank or other bank features).

## Members

### {{ renderMember(type='int', name='BagSlots') }}

:   How many bag slots (base slots for bags/items) your bank has.

### {{ renderMember(type='int', name='FreeSlots') }}

:   How many free (empty) slots your bank has.  This includes slots where you have a bag and the bag has empty slots.  It accepts an index specifying one of the case insensitive bag sizes (tiny, small, medium, large, giant) or the corresponding number (0, 1, 2, 3, 4).  An invalid string specifying size will return NULL.  Specifying a numeric value less than 0 will use 0 and a value greater than 4 will use 4.

### {{ renderMember(type='int', name='TotalSlots') }}

:   How many total slots your bank has.  This includes slots where you have a bag and the bag has items in.  It accepts an index specifying one of the bag sizes or the corresponding number (see FreeSlots for a longer explanation).

### {{ renderMember(type='int', name='Platinum') }}

:   How much platinum you have in your bank.

### {{ renderMember(type='int', name='Gold') }}

:   How much gold you have in your bank.

### {{ renderMember(type='int', name='Silver') }}

:   How much silver you have in your bank.

### {{ renderMember(type='int', name='Copper') }}

:   How much copper you have in your bank.


## Examples

!!! Example

    === "MQScript"

    How many giant items can I add to my bank?

    ```
    /echo ${Inventory.Bank.FreeSlots[giant]}
    ```
    or

    ```
    /echo ${Inventory.Bank.FreeSlots[4]}
    ```

    How many total slots are there in my bank?

    ```
    /echo ${Inventory.Bank.TotalSlots}
    ```

    How many large slots are there in my bank (used and unused)?

    ```
    /echo ${Inventory.Bank.TotalSlots[large]}
    ```
    or

    ```
    /echo ${Inventory.Bank.TotalSlots[3]}
    ```

    === "Lua"

    How many giant items can I add to my bank?

    ```lua
    print(mq.TLO.Inventory.Bank.FreeSlots('giant')())
    ```
    or

    ```lua
    print(mq.TLO.Inventory.Bank.FreeSlots(4)())
    ```

    How many total slots are there in my bank?

    ```lua
    print(mq.TLO.Inventory.Bank.TotalSlots())
    ```

    How many large slots are there in my bank (used and unused)?

    ```lua
    print(mq.TLO.Inventory.Bank.TotalSlots('large')())
    ```
    or

    ```lua
    print(mq.TLO.Inventory.Bank.TotalSlots(3)())
    ```

[int]: datatype-int.md
