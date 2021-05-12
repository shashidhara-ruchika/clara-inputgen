import re

def remove_directives(text):
    '''
    Preprocess a given source code file to remove all preprocessor directives
    '''
    newtext = ''
    includes = []
    defines = []
    for x in text.split('\n'):
        if x.startswith('#include'):
            includes.append(x.strip())
        elif x.startswith('#define'):
            defines.append(x.strip())
        else:
            newtext+= x+'\n'
    return newtext, includes, defines
    
def remove_comments(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return ""
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def reconstruct_source(code, includes, defines):
    '''
    From the CREST-compatible source code, and a list of all preprocessor directives
    reconstruct the full CREST-compatible source code
    '''
    source = ''
    for i in includes:
        source += i+'\n'
    for d in defines:
        source += d+'\n'
    source += code
    return "#include<crest.h>\n"+source 