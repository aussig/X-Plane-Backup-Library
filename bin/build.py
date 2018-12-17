#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Script to create a release
# Copyright (c) 2018 Austin Goudge

import sys
import os
import shutil
import re
import pcrt

# Basic EXPORT matching
exportObjectPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.obj)\s+.*\.obj")
exportPolygonPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.pol)\s+.*\.pol")
exportLinePattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.lin)\s+.*\.lin")
exportFacadePattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.fac)\s+.*\.fac")
exportForestPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.for)\s+.*\.for")
exportStringPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.str)\s+.*\.str")
exportNetworkPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.net)\s+.*\.net")
exportAutogenPointPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.agp)\s+.*\.agp")
exportDecalPattern = re.compile("(?:EXPORT|EXPORT_EXTEND)\s+(.*\.dcl)\s+.*\.dcl")

# Special processing
regionPattern = re.compile("REGION\s+([^\s]+)")

# Ignored items
blankPattern = re.compile("\s+")
silentIgnorePattern = re.compile("(EXPORT_BACKUP|REGION_DEFINE|REGION_BITMAP|REGION_RECT)\s+.*")

def processLibraries(libraryPath, openSceneryX):
    """ Process all the third party libraries and generate backup libraries """

    libraries = os.listdir(libraryPath)
    libraries.sort()

    for item in libraries:
        if (item == "OpenSceneryX" and openSceneryX):
            continue

        inputPath = os.path.join(libraryPath, item, "library.txt")
        outputPath = os.path.join(libraryPath, item, "processed.txt")
        versionPath = os.path.join(libraryPath, item, "version.txt")

        if (not os.path.isfile(inputPath)):
            continue

        handleLibraryFile(inputPath, outputPath, versionPath)


def handleLibraryFile(inputPath, outputPath, versionPath):
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
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.obj\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for polygons (rewrite into output file)
        result = exportPolygonPattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.pol\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for lines (rewrite into output file)
        result = exportLinePattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.lin\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for facades (rewrite into output file)
        result = exportFacadePattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.fac\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for forests (rewrite into output file)
        result = exportForestPattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.for\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for strings (rewrite into output file)
        result = exportStringPattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.str\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for networks (rewrite into output file)
        result = exportNetworkPattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.net\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for autogen points (rewrite into output file)
        result = exportAutogenPointPattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.agp\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
            continue
        
        # Handle EXPORT for decals (rewrite into output file)
        result = exportDecalPattern.match(line)
        if result:
            outputFile.write("EXPORT_BACKUP " + result.group(1) + " opensceneryx/placeholder.dcl\n")
            if (result.group(1)[:4] == "lib/"):
                hasLibExports = True
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
        shutil.copytree(os.path.join(supportPath, "placeholders"), os.path.join(fullBuildPath, "opensceneryx"))
        shutil.copy(os.path.join(supportPath, "readme.txt"), os.path.join(fullBuildPath, "readme.txt"))

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
		pcrt.fg(pcrt.RED)
		print "ERROR: " + message,
		pcrt.fg(pcrt.WHITE)
	elif (type == "warning"):
		pcrt.fg(pcrt.YELLOW)
		print "WARNING: " + message,
		pcrt.fg(pcrt.WHITE)
	elif (type == "note"):
		pcrt.fg(pcrt.CYAN)
		print "NOTE: " + message,
		pcrt.fg(pcrt.WHITE)
	elif (type == "message"):
		pcrt.fg(pcrt.WHITE)
		print message,

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
    version = raw_input("Enter the library version number (e.g. 2.0.0): ")

openSceneryXInput = raw_input("Build For OpenSceneryX? [y/N]: ")
openSceneryX = (openSceneryXInput == "y" or openSceneryXInput == "Y")

processLibraries(libraryPath, openSceneryX)
buildRelease(libraryPath, buildPath, supportPath, version, openSceneryX)