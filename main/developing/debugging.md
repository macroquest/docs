# Crash To Desktop

!!! warning

    this information is obsolete and needs to be revised!

## Necessary Information

1. We need to know the actual error. The address, the address that was probably trying to be read, etc. Copy and paste from the debugger.
2. We need to know if the crash itself was in EVERQUEST, or MACROQUEST. If it was in MacroQuest, the debugger will show you the source line. If not, it will show you some disassembly and an offset in eqgame.exe (most likely).
3. a. Inside MacroQuest - The error information from \#1 as well as the source line that caused the crash. If you can, copy and paste us the surrounding code block and let us know which source file it was in (e.g. MQ2Utilities.cpp)
4. b. Inside EverQuest - The error information \#1 including the offset in eqgame.exe, copy and paste a couple lines of the disassembly if you can, AND GET THE FUNCTION CALL STACK. If we get the function call stack, it may be VERY easy to fix the problem. If not, may be very DIFFICULT to fix the problem.

**If you cannot get this information, you might as well not report the bug.**

## Debuggers

Stuff you need to know about debuggers:

1. How to attach a debugger to the process, and how to enable trapping of the 0xC0000005 exception (the majority of crash bugs)
2. Where to find the debug spew as well as crash information (for info \#1) when eqgame.exe crashes
3. Where to find the source line (for info \#2a only) when eqgame crashes inside macroquest
4. Where to find the disassembly (for info \#2b only) when eqgame crashes
5. Where to find the function call stack (for info \#2b only) when eqgame crashes

### Visual Studio .Net

1. Debug menu-&gt;Processes option. In the "Available Processes" list select eqgame.exe. Click "Attach". In the "Attach to Process" box that pops up, select only "Native" in the list. Hit OK. The popup closes and the debugger attaches; click "Close" in the processes window. To enable trapping of the 0xC0000005 exception, open Debug-&gt;Exceptions (alternatively ctrl+alt+E). Expand "Win32 Exceptions". Select "c0000005 Access violation". Select the two "Break into the debugger" options. Hit OK.
2. Debug spew can be found in the "Output window" by hitting ctrl+alt+O, or by going View-&gt;Other Windows-&gt;Output. The crash information will be displayed there when eqgame crashes.
3. VS.NET will automatically point to the source file and put a green arrow by the source line that caused the problem, assuming macroquest was compiled on the computer you are running this on.
4. If the disassembly does not show up, you can switch to the disassembly window by hitting alt+8 or by going debug-&gt;windows-&gt;disassembly
5. The function call stack can be found in the toolbar that contains "Program", "Thread" and "Stack Frame". The call stack will be seen in the "stack frame" combo box. Pull it down and take note of the top few if not the entire list.

### Visual Studio 6

1. Build menu-&gt;Start Debug-&gt;Attach to process... Check the "Show System Processes" button. Select "eqgame" in the list. Hit OK. The c0000005 exception trapping can be enabled by going Debug-&gt;Exceptions. Select c0000005 Access violation.

   Click "Stop always". Hit "Change". Hit "OK.

2. Debug spew can be found in the "Output window" by hitting alt+2, or by going View-&gt;Output. The crash information will be displayed there when eqgame crashes.
3. VS6 should automatically point to the source file and put a green arrow by the source line that caused the problem, assuming MacroQuest was compiled on the computer you are running this on.
4. If the disassembly does not show up, you can switch to the disassembly window by hitting alt+8 or by going View-&gt;Debug Windows-&gt;Disassembly
5. The function call stack can be found in the "Call Stack" window, found by pressing alt+7 or by going View-&gt;Debug Windows-&gt;Call Stack

### WINDBG

1. Build MQ2 (nmake or VS are both fine)
2. Make sure that the PDB files created have the same date as DLLs
3. Download windbg ([http://www.microsoft.com/whdc/devtools/debugging/installx86.mspx\#a](http://www.microsoft.com/whdc/devtools/debugging/installx86.mspx#a)) and install it
4. Make sure that the PDB files are in the same directory as where you start MQ.
5. Start MQ, EQ, and windbg. (wineq or eqw will work too)
6. On windbg, press F6 and choose eqgame.exe. Once it has broken in, press F5 to continue. If you don't press F5

   quickly enough (a few seconds or so), there is a chance that you will be disconnected. This is because the game is

   stopped while you are in the debugger and it is not responding to the server.

7. In EQ, take the steps that normally crash.
8. When the debugger breaks in, goto to the command window of windbg
   * Enter this command: .sympath SRV\*c:\winnt\symbols\*[http://msdl.microsoft.com/download/symbols](http://msdl.microsoft.com/download/symbols)
   * or Enter this command: !symfix
9. Enter the command 'r' for registers.
10. Enter the command 'kv' for stack backtrace.
11. If the crash is in MQ code, you should see the source file open and show the line that caused the problem (if you compiled it on the same machine as you are running on). Alt-3 brings up the local variables. See if there is anything of interest there.
12. Post the output from those commands here: [http://www.macroquest2.com/phpBB3/viewforum.php?f=28](http://www.macroquest2.com/phpBB3/viewforum.php?f=28).

### Visual Studio 2005 Express

1. Tools-&gt;Attach to Process-&gt;Select instance of EQ to debug and click 'Attach" Should automatically detect "Native Code". Debug-&gt;Exceptions expand the "Win 32 Exceptions" tree and select "c0000005 Access violation" and hit ok.
2. When eqgame crashes the debug spew is in the output window usually in the upper right window, but can be foiund by Debug-&gt;Windows-&gt;Output.
3. When EQ crashes VS2005 will popup a box with "break", "ignore", or "continue" to choose from. Select "Break" or all your debug information will be wiped out. It should then open up the source file and place an error next to the line it crashed at.
4. Dissasembly can be found at alt+8, or Debug-&gt;Windows-&gt;Dissasembly.
5. Call stack may pop up on its own in lower window as a tab, but if not alt+7 or debug-&gt;windows-&gt;Call Stack

