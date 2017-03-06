#!/usr/bin/python

#
# Quick script for naming the mp4 files produced by the Voice Memos app on iOS (tested on iOS 8.1.2).
#
# Alex Hunsley 2015-01
#

import sqlite3
import os
import ntpath
# import datetime

print

conn = sqlite3.connect('Recordings.db')
c = conn.cursor()
c.execute('select ZPATH, ZCUSTOMLABEL, datetime(ZDATE + 978307200, "unixepoch", "localtime") from ZRECORDING')

res = c.fetchall()

fileNotFoundCount = 0
fileRenamedCount = 0

for (filePath, fileComment, fileDate) in res:
	filename = ntpath.basename(filePath)
	print "%s, %s, %s" % (filename, fileComment, fileDate)
	newFilename = "%s %s.mp4" % (fileComment, fileDate.split(" ")[0])
	print "Renaming %s -> %s" % (filename, newFilename)

	if (os.path.exists(filename)):
		fileRenamedCount += 1
		# print "Skipping %s" % newFilename
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

