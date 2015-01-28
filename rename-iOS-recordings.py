#!/usr/bin/python

#
# Quick script for naming the mp4 files produced by the Voice Memos app on iOS (tested on iOS 8.1.2).
#
# Alex Hunsley 2015-01
#

import sqlite3
import os
import ntpath

print

conn = sqlite3.connect('Recordings.db')
c = conn.cursor()
c.execute("select ZPATH, ZCUSTOMLABEL from ZRECORDING")

res = c.fetchall()

fileNotFoundCount = 0
fileRenamedCount = 0

for (filePath, fileComment) in res:
	filename = ntpath.basename(filePath)
	newFilename = "%s %s.mp4" % (filename[:-4], fileComment)
	print "Renaming %s -> %s" % (filename, newFilename)

	if (os.path.exists(filename)):
		fileRenamedCount += 1
		os.rename(filename, newFilename)
	else:
		fileNotFoundCount += 1
		print "  -- couldn't find input file. Maybe it has already been processed?"

conn.close()

print
print "Finished processing %d files:" % len(res)
print "%d files were successfully renamed." % fileRenamedCount
if (fileNotFoundCount > 0):
	print "%d files could not be found for renaming." % fileNotFoundCount
print

