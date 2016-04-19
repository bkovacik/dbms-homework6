import os
import re
import sys

actorTable = "actors_table/"
movieRoles = "movieroles_table/"
movieIdNum = 3
movieNameNum = 4
actorIdNumA = 1
actorIdNumM = 0
actorNameNum = 2

def queryDB3(movieIdLow, movieIdHigh, actorIdLow, actorIdHigh):
  movieCount = 0;
  actorCount = 0;
  actorSet = set();
  for filename in os.listdir(movieRoles):
    movieCount += 1;
    with open(movieRoles + filename) as f:

      for line in f:
        line = re.sub('".*"', '', line)
        tuples = line.split(',')

        movieId = int(tuples[movieIdNum])
        actorId = int(tuples[actorIdNumM])
        movieName = tuples[movieNameNum]

        if movieIdLow <= movieId and movieIdHigh >= movieId\
          and actorIdLow <= actorId and actorIdHigh >= actorId:
          actorSet.add(int(actorId))
  #print actorSet

  for actorPage in os.listdir(actorTable):
    actorCount += 1
    with open(actorTable + actorPage) as a:

      for actor in a:
        tuples = actor.split(',')
        if int(tuples[actorIdNumA]) in actorSet:
          actorSet.remove(int(tuples[actorIdNumA]))
          #print actorSet
        if len(actorSet) == 0:
          break;
    if len(actorSet) == 0:
      break;
#          sys.stdout.write(tuples[actorNameNum] + " " + tuples[actorNameNum+1])
  print "Method 3 total cost: " + str(actorCount+movieCount)
  print "\t", movieCount, "page movieroles_table"
  print "\t", actorCount, "page actors_table"
