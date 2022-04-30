# TLO:Pet

## Description

Pet object which allows you to get properties of your pet.

## Access to Types

* [_pet_](../data-types/datatype-pet.md) **pet**

Pet is a TLO that has access to your current Pet [pet](../data-types/datatype-pet.md) reference type. The [pet](../data-types/datatype-pet.md) type extends the spawn, and as such, has access to the properties of the [spawn](../data-types/datatype-spawn.md) type as well.

## Examples

`/echo My Pet's Stance is currently set to: ${Pet.Stance}`  
`/echo My Pet's Name: ${Pet.CleanName}%`  
`/echo My Pet's Target has gone Berserk! ${Pet.Target.IsBerserk}`
