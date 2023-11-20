"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
from ejercicios_3_2_1 import clean_terminal




def rellenar_diccionario():
    d = {}
    
    nombre = input("introduce tu nombre: ")
    d["nombre"] = nombre
    
    edad = int(input("Ahora introduce tu edad: "))
    d["edad"] = edad
    
    direccion = input("Introduce tu direccion: ")
    d["direccion"] = direccion
    
    telefono = input("Por ultimo introduce tu numero de telefono: ")
    d["telefono"] = telefono
    #meter excepciones.
    return d 

def terminar_ejercicio(d):
    
    print(f"{d["nombre"]} tiene {d["edad"]} años, vive en {d["direccion"]} y su numero de telefono es {d["telefono"]}")
    
    
def main():
    clean_terminal()

    d = rellenar_diccionario()
    terminar_ejercicio(d)
    

if __name__ == "__main__":
    main()  