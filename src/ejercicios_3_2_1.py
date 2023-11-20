"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
import os 

def clean_terminal():
    if os.name == "nt":
        os.system("cls")




def definir_diccionario():
    dicionario = {"Euro":"€", "Dollar":"$", "Yen":"¥"}

    return dicionario


def preguntar_diccionario(d):
    try:
        divisa = input("Dime una divisa -> ").capitalize()
        if divisa in d:
            print (d[divisa])
        else: 
            raise KeyError
        
    except KeyError:
        print("ERROR, esa divisa no se encuentra en el diccionario")





def main():
    clean_terminal()

    d = definir_diccionario()

    preguntar_diccionario(d)



if __name__ == "__main__":
    main()