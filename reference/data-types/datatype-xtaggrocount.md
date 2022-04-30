# DataType:xtaggrocount

## Description

Contains the data related to your extended target list

## Members

`XTAggroCount`  
`XTAggroCount[100]`

It returns the number of AUTO-HATER mobs on the extended target window where your aggro is less than the optional parameter N. N must be between 1-100 inclusive or it will be set to 100 (the default value).

So, ${Me.XTAggroCount} and ${Me.XTAggroCount[100]} are identical.
