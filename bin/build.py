# -*- coding: utf-8 -*-
# Script to create a release
# Copyright (c) 2018 Austin Goudge

import sys
import os
import datetime
import shutil
import re

from colorama import Fore, Style

# Basic EXPORT matching
exportObjectPattern = re.compile("(?:EXPORT)\s+(.*\.obj)\s+.*\.obj")
exportPolygonPattern = re.compile("(?:EXPORT)\s+(.*\.pol)\s+.*\.pol")
exportLinePattern = re.compile("(?:EXPORT)\s+(.*\.lin)\s+.*\.lin")
exportFacadePattern = re.compile("(?:EXPORT)\s+(.*\.fac)\s+.*\.fac")
exportForestPattern = re.compile("(?:EXPORT)\s+(.*\.for)\s+.*\.for")
exportStringPattern = re.compile("(?:EXPORT)\s+(.*\.str)\s+.*\.str")
exportNetworkPattern = re.compile("(?:EXPORT)\s+(.*\.net)\s+.*\.net")
exportAutogenPointPattern = re.compile("(?:EXPORT)\s+(.*\.agp)\s+.*\.agp")
exportDecalPattern = re.compile("(?:EXPORT)\s+(.*\.dcl)\s+.*\.dcl")

# Special processing
regionPattern = re.compile("REGION\s+([^\s]+)")

# Ignored items
blankPattern = re.compile("\s+")
silentIgnorePattern = re.compile("(EXPORT_EXTEND|EXPORT_BACKUP|REGION_DEFINE|REGION_BITMAP|REGION_RECT|REGION_DREF)\s+.*")

# 'lib/' paths to exclude - these should all be existing X-Plane library paths
pathExcludes = re.compile("lib/(airport/aircraft|cars)")

def processLibraries(libraryPath, openSceneryX):
    """ Process all the third party libraries and generate backup libraries """

    libraries = os.listdir(libraryPath)
    libraries.sort()

    for item in libraries:
        if (item == "OpenSceneryX" and openSceneryX):
            continue

        # If we are building for OpenSceneryX, look for a special version of the library. In the case of libraries that have been merged into OSX,
        # allows the OpenSceneryX version to be cut down to just those items that were not merged. Fall back to the normal library.
        if openSceneryX:
            inputPath = os.path.join(libraryPath, item, "library_osx.txt")
            if (not os.path.isfile(inputPath)):
                inputPath = os.path.join(libraryPath, item, "library.txt")
        else:
            inputPath = os.path.join(libraryPath, item, "library.txt")

        if (not os.path.isfile(inputPath)):
            continue

        outputPath = os.path.join(libraryPath, item, "processed.txt")
        versionPath = os.path.join(libraryPath, item, "version.txt")

        handleLibraryFile(inputPath, outputPath, versionPath, openSceneryX)


def handleLibraryFile(inputPath, outputPath, versionPath, openSceneryX):
    """ Parse the contents of a library file, and write out an equivalent backup library """

    displayMessage("Processing " + inputPath + "\n")

    inputFile = open(inputPath)
    outputFile = open(outputPath, "w")
    versionFile = open(versionPath)

    inputFileContents = inputFile.read()
    inputContents = inputFileContents.splitlines()
    inputFile.close()

    versionFileContents = versionFile.read()
    versionContents = versionFileContents.splitlines()
    versionFile.close()

    # Write version info header
    for line in versionContents:
        outputFile.write("# " + line + "\n")

    outputFile.write("\n")

    if openSceneryX:
        placeholderFolder = "opensceneryx"
    else:
        placeholderFolder = "placeholders"

    inRegion = False
    hasLibExports = False

    # Begin parsing
    for line in inputContents:
        # Handle empty lines (ignore)
        if line == "":
            continue

        # Handle OS filetype (ignore)
        if line == "A" or line == "I":
            continue

        # Handle X-Plane version (ignore)
        if line == "800":
            continue

        # Handle LIBRARY (ignore)
        if line == "LIBRARY":
            continue

        # Handle PRIVATE (ignore)
        if line == "PRIVATE":
            continue

        # Handle DEPRECATED (ignore)
        if line == "DEPRECATED":
            continue

        # Handle comments (ignore)
        if line[:1] == "#":
            continue

        # Handle whitespace lines (ignore)
        result = blankPattern.match(line)
        if result:
            continue

        # Handle various ignored patterns (ignore)
        result = silentIgnorePattern.match(line)
        if result:
            continue

        # Handle REGION patterns (ignore everything unless a REGION WORLD is encountered)
        result = regionPattern.match(line)
        if result:
            if (result.group(1).upper() == "WORLD"):
                inRegion = False
                displayMessage("Found REGION: " + result.group(1) + ", enabling EXPORTs\n", "note")
            else:
                inRegion = True
                displayMessage("Found REGION: " + result.group(1) + ", ignoring EXPORTs\n", "note")
            continue

        # If we're in a region, don't do any processing of EXPORTs
        if inRegion:
            continue

        # Handle EXPORT for objects (rewrite into output file)
        result = exportObjectPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to an excluded path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.obj\n")
            continue

        # Handle EXPORT for polygons (rewrite into output file)
        result = exportPolygonPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.pol\n")
            continue

        # Handle EXPORT for lines (rewrite into output file)
        result = exportLinePattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.lin\n")
            continue

        # Handle EXPORT for facades (rewrite into output file)
        result = exportFacadePattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.fac\n")
            continue

        # Handle EXPORT for forests (rewrite into output file)
        result = exportForestPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.for\n")
            continue

        # Handle EXPORT for strings (rewrite into output file)
        result = exportStringPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.str\n")
            continue

        # Handle EXPORT for networks (rewrite into output file)
        result = exportNetworkPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.net\n")
            continue

        # Handle EXPORT for autogen points (rewrite into output file)
        result = exportAutogenPointPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.agp\n")
            continue

        # Handle EXPORT for decals (rewrite into output file)
        result = exportDecalPattern.match(line)
        if result:
            if (pathExcludes.match(result.group(1))):
                # An export to the virtual X-Plane static aircraft path, we don't need to include this as it would just add a blank placeholder into the mix
                continue
            elif (result.group(1).startswith("lib/")):
                # An export to a different lib/ path, include but flag up
                hasLibExports = True
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " " + placeholderFolder + "/placeholder.dcl\n")
            continue

        # Default is to report an issue with the line.
        displayMessage("Unexpected line: " + line + "\n", "error")

    if hasLibExports:
        displayMessage("This library has lib/ paths which may need review\n", "note")

    outputFile.close()


