from pycparser import c_ast

def get_function_params(ast, function_name):
    function=None
    func_index=0
    for i in range(len(ast.ext)):
            func_index+=1
            try:
                if ast.ext[i].decl.name==function_name:
                    function = ast.ext[i]
                    break
            except AttributeError:
                pass
    funcParams = function.decl.type.args.params
    variables = []
    for i in funcParams:
        variables.append((i.name, i.type.type.names[0]))
    return variables


def remove_IO(ast):
    index = 0
    mainindex = 0
    for i in range(len(ast.ext)):
        if ast.ext[i].decl.name=='main':
            mainindex = i
            break
        mainindex+=1
    indices = []
    print("mainindex is ", mainindex)
    for i in ast.ext[mainindex].body.block_items:
        try:
            if type(i)==c_ast.FuncCall and i.name.name == 'scanf':
                indices.append(index)
        except AttributeError:
            pass
        index+=1
    main = ast.ext.pop(mainindex)
    body = []
    for i in range(len(main.body.block_items)):
        if i not in indices:
            body.append(main.body.block_items[i])
    decl = c_ast.Decl(name='main', quals=[], storage=[], funcspec=[],type = c_ast.FuncDecl(args=None, type=c_ast.TypeDecl(declname='main', quals=[], type=c_ast.IdentifierType(names=['int']))), init=None, bitsize=None)
    newmain = c_ast.FuncDef(decl=decl, param_decls=None, body=c_ast.Compound(block_items=body))
    ast.ext.insert(mainindex, newmain)
    return ast