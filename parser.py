#Owen Klaiss
#Word Counting
import sys

file = sys.argv[1]

numLines=0
numWords=0
numBytes=0

with open(file) as feed:
    for line in feed:
        words = line.split()
        numLines += 1
        numWords += len(words)
        numBytes += len(line)

print str(numLines) + "   " + str(numWords) + "   " + str(numBytes)
