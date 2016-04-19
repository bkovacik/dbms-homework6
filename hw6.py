import sys
import csv
from queryDB1 import queryDB1
import os
from queryDB3 import queryDB3 
assert len(sys.argv) == 2
inputFileName = sys.argv[1]

actorIdRoot = "actors_id_idx/root.txt"
movieRolesRoot = "movieroles_ma_idx/root.txt"

with open(inputFileName) as inputFile:
  for line in inputFile:
    print "Query: "+ str(line)
    
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

    #method 1
    method1IndexPagesRead = 0
    for actorId in actorIds:
	    method1IndexPagesRead +=1
	    minActor = actorId
	    maxActor = actorId
	    nextLeaf = None
	    nextLeafLowMovieId = -1
	    actorPageNums = set()
	    with open(actorIdRoot, "r") as actorRoot:
	    	for line in actorRoot:
	    		line = line.rstrip()
	    		if line == "internal":
	    			continue
	    		line = line.split(",")
	    		maxLeafId = int(line[0])
	    		leafPath = "actors_id_idx/" + line[1]
	    		if maxLeafId > minActor:
	    			nextLeaf = leafPath
	    			break
	    while nextLeaf and nextLeafLowMovieId < maxActor:
		    with open(nextLeaf, "r") as leaf:
		    	method1IndexPagesRead += 1
		    	for line in leaf:
		    		line = line.rstrip()
		    		if line == "leaf":
		    			continue
		    		line = line.split(",")
		    		if len(line)==1:
		    			nextLeaf = "actors_id_idx/" + line[0]
		    			break
		    		actorId = int(line[0])
		    		actorPageNum = line[1]
		    		nextLeafLowMovieId = actorId
		    		if actorId in actorIds:
		    			actorPageNums.add(actorPageNum)

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

    print "Method 1 total cost: " + str(method1IndexPagesRead + pagesRead + method1IndexPagesRead/2)
    print "\t" + str(pagesRead) + " page movieroles_ma_idx index"
    print "\t" + str(method1IndexPagesRead) + " page actors_id_idx index"
    print "\t" + str(method1IndexPagesRead/2) + " page actors_table" 

    print "Method 2 total cost: " + str(method2PagesRead+pagesRead) + " pages"
    print "\t" + str(pagesRead) + " page movieroles_ma_idx index"
    print "\t" + str(method2PagesRead) + " page actors_table"
    queryDB3(int(movieIdLow), int(movieIdHigh), int(actorIdLow), int(actorIdHigh))
    
    #queryDB2(actorIdRoot, movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow, actorIdHigh)
    print "********************************************************************"
