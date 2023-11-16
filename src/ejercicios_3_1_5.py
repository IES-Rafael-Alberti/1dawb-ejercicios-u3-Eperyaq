"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
from ejercicio_2_3_4 import  clean_terminal


def lista():
    numeros = tuple(i for i in range(1, 11))
    return numeros


def mostrarLista(lista_num: list, separador: str = ", "):
    lista_num.append(11)
    for i in range(-1, - len(lista_num) -1, -1):
        if i != -len(lista_num):
            print(lista_num[i], end=separador )
        else:
            print(lista_num[i])




def main():

    clean_terminal()
    numeros =  lista()
    #lista_num = list(numeros)

    #lista_num.reverse()
    mostrarLista(numeros)


    

   # print(lista()[::-1])


if __name__ == "__main__":
    main()

    """
    def mostrarLista(lista_num: list, separador: str = ", "):
    for i in range(len(lista_num)):
        if i != len(lista_num) -1:
            print(lista_num[i], end=separador )
        else:
            print(lista_num[i])
    """
    """
    def mostrarLista(lista_num: tuple, separador: str = ", "):
    for i in range(len(lista_num) -1, -1, -1):
        if i != 0:
            print(lista_num[i], end=separador )
        else:
            print(lista_num[i])
    """