#!/usr/bin/python

# Simple Coursesite submissions filter for graders/TA
# Sam Nguyen - github.com/exfoxz
# Usage: python filter.py list_of_name directory_of_submissions

import sys
import shutil
from os import listdir, getcwd, makedirs
from os.path import isfile, join, exists
import re

thisName = 'filter.py'

if(len(sys.argv) < 3):
	print 'usage: python filter.py list_of_name directory_of_submissions'
	print 'Exiting'
	sys.exit()

listName = sys.argv[1];
sourceFolder = sys.argv[2];
myPath = sourceFolder;
print myPath

exclude = [thisName, listName]
# Get all files in the current folder, except for this and fileName
onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f)) and f not in exclude]

onlyFiles.sort()
# Make a new directory

targetFolder = join(sourceFolder, 'toGrade')
print targetFolder
if not exists(targetFolder):
    makedirs(targetFolder)

notFound = []
counter = 0
f = open(listName, 'r')
for line in f:
	line = line.strip()
	# print line
	tokens = line.split(' ')

	tmp = []
	for a in tokens:
		if (a != ''):
			tmp.append(a)

	name = " ".join(tmp)

	files = [file for file in onlyFiles if file.startswith(name)]
	if(len(files) == 0):
		notFound.append(name)
	else:
		counter = counter + 1;

	for sourceFile in files:
		shutil.copy2(join(sourceFolder, sourceFile), join(targetFolder, sourceFile))

print "{0}/{1} files in '{2}' copied to '{3}' folder.".format(counter, counter + len(notFound), listName, targetFolder)

if(len(notFound) != 0):
	print "CANNNOT find the following {0} files. Please check:".format(len(notFound))
	for f in notFound:
		print f