"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
from ejercicios_3_2_1 import clean_terminal

def pedir_datos():

    todo_ok = False
    while not todo_ok:
        try:
            opcion = input("desea añadir dato? s/n").lower()

            if opcion not in {"s"/"n"}:

                raise ValueError
            
        except Exception:
            print("ERROR")

#hacer funcion que reciba los input pregunte el dato ya que han puesto que si y los meta en el diccionario
    
    

def main():
    clean_terminal()

    datos_cliente = {}

    pedir_datos(datos_cliente)
    print(datos_cliente)

    

if __name__ == "__main__":
    main() 