import sys
import csv
#import queryDB1 from queryDB1
#import queryDB2 from queryDB2
from queryDB3 import queryDB3 
assert len(sys.argv) == 2
inputFileName = sys.argv[1]

actorIdRoot = "actor_id_idx/root.txt"
movieRolesRoot = "movieroles_ma_idx/root.txt"

with open(inputFileName) as inputFile:
  linereader = csv.reader(inputFile, delimiter = "\n")
  for line_ in linereader:
    line = line_[0].split(",")
    [movieIdLow, movieIdHigh, actorIdLow, actorIdHigh] = line
    if movieIdLow == '*':
      movieIdLow = -1
    if actorIdLow == '*':
      actorIdLow = -1
    if movieIdHigh == '*':
      movieIdHigh = sys.maxint
    if actorIdHigh == '*':
      actorIdHigh = sys.maxint

		#queryDB1(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
		#queryDB2(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
    queryDB3(int(movieIdLow), int(movieIdHigh), int(actorIdLow), int(actorIdHigh))
