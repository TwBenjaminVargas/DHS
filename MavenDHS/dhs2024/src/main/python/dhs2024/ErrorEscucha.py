from antlr4.error.ErrorListener import ErrorListener
import sys

class ErrorEscucha (ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        err = "- " + f"\033[31mError de sintaxis en línea {line}, columna {column} \033[0m"
        if "missing ';'" in msg:
            err += "\033[31m: Se esperaba ';'\033[0m"
        print(err)
        sys.exit() 
