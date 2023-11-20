"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
from ejercicios_3_1_1 import clean_terminal

def usuariosLoteria():
    numeros = []
    
    while  numeros != "":
        numeros =  int(input("Dime los numeros de la lotería, cuando hayas terminado pulsa enter:"))
        numeros.append()

    print(numeros)




def main():

    clean_terminal()
    usuariosLoteria()


if __name__ == "__main__":
    main()