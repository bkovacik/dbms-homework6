import sys
import csv
#import queryDB1 from queryDB1
#import queryDB2 from queryDB2
#import queryDB3 from queryDB3

assert len(sys.argv) == 2
inputFileName = sys.argv[1]

with open inputFileName as inputFile:
	linereader = csv.reader(inputFile, delimiter = "\n")
	for line_ in linereader:
		line = line_[0].split(",")
		[movieIdLow, movieIdHigh, actorIdLow, actorIdHigh] = line
		#queryDB1(root, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
		#queryDB2(root, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
		#queryDB3(root, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)