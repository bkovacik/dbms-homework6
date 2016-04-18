#this function implements the first method of scanning for actors
#it looks at the movieRoles index and then grabs the actor names
def queryDB1(movieRolesRoot, movieIdLow, movieIdHigh, actorIdLow,\
                                                     actorIdHigh):
  pagesRead = 0
  actorIds = []
  with open(movieRolesRoot, "r") as root:
    pagesRead+=1
    #look for the right internal node
    for line in root:
      if line == "internal\n":
        continue
      line = line.rstrip().split(",")
      indexMovieIdHigh = int(line[0])
      indexActorIdHigh = int(line[1])
      indexPath = "movieroles_ma_idx/" + line[2]
      print str(indexMovieIdHigh) + " < " + str(movieIdLow)
      print str(indexActorIdHigh) + " < " + str(actorIdLow)
      if (indexMovieIdHigh < movieIdLow) or (indexActorIdHigh < actorIdLow):
      	print "1"
        continue
      else:
        #here is the case where we have found the right index to read
        print "2"
        pagesRead += 1
        [actorIds, leavesRead] = readIndexPage(movieIdLow,movieIdHigh,\
                                              actorIdLow, actorIdHigh,\
                                                             indexPath)
        pagesRead += leavesRead
        break
  return [pagesRead, actorIds]
  
def readIndexPage(movieIdLow, movieIdHigh, actorIdLow, actorIdHigh,\
                                                          indexPath):
  actorIds = []
  leavesRead = 0
  with open(indexPath, "r") as indexPage:
    startLeaf = None
    for line in indexPage:
      if line == "internal\n":
        continue
      print line
      line = line.rstrip().split(",")
      if len(line) == 1:
      	break
      leafMovieIdHigh = int(line[0])
      leafActorIdHigh = int(line[1])
      leafPath = "movieroles_ma_idx/" + line[2]
      if leafMovieIdHigh >= movieIdLow and leafActorIdHigh >= actorIdLow:
        startLeaf = leafPath

  if startLeaf != None:
    leavesRead+=1
    [newActorIds, nextLeaf, nextLeafLowMovieId] = \
      readLeafPage(movieIdLow, movieIdHigh, actorIdLow, actorIdHigh, startLeaf)
    actorIds += newActorIds
    while nextLeaf and nextLeafLowMovieId<movieIdHigh:
      leavesRead+=1
      [newActorIds, nextLeaf, nextLeafLowMovieId] = \
        readLeafPage(movieIdLow, movieIdHigh, actorIdLow, actorIdHigh, "movieroles_ma_idx/"+nextLeaf)
      actorIds+=newActorIds
  print "Done"
  return [actorIds, leavesRead]

#t
def readLeafPage(movieIdLow, movieIdHigh, actorIdLow, actorIdHigh, leafPath):

  nextLeaf = None
  newActorIds = []
  nextLeafLowMovieId = None
  with open(leafPath, "r") as leafPage:
    for line in leafPage:
      if line == "leaf\n":
        continue
      line = line.rstrip().split(",")
      if len(line) == 1:
        nextLeaf = line[0]
      else:
        movieId = int(line[0])
        actorId = int(line[1])
        pageNumber = int(line[2])
        nextLeafLowMovieId = movieId
        if movieIdLow <= movieId and movieIdHigh >= movieId and actorIdLow<=actorId and actorIdHigh>=actorId:
          #We have found a valid actor
          newActorIds.append([actorId, pageNumber])
  return [newActorIds, nextLeaf, nextLeafLowMovieId]

