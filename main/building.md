# Building MacroQuest

## Download & Install Visual Studio 2019/2022

Links and instructions can be found at:
[https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

## How to Build

### Download & Install Git for Windows

Links and instructions can be found at:
[https://git-scm.com](https://git-scm.com/downloads)

The recommended way to build MacroQuest is from a source code checkout using Git. There are many how to guides for installing and setting up git. [Here is one of them](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)

### Check Out the Latest Source Code

Clone (create a local copy) the repository. This will create the subfolder `macroquest` that containes a copy of the source code.

```
git clone git@github.com:macroquest/macroquest.git
```

Initialize the submodules. Move (cd) to the newly created `macroquest` folder before executing this command. If you have run this step before, you can skip it.

```
git submodule init
```

Update the submodules to the newest versions. Ensure you are in the newly created `macroquest` folder before executing this command.

```
git submodule update
```

If this is your first time downloading the source code, proceed to Build Steps.


### Updating an Existing Checkout

MacroQuest is updated often, especially after a patch. Make sure before you build that you have the latest source code for MacroQuest and all of its dependencies.

If you already have the source, it is a good idea to make sure that you pull all the latest changes.

```
git pull --rebase
```

Update Submodules. This ensures that dependencies have the latest code.

```
git submodule update
```

At this point, the source should be ready to compile. Proceed to Build Steps.

### Build Steps

1. Open the `MacroQuest.sln` file in the `src` directory. Double clicking this file should open Visual Studio 2019.
2. Select the `Release` and `(x64)`configuration from the drop-down menu near the top of the window.
3. Since the project moved to 64-bit, ensure all project configurations are set to `(x64)` in the **Solution Macroquest** Property Pages. From the Visual Studio main menu, select **Build** then **Configuration Manager** then ensure the Platform column for each project is set to `(x64)`.
4. Select `Build -> Build Solution` from the menu

The built files will be placed in `build/bin/Release`. To start MacroQuest, run `MacroQuest.exe`. This will launch the application to the tray, and install MacroQuest into any running EverQuest processes.

### Adding Your Own Plugins

Note: If you have any custom plugins you want to build, put the sources for them in the `plugins` folder, for example: `plugins/MQ2Foo/MQ2Foo.cpp` Do not put them in `src/plugins` this path is reserved for the MacroQuest developers.

To add any personal plugins to the solution:

1. Right-click the solution in the Solution Explorer and click `Add -> Add Existing Project...`&#x20;
2. Select your `.vcxproj`file
3. Repeat as necessary

### Updating Plugins from Legacy MacroQuest

If you are converting plugins over from Legacy MacroQuest (e.g. MQ2), it is recommended that you re-run the plugin generator first, and then copy your source files into the generated project.

For example:

```bash
cd plugins
mkplugin MQ2Foo
```

This will generate a `MQ2Foo.vcxproj`, `MQ2Foo.cpp` and several other files in a MQ2Foo folder. You can now add this project to the solution and add/replace the sources with your own.

### Directory Structure

| Folder Name | Purpose                                                                                                                    |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| build       | Build artifacts. This is where you can find the output when you compile MacroQuest and your plugins.                       |
| contrib     | Third-Party source code.                                                                                                   |
| data        | Additional non-source code files used by MacroQuest.                                                                       |
| docs        | Documentation                                                                                                              |
| extras      | Optional files that are not required, but may be useful. This includes sources for plugins that are no longer maintained.  |
| include     | Public header files that are used for building MacroQuest and plugins.                                                     |
| plugins     | This folder is reserved for you to add your own personal plugins.                                                          |
| src         | The source code for the MacroQuest executable and its core plugins.                                                        |
| tools       | Source code and additional tools that are used for MacroQuest development, but not part of the main project.               |

### Additional Files of Interest

`plugins/mkplugin.exe` Generates a new plugin from the template. Use this when creating a new plugin, or when converting an existing plugin from legacy MacroQuest.

`src/MacroQuest.sln`  The main MacroQuest solution file. Use this to build the project.
