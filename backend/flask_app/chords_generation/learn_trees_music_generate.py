from nltk import *
from nltk import Nonterminal
from nltk.corpus import treebank
from nltk.treetransforms import *

from nltk.tree import Tree
from nltk import grammar
from numpy.random import choice
import glob, os


#Removing the + symbol from the grammar to recognize it from the fromstring 
def remove_symbols(text):
    text = text.replace('+', '')
    return text


#When the production rules are extracted, only one should be chosen for each Nonterminal item of items.
#Return the frags in a list of chords
def generate_sample(grammar, items, frags):
    # print ("items ",items)
    #global frags
    for item in items:
        # print ("item ", item)
        # print ("nonterminal ",isinstance(item, Nonterminal))
        if isinstance(item, Nonterminal):
            prods = grammar.productions(lhs=item)
            probs = []
            for prod in prods:
                probs.append(prod.prob())
                # print (prod.prob())
            #This is because the probabilities hardly ever sum exactly 1.0
            if abs(1-sum(probs)) < 0.1:
                remaining = 1-sum(probs)
                probs[0]=probs[0]+remaining
                # print ("no dio 1")
            else:
                raise("Probabilities don't sum even near to 1.0")
            chosen_prod = prods[0] #Inicializing
            chosen_prod = choice(prods, p= probs)
            if str(item) == 'S':
                print ("chosen prod ", chosen_prod.rhs())
                grammar_file = open("chosen_prod.txt", "w")
                grammar_file.write(str(chosen_prod.rhs()))
                grammar_file.close()
            generate_sample(grammar, chosen_prod.rhs(), frags) #It passes the right hand items of the chosen production and the same grammar
        else:
            frags.append(item)
    return frags

if __name__ =='__main__':
    grammar_file = open("pcfg.txt", "r")
    grammar_str = grammar_file.read()
    grammar_file.close()
    # print ("GRAMÁTICA CON + \n"+grammar_str)
    grammar_str= remove_symbols(grammar_str)
    # print ("GRAMÁTICA SIN + \n"+grammar_str)
    grammar = PCFG.fromstring(grammar_str)
    s= Nonterminal('S')
    s = [s]
    chords = generate_sample(grammar, s, [])
    # print (chords)
