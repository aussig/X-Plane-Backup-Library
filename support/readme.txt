X-Plane® Backup Library
=======================

Currently maintained and supported by aussi (https://forums.x-plane.org/index.php?/profile/2431-aussi/)

Introduction
------------

This is a placeholder shim library for all the major X-Plane® third party scenery libraries.

It is based on ideas and work by Chris K (https://forums.x-plane.org/index.php?/profile/45106-chris-k/) and subsequently Richard Elliott (https://forums.x-plane.org/index.php?/profile/389608-einstein/).

- Tired of facade/forest/beach crashes?
- Get annoyed at missing a particular object in a 3rd party scenery?
- Can't find the library online, or the library has disappeared from x-plane.org downloads?

There is a solution!

This file creates a "backup" shim library for all of the known public libraries in X-Plane®. This file will allow you to load most sceneries which reference 3rd party libraries, even though you may not have the library installed. It will prevent X-Plane® from throwing an error (and in older versions of X-Plane®, quitting) if it cannot find the library.

To see which libraries are included, take a look at this folder listing: https://github.com/aussig/X-Plane-Backup-Library/blob/master/libraries.


End user Installation
---------------------

As an end-user of X-Plane®, simply unzip the backup library into your `X-Plane/Custom Scenery/` folder.


Notes
-----

This package does not include any actual objects. It does not replace actually having the true library. It will simply insert a blank object or art asset in case you do not have the actual library, and thus allowing scenery to load without error.

This file also does not interfere if you have the actual library. X-Plane® will simply ignore this file if you have the real library installed.


For Scenery Developers
----------------------

I highly suggest (and freely encourage) all of you to include this in any scenery you produce for the end-user. This way, if you reference any of the above libraries, and your end-user does not have it installed, your scenery will still work without errors. As scenery developers, we have an obligation to the end-user to make our scenery as easy and painless as possible to install and use.
 
This works the same as the OpenSceneryX shim library. However, since many of the other libraries never included their own 'ready to use' shim library for developer distribution, it wasn't easy to add. Now, you have an "easy button". Please consider using this, and it will make your users happy.

Note: If you include this Backup Library in your scenery package, you don't also need to include the OpenSceneryX Placeholder from the OpenSceneryX Developer Pack: https://www.opensceneryx.com/support/scenery-developers/.


Missing libraries
-----------------

If you find a library that isn't included, please get in touch - either create an issue in the GitHub project: https://github.com/aussig/X-Plane-Backup-Library/issues or contact me on x-plane.org: https://forums.x-plane.org/index.php?/profile/2431-aussi/