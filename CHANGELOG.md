# Release Notes

## vx.x.x - xxxx-xx-xx

* Updated OpenSceneryX to v4.0.0

## v2.3.0 - 2019-03-26

* Added OB Library
* Added Clock Tower Library
* Added RAF Towers Library
* Updated DT Library to v1.4
* Updated NAPS Library to v6.4
* Updated CCVA Library to v2.0.0
* Updated Handy Objects Library to v7.2

## v2.2.0 - 2019-02-14

* Updated CCVA Library to v1.10.0
* Updated OpenSceneryX Library to v3.2.0
* Updated Handy Objects Library to v7.0
* Updated DT Library to v1.3

## v2.1.0 - 2019-01-20

* Added DT Library
* Now include a <tt>version.txt</tt> file containing the version number and date, for utilities such as xOrganiser to use.
* Fix a UTF-8 encoding issue with the PM Library - meant it was missing a Forklift Truck object
* No longer include <tt>EXPORT_EXTEND</tt> lines - most of these are <tt>lib/</tt> entries so ignored anyway, and the rest should be extending existing paths so don't need backups. This was causing problems with libraries such as RuScenery, which use <tt>EXPORT_EXTEND</tt> to publish some of their objects to paths that don't already exist. This is an undocumented thing to do, and using the backup library with RuScenery and the optional visible placeholders would cause some objects to appear as red squares instead of the correct model.
* Updated NAPS library to v6.3

## v2.0.0 - 2018-12-27

* Now maintained by [aussi](https://forums.x-plane.org/index.php?/profile/2431-aussi/)
* Now includes 46 libraries, up from 12. The latest list of supported libraries is [always available here](https://github.com/aussig/X-Plane-Backup-Library/tree/master/libraries)
* Implemented a Python project to build the library automatically, hosted on [GitHub](https://github.com/aussig/X-Plane-Backup-Library) for futureproofing against abandonware
* Placeholder path is now `placeholders/` rather than `opensceneryx/` to avoid confusion
* Exports to built-in X-Plane® library paths (e.g. lib/airport/aircraft) are excluded - these are virtual paths that X-Plane® uses for e.g. placing static aircraft and adding blank placeholders to them is not appropriate

## v1.7 - 2015-04-25

* Now maintained by [einstein](https://forums.x-plane.org/index.php?/profile/389608-einstein/)
* Updated Handy Objects Library to v3.3

## v1.6

* Updated World Models Library to v7.1.0

## v1.5

* Updated RE Library
* Updated Handy Objects Library
* Updated OpenSceneryX Library
* Added 3D People Library

## v1.4 - 2015-02-01

* Added another 80 objects from RE Library v1.5 (einstein)

## v1.3 - 2015-01-10

* Updated RE Library

## v1.2 - 2014-12-13

* Fixed .STR placeholder
* Updated RE Library
* Marked library as PRIVATE so it doesnt show up in WED/OE as a usable art asset.

## v1.1 - 2014-12-02

* Added Madagascar Library

## v1.0 - 2014-12-01

* Initial release