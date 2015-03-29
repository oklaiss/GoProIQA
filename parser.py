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

numLines2 = numLines
numWords2 = numWords
numBytes2 = numBytes
#subtract from numWords and numBytes by the proper amount, assuming numLines remains the same
with open(file) as f:
    for line in f:
        words = line.split()
        for word in words:
            word.lower()
            if word == "i" or word == "we" or word == "you" or word == "they" or word == "a" or word == "and" or word == "the" or word == "that" or word == "of" or word == "for" or word == "with":
                numWords2 -= 1
                numBytes2 -= len(word)


print "all: " + str(numLines) + "   " + str(numWords) + "   " + str(numBytes) + " " + file
print "proper: " + str(numLines2) + "   " + str(numWords2) + "   " + str(numBytes2)
