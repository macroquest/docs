mq2main.dll checks the eqgame.exe client version to guarantee that you have the correct offsets/structures.

The date/time that is checked is in the eqgame.h file:  
#define \_\_ExpectedVersionDate "Apr 11 2005"

`#define __ExpectedVersionTime                              "14:42:23"`  
`#define __ActualVersionDate                                0x614CC4`  
`#define __ActualVersionTime                                0x614CD0`

The eqgame.exe client version is stored in the binary. The date on the file is when you downloaded it. For the April 12,
2005 patch as above, you can check these values with windbg. From your everquest directory, type:

windbg -Q eqgame.exe patchme

Then in the command window:

da 0x614CC4  
da 0x614CD0

It should match the expected values. If the expected values are **later** then the actual values, you need to patch
everquest. If the actual values are **later**, then you need to patch MQ. If you think you've already patched and
recompiled MQ, then you are using the wrong mq2main.dll.

You can find archived versions of Macroquest [here](https://macroquest2.com/downloads/zips.php).


