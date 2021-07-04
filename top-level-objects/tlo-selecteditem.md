## Description

Used to return information on the object that is selected in your own inventory while using a merchant.

## Forms

-   *[item](../data-types/datatype-item.md)* **SelectedItem**

## Access to Types

-   *[item](../data-types/datatype-item.md)* **item**

## Examples

`/if ( !${SelectedItem.ID} ) {`  
`   /echo Nothing in your inventory is selected`  
`} else {`  
`   /echo Size of the item: ${SelectedItem.Size}`  
`}`

`/if ( ${SelectedItem.Charges} < 1 ) {`  
`   Determines if the selected item is out of charges`  
`}`

`/if ( ${SelectedItem.Name.Equal[rusty dagger]} ) {`  
`   Checks to see if the selected item is a rusty dagger `  
`}`

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [item](../data-types/datatype-item.md)


