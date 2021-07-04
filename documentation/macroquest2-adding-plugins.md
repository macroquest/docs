# MacroQuest2:Adding Plugins

* "C:\MQ2" will be used throughout this "how to" for the MQ2 directory. Substitute the actual directory on your

  system as you installed it for this.

* "MyPlugin" will also be used for the name of the plugin. Substitute with a name for the plugin.

## Visual Studio 6.0

Note: Visual Studio 6.0 is 7 years old and should NOT be used. Upgrade to Visual Studio .NET if at all possible

1. Run the Mkplugin.exe as follows Goto the **START** button and click on **RUN** and type in the window **C:\MQ2\mkplugin** **myplugin**. When you run this the files and directory created will be **MQ2Myplugin** e.g. Say you want to make a plugin using the code at this URL [MQ2BuffUtils Plugin](https://macroquest2.com/phpBB3/viewtopic.php?t=10616) the plugin name for this is **BuffUtils**; this is what you would replace **myplugin** with in the command line. After being running the command line \(**C:\MQ2\mkplugin BuffUtils**\) you will find that **MQ2BuffUtils** and related files have been created and placed in a like named Folder \(in this case **c:\MQ2\MQ2BuffUtils**\).

2. Open your compiler. **Files... Recent Workspaces... C:\MQ2\Macroquest2**.

3. **Project... Insert Project into Workspace**.

4. Select **MQ2Myplugin** Folder and double click on **Myplugin.dsp**; it will likely give you a message saying something about Myplugin.dsw, click "YES". Check to see that **Myplugin** shows up the **Class View window** and that the code shows up in the large window on the right.

5. In the project you just added, open **Myplugin.cpp** and replace everything with the code for the plugin you're adding.

6. **Build... Build MQ2Myplugin** Be sure that it says the name of the plugin you are adding, and not something else.

7. **Save Workspace and Exit out**.

Your plugin should now be ready to use, provided there were no serious errors that prevented it from working. To load it in game **/plugin** **MQ2Myplugin**

## Visual Studio .NET

