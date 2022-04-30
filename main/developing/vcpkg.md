# Using Vcpkg in MacroQuest

MacroQuest incorporates the vcpkg library manager for C and C++ to make installing and maintaining third party libraries easier.
Microsoft's vcpkg is a compile-from-source library manager that uses cmake to compile the library on the system it is needed.
This has the benefits of both distributing a lib AND distributing source to make it easy to compile libs so that you don't have
to worry about which directories to include and setup.

For MacroQuest, we have slightly modified the way that vcpkg works.

## Installation of vcpkg

While you can bootstrap and install vcpkg yourself and it will work, it is easier to let MacroQuest's build scripts handle this
for you. The first time that you build MacroQuest from the sln file, vcpkg will bootstrap itself.

From that point, the vcpkg.exe will exist in contrib/vcpkg and this is the file that can be used to search for packages.
Because of the modifications for MacroQuest, you do not need to run vcpkg integrate or vcpkg integrate install.

## Installation of packages

vcpkg_mq is setup to use custom manifests to install required packages. These manifests are automatically set with the static triplet to match your architecture.

Including packages with your plugin or project requires that you create a manifest file next to your vcxproj. In that same directory,
you'll create `vcpkg_mq.txt` with a list of the packages that your project requires. The packages are separated by line breaks and
mimic the format that you would use on the command line to install a package. The triplet is only required if it is different from
your architecture or if you don't want it to be static.

For example, if you wanted yaml-cpp and sleepy-discord, but you wanted the websocketpp feature of sleepy-discord, your vcpkg_mq.txt
manifest would look like:

```txt title="vcpkg_mq.txt"
yaml-cpp
sleepy-discord[websocketpp]
```

Next time that you build, these packages will be automatically installed.

## Inclusion of libraries in your project

If you are building a plugin or one of the core projects, the include paths for headers and libraries are already set.
Just `#include "yourlibrary.h"` as you normally would and add any .lib file to your dependency list. You do not need
to add the paths unless your library installs to a non-standard location or a subdirectory. This can be done through
the Visual Studio interface, but below is an example of what a vcxproj might look like when adding yaml-cpp to the list of dependencies:

```xml
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Debug|Win32'">
    <Link>
      <AdditionalDependencies>libyaml-cppmdd.lib;%(AdditionalDependencies)</AdditionalDependencies>
    </Link>
  </ItemDefinitionGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">
    <Link>
      <AdditionalDependencies>libyaml-cppmd.lib;%(AdditionalDependencies)</AdditionalDependencies>
    </Link>
  </ItemDefinitionGroup>
```

If you do need to set specific paths, make sure that those paths are relative.


## Updates

When you update the repository, vcpkg_mq will update itself if you have git installed in your path. When the git hash
for the submodule changes, vcpkg_mq will manage its own updates both for the executable and for any installed packages,
there is nothing you need to do.

To force an update of vcpkg, delete the following file:

- contrib/vcpkg/vcpkg_mq_last_bootstrap.txt

This typically only needs to be done when the vcpkg repo is updated, but is also helpful for testing.


## Removing packages

Prebuilt packages are not removed, only updated as needed. To uninstall a package, use `vcpkg remove` as you would normally.
