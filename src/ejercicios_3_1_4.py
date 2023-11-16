"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
from ejercicio_2_3_4 import clean_terminal

def usuariosLoteria():
    while  numeros != "":
        numeros =  int(input("Dime los numeros de la lotería, cuando hayas terminado pulsa enter:"))

    return numeros

def crearLista(numeros): 

    lista = []
    lista.append(numeros)
    return lista

def main():

    clean_terminal()
    numero = usuariosLoteria()
    crearLista(numero)


if __name__ == "__main__":
    main()