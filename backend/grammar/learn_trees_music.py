from nltk import *
from nltk.corpus import treebank
from nltk.treetransforms import *
#from nltk import bracket_parse
from nltk.tree import Tree
from nltk import grammar
#import dynamic_pcfg

folder = "ArbolesTxtPuntosNoComillas/"
#os.chdir(folder)
#trees=[file for file in glob.glob("folder+*.txt")]#] #the whole folder is read. Only txt files.
three_trees = [Tree.fromstring(t) for t in
[open(folder+file).read() for file in os.listdir(folder) if file.endswith(".txt")]] #the whole folder is read. Only txt files.

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

if __name__ =='__main__':
  grammar = learn_trees(three_trees)
  grammar_str = str(grammar)
  grammar_str = grammar_str.splitlines(True) #The first line of grammar_str is a no important line
  grammar_str = ''.join(grammar_str[1:]) # Then, here is removed
  f = open("pcfg.txt", "w")
  f.write(str(grammar_str))
  f.close()
