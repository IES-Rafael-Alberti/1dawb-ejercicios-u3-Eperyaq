"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
from ejercicio_2_3_4 import clean_terminal
def preguntarPalabra():
    try:
        
        palabra = input("Dime una palabra y te dire si es palíndromo o no: ")
#problemita en esta linea no se como hacer para que si es un numero salte un valueError
        if palabra == int:
            raise ValueError
        
    except ValueError:
        print("ERROR")
    return palabra


def mirarPalindromo(palabra):
    
    if palabra == palabra[::-1]:
        print("Es palindromo")
    else:
        print("No es palindromo")
        
    return palabra





def main():
    clean_terminal()
    
    palabra = preguntarPalabra()
    
    mirarPalindromo(palabra)
    



if __name__ == "__main__":
    main()
#bien