## Description

**MQ2Vendors** is a plugin that will check a merchant's item list when you open that merchant, and will then notify you
if the merchant has any items that you are looking for.

-   If the vendor has an item you are looking for, you will be notified in the MQ chat window, and the merchant's name
    will be enclosed in >\>\>\> \<\<\<\< to highlight you to it.
-   **Note:** You will not be notified if the vendor item is a default item on that vendor (ie. if it does not have a
    quantity in the merchant window).

MQ2Vendors was created by Ceghkmv and can be found
[here](https://macroquest2.com/phpBB3/viewtopic.php?p=109662#109662).

## Commands

-   **/vendor add\|remove \<*ItemID\|ItemName\|ItemLink*\>**

  
Add/remove the relevant name/ID to/from the watch list. **Note:** Names are case sensitive! You can also use EQ links
instead of the name, and this is recommended, to ensure you get the correct capitalization.

-   **/vendor list**

  
List all items in the watch list.

-   **/vendor savevendors\|nosavevendors**

  
This enables or disables saving of vendors' default item list to a local INI file.

## Top-Level Objects

-   *[string](../data-types/datatype-string.md)* **${Vendor.Version}**  
    Outputs the version number.
-   *[bool](../data-types/datatype-bool.md)* **${Vendor.HasItems}**  
    Returns TRUE if the merchant has items you are looking for.

## See Also

-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Plugins](../documentation/macroquest2-plugins.md)


