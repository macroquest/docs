# CMake Build System Quickstart Guide

This guide explains how to use the CMake build system for MacroQuest, including the `gen_solution.ps1` helper script, direct CMake commands, and IDE setup.

## Table of Contents

- [Why CMake?](#why-cmake)
- [Quick Start with gen_solution.ps1](#quick-start-with-gen_solutionps1)
- [Direct CMake Usage](#direct-cmake-usage)
- [CLion Setup](#clion-setup)
- [Custom Plugin Management](#custom-plugin-management)
- [Troubleshooting](#troubleshooting)

---

## Why CMake?

### The Problem: Upstream Solution File Changes

The MacroQuest project previously relied on a hand-maintained Visual Studio solution (`.sln`) file. This approach had several challenges:

1. **Merge Conflicts**: When upstream changes the solution file structure (adding/removing projects, changing configurations, reorganizing folders), downstream users experienced frequent build issues.

2. **Custom Plugin Integration**: Users with custom plugins had to manually add their projects to the solution, and these changes would conflict with upstream updates.

3. **Platform-Specific Issues**: The solution file contained both Win32 and x64 configurations, leading to confusion and accidental builds for the wrong architecture.

4. **Build Configuration Drift**: Different developers might have different project settings, leading to inconsistent builds.

### The Solution: CMake as the Source of Truth

CMake provides a **declarative, text-based build system** that solves these problems:

- **Generated Solution File**: The `.sln` file is now a **generated artifact**, not a source file. You can safely delete and regenerate it at any time.

- **Architecture Auto-Detection**: CMake automatically detects the target architecture from `MQ_EXPANSION_LEVEL` in `BuildType.h`, generating a single-platform solution (Win32 OR x64, not both).

- **Conflict-Free Upstream Updates**: When upstream changes the CMake configuration, you simply re-run the generation script. No manual merge required.

- **Custom Plugin Flexibility**: Add custom plugins by placing them in `plugins/` directory or using a custom plugin list file. They integrate seamlessly without modifying tracked files.

- **Cross-IDE Support**: The same CMake configuration works with Visual Studio, CLion, Visual Studio Code, and command-line builds.

### Dual Build System

MacroQuest supports **two build systems** during the transition period:

1. **CMake** (recommended) - `gen_solution.ps1` generates `build/MacroQuest.sln`
2. **Legacy Visual Studio** - Hand-maintained `src/MacroQuest.sln`

The CMake build is recommended for all new development and could potentially become the only supported build method.

---

## Quick Start with gen_solution.ps1

The `gen_solution.ps1` PowerShell script provides a convenient wrapper around CMake with sensible defaults and automatic platform detection.

### Prerequisites

- **Git** - For submodule management
- **CMake 3.20+** - Build system generator
- **Visual Studio 2022** - C++ compiler and toolchain
- **PowerShell 5.1+** - Script execution (included with Windows)

### Basic Usage

```powershell
# First-time setup (initializes submodules, generates solution)
.\gen_solution.ps1

# Reconfigure after pulling upstream changes
.\gen_solution.ps1

# Clean cmake generated files and regenerate (not built binaries)
.\gen_solution.ps1 -Clean
.\gen_solution.ps1
```

### Generated Output

```
build/
  solution/          # CMake cache and generated project files
    MacroQuest.sln   # Full solution (includes CMake internal projects)
    CMakeCache.txt   # CMake configuration cache
    vcpkg_manifests/ # Combined vcpkg manifest files from all included projects
  MacroQuest.sln     # Cleaned solution (recommended - no CMake clutter)
  bin/               # Build output (after compilation, same as legacy output)
    debug/
    release/
```

**Recommendation**: Open `build/MacroQuest.sln` in Visual Studio (the cleaned version in the build root, not the one in `build/solution/`).

### Common Options

```powershell
# View all available options
.\gen_solution.ps1 -Help

# Skip dependency installation (faster reconfiguration)
.\gen_solution.ps1 -SkipVcpkg

# Don't build custom plugins from plugins/ directory
.\gen_solution.ps1 -SkipCustom

# Don't build core MQ plugins (chat, lua, map, etc.)
.\gen_solution.ps1 -SkipPlugins

# Build without the MacroQuest.exe loader
.\gen_solution.ps1 -SkipLauncher

# Include test projects
.\gen_solution.ps1 -BuildTest

# Verbose output (show detailed CMake messages)
.\gen_solution.ps1 -Verbose

# Sync submodules to latest remote commits
.\gen_solution.ps1 -SyncSubmodules
```

### Architecture Detection

The script **automatically detects** the target architecture from this line in `src/eqlib/include/eqlib/BuildType.h`:

```cpp
#define MQ_EXPANSION_LEVEL EXPANSION_LEVEL_TOB  // x64
// or
#define MQ_EXPANSION_LEVEL EXPANSION_LEVEL_ROF  // Win32
```

- **EXPANSION_LEVEL_ROF** → Generates Win32 (32-bit) solution
- **All other expansion levels** → Generates x64 (64-bit) solution

To switch architectures:
1. Edit `BuildType.h` and change `MQ_EXPANSION_LEVEL` (usually by pulling the emu eqlib branch)
2. Run `.\gen_solution.ps1` (automatically detects change and cleans build directory)

### Custom Plugin Management

**Auto-detection (default):**
```powershell
# Automatically includes all plugins in plugins/*/
.\gen_solution.ps1
```

**Generate a plugin configuration file:**
```powershell
# Scan plugins/ and write detected plugins to a file
.\gen_solution.ps1 -WritePluginsFile my_plugins.cmake.custom
```

This creates `my_plugins.cmake.custom` (anything with a .custom postfix is ignored by git) with contents like:
```cmake
# Auto-generated plugin configuration file
# Generated by plugins.cmake
# Platform: x64
# Toolset: v143

add_custom_vcxproj("plugins/MQ2Nav" "MQ2Nav" "external")
add_subdirectory("C:/dev/MyCustomPlugin")
```

**Use a custom plugin list:**
```powershell
# Override auto-detection with a custom file
.\gen_solution.ps1 -CustomPluginsFile my_plugins.cmake.custom
```

This allows you to:
- Maintain a specific set of plugins across reconfigures
- Check in a team plugin list to version control
- Easily switch between different plugin sets

**Add MQ2Main dependency to custom plugins:**
```powershell
# Automatically modify .vcxproj files to add MQ2Main dependency
.\gen_solution.ps1 -AddMQ2MainDependency
```

This is useful because build order in cmake is controlled entirely within the project files, so the need to be modified
in order to build from command line (outside Visual Studio) correctly. This is required if you want to use a different
development environment.

---

## Direct CMake Usage

For advanced users or CI/CD pipelines, you can use CMake directly without the PowerShell script.

### Initial Setup

```powershell
# Initialize submodules
git submodule update --init --recursive

# Generate x64 solution
cmake -B build -G "Visual Studio 17 2022" -A x64

# Generate Win32 solution
cmake -B build -G "Visual Studio 17 2022" -A Win32
```

### CMake Options

All options are prefixed with `MQ_`:

```powershell
# Disable vcpkg dependency management
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_BUILD_VCPKG=OFF

# Don't build custom plugins
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_BUILD_CUSTOM_PLUGINS=OFF

# Don't build core plugins
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_BUILD_PLUGINS=OFF

# Don't build launcher
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_BUILD_LOADER=OFF

# Enable test projects
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_BUILD_TESTS=ON

# Add MQ2Main dependency to custom plugins
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_ADD_MQ2MAIN_DEPENDENCY=ON

# Use custom plugin list file
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_CUSTOM_PLUGINS_FILE=my_plugins.cmake.custom

# Write detected plugins to file
cmake -B build -G "Visual Studio 17 2022" -A x64 -DMQ_WRITE_PLUGINS_FILE=my_plugins.cmake.custom
```

### Reconfiguration

```powershell
# Reconfigure (keeps cache, updates changed files)
cmake -B build

# Fresh reconfiguration (clears cache)
cmake -B build --fresh

# Clean and reconfigure
Remove-Item -Recurse -Force build
cmake -B build -G "Visual Studio 17 2022" -A x64
```

### Building from Command Line

```powershell
# Build entire solution (Release)
cmake --build build --config Release

# Build specific target
cmake --build build --config Release --target MQ2Main

# Build with multiple cores
cmake --build build --config Release -j 8

# Build Debug configuration
cmake --build build --config Debug
```

### CMake Variables Reference

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `MQ_BUILD_VCPKG` | BOOL | ON | Install dependencies via vcpkg |
| `MQ_BUILD_PLUGINS` | BOOL | ON | Build core MQ plugins |
| `MQ_BUILD_CUSTOM_PLUGINS` | BOOL | ON | Build plugins from plugins/ directory |
| `MQ_BUILD_LOADER` | BOOL | ON | Build MacroQuest.exe loader |
| `MQ_BUILD_TESTS` | BOOL | OFF | Build test projects |
| `MQ_ADD_MQ2MAIN_DEPENDENCY` | BOOL | OFF | Auto-add MQ2Main to custom vcxproj files |
| `MQ_CUSTOM_PLUGINS_FILE` | FILEPATH | "" | Path to custom plugin CMake file |
| `MQ_WRITE_PLUGINS_FILE` | FILEPATH | "" | Path to write plugin configuration |

---

## CLion Setup

JetBrains CLion is a cross-platform IDE with excellent CMake support. Here's how to set up MacroQuest in CLion.

### Step 1: Install Prerequisites

1. **Install Visual Studio 2022** with C++ desktop development workload (CLion uses MSVC compiler)
2. **Install CLion** from https://www.jetbrains.com/clion/
3. **Install Git** and initialize submodules:
   ```powershell
   git submodule update --init --recursive
   ```

### Step 2: Open Project in CLion

1. **Launch CLion**
2. **File → Open** → Select the `macroquest` directory (the one containing `CMakeLists.txt`)
3. Open CMakeLists.txt to create a cmake project
4. CLion will automatically detect all included projects

### Step 3: Configure CMake Settings

CLion will open the **CMake tool window** at the bottom. Configure the build:

1. **File → Settings → Build, Execution, Deployment → CMake**

2. **Add Configuration Profiles** (or modify existing):

   **Debug Profile:**
   - Name: `Debug`
   - Build type: `Debug`
   - Toolchain: `Visual Studio`
   - Generator: `Let CMake decide`
   - Build options: as above, `-j` is suggested
   - Build directory: `build/solution`

   **Release Profile:**
   - Name: `Release`
   - Build type: `Release`
   - Toolchain: `Visual Studio`
   - Generator: `Let CMake decide`
   - Build options: as above, `-j` is suggested
   - Build directory: `build/solution`

3. **Add CMake Options** (optional):
   ```
   -DMQ_BUILD_TESTS=ON
   ```

4. Click **Apply** and **OK**

### Step 4: Let CLion Generate Project

1. CLion will automatically run CMake configuration
2. Wait for "CMake project loaded" message in the CMake tool window
3. You should see all targets in the **Run/Debug Configurations** dropdown

### Step 5: Configure Build Targets

In the **Run/Debug Configurations** dropdown (top-right):

- **All targets** - Builds everything (like ALL_BUILD)
- **MQ2Main** - Builds only the core DLL
- **MQ2Chat** - Builds the chat plugin
- **MacroQuest** - Builds the loader executable
- *(Your custom plugins will also appear here)*

Select a target and click the **Build** (hammer) icon to compile.

### Step 6: Configure Debugging (Optional)

To debug MacroQuest in CLion:

1. **Run → Edit Configurations**
2. Click **+** → **CMake Application**
3. Configure:
   - **Name**: `eqgame` (whatever you want here)
   - **Target**: `All targets` (this will rebuild everything, can choose a single target if only changing one)
   - **Executable**: `eqgame.exe` (select your EQ install path)
   - **Program arguments**: `patchme`
4. Click **OK**

Attach the debugger by running this configuration.

### Step 7: Working with the Project

**Building:**
- **Build → Build Project** (Ctrl+F9) - Builds current configuration
- **Build → Rebuild Project** - Clean build

**CMake Reload:**
- **Tools → CMake → Reload CMake Project** - Refresh after editing CMakeLists.txt
- **Tools → CMake → Reset Cache and Reload Project** - Clean CMake cache

**Finding Files:**
- **Navigate → File** (Ctrl+Shift+N) - Fast file search
- **Navigate → Class** (Ctrl+N) - Search for classes
- **Navigate → Symbol** (Ctrl+Alt+Shift+N) - Search for functions

**Code Navigation:**
- **Ctrl+Click** on symbol - Go to definition
- **Ctrl+Alt+B** - Go to implementation
- **Alt+F7** - Find usages
- **Ctrl+F12** - File structure

### CLion Tips

**Performance Optimization:**
- Exclude build directories from indexing:
  - **Right-click `build/` folder** → **Mark Directory as** → **Excluded**

**Custom Plugin Development:**
- Place your plugin in `plugins/MQ2YourPlugin/`
- Add source files
- Reload CMake project
- Your plugin appears as a build target automatically

**Switching Architectures:**
1. Edit/Pull `src/eqlib/include/eqlib/BuildType.h`
2. Change `MQ_EXPANSION_LEVEL`
3. **Tools → CMake → Reset Cache and Reload Project**

---

## Custom Plugin Management

### Auto-Discovery Method

The simplest way to add custom plugins:

1. **Create plugin directory:**
   ```
   plugins/MQ2YourPlugin/
   ```

2. **Add source files:**
   ```
   plugins/MQ2YourPlugin/
     ├── MQ2YourPlugin.cpp
     ├── MQ2YourPlugin.h
     ├── (optional) MQ2YourPlugin.vcxproj
     └── (optional) CMakeLists.txt
   ```

3. **Regenerate solution:**
   ```powershell
   .\gen_solution.ps1
   ```

Your plugin is automatically detected and added to the solution.

### CMakeLists.txt Method

For advanced plugin configuration, create `plugins/MQ2YourPlugin/CMakeLists.txt`:

```cmake
# Collect source files
file(GLOB_RECURSE SOURCES "*.cpp" "*.c")
file(GLOB_RECURSE HEADERS "*.h")

# Create plugin library
add_library(MQ2YourPlugin MODULE ${SOURCES} ${HEADERS})

# Link against MQ2Main
target_link_libraries(MQ2YourPlugin PRIVATE MQ2Main fmt::fmt)

# Set output directory
set_target_properties(MQ2YourPlugin PROPERTIES
    FOLDER "CustomPlugins"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/${CONFIG}/plugins"
)
```

### .vcxproj Method

If you have an existing `.vcxproj` file:

1. **Place .vcxproj in plugin directory:**
   ```
   plugins/MQ2YourPlugin/MQ2YourPlugin.vcxproj
   ```

2. **Ensure platform/toolset compatibility:**
   - Platform: Must match (x64 or Win32)
   - Toolset: Must be `v143` (Visual Studio 2022)

3. **Regenerate solution:**
   ```powershell
   .\gen_solution.ps1
   ```

4. **Optionally add MQ2Main dependency:**
   ```powershell
   .\gen_solution.ps1 -AddMQ2MainDependency
   ```

### Custom Plugin List Method

For precise control over which plugins are included:

1. **Generate initial plugin list:**
   ```powershell
   .\gen_solution.ps1 -WritePluginsFile my_plugins.cmake.custom
   ```

2. **Edit `my_plugins.cmake.custom`:**
   ```cmake
   # Custom plugin configuration

   # CMake-based plugin
   add_subdirectory("C:/dev/MyPlugin1")

   # vcxproj-based plugin
   add_custom_vcxproj("plugins/MQ2Legacy" "MQ2Legacy" "external")

   # External plugin from different location
   add_custom_vcxproj("D:/projects/MQ2Special" "MQ2Special" "external")
   ```

3. **Use the custom list:**
   ```powershell
   .\gen_solution.ps1 -CustomPluginsFile my_plugins.cmake.custom
   ```

4. **Check in to version control (optional):**
   ```
   # Team plugin configuration
   git add my_plugins.cmake
   git commit -m "Add team plugin list"
   ```

---

## Troubleshooting

### "CMake is not installed"

**Problem**: Script fails with "CMake is not installed or not in PATH"

**Solution**:
1. Install CMake from https://cmake.org/download/
2. During installation, select "Add CMake to system PATH"
3. Or manually add to PATH: `C:\Program Files\CMake\bin`

### "Git is not installed"

**Problem**: Script fails with "Git is not installed or not in PATH"

**Solution**:
1. Install Git from https://git-scm.com/
2. Restart PowerShell
3. Verify: `git --version`

### "Submodule is empty"

**Problem**: `src/eqlib` or `contrib/vcpkg` directories are empty

**Solution**:
```powershell
.\gen_solution.ps1 -SyncSubmodules
```

### "Platform mismatch"

**Problem**: Custom plugin shows "incompatible platform" message

**Solution**:
- Check plugin `.vcxproj` contains the correct platform configuration
- For x64 build, must have: `<ProjectConfiguration Include="Release|x64">`
- For Win32 build, must have: `<ProjectConfiguration Include="Release|Win32">`

### "Toolset mismatch"

**Problem**: Custom plugin shows "incompatible toolset" message

**Solution**:
- Edit plugin `.vcxproj`
- Find: `<PlatformToolset>v142</PlatformToolset>` (or v141, v140, etc.)
- Change to: `<PlatformToolset>v143</PlatformToolset>`

### "CMake cache is stale"

**Problem**: Changes to CMakeLists.txt not reflected in solution

**Solution**:
```powershell
# Clear cache and regenerate
.\gen_solution.ps1 -Clean
.\gen_solution.ps1
```

### "Wrong architecture being built"

**Problem**: Building for x64 when you need Win32 (or vice versa)

**Solution**:
1. Check `src/eqlib/include/eqlib/BuildType.h`
2. Verify `MQ_EXPANSION_LEVEL` is set correctly
   - ROF = Win32
   - All others = x64
3. Regenerate: `.\gen_solution.ps1`
4. The script will auto-detect the change and clean the build

### CLion-Specific Issues

**"Cannot find Visual Studio"**

**Solution**:
- Install Visual Studio 2022 with C++ Desktop Development
- CLion → Settings → Build, Execution, Deployment → Toolchains
- Verify "Visual Studio" toolchain is detected
- Set as default if needed

**"CMake project not loaded"**

**Solution**:
- File → Reload CMake Project
- Or: Tools → CMake → Reload CMake Project
- Check CMake tool window for errors

**"Indexing takes forever"**

**Solution**:
- Right-click `build/` → Mark Directory as → Excluded
- Right-click `contrib/vcpkg/` → Mark Directory as → Excluded
- File → Invalidate Caches / Restart

---

## Best Practices

### For Developers

1. **Always regenerate after pulling upstream changes:**
   ```powershell
   git pull
   .\gen_solution.ps1
   ```

2. **Never commit generated files:**
   - `build/` directory (gitignored)
   - Generated `.sln` files
   - CMake cache files
   - Custom plugin list files (`my_plugins.cmake.custom`)

3. **Do commit:**
   - CMakeLists.txt for your plugins
   - Changes to root `CMakeLists.txt` (carefully)

4. **Keep plugins/ clean:**
   - Only plugin directories (MQ*/)
   - No random files or build artifacts

### For Plugin Developers

1. **Prefer CMakeLists.txt over .vcxproj:**
   - More portable
   - Easier to maintain
   - Better cross-IDE support

2. **Use auto-discovery when possible:**
   - Just place plugin in `plugins/MQ2YourPlugin/`
   - Let CMake handle integration

3. **Test both Debug and Release builds:**
   ```powershell
   cmake --build build --config Debug
   cmake --build build --config Release
   ```

4. **Link against MQ2Main and pluginapi, not eqlib:**
   ```cmake
   target_link_libraries(YourPlugin PRIVATE MQ2Main)
   target_link_libraries(YourPlugin PRIVATE pluginapi)
   # NOT: target_link_libraries(YourPlugin PRIVATE eqlib)
   ```

### For Teams

1. **Use custom plugin list for shared configuration:**
   ```powershell
   # Generate team plugin list
   .\gen_solution.ps1 -WritePluginsFile team_plugins.cmake

   # Commit to repository
   git add team_plugins.cmake
   git commit -m "Team plugin configuration"

   # Team members use it
   .\gen_solution.ps1 -CustomPluginsFile team_plugins.cmake
   ```

2. **Document team-specific CMake options in README**

3. **Consider Using CI/CD with CMake command-line builds:**
   ```yaml
   # GitHub Actions example
   - run: cmake -B build -G "Visual Studio 17 2022" -A x64
   - run: cmake --build build --config Release
   ```

---

## Next Steps

- **Detailed CMake documentation**: See [CMAKE_BUILD.md](CMAKE_BUILD.md)
- **Build workflow documentation**: See [BUILD_WORKFLOWS.md](BUILD_WORKFLOWS.md)
- **Plugin development guide**: See [PLUGIN_TEMPLATE.md](PLUGIN_TEMPLATE.md)
- **Migration from .vcxproj**: See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
- **Full MacroQuest docs**: https://docs.macroquest.org

---

## Summary

- **Use `gen_solution.ps1`** for convenient, automated builds
- **CMake generates .sln files** - they are not source files
- **Upstream changes merge cleanly** - just regenerate the solution
- **Custom plugins integrate automatically** - place in `plugins/` directory
- **CLion works great** - full CMake and debugging support
- **Architecture auto-detects** - no more platform confusion

The CMake build system provides a modern, flexible foundation for MacroQuest development that scales from individual contributors to large teams.
