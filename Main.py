import sys
import math

from random import *
from ReaderWriter import Reader, Writer

path = sys.argv[1]
k = sys.argv[2]

# print('Path is ',path,' and k is ', k)

class DataPoint:

  def __init__(self, data):
    self.data = data
    self.cluster = -1
  
  def getPoint(self, index):
    return self.data[index]
  
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
    return self.dataPoints[index]
  
  def removePoint(self, index):
    del self.dataPoints[index]

  def getDataPoints(self):
    return self.dataPoints
  
  def recenter(dimensions):
    self.dimensions = dimensions

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
  for i in range(len(centroid.getDataPoints)):
    newMeasures.append(centroid.getDimension(i) - dataObj.getPoint(i))
  total = 0
  for measure in newMeasures:
    squareMeasures.append(measure * measure)
  for measure in squareMeasures:
    total = total + measure
  return math.sqrt(total)

# Iterate through all centroids to find closes and assign to object

def assignCentroidToObj(centroids, dataObj):
  minDistance = getEuclidian(centroids[0], dataObj)
  dataObj.setCluster(0)
  for i in range(1,len(centroids)):
    newDistance = getEuclidian(centroids[i], dataObj)
    if newDistance < minDistance:
      minDistance = newDistance
      dataObj.setCluster(i)

def recenterSingleCentroid(centroid, dataObjs):
  newDimensions = [0] * len(dataObj.getData)
  for dataobj in dataObjs:
    for i in range(len(dataobj)):
      newDimensions[i] = newDimensions[i] + dataobj[i]
  
  for dimension in newDimensions:
    dimension = dimension / len(dataObjects)
  centroid.recenter(newDimensions)

def recenterCentroids(centroids, dataObjs):
  for centroid in centroids:
    recenterSingleCentroid(centroid, dataObjs)


gDataPoints = Reader(path).read()
print(gDataPoints)

centroidArray = initializeCentroids(k)
dataObjects = initializePoints(gDataPoints)

