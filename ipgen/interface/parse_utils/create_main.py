from pycparser import c_ast

def create_main(variables, function):
    '''
    Given a list of variables and a function (funcname and func return type)
    Generate a main() for the programs which do not contain one
    '''
    name='main'
    return_type = 'int'
    decl = c_ast.Decl(name=name, quals=[], storage=[], funcspec=[],
    type = c_ast.FuncDecl(args=None, type=c_ast.TypeDecl(declname=name, quals=[], type=c_ast.IdentifierType(names=[return_type]))), init=None, bitsize=None)
    body, args =[], []
    for var in variables:
        stmt = c_ast.Decl(name=var[0], quals=[], storage=[], funcspec=[], type=c_ast.TypeDecl(declname=var[0], quals=[], type=c_ast.IdentifierType(names=[var[1]])), init=None, bitsize=None)
        body.append(stmt)
    for var in variables:
        if var[1] in ['int', 'char', 'short', 'float', 'unsigned_short']:
            node = c_ast.FuncCall(name=c_ast.ID(name='CREST_'+var[1]), args=c_ast.ExprList(exprs=[c_ast.ID(name=var[0])]))
            body.append(node)
            argnode = c_ast.ID(name=var[0])
            args.append(argnode)
    call = c_ast.FuncCall(name=c_ast.ID(name=function), args=c_ast.ExprList(exprs=args))
    body.append(call)
    return_stmt = c_ast.Return(expr=c_ast.Constant(type=return_type, value='0'))
    body.append(return_stmt)
    mainFunc = c_ast.FuncDef(decl=decl, param_decls=None, body=c_ast.Compound(block_items=body))
    return mainFunc

