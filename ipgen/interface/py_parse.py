import ast

def get_variables(root):
    for node in ast.walk(root):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            yield node.id
        elif isinstance(node, ast.Attribute):
            yield node.attr
        elif isinstance(node, ast.FunctionDef):
            yield node.name
            
def get_variables_func(def_str):
        var = def_str[def_str.find("(") + 1: def_str.find(")")].split(",")
        return [i.strip() + ">=0" for i in var]      
            
def write_new_file_branch(filename, no_branch_func):
        all_lines = []
        f = open(filename, "r")
        lines = f.readlines() 
        i = 0
        while(i < len(lines)):
                if("def" in lines[i]):
                        flag = 0
                        for func in no_branch_func:
                                if func in lines[i]:
                                        flag = 1                        
                        if(flag):                
                                all_lines.append(lines[i])
                                j = i + 1
                                var = get_variables_func(lines[i])
                                if_str = "\tif " + " and ".join(var) + ":\n"
                                all_lines.append(if_str)
                                while(j < len(lines) and not(lines[j].startswith("def")) and not("__main__" in lines[j])):
                                        all_lines.append("\t" + lines[j])
                                        j += 1
                                i = j
                        else:
                                all_lines.append(lines[i])
                                i += 1        
                else:                             
                        all_lines.append(lines[i])
                        i += 1
        f.close()
        newfile = filename.split(".")[0] + "_with_branches" + ".py"
        fw = open(newfile, "w")
        fw.writelines(all_lines)
        fw.close()
        return newfile                                                     

def write_main_func_file(filename, all_variables):
        func_var = []
        all_lines = []
        i = -1
        f = open(filename, "r")
        lines = f.readlines()
        for line in lines:
                if ("input" in line or "sys.argv" in line):
                        lhs = line.split("=")
                        all_lines.append("\t" + "#" + line)
                        for var in all_variables:
                               if(var in lhs[0]): 
                                        func_var.append(var)
                elif(line.startswith("import") or line.startswith("from")):
                        all_lines.append(line)
                        i = lines.index(line)
                else:
                        all_lines.append("\t" + line) 
                            
        if i == -1:                                
                all_lines.insert(0, "def added_main(" + ",".join(func_var) + "):\n")
        else:        
                all_lines.insert(i + 1, "def added_main(" + ",".join(func_var) + "):\n")
        f.close()  
        newfile = filename.split(".")[0] + "_added_main" + ".py"
        fw = open(newfile, "w")
        fw.writelines(all_lines)
        fw.close()
        return newfile
                                                
       
def write_new_file(filename):     
        with open(filename, "r") as source:
                root = ast.parse(source.read())
                all_variables = list(get_variables(root))
                newfile = write_main_func_file(filename, all_variables)
                return newfile
                
        