def buildRelease(libraryPath, buildPath, supportPath, version, openSceneryX):
    """ Collate all the built backup libraries into a single library, with supporting files, in a build folder"""

    if openSceneryX:
        fullBuildPath = os.path.join(buildPath, "Backup Scenery Library (for OpenSceneryX) " + version)
        backupLibraryPath = os.path.join(fullBuildPath, "backup_library.txt")
    else:
        fullBuildPath = os.path.join(buildPath, "Backup Scenery Library " + version)
        backupLibraryPath = os.path.join(fullBuildPath, "library.txt")

    if os.path.isdir(fullBuildPath):
        displayMessage("Build path: " + fullBuildPath + " already exists\n", "error")
        return
    else:
        os.makedirs(fullBuildPath)

    if not openSceneryX:
        shutil.copytree(os.path.join(supportPath, "placeholders"), os.path.join(fullBuildPath, "placeholders"))
        shutil.copy(os.path.join(supportPath, "readme.txt"), os.path.join(fullBuildPath, "readme.txt"))
        versionInfoFileHandle = open(os.path.join(fullBuildPath, "version.txt"), "w")
        versionInfoFileHandle.write(version + " " + datetime.datetime.now().strftime("%a, %d %b %Y"))
        versionInfoFileHandle.close()

    backupLibraryFile = open(backupLibraryPath, "w")

    if not openSceneryX:
        backupLibraryFile.write("A\n")
        backupLibraryFile.write("800\n")
        backupLibraryFile.write("LIBRARY\n")
        backupLibraryFile.write("\n")
        backupLibraryFile.write("PRIVATE\n")
        backupLibraryFile.write("\n")

    backupLibraryFile.write("# Backup Library Version: v" + version + "\n")
    backupLibraryFile.write("# https://github.com/aussig/X-Plane-Backup-Library\n")
    backupLibraryFile.write("\n")

    libraries = os.listdir(libraryPath)
    libraries.sort()

    for item in libraries:
        if (item == "OpenSceneryX" and openSceneryX):
            continue

        inputPath = os.path.join(libraryPath, item, "processed.txt")

        if (not os.path.isfile(inputPath)):
            continue

        inputFile = open(inputPath)
        backupLibraryFile.write(inputFile.read())
        backupLibraryFile.write("\n")
        inputFile.close()

    backupLibraryFile.close()


def displayMessage(message, type="message"):
	""" Display a message to the user of a given type (determines message colour) """

	if (type == "error"):
		print(f'{Fore.RED}ERROR: {message}{Style.RESET_ALL}', end='')
	elif (type == "warning"):
		print(f'{Fore.YELLOW}WARNING: {message}{Style.RESET_ALL}', end='')
	elif (type == "note"):
		print(f'{Fore.CYAN}NOTE: {message}{Style.RESET_ALL}', end='')
	elif (type == "message"):
		print(message, end='')

	sys.stdout.flush()


displayMessage("========================\n")
displayMessage("Creating Backup Library\n")
displayMessage("========================\n")

libraryPath = "../libraries"
buildPath = "../builds"
supportPath = "../support"

if not os.path.isdir(libraryPath):
    displayMessage("This script must be run from the 'bin' directory\n", "error")
    sys.exit()

version = ""
while version == "":
    version = input("Enter the library version number (e.g. 2.0.0): ")

openSceneryXInput = input("Build For OpenSceneryX? [y/N]: ")
openSceneryX = (openSceneryXInput == "y" or openSceneryXInput == "Y")

processLibraries(libraryPath, openSceneryX)
buildRelease(libraryPath, buildPath, supportPath, version, openSceneryX)