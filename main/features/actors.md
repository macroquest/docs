# Actors

## Purpose
Actors are a system designed to facilitate simple yet powerful inter-client communication. The underlying technology for local (same computer) communication is Windows Named Pipes, and is very fast -- essentially no different than just using shared memory. Remote communication is ASIO-based TCP communication with a planned UDP discovery mechanism and the ability to specify peers (discovery is still WIP). This provides a system that can connect clients across computers in a network and multiple clients on a local machine simultaneously only opening the minimum number of ports. There is no server in this system, it's peer to peer, but to facilitate local pipe and socket management, the launcher is used as a router on each computer connected to the peer network.

## How to Use
Documentation for the following systems exist in their respective places:

- [Plugins](../../plugins/developing/actors.md)
- [Lua](../../lua/actors.md)

Outside of these two interfaces, it is possible to connect to actors from external applications. It would be similar to how a plugin does it, but it is out of the scope of this documentation.

The entire system hinges on the launcher (MacroQuest.exe) being present as the central routing mechanism. If the launcher goes down, then all routing will stop and the system will become inoperable.

While messaging can use any serialization for internal mailbox communication, protobuf has been utilized to wrap these messages in routing packages to allow for system-independent communication, implicit versioning, and efficient marshalling/unmarshalling. When selecting a serialization strategy, be aware that there are protobuf examples in code and you are probably already building the library.

The point of using this technology is to allow for consistent and simple communication between processes that couldn't communicate before. The framework is ideally highly extensible with a minimum amount of boilerplate needed to set up, feedback is welcome.

## Terminology

- **Actor**: An actor is self-contained computational entity that receives messages and performs actions based on the content of those messages such as side effects and composing replies.
- **Mailbox**: This is the receiver of messages. Each actor has exactly one, and this provides the unique address for said actor. A mailbox is set up by taking a callback function to process a message.
- **Dropbox**: This is the sender of messages. Each actor again has exactly one, and this provides automatic return address composition as well as an interface to the application's central Post Office.
- **Post Office**: The central authority for message routing in a single application. Each independent application will need to set one post office up for actors in that application to register mailboxes. This will maintain ownership of the mailboxes and dropboxes and route all messages received by the application.
- **Address**: A specifier for routing a message. On the sending side, this does not have to be unique -- one could address a message to all applications that have a certain mailbox, for instance. There are two levels of addressing: mailbox, and postoffice. On the receiving side, the post office must be fully qualified with one of three strategies:
    - By name: You can specify a unique name for an application, which is useful for external application naming. There is one name-specified application that should always be present: `launcher` -- the MQ launcher
    - By pid: You can use the PID of the application (not very useful to the sender as it is not deterministic)
    - By EQ information: The most available of the following three strings: account, server, character. All three of these strings present means that the address must be unique, and this type of addressing replaces name as a convenience mechanism.
- **Envelope**: This is a protobuf spec that all messages that need to be routed to actors will get wrapped in automatically (as a function of using the Dropbox) so the routing system can ensure it ends up at the correct post offices and mailboxes.

## Configuration
There are two configurations available in [MacroQuest.ini](../macroquest.ini.md) for actors, both dealing with networking. The goal was to keep configuration minimal, but there was need for some slight configuration.

In the \[MacroQuest\] section, there is an optional setting `NetworkPeerPort` that lets the user designate the port that the launcher will bind to in order to perform networking peer operations. In most cases, this does not need to be set and the default port of 7781 is fine. Set it if that port is used by another program.

The other setting is a complete section in the ini: \[NetworkPeers\]. The entries of this section are simply `host=port`, where a `port` value of 0 just tells MQ to use the default value of port for the peer (set by `NetworkPeerPort` above). An example of this section is as follows:

!!!example "[NetworkPeers]"
    ```
    [NetworkPeers]
    192.168.4.5=0
    192.168.4.6=8177
    ```

Where the launcher at the `192.168.4.5` host uses the default port (usually 7781) and the one at `192.168.4.6` has started with the special port of 8177, so we need to tell our local launcher to connect on that port instead. Currently, only IPv4 hosts are supported.