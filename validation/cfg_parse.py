#!/usr/bin/env python
# a program to parse specific sentences from a text file
# given a grammar file
# usage: $0 <grammar file> <sentence file> <sentence number [from 0]>

import sys
import nltk
from nltk.parse.chart import *
from datetime import datetime
import time

def parse(sentence, grammarfile, verbose=False):
    grammar = nltk.data.load("file:%s" %(grammarfile))
    chart_parser = ChartParser(grammar,strategy=EARLEY_STRATEGY,trace=0)

    start = datetime.now()
    trees = chart_parser.nbest_parse(sentence)
    end = datetime.now()
    elapsed = end - start
    microseconds = elapsed.microseconds + 1000000*elapsed.seconds
    return sentence, len(trees), microseconds, trees

def read_sentences(sentence_file):
    fd = open(sentence_file)
    sentences = fd.readlines()
    sentences = [sentence.split() for sentence in sentences]
    return sentences

'''
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print ("usage: %s <grammar file> <sentence file> <sentence number> [verbose]" %(sys.argv[0]))
        exit(1)

    grammarfile = sys.argv[1]
    sentence_file = sys.argv[2]
    sent_num = int(sys.argv[3])

    verbose = False
    if len(sys.argv) >= 5:
	   verbose = True #sys.argv[4]    
    sentences = read_sentences(sentence_file)
    if sent_num < 0 or sent_num >= len(sentences):
    	print ("error: sentence %d not in %s" %(sent_num, sentence_file))
    	exit(1)

    sentence, num_parses, timetaken, trees = parse(sentences[sent_num],\
						   grammarfile, verbose)

    print ("sentence\t# parses\ttime [us]")
    print ("%s\t%d\t%d" %(" ".join(sentence), num_parses, timetaken))
    i = 1
    if verbose:
    	for tree in trees:
    	    print (i, tree)
    	    i += 1
'''