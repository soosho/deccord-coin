Deccord Core
==========

This is the official reference wallet for Deccord digital currency and comprises the backbone of the Deccord peer-to-peer network. You can [download Deccord Core](https://www.deccord.org/downloads/) or [build it yourself](#building) using the guides below.

Running
---------------------
The following are some helpful notes on how to run Deccord Core on your native platform.

### Unix

Unpack the files into a directory and run:

- `bin/deccord-qt` (GUI) or
- `bin/deccordd` (headless)

### Windows

Unpack the files into a directory, and then run deccord-qt.exe.

### macOS

Drag Deccord Core to your applications folder, and then run Deccord Core.

### Need Help?

* See the [Deccord documentation](https://docs.deccord.org)
for help and more information.
* Ask for help on [Deccord Discord](http://staydeccordy.com)
* Ask for help on the [Deccord Forum](https://www.deccord.com/forum)

Building
---------------------
The following are developer notes on how to build Deccord Core on your native platform. They are not complete guides, but include notes on the necessary libraries, compile flags, etc.

- [Dependencies](dependencies.md)
- [macOS Build Notes](build-osx.md)
- [Unix Build Notes](build-unix.md)
- [Windows Build Notes](build-windows.md)
- [OpenBSD Build Notes](build-openbsd.md)
- [NetBSD Build Notes](build-netbsd.md)
- [Gitian Building Guide](gitian-building.md)

Development
---------------------
The Deccord Core repo's [root README](/README.md) contains relevant information on the development process and automated testing.

- [Developer Notes](developer-notes.md)
- [Productivity Notes](productivity.md)
- [Release Notes](release-notes.md)
- [Release Process](release-process.md)
- Source Code Documentation ***TODO***
- [Translation Process](translation_process.md)
- [Translation Strings Policy](translation_strings_policy.md)
- [JSON-RPC Interface](JSON-RPC-interface.md)
- [Unauthenticated REST Interface](REST-interface.md)
- [Shared Libraries](shared-libraries.md)
- [BIPS](bips.md)
- [Dnsseed Policy](dnsseed-policy.md)
- [Benchmarking](benchmarking.md)

### Resources
* See the [Deccord Developer Documentation](https://deccord.readme.io/)
  for technical specifications and implementation details.
* Discuss on the [Deccord Forum](https://www.deccord.com/forum), in the Development & Technical Discussion board.
* Discuss on [Deccord Discord](http://staydeccordy.com)
* Discuss on [Deccord Developers Discord](http://chat.deccorddevs.org/)

### Miscellaneous
- [Assets Attribution](assets-attribution.md)
- [deccord.conf Configuration File](deccord-conf.md)
- [Files](files.md)
- [Fuzz-testing](fuzzing.md)
- [I2P Support](i2p.md)
- [Init Scripts (systemd/upstart/openrc)](init.md)
- [PSBT support](psbt.md)
- [Reduce Memory](reduce-memory.md)
- [Reduce Traffic](reduce-traffic.md)
- [Tor Support](tor.md)
- [ZMQ](zmq.md)

License
---------------------
Distributed under the [MIT software license](/COPYING).
