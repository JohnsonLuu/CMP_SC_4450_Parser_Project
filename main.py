import sys

from antlr4 import *
from antlr4.tree.Trees import Trees
from pythonparserLexer import pythonparserLexer
from pythonparserParser import pythonparserParser

def main(argv):
    io_stream = FileStream(argv[1])
    lexer = pythonparserLexer(io_stream)
    stream = CommonTokenStream(lexer)
    parser = pythonparserParser(stream)
    tree = parser.start() 
    print(Trees.toStringTree(tree, None, parser))

    

    
if __name__ == "__main__":
    main(sys.argv)