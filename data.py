from os import listdir

# Goes into the specified folder for Galaxies and returns
#  all files in the specified relative folder
def getFiles(dirRelPath):
  return listdir(dirRelPath)

# Given a line of data from a file, convert each string value
#  (which are sepperated by tabs) to floats
def dataLineToValues(line):
  stringValues = line.split("\t")
  floatValues = list(map(lambda x: float(x), stringValues))
  return floatValues

# Returns all the galaxy data in the given folder
def GetGalaxyData(galaxiesDirRelPath):
  files = getFiles(galaxiesDirRelPath)

  # Dictionary "galaxy name"->[list of data points]
  data = {}

  for fileName in files:
    file = open(galaxiesDirRelPath + fileName, "r")
    # Convert the file string to an array of each line
    lines = file.read().splitlines()
    # Cut off the first 3 lines which are just comments
    dataLines = lines[3:]
    # Convert each line to a list of data points
    parsedLines = list(map(dataLineToValues, dataLines))
    
    data[fileName[:-4]] = parsedLines
    file.close()

  return data