# Anonymize

## Reason for Existence
MQ2Anonymize has the singular purpose of filtering text displayed to the user. It is mostly useful in streaming/recording applications with the hope that any identifying information is not visible to others. This, of course, is an intractable problem so the best that we can do is filter _words_ and hope it works. It is by no means a perfect safety tool and if the user cares about anonymity, should be used _in service_ of supporting a larger anonymization strategy.

## Word of Warning
This plugin will only filter **in game**. What that means is that any text at server select, character select, login, etc ***will not be filtered***. Please make any considerations necessary to prevent visibility of the client outside of actual in-game experiences.

## How Your Plugin Can Anonymize
MQ2Anonymize cannot control what plugin authors do, so instead we provide the API to anonymize any text that the plugin may render _if anonymization is turned on_. We are able to anonymize central points of text display (such as writing the the MQ2 console with `WriteChatColor` and variants of it), but anything that renders text outside those plugins will need to have explicit API calls to `Anonymize()`. For plugin authors: when in doubt make sure to test that anonymization works in game with your plugin before releasing it!

### API
The API is very simple: `CXStr& Anonymize(CXStr& Text)`
The signature is such that it satisfies 2 things: can be linked via C-style linkage for use externally, and can be called in-line. The function uses `Text` as a buffer and returns it as a result. This means that the plugin writer will need to allocate the `CXStr` passed to the appropriate scope (usually on the stack is fine), but since it's not a c-string, we don't need to support `MAX_STRING` allocations on the stack anymore. This also has the advantage of using EQ's native string class (`CXStr`) so it should be very easy to integrate.

### Example
```cpp
CXStr text(text_to_anonymize);
text = Anonymize(text);
```

## End-User Instructions
In order to enable anonymization, the end-user (player) needs to do some setup. Turning it on and off is simple: `/mqanon` will simply toggle the active state of anonymization. All interaction with this functionality is done with arguments to this command, here is a brief summary.

**Important Note:** Due to the quirky nature of how EQ sets bone sprite text, we have implemented anon into the captions code. If you want name sprites to anonymize, you _must_ turn captions on with `/caption MQCaptions on`!

### Command Reference
 - no arguments: toggle on/off state of anonymization
 - `/mqanon asterisk <name>`
   - add a filter for `name` and replace it with asterisks
 - `/mqanon class <name>`
   - add a filter for `name` and replace it with class information
 - `/mqanon custom <name> <text>`
   - add a filter for `name` and replace it with custom `text`
 - `/mqanon drop <name>`
   - remove the filter for `name`
 - `/mqanon alias <name> <alternate>`
   - add an alternate for `name`
   - will use the same replacement strategy as `name`
 - `/mqanon unalias [name] <alternate>`
   - remove an alternate from `name`
   - specifying the name is optional here
 - `/mqanon me [asterisk|class|me|none]`
   - set self anonymization to strategy
   - if no argument is specified, will use the `me` strategy
 - `/mqanon group <asterisk|class|none>`
   - set group anonymization to strategy
 - `/mqanon fellowship <asterisk|class|none>`
   - set fellowship anonymization to strategy
 - `/mqanon guild <asterisk|class|none>`
   - set guild anonymization to strategy
 - `/mqanon raid <asterisk|class|none>`
   - set raid anonymization to strategy
 - `/mqanon save`
   - save the current configuration
 - `/mqanon load`
   - load the configuration from file
   - for use when editing the config externally
 - `/mqanon [command] -h` or `/mqanon [command] --help`
   - display help
   - commands that take arguments also allow this switch

### Replacement Priority
Since the same character can exist in multiple groupings (guild/group/raid, etc) and each grouping can have a separate strategy, there is a defined order in which text replacing is done. That means that a name that exists in multiple groupings will use the highest priority replacement strategy. The priority is as follows:
1) Custom
2) Self
3) Group
4) Guild
5) Raid

### Replacement Strategies
There are some pre-built strategies that are commonly used (as seen in the command reference):
 - asterisk
   - replaces the middle characters in the name with asterisks
   - `Myname` becomes `M****e`
 - class
   {% raw %}
   - replaces the name with `"[${{Spawn[pc {0}].Level}}] ${{Spawn[pc {0}].Race}} ${{Spawn[pc {0}].Class}} ${{Spawn[pc {0}].Type}}"`
   {% endraw %}
   - note that this assumes a pc
 - me
   {% raw %}
   - replaces the name with `"[${Me.Level}] ${Me.Race} ${Me.Class} ${Me.Type}"`
   {% endraw %}
   - only appropriate when anonymizing the client's character
 - where
   - this keyword allows completely generic anonymization
   - the string will be processed as macro text _at the time of replacement_
