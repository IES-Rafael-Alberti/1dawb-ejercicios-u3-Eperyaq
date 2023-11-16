"""
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""
from ejercicio_2_3_4 import clean_terminal

def tuplaPrecios ():
    
    precios = [50, 75, 46, 22, 80, 65, 8]
    
    precios.sort()
    
    return precios

#precios.sort() solo funciona con listas, si usas una tupla tienes que usar: precio_ordenado = sorted(precios)




def main():
    clean_terminal()
    
    print(tuplaPrecios())
    

if __name__ == "__main__":
    main()