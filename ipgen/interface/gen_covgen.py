from covgen.run.inputgenerator import InputGenerator
import py_parse
import sys

generator = InputGenerator(sys.argv[1])

try:
        inputs = generator.generate_all_inputs()
        no_branch_func = [func for func in inputs if(len(inputs[func])==0)]
        if(len(no_branch_func)== 0):
                ip_file = open("concatOut.txt", "w")
                for func in inputs:
                        for cases in inputs[func]:
                                if(inputs[func][cases] != None):
                                        ip_file.write(str(" ".join(list(map(str, inputs[func][cases])))) + "\n")
                ip_file.close()         
        #fix for files where no branches are detected
        else:                       
                newfile = py_parse.write_new_file_branch(sys.argv[1], no_branch_func)
                generator = InputGenerator(newfile)
                inputs = generator.generate_all_inputs()
                print(inputs)
                ip_file = open("concatOut.txt", "w")
                for func in inputs:
                        for cases in inputs[func]:
                                if(inputs[func][cases] != None):
                                        ip_file.write(str(" ".join(list(map(str, inputs[func][cases])))) + "\n")
                ip_file.close()                       
#when the program is written without any function or __main__:
except:
        newfile = py_parse.write_new_file(sys.argv[1])        
        generator = InputGenerator(newfile)
        inputs = generator.generate_all_inputs()
        no_branch_func = [func for func in inputs if(len(inputs[func])==0)]
        if(len(no_branch_func)== 0):
                ip_file = open("concatOut.txt", "w")
                for func in inputs:
                        for cases in inputs[func]:
                                if(inputs[func][cases] != None):
                                        ip_file.write(str(" ".join(list(map(str, inputs[func][cases])))) + "\n")
                ip_file.close() 
        #fix for files where no branches are detected                        
        else: 
                newfile = py_parse.write_new_file_branch(newfile, no_branch_func)
                generator = InputGenerator(newfile)
                inputs = generator.generate_all_inputs()
                ip_file = open("concatOut.txt", "w")
                for func in inputs:
                        for cases in inputs[func]:
                                if(inputs[func][cases] != None):
                                        ip_file.write(str(" ".join(list(map(str, inputs[func][cases])))) + "\n")
                ip_file.close()                    
                
               
                       
"""
Run this file using: python3 covgen_py_ip.py p1.py
p1.py is the file for which inputs are to be generated
p1_added_main.py will be created if p1.py has no function definitions
p1_with_branches.py will be created if no branches were detected by covgen
p1_added_main_with_branches.py will be created along with py.added_main.py if both 
no function definitions were presented or no branches were detected by covgen
ip_gen.txt will be generated that will contain the inputs for the latest created .py file
"""
