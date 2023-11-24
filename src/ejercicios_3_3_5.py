"""
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.

Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.

Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""
from ejercicios_3_2_1 import clean_terminal

def conjunto_extraccion(numeros: set, divisor: int = 2)-> set:

    conjunto_nuevo = {}

    for numero in numeros:
        if numero % divisor == 0:
            conjunto_nuevo.add(numeros)
   
    return conjunto_nuevo





def main():

    clean_terminal()

    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(f"Múltiplos de 2 => {conjunto_extraccion(numeros)}")
    print(f"Múltiplos de 3 => {conjunto_extraccion(numeros, 3)}")

if __name__ == "__main__":
    main() 