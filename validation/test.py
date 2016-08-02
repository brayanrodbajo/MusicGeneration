from nltk import *
from learn_trees_music import *
grammar = learn_trees(three_trees)
#print (grammar)
#print (grammar.start())
print("----------------PARSEO--------------")
p = prob_parse(grammar, '''"i" "V7" "V7" "i" ''')
print (p)

