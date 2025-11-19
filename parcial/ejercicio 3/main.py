from antlr4 import *
from matrizLexer import matrizLexer
from matrizParser import matrizParser
from matrizVisitor import matrizVisitor
from matriz import matriz

import sys

if __name__=='__main__':
    input_stream=FileStream('matrices.txt')

    lexer=matrizLexer(input_stream)
    tokens=CommonTokenStream(lexer)
    parser=matrizParser(tokens)

    tree=parser.programa()

    visitor=matrizVisitor()
    codigo=visitor.visit(tree)

    print("codigo generado:\n")
    print(codigo)
    print("\nsalida del programa:\n")
    exec(codigo)

