"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello
"""""
from ejercicios_3_2_1 import clean_terminal


def precio_fruta()-> dict:
    
    precio = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70 }
    
    return precio

def preguntar_fruta(precio: dict):
    print("Frutas disponibles:", list(precio.keys()))
    fruta = input("Que fruta de la lista quieres?: ").capitalize()
    
    return fruta

def preguntar_kilos(fruta:str):
    
    kilos = float(input(f"cuantos kilos de {fruta} quieres?: "))
    
    return kilos

def precio_final(fruta: str, precio : dict,  kilos: float):
    
    if fruta in precio:
        precio_unitario =  precio[fruta]
        precio_total = kilos * precio_unitario
        print(f"El precio final va a ser {precio_total}")
    else:
        print("Lo siento esa fruta no esta dentro de la lista")
    
    

def main():
    
    clean_terminal()
    precio = precio_fruta()
    fruta = preguntar_fruta(precio)
    kilos = preguntar_kilos(fruta)
    precio_final(fruta, precio, kilos)
    
    

if __name__ == "__main__":
    main()
#El orden de precio_final tiene que ser ese si o si, sino, da error tenia puesto fruta, kilos, precio y daba type error