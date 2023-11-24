"""
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.

Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes. BIEN

Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.

Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""
from ejercicios_3_2_1 import clean_terminal

def nuevo_conjunto(set_frutas1: set, set_frutas2: set):
    
    frutas_comunes = set_frutas1 | set_frutas2

    return frutas_comunes

def frutas_solo_en_una(set_frutas1: set, set_frutas2: set):

    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2

    return frutas_solo_en_frutas1

def frutas_solo_en_dos(set_frutas1: set, set_frutas2: set):

    frutas_solo_en_frutas1 = set_frutas2 - set_frutas1

    return frutas_solo_en_frutas1



def main():

    clean_terminal()

    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    set_frutas1 = set(frutas1)
    
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"] 
    set_frutas2 =  set(frutas2)
    
    print(nuevo_conjunto(set_frutas1,  set_frutas2))

    print(frutas_solo_en_una(set_frutas1,  set_frutas2))

    print(frutas_solo_en_dos(set_frutas1,  set_frutas2))


if __name__ == "__main__":
    main() 