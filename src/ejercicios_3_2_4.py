"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
from ejercicios_3_2_1 import clean_terminal

def preguntar_fecha()-> dict:
    diccionario_fecha = {}
    fecha_junta = input("Añade una fecha formato (dd/mm/aaaa)")
    fecha_separada = fecha_junta.split("/")

    diccionario_fecha["Dia"] = fecha_separada[0]
    diccionario_fecha["Mes"] = fecha_separada[1]
    diccionario_fecha["Año"] = fecha_separada[2]
        
    if diccionario_fecha["Dia"] > 30:
        raise ValueError("ERROR introduce un dia real.")
    elif diccionario_fecha["Mes"] > 12:
        raise ValueError("ERROR introduce un mes real.")
    elif diccionario_fecha["Año"] > 2023 or diccionario_fecha["Año"] < 1900:
        raise ValueError("ERROR introduce un dia real.")
    return diccionario_fecha


def main():
    
    clean_terminal()
    print(preguntar_fecha())
    
    
    

if __name__ == "__main__":
    main()
#me rallé