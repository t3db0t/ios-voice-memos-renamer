# ios-voice-memos-renamer
Applies your voice memo names (as set on iOS) to the mp4 files themselves

If, like me, you usually transfer voice memos from iOS to your desktop using something like iFunbox, you 
end up with a load of mp4 files that are missing the titles you set in iOS. This little Python script pulls the recording names out of the sqlite3 database that iOS uses and renames your files.

To use:

1) transfer all the mp4s files and the Recordings.db* files (usually three of them) to a single directory on your desktop (I use iFunbox for this)
2) run the script 

The .waveform and .composition files aren't needed.
