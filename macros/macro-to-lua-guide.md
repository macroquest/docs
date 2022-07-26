Author: aquietone : from RG `https://www.redguides.com/community/resources/macroscript-to-lua.2197/`

# MacroScript to Lua 0.2

This guide will cover what (I) think seem to be some of the more common building blocks of code found in macros, and ways they may be written in Lua. They may not be the only ways or the best ways, but hopefully they are useful to see.

The purpose of this guide is primarily to help those who know the macro language, but not necessarily Lua or other programming languages, to be able to write new scripts in Lua. Its not to suggest that existing macros should be rewritten in Lua, although that may be a good learning exercise as well.

All the Lua code from this guide is also included in the ```howto.lua``` script provided with the guide. Note that this script is by no means an example of well formatted code, but just a compilation of all the examples in this guide mashed into one script that can be run.

Before getting started, I'd recommend (and probably everyone else too) using Visual Studio Code (not the same thing as Visual Studio) as your editor for Lua files. it should provide syntax highlighting out of the box, and some extended capabilities when adding a Lua language server extension. Coldblooded also wrote some autocompletion things for MQ and ImGui which are linked below, and require a language server extension. VS Code also has an MQ macro extension in case you don't already have that, which is a nice added bonus.

Other Resources
[MQ2Lua wiki]('https://docs.macroquest.org/lua/')
[Lua Events and Binds]('https://docs.macroquest.org/lua/events-and-binds/')
[Programming in Lua]('https://www.lua.org/pil/contents.html')
[Coldblooded's Lua autocompletion]('https://gitlab.com/Coldblooded/mq-emmylua-definitions')

Table of Contents


1. Getting Started

1. Terminology
1. Hello World
1. Variables
1. Output
1. Functions
1. Tables
1. Command Line Args/Parameters
1. Require
1. Scope and processing order

* Control Flow

1. If then else
1. For loops
1. While loops
1. Repeat until
1. Goto (Probably best to this)

* MQ

1. TLOs
1. Commands
1. Bindings
1. Events
1. Macro ${Select[...]} Statement
1. Macro /delay
1. Macro Sub Main
1. Macro /call and ${Macro.Return}

* Storage

1. INI
1. SQLite
1. Lua Tables

* Extras

1. The ```/lua parse``` command
1. VS Code extensions
1. Mixing Lua and Macro

* Common Gotchas

## 1. Getting Started
To get started, this guide will cover the basics of a Lua script, without getting into any of the MQ integrations.

## 1.1 Terminology
- *lua script:* Like a macro, Lua are scripts which will be run in game by issuing a command like ```/lua run examples/demo_tables``` where ```examples/demo_tables.lua``` is a Lua script which exists in the MQ Lua folder.

- *variable*: A variable is a symbolic name for some information. Variables are declared in a lua script like ```local script_name = 'demo_tables'```. This would define the ```script_name``` variable which can then be referenced elsewhere in the script, and its value would be the string, ```demo_tables```. Variables can be local or global, but should typically always be made local. If you're familiar with declaring variables in macros, its pretty much the same thing.

- [*function*]('https://www.lua.org/pil/2.6.html'): A function in lua is a callable, reusable block of code. Functions can take 0 or more arguments, as well as return 0 or more results. Lua functions would be comparable to subroutines in macro script.

- [*table*]('https://www.lua.org/pil/2.5.html'): In Lua, nearly everything is a table. Tables are the main data structure for the language. If you are familiar with arrays or maps from other programming languages, Lua combines both of these together into tables. Tables store a collection of key, value pairs, and the values can be accessed by their keys. The keys can be numbers or strings. When the keys are contiguous numbers from 1 to N, then the table can be accessed in a similar fashion to an array. They can also be iterated over by index (like an array) or by key (like a map).

*- *[*userdata:*]('https://www.lua.org/pil/2.7.html') Lua represents arbitrary C data as the type ```userdata```. There will be more on this later, but it is important to note that all unevaluated data returned to Lua from MQ is of type userdata.

*- *[*nil*]('https://www.lua.org/pil/2.1.html')*: *NULL, None. nil is Luas representation of no value. One common thing to do is check that a variable is not nil, i.e. the variable has a value. This might look like ```if mob then do_something() end```. This is the same as ```if mob ~= nil then do_something() end```.

*-*[* string*]('https://www.lua.org/pil/2.4.html'): A string is used for data values that are made up of ordered sequences of characters, such as "hello world". I only mention strings here because in macros, everything was a string, and in lua not everything is treated as a string. In Lua, like most programming languages, strings belong inside of quotes. This was not required in macros. For example, ```local name = aquietone``` would fail. ```local name = "aquietone"``` would work.

*- literal: *Defining this word here just to highlight the different between macro script and pretty much any other programming language in the world. A literal would be something like the number 2 or the string "hello world". Specifically for strings, as mentioned a few times throughout this guide, they must be in quotes. This differs from macro script.

*- *[*true/false:*]('https://www.lua.org/pil/2.2.html') One quick note on true/false in Lua, numbers do not behave like booleans in conditions like they do in macros or several other languages. ```if my_int_variable then``` where my_int_variable is 0 would not evaluate to false. If you want to compare numbers in if statements, you need to actually check == or ~= in your conditions.

## 1.2 Hello World
The typical Hello World example for a Lua script is relatively short. No functions need to be written, no variables declared. Simply create a file in  the MQ Lua folder called ```helloworld.lua``` with the following content:

```lua
print('Hello, world')
```

And then execute the script in game by running the command: ```/lua run helloworld```

This script calls the built in Lua ```print``` function to print the string ```Hello, world```. It will print to the MQ console window. The Lua ```print``` function behaves the same way as ```/echo``` in macro script.

## 1.3 Variables
`https://www.lua.org/pil/4.2.html`
Lua can have both local and global variables, similar to a macro. In most cases, variables probably don't need to be made global. Global variables may have some use cases as script grow and begin to include multiple other scripts, but even then they are unlikely to be necessary, and most likely problems can be solved other ways.

To declare a variable, its as simple as:
```lua
-- my_global_var will be a global variable with a value of 1
my_global_var = 1
-- my_local_var will be a local variable with a value of 2
local my_local_var = 2
-- my_string_var will be a local variable which stores the string "test"
local my_string_var = "test"
```

NOTE: ```--``` is used to write comments (text which will not be executed as part of the script) in Lua.

`https://www.lua.org/pil/4.2.html`
Local variables are valid for the block of code in which they are declared in. For example:
```lua
if some_variable > 1 then
    local some_other_variable = 1
end
print(some_other_variable)
```
The above code snippet defines a local variable inside the if block, so it is no longer in scope after the end of the if block. The print statement will output ```nil``` because ```some_other_variable``` is no longer defined.

The entirety of a lua script is also one code block. Local variables defined at the top level of the script can be referenced anywhere else in the script below where they have been defined. However, its always best to define your variables as close as possible to where you will use them, and with as limited scope as possible.

Variables in Lua are not strongly typed, and so you can assign all sorts of values to any variable. For your own sanity, I would not recommend using one variable for multiple different types of data, but there is nothing stopping you from assigning a variable a number value in one line, and then assigning it a string value in the next.

NOTE: As mentioned previously, all string literals in Lua must be in quotes. This is true when assigning string values to variables, as well as for static strings used in comparisons or elsewhere.

The following code snippet shows some macro variable related commands and their lua equivalents:
    
    /declare variable_name type scope value
    
    /declare script_name string local test
    local script_name = 'test'
    
    /declare version int global 1
    version = 1
    
    /varset version 2
    version = 2
    
    /varcalc version ${version}+1
    version = version + 1
    
    /declare nearest_npcspawn local
    /vardata nearest_npc Spawn[npc targetable]
    
    local nearest_npc = nil
    nearest_npc = mq.TLO.Spawn('npc targetable')
    

## 1.4 Output
`https://www.lua.org/pil/1.html` (hello world example, starts with printing text)
In Lua, output text to the console using print:
*Macro:  *```/echo some text```
*Lua:      *```print('Some text')```

print colored text using the same color codes as /echo:
*Macro:  *```/echo \arRed text```
*Lua: *     ```print('\arRed text')```

print the value of a variable:
*Macro:  *```/echo ${script_name}```
*Lua: *     ```print(script_name)```

print the value of a variable with some other text: .. is used to concatenate strings
`https://www.lua.org/pil/3.4.html`
*Macro:  *```/echo Script Name: ${script_name}```
*Lua:      *```print('Script Name: '..script_name)```

another way is to use a formatted string:
*Lua:      *```print(string.format('Script Name: %s', script_name))```
another syntax for formatted strings:
*Lua:      *```print(('Script Name: %s'):format(script_name))```

Also check out Write.lua for debug logging helpers:
`https://www.redguides.com/community/resources/write-lua.2193/`

## 1.5 Functions
`https://www.lua.org/pil/5.html`
Lua functions are the equivalent of macro subroutines. Like variables, functions
can be declared as local or global. In most cases, they don't need to be defined globally.

Example 1: A function which takes no arguments
*Macro:*
    
    Sub echo_my_name
      /echo ${Me.Name}
    /return
    
    Sub Main
      /call echo_my_name
    /return
    

*Lua:*
```lua
local function echo_my_name()
  print(mq.TLO.Me.Name())
end
echo_my_name()
```

Example 2: A function with 1 named argument
*Macro*:
    
    Sub eyecatcher(string message)
      /echo \ar${script_name}: \a-x${message}
    /return
    
    Sub Main
      /call eyecatcher "section about subroutines"
    /return
    

*Lua:*
```lua
-- Define a local function which prints a formatted string with the script name and a message:
local function eyecatcher(message)
  print(string.format('\ar%s: \a-x%s', script_name, message))
end
-- Call the function which we just defined, similar to a macro /call eyecatcher "section about subroutines"
eyecatcher('section about subroutines')
```

Example 3: A function with multiple named arguments
*Macro:*
    
    Sub somefunc(bool arg1, int arg2)
      /echo ${arg1}
      /echo ${arg2}
    /return
    
    Sub Main
      /declare debug bool local true
      /declare id int local ${Me.ID}
      /call somefunc ${debug} ${id}
    /return
    

*Lua:*
```lua
local function somefunc(arg1, arg2)
  print(arg1)
  print(arg2)
end

local debug = true
local id = mq.TLO.Me.ID()
somefunc(debug, id)
```

Example 4: A function with a variable number of arguments: (`https://www.lua.org/pil/5.2.html`)
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


## 1.6 Tables

Before getting into flow control, some knowledge of Lua tables is needed. They will be used in several of the examples.

In lua, tables are the goto data structure for arrays, maps, all sorts of things.
Tables are key/value pairs. The keys can be numbers or strings. They aren't required
to be contiguous numbers, but if using the table as an array, then they will be. Lua array tables start from index 1.

Array table examples: by passing just a set of values, it will automatically give each value an index and treat it as an array

```local priests = { 'clr', 'dru', 'shm' }```
Values can also be indexed explicitly:
```local casters={ [1]='enc', [2]='mag', [3]='nec', [4]='wiz' }```
Lua also provides a table function for appending to arrays:
```lua
local tanks = {}
table.insert(tanks, 'war')
table.insert(tanks, 'pal')
table.insert(tanks, 'shd')
```

To access the values:
```print(priests[2])```
this would print 'dru'

Tables can also be maps instead of arrays:
```local mez_classes = { brd=true, enc=true }```

Look up a values by key:
```lua
print(mez_classes.brd)
print(mez_classes['brd'])
```

While the above examples each just show grabbing a table value directly by index or key, tables will probably more often be accessed
by iterating over the values. This will be covered more in the examples under section 5 on control flow.

Deciding whether a table should be an array or a map depends on the application and how the data will be used. The examples coming up prefer
using tables as maps so that values could be looked up directly by key without having to iterate over the table to find the value.
One approach is to treat the table as a set, where the key is the value you are interested in, and the value is just something like 1 or true.
[Lua Sets]('https://www.lua.org/pil/11.5.html') provides an example helper function to create sets like this.

## 1.7 Command Line Args/Parameters
Lua provides access to command line arguments through the use of the same ```...``` which was introduced earlier with functions for variable number of arguments.

Below is an example which iterates over the arguments which the script is called with:
```lua
local args = {...}
print('Script called with '..#args..' arguments:')
for i,arg in ipairs(args) do
  print(string.format('arg[%d]: %s', i, arg))
end
```
Add this code to a lua script ```testarg1.lua``` and execute it with: ```/lua run testarg1 assist ini server_toon.ini```
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
  print(string.format('Settings[%s]=%s', key, value))
end
```
Add this code to a lua script ```testarg2.lua``` and execute it with: ```/lua run testarg2 role assist ini server_toon.ini```
This would output:
    
    Settings[role]=assist
    Settings[ini]=server_toon.ini
    

## 1.8 Require
The Lua ```require``` function is used to load one Lua file from another. For example, ```Write.lua```, by Knightly, is a library which provides useful functions for logging. Write.lua is meant to be used by other scripts, and would be included with a statement like ```local write = require('write')```. This would then allow a script to call the functions from Write.lua such as ```write.debug('my debug message here')```.
This is similar to include files in macros, though works slightly differently. Include files in macros make the macro behave as if the included files code was all inserted directly where the include was done. In Lua, the results of requiring another Lua file are typically stored into a variable. So, if a script is required, and it returns a table containing several helper functions, then that table is stored into a variable and those functions are accessed through that variable.

Require is also how MQ makes its own functionality available to Lua scripts, such as TLOs, events, bindings and commands which will all be discussed later. In short, its all made available by including the following line:
```lua
local mq = require 'mq'
```
This provides access to all the MQ functionality that has been made available to lua, and assigns it into the variable ```mq```.

A short example using require:
Create your include file, like ```utils.lua```
```lua
-- Create a table which will hold everything we want to be exported from this lua file
local utils = {}

-- Add a function to the utils table under the key "perform_some_task"
utils.perform_some_task = function()
  print('successfully performed some task')
end

-- Return the utils table containing our function
return utils
```

Then include your utils.lua into your main script using a require statement:
```lua
local utils = require 'utils'

utils.perform_some_task()
```

## 1.9 Scope and Processing Order
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
This will print ```nil``` because ```version``` has not been defined ahead of the function ```print_version```, so it will be printing an unknown variable.

```lua
local version = '1.0.0'
local function print_version()
    print(version)
end

print_version()
```
This will print ```1.0.0``` because ```version``` has been defined ahead of the function ```print_version```, so it will be able to find the correct variable.

```lua
local function print_version(version)
    print(version)
end

local version = '1.0.0'
print_version(version)
```
While the second example works, it sort of treats ```version``` like a global variable. You could limit the scope of the ```version``` variable by passing it as an argument to the function instead.

##2. Control Flow
`https://www.lua.org/pil/4.3.html`

A number of options are provided to control the flow of the script, such as if then else, for loops, while loops and repeat until.

##2.1 If then else
`https://www.lua.org/pil/4.3.1.html`

If conditions from macros should look pretty similar in lua.

*Macro:*
    
    /declare my_name string local noone
    /declare max_level int local 115
    /if (${my_name.Equal[noone]}) {
        /echo the values match
    }
    /if (${Me.Level} < ${max_level}) {
        /echo must get more levels
    }
    | In macros, you would usually have to check .ID on something
    /if (${Me.Invulnerable.ID}) {
        /removebuff ${Me.Invulnerable}
    }
    
*Lua:*
```lua
local my_name = 'noone'
local max_level = 115
if my_name == 'noone' then
    print('the values match')
end
if mq.TLO.Me.Level() < max_level then
    print('must get more levels')
end
-- In Lua, you should be able to just check something is not nil, without
-- having to check the ID.
if mq.TLO.Me.Invulnerable() then
    mq.cmdf('/removebuff %s', mq.TLO.Me.Invulnerable())
end
```

*Macro:*
    
    /if (${my_name.NotEqual[someone]}) {
        /echo =~ is not equals in lua
    }
    

*Lua:*
```lua
if my_name ~= 'someone' then
    print('~= is not equals in lua')
end
```

## 2.2 For Loops
`https://www.lua.org/pil/4.3.5.html`

For loops in lua are most often going to be iterating over table values. This is done using either ```pairs``` or ```ipairs```.
Both ```pairs(a_table)``` and ```ipairs(a_table)``` will return 2 values on each pass of the loop, the key and the value for that key.

pairs iterates over all keys in a table (treats the table as a map).
```lua
for class, value in pairs(mez_classes) do
    print(string.format('Class %s can mez: %s', class, value))
end
```

ipairs iterates over contiguous numeric keys in a table starting from index 1 (treats the table as an array).
```lua
for index, value in ipairs(casters) do
    print(string.format('casters[%d]=%s', index, value))
end
```

`https://www.lua.org/pil/4.3.4.html`
You can also just iterate over a range like 1 to N:
```lua
for spellIter=1,5 do
  print(mq.TLO.Me.Book(spellIter).Name())
end
```

Or, an example taken from pocketfarm.mac but changed so it doesn't print a lot of stuff
*Macro:*
    
    /for i 1 to ${SpawnCount[pc targetable]}
      /if (${NearestSpawn[${i},pc targetable].Name.Equal[${Me.Name}]}) {
        /echo ${NearestSpawn[${i},pc targetable].Name.Length}
      }
    /next i
    

*Lua:*
```lua
for i=1,mq.TLO.SpawnCount('pc targetable')() do
  if mq.TLO.NearestSpawn(i..', pc targetable').Name() == mq.TLO.Me.Name() then
    print(mq.TLO.NearestSpawn(i..', pc targetable').Name.Length())
  end
end
```

## 2.3 While Loops
`https://www.lua.org/pil/4.3.2.html`
You could also use a while loop:
```lua
local loop = 1
while loop < 3 do
  print('Loop #'..loop)
  loop = loop + 1
end
```

## 2.4 Repeat Until
`https://www.lua.org/pil/4.3.3.html`
There is also repeat until:
```lua
repeat
  print('Loop #'..loop)
  loop = loop - 1
until loop == 0
```

## 2.5 /goto
Macros often used /goto for flow control. While Lua also has goto, you can probably handle most situations with normal flow control like those described above.

##3. MQ

## 3.1 TLOs
Top Level Objects, or TLOs, are how data is accessed from MQ. This should already be a pretty familiar concept from doing just about anything with MQ, including echoing data to the console, writing conditions in KissAssist INIs, writing macros, writing reacts, etc. We use TLOs every day. Some examples include ```${Me}```, ```${Target}```, ```${Spawn}``` and ```${FindItem}```.

All of the TLOs in MQ are made available to Lua by requiring MQ in your script, like so:
```lua
local mq = require 'mq'
```
This provides access to all the MQ functionality that has been made available to Lua, and assigns it into the variable ```mq```.

To access TLOs using this ```mq``` variable:
```lua
local assist_name = mq.TLO.Group.MainAssist.CleanName()
print(string.format('Assisting: %s', assist_name))
```

```lua
if mq.TLO.Target() then
    local mob_hp = mq.TLO.Target.PctHPs()
    if mob_hp < 98 then
        print(string.format('Assisting on %s', mq.TLO.Target.CleanName()))
        -- call some assist code
    end
end
```

```lua
local target = mq.TLO.Target
if target() then
    if target.Distance3D() > 15 then
        print('Moving closer to target')
        -- call some movement code
    end
end
```

In general, to convert from a TLO in macro format to a TLO in Lua format, just strip the ```${ }``` and add ```mq.TLO.``` on the front. And then, depending on whether you want to evaluate the data to a Lua type yet, add ```()``` on the end. For example, ```${Me.PctHPs}``` becomes ```mq.TLO.Me.PctHPs()```.

A note on () after mq.TLO.*:  `https://www.lua.org/pil/2.7.html`

```lua
print('type(mq.TLO.Me.Name) == '..type(mq.TLO.Me.Name)) -- prints userdata
print('type(mq.TLO.Me.Name()) == '..type(mq.TLO.Me.Name())) -- prints string
```

Data returned by MQ is always of type userdata. Adding () on the end will convert the MQ userdata to the appropriate lua datatype.
```lua
print('type(mq.TLO.Spawn("npc") == '..type(mq.TLO.Spawn("npc")))
-- The following print would throw an error because you cannot concatenate a userdata value to a string
print('mq.TLO.Spawn("npc") == '..mq.TLO.Spawn("npc"))

print('type(mq.TLO.Spawn("npc")() == '..type(mq.TLO.Spawn("npc")()))
print('mq.TLO.Spawn("npc")() == '..mq.TLO.Spawn("npc")())
```

More details on the [MQNext wiki]('https://docs.macroquest.org/lua/')

## 3.2 Commands
You can execute commands EQ and MQ commands from Lua scripts like so:
```lua
mq.cmd('/keypress DUCK')
mq.delay(1000)
mq.cmd('/keypress DUCK')
```

You can also use formatted strings in commands with:
```mq.cmdf('/echo %s', mq.TLO.Me.Name())```

## 3.3 Bindings
Define a function for the bind to call when its executed
```lua
local function bind_help()
  print('some helpful text')
end
```

Assign the function to a command that you can run in game
```lua
mq.bind('/howto', bind_help)
```

## 3.4 Events

First step is to define the function which will be called when your event triggers:
```lua
local function event_handler()
  print('entered event_handler')
end
```

Next, define the event using ```mq.event``` and pass the event name, match text, and the function.
```lua
mq.event('BrokenPole', "#*#You can't fish without a fishing pole, go buy one.#*#", event_handler)
```

Then later, typically in the main run loop of your script, call mq.doevents.
```lua
mq.doevents()
```

## 3.5 Macro ${Select[...]} Statements

Lua doesn't have ```${Select[...]}``` quite like the macro language does, but it has other solutions:

*1. Use a loop and iterate through values:*
Consider a select statement like ```${Select[${Me.Class.ShortName},clr,dru,shm]}```
```lua
local my_class = mq.TLO.Me.Class.ShortName()
for _,class in  ipairs({'clr','dru','shm'}) do
    if my_class == class then
        -- assign something or perform some action based on matching class
    end
end
```

*2. Use logical operators like "or"* (`https://www.lua.org/pil/3.3.html`)
Consider a select statement like ```${Select[${role},pullertank,tank]}```
```lua
local role = 'tank'
if role == 'pullertank' or role == 'tank' then
    -- assign something or perform some action based on matching role
end
```

*3. Use tables by checking for the presence of the value in the table*
Consider a select statement like ```${Select[${Zone.ID},345,344,202,203,279,151,33506]}```
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

## 3.6 Macro /delay
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

## 3.7 Macro Sub Main Function
Lua scripts are processed from top to bottom, and don't actually require code to be inside of a function, unlike how macros always have a Sub Main where execution begins. You can think of the entire lua file itself as the main function, entering at line 1 of the file when you run the script.
There will often times still be blocks of code that perform a similar function to the main subroutine of a macro, like the typical /while or /goto loops people are familiar with from macros.
For example, consider a macro Sub Main like below:
    
    Sub Main
      /while (1) {
        /doevents
        /call check_target
        /delay 10
      }
    /return
    

You might accomplish the same in lua with something like:
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

## 3.8 Macro /call and ${Macro.Return}
Macro subroutines call other subroutines using ```/call my_function "${arg1}"```. Lua functions are just called like ```my_function(arg1)```.
Macro subroutines return results using ```/return ${result}```. Lua functions return similarly, using ```return result```.

Example: The macro Main sub calls subroutine IsPluginLoaded with argument "mq2eqbc". IsPluginLoaded returns the result of the Plugin.IsLoaded TLO Member, which is TRUE or FALSE.
    
    Sub IsPluginLoaded(plugin)
        /if (${Plugin[${plugin}].IsLoaded}) /return TRUE
    /return FALSE
    
    Sub Main
        /call IsPluginLoaded "mq2eqbc"
        /echo ${Macro.Return}
    /return
    

Example: The lua script calls function IsPluginLoaded with argument 'mq2eqbc'. IsPluginLoaded returns the result of the Plugin.IsLoaded TLO Member, which is true or false.
```lua
local function IsPluginLoaded(plugin)
    return mq.TLO.Plugin(plugin).IsLoaded()
end

local eqbcLoaded = IsPluginLoaded('mq2eqbc')
print(eqbcLoaded)
```

## 4. Storage
Lua can support the same storage mechanisms that were used in macros, such as INI files, JSON, YAML, sqlite. The native Lua YAML and JSON implementations I've found aren't particularly great, usually they have some caveats and often don't maintain formatting / pretty printing of files. They may be ok if you never expect users to hand edit the files, but that rarely seems to be the case in MQ.
One new storage method which Lua makes available, is to simply persist Lua tables to a file which can then be loaded using standard Lua calls.

## 4.1 INI
Lua has a library LIP.lua which can be included, which some scripts have already begun using. Buttonmaster, MAUI and a few others each use LIP, but with slight modifications like for supporting a wider variety of keys, such as keys including spaces.
This replaces the need for the INI TLO from MQ. However, it is also still possible to use the INI TLO and /ini command if you really want to.

## 4.2 SQLite
Some Lua scripts available on RG or elsewhere are including an sqlite3 DLL which can be used to connect to an SQLite database. This DLL has been compiled against the version of Lua used in MQ and works well. TradeSkill Construction Set NeXT and the Entropy macro both use this.

## 4.3 Lua Tables
[Several implementations]('http://lua-users.org/wiki/TableSerialization') are available online for persisting Lua tables to a file. Table serialization is also covered in [Programming in Lua.]('https://www.lua.org/pil/contents.html#12')
Most of the implementations include both the writing and reading of tables to and from a file.

## 5. Extras

## 5a. The /lua parse command

MQ provides a command line utility for parsing lua, which is pretty useful for debugging. It automatically includes ```local mq = require('mq')```, and can be used like:

```/lua parse mq.TLO.Me.Name()```

It can do much more than that, including multiple statements strung together, loops, etc. The output gets printed to the console.

```/lua parse i = 1 while mq.TLO.NearestSpawn(i..', pc')() do print(mq.TLO.NearestSpawn(i..', pc')) i=i+1 end```
The above example would print the name of PCs incrementing over a NearestSpawn search.

## 5b. VS Code Extensions

In addition to ColdBlooded's emmylua definitions mentioned at the beginning, some other extensions mentioned often include:
- Rainbow Brackets
- Indent Rainbow
- Vscodemq2
- Codemap

For the codemap extension, you would add a reference to this javascript file (ColdBlooded's handywork again) to the codemap settings.json:
```"codemap.mac": "<location of that file>",  ```
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

## 5c. Mixing Lua and Macro
Macro variables have always been available through the command line while a macro is running. For example, if you were running a macro that created a global variable MainAssistID, then you could /echo ${MainAssistID} and see the value of that variable at any time.
Similarly, you were able to update macro variables with /varset.

Lua variables are not exposed in the same way, regardless of whether they are global or local. One Lua script cannot access variables from another separately running Lua script, or by the lua parse command.

Lua does have access to Macro variables, through ```mq.TLO.Macro.Variable('macro_variable_name')()```. This makes it possible to do something like use Lua to create an ImGui based UI for an existing macro.

## 6. Common Problems

* Comparing values with data from ```mq.TLO.Something```: Due to the difference between userdata and regular lua types like numbers or strings, comparisons will often fail when the value looks like you would expect it to work.

* Example: ```if mq.TLO.Target.CleanName == 'aquietone' then``` This will never succeed because ```mq.TLO.CleanName``` is of type userdata, not string. It needs () on the end to trigger the evaluation from userdata to a lua string, like ```if mq.TLO.Target.CleanName() == 'aquietone'```.
* Example:     if mq.TLO.Target.PctHPs < 90 then``` This will have the same issue, printing ```mq.TLO.Target.PctHPs``` will look like a number, but it is actually userdata, and it needs to be evaluated by adding ().
    
    * Command line argument types for bindings are always going to be passed into the bind function as strings. ```tonumber(variable)``` can be used to convert the type to a number if you wanted to accept a number input to your binding command. If the input can not be parsed to a valid number, then ```tonumber(variable)``` will return ```nil```.
    

