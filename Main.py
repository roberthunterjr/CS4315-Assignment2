import sys
import math

from random import *
from ReaderWriter import Reader, Writer

# print('Path is ',path,' and k is ', k)

class DataPoint:

  def __init__(self, data):
    self.data = data
    self.cluster = 0
  
  def getPoint(self, index):
    return int(self.data[index])
  
  def getCluster(self):
    return self.cluster

  def setCluster(self, cluster):
    self.cluster = cluster
  
  def getData(self):
    return self.data

  def getDimension(self):
    return len(self.data)

class Centroid:

  def __init__(self, dimensions):
    self.dataPoints = []
    self.dimensions = dimensions
  
  def addPoint(self, data):
    self.dataPoints.append(data)
  
  def getDimension(self, index):
    return self.dimensions[index]

  def getDimensions(self):
    return self.dimensions

  def removePoint(self, index):
    del self.dataPoints[index]

  def removeAllPoints(self):
    self.dataPoints = []

  def getDataPoints(self):
    return self.dataPoints
  
  def recenter(self):
    numPoints = len(self.dataPoints)
    # print('This centroid has ',numPoints, 'dataPoints')
    if(numPoints > 0):
      numDimensions = len(self.dataPoints[0].getData())
      newDimensions = [0] * numDimensions
      for point in self.dataPoints:
        for i in range(len(point.getData())):
          newDimensions[i] = newDimensions[i] + point.getPoint(i)
      avgDimensions = []
      for dimension in newDimensions:
        avg = dimension/numPoints
        avgDimensions.append(avg)
      self.dimensions = avgDimensions
      self.removeAllPoints()

# Generate K centroids and base the number of measures they contain on the num dimensions passed in 
def initializeCentroids(numK, numDimensions):
  centroids = []
  for i in range(numK):
    measures = []
    for j in range(numDimensions):
      measures.append(randint(0,30))
    centroids.append(Centroid(measures))
  return centroids

# Initialize the data points from the array of data read in from the text file
def initializePoints(dataPoints):
  dataPointObjects = []
  for point in dataPoints:
    dataPointObjects.append(DataPoint(point))
  return dataPointObjects


# get the Euclidian distance of from the datapoint to the centroid
def getEuclidian(centroid,dataObj):
  newMeasures = []
  squareMeasures = []
  # print('centroid dimensions',centroid.getDimensions())
  for i in range(len(centroid.getDimensions())):
    # print(dataObj.getPoint(i))
    newMeasures.append(centroid.getDimension(i) - dataObj.getPoint(i))
  total = 0
  for measure in newMeasures:
    squareMeasures.append(measure * measure)
  for measure in squareMeasures:
    total = total + measure
  return math.sqrt(total)


 # Iterate through all centroids to find closest and assign to object
def assignCentroidToObj(centroids, dataObj):
  wasReassigned = False
  minDistance = getEuclidian(centroids[0], dataObj) # This is a default for the first iteraton of AssignCentroidToObj
  for i in range(1,len(centroids)):
    newDistance = getEuclidian(centroids[i], dataObj)
    if newDistance < minDistance:
      # print('Old distance is ',minDistance,' and new distance is ',newDistance)
      minDistance = newDistance
      if(dataObj.getCluster() != i):
        dataObj.setCluster(i)
        # print('Cluster set to ',i)
        wasReassigned = True
  return wasReassigned

# Add each point to a corresponding centroid for recentering puposes, then clear them out
def addPointsToCentroids(centroids, dataObjs):
  for point in dataObjs:
    # print('Adding',point.getData(),' to cluster ',point.getCluster())
    centroids[point.getCluster()].addPoint(point) # Adds deach point to their corresponding centroid in the centroid array

# Method to recenter all of the centroids based on datapoints currently assigned
def recenterCentroids(centroids, dataObjs):
  # print('Recentering Centroids')
  addPointsToCentroids(centroids, dataObjs)
  for centroid in centroids:
    centroid.recenter()

#########################
##  Starting main process
# print('Starting***********************************************')
path = sys.argv[1]
k = int(sys.argv[2])

gDataPoints = Reader(path).read()

centroidArray = initializeCentroids(k, len(gDataPoints[0]))
dataObjects = initializePoints(gDataPoints)


# Initial assignment of centroids to each datapoint
for point in dataObjects:
  assignCentroidToObj(centroidArray, point)


# Initial recentering of centroids
while(True):
  looping = False
  recenterCentroids(centroidArray, dataObjects)
  for point in dataObjects:
    # While there is still a new centroid assignment from the dataObjects
    if(assignCentroidToObj(centroidArray, point)):
      looping = True
  # for point in dataObjects:
    # print('In Loop: data is ',point.getData(),' and cluster is',point.getCluster())
  if(looping == False):
    break

# Append cluster numbers
finalData = []
for point in dataObjects:
  data = point.getData()
  data.append(str(point.getCluster()))
  finalData.append(data)

# Done recentering, ready to output
outWriter = Writer('output.txt')
outWriter.write(finalData)
  