import os
import sys

def rec(rootdir):
	for root, subFolders, files in os.walk(rootdir):
		print "Current dir - " + root

		for filename in files:
			if filename == "content.txt":
				filePath = os.path.join(root, filename)
				print "Current file - filepath"

				toWrite = ""
			
				f = open( filePath, 'r' )
				toWrite = f.read()
				f.close
				f = open( filePath, 'w' )	
				f.write(toWrite.replace("|check|code|0<_<500|", ""))
				f.close
		
		for folder in subFolders:
			rec(folder)
			
if __name__ == '__main__':
	# rootdir = sys.argv[1]
	rootdir = "/Users/ssullivan/Git/fitnesseroot/FitNesseRoot"
	rec(rootdir)