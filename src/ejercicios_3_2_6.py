"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
from ejercicios_3_2_1 import clean_terminal

def pedir_datos():

    todo_ok = False
    while not todo_ok:
        try:
            opcion = input("desea añadir dato? s/n: ").lower()

            if opcion not in {"s","n"}:

                raise ValueError
            else: 
                todo_ok = True
        except Exception:
            print("ERROR")

#hacer funcion que reciba los input pregunte el dato ya que han puesto que si y los meta en el diccionario

def añadir_dato():
    diccionario_datos = {}
    todo_ok = False
    while not todo_ok:
        if pedir_datos() == "s":
            dato = input("Añada el nombre del dato-> ")
            diccionario_datos[dato] = input("Introduce el dato: ")
        else:
            todo_ok = True
            
def mostrar_diccionario(diccionario_datos: dict):
    
    guardado = print("El diccionario tiene: ")
    for clave, dato in diccionario_datos.items():
        guardado += clave + "-" + dato
    print (guardado)
    
    
    

def main():
    clean_terminal()

    pedir_datos()
    diccionario = añadir_dato()
    mostrar_diccionario(diccionario)
    

    

if __name__ == "__main__":
    main() 