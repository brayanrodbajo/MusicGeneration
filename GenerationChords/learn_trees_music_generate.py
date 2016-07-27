from nltk import *
from nltk.corpus import treebank
from nltk.treetransforms import *
#from nltk import bracket_parse
from nltk.tree import Tree
from nltk import grammar
from numpy.random import choice
#import dynamic_pcfg

# Three parse trees that you'll use for the first question.
folder = "ArbolesTxtPuntos/"
three_trees = [Tree.fromstring(t) for t in #SE DEBE LEER TODA LA CARPETA, NO ARCHIVO POR ARCHIVO
[open(folder+"calipachanguero.txt").read(), open(folder+"buscapordentro.txt").read(), open(folder+"anamile.txt").read(),open(folder+"apruebadefuego.txt").read(),open(folder+"hagamosloquedigaelcorazon.txt").read(),open(folder+"miserable.txt").read()]]

def learn_trees(trees, collapse=True, markov_order=None):
    """
    Given a list of parsed sentences, return the maximum likelihood PCFG
    for those sentences.

    If 'collapse' is True, it will collapse the trees before learning the
    grammar so that there are no unary productions.

    This will reduce productions of length more than 2 using Chomsky normal
    form.  You can Markov-smooth the results by setting markov_order to a
    number such as 2.
    """
    productions = []
    for tree in trees:
      if collapse: tree.collapse_unary(collapsePOS=False)
      #if markov_order:
       # tree.chomsky_normal_form(horzMarkov=markov_order)
      #else:
        #tree.chomsky_normal_form()
      productions += tree.productions()
      #print productions

    grammar_p = grammar.induce_pcfg(Nonterminal('S'), productions)
    return grammar_p


#Para quitar el + de la gramática y sea reconocida como tal por el metodo fromstring
def quitar_simbolos(text):
    text = text.replace('+', '')
    return text


# def prob_parse(grammar, sentence, n=1):
#     """
#     Return the n most likely parses (default 1) for a sentence, given a PCFG.

#     If n=1, this will use Viterbi (A*) parsing for efficiency.

#     If the grammar was trained on trees in Chomsky normal form, this function
#     will un-Chomsky the trees before outputting them.
#     """
#     words = sentence.split()
#     if n == 1:
#         parses = [dynamic_pcfg.best_parse(grammar, sentence, trace=2)]
#     else:
#         parser = InsideChartParser(grammar, trace=2)
#         parses = parser.nbest_parse(words, n)
#     for parse in parses: un_chomsky_normal_form(parse)
#     return parses


#When the production rules are extracted, only one should be chosen for each Nonterminal item.
#Return the frags in a list of chords
def generate_sample(grammar, items, frags):
    # print ("items ",items)
    #global frags
    for item in items: 
        # print ("item ", item)
        # print ("nonterminal ",isinstance(item, Nonterminal))
        if isinstance(item, Nonterminal):
            prods = grammar.productions(lhs=item)
            # print ("prods ", prods)
            probs = []
            for prod in prods:
                probs.append(prod.prob())
                # print (prod.prob())
            chosen_prod = choice(prods, p= probs)
            # print ("chosen prods ", chosen_prod)
            generate_sample(grammar, chosen_prod.rhs(), frags) #It passes the right hand items of the chosen production and the same grammar
        else:
            frags.append(item)
    return frags


if __name__ =='__main__':
    # grammar_file = open("pcfg.txt", "r")
    # grammar_str = grammar_file.read()
    # grammar_file.close()
    # print ("GRAMÁTICA CON + \n"+grammar_str)
    # grammar_str= quitar_simbolos(grammar_str)
    # print ("GRAMÁTICA SIN + \n"+grammar_str)
    # grammar = PCFG.fromstring(grammar_str)
    grammar = learn_trees(three_trees)
    f = open("pcfg.txt", "w")
    f.write(str(grammar))
    f.close()
    s= Nonterminal('S')
    s = [s]
    chords = generate_sample(grammar, s, [])
    print (chords)


