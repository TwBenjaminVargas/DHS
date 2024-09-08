
#Devuelve una lista con los datos de la linea
def processLine(linestr):
    data = [linestr[:8]]
    data.append(linestr[8:14].split())
    data.append(linestr[14:20].split())
    data.append(linestr[20:].strip())
    return data

file = open ("registro_temperatura365d_smn.txt", "r")
registros = file.readlines()
file.close()

diccionario = dict()
i=0
for l in registros:
    if i > 2:
        data = processLine(l)
        if data[-1] in diccionario.keys(): # si la clave esta en el diccionario
            diccionario[data[-1]]["tmax"].append(data[1])
            diccionario[data[-1]]["tmin"].append(data[2])  
        else: #clave no esta en el diccionario
            temp = {"tmax":[data[1]],
                        "tmin":[data[2]]}
            item = {data[-1]: temp}
            diccionario.update(item)
    i+= 1
    
try:
    print(diccionario["AEROPARQUE AERO"]["tmax"][0])
except KeyError:
    print("clave ingresada es invalida")