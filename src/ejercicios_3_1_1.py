"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
from ejercicio_2_3_4 import clean_terminal

def pedirAsignaturas():
    """Asks for the name of the subject.
    
    Args:
        asignaturas(str): an input to save the name of the subject
        
    returns:
        asignaturas(str): 
    
    """

    asignaturas = []
    try:
        while  len(asignaturas) == 0  or asignatura != "" :
            asignatura  = input("Dime que asignatura quieres meter y si no quieres meter nada introduce un espacio vacio: ")
            
            if asignatura != "":
                asignaturas.append(asignatura) 
            
            
    except ValueError:
        print("Un numero en el nombre de las asignaturas??")
    except Exception:
        print("Ya la liaste")
    return asignaturas


def conclusion(asignaturas):
    
    for perro in asignaturas:
        print(f"Mis asignaturas finales son: {perro}")
        
    return perro


def main():

    clean_terminal()

    asignaturas = pedirAsignaturas()
    
    conclusion(asignaturas)
    
    


if __name__ == "__main__":
    main()
#Como puedo hacer para, si asignaturas == a un numero raise ValueError