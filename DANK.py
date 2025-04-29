import sys
import os
from antlr4 import *
from modules.DANKLexer import DANKLexer
from modules.DANKParser import DANKParser
from modules.DANKVisitor import DANKVisitor
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

TEST_DIR = "./test_files"
class ThrowingErrorListener(ErrorListener):
    INSTANCE = None

    def __init__(self):
        super(ThrowingErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException(f"line {line}:{column} {msg}")

ThrowingErrorListener.INSTANCE = ThrowingErrorListener()

def main(code, print_debug):
    input_stream = InputStream(code)
    lexer = DANKLexer(input_stream)
    
    token_stream = CommonTokenStream(lexer) 
    
    parser = DANKParser(token_stream) 
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener.INSTANCE)
    
    
    tree = parser.program() 
    if print_debug:
        print(tree.toStringTree(recog=parser)) 
    
    visitor = DANKVisitor(parser)
    visitor.visit(tree)

def test(filename):
    f = open(filename)
    codes=f.read().split("\n\n")
    f.close()
    validity = [0, 0]
    for _,code in enumerate(codes):
        try:
            print(code+"\n")
            
            main(code,False)
            validity[0] += 1
        except Exception as e:
            print("Exception:",e)
            
        finally:
            print("\n-------------------------------------------------------------------------------------\n")
            validity[1] += 1
    print("valid: " + str(validity[0]) + "/" + str(validity[1]))

def quick_check():
    try:
        code = input("Enter your code: ")
        print(code)
        main(code,True) 
    except Exception as e:
        print("Exception:",e)

def print_help():
    help = """
python .\\DANK.py (--help|-h)
    Prints this help
    
MODES OF TESTING
python .\\DANK.py
    debug/interactive mode - Takes code to be validated as input. Prints parser tree.

python .\\DANK.py (--test|-t)
    Takes and tests all the files in [test_files](/test_files/) directory. 
    Prints tested codes, outputs and number of tests, that did not result in error.

python .\\DANK.py (--test|-t) filename
    Tests the code in the given file. 
    Prints tested codes, outputs and number of tests, that did not result in error.
    """
    print(help)

if __name__ == "__main__":
    args = sys.argv
    if len(args)>1 and (args[1] == "--test" or args[1] == "-t"):
        if len(args)>2:
            test(args[2])
        else:
            files = os.listdir(TEST_DIR)
            for file in files:
                test(TEST_DIR+"/"+file)
    elif len(args)>1 and (args[1] == "--help" or args[1] == "-h"):
        print_help()
    else:
        quick_check()