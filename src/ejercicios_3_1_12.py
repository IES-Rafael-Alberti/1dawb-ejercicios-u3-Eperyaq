"""
Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""
from ejercicios_3_1_1 import clean_terminal
def main():
    

    m1 = ((1,2), (3,4), (5,6))
    m2 =((-1,0), (0,4), (5,6))
    m3 = []


    for fila in range (3):
        m3.append(list())
        for columna in range(2):
            m3[fila].append(
                m1[fila][columna] *
                m2[fila][columna]
                )
            
    print(m3)

if __name__ == "__main__":
    main()