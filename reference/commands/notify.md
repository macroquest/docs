# /notify

## Syntax

**/notify** _**windowname**_ **\*\*\_**0**\_**\|**\_**controlname**\_** [ **\_**notification**\_** \[**\_**data**\_**\] ]\*\*

## Description

This is used to interact with UI windows instead of using the mouse (/notify cannot be used to interact with objects).

* Entering "0" for _controlname_ would send the message to the window itself \(used for "close" at least, possibly

  others\).

* The use of _data_ will usually not be necessary unless you are notifying a slider control or a list.

|  |  |
| :--- | :--- |
| **leftmouseup** | Left-click _controlname_ |
| **leftmouseheld** | Left-click and hold _controlname_ until _leftmouseheldup_ is performed |
| **leftmouseheldup** | Releases the mouse from _leftmouseheld_ |
| **rightmouseup** | Right-click _controlname_ |
| **rightmouseheld** | Right-click and hold _controlname_ until _rightmouseheldup_ is performed |
| **rightmouseheldup** | Releases the mouse from _rightmouseheld_ |
| **enter** | Press the enter key on _controlname_ |
| **close** | Clicks the Close Window gadget of _windowname_ |
| **mouseover** | Hovers the mouse over _controlname_ |
| **newvalue \#** | Changes the value in _controlname_ to \# |
| **listselect \#** | Selects the \#th item in the _controlname_ list |
| **leftmouse \#** | Clicks the \#th item in the _controlname_ list |
| **tabselect \#** | Selects the \#th tab in the _controlname_ list |

**Notifications:**

## Examples

```text
/notify hotbuttonwnd HB_Button1 leftmouseup                                        Activates the first hotkey 
/notify somewindow SomeSlider newvalue 100                                         Moves the referenced slider in the window to 100 
/notify trackingwnd 0 close                                                        Closes the tracking window 
/notify TradeskillWnd RecipeList listselect 1                                      Selects the first item in the RecipeList listbox
/notify BuffWindow Buff${Math.Calc[${Me.Buff[BuffName].ID}-1].Int} leftmouseup     Cancels the buff called "BuffName"
/notify InventoryWindow IW_Subwindows tabselect 4                                  Select 4th tab in the Inventory window  
/notify AuraWindow Remove_Aura leftmouseup                                         Removes aura through the aura window
/notify QuantityWnd QTYW_slider newvalue #                                         Adjust the value of the slider in Quantity Window.
```

Put the item name in the bazaar search dialog box

```text
/echo ${SelectedItem.Name}
/notify BazaarSearchWnd ${SelectedItem.Name}
```

Select and click an item in a list

```text
/notify TaskWnd TASK_TaskList listselect 1
/delay 4
/notify TaskWnd TASK_TaskList leftmouse 1
/delay 4
```

Select Parcel tab on Parcel Merchant and click Receive All button

```text
/notify MerchantWnd MW_MerchantSubWindows tabselect 3
/delay 1s
/notify MerchantWnd MW_Retrieve_All_Button leftmouseup
```

