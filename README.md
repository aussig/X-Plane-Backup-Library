# X-Plane® Backup Library

## Introduction
This is a placeholder shim library for all the major X-Plane® third party scenery libraries.

It is based on ideas and work by [Chris K](https://forums.x-plane.org/index.php?/profile/45106-chris-k/) and subsequently [Richard Elliott](https://forums.x-plane.org/index.php?/profile/389608-einstein/).

- Tired of facade/forest/beach crashes?
- Get annoyed at missing a particular object in a 3rd party scenery?
- Can't find the library online, or the library has disappeared from x-plane.org downloads?

There is a solution!

This file creates a "backup" shim library for all of the well known and well used public libraries in X-Plane®. This file will allow you to load most sceneries which reference 3rd party libraries, even though you may not have the library installed. It will prevent X-Plane® from crashing out if it cannot find the library.

To see which libraries are included, take a look at [this folder listing](https://github.com/aussig/X-Plane-Backup-Library/blob/master/libraries).

## End user Installation

As an end-user of X-Plane®, simply unzip the backup library into your `X-Plane/Custom Scenery/` folder.

## Notes

This package does not include any actual objects. It does not replace actually having the true library. It will simply insert a blank object or art asset in case you do not have the actual library, and thus prevent X-Plane® from crashing and allow scenery to load without error.

This file also does not interfere if you have the actual library. X-Plane® will simply ignore this file if you happen to have the actual library.

## For Scenery Developers
 
I highly suggest (and freely encourage) all of you to include this in any scenery you produce for the end-user. This way, if you reference any of the above libraries, and your end-user does not have it installed, your scenery will still work without errors. As scenery developers, we have an obligation to the end-user to make our scenery as easy and painless as possible to install and use.
 
This works the same as the OpensceneryX shim library. However, since many of the other libraries never included their own 'ready to use' shim library for developer distribution, it wasn't easy to add. Now, you have an "easy button". Please consider using this, and it will make your users happy.

## Building

The library is built by running `create.py` from within the `bin` folder. It trawls the `libraries` folder, expecting one subfolder per 3rd party library, containing a `library.txt` file and a `version.txt` file. If a library is updated, update these files and rebuild.

It outputs a folder into `builds` which includes the version number.

## Distribution

The library is distributed by zipping the built version folder and uploading to x-plane.org.

