## Intro

This is a page for help with compiling MQ2. You should start here if you can't get it compiled, or it's crashing when
you enter the game, or crashing when you use a command.

If you're having a problem with a macro or snippet, see [Help_Macros](help-macros.md) or if you're having a
problem with a plugin, see [Help_Plugins](help-plugins.md)

## General Compiling Help

-   First, do you have the latest MQ2 source? Check the [download](https://macroquest2.com/main.php?p=download) page
    for the latest source and use that if you're not already. If the link says MQ2-down.zip or something similar, then
    MQ2 is not working. Keep checking back until a formal release is posted. The main download may get updated several
    times a day if it's around patch days. Even if it's not, you should always be using the latest source files.
-   Is the problem with MacroQuest2 or with a custom plugin? If you suspect it may be a plugin problem (or if you're
    unsure), then it's worth downloading the source again and just compiling MQ2 to see if you can narrow down the
    problem. Follow the directions in [MacroQuest2:Compiling](macroquest2-compiling.md) and compile a fresh MQ2
    with no plugins.
    -   If it does turn out to be a plugin problem, see [Help_Plugins](help-plugins.md) for further help
        diagnosing plugin problems.

## Compiling Problems

### Crash to Desktop

If you're crashing to desktop, EQ is crashing when starting, or you're crashing immediately when entering the game, make
sure you unload any custom or non-standard plugins. Better yet, delete your MacroQuest2.ini file and restart MQ2. This
will load up a "vanilla" MQ2 with no additional plugins. You can then load each plugin manually to find the faulty one.
If you're still having problems when you've got no custom plugins loaded, see the [Crash to
Desktop](crash-to-desktop.md) page for more information on how to report problems when MQ2 crashes completely.

### Incorrect Client Version

See the [Incorrect Client Version](incorrect-client-version.md) page for further information.

### LINK : fatal error LNK1181: cannot open input file "..\\Release\\MQ2Main.lib"

This means that MQ2Main has not been compiled. Compile MQ2Main first, and then build the rest of the project.

### error C2143: syntax error : missing ')' before 'if'

Edit the following line:

    pDefault=strtok(NULL,"▌");"

And change it to:

    pDefault=strtok(NULL,"|");

### Fatal error C1189: #error : Unknown CPU Architecture!

This is caused by the MQ2 source files being posted in an incorrect OS format (eg. Mac format). This problem will be
fixed very quickly, so check the download page again to see if a new version has been posted.

### C:\\MQ\\MQ2Main\\MQ2Main.h(31) : fatal error C1083: Cannot open include file: 'windows.h': No such file or directory

windows.h is part of Microsoft's SDK. You don't have it. Go get it. Or, maybe you do have it but you didn't set the
environment variables correctly. Either way: [1](http://www.microsoft.com)

(if you change this section, i will ban you.) :)

### No .exe file generated

The .exe file is not suposed to be produced by the compilation / linking - it is pre-compiled and part of the
distribution! Only the DLL-files are produced!

### LINK : fatal error LNK1181: Cannot open file 'Release\\MQ2Main.lib'

You shouldn't be here -- you didn't follow directions.

You must compile the MQ2Main project before the other subprojects.

### LINK : fatal error LNK1104: cannot open file 'libcpmt.lib'

Problem occured during step 9 of the walkthrough. Researched the problem extensively, the closest match find was
libcp.lib and several discussions on how it might be due to an older version, however, the version that produced the
libcpmt.lib error was just downloaded. Any modifications to this wiki with thoughts as to how it might be solved would
be much appreciated.

    #8 In the Solution Explorer, right-click on MQ2Main and choose "Set as Startup Project"
    #9 With MQ2Main selected in the Solution Explorer, go to Build - Build MQ2Main
    #10 Go to Build - Batch Build, click "Select All" and then "Build"

(Solution will have to do with one of the previous steps that was missed, or done incorrectly.)

### LINK : fatal error LNK1104: cannot open file '..\\Release\\MQ2Main.dll'

Because mq2main.dll is injected to exes, it can be held open by any process. The top three contenders are eqgame.exe,
macroquest2.exe, and wineq2.exe. You must stop these programs before you can write to mq2main.dll. Occasionally,
mq2main.dll stays injected to another app. You can use Process Explorer from
here to find the offending process and stop it.

### error C3068: : a 'naked' function cannot contain objects that would require unwinding if a C++ exception occurred

You shouldn't be here -- you didn't follow directions.

This is almost always caused by clicking macroquest2.dsw file instead of the MacroQuest2.sln when using Visual C++ 2005
Express Edition as their compiler.

You have the wrong compiler flags for your version of the compiler. Reread the instructions and open the correct file
and/or set the correct environment variables.

More info: google(error C3068) and look at the first link. Two of those things you can't do so you'll have to do the
third. Still don't know how? Tough shit.

If you are compiling using Visual C++ 2005 Express Edition, you may need to disable Exceptions for compiling older
versions of MQ2. Here are the instructions:

1\. Under the **Solution Explorer** right click **MQ2Main** and select **Properties**.

2\. Expand **Configuration Properties** if it isn't already expanded by clicking the **+** sign to the left of it. Then,
expand **C/C++** and select **Code Generation**.

3\. Last, look at the line on the right side of that window that says **Enable C++ Exceptions** and if it is set to
**Yes (/EHsc)**, click that dropdown box and select **No**, and then click **OK**.

4\. You can now run your compile like normal.

### error LNK2019: unresolved external symbol

If you see these symbols: \_\_imp\_\_CallNextHookEx@16, \_\_imp\_\_ShellExecuteA@24, \_\_imp\_\_MessageBoxA@16, you
didn't follow the directions. These symbols are resolved by libraries included by Microsoft's platform SDK, which you
already have installed if you got here. That means that you either screwed up the link compile step or the libraries are
not were the compiler thinks they are. Start again and follow the directions or try to trouble shoot your installation.

To find out what library file is not found try to google for the function name (if you are missing
\_\_imp\_\_CallNextHookEx@16 google for CallNextHookEx and you will find that the library file is User32.lib etc).

When linking fail it is most likely the information you supplied under Tools - Options - VC++ Directories - Library
Files that is wrong or have for some reason not taken effect.

### error PRJ0003: Error spawning 'cmd.exe'

If you get this error try opening up the cmd.exe file yourself prior to compiling.

### error C2360: initialization of 'i' is skipped by 'case' label

If you get this error, check to see if the file(s) that won't process correctly are featured in the Latest Release post
as a known issue. Otherwise, the error message should tell you what line the error occurs at as follows:

    C:\MQcompile\MQ2Main\MQ2DataTypes.cpp(7001) : error C2360: initialization of 'i' is skipped by 'case' label
    C:\MQcompile\MQ2Main\MQ2DataTypes.cpp(6996) : see declaration of 'i'

### When opening the SLN file in Visual Studio C++ 2010 or Visual Studio C++ 2010 SP 1, you receive a message "The project file 'name of dsp' cannot be loaded. Do you want to remove the unloadable project from the solution?The output window states " : error : Project upgrade failed.", lacking any obvious useful data.

There seems to be a known issue with 2010 opening 6.0 files directly. The workaround I found was to first open them in
2008. There may very well be other workarounds as well. 2008 is available
[here](http://www.microsoft.com/visualstudio/en-us/products/2008-editions/express/). There may very well be other, or
better workarounds- Please update this when you find them.


