"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""
from ejercicio_2_3_4 import clean_terminal


def nombreAsignaturas():
    """a list with the name of the subjects
    
    Args:
        asignaturas(list): list with subjects names
        
    Returns:
        list = list with subjects names
    
    """
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Hisotria", "Lengua"]
    
    return asignaturas


def llamarAsignaturas(asignaturas):
    """Str who calls the list and make a custom sentence
    
    Args:
        asignatura(str): each subjetc of the list asignaturas
        asignaturas(list): a list with the name of some subjects
    
    Returns:
        asignatura(str): a print with a especific sentence for each of the subjects
    
    """
    
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")
        
    return asignatura
    
    
    
    
    
def main():

    clean_terminal()

    asignaturas = nombreAsignaturas()
    llamarAsignaturas(asignaturas)

if __name__ == "__main__":
    main()
    
#perfe a la primera