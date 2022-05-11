# /exec

## Syntax

```text
/exec command ["parameters" | bg] [bg]
```

## Description

Executes the specified command as if from the command line.  If parameters are passed in, it will execute those parameters.  If "bg" is passed as either the second or third parameter, it will execute the program in the background, otherwise it executes in the foreground.

The Application Paths section in the MacroQuest.ini file allows you to specify aliases for applications, but it's not necessary for usage.

## Ini Example

MacroQuest.ini
```ini
[Application Paths]
vscode="C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
```

## Examples

Shutdown the computer:
```text
/exec shutdown /s
```
Force shutdown the computer:
```text
/exec shutdown "/s /f"
```
Open Notepad in the background:
```text
/exec notepad bg
```

Open your MacroQuest.ini file in Visual Studio Code when using the above ini:
```text
/exec vscode "${MacroQuest.Path[mqini]}"
```

Or the same thing if vscode is just in your path, with no ini:
```text
/exec code "${MacroQuest.Path[mqini]}"
```


