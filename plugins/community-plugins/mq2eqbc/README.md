# MQ2EQBC

### Description

**MQ2EQBC** \(EQ box chat\) is a plugin composed of two parts, a server \(EQBCS\) and a client \(MQ2EQBC\).

* The server provides a similar service to an IRC server but is much easier to setup.
* The client is similar to the [MQ2IRC](../../discontinued-unsupported/mq2irc/) client in that it monitors text that is sent to the EQBC

  server.

* The main advantage of MQ2EQBC is that it allows remote commands to be sent directly to a single _or_ all connected

  clients.

This plugin was originally written by Omnictrl, with ascii38 and pms providing maintenance for a period. The plugin and server currently have no active maintainer.

The discussion thread regarding this plugin is found in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12147).  
The current client source release is located [here](https://macroquest2.com/phpBB3/viewtopic.php?p=170061#p170061).  
The current compiled server application, which also will compile and run on Linux, can be found at the link in [this post](https://macroquest2.com/phpBB3/viewtopic.php?p=161994#p161994).

For the development history of this plugin see the article [here](mq2eqbc-revisions.md).

### Features

* Allows remote commands via box chat much like mastermind does.
* Allows you to control any connected client anywhere \(ie. someone in your raid needs to afk for a while: they connect

  to your server, you remotely load macros and control their toon as needed until they return\).

* Is mostly compatible with scripts that already support MQ2Irc \(replace '/i say' with '/bc'\).
* Offers private chat \(and private chat channels\) that do not go through EQ servers.
* Optional dedicated UI window for chat output.
* Input typed in dedicated UI window defaults to private '/bc' chat much like EQ's chat window defaults to /say.
* Dedicated UI window supports a configurable keybind for fast private chatting.

### Commands

#### /bccmd

* **/bccmd** connect   

Connect to _server_ on _port_ using _password_ \(defaults: 127.0.0.1 2112\). **Note:** Once you connect, it will remember that connection, so next time you just have to type: _/bccmd connect_

* **/bccmd** forceconnect   

Connect to _server_ on _port_ using _password_ \(defaults: 127.0.0.1 2112\). This differs from _connect_ in that it works while already connected to a server.

* **/bccmd** iniconnect 

Connect to a server by ini key name using information defined in your MQ2EQBC.ini file. Example:

```text
;2100 would be the keyname
[2100]
Server=10.0.0.1
Port=2100

;2150 would be the keyname
[2150]
Server=10.0.0.1
Port=2150
Password=mypassword
```

* **/bccmd** quit

Disconnects from the server

* **/bccmd** help

Show Help

* **/bccmd** status

Show if connected or not

* **/bccmd** reconnect

Close the current connection and connect again

* **/bccmd** names

List everyone that is connected to the server

* **/bccmd** colordump

Show color codes

* **/bccmd** toggle _option_
* **/bccmd** set _option_ \&lt; on \| off &gt;

Toggle or set _option_ on or off. Valid _options_:

:\* **autoconnect**

Auto connect to server when plugin loads

:\* **control**

Allow remote control

:\* **compatmode**

IRC compatibility mode keeps name formatting IRC friendly and echoes outgoing /bct

:\* **reconnect**

Auto-reconnect on server disconnect or zone change

:\* **window**

Use dedicated EQBC UI window

:\* **localecho**

Echoing outgoing commands back if in a channel \(echo is server-driven\)

:\* **tellwatch**

Relay received tells to /bc

**does not support tell windows**

:\* **guildwatch**

Relay guild chat received to /bc

:\* **groupwatch**

Relay group chat received to /bc

:\* **fswatch**

Relay fellowship chat received to /bc

:\* **silentcmd**

Squelch 'CMD: \[command\]' echo

:\* **savebychar**

Saving custom UI window settings to _CharName_ sections of the configuration file \(saves to _Window_ if disabled\)

:\* **silentinccmd**

Squelches incoming eqbc command requests

:\* **silentoutmsg**

Squelches outgoing /bct with compatmode on

:\* **notifycontrol**

Relays a message to /bc if the control option is disabled when a command request is received

:\* **echoall**

Echoes outgoing /bca commands if enabled

* **/bccmd** set reconnectsecs \#

Set the number of seconds to wait until reconnecting \(default 15\)

* **/bccmd** stopreconnect

Stop trying to reconnect for now

* **/bccmd** channels 

Set the list of channels to receive tells from.

* **/bccmd** version

Show plugin version

#### /bc

* **/bc** _your text here_

Send "_your text here_" to the server.

#### /bct

* **/bct** ToonName _your text here_

Send "_your text here_" to _ToonName_

* **/bct** ToonName //command

Send /command to _ToonName_

#### /bca

* **/bca** //command

Send /command to all connected clients, _excluding_ the client you issued the command from.

#### /bcaa

* **/bcaa** //command

Send /command to all connected clients, _including_ the client you issued the command from.

#### /bcfont

* **/bcfont** \#

Sets the font size of the UI window, similar to the [/mqfont](../../../commands/slash-commands/mqfont.md) command

#### /bcmin

* **/bcmin**

Minimizes the UI window, similar to the [/mqmin](../../../commands/slash-commands/mqmin.md) command

#### /bcclear

* **/bcclear**

Clears the buffer of the UI window, similar to the [/mqclear](../../../commands/slash-commands/mqclear.md) command

### Configuration File

The EQBC client will create the configuration file **MQ2EQBC.ini** in your root MQ2 folder.  
An example of this configuration file is as follows:

```text
[Settings]
AllowControl=1
AutoConnect=1
AutoReconnect=1
ReconnectRetrySeconds=15
LocalEcho=0
SaveByCharacter=0
SilentCmd=1
TellWatch=1
GuildWatch=1
GroupWatch=1
FSWatch=1
UseWindow=1
Keybind=.

[Window]
ChatTop=600
ChatBottom=800
ChatLeft=700
ChatRight=1100
Fades=0
Alpha=255
FadeToAlpha=255
Duration=500
Locked=1
Delay=2000
BGType=1
BGTint.red=0
BGTint.green=0
BGTint.blue=0
FontSize=3
UseMyTitle=1
WindowTitle=Custom Title Goes Here With No Quotes

[Last Connect]
Server=10.0.0.1
Port=2112

[Custom1]
Server=10.0.0.1
Port=2115
Password=custompass

[Custom2]
Server=soe.sony.com

[Custom3]
Server=eqbc.google.com
Port=1337
```

* _\*If you wish to use a custom window title you must set_ UseMyTitle _to 1 and change the_ WindowTitle\* line before

  loading the plugin\*\*.

### Top-Level Objects

#### ${EQBC}

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member Name** | **Description** |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Connected** | Client connection status |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Names** | List of connected characters |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Port** | OFFLINE if not connected, port if connected |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **Server** | hostname or IP of server you connected to |
| [_string_](../../../data-types-and-top-level-objects/data-types/datatype-string.md) | **ToonName** | Character name **as seen by EQBC** \(may reflect YouPlayer\) |
| [_bool_](../../../data-types-and-top-level-objects/data-types/datatype-bool.md) | **Setting\[**_**option**_**\]** | Option enabled/disabled status. \(see **/bccmd set** for complete list\) |

### Examples

Sending commands to other toons:

```text
/bct ToonName //sit
/bct ToonName //stand
/bct ToonName //macro ninjalooter
/bct ToonName //endmacro
```

Sending commands to channels:

```text
/bccmd channels chatchan, commands
/bct chatchan hey there guys
/bct commands //bct chatchan My zone: $\{Zone.ShortName}
```

Sending commands to all other connects clients:

```text
/bca //target id ${Me.ID}
/bca //timed 10 /stick 10
```

Sending commands to all clients including yourself:

```text
/bcaa //makecamp return
```

Using noparse to get MQData with bca & bcaa \(one day this will be fixed\):

```text
/noparse /bcaa //bc I am ${Me.PctExp} into ${Me.Level}
```

Taking advantage of escape characters instead of noparse \(only works with _/bct_ at this time\):

```text
/bct Mycleric //bc I am level $\{Me.Level}
```

### EQBCS

EQBCS is a server that can be run as a console application on windows, or as either a foreground application or daemon on a Unix-like system \(tested with Linux and FreeBSD\).

It currently takes the following command line parameters:

* -p  which is the port you want to bind to \(default is 2112, which is dedicated to the Canadian trio Rush\).
* -i

  which is the IP address that you want to the server to listen on if there is more than one network interface in the computer \(default is to listen on all interfaces, which is what you want unless you know otherwise\).

* -l will send all output to rather than to the screen.
* -d will cause the application to run as a deamon process in the background \(UNIX only\).

**Examples:**

```text
C:\> eqbcs              Listens on port 2112
C:\> eqbcs -p 4224      Listens on port 4224
C:\> eqbcs -l log.txt   Listens on port 2112 and sends all server output to the file log.txt.
C:\> eqbcs ftp          Does not work, it does not look up service names to map to port, and the text won't work.
```

#### Compiling EQBCS \(Windows\)

'''This guide for compiling EQBCS for Windows is credited to Tinydru from [this post](https://macroquest2.com/phpBB3/viewtopic.php?p=108811#108811)

## Copy the two parts of the eqbsc post in to a single eqbcs.cpp file \(you can just use Notepad to do this - just

remember to replace the .txt extension with .cpp\).

1. Launch Visual Studio 2005
2. Create a new project. For the project type, select Visual C++ \| Win32 and then Win32 Console Application template.
3. Name the project \(I used eqbcs\). Make sure to pay attention as to where it is creating the directory for the project

   \(so you know where to grab the app files after you build the solution\). Click the OK button after you've given it a

   name.

4. Click the Next button on the first page of the Win32 Application Wizard
5. On the Applications Settings window:
   * Leave the default Application type as "Console application"
   * Uncheck "Precompiled header"
   * Check "Empty project"
6. Click the Finish button
7. Your empty project should now be open. In the Solution Explorer, right click on the "Source Files" folder and select

   Add -&gt; Existing Item from the list.

8. Navigate to the folder where you saved the eqbcs.cpp file you created in step 1 and double click on it \(eqbcs.cpp\).

   This will add eqbcs.cpp to the Source Files folder.

9. In the Solution Explorer, double click on the eqbcs.cpp file - this will open the code in the code window.
10. In the code, find "tempPort = atoi\(argv\[1\]\);" and replace it with "tempPort = atoi\(\(const char \*\)argv\[1\]\);"

    \(this will be on or near line 1983\). Thanks much to Bardomatic for fixing this piece of code.

11. From the File menu, select Save All.
12. From the Build menu, select "Configuration Manager..."
13. In the Active solution configuration: drop down box, select "Release" and then click the Close button.
14. From the Project menu, select eqbcs Properties... \("eqbcs" might be diffent if you named the project something

    else\).

15. In the Configuration: drop down at the top of the Property Pages window, select "Release" from the list.
16. Open the Configuration Properties node \(click on the little +\) and then the Linker node. Now click on "Input" \(found

    beneath "Linker"\).

17. In the right hand window of the Propery Pages window, click on "Additional Dependencies". When you click on that, a

    little box with elipses \(...\) will appear on the right side of the field - click on that. The Additional

    Dependencies window will open.

18. Type wsock32.lib in the text box and then click the OK button.
19. Click the OK button on the Property Pages window.
20. From the File menu, select Save All.
21. From the Build menu, select Build solution. The build \*should\* succeed.
22. You are done - go get your new eqbcs.exe from the Release folder where you created the solution!!

#### Compiling EQBCS \(Windows cmd line\)

'''This guide for compiling EQBCS from the Windows cmd line is credited to dont\_know\_at\_all from [this post](https://macroquest2.com/phpBB3/viewtopic.php?p=145001#145001)

## ctrl-esc Run

1. cmd
2. in the cmd.exe window type the following:
3. c:\Program Files\Microsoft Visual &lt;add your version/path here&gt;/common7/tools/vsvars32.bash
4. cl eqbcs.cpp
5. that's it.

=== Compiling EQBCS \(Linux\) === '''This guide for compiling EQBCS for Linux is credited to ascii38 from [this post](https://macroquest2.com/phpBB3/viewtopic.php?p=144868#144868)

## g++ -fpermissive eqbcs.cpp -o eqbcs

#### EQBCS as a Windows Service

1. Download the \[Windows Resource Kit

   2003\]\([http://www.microsoft.com/downloads/details.aspx?FamilyID=9d467a69-57ff-4ae7-96ee-b18c4790cffd&DisplayLang=en](http://www.microsoft.com/downloads/details.aspx?FamilyID=9d467a69-57ff-4ae7-96ee-b18c4790cffd&DisplayLang=en)\)

2. Run the executable to install the Resource Kit
3. Open up a command prompt and run the following to install a service stub \(\*default install location used in this

   example\*\):

'''You may substitute "EQBC Service" with whatever name you would like to give to the service for display purposes

```text
"C:\Program Files\Windows Resource Kits\Tools\instsrv.exe" "EQBC Service" "C:\Program Files\Windows Resource Kits\Tools\srvany.exe"
```

1. Run **regedit** to edit the Windows registry, and navigate to the following registry key:

   HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\EQBC Service

2. From the **Edit** menu, select **New**, select **Key**, and name the new key **Parameters**
3. Highlight the **Parameters** key
4. From the **Edit** menu, select **New**, select **String Value**, and name the new value **Application**
5. From the **Edit** menu, select **Modify**, and type in the full path name and application name of EQBCS, including

   the drive letter and file extension. You would use the following example if you had the server located in folder

   **MQ2** on your **C:** drive

```text
C:\MQ2\eqbcs.exe
```

1. Now go to _Start_ and _Run_ and type in _services.msc_
2. From here scroll down to _EQBC Service_ \(or whatever name you gave the service above\), right-click and select

   _Properties_

3. On the _General_ tab, change the _Startup type_ to _Automatic_
4. Click the _Start_ button to start your service
5. Select the _Recovery_ tab, and you have the option of changing the drop-down boxes for First-Failure and so on to

   **Restart the service**

6. Select _OK_ and you are finished

#### Problems

* _This application has failed to start because the application configuration is incorrect. Reinstalling this application may fix the problem_

  This is the most common issue with EQBCS failing to run in Windows. Your system is missing runtime libraries. Get both below.

* [2005](http://www.microsoft.com/downloads/details.aspx?familyid=32BC1BEE-A3F9-4C13-9C99-220B62A191EE&displaylang=en)
* [2008](http://www.microsoft.com/downloads/details.aspx?familyid=A5C84275-3B97-4AB7-A40D-3802B2AF5FC2&displaylang=en)

### EQBC Interface

EQBC Interface is an application developed by ieatacid to allow communication with EQBCS outside of the EverQuest game client.  
The discussion thread for this application is found in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?t=15835).  
The most recent release of this application also allows you to view detailed information about characters connected to your server by selecting their name, which will display their statistics on the right-hand side of EQBC Interface. The interval of how often to poll the selected character is configurable by the user so that this information can be very close to real-time.

Jimbob extended the functionality of this program in July 2015. The discussion thread for his fork of the project is found in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?p=169990#p169990).

### See Also

* [Top-Level Objects](../../../data-types-and-top-level-objects/top-level-objects/)
* [Plugins](../../../documentation/macroquest2-plugins.md)
* [MQ2NetHeal](../mq2netheal.md)
* [MQ2NetBots](../mq2netbots.md)
* [MQ2EQBC:Revisions](mq2eqbc-revisions.md)

