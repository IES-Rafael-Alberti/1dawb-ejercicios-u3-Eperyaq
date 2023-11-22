"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""
from ejercicios_3_2_1 import clean_terminal

def crear_diccionario()-> dict:
    lista_compra = {}
    todo_ok = False
    while not todo_ok:
        nombre = input("Añada el nombre del objeto a la cesta(presione x para salir) -> ")
        if nombre == "x":
            todo_ok= True
        else:
            precio = float(input(f"Introduzca el precio de {nombre}: "))
            lista_compra[nombre] = precio
#se guarda la x que es el valor de salida tambien     
    return lista_compra
        
def sumar_precios(lista_compra: dict):
    
    precio_total = sum(lista_compra.values())
    print(f"La lista de la compra lleva {lista_compra} y su precio total es {precio_total}")
    return precio_total
            
            
    
    





def main():
    clean_terminal()
    lista = crear_diccionario()
    sumar_precios(lista)

    

    

if __name__ == "__main__":
    main() 