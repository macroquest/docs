## Description

This plugin adds a telnet server, which can be used to access your EQ session remotely.

### INI File

By default, the telnet server is disabled. If you want to use it, you will need to edit the mq2telnet.ini file and do
the following:

-   Define a port number that the server will run on:

<!-- -->

    Port=6669

-   Add some users and passwords under the \[Users\] section:

<!-- -->

    [Users]
    wassup=ubahmanualguy

-   It is recommended that you change the **Welcome** message.
-   The following setting will limit the connection to just one user. Setting it to 0 and defining usernames and
    passwords will allow multiple users to connect.

<!-- -->

    LocalOnly=1

### Using the Telnet server

-   Use a real telnet client to connect (Putty works well).
-   After entering your username and password, you will be presented with your Welcome message.
-   From now, and commands you enter in the telnet session will work the same as typing them into your EQ console.
-   Any chat output will be sent to your telnet session.

To disconnect from the server, just close your telnet client. The plugin will notice when the connection is no longer
active and will clean up.

## Commands

-   [/telnet](../commands/telnet.md)

## See Also

-   [Data Types](../data-types/data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Plugins](../documentation/macroquest2-plugins.md)


