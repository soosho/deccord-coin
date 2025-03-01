
Debian
====================
This directory contains files used to package deccordd/deccord-qt
for Debian-based Linux systems. If you compile deccordd/deccord-qt yourself, there are some useful files here.

## deccord: URI support ##


deccord-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install deccord-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your deccord-qt binary to `/usr/bin`
and the `../../share/pixmaps/deccord128.png` to `/usr/share/pixmaps`

deccord-qt.protocol (KDE)

