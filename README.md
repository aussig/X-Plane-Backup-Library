# X-Plane® Backup Library

## Introduction

This is a placeholder shim library for all known X-Plane® third party scenery libraries.

It is based on ideas and work by [Chris K](https://forums.x-plane.org/index.php?/profile/45106-chris-k/) and subsequently [Richard Elliott](https://forums.x-plane.org/index.php?/profile/389608-einstein/).

- Tired of facade/forest/beach warnings?
- Get annoyed at missing a particular object in a 3rd party scenery?
- Can't find the library online, or the library has disappeared from x-plane.org downloads?

There is a solution!

This file creates a "backup" shim library for all of the known public libraries in X-Plane®. This file will allow you to load most sceneries which reference 3rd party libraries, even though you may not have the library installed. It will prevent X-Plane® from throwing an error (and in older versions of X-Plane®, quitting) if it cannot find the library.

To see which libraries are included, take a look at [this folder listing](https://github.com/aussig/X-Plane-Backup-Library/blob/master/libraries).

## End user Installation

As an end-user of X-Plane®, simply unzip the backup library into your `X-Plane/Custom Scenery/` folder.

## Notes

This package does not include any actual objects. It does not replace actually having the true library. It will simply insert a blank object or art asset in case you do not have the actual library, and thus allowing scenery to load without error.

This file also does not interfere if you have the actual library. X-Plane® will simply ignore this file if you have the real library installed.

## For Scenery Developers

Feel free to include this in any scenery you produce for the end-user. 

This works the same as the [OpenSceneryX](https://www.opensceneryx.com) shim library. However, since many of the other libraries never included their own 'ready to use' shim library for developer distribution, it wasn't easy to add. Now, you have an "easy button".

_Note: If you include this Backup Library in your scenery package, you don't also need to include the OpenSceneryX Placeholder from the [OpenSceneryX Developer Pack](https://www.opensceneryx.com/support/scenery-developers/)._

## Building

The library is built by running `python3 build.py` from within the `bin` folder. It trawls the `libraries` folder, expecting one subfolder per 3rd party library, containing a `library.txt` file and a `version.txt` file. In addition, it looks for an optional `versions` subfolder and scans that for previous versions of the library. 

It outputs a folder into `builds` which includes the version number.

_Note: There is also an option to build 'For OpenSceneryX', which should only be used by the maintainer of the [OpenSceneryX Library](https://github.com/OpenSceneryX/Library). Using this option produces a text file rather than a library file, which is ready for inclusion in an OpenSceneryX build, omits OpenSceneryX itself, and uses special OpenSceneryX-specific versions for libraries that are partially or fully integrated into OpenSceneryX._

## Adding and Updating Libraries

### To Add a Library

1. Create a new subfolder in the `libraries` folder with a suitable name.
2. Create a `version.txt` file in the new library folder (copy one from another library) and update the details, including the author and a URL to the original library.
3. Put the `library.txt` file into the new library folder.
4. Update `CHANGELOG.md`.

### To Update a Library

1. Locate the existing library folder inside the `libraries` folder.
2. Move the previous `library.txt` found in the existing library folder into the `versions` subfolder (create the subfolder if it doesn't already exist). Rename this old `library.txt` with the previous version number.
2. Put the new `library.txt` into the existing library folder.
3. Update the `version.txt` file, found in the existing library folder, with the new version number.
4. Update `CHANGELOG.md`.

## Distribution

The library is distributed by zipping the built version folder and uploading to the [Downloads page on x-plane.org](https://forums.x-plane.org/index.php?/files/file/25033-backup-scenery-library/). Also create a [Release](https://github.com/aussig/X-Plane-Backup-Library/releases) here on GitHub, include the latest changes from the `CHANGELOG` in the description and upload the zip to the release.

## Missing libraries

If you find a library that isn't included, please get in touch - either [create an issue in the GitHub project](https://github.com/aussig/X-Plane-Backup-Library/issues) or [contact me on x-plane.org](https://forums.x-plane.org/index.php?/profile/2431-aussi/).
