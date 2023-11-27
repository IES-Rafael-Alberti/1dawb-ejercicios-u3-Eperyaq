"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""
from ejercicios_3_2_1 import clean_terminal

def crear_diccionario()-> dict:
    
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    
    return asignaturas

def sumar_datos(asignaturas: dict):
    
    #suma_asignaturas = asignaturas.values + asignaturas.values
    
    asignaturas.items()
    
    print(f"{"key"} tiene {"value"} y en total tienes  ")





def main():
    
    clean_terminal()
    
    asignaturas = crear_diccionario()
    sumar_datos(asignaturas)
    
    
    

if __name__ == "__main__":
    main()
#no se como va eso del key y el value