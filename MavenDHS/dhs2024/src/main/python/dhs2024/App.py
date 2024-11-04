"""
    Trabajo practico nro 1
    - Badami Celeste Antonella
    - Vargas Benjamin
    
    Nuestro repositorio: https://github.com/TwBenjaminVargas/DHS
    En la carpeta MavenDHS/dhs2024
"""

import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha # de esta forma se trae especificamente la clase
from Walker import Walker
def main(argv):
    archivo = "input/entrada.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    #print(tree.toStringTree(recog=parser))
    #caminante = Walker()
    #caminante.visitPrograma(tree)

if __name__ == '__main__':
    main(sys.argv)