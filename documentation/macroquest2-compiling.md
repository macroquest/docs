# MacroQuest2:Compiling

## Overview

The easiest "1 click to build and be done solution" is to just use [http://www.macroquest2.com/builder](http://www.macroquest2.com/builder)

If you are going to compile "manually" set \#define LIVE to TEST in mq2main.h and follow the steps below: If you are going to build for LIVE, you will need to fix the structs for it first.

MacroQuest2 does not come pre-compiled, which means that you need to compile it in order to use it.

Quick start for MQ2:

1. Download & Install a C++ compiler
2. Download and [Unzip](http://www.7-zip.org/download.html) the source \( \[Link for Latest

   Source\]\([https://macroquest2.com/main.php?p=download](https://macroquest2.com/main.php?p=download)\) \)

3. Create MQ2Auth0.h
4. Compile MQ2 source
5. Run MQ2
6. Run Everquest

## Download & Install C++ compiler

[ Wiki page about Compilers](compilers.md)

Support for Compilers older than Visual Studio 2013 are phased out. Compile instructions for old compilers are kept below in case you need to compile a really old zip for legacy reasons...

VS2013 & VS2015 are completely free from Microsoft and commonly used.

* Option 1 : Download and install Visual Studio Community

  2015.

* Option 2 : Download and install Visual Studio Community

  2013.

## Download and Unzip the MQ2 Source

1. Download the latest MacroQuest2 source files from [here](https://macroquest2.com/main.php?p=download).
2. Unzip the source files to a directory of your choice, **making sure that subdirectories are retained**.

## Create MQ2Auth0.h

MQ2Auth is a form of protection to restrict the distribution of pre-compiled binaries.

It checks that MQ2 was complied with a list of computers you indicated MQ2 is allowed to run upon.

If you compile mq2 and it does not work on a specific computer it is because that computers hash identification was not included during the compile.

### How MQ2Auth0.h works

MQ2Auth0.h is required when you compile a binary of mq2.

When compiling mq2 a MQ2Auth0.h **MUST** be in your .\MQ2Main folder and it **MUST** contain a hash for **EVERY** computer you plan to run the compiled binary on.

Recap.... you must have .\MQ2Main\MQ2Auth0.h with your computer\(s\) hash codes in it!

Each computer is 2 lines in MQ2Auth0.h

### How MQ2Auth.exe works

MQ2Auth.exe is included in every zip download of source and it creates a hash of the computer it was run on and inserts that hash into MQ2Auth0.h

You need to run MQ2Auth.exe as administrator.

If you run MQ2Auth.exe and there is a MQ2Main folder in the folder where MQ2Auth.exe was run it will create MQ2Auth0.h in MQ2Main \(.\MQ2Main\MQ2Auth0.h\)

If you run MQ2Auth.exe and there is no MQ2Main folder in the folder MQ2Auth.exe was run it will create MQ2Auth0.h where it was run \(.\MQ2Auth0.h\)

Generally MQ2Auth.exe will append another 2 lines to the end of MQ2Auth0.h for new computers

### Compiling with MQ2Auth for 1 computer

Open the folder you extracted the source files on the computer you will run mq2 and compile mq2 on, then run MQ2Auth.exe as administrator.

This will automatically create the MQ2Auth0.h file in the MQ2Main directory \(.\MQ2Main\MQ2Auth0.h\).

### Compiling with MQ2Auth for multiple computers or for friends computers

If you are compiling for someone else, you must get their computer hash from their MQ2Auth0.h file and add it to your .\MQ2Main\MQ2Auth0.h file.

You can ask them to download the MQ2 source, extract just the MQ2Auth.exe file and run it.

It will create the MQ2Auth0.h file in the same folder it is run.

They should then send that file to you or send you the text from that file so you can add it to your .\MQ2Main\MQ2AUth0.h

You can add comments to the end of each line if required, for example:

`MQ2AUTH(KkIRzfsLfkcViSKKbFCLPrxJssu); // Computer1`  
`MQ2AUTH(ZRCmvQxmFDmZulHeCBwHsoGxisc); // Computer1`  
`MQ2AUTH(VH_ThwYG_KbCWRVAWDzTayIPCRS); // Computer2`  
`MQ2AUTH(EaQEdgNNAcQWCxYVYVVzARBDERw); // Computer2`  
`MQ2AUTH(pXfpGxHTMSHw_CSFTnuEFAbqZhr); // Computer3`  
`MQ2AUTH(GLpOCyCpmkxIWqkuXpEOgTTQihF); // Computer3`  
`MQ2AUTH(LFlYfuraYsIHoUBpElTCllRZwET); // Computer4`  
`MQ2AUTH(_tboUtEhOFwvsfUKaSJEqo_NqEk); // Computer4`

or add comments like so

`// my computer`  
`MQ2AUTH(YnRfLsTqRiRuV_YVXrt_Suido_Z);`  
`MQ2AUTH(mUagPMfSqQaTotVpTYYrqbrnm_u);`  
`// my other computer`  
`MQ2AUTH(arleLHCoRICQUhgFEzJPAKXMdYw);`  
`MQ2AUTH(MfvDHmxLXaObvWzucfnDHcOlnYe);`  
`// Bob's computer 1`  
`MQ2AUTH(cStosrJIZCzkxxQaGjXuhvzXXnt);`  
`MQ2AUTH(tlnNECUePppwJRxQfQRiEOGaRnb);`  
`// Bob's computer 2`  
`MQ2AUTH(okmRVfXLKkyVESoKGFYLtrbJOsQ);`  
`MQ2AUTH(DRgmRQbmjDIZQllegBSHXokxEsy);`  
`// John's computer`  
`MQ2AUTH(WjaYVZgaiXbHzyqptQICwQGZQiI);`  
`MQ2AUTH(kYRoJYthZjlvDKnKlwyEBTPNKi_);`  
`// Sue's computer`  
`MQ2AUTH(CWGFhFeWngQUBhXfJpjVGSFUGbh);`  
`MQ2AUTH(lhQatoUxxyEYxW_AkltRzkydMbQ);`

## Compile the Source

### Choose LIVE/BETA/TEST Compile

1. By default the zip compiles for LIVE
2. Compile for Beta = Modify MQ2Main\mq2main.h , search for "\#define LIVE" and change it to "\#define BETA"
3. Compile for Test = Modify MQ2Main\mq2main.h , search for "\#define LIVE" and change it to "\#define TEST"

### Visual Studio Community 2013 & 2015

1. Browse to the folder you extracted the source to and open MacroQuest2.sln alternative start visual studio and browse

   to it.

2. If you are using VS 2015 you will be asked to upgrade to toolset, you can click OK.
3. Did you run mq2auth.exe as admin?
4. If you did, Go to the Build menu and select Build Solution and wait for build to finish
5. now do that again.
6. and again.
7. and one more time for good measure. The reason we repeat this is that we want to be absolutely sure every single dll

   will be built.

8. you should see 0 warnings and 0 errors now and it's all built and ready to go.

### Compiling from the command line

1. This might no longer work, but if you actually compile from the command line, you would know how to make it work.
2. Open a command prompt \(Start-&gt;Run-&gt;cmd\)
3. Find the bat file that sets the environment for your VC installation. This will be vcX\bin\vcvars32.bat for most

   installation, where X is 98, 7, 8, 9, 10, 11, 12, or 14 depending on which version you have.

4. Run that bat file from the cmd window by typing in the path to it.
5. In the cmd window, cd 
6. In the cmd window, nmake clean all
   * If you get a "Cannot determine compiler version." error, type "set COMPILER=8" in the cmd window.
   * **Note:** to add plugins, add them to the extra.mak file in the following format:

`DIRECTORIES= MQ2Clickies mq2eqbc mq2fps mq2moveutils`

## Run MQ2

Once compiled, the relevant files will be placed in the _\Release_ subdirectory. Run MacroQuest2.exe as admin

## Troubleshooting

See [here](help-compiling.md) for Help and Troubleshooting of the compile process.

## Unsupported older c++ compiler information

### Visual C++ 6.0 \(**NO LONGER SUPPORTED**\)

After installation of Visual C++ 6.0, install Service Pack 6 from [here](http://www.microsoft.com/downloads/details.aspx?FamilyID=a8494edb-2e89-4676-a16a-5c5477cb9713&DisplayLang=en).

### Visual C++ 2003 \(**NO LONGER SUPPORTED**\)

No additional service packs are needed if you have Visual C++ 2003 installed.

### Visual C++ 2005 Express \(**NO LONGER SUPPORTED**\)

1. Download the Setup program [here](http://go.microsoft.com/fwlink/?LinkId=51410&clcid=0x409) and install it.
2. Download SDK files and install them:
   1. If you are using **XP** or **Vista 32-bit**, download the Microsoft Platform SDK from

      [here](http://www.microsoft.com/downloads/info.aspx?na=46&p=3&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=A55B6B43-E24F-4EA3-A93E-40C0EC4F68E5&u=http%3a%2f%2fdownload.microsoft.com%2fdownload%2fa%2f5%2ff%2fa5f0d781-e201-4ab6-8c6a-9bb4efed1e1a%2fPSDK-x86.exe&oRef=http%3a%2f%2fmsdn.microsoft.com%2fwindowsmedia%2fdownloads%2fdefault.aspx).

   2. If you are using **Vista 64-bit** download the Windows SDK

      [here](http://www.microsoft.com/downloads/details.aspx?FamilyId=E6E1C3DF-A74F-4207-8586-711EBE331CDC&displaylang=en).
3. Open Visual Studio 2005 Express.
4. From the Tools drop down menu, select Options...
5. Expand the "Projects and Solutions" tree and select "VC++ Directories"
6. In the right window from the "Show Directories for" drop down menu select the following items and add the paths

   below:

   1. _Executable files:_
      * **C:\Program Files\Microsoft Platform SDK\Bin** for 32-bit
      * **C:\Program Files\Microsoft SDKs\Windows\v6.1\Bin** for 64-bit
   2. _Include files:_
      * **C:\Program Files\Microsoft Platform SDK\include** for 32-bit
      * **C:\Program Files\Microsoft SDKs\Windows\v6.1\Include** for 64-bit
   3. _Library files:_
      * **C:\Program Files\Microsoft Platform SDK\lib** for 32-bit
      * **C:\Program Files\Microsoft SDKs\Windows\v6.1\Lib** for 64-bit

7. Make sure the directories you just entered are at the top of the list. If not, use the Up or Down arrows to put them

   in the correct order.

8. If you installed using default directories, navigate to C:\Program Files\Microsoft Visual Studio

   8\VC\VCProjectDefaults and edit **corewin\_express.vsprops**:

   * Change **AdditionalDependencies="kernel32.lib"** to \*\*AdditionalDependencies="kernel32.lib user32.lib gdi32.lib

     winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib"\*\*

9. Navigate to C:\Program Files\Microsoft Visual Studio 8\VC\VCWizards\AppWiz\Generic\Application\html\1033\

   and edit AppSettings.htm, commenting out lines 441-444 like this:

`// WIN_APP.disabled = true;`  
`// WIN_APP_LABEL.disabled = true;`  
`// DLL_APP.disabled = true;`  
`// DLL_APP_LABEL.disabled = true;`

### Visual C++ 2008 Express \(**NO LONGER SUPPORTED**\)

Download Visual C++ 2008 Express Edition from [here](http://www.microsoft.com/visualstudio/en-us/products/2008-editions/express/) and install it.

### Visual C++ 2010 Express \(**NO LONGER SUPPORTED**\)

Download and install Visual C++ 2010 Express Edition from [here](http://go.microsoft.com/?linkid=9709949).

### Visual Studio Express 2012 \(**NO LONGER SUPPORTED**\)

Download and install Visual Studio Express 2012 for Windows Desktop from [here](http://go.microsoft.com/?linkid=9816758).

### Visual C++ 6.0 **NO LONGER SUPPORTED**

1. Browse to the folder you extracted the source to and open macroquest2.dsw
2. Select Build -&gt; Set Active Config and select MQ2main. Click OK
3. Select Build -&gt; Build MQ2main.dll
4. Select Build -&gt; Batch Build. Make sure everything in the batch build window that says release has a check next to it
5. Click the Build button

### Visual C++ 2003 **NO LONGER SUPPORTED**

1. Browse to the folder you extracted the source to and open MacroQuest2.sln
2. If asked to update the code for the current version of .NET, do so
3. Go to Build -&gt; Configuration Manager
4. Select Release, and place a check in each dll you want compiled
5. Go to Build --&gt; Build Solution

### Visual C++ 2005/2008 Express **NO LONGER SUPPORTED**

1. Browse to the folder you extracted the source to and open MacroQuest2.sln
2. If asked to update the code for the current version of .NET, do so
3. Go to Build -&gt; Configuration Manager
4. Select Release, and place a check in each dll you want compiled
5. In the Solution Explorer, right-click on MQ2Main and choose "Set as Startup Project"
6. With MQ2Main selected in the Solution Explorer, go to Build -&gt; Build MQ2Main
7. Go to Build -&gt; Batch Build, click "Select All" and then "Build"

### Visual C++ 2010 Express **NO LONGER SUPPORTED**

1. Browse to the folder you extracted the source to and open MacroQuest2.sln
2. If asked to update the code for the current version of .NET, do so
3. Select the MacroQuest2 solution in the Solution Explorer window
4. Go to Project -&gt; Properties
5. On the left, choose Configuration Properties -&gt; Configuration
6. In the Build column, place a check next to each dll you want compiled
7. In the Solution Explorer, right-click on MQ2Main and choose "Set as Startup Project"
8. Right-click on MQ2Main and choose Build
9. Right-click on Solution 'MacroQuest2' and choose Batch Build
10. Click Select All and then Build

