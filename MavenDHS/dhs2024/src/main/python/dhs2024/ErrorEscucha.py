from antlr4.error.ErrorListener import ErrorListener
import sys

class ErrorEscucha (ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        pass  # No hace nada, evita que se impriman errores en consola
    
    

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("- " + f"\033[31mError de sintaxis en línea {line}, columna {column}\033[0m")
        sys.exit() 
