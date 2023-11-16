"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
from ejercicios_3_1_2 import nombreAsignaturas
from ejercicio_2_3_4 import clean_terminal
from ejercicios_3_1_3 import preguntarNota

def controlarAsignaturas(asignatura, notas):
    for perro in asignatura:
        if perro < 5:
            print(f"has sacado un {notas}.")
    return perro





def main():

    clean_terminal()
    asignatura = nombreAsignaturas()
    notas = print(preguntarNota(asignatura))
    controlarAsignaturas(asignatura ,notas)


if __name__ == "__main__":
    main()
#me falla la condicion