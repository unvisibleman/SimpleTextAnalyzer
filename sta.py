#!/usr/bin/python
# -*- cofing utf-8 -*-

import sys
#import numpy as np

punctMarks = [",", "-", ":", ";"]
stopMarks = [".", "!", "?"]

# 1. open file with data and load it

if len(sys.argv) == 1:
    sys.argv("Not given file name of input file")
inputFile = sys.argv[1]
outputFile = inputFile.replace("txt", "brain")
if inputFile == outputFile:
    sys.exit("Input file have extension not .txt")
try:
    inputText = [line.rstrip('\n') for line in open(inputFile)]
except IOError:
    sys.exit("Input-output error")
print inputText

# todo place better text pre-editing here
inputText[0] = inputText[0].lower()
# for the first line solate all puctuation marks and ends of sentenses with extra spaces
for char in punctMarks:
    inputText[0] = inputText[0].replace(char, " "+char)
for char in stopMarks:
    inputText[0] = inputText[0].replace(char, " "+char)
sentense = inputText[0].split(' ')
sentense = list(filter(None, sentense)) # remove empty elements
print sentense  

# create and fill a vocabulary and frequency
freq = dict() # dict. of words and number of their usage
for word in sentense:
    if not freq.get(word):
        freq[word] = 1
    else:
         freq[word] += 1
powerful = len(freq)
print freq
vocabulary = dict() # dict. of words and seq. number of it
words = freq.keys()
for i in xrange(0, powerful):
    vocabulary[words[i]] = i
print vocabulary

# create and fill conversion matrix. It contains numbers of changing from one word to another
M = [[ 0 for j in xrange(0, powerful)] for i in xrange(0, powerful)]
for i in xrange(1, len(sentense)):
    M[
         vocabulary[sentense[i-1]]
    ][
        vocabulary[sentense[i]]
    ] +=1 

#cute M output
print "\t",
for i in xrange(0, powerful):
    print words[i], "\t",
print
for i in xrange(0, powerful):
    print words[i], "\t",
    for j in xrange(0, powerful):
        print M[i][j], "\t",
    print

#simple analyzing: top 5 freq words and sequence of high possible words
top5words = sorted(freq, freq.get, reverse=True)[:5]
print top5words
# find max value in M
i_max=-1
j_max=-1
m_max=-1
for i in xrange(0, powerful):
    for j in xrange(0, powerful):
        if (M[i][j] > m_max) and not (words[i] in punctMarks) and not (words[j] in stopMarks):
            m_max = M[i][j]
            i_max = i
            j_max = j
print words[i_max], words[j_max], 
# get in M and find route from j_max
count=0
while True:
    m_max=-1
    i_max=-1
    # find most possible conversion from this word
    for i in xrange(0, powerful):
        if  M[j_max][i] > m_max:
            m_max = M[j_max][i]
            i_max = i
    print words[i_max],
    j_max = i_max
    if count==5:
        break
    count+=1
print "\n"
