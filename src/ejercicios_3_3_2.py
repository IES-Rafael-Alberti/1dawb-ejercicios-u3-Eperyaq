"""
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""
#interseccion de conjunto para los nombres que se repiten
#conjunto A y B los que estan en A que no estan en B
from ejercicios_3_2_1 import clean_terminal

def pedir_alumnos():
    salir = False
    alumnos_primaria = ""

    

    while not salir:
        if alumnos_primaria != "x" :
            alumnos_primaria = input("Dime el nombre de pila de los alumnnos de primaria ('x' para salir): ").lower()
            
        else:
            salir = True
    nombres_alumnos = set(list(alumnos_primaria))

    print(nombres_alumnos)

    return nombres_alumnos






def main():
    clean_terminal()

    nombres_alumnos = pedir_alumnos()
    print(nombres_alumnos)


if __name__ == "__main__":
    main()