import sys
import csv
#import queryDB1 from queryDB1
#import queryDB2 from queryDB2
#import queryDB3 from queryDB3

assert len(sys.argv) == 2
inputFileName = sys.argv[1]

actorIdRoot = "actor_id_idx/root.txt"
movieRolesRoot = "movieroles_ma_idx.txt"

with open inputFileName as inputFile:
	linereader = csv.reader(inputFile, delimiter = "\n")
	for line_ in linereader:
		line = line_[0].split(",")
		[movieIdLow, movieIdHigh, actorIdLow, actorIdHigh] = line
		#queryDB1(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
		#queryDB2(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
		#queryDB3(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)