## Syntax

**<span style="color:red">/notify</span> *<span style="color:blue">windowname</span>*
*<span style="color:blue">0</span>*\|*<span style="color:blue">controlname</span>* \[ *notification* \[*data*\] \]**

## Description

This is used to interact with UI windows instead of using the mouse (/notify cannot be used to interact with objects).

-   Entering "0" for *controlname* would send the message to the window itself (used for "close" at least, possibly
    others).
-   The use of *data* will usually not be necessary unless you are notifying a slider control or a list.

|                      |                                                                          |
|----------------------|--------------------------------------------------------------------------|
| **leftmouseup**      | Left-click *controlname*                                                 |
| **leftmouseheld**    | Left-click and hold *controlname* until *leftmouseheldup* is performed   |
| **leftmouseheldup**  | Releases the mouse from *leftmouseheld*                                  |
| **rightmouseup**     | Right-click *controlname*                                                |
| **rightmouseheld**   | Right-click and hold *controlname* until *rightmouseheldup* is performed |
| **rightmouseheldup** | Releases the mouse from *rightmouseheld*                                 |
| **enter**            | Press the enter key on *controlname*                                     |
| **close**            | Clicks the Close Window gadget of *windowname*                           |
| **mouseover**        | Hovers the mouse over *controlname*                                      |
| **newvalue #**       | Changes the value in *controlname* to #                                  |
| **listselect #**     | Selects the #th item in the *controlname* list                           |
| **leftmouse #**      | Clicks the #th item in the *controlname* list                            |
| **tabselect #**      | Selects the #th tab in the *controlname* list                            |

**Notifications:**

## Examples

    /notify hotbuttonwnd HB_Button1 leftmouseup                                        Activates the first hotkey 
    /notify somewindow SomeSlider newvalue 100                                         Moves the referenced slider in the window to 100 
    /notify trackingwnd 0 close                                                        Closes the tracking window 
    /notify TradeskillWnd RecipeList listselect 1                                      Selects the first item in the RecipeList listbox
    /notify BuffWindow Buff${Math.Calc[${Me.Buff[BuffName].ID}-1].Int} leftmouseup     Cancels the buff called "BuffName"
    /notify InventoryWindow IW_Subwindows tabselect 4                                  Select 4th tab in the Inventory window  
    /notify AuraWindow Remove_Aura leftmouseup                                         Removes aura through the aura window
    /notify QuantityWnd QTYW_slider newvalue #                                         Adjust the value of the slider in Quantity Window.

Put the item name in the bazaar search dialog box

    /echo ${SelectedItem.Name}
    /notify BazaarSearchWnd ${SelectedItem.Name}

Select and click an item in a list

    /notify TaskWnd TASK_TaskList listselect 1
    /delay 4
    /notify TaskWnd TASK_TaskList leftmouse 1
    /delay 4

Select Parcel tab on Parcel Merchant and click Receive All button

    /notify MerchantWnd MW_MerchantSubWindows tabselect 3
    /delay 1s
    /notify MerchantWnd MW_Retrieve_All_Button leftmouseup


