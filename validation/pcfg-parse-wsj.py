#!/usr/bin/env python

import nltk
from nltk.parse import pchart
from datetime import datetime
import cfg_parse
import grammar #porque la libreria de nltk descargada no tiene el metodo parse_pcfg


def pcfg_chartparser(grammarfile):
 f = open(grammarfile)
 grammar_str = f.read()
 f.close()
 return nltk.ViterbiParser(grammar.parse_pcfg(grammar_str))


def main():
  grammarp = pcfg_chartparser("pcfg.txt")
  sents = cfg_parse.read_sentences("simple-sentences.txt")
  #grammarp = pcfg_chartparser("wsjp.cfg")
  #sents = cfg_parse.read_sentences("sentences.txt")
  print ("sentence\ttime elapsed (us)")
  for sent in sents:
    start = datetime.now()
    tree = grammarp.parse(sent) 
    end = datetime.now()
    elapsed = end - start
    microseconds = elapsed.microseconds + 1000000*elapsed.seconds
    print (sent, microseconds)
    for t in tree:
      print (t)
    #print (list(tree))
    
if __name__ == '__main__': main()
