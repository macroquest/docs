---
tags:
    - lua
---
# MacroScript to Lua

> Ported from RedGuides: [MacroScript to Lua](https://www.redguides.com/community/resources/macroscript-to-lua.2197/).

This guide will cover some of the more common building blocks of code found in macros, and ways they may be written in Lua. They may not be the only ways or the best ways, but hopefully they are useful to see.  

The purpose of this guide is primarily to help those who know the macro language, but not necessarily Lua or other programming languages, to be able to write new scripts in Lua. Its not to suggest that existing macros should be rewritten in Lua, although that may be a good learning exercise as well.  

Before getting started, its recommended to have [VS Code](https://code.visualstudio.com/) (not the same thing as Visual Studio) installed for working with Lua files. it provides syntax highlighting out of the box and some extended capabilities when adding a Lua language server extension. Also setup the [mq-definitions](https://github.com/macroquest/mq-definitions) for auto-completion.  

## Getting Started
Before getting into MQ specifics, some basics about the Lua programming language should be understood.

### Terminology
- **lua script:** Like a macro, Lua scripts are run in game via command. For example, `/lua run examples/demo_tables` where `examples/demo_tables.lua` is a Lua script which exists in the MQ Lua folder.  
- **variable:** A variable is a symbolic name for some information. `local script_name = 'demo_tables'` would define the `script_name` variable which can then be referenced elsewhere in the script, and its value would be the string, `demo_tables`. Variables can be **local** or **global**, but should typically always be made **local**.  
- **function:** A function in lua is a callable, reusable block of code. Functions can take 0 or more arguments, as well as return 0 or more results. Lua functions would be comparable to subroutines in macro script.  
- **table:** In Lua, nearly everything is a table. Tables are the main data structure for the language. Think of tables as a combination of arrays, maps, sets, lists, etc. from other languages. Tables store a collection of key, value pairs, and the values can be accessed by their keys. The keys can be numbers or strings. When the keys are contiguous numbers from 1 to N, then the table can be accessed in a similar fashion to an array. They can also be iterated over by index (like an array) or by key (like a map).  
- **userdata:** Lua represents arbitrary C data as the type `userdata`. There will be more on this later, but it is important to note that all unevaluated data returned to Lua from MQ is of type `userdata`.  
- **nil:** The Lua equivalent of macros `NULL`. nil is Luas representation of no value. One common thing to do is check that a variable is not nil, i.e. the variable has a value. This might look like `if mob then do_something() end`. This is the same as `if mob ~= nil then do_something() end`.  
- **string:** A string is used for data values that are made up of ordered sequences of characters, such as "hello world". Strings are only mentioned here because in macros, everything was a string, and in lua not everything is treated as a string. In Lua, like most programming languages, strings belong inside of quotes. This was not required in macros. For example, `local name = fippy darkpaw` would fail. `local name = "fippy darkpaw"` would work.  
- **literal:** Defining this word here just to highlight the difference between macro script and pretty much any other programming language in the world. A literal would be something like the number `2` or the string `"hello world"`. Specifically for strings, as mentioned a few times throughout this guide, they must be in single (`'`) or double (`"`) quotes. This differs from macro script where strings don't need to be in quotes.  
- **true/false:** Boolean values in Lua. They must be written lowercase, not to be confused with `TRUE` and `FALSE` seen in macros. One quick note on true/false in Lua is that numbers do not behave like booleans in conditions like they do in macros or several other languages. `if my_int_variable then` where `my_int_variable` is `0` would not evaluate to `false`. To compare numbers in if statements, the `==` or `~=` operators should be used.

### Hello World
[PIL: Hello World](https://www.lua.org/pil/1.html)  
The typical Hello World example for a Lua script is relatively short. No functions need to be written, no variables declared. Simply create a file in  the MQ Lua folder called `helloworld.lua` with the following content:

```lua
print('Hello, world')
```

And then execute the script in game by running the command: `/lua run helloworld`

This script calls the built in Lua `print` function to print the string `Hello, world`. It will print to the MQ console window. The Lua `print` function behaves the same way as `/echo` in macro script.

### Variables
[PIL: Local Variables and Blocks](https://www.lua.org/pil/4.2.html)  
Lua can have both local and global variables within the scope of a lua script, similar to a macro. In most cases, variables probably don't need to be made global. Global variables may have some use cases as script grow and begin to include multiple other scripts, but even then they are unlikely to be necessary, and most likely problems can be solved other ways.  

To declare a variable, its as simple as:
```lua
-- DEBUG_FLAGS will be a global variable with a value of 0
DEBUG_FLAGS = 0

-- healPct will be a local variable with a value of 70
local healPct = 70

-- mobName will be a local variable which stores the string "Fippy Darkpaw"
local mobName = "Fippy Darkpaw"
```

> NOTE: `--` is used to write comments (text which will not be executed as part of the script) in Lua.

Local variables are valid for the block of code in which they are declared in. For example:
```lua
local myLevel = mq.TLO.Me.Level()
if myLevel > 5 then
    local canUseKick = true
end
print(canUseKick)
```

The above code snippet defines a local variable inside the if block, so it is no longer in scope after the end of the if block. The print statement will output `nil` because `canUseKick` is no longer in scope.  

The entirety of a lua script is also one code block. Local variables defined at the top level of the script can be referenced anywhere else in the script below where they have been defined. However, its always best to define variables as close as possible to where they will be used, and with as limited scope as possible.  

Variables in Lua are not strongly typed, and can be assigned all sorts of values to any variable. To keep code simple and easy to follow, avoid reusing one variable for multiple different types of data. Just note that there is nothing stopping assigning a variable a number value in one line, and then assigning it a string value in the next.  

The following code snippet shows some macro variable related commands and their lua equivalents:  

Create a local variable `scriptName` with the value `helloworld`.
```
| /declare variable_name type scope value
/declare scriptName string local helloworld
```
```lua
local scriptName = 'helloworld'
```

Create a global variable with the value `1`:
```
/declare mobCount int global 1
```
```lua
mobCount = 1
```

Update the value of variable `mobCount` to `2`:
```
/varset mobCount 2
```
```lua
mobCount = 2
```

Perform some math operation on a variable:
```
/varcalc mobCount ${mobCount}+1
```
```lua
mobCount = mobCount + 1
```

Store an MQ DataType in a variable:
```
/declare nearestNPC spawn local
/vardata nearestNPC Spawn[npc targetable]
```
```lua
local nearestNPC = nil
nearestNPC = mq.TLO.Spawn('npc targetable')
```

### Output
In Lua, output text to the console using `print`. Do not use `mq.cmd.echo` or `mq.cmd('/echo ...')`.  
Macro: `/echo some text`  
Lua:   `print('Some text')`  

Print colored text using the same color codes as `/echo`:  
Macro: `/echo \arRed text`  
Lua:   `print('\arRed text')`  

Print the value of a variable:  
Macro: `/echo ${scriptName}`  
Lua:   `print(scriptName)`  

Print the value of a string variable with some other text. `..` is used to concatenate strings:  
[PIL: String concatenation](https://www.lua.org/pil/3.4.html)  
Macro: `/echo Script Name: ${scriptName}`  
Lua:   `print('Script Name: '..scriptName)`  

> NOTE: This requires that the type of data stored in the variable `scriptName` be a string.

Another way is to use a formatted string:  
Lua:   `print(string.format('Script Name: %s', scriptName))`  

Another syntax for formatted strings:  
Lua:   `print(('Script Name: %s'):format(scriptName))`  

MQ automatically adds a `printf` function for all Lua scripts to make use of as well, so the above string.format isn't necessary:  
Lua:   `printf('Script Name: %s', scriptName)`  

Refer to the [C++ printf](https://cplusplus.com/reference/cstdio/printf/) reference for details on formatted string specifiers.

> TIP: `%s` in a formatted string can cope with a variable being `nil`.

Also check out [Knightly's Write.lua](https://www.redguides.com/community/resources/write-lua.2193) resource for debug logging helpers.

### Functions
[PIL: Functions](https://www.lua.org/pil/5.html)  
Lua functions are the equivalent of macro subroutines. Like variables, functions can be declared as `local` or `global`. In most cases, they don't need to be defined globally.  

Example 1: A function which takes no arguments

Macro:
```
Sub echoMyName
  /echo ${Me.Name}
/return

Sub Main
  /call echoMyName
/return
```

Lua:
```lua
local function printMyName()
  print(mq.TLO.Me.Name())
end

printMyName()
```

Example 2: A function with 1 named argument

Macro:
```
Sub Main
  /declare scriptName global helloworld
  /call eyecatcher "section about subroutines"
/return

Sub eyecatcher(string message)
  /echo \ar${scriptName}: \a-x${message}
/return
```

Lua:
```lua
local scriptName = 'helloworld'

-- Define a local function which prints a formatted string with the script name and a message:
local function eyecatcher(message)
  printf('\ar%s: \a-x%s', scriptName, message)
end

-- Call the function which we just defined, similar to a macro /call eyecatcher "section about subroutines"
eyecatcher('section about subroutines')
```

Example 3: A function with multiple named arguments

Macro:
```
Sub somefunc(bool arg1, int arg2)
  /echo ${arg1}
  /echo ${arg2}
/return

Sub Main
  /declare debug bool local true
  /declare id int local ${Me.ID}
  /call somefunc ${debug} ${id}
/return
```


Lua:

```lua
local function somefunc(arg1, arg2)
  print(arg1)
  print(arg2)
end

local debug = true
local id = mq.TLO.Me.ID()
somefunc(debug, id)
```

Example 4: A function with a variable number of arguments:  
[PIL: Variable number of arguments](https://www.lua.org/pil/5.2.html)
```lua
local function print_values(...)
  local arg = {...}
  for _,value in ipairs(arg) do
    print(value)
  end
end

local name = mq.TLO.Me.Name()
local level = mq.TLO.Me.Level()
local class = mq.TLO.Me.Class()
print_values(name, level, class)
```

Example 5: A function which returns multiple values  
[PIL: Multiple Results](https://www.lua.org/pil/5.1.html)  
```lua
local function get_class_and_race(a_spawn)
  return a_spawn.Class(), a_spawn.Race()
end

local class, race = get_class_and_race(mq.TLO.Target)
```

Example 6: Return a table of values  
In most cases it will be more extensible and easier to read to return multiple values in a table rather than returning multiple values.
```lua
local function get_class_and_race(a_spawn)
  return {class=a_spawn.Class(), race=a_spawn.Race()}
end

local targetInfo = get_class_and_race(mq.TLO.Target)
printf('Target class=%s, race=%s', targetInfo.class, targetInfo.race)
```

### Tables
Before getting into flow control, some knowledge of Lua tables is needed. They will be used in several of the examples.

In lua, tables are the goto data structure for arrays, maps, pretty much everything.

Tables store key/value pairs. The keys can be numbers or strings. They aren't required to be contiguous numbers, but if using the table as an array, then they must be.

> NOTE: Lua array tables start from index 1.

Array table examples: 

Define an array by passing just a set of values. It will automatically give each value an index starting from `1`.
```lua
local priests = { 'clr', 'dru', 'shm' }
```

Values can also be indexed explicitly, but prefer the example above:
```lua
local casters={ [1]='enc', [2]='mag', [3]='nec', [4]='wiz' }
```

Lua also provides a table function for appending to arrays:
```lua
local tanks = {}
table.insert(tanks, 'war')
table.insert(tanks, 'pal')
table.insert(tanks, 'shd')
```

To access a value directly by its index:
```lua
print(priests[2])
```
This would print `dru`.

Tables can also be maps instead of arrays:
```lua
local mez_classes = { brd=true, enc=true }
```

Values from the table can be looked up by key:
```lua
print(mez_classes.brd)
print(mez_classes['brd'])
local key = 'enc'
print(mez_classes[key])
```

While the above examples each just show grabbing a table value directly by index or key, tables can also be accessed by iterating over the values. This will be covered more in the examples under the section on control flow.

Deciding whether a table should be an array or a map depends on the application and how the data will be used. The examples coming up prefer using tables as maps so that values could be looked up directly by key without having to iterate over the table to find the value.

The `mez_classes` example above is using a table as a `Set` data structure, where the key is the unique value in the table like class short names, and the value is `true`.

[Lua Sets](https://www.lua.org/pil/11.5.html) provides an example helper function to create sets like this.

### Command Line Arguments

Lua provides access to command line arguments through the use of the same `...` which was introduced earlier with functions for variable number of arguments.

Below is an example which iterates over the arguments which the script is called with:
```lua
local args = {...}
printf('Script called with %d arguments:', #args)
for i,arg in ipairs(args) do
  printf('arg[%d]: %s', i, arg)
end
```

Add this code to a lua script `testarg1.lua` and execute it with: `/lua run testarg1 assist ini server_toon.ini`

This would output:
```lua
Script called with 3 arguments:
arg[1]: assist
arg[2]: ini
arg[3]: server_toon.ini
```

Another example, uses named key/value arguments to add the args directly to a settings table:
```lua
local settings = {}
local current_key = nil

for _,arg in ipairs(args) do
  if not current_key then
    current_key = arg
  else
    settings[current_key] = arg
    current_key = nil
  end
end

for key,value in pairs(settings) do
  printf('Settings[%s]=%s', key, value)
end
```

Add this code to a lua script `testarg2.lua` and execute it with: `/lua run testarg2 role assist ini server_toon.ini`

This would output:
```
Settings[role]=assist
Settings[ini]=server_toon.ini
```

### Require

The Lua `require` function is used to load one Lua file from another. For example, `Write.lua`, by Knightly, is a library which provides useful functions for logging. `Write.lua` is meant to be used by other scripts, and would be included as a module with: `local write = require('write')`. This would then allow a script to call the functions from `Write.lua` such as `write.debug('my debug message here')`.

This is similar to include files in macros, though works slightly differently. Include files in macros make the macro behave as if the included files code was all inserted directly where the include was done. In Lua, the results of requiring another Lua file are typically stored into a variable. So, if a script is required, and it returns a table containing several helper functions, then that table is stored into a variable and those functions are accessed through that variable.

Require is also how MQ makes its own functionality available to Lua scripts, such as TLOs, events, binds and commands which will all be discussed later. In short, its all made available by including the following line:
```lua
local mq = require('mq')
```

This provides access to all the MQ functionality that has been made available to lua, and assigns it into the variable `mq`.

A couple short examples using require:

Create a file named `utils.lua`
```lua
-- Create a table which will hold everything we want to be exported from this lua file
local utils = {}

-- Add a function to the utils table under the key "perform_some_task"
function utils.perform_some_task()
  print('successfully performed some task')
end

-- Return the utils table containing our function
return utils
```

Then include `utils.lua` into the main script using a require statement:
```lua
local utils = require 'utils'

utils.perform_some_task()
```

Another way:
```lua
-- Create a local function which will not be exported, so only functions in this file may use it
local function internal_helper()
  print('successfully performed some task')
end

-- Create a local function which will be exported and callable by scripts which require this file
local function perform_some_task()
  internal_helper()
end

-- Create a table which will hold everything we want to be exported from this lua file
local exports = {
  perform_some_task = perform_some_task
}

-- Return the export table
return exports
```

Then include `utils.lua` into the main script using a require statement:
```lua
local utils = require 'utils'

utils.perform_some_task()
-- Calling utils.internal_helper() would result in an error
--utils.internal_helper()
```

### Scope and Processing Order

Scope was touched on a little bit earlier when talking about variables. The same applies to functions as well. Its always important to be aware of where variables or functions are defined, and when they will be in the correct scope to be referenced.

An important part of this is understanding that Lua scripts are processed top down. A variable or function can only be referenced by code that occurs after it has been declared.


Compare these three examples:
```lua
local function print_version()
    print(version)
end

local version = '1.0.0'
print_version()
```

This will print `nil` because `version` has not been defined ahead of the function `print_version`, so it will be printing an unknown variable.
```lua
local version = '1.0.0'
local function print_version()
    print(version)
end

print_version()
```

This will print `1.0.0` because `version` has been defined ahead of the function `print_version`, so it will be able to find the correct variable.
```lua
local function print_version(version)
    print(version)
end

local version = '1.0.0'
print_version(version)
```

While the second example works, it sort of treats `version` like a global variable. The scope of the `version` variable could be limited by passing it as an argument to the function instead.

## Control Flow
[PIL: Control Structures](https://www.lua.org/pil/4.3.html)  
A number of options are provided to control the flow of the script, such as if then else, for loops, while loops and repeat until.

### If then else
[PIL: if then else](https://www.lua.org/pil/4.3.1.html)  
If conditions from macros should look pretty similar in lua.

Macro:
```
/declare my_name string local noone
/declare max_level int local 115
/if (${my_name.Equal[noone]}) {
    /echo the values match
}

/if (${Me.Level} < ${max_level}) {
    /echo must get more levels
}

| In macros, conditions usually have to check .ID on something
/if (${Me.Invulnerable.ID}) {
    /removebuff ${Me.Invulnerable}
}
```

Lua:
```lua
local my_name = 'noone'
local max_level = 115
if my_name == 'noone' then
    print('the values match')
end

if mq.TLO.Me.Level() < max_level then
    print('must get more levels')
end

-- In Lua, conditions should be able to just check something is not nil, without
-- having to check the ID.
if mq.TLO.Me.Invulnerable() then
    mq.cmdf('/removebuff %s', mq.TLO.Me.Invulnerable())
end
```

Macro:
```
/if (${my_name.NotEqual[someone]}) {
    /echo =~ is not equals in lua
}
```

Lua:
```lua
if my_name ~= 'someone' then
    print('~= is not equals in lua')
end
```

> NOTE: Do not write a condition that combines both `not` and `==`.
> For example, instead of this:
> ```lua
> if not myName == 'aquietone' then
> ```
> use this:
> ```lua
> if myName ~= 'aquietone' then
> ```

### For Loops
[PIL: For Loops](https://www.lua.org/pil/4.3.5.html)  
For loops in lua are most often going to be iterating over table values. This is done using either `pairs` or `ipairs`. Both `pairs(a_table)` and `ipairs(a_table)` will return 2 values on each pass of the loop, the key and the value for that key.

`pairs` iterates over all keys in a table (treats the table as a map).
```lua
for class, value in pairs(mez_classes) do
    printf('Class %s can mez: %s', class, value)
end
```

`ipairs` iterates over contiguous numeric keys in a table starting from index 1 (treats the table as an array).
```lua
for index, value in ipairs(casters) do
    printf('casters[%d]=%s', index, value)
end
```

[PIL: Numeric For](https://www.lua.org/pil/4.3.4.html)  
Lua also allowed to iterate over a range like 1 to N:
```lua
for spellIter=1,5 do
  print(mq.TLO.Me.Book(spellIter).Name())
end
```

Or, an example taken from `pocketfarm.mac` but changed so it doesn't print a lot of stuff:  
Macro:
```
/for i 1 to ${SpawnCount[pc targetable]}
  /if (${NearestSpawn[${i},pc targetable].Name.Equal[${Me.Name}]}) {
    /echo ${NearestSpawn[${i},pc targetable].Name.Length}
  }
/next i
```

Lua:
```lua
for i=1,mq.TLO.SpawnCount('pc targetable')() do
  if mq.TLO.NearestSpawn(i..', pc targetable').Name() == mq.TLO.Me.Name() then
    print(mq.TLO.NearestSpawn(i..', pc targetable').Name.Length())
  end
end
```

### While Loops
[PIL: While Loops](https://www.lua.org/pil/4.3.2.html)  
While loops can also be used to iterate over a range:
```lua
local loop = 1
while loop < 3 do
  print('Loop #'..loop)
  loop = loop + 1
end
```

### Repeat Until
[PIL: Repeat Until](https://www.lua.org/pil/4.3.3.html)  
There is also repeat until:
```lua
repeat
  printf('Loop #%d', loop)
  loop = loop - 1
until loop == 0
```

### /goto
This is only mentioned here because it is commonly used in macros. Avoid using this in Lua.

While Lua also has goto, it should be possible to handle most situations with normal flow control like those described above.  

One valid scenario for goto would be to handle the lack of `continue` in Lua, however, this can still be avoided in most situations.

## MQ
The first line to most lua scripts written for MQ will be:  
```lua
local mq = require('mq')
```

This provides access to all the MQ functionality.

### TLOs
Top Level Objects, or TLOs, are how data is accessed from MQ. This should already be a pretty familiar concept from doing just about anything with MQ, including echoing data to the console, writing conditions in KissAssist INIs, writing macros, writing reacts, etc. We use TLOs every day. Some examples include `${Me}`, `${Target}`, `${Spawn}` and `${FindItem}`.

To access TLOs using the `mq` variable:

```lua
local mq = require('mq')

local assist_name = mq.TLO.Group.MainAssist.CleanName()
printf('Assisting: %s', assist_name)
```

```lua
local mq = require('mq')

if mq.TLO.Target() then
    local mob_hp = mq.TLO.Target.PctHPs()
    if mob_hp < 98 then
        printf('Assisting on %s', mq.TLO.Target.CleanName())
        -- call some assist code
    end
end
```

```lua
local mq = require('mq')

local target = mq.TLO.Target
if target() then
    if target.Distance3D() > 15 then
        print('Moving closer to target')
        -- call some movement code
    end
end
```

In general, to convert from a TLO in macro format to a TLO in Lua format, strip the `${ }` and add `mq.TLO.` on the front. If the goal is to evaluate the data to a Lua type, add `()` on the end. For example, `${Me.PctHPs}` becomes `mq.TLO.Me.PctHPs()`.

> To evaluate to a Lua type, it must always end in **empty** (). `mq.TLO.Spawn('npc')` will be type `userdata` while `mq.TLO.Spawn('npc')()` will be type `string`.  

> Background on Lua userdata: [PIL: Userdata](https://www.lua.org/pil/2.7.html)  

```lua
printf('type(mq.TLO.Me.Name) == %s', type(mq.TLO.Me.Name)) -- prints userdata
printf('type(mq.TLO.Me.Name()) == %s', type(mq.TLO.Me.Name())) -- prints string
```

Data returned by MQ is always of type userdata. Adding () on the end will convert the MQ userdata to the appropriate lua datatype.
```lua
printf('type(mq.TLO.Spawn("npc") == %s', type(mq.TLO.Spawn("npc")))
-- The following print would throw an error because userdata cannot be concatenated to a string
printf('mq.TLO.Spawn("npc") == %s', mq.TLO.Spawn("npc"))

printf('type(mq.TLO.Spawn("npc")() == %s', type(mq.TLO.Spawn("npc")()))
printf('mq.TLO.Spawn("npc")() == %s', mq.TLO.Spawn("npc")())
```

### Commands
Execute EQ and MQ commands from Lua scripts like so:
```lua
mq.cmd('/keypress DUCK')
mq.delay(1000)
mq.cmd('/keypress DUCK')
```

To run a command with formatted input, use `mq.cmdf`:
```lua
mq.cmdf('/echo %s', mq.TLO.Me.Name())
```

### Bindings
[Lua Events and Binds](events-and-binds.md)  
Define a function for the bind to call when its executed
```lua
local function bind_help()
  print('some helpful text')
end
```

Assign the function to a command that can be run in game:
```lua
mq.bind('/howto', bind_help)
```

Binds can be removed using `mq.unbind(bindCommand)`.

### Events
[Lua Events and Binds](events-and-binds.md)  
First step is to define the function which will be called when the event triggers:
```lua
local function event_handler()
  print('entered event_handler')
end
```

Next, define the event using `mq.event` and pass the event name, match text, and the function.
```lua
mq.event('BrokenPole', "#*#You can't fish without a fishing pole, go buy one.#*#", event_handler)
```

Then later, typically in the main run loop of the script, call `mq.doevents`.
```lua
mq.doevents()
```

Similar to macros, events can also be flushed with `mq.flushevents()`.  

Events can be deregistered using `mq.unevent(eventName)`.

### Macro ${Select[...]} Statements
Lua doesn't have `${Select[...]}` quite like the macro language does, but it has other solutions:

1. Use a loop and iterate through values:

    Consider a select statement like `${Select[${Me.Class.ShortName},clr,dru,shm]}`

    ```lua
    local my_class = mq.TLO.Me.Class.ShortName()
    for _,class in  ipairs({'clr','dru','shm'}) do
        if my_class == class then
            -- assign something or perform some action based on matching class
        end
    end
    ```

2. Use logical operators like "or" (https://www.lua.org/pil/3.3.html)

    Consider a select statement like `${Select[${role},pullertank,tank]}`

    ```lua
    local role = 'tank'
    if role == 'pullertank' or role == 'tank' then
        -- assign something or perform some action based on matching role
    end
    ```

3. Use tables by checking for the presence of the value in the table

    Consider a select statement like `${Select[${Zone.ID},345,344,202,203,279,151,33506]}`

    ```lua
    local safe_zones = { [345]=true, [344]=true, [202]=true, [203]=true,  [279]=true, [151]=true, [33506]=true}
    local current_zone = mq.TLO.Zone.ID()
    if safe_zones[current_zone] then
        -- disable some functionality because we are in a safe zone
    end
    ```

    The above example checks the current zone ID against a list of zone IDs which have been classified as safe zones.

    ```lua
    local mez_classes = { brd=true, enc=true }
    local my_class = mq.TLO.Me.Class.ShortName()
    if mez_classes[my_class] then
        -- enter into mez handling routines
    end
    ```

    The above example checks the characters class against a list of mez capable classes to gate entering mez handling functions.

    Taking this a bit further, table values can also be functions:
    ```lua
    local function enc_mez()
    print('handle mezzing as an enc')
    end

    local function brd_mez()
    print('handle mezzing as a brd')
    end

    local mez_funcs = { enc=enc_mez, brd=brd_mez }
    local my_class = mq.TLO.Me.Class.ShortName()
    if mez_funcs[my_class] then
    mez_funcs[my_class]() -- call the function from the table
    end
    ```

### Macro /delay
Use mq.delay to achieve the same thing as a macros /delay command.

Delay a fixed amount of time:
```lua
print('wait 1 second then print again')
mq.delay(1000)
print('finished waiting')
```

Delay with a condition to end the delay early:
```lua
local function should_stop_waiting()
  -- implement some more complex condition for when to break
  -- early from the delay.
  return not mq.TLO.Me.Casting()
end

print('wait 5 seconds or until should_stop_waiting() returns true')
mq.delay(5000, should_stop_waiting)
print('finished waiting')
```

This provides a function which will be called, which should return true or false, to decide whether to cancel the delay.

!!! warning

    `mq.delay` cannot be used within an ImGui callback. It will result in an error, as the ImGui callback is called every frame and cannot be delayed. A required module also cannot include `mq.delay` within its global scope.  

    In this example, a button click in the UI attempts to wait for an action to complete. The UI cannot be delayed, so it does not work.
    ```lua
    if ImGui.Button('mem spell') then
        mq.cmd('/memspell 1 "minor healing"')
        mq.delay(5000)
    end
    ```
    A more appropriate way to solve this would be to set some state from the button, and then handle the spell memorization from the scripts main loop.

    In this example, `init.lua` tries to require a module which uses `mq.delay` at the global scope, and so it does not work.
    ```lua
    -- navHelper.lua
    local mq = require('mq')

    mq.cmd('/nav target')
    mq.delay(5000)
    print('ran to target')
    ```
    ```lua
    -- init.lua
    require('navHelper')
    ```
    Modules which are loaded with require should generally have all logic contained within functions, which can then be called.


### Macro Sub Main Function
Lua scripts are processed from top to bottom, and don't actually require code to be inside of a function, unlike how macros always have a Sub Main where execution begins. Think of the entire lua file itself as the main function, entering at line 1 of the file when the script is run.

There will often times still be blocks of code that perform a similar function to the main subroutine of a macro, like the typical /while or /goto loops people are familiar with from macros.

For example, consider a macro Sub Main like below:
```
Sub Main
  /while (1) {
    /doevents
    /call check_target
    /delay 10
  }
/return
```

This could be accomplished in lua using a while loop:
```lua
while true do
  mq.doevents()
  check_target()
  mq.delay(10)
end
```

Code like the above example will usually be near the bottom of the file, due to how lua scripts are processed. Variables and functions can only refer to things which have already been defined, i.e. were declared earlier in the file (unless defined globally, but avoid that unless necessary).

Alternatively, the code could be placed inside of a function, which is then called later on near the bottom of the file.

```lua
local function main()
  while true do
    mq.doevents()
    mq.delay(100)
  end
end

main()
```

### Macro /call and ${Macro.Return}
Macro subroutines call other subroutines using `/call my_function "${arg1}"`. Lua functions are just called like `my_function(arg1)`.

Macro subroutines return results using `/return ${result}`. Lua functions return similarly, using `return result`.

Example: The macro Main sub calls subroutine IsPluginLoaded with argument "mq2eqbc". IsPluginLoaded returns the result of the Plugin.IsLoaded TLO Member, which is TRUE or FALSE.
```
Sub IsPluginLoaded(plugin)
    /if (${Plugin[${plugin}].IsLoaded}) /return TRUE
/return FALSE

Sub Main
    /call IsPluginLoaded "mq2eqbc"
    /echo ${Macro.Return}
/return
```

Example: The lua script calls function IsPluginLoaded with argument 'mq2eqbc'. IsPluginLoaded returns the result of the Plugin.IsLoaded TLO Member, which is true or false.
```lua
local function IsPluginLoaded(plugin)
    return mq.TLO.Plugin(plugin).IsLoaded()
end

local eqbcLoaded = IsPluginLoaded('mq2eqbc')
print(eqbcLoaded)
```

### Timers
Timer variables are used commonly throughout macros for controlling how often to attempt an action as well as other scenarios. There is no direct translation from the macro Timer type to Lua, however, a couple different options are available to implement them.  

1. `mq.gettime`: MQ provides this function for getting the current time with millisecond precision.  
2. `os.time` and `os.difftime`: These can be used to implement a timer with second precision. [PIL](https://www.lua.org/pil/22.1.html)  

Example: Only use an ability when its reuse time has passed.
```lua
local function do_ability(ability)
  if mq.gettime() - ability.lastUsedMillis > ability.reuseTimeMillis then
    mq.cmdf('/useability %s', ability.name)
    ability.lastUsedMillis = mq.gettime()
  end
end
```
Alternatively, a timer class could be created using similar logic to above for better reusability, allowing for code like `if ability.timer.is_expired() then`.

### mq.parse

The `mq.parse` command allows to evaluate a macro expression in Lua and assign the result to a variable. This could be useful if reading macro expressions such as conditions like those in KA or reacts from an INI file.

```lua
local mq = require('mq')

local IF_STMT = '${If[%s,1,0]}'

local function testCondition(condition)
  -- the output from mq.parse is a string
  return mq.parse(IF_STMT:format(condition)) == '1'
end

-- pretend these conditions were just read in from some config file like a KA INI
local conditions = {
  '${Me.PctHPs}<50',
  '${Me.PctHPs}>50',
}

for _,condition in ipairs(conditions) do
  if testCondition(condition) then
    printf('Condition "%s" was true', condition)
  else
    printf('Condition "%s" was false', condition)
  end
end
```

### Other commonly used TLOs

- **Math**: Prefer to use the native math operations supported in Lua. There's no need to use `${Math.Calc[]}` or `/varcalc` when the language can already do `1 + 1`. For other operations like rounding, floor, ceiling, see the [math library](http://lua-users.org/wiki/MathLibraryTutorial).
- **String**: Lua provides plenty of string related operations which can be found [here](http://lua-users.org/wiki/StringLibraryTutorial). There should be no need to use the `String` TLO.
- **.Equal** and **.NotEqual**: No need to use macro language sorts of comparators, just use lua `==` and `~=` instead.
- **.Arg[|,2]**: Lua provides [many examples]((http://lua-users.org/wiki/SplitJoin)) for splitting strings which remove the need to use macro `.Arg`.

## Storage
For more info on storage, such as persisting configuration for a Lua script, refer to [Persisting Configuration in Lua Scripts](pickle.md)  

## Extras

### The /lua parse command
MQ provides a command line utility for parsing lua, which is pretty useful for debugging. It automatically includes `local mq = require('mq')`, and can be used like:
```
/lua parse mq.TLO.Me.Name()
```

It can do much more than that, including multiple statements strung together, loops, etc. The output gets printed to the console.
```
/lua parse i = 1 while mq.TLO.NearestSpawn(i..', pc')() do print(mq.TLO.NearestSpawn(i..', pc')) i=i+1 end
```

The above example would print the name of PCs incrementing over a NearestSpawn search.

### VS Code Extensions
In addition to `mq-definitions`, some useful VS Code extensions include:

- Rainbow Brackets  
- Indent Rainbow  
- Vscodemq2  
- Codemap  

For the codemap extension, add a reference to this javascript file (ColdBlooded's handywork again) to the codemap section in `settings.json`:

`"codemap.mac": "<location of that file>",  `

```javascript
"use strict";

Object.defineProperty(exports, "__esModule", { value: true });
const fs = require("fs");
class mapper {
    static read_all_lines(file) {
        let text = fs.readFileSync(file, 'utf8');
        return text.split(/\r?\n/g);
    }
    static generate(file) {
        "".match(/.* \(.*\) {/g);
        let members = [];
        try {
            let line_num = 0;
            mapper
                .read_all_lines(file)
                .forEach(line => {
                line_num++;
                line = line.trimStart();
                if (line.startsWith("Sub "))
                    members.push(`${line.substr(4)}|${line_num}|function`);
                else if (line.startsWith(": "))
                    members.push(`${line.substr(1)}|${line_num}|level2`);
            });
        }
        catch (error) {
        }
        return members;
    }
}
exports.mapper = mapper;
//# sourceMappingURL=mapper_md.js.map
```

### Mixing Lua and Macro
Macro variables have always been available through the command line while a macro is running. For example, when running a macro that created a global variable `MainAssistID`, then it is possible to `/echo ${MainAssistID}` and see the value of that variable at any time.

Similarly, macro variables could be updated from the console using `/varset`.

Lua variables are not exposed in the same way, regardless of whether they are global or local. One Lua script cannot access variables from another separately running Lua script, or by the lua parse command.

Lua does have access to Macro variables, through `mq.TLO.Macro.Variable('macro_variable_name')()`. This makes it possible to do something like use Lua to create an ImGui based UI for an existing macro.

## Common Problems

- Comparing values with data from `mq.TLO.Something`: Due to the difference between userdata and regular lua types like numbers or strings, comparisons will often fail when the values visibly look like they should be the expected type.

    Example: 
    ```lua
    if mq.TLO.Target.CleanName == 'aquietone' then
    ```
    This will never succeed because `mq.TLO.Target.CleanName` is of type `userdata`, not `string`. It needs `()` on the end to trigger the evaluation from `userdata` to a lua `string`, like:
    ```lua
    if mq.TLO.Target.CleanName() == 'aquietone'
    ```

    Example:
    ```lua
    if mq.TLO.Target.PctHPs < 90 then
    ```
    This will have the same issue, printing `mq.TLO.Target.PctHPs` will look like a number, but it is actually `userdata`, and it needs to be evaluated by adding `()`.

- Command line argument types for bindings are always going to be passed into the bind function as strings. `tonumber(variable)` can be used to convert the type to a number in order to accept a number input to a binding command. If the input can not be parsed to a valid number, then `tonumber(variable)` will return `nil`.

- `mq.delay` is causing errors or being ignored. There may be scenarios, as outlined above in the section on `mq.delay`, where delays are not supported. MQ will normally throw an error saying so, but there may be scenarios which are missing the appropriate error handling.
