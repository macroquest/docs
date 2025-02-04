---
tags:
    - command
---
# /echo

## Syntax

**/echo** _text_

## Description

Echoes the specified text (or variables) to the MQ Console window.

## Examples

**Colorized usage**

```text
/echo \amThis is a \attest\ax \n\a-gAll done, let's show a backslash: \ar\\
```

**Output:**
<style>
span[style*="#FF00FF"] { color: #FF00FF !important; }
span[style*="#00FF00"] { color: #00FF00 !important; }
span[style*="#FF0000"] { color: #FF0000 !important; }
span[style*="#00FFFF"] { color: #00FFFF !important; }
</style>

<span style="color:#FF00FF">[MQ]</span> <span style="color:#FF00FF">This is a</span> <span style="color:#00FFFF">test</span>  
<span style="color:#009900">All done, let's show a backslash:</span> <span style="color:#FF0000"> \\ </span>

**Variable usage**

```text
/echo My current health percent is ${Me.PctHPs}
```

[MQ] My current health percent is 100

## Color Codes

| Code  | Color          | Code  | Dark Variant       |
|-------|----------------|-------|--------------------|
| `\ab` | Black          | `\a-b`| Black (dark)       |
| `\ag` | Green          | `\a-g`| Green (dark)       |
| `\am` | Magenta        | `\a-m`| Magenta (dark)     |
| `\ao` | Orange         | `\a-o`| Orange (dark)      |
| `\ap` | Purple         | `\a-p`| Purple (dark)      |
| `\ar` | Red            | `\a-r`| Red (dark)         |
| `\at` | Cyan           | `\a-t`| Cyan (dark)        |
| `\au` | Blue           | `\a-u`| Blue (dark)        |
| `\aw` | White          | `\a-w`| White (dark)       |
| `\ay` | Yellow         | `\a-y`| Yellow (dark)      |
| `\ax` | Previous color |       | (Default if none)  |

## Special Codes

| Code | Description                          |
|------|--------------------------------------|
| `\n` | Newline                              |
| `\d` | Down (same as newline, LamahHerder knows not why) |
