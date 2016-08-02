from nltk import *
from nltk.corpus import treebank
from nltk.treetransforms import *
#from nltk import bracket_parse
from nltk.tree import Tree
from nltk import grammar
#import dynamic_pcfg

# Three parse trees that you'll use for the first question.
folder = "ArbolesTxtPuntos/"
three_trees = [Tree.fromstring(t) for t in #SE DEBE LEER TODA LA CARPETA, NO ARCHIVO POR ARCHIVO
[open(folder+"calipachanguero.txt").read(), open(folder+"buscapordentro.txt").read(), open(folder+"anamile.txt").read(),open(folder+"apruebadefuego.txt").read(),open(folder+"hagamosloquedigaelcorazon.txt").read(),open(folder+"miserable.txt").read(),open(folder+"sinsentimiento.txt").read()]]

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

if __name__ =='__main__':
  grammar = learn_trees(three_trees)
  grammar_str = str(grammar)
  grammar_str = grammar_str.splitlines(True) #The first line of grammar_str is a not important line 
  grammar_str = ''.join(grammar_str[1:]) # Then, here is removed
  f = open("pcfg.txt", "w")
  f.write(str(grammar_str))
  f.close()


