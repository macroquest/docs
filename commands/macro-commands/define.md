# Define

### Description

\#define can be used in place of some common variables, but variables are a lot more flexible \(eg. they can be changed within the macro\) and are preferred. One good use of \#define would be to enable or disable debugging information within a macro.

### Use

* **\#define** _replaceme_ replacement

Replaces all occurrences of _replaceme_ with replacement throughout the macro. Example:

`#define Me charactername`

When the macro executes, all occurrences of "Me" will be replaced by "charactername". You can't use variables with

## define \(since they execute before Sub Main\).

### Example

```text
#define DEBUG /echo
Sub Main
  /declare spell string local Complete Healing
  DEBUG I am casting ${spell}
  /call Cast "${spell}" gem1
/return
```

In this situation, DEBUG would be replaced by /echo before the macro started, thereby giving you some information on which spell you were casting.

Changing the **\#define** line to this:

```text
#define DEBUG /squelch /echo
```

Would effectively disable the debugging, since there would be no output to the screen.

Also useful for color coding your echoes. For example:

```text
#define DEBUG "/echo \aw[\arDEBUG\aw]\ax"
Sub Main
  /declare spell string local Complete Healing
  DEBUG I am casting ${spell}
  /call Cast "${spell}" gem1
/return
```

Would allow your debug message to show up with a color coded prefix denoting that this message is from the debug side, and not a standard echo. In this case echoing out:

```text
[DEBUG] I am casting Yaulp
```

Where the brackets are white, the word debug is red, and the text is your default color.

### See Also

* [Pound\_Commands](pound-commands/)
* [Macro\_Reference](../../documentation/macro-reference.md)

