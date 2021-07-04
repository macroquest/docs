` #turbo `  
` Sub Main()`  
`   /declare itemname string local`  
`   /declare itemqty int local`  
`   /declare itemprice int local`  
`   /declare result int local`  
`   `  
`   /if (!${Window[BarterMerchantWnd].Open}) {`  
`     :RightClickBuyer  `  
`     /click right target`  
`     /delay 10s ${Window[BarterMerchantWnd].Open}`  
`     /if (!${Window[BarterMerchantWnd].Open}) {`  
`       /echo You need to move closer to your target`  
`       /delay 1s`  
`       /goto :RightClickBuyer`  
`     }`  
`   }`  
`   /delay 3s`  
`   /for result 1 to 100`  
`     /if (${Bool[${Window[BarterMerchantWnd].Child[BTRMERCH_BuyLineList].List[${result},2]}]}) {`  
`       /varset itemname ${Window[BarterMerchantWnd].Child[BTRMERCH_BuyLineList].List[${result},2]}`  
`       /varset itemqty ${Window[BarterMerchantWnd].Child[BTRMERCH_BuyLineList].List[${result},3]}`  
`       /varset itemprice ${Window[BarterMerchantWnd].Child[BTRMERCH_BuyLineList].List[${result},4]}`  
`       /echo ${result} ${itemname} ${itemqty} ${itemprice}`  
`     }`  
`   /next result`  
` /return`


