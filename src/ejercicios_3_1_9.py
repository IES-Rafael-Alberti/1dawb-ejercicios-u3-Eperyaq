"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
from ejercicio_2_3_4 import clean_terminal

def listaPalabra():
    
    palabra = input("Dime una palabra: ")

    return palabra

def buclePalabra(palabra: str):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letra in palabra:
        if letra in palabra == "a":
            a += 1
        elif letra in palabra == "e":
            e += 1
        elif letra in palabra == "i":
            i += 1
        elif letra in palabra == "o":
            o += 1
        elif letra in palabra == "u":
            u += 1
    
    print(f"El numero de veces que la letra a ha salido han sido {a} veces")
    print(f"El numero de veces que la letra e ha salido han sido {e} veces")
    print(f"El numero de veces que la letra i ha salido han sido {i} veces")
    print(f"El numero de veces que la letra o ha salido han sido {o} veces")
    print(f"El numero de veces que la letra u ha salido han sido {u} veces")
    
    
    return palabra
    
    
def main():
    clean_terminal()
    
    palabra = listaPalabra()
    
    buclePalabra(palabra)



if __name__ == "__main__":
    main()
#falla la condicion
