"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
from ejercicio_2_3_4 import clean_terminal
from ejercicios_3_1_2 import nombreAsignaturas

def preguntarNota(asignaturas):
    """Ask for the note that the user have in each subject
    
    Args:
        nota(str): a sentence that ask for the note
        notas(list): List that isnt working either :D
    
    """
    notas = []

    for asignatura in asignaturas:
        try:
            nota = int(input(f"Que nota has sacado en {asignatura}?: "))
            notas.append(nota)
            
            if nota<0 or nota>10:
                raise Exception(print("ERROR, solo numeros correctos."))
            
        except ValueError:
            print("ERROR")
        except Exception as e:
            print(e)
        
        
        
    
    return notas


def resolucionNotas(nota: list, asignaturas: str):
    """Do a sentence for the notes and the subject of the user
    
    Args:
        nombre(str): the user name
        asignatura(str): each subject
        asignaturas(list): list with the name of the subjects    
    """
    
    nombre = input("Dime tu nombre: ")
    
    try:
        for i in range(0, len(asignaturas)):
            
            print(f"{nombre} en {asignaturas[i]} ha sacado un {nota[i]}")
    except IndexError:
        print("La has liado, por eso no te sale la lista completa")

        
    return asignaturas
        


def main():

    clean_terminal()
    asignaturas = nombreAsignaturas()
    notas = preguntarNota(asignaturas)
    clean_terminal()
    resolucionNotas(notas, asignaturas)


if __name__ == "__main__":
    main()
#me salta el error pero aun así guarda el valor

"""
pos = 0
    for asignatura in asignaturas:
        
        print(f"{nombre} en {asignatura} ha sacado un {nota[pos]}")
        pos += 1

"""