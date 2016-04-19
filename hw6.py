import sys
import csv
from queryDB1 import queryDB1
import os
from queryDB3 import queryDB3 
assert len(sys.argv) == 2
inputFileName = sys.argv[1]

actorIdRoot = "actor_id_idx/root.txt"
movieRolesRoot = "movieroles_ma_idx/root.txt"

with open(inputFileName) as inputFile:
  for line in inputFile:
    print ""
    print line
    line = line.rstrip().split(",")

    [movieIdLow, movieIdHigh, actorIdLow, actorIdHigh] = line
    if movieIdLow == '*':
      movieIdLow = "-1"
    if actorIdLow == '*':
      actorIdLow = "-1"
    if movieIdHigh == '*':
      movieIdHigh = str(sys.maxint)
    if actorIdHigh == '*':
      actorIdHigh = str(sys.maxint)

    [pagesRead, actors] = queryDB1(movieRolesRoot, int(movieIdLow), int(movieIdHigh), int(actorIdLow), int(actorIdHigh))
    actorIds = set()
    actorPages = set()
    actorNames = set()
    for [actorId, pageNumber] in actors:
      actorIds.add(actorId)
      actorPages.add(pageNumber)
    print actorIds

    #method 1

    #method 2
    method2PagesRead = 0
    shouldBreak = False
    for pageName in os.listdir("actors_table"):
      method2PagesRead += 1
      with open("actors_table/" + pageName,"r") as page:
        for line in page:
          line = line.rstrip().split(",")
          assert len(line) == 4
          if int(line[1]) in actorIds:
            actorNames.add(line[2] + " " + line[3])
            if len(actorNames) == len(actorIds):
            	shouldBreak = True
      if shouldBreak:
      	break
    

    #do our printing here
    print "Results (" + str(len(actorNames)) + " total):"
    for name in actorNames:
    	print "\t" + name

    print "Method 2 total cost: " + str(method2PagesRead+pagesRead) + " pages"
    print "\t" + str(pagesRead) + " page movieroles_ma_idx index"
    print "\t" + str(method2PagesRead) + " page actors_table"
    queryDB3(int(movieIdLow), int(movieIdHigh), int(actorIdLow), int(actorIdHigh))
    
    #queryDB2(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
    
