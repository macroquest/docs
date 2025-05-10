---
tags:
    - command
---
# /notify

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/notify <windowname> <control> [ <notification> [ <data> ] ]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
This command is used to interact with UI windows. It can simulate various mouse and keyboard interactions with UI elements.
<!--cmd-desc-end-->
## Parameters

- _windowname_ is the name of the window (e.g., "HotButtonWnd"). Use the Window Inspector (preferred) within the [/mqconsole](mqconsole.md) or the [/windows](windows.md) command to list all available windows.
- _control_ can be:
    * Control name (e.g., "HB_Button1")
    * "0" to send the notification to the window itself (commonly used for "close" and other window-level notifications)
- The _data_ parameter is primarily used with notifications like "newvalue" for sliders or "listselect" for lists

### Notifications:

| Notification | Description | Data Required |
|-------------|-------------|---------------|
| leftmouseup | Left-click on _controlname_ | No |
| leftmouseheld | Left-click and hold _controlname_ until _leftmouseheldup_ is performed | No |
| leftmouseheldup | Releases the mouse from _leftmouseheld_ | No |
| rightmouseup | Right-click on _controlname_ | No |
| rightmouseheld | Right-click and hold _controlname_ until _rightmouseheldup_ is performed | No |
| rightmouseheldup | Releases the mouse from _rightmouseheld_ | No |
| enter | Press the enter key on _controlname_ | No |
| close | Clicks the Close Window gadget of _windowname_ | No |
| mouseover | Hovers the mouse over _controlname_ | No |
| newvalue # | Changes the value in _controlname_ to # | Yes - number |
| listselect # | Selects the #th item in the _controlname_ list | Yes - number |
| leftmouse # | Clicks the #th item in the _controlname_ list | Yes - number |
| tabselect # | Selects the #th tab in the _controlname_ list | Yes - number |
| menuselect | Selects context menu item | Yes - menu item number/text |
| history | Used for command history in input boxes | No |
| link | Handles clickable links in windows | No |
| contextmenu | Opens context menu | No |
| resetdefaultposition | Resets window position to default | No |

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
