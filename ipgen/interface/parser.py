from __future__ import print_function
from pycparser import c_parser, c_generator, c_ast
from parse_utils.ast_manip import remove_IO, get_function_params
from parse_utils.text_preproc import remove_comments, remove_directives, reconstruct_source
from parse_utils.create_main import create_main
import sys

try:
	'''
	Preprocessing source code
	'''
	filename = sys.argv[1]
	negative = int(sys.argv[2])
	text = open(filename).read()
	text, includes, defines = remove_directives(text)
	text = remove_comments(text)
	variable_names = []
	main_index=0
	parser = c_parser.CParser()
	mainFunction = None
	ast = parser.parse(text)
	ast = remove_IO(ast)  #remove all scanf
	for i in range(len(ast.ext)):
		main_index+=1
		try:
			if ast.ext[i].decl.name=='main':
				mainFunction = ast.ext[i]
				break
		except AttributeError:
			pass
	index = 0
	if mainFunction==None:           #No main function exists in the given code
		variable_names = get_function_params(ast, ast.ext[0].decl.name)
		mainFunction = create_main(variable_names, ast.ext[0].decl.name)
		ast.ext.append(mainFunction)
	else:							#Main function exists
		'''
		Loop through each statement in main
		if stmt is a variable declaration add it to a list called variable_names, else if it is a function call then stop
		'''
		for i in mainFunction.body.block_items:
			try:
				if type(i.init) == c_ast.FuncCall or type(i)==c_ast.FuncCall: 
					break
				if type(i)==c_ast.Decl:
					if type(i.type) == c_ast.PtrDecl:
						variable_names.append((i.name, i.type.type.type.names+'*'))
					else:
						variable_names.append((i.name, '_'.join(i.type.type.names)))
				index+=1
			except AttributeError:
				pass
		nodes = []     #For each variable in variable_names create nodes that represent crest function calls
		for var in variable_names:
			if var[1] in ['char', 'short', 'float', 'unsigned_short']:
				data_type = var[1]
			elif var[1]=='int':
				if negative==1:
					data_type = 'short'
				else:
					data_type = 'unsigned_short'
			node = c_ast.FuncCall(name=c_ast.ID(name='CREST_'+data_type), args=c_ast.ExprList(exprs=[c_ast.ID(name=var[0])]))
			nodes.append(node)
		for node in nodes:  #Append the nodes to the AST
			ast.ext[main_index-1].body.block_items.insert(index, node)
			index+=1

	generator = c_generator.CGenerator()  #Parse the new AST and reconstruct the new, CREST-compatible source code
	new_source_code = generator.visit(ast)
	filename = sys.argv[1].split('.')[0]+'.'+sys.argv[1].split('.')[1]
	code = reconstruct_source(new_source_code, includes, defines)
	f = open(filename, 'w')
	f.write(code)
	f.close()
except FileNotFoundError:
	print('File ' + sys.argv[1] + ' not found!')


