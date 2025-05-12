---
tags:
    - command
---
# /hotbutton

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/hotbutton <name> [<color>] [<line>:][<cursor>:][<text>]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Extends the built in /hotbutton command with multiple lines support, cursor attachment, and "names with spaces" (in quotes) support.
<!--cmd-desc-end-->
## Examples

|  |  |
| :--- | :--- |
| **Example** | **Description** |
| /hotbutton TheName 14 1:0:/echo hi | Where 14 1:0: in this case means use color 14, then place /echo hi on LINE 1 and NO Cursor Attachment. |
| /hotbutton TheName 14 1:/echo hi | Where 14 1: in this case means use color 14, then place /echo hi on LINE 1. |
| /hotbutton TheName 1:0:/echo hi | Where 1:0: in this case means place /echo hi on LINE 1 and NO Cursor Attachment. |
| /hotbutton TheName 1:/echo hi | Where 1: in this case means place /echo hi on LINE 1. |
| /hotbutton TheName 0:/echo hi | Where 0: in this case means NO Cursor Attachment. |
| /hotbutton TheName 14 /echo hi | just calls the eq function like before. |
| /hotbutton TheName /echo hi | just calls the eq function like before. |

