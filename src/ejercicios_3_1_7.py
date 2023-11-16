"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
from ejercicio_2_3_4 import clean_terminal

def definirLista():
    abecedario = list("abcdefghijklmnñopqrstuvwxyz")
    
    return abecedario


def calculoLista(abecedario: list):
    cont = 0
    max = len(abecedario) - 1
    while cont <= max:
        if cont % 3 == 0:
            abecedario.pop(cont)
            max -= 1
        cont += 1
             
    return abecedario




def main():
    clean_terminal()
    
    abecedario = definirLista()
    print(calculoLista(abecedario))



if __name__ == "__main__":
    main()
#me falla la letra ya tengo las posiciones metida en la lista pero no se como hacer para meter las letra