"""
    Final Desarrollo de herramientas de Software
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
from OptCode import OptCode
from ErrorEscucha import ErrorEscucha

def main(argv):
    archivo = "input/entrada.txt"
    salida = "src/main/python/dhs2024/out/cod.txt"
    optroute = "src/main/python/dhs2024/out/optcod1.txt"
    pasadas = 8
    
    if len(argv) > 1 :
        archivo = argv[1]

    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    
    escucha = Escucha()
    parser.addParseListener(escucha)
    
    # Remover el listener de errores por defecto y agregar el personalizado
    error = ErrorEscucha()
    parser.removeErrorListeners()
    parser.addErrorListener(error)
    
    
    tree = parser.programa()
    
    if escucha.isAnyError():
        sys.exit()
        
    #print(tree.toStringTree(recog=parser))
    caminante = Walker(salida)
    caminante.visitPrograma(tree)
    caminante.finish()
    
    optimizador = OptCode()
    for i in range(pasadas):
        optimizador.optimizar(salida,optroute)
        salida = optroute
        
if __name__ == '__main__':
    main(sys.argv)