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

#Articles and Sections counter
dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
current = 1
with open(file) as fin:
    for line in fin:
        if "Article 2." in line:
            current = 2
        if "Article 3." in line:
            current = 3
        if "Article 4." in line:
            current = 4
        if "Article 5." in line:
            current = 5
        if "Article 6." in line:
            current = 6
        if "Article 7." in line:
            current = 7
        if "Section 1" in line or "Section 2" in line or "Section 3" in line or "Section 4" in line or "Section 5" in line or "Section 6" in line or "Section 7" in line or "Section 8" in line or "Section 9" in line or "Section 10" in line or "Section 11" in line or "Section 12" in line or "Section 13" in line:
            dict[current] += 1

print "Total Articles: " + "07"
total = dict[1] + dict[2] + dict[3] + dict[4] + dict[5] + dict[6] + dict[7]
print "Total Sections: " + str(total)
print "Total Sections per Article:"
print "   Article 1: " + str(dict[1])
print "   Article 2: " + str(dict[2])
print "   Article 3: " + str(dict[3])
print "   Article 4: " + str(dict[4])
print "   Article 5: " + str(dict[5])
print "   Article 6: " + str(dict[6])
print "   Article 7: " + str(dict[7])
