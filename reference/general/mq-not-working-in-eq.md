# MQ2 not working in EQ

If you are able to run MQ2 on your computer and if you have followed all the instructions given in the [Compile Manual](https://macroquest.org/includes/wassup/manual.php#compile) perfectly, and you are still having trouble getting MQ2 to work in EQ, the most likely issue is that you compiled using the wrong compiling program.

The only supported compilers are VC6++ (Visual C++ 6.0) and VC.net (Visual C++ .NET 2003 or 2005), and support for VC6 is being phased out.

[Use this page](https://macroquest.org/wiki/index.php/MacroQuest2:Compiling#Compiling_for_Free_with_VS2005_Express) and follow the instructions, and you will not fail.

Something else that can cause MQ2 to not show up in game. Even though it is in the Windows tray and also shows as loading when you are getting the splash screen prior to character select and on the splash screen as you enter the game world. A corrupted or missing macroquest.ini in the Release folder. If this is the case, download a new zip and recompile. Make sure there is a macroquest.ini in the release folder and that it is not corrupt by trying to open it with notepad or a text editor.

