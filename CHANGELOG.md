# Release Notes

## vx.x.x - xxxx-xx-xx

* Updated Helipad Markings Library to v1.1.0
* Added HeliSimuFrance Library
* Added Headwind Radio Tower Library
* Added Headwind Water Tower Library
* Added Mountain Helipads Library
* Updated CCVA Library to 2.11
* Updated ALES Library to v1.1.3
* Added Canada4XP Static Aircraft Library
* Added Devinci Library

## v3.0.0 - 2020-05-28

* Some library authors are not careful about supporting old paths in their libraries, so when they release a new version it can cause errors. So from this release of the Backup Library onwards we now track historical versions of libraries too, and include all paths that have ever been seen in a library's history.
* Updated NAPS Library to v7.2
* Updated and renamed EMWINGS Catering Trucks Library to EMWINGS Ground Services Library v1.2
* Updated Handy Objects Library to v7.70
* Updated Parking Stands and Signs Library to v6.0
* Updated PuF Library to v1.0.1
* Updated x_Prefab Library to v8.0
* Updated CCVA Library to v2.8.0
* SAM Seasons SDK now merged into SAM library 2.0.3
* Added Helipad Markings Library

## v2.8.0 - 2020-04-07

* Updated EMWINGS Catering Trucks Library to v1.1
* Updated OpenSceneryX Library to v4.4.0
* Updated SAM Library to v2.0.3
* Updated SAM Seasons SDK Library

## v2.7.0 - 2020-02-18

* Added Static and Animated Aircraft Library
* Added SAM Seasons SDK Library
* Added EMWINGS Catering Trucks Library
* Updated SAM Library to v2.0.1

## v2.6.0 - 2019-12-04

* Updated NAPS Library to v7.0
* Updated CCVA Library to v2.7
* Updated OpenSceneryX Library to v4.3.0
* Updated DT Library to v1.5.2
* Updated FlyAgi Vegetation Library
* Build process now automatically removes any duplicate lines, making the library smaller.
* Build process now includes `EXPORT_EXCLUDE` entries, for libraries which include `REGION`s but have `EXPORT_EXCLUDE`s without corresponding `EXPORT`s for some items (e.g. FlyAgi Vegetation).

## v2.5.0 - 2019-09-03

* Added x_Prefab Library
* Added SAM (Scenery Animation Manager) Library
* Added ALES Developer Library
* Added Greek Houses and Buildings Library
* Added OB_SAV (South American Vegetation) Library
* Updated OpenSceneryX Library to v4.2.0
* Updated NAPS Library to v6.7

## v2.4.0 - 2019-04-14

* Added PuF Library
* Updated OpenSceneryX Library to v4.0.0
* Updated Handy Objects Library to v7.50
* Updated CCVA Library to v2.1.0
* Updated NAPS Library to v6.5
* Updated DT Library to v1.5.1
* We now include any items found within a `REGION`. This allows us to provide backups for items that only appear in some parts of the world or in other specific circumstances.

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
* Now include a `version.txt` file containing the version number and date, for utilities such as xOrganiser to use.
* Fix a UTF-8 encoding issue with the PM Library - meant it was missing a Forklift Truck object
* No longer include `EXPORT_EXTEND` lines - most of these are `lib/` entries so ignored anyway, and the rest should be extending existing paths so don't need backups. This was causing problems with libraries such as RuScenery, which use `EXPORT_EXTEND` to publish some of their objects to paths that don't already exist. This is an undocumented thing to do, and using the backup library with RuScenery and the optional visible placeholders would cause some objects to appear as red squares instead of the correct model.
* Updated NAPS library to v6.3

## v2.0.0 - 2018-12-27

* Now maintained by [aussi](https://forums.x-plane.org/index.php?/profile/2431-aussi/)
* Now includes 46 libraries, up from 12. The latest list of supported libraries is [always available here](https://github.com/aussig/X-Plane-Backup-Library/tree/master/libraries)
* Implemented a Python project to build the library automatically, hosted on [GitHub](https://github.com/aussig/X-Plane-Backup-Library) for futureproofing against abandonware
* Placeholder path is now `placeholders/` rather than `opensceneryx/` to avoid confusion
* Exports to built-in X-Plane® library paths (e.g. `lib/airport/aircraft`) are excluded - these are virtual paths that X-Plane® uses for e.g. placing static aircraft and adding blank placeholders to them is not appropriate

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