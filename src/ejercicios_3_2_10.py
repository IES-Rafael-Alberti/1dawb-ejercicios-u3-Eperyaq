"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 

Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente.

El programa debe preguntar al usuario por una opción del siguiente menú: 

(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""

from ejercicios_3_2_1 import clean_terminal
    
    
def añadir_clientes():
    nombre = input("Introduce tu nombre-> ")
    nif = input("Introduce tu nif-> ")
    direccion = input("Introduce tu direccion-> ")
    telefono = input("Introduce tu telefono-> ")
    correo = input("Introduce tu correo-> ")
    preferente = input("Eres cliente preferente?  ")
    nombre = input("Introduce tu nombre-> ")
    nombre = input("Introduce tu nombre-> ")

def eliminar_clientes():
    print()
def mostrar_cliente():
    print()
def listar_clientes():
    print()
def clientes_preferentes():
    print()
def terminar_programa():
    print()




def main():
    clean_terminal()
    diccionario = {}
    todo_ok= False
    
    while not todo_ok:
        try:
            gestion = int(input("Bienvenido, que gestion desea realizar? \n (1) Añadir cliente \n (2) Eliminar cliente \n (3) Mostrar cliente \n (4) Listar todos los clientes \n (5) Listar clientes preferentes \n (6) Terminar. \n ->"))
            if gestion >6:
                raise ValueError
            else: 
                todo_ok = True
        except ValueError:
            print("ERROR escribe un numero correcto \n ")
        
    if gestion == 1:
        añadir_clientes()
    elif gestion == 2:
        eliminar_clientes()
    elif gestion == 3:
        mostrar_cliente()
    elif gestion == 4:
        listar_clientes()
    elif gestion == 5:
        clientes_preferentes()
    else:
        terminar_programa()
        

    

    

if __name__ == "__main__":
    main() 
