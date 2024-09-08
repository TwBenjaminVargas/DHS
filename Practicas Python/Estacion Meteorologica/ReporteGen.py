#Error en captacion de keys, ya que al utilizar el metodo split no se conto con la 
#utilizacion de nombres separados por espacio, por lo que la key sera el ultimo elemento de la lista
#que se obtiene al usar split() en la linea del archivo, y hay varios que repiten AERO en sus nombres
#Ademas el codigo ignora datos incompletos, por lo que si pones [3] no seran 3 dias antes si no 
# 3 dias sin errores antes, funciona pero se puede mejorar :)
file = open ("registro_temperatura365d_smn.txt", "r")
registros = file.readlines()
file.close()

diccionario = dict()
i=0
for l in registros:
    data = l.split()
    if not len(data) < 4 and i > 2: #ignora primeras lineas y toda aquella que no este completa
        if data[-1] in diccionario.keys(): # si la clave esta en el diccionario
            diccionario[data[-1]]["tmax"].append(data[1])
            diccionario[data[-1]]["tmin"].append(data[2])
            
        else: #clave no esta en el diccionario
            temp = {"tmax":[data[1]],
                    "tmin":[data[2]]}
            item = {data[-1]: temp}
            diccionario.update(item)
    i+=1

try:
    print(diccionario["ESPERANZA"]["tmax"][0])
except KeyError:
    print("clave ingresada es invalida")