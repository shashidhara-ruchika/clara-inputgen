import numpy as np
from zss import Node
def levenshtein(source: str, target: str):
    rows = len(source)+1
    cols = len(target)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    for i in range(1, rows):
        dist[i][0] = i
    for i in range(1, cols):
        dist[0][i] = i
    for col in range(1, cols):
        for row in range(1, rows):
            if source[row-1] == target[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution
    return dist[rows-1][cols-1]

def normalized_levenshtein(s: str, t: str):
    maxlen = max(len(s),len(t))
    lev_dist = levenshtein(s, t)
    return lev_dist/maxlen

 
def convert_body(body,parent_node = None, root_node = None):
    """
    Convert the body to ZSS node
    """
    body = seperate_dict(body)
    if isinstance(body, dict):
        if parent_node == None:
            parent_node = Node(body['_type'])
            new_parent = parent_node
            root_node = parent_node
        for j in body:
            if j!= '_type':
                # still have a kid, then recursion needed
                if isinstance(body[j],dict):
                    if '_type' in body[j].keys():
                        if 'attr' in body[j].keys():
                            node_content = j+' '+body[j]['_type']+' '+body[j]['attr']
                            new_parent = Node(node_content)
                            parent_node.addkid(new_parent)
                            new_parent = convert_body(body[j],parent_node = new_parent,root_node = root_node)
                        else:
                            call_call_func_name = ''
                            #if j == ''
                            if j == 'func':
                                call_call_func_name =' '+body[j]['id']
                            node_content = j+' '+body[j]['_type']+call_call_func_name
                            new_parent = Node(node_content)
                            parent_node.addkid(new_parent)
                            new_parent = convert_body(body[j],parent_node = new_parent,root_node = root_node)
                    else:
                        # case when it's a dict but not with PyType
                        if 'udv' in json.dumps(body[j]):
                            node_content = j+' '+'udv'
                        else:
                            node_content = j+' '+json.dumps(body[j])
                        parent_node = parent_node.addkid(Node(node_content))

                elif isinstance(body[j],list) or isinstance(body[j],str):
                    if body[j]:
                        node_content = j+' '+body[j]
                    else:
                        node_content = j+' '+''
                    parent_node = parent_node.addkid(Node(node_content))
    return root_node

def seperate_dict(dic):
    """
    Helper method to add a suffix dict key
    """
    dic = dic.copy()
    for i in dic.copy():
        if isinstance(dic[i],list):
            if dic[i]:
                count= 0
                for j in dic[i]:
                    count+=1
                    dic[i+str(count)] = j
            del dic[i]
    return dic

def get_ast_length(node):
    len_tree = 1
    for c in node.get_children(node):
        len_tree += get_ast_length(c)
    return len_tree