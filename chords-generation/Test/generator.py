import nltk
from numpy.random import choice
from nltk import Nonterminal


groucho_grammar = nltk.PCFG.fromstring("""
    ADVP -> 'loudly' [0.333333]
    NP -> 'Fred' [0.166667]
    V1 -> 'pronounced' [0.333333]
    V1 -> 'declared' [0.333333]
    NP -> 'Sally' [0.333333]
    VP -> V1 SBAR [0.333333]
    NP -> 'Jeff' [0.166667]
    V2 -> 'ran' [0.333333]
    ADVP -> 'quickly' [0.333333]
    NP -> 'John' [0.166667]
    ADVP -> 'elegantly' [0.333333]
    V2 -> 'snored' [0.333333]
    V2 -> 'swam' [0.333333]
    SBAR -> COMP S [1.0]
    V1 -> 'said' [0.333333]
    VP -> V2 [0.333333]
    COMP -> 'that' [1.0]
    NP -> 'Bill' [0.166667]
    S -> NP VP [1.0]
    VP -> VP ADVP [0.333333]
 """)


#When the production rules are extracted, only one should be chosen for each Nonterminal item.
def generate_sample(grammar, items, frags):
    print ("items ",items)
    #global frags
    for item in items: 
        print ("item ", item)
        print ("nonterminal ",isinstance(item, Nonterminal))
        if isinstance(item, Nonterminal):
            prods = grammar.productions(lhs=item)
            print ("prods ", prods)
            probs = []
            for prod in prods:
                probs.append(prod.prob())
                print (prod.prob())
            chosen_prod = choice(prods, p= probs)
            print ("chosen prods ", chosen_prod)
            generate_sample(grammar, chosen_prod.rhs(), frags) #It passes the right hand items of the chosen production and the same grammar
        else:
            frags.append(item)
    return frags

s= nltk.grammar.Nonterminal('S')
s = [s]
frags = generate_sample(groucho_grammar, s, [])
print (frags)