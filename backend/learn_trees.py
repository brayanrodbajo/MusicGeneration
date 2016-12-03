from nltk import *
from nltk.corpus import treebank
from nltk.treetransforms import *
#from nltk import bracket_parse
from nltk.tree import Tree
from nltk import grammar

# Three parse trees that you'll use for the first question.
three_trees = [Tree.fromstring(t) for t in
['''(S (NP John) (VP (V1 said) (SBAR (COMP that)
(S (NP Sally) (VP (VP (V2 snored)) (ADVP loudly))))))''',
'''(S (NP Sally) (VP (V1 declared) (SBAR (COMP that)
(S (NP Bill) (VP (VP (V2 ran)) (ADVP quickly))))))''',
'''(S (NP Fred) (VP (V1 pronounced) (SBAR (COMP that)
(S (NP Jeff) (VP (VP (V2 swam)) (ADVP elegantly))))))''']]

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
      if markov_order:
        tree.chomsky_normal_form(horzMarkov=markov_order)
      else:
        tree.chomsky_normal_form()
      productions += tree.productions()
      print "producciones ", productions

    grammar_p = grammar.induce_pcfg(Nonterminal('S'), productions)
    return grammar_p

if __name__ =='__main__':
	grammar = learn_trees(three_trees)
	print grammar
