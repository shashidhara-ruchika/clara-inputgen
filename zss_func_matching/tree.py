from zss import Node, simple_distance, distance
import ast
from ast2json import ast2json
from utils import normalized_levenshtein, convert_body, get_ast_length

filenames =  [['tests/bubbleSort.py', 'tests/bubbleSort2.py'],
 ['tests/swapXOR.py', 'tests/swapAddSub.py'], 
 ['tests/swapXOR.py', 'tests/swapTempVar.py'],
 ['tests/swapAddSub.py', 'tests/swapTempVar.py'],
['tests/rootNprime.py', 'tests/primeN_2.py'], 
['tests/prime2N.py', 'tests/primeN_2.py'],
['tests/rootNprime.py', 'tests/prime2N.py']]
for fileset in filenames:
    print(fileset)    
    trees, tree_lens = [], []
    for file in fileset:
        text = open(file).read()
        tree = ast.parse(text)
        j = ast2json(tree)
        tt = convert_body(j)
        trees.append(tt)
        tree_lens.append(get_ast_length(tt))
    d = simple_distance(trees[0], trees[1], label_dist=normalized_levenshtein, return_operations=False)
    max_tree_len = max(tree_lens[0],tree_lens[1])
    similarity_score = (1 - (d/max_tree_len))*100
    print("Similarity Score: %.3f percent" % similarity_score)